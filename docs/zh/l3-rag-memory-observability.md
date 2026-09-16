---
title: L3 RAG、记忆与可观测
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l3-rag-memory-observability
last-synced: 2026-09-16
---

# L3 RAG、记忆与可观测

## 目标

把 RAG、记忆、生成和可观测组合成可追踪骨架。

## 前置

- 已完成 L0 到 L2
- 理解检索与上下文组装

## 核心数据流

1. 用户 query 进入。
2. RAG 检索限定范围上下文。
3. Memory 补充长期上下文。
4. Agent 规划并调用工具。
5. Observability 记录 prompt、检索、工具调用、延迟和成本。

## 关联 Lab

见 [`../../labs/l3/rag_memory_observability/README.md`](../../labs/l3/rag_memory_observability/README.md)。
