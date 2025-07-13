# Using Task Decorator

import controlflow as cf # type: ignore
from controlflow import Task, task # type: ignore
from langchain_anthropic import ChatAnthropic # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore

load_dotenv(find_dotenv())

agent = cf.Agent(
    model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
        )
    )

@task(user_access=True)
def get_user_name() -> str:
    "Politely ask the user for their name."
    pass

@task(user_access=True)
def get_user_interest() -> list[str]:
    interests = Task(
        objective = "Ask user for 3 interests",
        agents = [agent],
        instructions = "Politely ask the user to provide three of their interests or hobbies."
    )

    return interests

@cf.flow()
def task_class():
    
    get_user_name()

    interest_ls = get_user_interest()
    
    return interest_ls

interests = task_class()
print(f"User Interests: {interests}")