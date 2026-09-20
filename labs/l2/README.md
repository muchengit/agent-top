---
title: L2 Labs
capability_level: L2
validated_date: 2026-09-18
---

# L2 Labs


中文版：[`README.zh-CN.md`](README.zh-CN.md)

## Goal

Build a reliable single Agent with a framework-style tool boundary and MCP-style integration, plus cost- and latency-aware routing.

## Prerequisites

- L1: core Agent components
- Python 3.10+
- Basic understanding of MCP-style tool boundaries

## Labs in This Level

- [`single_agent_mcp`](single_agent_mcp/README.md): single Agent with MCP-style tool boundary and guardrails.
- [`cost_aware_router`](cost_aware_router/README.md): cost and latency-aware routing.
- [`mcp_tool_selection`](mcp_tool_selection/README.md): deterministic MCP tool selection and validation.

## Run

```bash
python -m unittest discover -s labs/l2 -p "test_*.py"
```

## Common Pitfalls

- Treating MCP as a transport detail instead of a tool-boundary contract.
- Routing only on cost while ignoring latency and correctness.
- Adding framework code without version anchors such as `tested_against`.

## Self-Check

1. What does an MCP-style tool boundary protect?
2. Which signals should a cost-aware router balance?
3. Why are version anchors important for framework-dependent Labs?
