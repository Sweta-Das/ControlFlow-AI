import controlflow as cf
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv(find_dotenv())

# Agent-1: Writer
writer = cf.Agent(
    name="Writer",
    model = ChatOpenAI(model="gpt-3.5-turbo"),
    description="An AI agent that writes paragraphs."
)

# Agent-2: Editor
editor = cf.Agent(
    name="Editor",
    model = ChatOpenAI(model="gpt-3.5-turbo"),
    description="An AI agent that edits paragraphs for clarity and coherence."
)
# ChatAnthropic(model="claude-3-5-sonnet-20240620")
# Agent-3: Manager
manager = cf.Agent(
    name="Manager",
    model = ChatOpenAI(model="gpt-3.5-turbo"),
    description="An AI agent that manages the writing process.",
    instructions="""
    Ensure that the final paragraph meets high standards of high quality, clarity and coherence. Be strict in your assessments and only approve those paragraphs who fully meets the criteria.
    """
)

@cf.flow
def writing_flow():

    # Task-1: Writing 
    draft_task = cf.Task(
        "Write a paragraph on AI regulations.",
        agents=[writer],
    )

    approved = False
    while not approved:

        # Task-2: Editing
        edit_task = cf.Task(
            "Edit the paragraph for clarity and coherence.",
            context = dict(draft=draft_task),
            agents=[editor]
        )

        # Task-3: Approving
        approval_task = cf.Task(
            "Review the edited paragraph to see if it meets the quality standards.",
            result_type = bool,
            context = dict(edit=edit_task),
            agents=[manager]
        )

        approved = approval_task.run()

    return approved, edit_task.result

approved, draft = writing_flow()
print(f'{"Approved" if approved else "Rejected"} paragraph:\n{draft}')