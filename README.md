# 🧩 Pydantic AI — Agent Framework with Pydantic

[Pydantic AI](https://ai.pydantic.dev/) is a **Python-first agent framework** built by the Pydantic team. It uses Pydantic models to bring **type safety**, **structured responses**, and **smooth integration** with LLMs into your agent workflows.

---

## 🚀 Why Use Pydantic AI

- **Built by the Pydantic team** — designed for production-grade GenAI apps  
- **Model-agnostic** — supports OpenAI, Anthropic, Gemini, Groq, Cohere, Mistral, and more 
- **Type-safe & structured** — outputs validated and enforced via Pydantic schemas 
- **Tool integration** — supports function tools and dependency injection for dynamic behavior 
- **Streamed & instrumented** — live output streaming and optional Logfire telemetry 

---

## ⚙️ Installation

Requires **Python 3.9+**:

```bash
pip install pydantic-ai
# Optional tool support:
pip install "pydantic-ai[logfire]"        # For telemetry
pip install "pydantic-ai[examples]"       # To run built-in examples
