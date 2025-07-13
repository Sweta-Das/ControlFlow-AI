# Task Properties

"""3. Result Validator
- With `result_validator` parameter in ControlFlow, we can specify a custom validation function for the task's result.
- The function will be called with the raw result, but it'll return the validated result or raise an exception if the result isn't valid.
"""


# import os
# import controlflow as cf
# from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI

# load_dotenv()
# openai_api_key = os.getenv('OPENAI_API_KEY')

# agent = cf.Agent(
#     model = ChatOpenAI(
#         openai_api_key=openai_api_key,
#         model="gpt-3.5-turbo"
#     )
# )

# def validate_even(value: int) -> int:
#     if value % 2 != 0:
#         raise ValueError("Value must be even.")
#     return value

# number = cf.run(
#     objective="Choose a number", 
#     result_validator=validate_even)

# print(number)

"""
### Error: 
ValueError: 1 task failed: - Task #f2d592e4 ("Choose a number"): Repeated error in function call with argument conversion, preventing task completion.
22:13:30.082 | ERROR   | Task run 'Run task: Task #f2d592e4 ("Choose a number")' - Finished in state Failed('Task run encountered an exception ValueError: 1 task failed: - Task #f2d592e4 ("Choose a number"): Repeated error in function call with argument conversion, preventing task completion.')
"""

"""
### Explanation

The error in the above code is most likely because;
- `cf.run()` does not directly accept a `result_validator` parameter in this way.
- It executes an objective and returns a result, but validation typically needs to be applied to the result afterward.
- If `cf.run()` is returning a string instead of an integer, then `validate_even(value: int)` will fail when `%` is applied to a string.
"""

# Validating the result separately
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

def validate_even(value):
    try:
        number = int(value)  # Convert to integer before validation
        if number % 2 != 0:
            raise ValueError("Value must be even.")
        return number
    except ValueError as e:
        raise ValueError(f"Invalid number input: {value}. {str(e)}")

# Run the task
result = cf.run(objective="Choose a number")

# Validate the result manually
validated_number = validate_even(result)

print(validated_number)