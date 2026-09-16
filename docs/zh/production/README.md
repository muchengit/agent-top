---
i18n-key: production-readme
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# 生产指南

生产指南是 Agent 系统的上线准备层。

## 指南

- [`evals-checklist.md`](evals-checklist.md)
- [`safety-checklist.md`](safety-checklist.md)
- [`quarterly-maintenance.md`](quarterly-maintenance.md)

## 最低生产门槛

发布前确认：

- Auth 和 permissions 明确。
- Tool allowlist 和风险分类存在。
- Destructive actions 需要确认或审批。
- Safety evals 通过。
- Trace schema 包含 request、tool、retrieval、final answer 字段。
- Rollback plan 已记录并测试。
- Cost 和 latency budgets 已定义。

## 事故响应循环

1. 禁用 risky action path。
2. 数据完整性不确定时冻结 writes。
3. 检查 traces 和 tool logs。
4. 定位 root cause。
5. 增加 regression eval。
6. 用 owner、due date、prevention action 记录 postmortem。

## 相关案例

- [`../cases/production-regression-gate.md`](../cases/production-regression-gate.md)
