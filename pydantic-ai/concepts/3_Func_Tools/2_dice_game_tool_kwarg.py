"""Registering Function Tools via Agent Argument"""

import random
from dotenv import load_dotenv, find_dotenv
from pydantic_ai import Agent, RunContext, Tool

load_dotenv(find_dotenv())

system_prompt = """
    You're a dice game, you should roll the die and see if the number you get back
    matches the user's guess. If so, tell them that they're a winner. Use the player's
    name in the response.
    """
    
# 1st func: To roll a dice
def roll_dice() -> str:
    """Roll a 6-sided die and return the result"""
    return str(random.randint(1, 6))
    
# 2nd func: Get player's name
def get_player_name(context: RunContext[str]) -> str:
    """Get the player's name"""
    return context.deps
    
# 1st agent
agent_1 = Agent(
    model='google-gla:gemini-2.0-flash',
    deps_type=str,
    tools=[roll_dice, get_player_name],
    system_prompt=system_prompt
)

# 2nd agent
agent_2 = Agent(
    model='google-gla:gemini-2.0-flash',
    deps_type=str,
    tools=[
        Tool(roll_dice, takes_ctx=False),
        Tool(get_player_name, takes_ctx=True)
    ],
    system_prompt=system_prompt
)

if __name__=="__main__":
    dice_result = {}
    dice_result['1'] = agent_1.run_sync(
        'My guess is 3',
        deps='Minar'
    )
    print(dice_result['1'].output)
    
    """Minar, you're a winner!"""
    
    dice_result['2'] = agent_2.run_sync(
        'My guess is 6',
        deps='Katie'
    )
    print(dice_result['2'].output)
    """Tough luck, Katie! You guessed 6, but I rolled a 5. Better luck next time!"""