---
title: Single Agent with MCP-style Tool Boundary
capability_level: L2
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L2 Lab: Single Agent with MCP-style Tool Boundary

## Goal

Model a single Agent using a small MCP-style tool interface without requiring an external MCP server.

## Run

```bash
python -m unittest labs.l2.single_agent_mcp.test_lab
```

## What to Learn

- Tool servers expose typed operations.
- Agents should validate tool results.
- Guardrails can reject unsafe or malformed requests.

## Prerequisites

- L1 completed.
- Basic understanding of validation and guardrails.

## Common Pitfalls

- Calling tools without validating inputs first.
- Trusting tool output without a response schema or sanity check.
- Letting unsafe requests reach a tool boundary.

## Self-Check

1. Why should tool calls be explicitly typed?
2. How should an Agent handle malformed tool arguments?
3. What guardrail prevents empty requests?
