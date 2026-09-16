---
i18n-key: interviews-questions-l4-production
last-synced: 2026-09-16
validated_date: 2026-09-16
---

L4 生产题

## 1. 发布 Agent feature 前要做什么？

答案要点：

- auth 和 permissions。
- rate limits 和 cost guardrails。
- eval set green。
- observability traces。
- rollback plan。

## 2. 客户报告 Agent 做了错误账户变更怎么办？

答案要点：

- stop unsafe action path。
- inspect traces。
- identify root cause。
- add regression eval。
- document postmortem。

## 3. model version change 怎么处理？

答案要点：

- treat as release。
- run golden and safety evals。
- compare latency、cost、refusal、tool-call behavior。
- shadow/canary。
- rollback to prior model/prompt path。

