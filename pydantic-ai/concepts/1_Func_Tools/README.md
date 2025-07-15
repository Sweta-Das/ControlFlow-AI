# Function Tools

- provides a mechanism for models to retrieve extra information to help them generate a response
- useful when we want to enable the model to take some action and use the result; especially in cases where:
    - it is impractical or impossible to put all the context into the sys prompt
    - we want to make agent's behavior more deterministic or reliable by deferring some of the logic required to generate response
    
*Note: To call a function as its final action, without the result being sent back to the model, we can use **output function** instead.*

## Number of ways to register tools with an agent:
1. **@agent.tool** decorator
- tools that need access to the agent context
- It is considered as the default decorator since in the majority of cases, tools will need access to the agent context.
2. **@agent.tool_plain** decorator
- tools that don't need access to the agent context
3. **tools**
- keyword arg to `Agent` which can take either plain functions, or instances of `Tool`
- useful when we want to reuse tools
- gives more fine-grained control over the tools

### Function Tool output
- Tools can return anything that Pydantic can serialize to JSON, as well as audio, video, image or document content depending on the types of multi-modal input the model supports.
- Some models (e.g. Gemini) natively support semi-structured return values, while some expect text (OpenAI) but seem to be just as good at extracting meaning from the data. 
- If a Python object is returned and the model expects a string, the value will be serialized to JSON.

### Advanced Tool Returns
- For more control over both tool's return value and the content sent to the model, `ToolReturn` is used.
- Useful in case of;
    - Provide rich multi-modal content (images, documents, etc.) to the model as context
    - Separate the programmatic return value from the model's context
    - Include additional metadata that shouldn't be sent to the LLM