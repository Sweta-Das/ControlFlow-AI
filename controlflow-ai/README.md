# 🔄 ControlFlow — Structured Agentic AI Workflows

[ControlFlow](https://controlflow.ai/welcome) is a Python framework (built on Prefect 3.0) for creating **task-centric**, **observable**, and **type-safe** AI workflows powered by LLM agents.

---

## ⚙️ Why ControlFlow?

- **Task-centric architecture**: Break complex workflows into clear, manageable steps :contentReference[oaicite:2]{index=2}.
- **Type-safe outputs**: Leverage Pydantic models for validated, structured results :contentReference[oaicite:3]{index=3}.
- **Specialized agents**: Assign different agents (with unique models, instructions, and tools) to each task :contentReference[oaicite:4]{index=4}.
- **Flexible orchestration**: Build flows to coordinate complex multi-task, multi-agent processes with full observability :contentReference[oaicite:5]{index=5}.
- **Tool integration**: Easily add custom Python functions as tools. Use streaming, interactivity, memory, and AI-planning support :contentReference[oaicite:6]{index=6}.

---

## 🚀 Installation

```bash
pip install controlflow
export OPENAI_API_KEY="your-api-key"
