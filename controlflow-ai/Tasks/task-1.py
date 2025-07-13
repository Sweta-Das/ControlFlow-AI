# Using Task Class

import controlflow as cf
from controlflow import Task
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@cf.flow()
def task_class():
    agent = cf.Agent(
    model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
        )
    )

    interests = Task(
        objective = "Ask user for 3 interests",
        agents = [agent],
        result_type = list[str],
        user_access = True,
        instructions = "Politely ask the user to provide three of their interests or hobbies."
    )

    return interests

interests = task_class()
print(f"User Interests: {interests}")