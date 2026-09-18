---
title: 自定义模式 Lab
capability_level: L5
validated_date: 2026-09-19
i18n-key: l5-custom-pattern
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L5 Lab：自定义模式

## Goal

抽象一个可复用的 Agent 模式，具有稳定输入、输出、失败模式与安全检查。

## Prerequisites

- 完成 L0 到 L4。
- 熟悉设计小型可复用系统。

## Run

```bash
python -m unittest labs.l5.custom_pattern_lab.test_lab
```

## 本 Lab 教什么

- 可复用模式需要显式输入与输出。
- 安全检查应在执行前完成。
- 验证应是循环的一部分，而不是事后补丁。

## 常见踩坑

- 在定义边界之前就命名模式。
- 把失败模式藏进 happy path。
- 对高风险动作跳过验证。

## Self-Check

1. 可复用 Agent 模式的稳定边界是什么？
2. 为什么安全检查应在执行前运行？
3. 其他贡献者如何维护这个模式？
