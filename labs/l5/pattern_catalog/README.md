---
title: Pattern Catalog Lab
capability_level: L5
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L5 Lab: Pattern Catalog

## Goal

Practice defining reusable Agent patterns with stable inputs, outputs, safety checks, and verification.

## Prerequisites

- L5 custom patterns concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l5.pattern_catalog.test_lab
```

## What This Lab Teaches

- Patterns need explicit contracts.
- Safety and verification belong in the pattern definition.
- Unknown patterns should fail closed.

## Common Pitfalls

- Treating a framework wrapper as a pattern.
- Defining outputs but not failure modes.
- Omitting verification.

## Self-Check

1. What makes a pattern ready for reuse?
2. Why should an unknown pattern fail closed?
3. How would you add adoption examples to the catalog?
