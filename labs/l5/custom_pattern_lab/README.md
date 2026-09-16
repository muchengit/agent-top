---
title: Custom Pattern Lab
capability_level: L5
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L5 Lab: Custom Pattern

## Goal

Abstract a reusable Agent pattern with stable inputs, outputs, failure modes, and safety checks.

## Prerequisites

- L0 through L4 completed.
- Comfort with designing small reusable systems.

## Run

```bash
python -m unittest labs.l5.custom_pattern_lab.test_lab
```

## What This Lab Teaches

- Reusable patterns need explicit inputs and outputs.
- Safety checks should happen before execution.
- Verification should be part of the loop, not an afterthought.

## Common Pitfalls

- Naming a pattern before defining its boundaries.
- Hiding failure modes inside the happy path.
- Skipping verification for risky actions.

## Self-Check

1. What are the stable boundaries of a reusable Agent pattern?
2. Why should safety checks run before execution?
3. How would another contributor maintain this pattern?
