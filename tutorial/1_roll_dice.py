import os
import random
import controlflow as cf # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langchain_anthropic import ChatAnthropic # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore

load_dotenv(find_dotenv())

oaikey = os.getenv('OPENAI_API_KEY')
claudekey = os.environ['ANTHROPIC_API_KEY']

if oaikey is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

def roll_dice(n: int) -> int:
    '''Roll n dice'''
    return [random.randint(1, 6) for _ in range(n)]

@cf.flow
def dice_flow():

    # agent = cf.Agent(
    #     model = ChatOpenAI(
    #         model="gpt-3.5-turbo",
    #         openai_api_key=oaikey,)
    # )

    agent = cf.Agent(
        model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
        )
    )

    # Task-1: Asking the user how many dice to roll.
    user_task = cf.Task(
        "Ask the user how many dice to roll.",
        agents = [agent],
        result_type=int,
        user_access=True, # By default, agents can't interact with users so, we need to set the parameter for user interaction.
    )

    # Task-2: Rolling the dice.
    dice_task = cf.Task(
        "Roll the dice.",
        agents=[agent],
        context = dict(n=user_task),
        tools = [roll_dice],
        result_type=list[int],
    )
    return dice_task

result = dice_flow()
print(f"The result is: {result}")