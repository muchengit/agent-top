---
title: L3 System Design Questions
validated_date: 2026-09-16
i18n-key: interviews-questions-l3-system-design
last-synced: 2026-09-16
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

Follow-up:

- How do you tell whether the final answer came from RAG, memory, or live tool state?

## 3. When should a system use multi-agent versus single-agent?

Expected answer:

- Use multi-agent when decomposition improves clarity, isolation, or specialization.
- Avoid multi-agent when it adds coordination cost without improving reliability.
- Add verification agents only when independent checks add value.

Listen for:

- Simplicity first.
- Coordination cost awareness.
- Concrete failure modes.

Follow-up:

- What makes a multi-agent system unsafe?

## 4. How do you evaluate a retrieval agent before launch?

Expected answer:

- Build a corpus and query set.
- Measure relevance and recall for required facts.
- Measure answer support and citation quality.
- Include negative cases where no answer should be provided.
- Track latency and retrieval cost.

Listen for:

- Eval design before tuning.
- Negative and refusal cases.
- Metrics tied to user harm.

Follow-up:

- What do you do when retrieval is correct but the answer is wrong?
