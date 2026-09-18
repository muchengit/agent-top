---
title: MCP 工具选择
capability_level: L2
validated_date: 2026-09-19
i18n-key: l2-mcp-tool-selection
last-synced: 2026-09-19
tested_against: "python 3.10+"
---

# L2 Lab：MCP 工具选择

## Goal

从 MCP 风格工具清单中确定性挑选正确工具。当用户请求到达时，选择器将其与工具描述匹配、校验参数，并对危险操作执行确认或拦截——全部基于规则，无需任何 LLM 或 API key。

## Prerequisites

- 完成 L1（核心 Agent 组件）。
- Python 3.10+，具备 `unittest` 与 `ruff`。
- 基本理解 MCP 风格工具边界（参见 L2 `single_agent_mcp`）。

## Run

```bash
python -m unittest labs.l2.mcp_tool_selection.test_lab
```

Lint 检查：

```bash
python3 -m ruff check labs/l2/mcp_tool_selection/
```

## 常见踩坑

- 匹配整句而不是稳定关键词，导致轻微措辞变化就悄悄改变所选工具。
- 因为某工具“大概”需要确认就把它当中风险当安全；除非用户显式确认，否则先问。
- 跳过参数校验，让格式错误或未知参数到达工具边界。
- 忘记一个请求匹配多个工具是歧义问题，而不是用第一个匹配悄悄解决的谜题。

## Self-Check

1. 为什么用确定性关键词/意图匹配而不是 LLM 调用？
2. 当一个请求匹配多个工具时会发生什么？
3. 高风险操作如何在调用任何工具之前被阻止？
