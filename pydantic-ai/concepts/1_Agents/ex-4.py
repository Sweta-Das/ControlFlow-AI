# agent_iter_next.py

"""We can also drive the iteration manually by passing the node we want to run next to the AgentRun.next(...) method. This allows to inspect or modify the node 
before it executes or skip nodes based on our own logic, and to catch errors in `next()` more easily:"""

import asyncio
from pydantic_ai import Agent
from pydantic_graph import End
from dotenv import load_dotenv, find_dotenv

# Load env vars
load_dotenv(find_dotenv())


# Instantiate an agent
agent = Agent(
    model='google-gla:gemini-2.5-flash'
)


async def main():
    
    async with agent.iter("What is the capital of France?") as agent_run:
        node = agent_run.next_node # Grab the 1st node
        
        all_nodes = [node]
        
        # Drive iteration manually
        while not isinstance(node, End): # The agent run is finished once an End node has been produced; instances of End cannot be passed to next.
            node = await agent_run.next(node)
            all_nodes.append(node)
            
        print(all_nodes)
        
        
        """
        [
            UserPromptNode(
                user_prompt='What is the capital of France?', 
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
                            content='What is the capital of France?', 
                            timestamp=datetime.datetime(2025, 7, 21, 10, 19, 7, 827793, tzinfo=datetime.timezone.utc)
                        )
                    ]
                )
            ), 
            CallToolsNode(
                model_response=ModelResponse(
                    parts=[
                        TextPart(content='The capital of France is Paris.')
                    ], 
                    usage=Usage(
                        requests=1, 
                        request_tokens=8, 
                        response_tokens=7, 
                        total_tokens=39, 
                        details={
                            'thoughts_tokens': 24, 
                            'text_prompt_tokens': 8
                        }
                    ), 
                    model_name='gemini-2.5-flash', 
                    timestamp=datetime.datetime(2025, 7, 21, 10, 19, 8, 963032, tzinfo=datetime.timezone.utc), 
                    vendor_details={'finish_reason': 'STOP'}
                )
            ), 
            End(data=FinalResult(output='The capital of France is Paris.'))
        ]
        """
        
if __name__=="__main__":
    asyncio.run(main())