"""Task Status

- Status of a task reflects whether an agent has started working on it, is currently working on it, or has completed it.
- They're always created with statuses such as;
    - 'PENDING': The task has been created but no agent has started working on it.
    - 'RUNNING': An agent is currently working on the task.
    - 'SUCCESSFUL'/'FAILED': The task has been successfully completed/failed by an agent."""


import os
import controlflow as cf
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

song_writer = cf.Agent(
    name="Song Writer",
    model=ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
)

task = cf.Task(
    objective="Write a song about witches.",
    agents=[song_writer],
)
task.run()
print(task.status)

