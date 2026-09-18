---
title: L5 Lab: Pattern Evaluation Gate
capability_level: L5
validated_date: 2026-09-18
tested_against: "python 3.10+"
---

# L5 Lab: Pattern Evaluation Gate

## Goal

Build a deterministic gate that evaluates whether a reusable Agent pattern is ready to enter the catalog, scoring reproducibility, evidence, safety, documentation, and ownership, then aggregating each pattern into passed, needs-fix, or rejected.

## Prerequisites

- L4: productionized Agent systems
- Python 3.10+
- Familiarity with pattern-first design and release gating

## Run

```bash
python -m unittest labs.l5.pattern_eval_gate.test_lab
```

## Common Pitfalls

- Treating missing reproduction steps or unmitigated high-risk items as fixable; they are blocking and must reject the pattern.
- Skipping human sign-off for high-risk patterns even when no unresolved items remain.
- Confusing "needs review" (human attention) with "needs fix" (clear remediation) or "rejected" (blocking).
- Forgetting that documentation and ownership gaps are quality gates, not safety blockers.

## Self-Check

1. Which dimensions block a pattern outright and which only require fixes?
2. When does a high-risk pattern pass instead of needing review?
3. How would you add a sixth dimension such as performance evidence?

