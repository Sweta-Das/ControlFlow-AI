"""Tool Schema"""

"""
Pydantic AI is able to extract the docstring from functions and extract parameter descriptions from the docstring, and adds it to the schema using Griffe.

Griffe supports extracting parameters from `google`, `numpy`, and `sphinx` style docstrings.
"""

from pydantic_ai import Agent
from pydantic_ai.models.function import AgentInfo, FunctionModel
from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart


agent = Agent()


@agent.tool_plain(docstring_format='google', require_parameter_descriptions=True)
def food(a: int, b: str, c: dict[str, list[float]]) -> str:
    """Get me food.
    
    Args:
        a: apple pie
        b: banana cake
        c: carrot smoothie
    """
    
    return f'{a} {b} {c}'


def print_schema(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
    """Print the schema"""
    tool = info.function_tools[0]
    print(tool.description)
    """Get me food.""" # Output
    
    print(tool.parameters_json_schema)
    # Output
    """
    {
        'additionalProperties': False,
        'properties': {
            'a': {'description': 'apple pie', 'type': 'integer'},
            'b': {'description': 'banana cake', 'type': 'string'},
            'c': {
                'additionalProperties': {'items': {'type': 'number'}, 'type': 'array'},
                'description': 'carrot smoothie',
                'type': 'object', 
            },
        },
        'required': ['a', 'b', 'c'],
        'type': 'object',
    }
    """
    
    print(ModelResponse(parts=[TextPart('food')]))
    # Output
    """
    ModelResponse(
        parts=[TextPart(content='food')], 
        usage=Usage(), 
        timestamp=datetime.datetime(2025, 7, 21, 6, 6, 18, 19190, tzinfo=datetime.timezone.utc)
    )
    """
    
    return ModelResponse(parts=[TextPart('food')])

if __name__=="__main__":
    agent.run_sync('Hie!', model=FunctionModel(print_schema))