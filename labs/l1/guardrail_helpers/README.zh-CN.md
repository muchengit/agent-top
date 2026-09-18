---
title: 护栏辅助 Lab
capability_level: L1
validated_date: 2026-09-19
i18n-key: l1-guardrail-helpers
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L1 Lab：护栏辅助

## Goal

练习本地工具策略决策，无需调用任何外部工具。

## Prerequisites

- 理解 L1 核心组件。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l1.guardrail_helpers.test_lab
```

## 本 Lab 教什么

- 工具需要角色权限。
- 破坏性工具需要确认。
- 策略评估应在执行前完成。

## 常见踩坑

- 在执行后才检查权限。
- 把破坏性工具与写入工具同等对待。
- 忘记未知工具必须被拦截。

## Self-Check

1. 为什么破坏性工具应要求确认？
2. 当角色未被允许时应该发生什么？
3. 你会如何为该策略添加成本上限？
