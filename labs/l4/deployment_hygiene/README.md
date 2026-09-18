---
title: Deployment Hygiene Lab
capability_level: L4
validated_date: 2026-09-18
i18n-key: l4-deployment-hygiene
last-synced: 2026-09-18
tested_against: "python 3.10+"
---

# L4 Lab: Deployment Hygiene

## Goal

Combine observability completeness, cost budget, and release gate checks into one deterministic deploy decision, with explicit reasons for deploy, defer, or block.

## Prerequisites

- L4 production systems concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l4.deployment_hygiene.test_lab
```

## What This Lab Teaches

- Deploy hygiene is one combined decision, not three separate opinions.
- Missing critical trace fields and unconfigured alerts block a deploy.
- Cost over budget only blocks when there is no rollback budget.

## Common Pitfalls

- Treating partial trace coverage as a hard block instead of a defer.
- Confusing missing rollback budget with cost over budget.
- Approving a deploy before alerts are configured.

## Self-Check

1. Which hygiene failure blocks immediately, and which only defers?
2. Why does a rollback budget change a cost decision?
3. How would you add latency p95 to this assessment?

## Bilingual Notes

The Chinese mirror lives at [`README.zh-CN.md`](README.zh-CN.md) with the same `i18n-key`. Keep both mirrors in sync when changing this lab.
