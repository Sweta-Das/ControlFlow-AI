"""A simple `prepare` method that includes the tool if the dependency value is `63`."""

from typing import Union
from pydantic_ai import Agent, RunContext
from pydantic_ai.tools import ToolDefinition

agent = Agent('test')

async def only_if_63(
    context: RunContext[int],
    tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    
    """Check if context dependeny is 63"""
    if context.deps == 63:
        return tool_def
    

@agent.tool(prepare=only_if_63)
def hitchhiker(context: RunContext[int], answer: str) -> str:
    """Check for dependency and return answer if correct"""
    return f'{context.deps} {answer}'


if __name__ == "__main__":
    result1 = agent.run_sync('testing...', deps=42)
    print(result1.output) # success (no tool calls)
    
    result2 = agent.run_sync('testing...', deps=63)
    print(result2.output) # {"hitchhiker":"63 a"}
    