---
title: Core Concept Deep-Dive Sources
validated_date: 2026-09-16
i18n-key: concepts-deep-dive-sources
last-synced: 2026-09-16
---

# Core Concept Deep-Dive Sources

This page links the external references used to deepen Agent-Top's core concept pages. It is not a copied tutorial collection. It explains how each source maps to Agent-Top patterns, Labs, and contribution work.

## Source Map

| Source | Agent-Top Concept | What To Absorb | Local Evidence |
| --- | --- | --- | --- |
| MCP Specification and Security Best Practices | [`mcp.md`](mcp.md) | Host/client/server model, tools/resources/prompts/sampling/roots/elicitation, transport, security controls | [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md) |
| NVIDIA 12-Factor Agents | [`multi-agent-scheduling.md`](multi-agent-scheduling.md) | Treat agent systems like production software: state, fault tolerance, observability, cost, rollback | [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md) |
| Microsoft Azure Multi-Agent Patterns | [`multi-agent-scheduling.md`](multi-agent-scheduling.md) | Supervisor, handoff, sequential, hierarchical, and fan-out/fan-in coordination patterns | [`../cases/multi-agent-collaboration.md`](../cases/multi-agent-collaboration.md) |
| Letta memory layers | [`long-term-memory.md`](long-term-memory.md) | Conversation, core, and recall memory layers; memory lifecycle | [`../../../labs/l1/multi_turn_state/README.md`](../../../labs/l1/multi_turn_state/README.md) |
| Mem0 | [`long-term-memory.md`](long-term-memory.md) | User/session/agent memory, memory extraction, update, and privacy considerations | [`../portfolio/projects.md`](../portfolio/projects.md) |
| Ragas hallucination guide | [`model-hallucination.md`](model-hallucination.md) | Unsupported claim evaluation, faithfulness, answer relevance, abstention-style checks | [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) |
| LangGraph plan-and-execute and search-tree planning | [`plan-decision-making.md`](plan-decision-making.md) | Plan/act separation, search-tree planning, cost/latency trade-off | [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md) |
| LlamaIndex planner docs | [`plan-decision-making.md`](plan-decision-making.md) | Planner as a decision policy, steps, and execution boundary | [`../skills/tool-mcp-safety.md`](../skills/tool-mcp-safety.md) |

## How To Use This Page

1. Pick one external source.
2. Read the corresponding Agent-Top concept page first.
3. Run the linked Lab or case evidence.
4. Write down what is stable and what is framework-specific.
5. If the source reveals a gap, open a `docs-only` or `lab` issue with a scoped patch proposal.

## Contribution Rules

- Do not copy external tutorials wholesale.
- Extract stable patterns and production trade-offs.
- Keep framework-specific API details in Labs or framework maps.
- Update `validated_date` when adapting a source into Agent-Top docs.
- Prefer reproducible local evidence over external screenshots or claims.
