"""If a custom function lacks appropriate docs (i.e., poorly named, no type info, poor docstring, use of *args or **kwargs and suchlike) then, we can still turn
it into a tool using `Tool.from_schema` function. Using this, we can provide the name, desc and JSON schema for the function directly."""

from pydantic_ai import Agent, Tool
from pydantic_ai.models.test import TestModel


def foobar(**kwargs) -> str:
    return kwargs['a'] + kwargs['b']

tool = Tool.from_schema(
    function=foobar,
    name='sum',
    description='Sum two numbers.',
    json_schema={
        'additionalProperties': False,
        'properties': {
            'a': {'description': 'the first number', 'type': 'integer'},
            'b': {'description': 'the second number', 'type': 'integer'},
        },
        'required': ['a', 'b'],
        'type': 'object',
    }
)

test_model = TestModel()
agent = Agent(test_model, tools=[tool])

result = agent.run_sync('testing...')
print(result.output)
#> {"sum":0}


"""Note that validation of the tool arguments will not be performed, and this will pass all arguments as keyword arguments."""