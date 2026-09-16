---
title: L1 Component Questions
validated_date: 2026-09-16
---

# L1 Component Questions

## 1. Explain the four core Agent components.

Expected answer:

- Perception turns input, tools, and observations into context.
- Planning decides what to try next.
- Tool use executes external actions.
- Memory preserves context across steps or sessions.

Listen for:

- Clear separation between components.
- Awareness of how failures propagate.
- Example that grounds each component.

Follow-up:

- What breaks if tool feedback is ambiguous?

## 2. Why use a max step limit in ReAct?

Expected answer:

- Prevents infinite loops.
- Bounds latency and cost.
- Makes failure visible and debuggable.

Listen for:

- Production thinking.
- Awareness of stop conditions.
