# Agents

- primary interface for interacting with LLMs.
- Some usecases require only a single Agent to control an entire app or component, but multiple agents can also interact to embody more complex workflows.
- Agent can be called as a container for:
    - **System Prompt(s)** -> A set of instructions for the LLM written by the developer.
    - **Function tool(s)** -> Functions that the LLM may call to get information while generating a response.
    - **Structured Output Type** -> The structured datatype the LLM must return at the end of a run, if specified.
    - **Dependency Type Constraint** -> System prompt functions, tools, and output validators may all use dependencies when they're run.
    - **LLM Model** -> [Optional] default LLM associated with the agent. Can also be specified when running the agent
    - **Model Settings** -> [Optional] default model settings to help fine tune requests. Can also be specified when running the agent


## Running Agents

- 4 ways to run an agent:
1. `agent.run()`
    - a coroutine which returns a RunResult containing a completed response
2. `agent.run_sync()`
    - a plain, synchronous function which returns a RunResult containing a completed response (internally, this just calls `loop.run_until_complete(self.run()`)
3. `agent.run_stream()`
    - a coroutine which returns a `StreamedRunResult`, which contains methods to stream a response as an async iterable
4. `agent.iter()`
    - a context manager which returns an `AgentRun`, an async-iterable over the nodes of the agent's underlying `Graph`


## Iterating Over an Agent's Graph

- Each agent in Pydantic AI uses **`pydantic-graph`** to manage its execution flow.
- *pydantic-graph* is a generic, type-centric lib. for building and running finite state machines in Python
- It can also be used standalone for workflows that have nothing to do with Gen-AI.
- Pydantic-AI uses pydantic-graph to orchestrate the handling of model requests and model responses in an agent's run.
- Developers may not need to use `pydantic-graph` as it is automatically called and traversed from start to finish internally with `agent.run(...)`. </br>
- However, for deeper insight or control (to capture each tool invocation, injecting own logic at specific stages), Pydantic AI exposes the lower level iteration process via `Agent.iter`. This method returns an `AgentRun`, which we can async-iterate over, or manually drive node-by-node via the next method. Once the agent's graph returns an `End`, we've the final result along with a detailed history of all steps.