---
title: RAG、记忆与可观测性骨架
capability_level: L3
validated_date: 2026-09-19
i18n-key: l3-rag-memory-observability
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L3 Lab：RAG、记忆与可观测性骨架

## Goal

把检索、记忆、生成与可观测性组合成一个本地骨架。

## Run

```bash
python -m unittest labs.l3.rag_memory_observability.test_lab
```

## Prerequisites

- 完成 L2。
- 基本理解检索、记忆与 trace。

## 要学什么

- 检索为 Agent 提供有边界的上下文。
- 记忆跨轮保留会话状态。
- 可观测性应记录检索、记忆与答案生成。

## 常见踩坑

- 为一次查询检索过多上下文。
- 把会话记忆与持久化用户记忆混为一谈。
- 生成答案时不记录使用了哪些上下文。

## Self-Check

1. 检索期间应记录什么？
2. 为什么会话记忆与长期记忆不同？
3. 什么让可观测性 trace 在调试时有用？
