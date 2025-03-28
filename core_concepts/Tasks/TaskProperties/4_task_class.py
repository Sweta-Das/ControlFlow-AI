"""
Most straighforward way to create a task is using the `Task` class.
"""

import os
import controlflow as cf
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai_key = os.getenv("OPENAI_API_KEY")

agent = cf.Agent(
    name = "Poet",
    model=ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key = openai_key
    )
)

task = cf.Task(
    objective = "Write a poem about the provided topic.",
    instructions = "Write 10 lines that rhymes.",
    agents = [agent],
    context = {"topic": "Life"},
)

result = task.run()
print(result)