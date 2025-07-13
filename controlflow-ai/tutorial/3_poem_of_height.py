import controlflow as cf
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@cf.flow
def height_flow(poem_topic:str):

    # Defining agent
    agent = cf.Agent(
        model = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
        )
    )

    # Getting user's height and converting it into inches 
    height = cf.Task("Get the user's height in feet.", 
                       agents=[agent],
                       user_access=True,
                       result_type=int,
                       instructions="Convert the height to inches.")
    height.run()

    # Accessing height result
    if height.result < 40:
        raise ValueError("You must be at least 40 inches tall to receive a poem.")
    else:
        # Generating poem from user's interest
        poem = cf.Task(
            "Write a personalized poem for the user that takes their height into account.",
            agents=[agent],
            context = dict(height=height, topic=poem_topic)
        )
        return poem

poem = height_flow(poem_topic='Machine Learning')
print(f"Poem: \n{poem}")