---
i18n-key: interviews-questions-l5-patterns
last-synced: 2026-09-16
validated_date: 2026-09-16
---

L5 模式题

## 1. 什么让 Agent pattern 有价值？

答案要点：

- 解决跨场景重复问题。
- 稳定输入输出。
- 定义 failure modes。
- 包含 safety 和 verification。
- 比框架专用代码更好维护。

## 2. 如何判断该自建框架还是用现有框架？

答案要点：

- 现有框架能覆盖 state/tooling/observability 时先用现有。
- 反复出现的痛点且现有框架隐藏失败模式时才自建。
- 框架代码版本化隔离。

## 3. 设计高风险工具执行 pattern。

答案要点：

- classify risk by reversibility、blast radius、data sensitivity。
- preflight checks。
- destructive action confirmation/approval。
- audit logs。
- rollback/compensation。
- verify after execution。

