---
title: Cost Aware Router Lab
capability_level: L2
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L2 Lab: Cost Aware Router

## Goal

Learn to route requests by tool need, retrieval need, confirmation state, and latency budget.

## Prerequisites

- L1 and L2 tool boundary concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l2.cost_aware_router.test_lab
```

## What This Lab Teaches

- Routing can protect latency budgets.
- Confirmation is part of routing, not an afterthought.
- Escalation is a valid route when constraints are violated.

## Common Pitfalls

- Routing on keywords only.
- Ignoring latency budget.
- Allowing write actions without confirmation.

## Self-Check

1. Why can escalation be a route instead of an error?
2. Which constraint should block a risky action?
3. How would you add cost per task to the router?
