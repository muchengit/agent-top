---
title: Framework Map
validated_date: 2026-09-16
---

# Framework Map

Agent-Top treats frameworks as examples of stable patterns.

| Camp | Frameworks | Why It Matters |
| --- | --- | --- |
| Graph orchestration | LangGraph | Explicit state, cycles, checkpoints, and debugging. |
| Multi-agent | CrewAI, AutoGen | Role-based workflows and conversational coordination. |
| Lightweight | Smolagents, Agno | Small APIs and fast iteration. |
| SDK | OpenAI, Claude, Google ADK | Direct model platform integration. |
| Type-safe | Pydantic AI | Strong schema and validation ergonomics. |
| Enterprise | Semantic Kernel | .NET / enterprise ecosystems and plugins. |
| RAG | LlamaIndex, Haystack | Retrieval and document pipelines. |
| Optimization | DSPy | Declarative prompt and pipeline optimization. |

## Example Policy

Framework-specific code belongs in Labs. Concepts should stay independent of one framework where possible.

Each framework-sensitive example should include:

```yaml
validated_date: YYYY-MM-DD
tested_against: framework-name x.y.z
```
