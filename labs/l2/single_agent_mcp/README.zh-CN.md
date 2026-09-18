---
title: 带 MCP 风格工具边界的单 Agent
capability_level: L2
validated_date: 2026-09-19
i18n-key: l2-single-agent-mcp
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L2 Lab：带 MCP 风格工具边界的单 Agent

## Goal

用一个小型 MCP 风格工具接口建模单 Agent，无需外部 MCP server。

## Run

```bash
python -m unittest labs.l2.single_agent_mcp.test_lab
```

## 要学什么

- 工具服务器暴露类型化操作。
- Agent 应验证工具结果。
- 护栏可以拒绝不安全或格式错误的请求。

## Prerequisites

- 完成 L1。
- 基本理解校验与护栏。

## 常见踩坑

- 不先验证输入就调用工具。
- 没有响应 schema 或健全性检查就信任工具输出。
- 让不安全请求到达工具边界。

## Self-Check

1. 为什么工具调用应显式类型化？
2. Agent 应如何处理格式错误的工具参数？
3. 什么护栏能阻止空请求？
