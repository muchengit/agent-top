---
title: 回归门禁 Lab
capability_level: L4
validated_date: 2026-09-19
i18n-key: l4-regression-gate
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L4 Lab：回归门禁

## Goal

练习面向安全、trace 完整性、回滚与成本的发布门禁。

## Prerequisites

- L4 生产系统概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l4.regression_gate.test_lab
```

## 本 Lab 教什么

- 发布门禁可以表达为确定性检查。
- 安全与回滚应是阻塞性要求。
- 成本超预算是一种发布风险。

## 常见踩坑

- 把成本警告当作可选项。
- 带着缺失 trace 字段发布。
- 跳过回滚检查。

## Self-Check

1. 哪个失败应始终阻塞发布？
2. 为什么缺失 trace 字段是阻塞性的？
3. 你会如何为这个门禁添加延迟 p95？
