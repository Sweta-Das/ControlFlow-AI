# from pydantic_ai import Agent
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv())

# agent = Agent(  
#     model='google-gla:gemini-1.5-flash',
#     system_prompt='Be concise, reply with one sentence.',  
# )

# result = agent.run_sync('Where does "hello world" come from?')  
# print(result.output)


# """
# The phrase "hello, world" originated in Brian Kernighan's 1972 "A Tutorial Introduction to the Language B".
# """
import os
from pydantic_ai.providers.openai import OpenAIProvider

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


model = OpenAIModel(
    "gemini/gemini-2.5-flash-lite",
    provider=OpenAIProvider(
        base_url=os.getenv("LITELLM_API_BASE"),
        api_key=os.getenv("LITELLM_API_KEY"),
    ),
)
agent = Agent(model, system_prompt="What is the capital of France?")



result = agent.run_sync()
print(result.output)