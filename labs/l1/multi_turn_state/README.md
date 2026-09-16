---
title: Multi-Turn State Lab
capability_level: L1
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L1 Lab: Multi-Turn State

## Goal

Practice multi-turn Agent state, recent-message windows, and summary handoff without calling an LLM.

## Prerequisites

- L1 memory concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l1.multi_turn_state.test_lab
```

## What This Lab Teaches

- Recent context and long history are different concerns.
- Multi-turn state can grow beyond the prompt window.
- Summaries are a controlled context compression strategy.

## Common Pitfalls

- Passing every message forever.
- Letting old preferences override newer user corrections.
- Losing facts during summary without auditability.

## Self-Check

1. When should an Agent summarize older messages?
2. What information should stay in recent context?
3. How would you test whether a summary loses important facts?
