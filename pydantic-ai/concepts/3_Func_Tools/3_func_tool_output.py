"""Tool Output"""
# Tools can return anything that Pydantic can serialize to JSON; audio, video, image or doc, depending on the types of multi-modal input the model supports

"""Getting results from model on sending them Doc or Image"""

from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from pydantic_ai import Agent, DocumentUrl, ImageUrl
from pydantic_ai.models.openai import OpenAIResponsesModel

# Load env vars
load_dotenv(find_dotenv())

# Instantiate agent
agent = Agent(
    model=OpenAIResponsesModel('gpt-4o')
) 

@agent.tool_plain
def get_current_time() -> datetime:
    """Returns current date and time"""
    return datetime.now() 


@agent.tool_plain
def get_company_logo() -> ImageUrl:
    """Returns company's logo image from the URL"""
    return ImageUrl(url="https://gdm-catalog-fmapi-prod.imgix.net/ProductLogo/c58a8b76-1575-4060-afa8-cd3d43ed12c7.png")


@agent.tool_plain
def get_doc() -> DocumentUrl:
    """Returns doc's content from the doc URL"""
    return DocumentUrl(url="https://arxiv.org/pdf/2507.13337")


def main():
    # Get current time
    result1 = agent.run_sync("What is the current time?")
    print(result1.output)
    """The current time is 23:11 on July 19, 2025."""
    
    # Get the company's name
    result2 = agent.run_sync("What is the name of the company?")
    print(result2.output)
    """Could you please provide more context or specify which company you are referring to?""" # Not that smart after all 😏
    
    result3 = agent.run_sync("What is the name of the company in the logo?")
    print(result3.output)
    """The company in the logo is 'grepsr.'""" # Grammar is wrong since '.' is within the quotes, but it's ok. 😐
    
    # Get doc info
    result4 = agent.run_sync("What is the main content of the doc? Explain in 5-8 lines.")
    print(result4.output)
    """
    The document presents the FormulaOne benchmark, which evaluates the algorithmic reasoning capabilities of AI models beyond competitive programming. 
    It focuses on real-life research problems at the intersection of graph theory, logic, and algorithms, requiring deep reasoning skills like topological and 
    geometric insight, mathematical knowledge, and precise implementation. Despite the inclusion of these problems in a familiar domain for modern reasoning models, 
    state-of-the-art AI models struggle significantly, highlighting a gap between current AI capabilities and genuine expert-level understanding. The dataset 
    includes problems formulated using Monadic Second-Order logic, emphasizing both theoretical and practical implications, particularly in relation to the Strong 
    Exponential Time Hypothesis (SETH). The document underscores the need for better benchmarks and structured approaches to advance AI's problem-solving capabilities.
    """
    # Pretty cool 👏
    
if __name__ == "__main__":
    main()