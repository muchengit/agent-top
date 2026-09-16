---
title: L2 Framework and MCP Questions
validated_date: 2026-09-16
---

# L2 Framework and MCP Questions

## 1. How do you choose between a graph orchestration framework and a lightweight SDK?

Expected answer:

- Use graph orchestration when state, cycles, checkpoints, and human review matter.
- Use a lightweight SDK when the flow is small, mostly linear, and easier to debug.
- Prefer the simplest framework that makes failure modes explicit.

Listen for:

- Framework choice tied to system shape.
- Awareness of debugging and observability.
- Avoidance of framework tribalism.

Follow-up:

- What framework feature would force you to choose LangGraph-style orchestration over a plain loop?

## 2. What is a good tool boundary for an Agent?

Expected answer:

- A tool should have one clear job.
- Inputs and outputs should be typed and validated.
- Side effects should be explicit.
- Errors should be distinguishable from empty results.
- Destructive actions need confirmation or approval.

Listen for:

- Safety first.
- Schema and validation discipline.
- Small, observable tools.

Follow-up:

- How do you handle a tool that returns a valid response but wrong data?

## 3. MCP server integration fails. How do you debug it?

Expected answer:

- Check server availability and transport.
- Check schema and capability discovery.
- Check auth and permissions.
- Inspect first tool call logs.
- Confirm whether failure is discovery, invocation, timeout, or output parsing.

Listen for:

- Layered debugging.
- Trace-first thinking.
- Clear distinction between protocol, permission, and application failure.

Follow-up:

- How would you make this failure visible in production?

## 4. Should every tool call be confirmed by a human?

Expected answer:

- Read-only tools can often be automated.
- Writes, payments, deletions, and policy-sensitive actions need confirmation, approval, or rollback.
- Risk should be classified by reversibility, blast radius, and user trust.

Listen for:

- Risk model.
- Reversibility awareness.
- Good defaults and clear exceptions.

Follow-up:

- What approval workflow would you design for a high-risk support action?
