---
title: ReAct Pattern
validated_date: 2026-09-16
---

# ReAct Pattern

ReAct interleaves reasoning and action.

A minimal loop:

1. Observe current state.
2. Think about the next step.
3. Call a tool if needed.
4. Observe tool result.
5. Repeat until the answer is complete.

## Trade-offs

- Simple and debuggable.
- Can loop if tool feedback is poor.
- Needs stop conditions and validation.
- Works best when tools are small, reliable, and observable.
