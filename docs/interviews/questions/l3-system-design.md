---
title: L3 System Design Questions
validated_date: 2026-09-16
---

# L3 System Design Questions

## 1. Design a multi-agent customer support system.

Expected answer:

- Clarify intent and permissions first.
- Route between retrieval, tool execution, escalation, and memory.
- Add guardrails for unsafe actions.
- Log prompts, tool calls, decisions, and evaluation outcomes.

Listen for:

- Requirement decomposition.
- Component boundaries.
- Error isolation.
- Cost and latency awareness.

Follow-up:

- How do you prevent one agent from overwriting another agent's decision?

## 2. Design a RAG + memory + MCP data flow.

Expected answer:

- User query enters context.
- RAG retrieves scoped documents.
- Memory adds long-term context.
- MCP exposes tools.
- Agent plans, calls tools, observes, and verifies.

Listen for:

- Clear data flow.
- Privacy boundaries.
- Evaluation hooks.
