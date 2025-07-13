"""Task Result:

- Task results are generated after the task has been completed. This is a value that satisfies the task’s objective and result type configuration.
- If a task fails, its result property will contain an error message describing the failure."""

import os
import controlflow as cf
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

artist = cf.Agent(
    model=ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
)

art = cf.Task(
    objective="Create a sad song of a sunset.",
    agents=[artist],
    result_type=str,
)

result = art.run()
print(result)