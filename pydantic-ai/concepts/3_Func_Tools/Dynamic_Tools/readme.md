## Dynamic Tools

Tools can also be defined with another function: `prepare`.
- This function is called at each step of a run to customize the definition of the tool passed to the model, or omit the tool completely from that step.
- This method can be registered via the `prepare` kwarg to any of the tool registration mechanisms:
    - `@agent.tool` decorator
    - `@agent.tool_plain` decorator
    - `Tool` dataclass

The `prepare` method should be of type `ToolPrepareFunc`.
- `ToolPrepareFunc` function takes `RunContext` and a pre-built `ToolDefinition`, and 
    - should either return that `ToolDefinition` with or without modifying it,
    - return a new `ToolDefinition`, or
    - return None to indicate that this tool should not be registered for that step