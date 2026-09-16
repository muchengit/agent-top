---
title: Minimal ReAct Agent
capability_level: L1
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L1 Lab: Minimal ReAct Agent

## Goal

Build a tiny ReAct-style agent from first principles with no framework.

## Run

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

## What to Learn

- Perception is the current observation.
- Planning chooses the next action.
- Tool calls produce observations.
- Stop conditions prevent infinite loops.

## Prerequisites

- L0 completed.
- Comfort with Python control flow and simple functions.

## Common Pitfalls

- Letting an agent loop forever without a stop condition.
- Treating tool output as truth without validation.
- Mixing perception, planning, and execution into one opaque step.

## Self-Check

1. What observation does the agent receive after a tool call?
2. Why is a stop condition necessary?
3. What fails if tool output is malformed?
