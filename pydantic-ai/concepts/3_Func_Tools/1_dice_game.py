"""Registering Function Tools via Decorator"""

import random
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Define agent
agent = Agent(
    model='google-gla:gemini-2.0-flash',
    deps_type=str,
    system_prompt=(
        "You're a dice game, you should roll the die and see if the number "
        "you get matches the user's guess. If so, tell them they won. "
        "Use the player's name in the response."
    )
)

@agent.tool_plain
def roll_dice() -> str:
    """Roll a 6-sided die and return the result"""
    return str(random.randint(1, 6))
    
@agent.tool
def get_player_name(context: RunContext[str]) -> str:
    """Get the player's name"""
    return context.deps
    
if __name__=="__main__":
    # dice_result = agent.run_sync(
    #     user_prompt="My guess is 3",
    #     deps='Marie'
    # )
    # print(dice_result.output)
    # """Great job, Marie! The die roll was 3, and you guessed 3. You won!"""
    
    # dice_result = agent.run_sync(
    #     user_prompt="My guess is 8",
    #     deps='Marie'
    # )
    # print(dice_result.output)
    # """Sorry, I can only roll a 6-sided die, so the value will be between 1 and 6. Your guess of 8 is not possible."""
    
    dice_result = agent.run_sync(
        user_prompt="My guess is 5",
        deps='8'
    )
    print(dice_result.output)
    """Sorry 8, you guessed 5 and the die roll was 2. You did not win."""
    
    print(dice_result.all_messages())