import controlflow as cf # type: ignore
from langchain_anthropic import ChatAnthropic # type: ignore
from dotenv import load_dotenv, find_dotenv # type: ignore

load_dotenv(find_dotenv())

@cf.flow
def hello_flow(poem_topic:str):

    # Defining agent
    agent = cf.Agent(
        model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
        )
    )

    # Getting user's interest 
    interests = cf.Task("Get the user's interest", 
                       agents=[agent],
                       user_access=True)
    
    # Generating poem from user's interest
    poem = cf.Task(
        "Write a personalized poem about the provided topic.",
        agents=[agent],
        context = dict(interest=interests, topic=poem_topic)
    )
    return poem

poem = hello_flow(poem_topic='Machine Learning')
print(f"Poem: \n{poem}")


"""`hello_flow` is a portable agentic workflow which on every call will automatically create a flow context for all tasks
inside the flow, ensuring that they share the same state and history.

NOTE: `interests` task was never explicitly ran inside the flow, nor did we explicitly access its `result` attribute at the end.
This is because `@flow`-decorated functions are executed eagerly by default, meaning that when we call a flow function, all tasks
inside the flow are run automatically and any tasks returned from the flow are replaced with their result values.

`@flows` are eagerly-executed and `Tasks` are lazily-executed within the workflows.
"""