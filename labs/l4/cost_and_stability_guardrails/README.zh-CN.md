---
title: 成本与稳定性护栏 Lab
capability_level: L4
validated_date: 2026-09-19
i18n-key: l4-cost-and-stability-guardrails
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L4 Lab：成本与稳定性护栏

## Goal

练习面向 Agent 成本、延迟、重试循环与降级决策的确定性运行时护栏，无需 API key。

## Prerequisites

- L4 生产系统概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l4.cost_and_stability_guardrails.test_lab
```

## 本 Lab 教什么

- 成本与延迟应是一等发布与运行时风险。
- Agent 循环需要最大步数、重试预算与工具调用上限。
- 降级应在降低风险的同时保留安全与可观测性。

## 常见踩坑

- 把成本飙升当作计费问题而不是可靠性问题。
- 让重试无限递归。
- 降级性能时移除 trace。

## Self-Check

1. 运行时何时应降级而不是阻塞每个请求？
2. 为什么应在再次调用模型前统计 token 预算？
3. 降级模式下哪个护栏应保持活跃？
