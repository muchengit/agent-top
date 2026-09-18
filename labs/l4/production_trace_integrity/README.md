---
title: L4 Lab: Production Trace Integrity
capability_level: L4
validated_date: 2026-09-18
tested_against: "python 3.10+"
---

# L4 Lab: Production Trace Integrity

## Goal

Build a deterministic validator that checks production observability traces for structural integrity: grouping events by trace id, requiring prompt start and result end events, enforcing monotonic timestamps, validating required fields on key events, and producing a structured issue report.

## Prerequisites

- L3: end-to-end RAG, memory, and multi-agent flows
- Python 3.10+
- Basic familiarity with tracing and observability event schemas

## Run

```bash
python -m unittest labs.l4.production_trace_integrity.test_lab
```

## Common Pitfalls

- Treating missing prompt or result events as non-blocking; every trace must start with a prompt and end with a result.
- Checking timestamps by sorting instead of stream order; out-of-order events must be flagged in arrival order.
- Forgetting that tool_call events require both a tool name and arguments.
- Counting orphan events (missing trace id) as traces; they cannot be grouped and must be flagged separately.

## Self-Check

1. When is a trace "broken" versus "complete"?
2. Why must timestamp checks follow stream order rather than sorted order?
3. How would you extend required-field checks to decision events?
