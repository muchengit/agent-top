---
i18n-key: quick-reference-architecture-patterns
last-synced: 2026-09-16
validated_date: 2026-09-16
---

架构模式速查

| Pattern | Use When | Avoid When |
| --- | --- | --- |
| Single LLM call | 简单回答、无工具 | 需要 evidence 或 action |
| ReAct loop | 需要工具的 observable steps | tool results 不可信 |
| RAG Agent | 答案依赖私有或当前 docs | corpus stale/untrustworthy |
| Tool-using Agent | 需要外部状态或 side effects | permissions 不清楚 |
| Multi-agent supervisor | specialization 和 verification 有帮助 | 单 Agent + tools 就够 |
| Production Agent | 需要 auth、evals、traces、rollback | 只需要 prototype |

