---
i18n-key: interviews-questions-l3-system-design
last-synced: 2026-09-16
validated_date: 2026-09-16
---

L3 系统设计题

## 1. 设计多 Agent 客服系统。

答案要点：

- 先澄清 intent 和 permissions。
- 路由 retrieval、tool、escalation、memory。
- 对 unsafe actions 加 guardrails。
- 记录 prompt、tool calls、decisions、eval outcomes。

## 2. 设计 RAG + memory + MCP data flow。

答案要点：

- user query enters context。
- RAG retrieves scoped documents。
- 记忆 adds durable context。
- MCP exposes tools。
- Agent plans, calls tools, observes, verifies。

## 3. 什么时候用多 Agent？

答案要点：

- decomposition improves clarity、isolation、specialization 时。
- coordination cost 不值时不要用。

