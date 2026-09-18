---
title: 模式目录 Lab
capability_level: L5
validated_date: 2026-09-19
i18n-key: l5-pattern-catalog
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L5 Lab：模式目录

## Goal

练习定义带稳定输入、输出、安全检查与验证的可复用 Agent 模式。

## Prerequisites

- L5 自定义模式概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l5.pattern_catalog.test_lab
```

## 本 Lab 教什么

- 模式需要显式契约。
- 安全与验证属于模式定义的一部分。
- 未知模式应失败关闭（fail closed）。

## 常见踩坑

- 把框架包装器当作模式。
- 定义输出但不定义失败模式。
- 省略验证。

## Self-Check

1. 什么让模式可以复用于生产？
2. 为什么未知模式应失败关闭？
3. 你会如何为目录添加采用示例？
