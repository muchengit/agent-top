---
title: L1 Labs
capability_level: L1
validated_date: 2026-09-18
---

# L1 Labs


中文版：[`README.zh-CN.md`](README.zh-CN.md)

## Goal

Understand and implement the core Agent components: tool use, guardrails, and multi-turn state, without a framework.

## Prerequisites

- L0: first LLM call concepts
- Python 3.10+
- Basic familiarity with the ReAct pattern

## Labs in This Level

- [`minimal_react_agent`](minimal_react_agent/README.md): minimal ReAct agent without a framework.
- [`guardrail_helpers`](guardrail_helpers/README.md): local tool policy and confirmation boundaries.
- [`multi_turn_state`](multi_turn_state/README.md): multi-turn context state and summary handoff.

## Run

```bash
python -m unittest discover -s labs/l1 -p "test_*.py"
```

## Common Pitfalls

- Skipping guardrails when adding new tools. Every tool boundary needs a policy.
- Losing conversational context between turns because state is not summarized.
- Mixing framework concepts into framework-free Labs; keep each Lab self-contained.

## Self-Check

1. What are the core components of a minimal ReAct agent?
2. When should a tool call require a confirmation boundary?
3. How is multi-turn state preserved and compressed?

