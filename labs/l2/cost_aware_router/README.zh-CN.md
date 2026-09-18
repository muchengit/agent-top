---
title: 成本感知路由器 Lab
capability_level: L2
validated_date: 2026-09-19
i18n-key: l2-cost-aware-router
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L2 Lab：成本感知路由器

## Goal

学习按工具需求、检索需求、确认状态与延迟预算来路由请求。

## Prerequisites

- L1 与 L2 工具边界概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l2.cost_aware_router.test_lab
```

## 本 Lab 教什么

- 路由可以保护延迟预算。
- 确认是路由的一部分，而不是事后补丁。
- 当约束被违反时，升级（Escalation）是合理的路由。

## 常见踩坑

- 只按关键词路由。
- 忽略延迟预算。
- 未经确认就允许写入动作。

## Self-Check

1. 为什么升级可以是路由而不是错误？
2. 哪个约束应拦截高风险动作？
3. 你会如何为路由器添加每次任务的成本？
