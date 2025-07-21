"""Iterating over an agent's graph"""

# agent_iter_async_for.py

import asyncio
from pydantic_ai import Agent
from dotenv import load_dotenv, find_dotenv

# Load env vars
load_dotenv(find_dotenv())


# Instantiate an agent
agent = Agent(
    model='google-gla:gemini-2.5-flash'
)


async def main():
    nodes = []
    
    async with agent.iter("How are you?") as agent_run:
        async for node in agent_run:
            nodes.append(node)
            
    print(nodes)
    
    """
    [
        UserPromptNode(
            user_prompt='How are you?', 
            instructions=None, 
            instructions_functions=[], 
            system_prompts=(), 
            system_prompt_functions=[], 
            system_prompt_dynamic_functions={}
        ), 
        ModelRequestNode(
            request=ModelRequest(
                parts=[
                    UserPromptPart(
                        content='How are you?', 
                        timestamp=datetime.datetime(2025, 7, 21, 10, 1, 17, 288248, tzinfo=datetime.timezone.utc)
                    )
                ]
            )
        ), 
        CallToolsNode(
            model_response=ModelResponse(
                parts=[
                    TextPart(content='As an AI, I don\'t have personal feelings or experiences, so I can\'t be "fine" or "unwell" in the human sense.\n\nHowever, I am functioning perfectly and ready to assist you! How can I help you today?')
                ], 
                usage=Usage(
                    requests=1, 
                    request_tokens=5, 
                    response_tokens=53, 
                    total_tokens=387, 
                    details={'thoughts_tokens': 329, 'text_prompt_tokens': 5}
                ), 
                model_name='gemini-2.5-flash', 
                timestamp=datetime.datetime(2025, 7, 21, 10, 1, 20, 203004, tzinfo=datetime.timezone.utc), 
                vendor_details={'finish_reason': 'STOP'}
            )
        ),
        End(
            data=FinalResult(
                output='As an AI, I don\'t have personal feelings or experiences, so I can\'t be "fine" or "unwell" in the human sense.\n\nHowever, I am functioning perfectly and ready to assist you! How can I help you today?')
            )
    ]
    """
    
    
if __name__=="__main__":
    asyncio.run(main())