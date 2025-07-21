import asyncio
from dataclasses import dataclass
from datetime import date
from dotenv import load_dotenv, find_dotenv
from pydantic_ai import Agent
from pydantic_ai.messages import (
    FinalResultEvent,
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    PartStartEvent,
    TextPartDelta,
    ToolCallPartDelta,
)
from pydantic_ai.tools import RunContext


load_dotenv(find_dotenv())

@dataclass
class WeatherService:
    async def get_forecast(self, location: str, forecast_date: date) -> str:
        # In real code: call weather API, DB queries, etc.
        return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'

    async def get_historic_weather(self, location: str, forecast_date: date) -> str:
        # In real code: call a historical weather API or DB
        return (
            f'The weather in {location} on {forecast_date} was 18°C and partly cloudy.'
        )


weather_agent = Agent[WeatherService, str](
    'openai:gpt-4o',
    deps_type=WeatherService,
    output_type=str,  # We'll produce a final answer as plain text
    system_prompt='Providing a weather forecast at the locations the user provides.',
)


@weather_agent.tool
async def weather_forecast(
    ctx: RunContext[WeatherService],
    location: str,
    forecast_date: date,
) -> str:
    if forecast_date >= date.today():
        return await ctx.deps.get_forecast(location, forecast_date)
    else:
        return await ctx.deps.get_historic_weather(location, forecast_date)


output_messages: list[str] = []


async def main():
    user_prompt = 'What will the weather be like in Paris on Tuesday?'

    # Begin a node-by-node, streaming iteration
    async with weather_agent.iter(user_prompt, deps=WeatherService()) as run:
        async for node in run:
            if Agent.is_user_prompt_node(node):
                # A user prompt node => The user has provided input
                output_messages.append(f'=== UserPromptNode: {node.user_prompt} ===')
            elif Agent.is_model_request_node(node):
                # A model request node => We can stream tokens from the model's request
                output_messages.append(
                    '=== ModelRequestNode: streaming partial request tokens ==='
                )
                async with node.stream(run.ctx) as request_stream:
                    async for event in request_stream:
                        if isinstance(event, PartStartEvent):
                            output_messages.append(
                                f'[Request] Starting part {event.index}: {event.part!r}'
                            )
                        elif isinstance(event, PartDeltaEvent):
                            if isinstance(event.delta, TextPartDelta):
                                output_messages.append(
                                    f'[Request] Part {event.index} text delta: {event.delta.content_delta!r}'
                                )
                            elif isinstance(event.delta, ToolCallPartDelta):
                                output_messages.append(
                                    f'[Request] Part {event.index} args_delta={event.delta.args_delta}'
                                )
                        elif isinstance(event, FinalResultEvent):
                            output_messages.append(
                                f'[Result] The model produced a final output (tool_name={event.tool_name})'
                            )
            elif Agent.is_call_tools_node(node):
                # A handle-response node => The model returned some data, potentially calls a tool
                output_messages.append(
                    '=== CallToolsNode: streaming partial response & tool usage ==='
                )
                async with node.stream(run.ctx) as handle_stream:
                    async for event in handle_stream:
                        if isinstance(event, FunctionToolCallEvent):
                            output_messages.append(
                                f'[Tools] The LLM calls tool={event.part.tool_name!r} with args={event.part.args} (tool_call_id={event.part.tool_call_id!r})'
                            )
                        elif isinstance(event, FunctionToolResultEvent):
                            output_messages.append(
                                f'[Tools] Tool call {event.tool_call_id!r} returned => {event.result.content}'
                            )
            elif Agent.is_end_node(node):
                assert run.result.output == node.data.output
                # Once an End node is reached, the agent run is complete
                output_messages.append(
                    f'=== Final Agent Output: {run.result.output} ==='
                )


if __name__ == '__main__':
    asyncio.run(main())

    print(output_messages)
    """
    [
        '=== UserPromptNode: What will the weather be like in Paris on Tuesday? ===', 
        '=== ModelRequestNode: streaming partial request tokens ===', 
        "[Request] Starting part 0: ToolCallPart(
            tool_name='weather_forecast', 
            args='', 
            tool_call_id='call_AWjruCrgi3gaOE4JH6X0E37M'
        )", 
        '[Request] Part 0 args_delta={"', '[Request] Part 0 args_delta=location', '[Request] Part 0 args_delta=":"', '[Request] Part 0 args_delta=Paris', '[Request] Part 0 args_delta=","', '[Request] Part 0 args_delta=forecast', '[Request] Part 0 args_delta=_date', '[Request] Part 0 args_delta=":"', '[Request] Part 0 args_delta=202', '[Request] Part 0 args_delta=3', '[Request] Part 0 args_delta=-', '[Request] Part 0 args_delta=11', '[Request] Part 0 args_delta=-', '[Request] Part 0 args_delta=07', '[Request] Part 0 args_delta="}', '=== CallToolsNode: streaming partial response & tool usage ===', '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2023-11-07"} (tool_call_id=\'call_AWjruCrgi3gaOE4JH6X0E37M\')', "[Tools] Tool call 'call_AWjruCrgi3gaOE4JH6X0E37M' returned => The weather in Paris on 2023-11-07 was 18°C and partly cloudy.", '=== ModelRequestNode: streaming partial request tokens ===', "[Request] Starting part 0: TextPart(content='')", '[Result] The model produced a final output (tool_name=None)', "[Request] Part 0 text delta: 'The'", "[Request] Part 0 text delta: ' weather'", "[Request] Part 0 text delta: ' in'", "[Request] Part 0 text delta: ' Paris'", "[Request] Part 0 text delta: ' on'", "[Request] Part 0 text delta: ' Tuesday'", "[Request] Part 0 text delta: ','", "[Request] Part 0 text delta: ' November'", "[Request] Part 0 text delta: ' '", "[Request] Part 0 text delta: '7'", "[Request] Part 0 text delta: 'th'", "[Request] Part 0 text delta: ','", "[Request] Part 0 text delta: ' is'", "[Request] Part 0 text delta: ' expected'", "[Request] Part 0 text delta: ' to'", "[Request] Part 0 text delta: ' be'", "[Request] Part 0 text delta: ' partly'", "[Request] Part 0 text delta: ' cloudy'", "[Request] Part 0 text delta: ' with'", "[Request] Part 0 text delta: ' a'", "[Request] Part 0 text delta: ' temperature'", "[Request] Part 0 text delta: ' of'", "[Request] Part 0 text delta: ' '", "[Request] Part 0 text delta: '18'", "[Request] Part 0 text delta: '°C'", "[Request] Part 0 text delta: '.'", '=== CallToolsNode: streaming partial response & tool usage ===', '=== Final Agent Output: The weather in Paris on Tuesday, November 7th, is expected to be partly cloudy with a temperature of 18°C. ===']
    """