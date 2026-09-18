---
title: 多轮状态 Lab
capability_level: L1
validated_date: 2026-09-19
i18n-key: l1-multi-turn-state
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L1 Lab：多轮状态

## Goal

在不调用 LLM 的情况下，练习多轮 Agent 状态、最近消息窗口与摘要交接。

## Prerequisites

- L1 记忆概念。
- Python 3.10+。

## Run

```bash
python -m unittest labs.l1.multi_turn_state.test_lab
```

## 本 Lab 教什么

- 最近上下文与长历史是不同的问题。
- 多轮状态可能超出 prompt 窗口。
- 摘要是受控的上下文压缩策略。

## 常见踩坑

- 永远传递所有消息。
- 让旧偏好覆盖用户更新的纠正。
- 摘要丢失事实且无法审计。

## Self-Check

1. Agent 何时应该摘要旧消息？
2. 哪些信息应留在最近上下文中？
3. 你会如何测试摘要是否丢失重要事实？
