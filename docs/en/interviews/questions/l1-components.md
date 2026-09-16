---
title: L1 Component Questions
validated_date: 2026-09-16
i18n-key: interviews-questions-l1-components
last-synced: 2026-09-16
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

Follow-up:

- What should happen when the step limit is reached: fail, clarify, summarize, or escalate?

## 3. What belongs in short-term versus long-term memory?

Expected answer:

- Short-term memory stores current conversation and task state.
- Long-term memory stores durable facts, preferences, or policies.
- Long-term memory must be scoped, stale-checked, and privacy-sensitive.

Listen for:

- Privacy awareness.
- Understanding that memory can be wrong or stale.
- Separation between retrieval evidence and user profile.

Follow-up:

- How do you avoid storing sensitive data in memory?

## 4. When should an Agent answer directly versus call a tool?

Expected answer:

- Answer directly when context is sufficient and no external side effect is needed.
- Call a tool when facts, permissions, state, or side effects require an external source.
- Ask for clarification when the request is ambiguous or risky.

Listen for:

- Side-effect awareness.
- Safety and permission boundaries.
- Cost and latency trade-off.

Follow-up:

- How do you prevent an Agent from using a tool when it only has stale retrieved context?
