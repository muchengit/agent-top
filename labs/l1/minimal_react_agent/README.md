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
