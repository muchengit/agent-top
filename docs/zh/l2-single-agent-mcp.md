---
title: L2 带 MCP 的可靠单 Agent
validated_date: 2026-09-16
tested_against: "python 3.10+"
i18n-key: l2-single-agent-mcp
last-synced: 2026-09-16
---

# L2 带 MCP 的可靠单 Agent

## 目标

构建一个通过清晰 MCP 风格边界调用工具的可靠单 Agent。

## 前置

- 已完成 L0 和 L1
- 理解 guardrail 与工具校验

## 核心思路

- Tool server 应暴露小型、类型清晰的操作。
- Agent 应在调用工具前校验输入。
- 工具结果应在成为最终答案前再次检查。
- Guardrail 应阻止空输入、过长输入或高风险请求。

## 关联 Lab

见 [`../../labs/l2/single_agent_mcp/README.md`](../../labs/l2/single_agent_mcp/README.md)。
