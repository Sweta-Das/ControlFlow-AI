"""Build a Pydantic model from a text input"""

import os
import logfire
from pydantic_ai import Agent
from pydantic import BaseModel
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logfire.configure()
logfire.instrument_pydantic_ai()

class MyModel(BaseModel):
    city: str
    country: str
    
model = 'google-gla:gemini-1.5-flash'
print(f'Using model: {model}')

agent = Agent(
    model=model,
    output_type=MyModel
)

if __name__=="__main__":
    result = agent.run_sync('The beautiful city of Nepal')
    print(result.output)
    
    """
    Using model: google-gla:gemini-1.5-flash
    17:21:17.983 agent run
    17:21:17.985   chat gemini-1.5-flash
    Logfire project URL: https://logfire-us.pydantic.dev/swetadas0707/starter-project
    city='Kathmandu' country='Nepal'
    Usage(requests=1, request_tokens=22, response_tokens=8, total_tokens=30, details={'text_candidates_tokens': 8, 'text_prompt_tokens': 22})
    """
    print(result.usage())