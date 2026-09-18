---
title: MCP Tool Selection
capability_level: L2
validated_date: 2026-09-18
tested_against: "python 3.10+"
---

# L2 Lab: MCP Tool Selection

## Goal

Deterministically pick the correct tool from an MCP-style tool manifest.
When a user request arrives, the selector matches it against tool
descriptions, validates arguments, and enforces confirmation or blocking
for dangerous operations — all rule-based, without any LLM or API key.

## Prerequisites

- L1 completed (core Agent components).
- Python 3.10+ with `unittest` and `ruff` available.
- Basic understanding of MCP-style tool boundaries (see L2 `single_agent_mcp`).

## Run

```bash
python -m unittest labs.l2.mcp_tool_selection.test_lab
```

Lint check:

```bash
python3 -m ruff check labs/l2/mcp_tool_selection/
```

## Common Pitfalls

- Matching on the whole sentence instead of stable keywords, so minor rewording
  silently flips the selected tool.
- Treating a medium-risk tool as safe just because it "probably" needs
  confirmation; always ask first unless the user explicitly confirmed.
- Skipping argument validation, letting malformed or unknown arguments reach
  the tool boundary.
- Forgetting that a request matching several tools is an ambiguity problem,
  not a puzzle to quietly resolve with the first match.

## Self-Check

1. Why is a deterministic keyword/intent matcher used instead of an LLM call?
2. What happens when a request matches more than one tool?
3. How is a high-risk operation stopped before any tool is invoked?
