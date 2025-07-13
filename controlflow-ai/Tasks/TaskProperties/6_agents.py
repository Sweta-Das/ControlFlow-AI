"""Agents are workers, who are assigned to work on the task.
By default, every agent is assigned to a task, and are given tools for marking the task as successful or failed.

`Completion Agents` are agents who can be set to mark the task completion."""

import os
import controlflow as cf
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai_key = os.getenv("OPENAI_API_KEY")

script_writer = cf.Agent(
    name="Script Writer",
    model=ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=openai_key
    )
)

script_reviewer = cf.Agent(
    name="Script Reviewer",
    model=ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=openai_key
    )
)

task = cf.Task(
    objective="Write a script for a 5-minute video.",
    instructions="Write a script that is engaging and informative related to self-development.",
    agents=[script_writer, script_reviewer],
    completion_agents=[script_reviewer],
)

result = task.run()
print(result)

"""Here, `completion tools` get automatically assigned to the `completion agents`."""