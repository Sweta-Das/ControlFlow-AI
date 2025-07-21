"""Running Agents"""

from pydantic_ai import Agent
from dotenv import load_dotenv, find_dotenv
import asyncio

# Load env vars
load_dotenv(find_dotenv())

agent = Agent('openai:gpt-4o-mini')


async def main():
    result_sync = agent.run_sync('What is the capital of Italy?')
    print(result_sync.output)
    #> The capital of Italy is Rome.
    
    
    result = await agent.run('What is the capital of France?')
    print(result.output)
    #> The capital of France is Paris.

    async with agent.run_stream('What is the capital of the UK?') as response:
        print(await response.get_output())
        #> The capital of the United Kingdom is London.
        
if __name__=="__main__":
    asyncio.run(main())