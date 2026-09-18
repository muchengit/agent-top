---
title: L4 Lab：生产 Trace 完整性
capability_level: L4
validated_date: 2026-09-19
i18n-key: l4-production-trace-integrity
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L4 Lab：生产 Trace 完整性

## Goal

构建一个确定性校验器，检查生产可观测性 trace 的结构完整性：按 trace id 分组事件、要求 prompt 开始与 result 结束事件、强制时间戳单调、校验关键事件必填字段，并生成结构化问题报告。

## Prerequisites

- L3：端到端 RAG、记忆与多 Agent 流程
- Python 3.10+
- 基本熟悉 trace 与可观测性事件 schema

## Run

```bash
python -m unittest labs.l4.production_trace_integrity.test_lab
```

## 常见踩坑

- 把缺失 prompt 或 result 事件当作非阻塞；每个 trace 必须以 prompt 开始、以 result 结束。
- 用排序而不是流顺序检查时间戳；乱序事件必须按到达顺序标记。
- 忘记 tool_call 事件同时需要工具名与参数。
- 把孤儿事件（缺失 trace id）当成 trace；它们无法分组，必须单独标记。

## Self-Check

1. 什么时候 trace 是“broken”而不是“complete”？
2. 为什么时间戳检查必须按流顺序而不是排序顺序？
3. 你会如何把必填字段检查扩展到 decision 事件？
