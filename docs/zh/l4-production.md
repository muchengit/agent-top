---
title: L4 生产级 Agent 系统
validated_date: 2026-09-16
i18n-key: l4-production
last-synced: 2026-09-16
---

# L4 生产级 Agent 系统

## 目标

把 Agent 原型推向生产可用系统。

## 前置

- 已完成 L0 到 L3
- 已有 evals、可观测和安全 guardrail 基础

## 生产检查清单

- 鉴权与权限。
- 限流与成本限制。
- 评估集与回归测试。
- 可观测 trace。
- 回滚方案。
- Postmortem 模板。

## 关联资产

- [`../production/evals-checklist.md`](../production/evals-checklist.md)
- [`../production/safety-checklist.md`](../production/safety-checklist.md)
- [`../../templates/postmortem-template.md`](../../templates/postmortem-template.md)
