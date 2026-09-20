---
title: L4 Labs
capability_level: L4
validated_date: 2026-09-18
---

# L4 Labs


中文版：[`README.zh-CN.md`](README.zh-CN.md)

## Goal

Productionize Agent systems with evaluation, safety, deployment, cost, and postmortems.

## Prerequisites

- L3: end-to-end RAG, memory, and multi-agent flows
- Python 3.10+
- Basic familiarity with release gates and observability contracts

## Labs in This Level

- [`production_postmortem`](production_postmortem/README.md): executable production postmortem structure, coverage checks, and action-item closure.
- [`regression_gate`](regression_gate/README.md): release gating for safety, trace, rollback, and cost.
- [`cost_and_stability_guardrails`](cost_and_stability_guardrails/README.md): runtime cost, latency, retry, and degradation guardrails.
- [`production_trace_integrity`](production_trace_integrity/README.md): deterministic trace integrity validation for production observability.
- [`deployment_hygiene`](deployment_hygiene/README.md): combined observability, cost, and release gate deploy decision.

## Run

```bash
python -m unittest discover -s labs/l4 -p "test_*.py"
```

## Common Pitfalls

- Deploying without a regression gate that checks safety, trace, rollback, and cost.
- Writing postmortems that describe symptoms without coverage or action-item closure.
- Ignoring degradation guardrails until a cost or latency incident occurs.

## Self-Check

1. What does a release gate verify before production deployment?
2. How do you prove a postmortem action item is closed?
3. Which guardrails protect cost and stability at runtime?

