# Task Properties

"""3. Instructions
- The instructions of a task are a string that provides detailed instructions for the task. 
- This information is visible to agents during execution, helping them understand the task they are working on.
"""

import os
import controlflow as cf
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

agent = cf.Agent(
    model=ChatOpenAI(
        openai_api_key=openai_api_key,
        model="gpt-3.5-turbo"
    )
)

poem = cf.run(
    objective="Write a poem about AI",
    instructions="Write only 6 lines, and end the first line with `not evil`, second line with `be civil`",
)

print(poem)

"""Rule of thumb:
Use the task’s objective to describe what the task’s result should be, and use the instructions to provide more detailed instructions on how to achieve the objective.
"""