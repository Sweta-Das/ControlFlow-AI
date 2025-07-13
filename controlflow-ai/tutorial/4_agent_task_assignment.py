import controlflow as cf
from dotenv import load_dotenv, find_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv(find_dotenv())

@cf.flow
def task_assignment():

    model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
    )

    # Defining agents
    doc_agent = cf.Agent(
        name = "DocsBot",
        model=model,
        description = "An agent that specializes in summarizing and relaying the information about a certain topic",
        instructions = (
            """
            You are an expert in summarizing. Your goal is to provide the user with accurate, informative brief summary that is easy to
            understand.
            """
        )
    )
    edit_agent = cf.Agent(
        name="EditorBot",
        model=model,
        description = "An agent that specializes in editing the summary",
        instructions = (
            """You are an expert in grammar, style, and clarity. Your goal is to review the summary created by DocsBot.
            You should output notes rather than rewriting the document."""
        )
    )

    # Getting summary
    summary = cf.Task(
        "Write a summary",
        agents = [doc_agent, edit_agent],
        instructions = (
            "Write a brief summary on Ramayana. The docs agent should generate the summary, after which the edit agent should review it. Only the editor can mark the task as complete."
        ),
    )

    with cf.instructions('No more than 2 paragraphs.'):
        return summary.run()
    
summary = task_assignment()
print(f"Ramayana Summary: \n{summary}")