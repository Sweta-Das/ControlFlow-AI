# Task Properties

"""1. Objective
- Objective is the main goal of the task.
- It's used to guide the task's execution and to help agents understand the task's purpose.
"""

import os
import controlflow as cf  # type: ignore
from controlflow import Task, task  # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore
from dotenv import load_dotenv, find_dotenv  # type: ignore

load_dotenv(find_dotenv())
oaikey = os.getenv('OPENAI_API_KEY')

# Initialize the agent
agent = cf.Agent(
    model=ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key = oaikey
    )
)

# Define a task to write a poem
@task(user_access=False)
def write_poem():
    poem_task = cf.Task(
        objective="Write a poem about clouds.",
        agents=[agent]
    )
    # Run the task and return the result
    poem_result = poem_task.run()
    return poem_result

# Define the control flow
@cf.flow()
def poem_flow():
    poem = write_poem()
    return poem

# Execute the flow
poem = poem_flow()
print(poem)