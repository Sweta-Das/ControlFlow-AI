"""If a tool has a single parameter that can be represented as an object in JSON schema (e.g., dataclass, TypedDict, pydantic model), the schema for the tool is simplified to be just that object."""

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel


# Instantiate agent
agent = Agent()


# Pydantic Models
class Foobar(BaseModel):
    x: int
    y: str
    z: float = 3.14
    
    
@agent.tool_plain
def foobar(f: Foobar) -> str:
    return str(f)


# Instantiate test model
test_model = TestModel()
result = agent.run_sync('Hey!', model=test_model)
print(result.output) 
# Output: {"foobar":"x=0 y='a' z=3.14"}

print(test_model.last_model_request_parameters.function_tools)
# Output:
"""
[
    ToolDefinition(
        name='foobar', 
        parameters_json_schema={
            'properties': {
                'x': {'type': 'integer'},
                'y': {'type': 'string'}, 
                'z': {'default': 3.14, 'type': 'number'}
            }, 
            'required': ['x', 'y'], 
            'title': 'Foobar', 
            'type': 'object'
        }
    )
]
"""
