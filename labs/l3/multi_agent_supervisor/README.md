---
title: Multi-Agent Supervisor Lab
capability_level: L3
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L3 Lab: Multi-Agent Supervisor

## Goal

Practice assigning work to specialized agents from a deterministic task profile.

## Prerequisites

- L3 multi-agent flow concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l3.multi_agent_supervisor.test_lab
```

## What This Lab Teaches

- A supervisor should choose the smallest useful set of agents.
- Human confirmation is an agent route for risky tool work.
- Verification can be a separate agent responsibility.

## Common Pitfalls

- Creating more agents than needed.
- Letting a tool agent decide its own safety boundary.
- Forgetting a verifier for evidence-heavy tasks.

## Self-Check

1. When is a single agent better than a supervisor setup?
2. Why should confirmation be routed before a tool call?
3. How would you add a retry loop to this supervisor?
