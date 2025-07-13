# Task Properties

"""2. Result Type
- Task's result type indicates the type of value that the task will run.
- Used to validate the task's result & to help agents understand the task's output.
"""

import os
import controlflow as cf  # type: ignore
from controlflow import task  # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore
from dotenv import load_dotenv  # type: ignore
from pydantic import BaseModel  # type: ignore

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

agent = cf.Agent(
    model=ChatOpenAI(
        openai_api_key=openai_api_key,
        model="gpt-3.5-turbo",
    )
)

# Pydantic Model
class Name(BaseModel):
    first: str
    last: str

@task
def create_name_task():
    name_task = cf.Task(
        objective="The input is 'John Doe'",
        agents=[agent],
        result_type=Name
    )
    return name_task.run()

@task
def classification():
    media_task = cf.Task(
        objective = "Star Wars: Return of the Jedi",
        agents=[agent],
        result_type=["book", "movie", "album"]
    )

# Define the flow to run the task
@cf.flow()
def name_flow():
    result = create_name_task()
    return result

# Execute the flow and print the result
result = name_flow()
print(result)

