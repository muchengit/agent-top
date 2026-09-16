---
title: Guardrail Helper Lab
capability_level: L1
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L1 Lab: Guardrail Helpers

## Goal

Practice local tool policy decisions without calling any external tool.

## Prerequisites

- L1 core components understood.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l1.guardrail_helpers.test_lab
```

## What This Lab Teaches

- Tools need role permissions.
- Destructive tools require confirmation.
- Policy evaluation should happen before execution.

## Common Pitfalls

- Checking permissions after execution.
- Treating destructive and write tools the same.
- Forgetting that unknown tools must be blocked.

## Self-Check

1. Why should a destructive tool require confirmation?
2. What should happen when the role is not allowed?
3. How would you add a cost limit to this policy?
