---
title: 生产复盘模板 Lab
capability_level: L4
validated_date: 2026-09-19
i18n-key: l4-production-postmortem
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L4 Lab：生产复盘模板

## Goal

把生产故障转化为结构化复盘：根因、可度量行动项、评估覆盖、安全控制与回滚规划。

## Prerequisites

- 完成 L0 到 L3。
- 基本理解评估、可观测性与回滚。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l4.production_postmortem.test_lab
```

## 生产清单

- 认证与权限。
- 速率限制。
- 成本护栏。
- 评估集。
- 可观测性 trace。
- 回滚计划。

## 本 Lab 教什么

- 复盘必须指出根因，而不仅是总结症状。
- 行动项需要负责人、截止日期与类型标签。
- 回滚、评估与安全控制是生产就绪的一部分。
- 缺失覆盖应被显式暴露。

## 参考模板

参见 [`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md)。

## 常见踩坑

- 只写总结而没有根因。
- 创建没有负责人或截止日期的行动项。
- 跳过回滚、评估或安全控制跟进。

## Self-Check

1. 什么让复盘可执行？
2. 行动项没有负责人时缺失什么覆盖？
3. 为什么回滚与评估计划是生产就绪的一部分？
