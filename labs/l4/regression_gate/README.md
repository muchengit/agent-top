---
title: Regression Gate Lab
capability_level: L4
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L4 Lab: Regression Gate

## Goal

Practice release gating for safety, trace completeness, rollback, and cost.

## Prerequisites

- L4 production systems concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l4.regression_gate.test_lab
```

## What This Lab Teaches

- Release gates can be expressed as deterministic checks.
- Safety and rollback should be blocking requirements.
- Cost over budget is a release risk.

## Common Pitfalls

- Treating cost warning as optional.
- Shipping with missing trace fields.
- Skipping rollback checks.

## Self-Check

1. Which failure should always block release?
2. Why are missing trace fields blocking?
3. How would you add latency p95 to this gate?
