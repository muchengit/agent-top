---
title: L0 Labs
capability_level: L0
validated_date: 2026-09-19
---

# L0 Labs

英文版：[`README.md`](README.md)

## 目标

完成第一次 LLM 调用，理解请求/响应形态、prompt、system prompt 与 context window 等概念；无需 API key。

## 前置条件

- Python 3.10+
- 基本的 Markdown 与终端操作能力

## 本级别 Labs

- [`first_llm_call`](first_llm_call/README.md)：首次 LLM 调用的形态与术语，附确定性测试。

## 运行

```bash
python -m unittest discover -s labs/l0 -p "test_*.py"
```

## 常见踩坑

- 把 token 当成 word。token 是模型相关的文本块划分。
- 假设同一个 prompt 一定产生同一个确定性答案。
- 忽略空 prompt 可能带来的未定义或危险行为。

## 自检

1. system prompt 的作用是什么？
2. 为什么 token 不等于 word？
3. prompt 为空时可能出什么问题？
