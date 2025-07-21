"""Advanced Tool Returns"""

"""
For scenarios where there's need for more control over both the tool's return value
and the content sent to the model, `ToolReturn` is used.

Useful when:
- Provide rich multi-modal content (images, docs, etc.) to the model as context
- Separate the programmatic return value from the model's context
- Include additional metadata that shouldn't be sent to the LLM
"""

"""A computer automation tool that captures screenshots and provide visual feedback"""

import io
import time
import pyautogui
from pydantic_ai import Agent
from dotenv import load_dotenv, find_dotenv
from pydantic_ai.messages import ToolReturn, BinaryContent


# Load env vars
load_dotenv(find_dotenv())


def capture_ss() -> bytes:
    """Capture the entire screen using pyautogui and return the image as bytes"""
    screenshot = pyautogui.screenshot()
    buf = io.BytesIO()
    screenshot.save(buf, format='PNG')
    return buf.getvalue()
    
    
def perform_click(x: int, y: int):
    """Moves the mouse to the specified coordinates & clicks"""
    pyautogui.click(x, y)
    print(f"Performed a click at coordinates: ({x}, {y})")
    
    
# Instantiate an agent
agent = Agent(
    model='openai:gpt-4o'
)


@agent.tool_plain
def click_and_capture(x: int, y: int) -> ToolReturn:
    """Click at coordinates and show before/after screenshots"""
    
    # Take screenshot before action
    before_ss = capture_ss() 
    
    # Perform click operation
    perform_click(x, y)
    time.sleep(0.5) # Wait for UI to update
    
    # Take screenshot after action
    after_ss = capture_ss() 
    
    return ToolReturn(
        return_value=f"Successfully clicked at ({x}, {y})",
        content=[
            f"Clicked at coordinates ({x}, {y}). Here's the comparison:",
            "Before:",
            BinaryContent(data=before_ss, media_type='image/png'),
            "After:",
            BinaryContent(data=after_ss, media_type='image/png'),
            "Please analyze the changes and suggest next steps."
            ],
        metadata={
            "coordinates": {"x": x, "y": y},
            "action_type": "click_and_capture",
            "timestamp": time.time()
        }
    )
    
result = agent.run_sync("Click on the 1st product and tell me what happened")
print(result.output)

