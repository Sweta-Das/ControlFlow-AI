"""Agent Wide Prepare Tools

In addition to per-tool `prepare` methods, we can also define an agent-wide `prepare_tools` method.
- This function is called at each step of a run and allows to filter or modify thel list of all tool definitions available to the agent for that step.
- Useful to enable or disable multiple tools at once, or apply global logic based on the current context.
- It should be of type `ToolsPrepareFunc`, that takes the `RunContext` and a list of `ToolDefinition`, and returns a new list of tool definitions (or None to 
disable all tools).
"""

# agent_prepare_tools_customize.py

from dataclasses import replace
from typing import Union
from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import ToolDefinition
from pydantic_ai.models.test import TestModel


async def turn_on_strict_if_openai(
    ctx: RunContext[None], tool_defs: list[ToolDefinition]
) -> Union[list[ToolDefinition], None]:
    if ctx.model.system == 'openai':
        return [replace(tool_def, strict=True) for tool_def in tool_defs]
    return tool_defs


test_model = TestModel()
agent = Agent(test_model, prepare_tools=turn_on_strict_if_openai)


@agent.tool_plain
def echo(message: str) -> str:
    return message


agent.run_sync('testing...')
# assert test_model.last_model_request_parameters.function_tools[0].strict is None

# Set the system attribute of the test_model to 'openai'
test_model._system = 'openai'

agent.run_sync('testing with openai...')
# assert test_model.last_model_request_parameters.function_tools[0].strict