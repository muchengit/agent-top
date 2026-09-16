---
title: Labs Index
validated_date: 2026-09-16
---

# Labs

Executable Labs are the primary hands-on format for Agent-Top.

## Current Labs

- [`l0/first_llm_call`](l0/first_llm_call/README.md): first LLM call shape and terminology.
- [`l1/minimal_react_agent`](l1/minimal_react_agent/README.md): minimal ReAct agent without a framework.
- [`l2/single_agent_mcp`](l2/single_agent_mcp/README.md): single Agent with MCP-style tool boundary and guardrails.
- [`l3/rag_memory_observability`](l3/rag_memory_observability/README.md): RAG, memory, and observability skeleton.
- [`l4/production_postmortem`](l4/production_postmortem/README.md): executable production postmortem structure, coverage checks, and action-item closure.
- [`l5/custom_pattern_lab`](l5/custom_pattern_lab/README.md): reusable custom pattern with safety and verification.

## Run All Tests

```bash
python -m unittest discover -s labs -p "test_*.py"
```
