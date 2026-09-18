---
title: L3 Labs
capability_level: L3
validated_date: 2026-09-18
---

# L3 Labs

## Goal

Build end-to-end systems with RAG, memory, observability, and multi-agent flows.

## Prerequisites

- L2: reliable single Agent and MCP
- Python 3.10+
- Familiarity with RAG, memory, and multi-agent concepts

## Labs in This Level

- [`rag_memory_observability`](rag_memory_observability/README.md): RAG, memory, and observability skeleton.
- [`rag_evaluator`](rag_evaluator/README.md): deterministic retrieval evaluation.
- [`multi_round_research_discussion`](multi_round_research_discussion/README.md): multi-round evidence planning and discussion convergence.
- [`multi_agent_supervisor`](multi_agent_supervisor/README.md): deterministic multi-agent routing.

## Run

```bash
python -m unittest discover -s labs/l3 -p "test_*.py"
```

## Common Pitfalls

- Adding memory without evaluating retrieval quality first.
- Letting multi-agent topologies grow without a deterministic supervisor.
- Forgetting observability when combining RAG, memory, and orchestration.

## Self-Check

1. How do you evaluate retrieval quality deterministically?
2. What role does a supervisor play in multi-agent routing?
3. Which observability signals matter most in a RAG memory pipeline?

