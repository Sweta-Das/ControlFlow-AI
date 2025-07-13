from pydantic_ai import Agent
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

agent = Agent(  
    model='google-gla:gemini-1.5-flash',
    system_prompt='Be concise, reply with one sentence.',  
)

result = agent.run_sync('Where does "hello world" come from?')  
print(result.output)


"""
The phrase "hello, world" originated in Brian Kernighan's 1972 "A Tutorial Introduction to the Language B".
"""