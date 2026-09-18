---
title: 首次 LLM 调用
capability_level: L0
validated_date: 2026-09-19
i18n-key: l0-first-llm-call
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L0 Lab：首次 LLM 调用

## Goal

理解 LLM 调用的基本请求/响应形态，无需 API key。

## Prerequisites

- Python 3.10+
- 熟悉 Markdown 与终端命令

## Run

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

## 要学什么

- 模型请求包含 prompt。
- 响应包含生成的文本。
- Token 并不完全等于单词。
- System prompt 设定助手角色。
- 上下文窗口限制模型可处理的总文本量。

## 常见踩坑

- 把 token 当成单词。Token 是模型特定的文本块。
- 忘记空 prompt 可能产生未定义或不安全的行为。
- 假设一个 prompt 一定对应一个确定性答案。

## Self-Check

1. System prompt 的作用是什么？
2. 为什么 token 与单词不同？
3. 如果 prompt 为空可能出什么问题？
