---
i18n-key: quick-reference-production-checklist
last-synced: 2026-09-16
validated_date: 2026-09-16
---

生产清单

## 发布前

- [ ] Auth 和 permissions 已定义。
- [ ] Tool allowlist 和风险分类存在。
- [ ] Destructive actions 需要确认。
- [ ] Safety evals 通过。
- [ ] Golden prompts 通过。
- [ ] Trace fields 存在。
- [ ] Rollback plan 已记录。
- [ ] Cost 和 latency budgets 已设置。
- [ ] Incident owner 已命名。

## 事故中

- [ ] Disable risky action path。
- [ ] 必要时 freeze writes。
- [ ] Inspect traces。
- [ ] Identify root cause。
- [ ] Add regression eval。
- [ ] Document postmortem。

## 事故后

- [ ] Fix owner 和 due date assigned。
- [ ] Rollback tested。
- [ ] Evals updated。
- [ ] 文档 updated。
- [ ] Follow-up monitored。

