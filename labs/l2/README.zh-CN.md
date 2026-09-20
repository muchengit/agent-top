---
title: L2 Labs
capability_level: L2
validated_date: 2026-09-19
---

# L2 Labs

英文版：[`README.md`](README.md)

## 目标

构建一个可靠单 Agent，具备框架风格工具边界与 MCP 风格集成，并加入成本与延迟感知路由。

## 前置条件

- L1：核心 Agent 组件
- Python 3.10+
- 了解 MCP 风格工具边界

## 本级别 Labs

- [`single_agent_mcp`](single_agent_mcp/README.md)：带 MCP 风格工具边界与护栏的单 Agent。
- [`cost_aware_router`](cost_aware_router/README.md)：成本与延迟感知路由。
- [`mcp_tool_selection`](mcp_tool_selection/README.md)：确定性 MCP 工具选择与校验。

## 运行

```bash
python -m unittest discover -s labs/l2 -p "test_*.py"
```

## 常见踩坑

- 把 MCP 当成传输细节，而不是工具边界契约。
- 只按成本路由，忽略延迟与正确性。
- 引入框架代码却不带 `tested_against` 之类的版本锚点。

## 自检

1. MCP 风格工具边界保护了什么？
2. 成本感知路由器应权衡哪些信号？
3. 为什么依赖框架的 Lab 需要版本锚点？
