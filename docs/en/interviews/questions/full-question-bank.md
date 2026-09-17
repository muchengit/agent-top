---
title: L0-L5 Full Interview Question Bank
validated_date: 2026-09-17
i18n-key: interviews-questions-full-question-bank
last-synced: 2026-09-17
---

# L0-L5 Full Interview Question Bank

This is the compact all-level interview bank for Agent-Top. It includes one required question per level and keeps the same answer structure used across the question sets: question, expected answer, what to listen for, follow-up, and red flags.

## How To Use

- Use one question per level for a fast 30-45 minute screen.
- Use three questions for a serious technical review: one baseline, one system-level, one production or pattern question.
- Always ask candidates to explain trade-offs and failure modes, not just definitions.

## L0: Baseline Concepts

### Question

What is the difference between a prompt, a system instruction, and a tool result?

### Expected Answer

- A prompt is the user task or request.
- A system instruction sets role, policy, output shape, safety rules, and escalation behavior.
- A tool result is external evidence or state returned by a tool, and it still needs validation.

### Listen For

- Candidate separates user input, system control, and external evidence.
- Candidate recognizes that tool results can be stale, incomplete, malformed, or wrong.

### Follow-Up

If the same final answer changes after a one-token prompt edit, what do you inspect first?

### Red Flags

- Treats all model inputs as equivalent.
- Assumes tool output is always trustworthy.

## L1: Agent Components

### Question

Explain a minimal ReAct Agent and the stop conditions you would use.

### Expected Answer

- The Agent alternates between thinking/planning, acting through tools, and observing results.
- It should stop on success, max steps, repeated failure, ambiguous intent, policy violation, or escalation.
- Every step should be logged enough to debug later.

### Listen For

- Clear loop: state -> plan -> action -> observation -> next state.
- Awareness that unbounded loops cause cost, latency, and safety risk.

### Follow-Up

What should happen when the tool returns an ambiguous result?

### Red Flags

- Cannot explain why a step limit is needed.
- Treats ReAct as only a prompt template.

## L2: Framework and MCP

### Question

How would you design a tool boundary and MCP-style failure handling for a reliable single Agent?

### Expected Answer

- Tools should have one clear job, typed inputs, validated outputs, explicit permissions, and side-effect classification.
- MCP failures should be separated into discovery, auth, schema, invocation, timeout, and parsing failures.
- Destructive or irreversible actions need confirmation, audit logs, or rollback.

### Listen For

- Candidate thinks in risk classes, not just API calls.
- Candidate can give concrete logs and trace fields.

### Follow-Up

How do you prevent an Agent from making a destructive write based on stale retrieved context?

### Red Flags

- Confirms every tool call regardless of risk.
- Cannot distinguish permission failure from malformed output.

## L3: System Design

### Question

Design a customer support Agent with RAG, memory, tools, and human escalation.

### Expected Answer

- Start with intent, permissions, and trust boundaries.
- Use RAG for scoped policy/product knowledge, memory for durable user context, tools for order/ticket state, and escalation for unsafe or ambiguous actions.
- Define data ownership, citations, refusal behavior, evals, latency, and cost.

### Listen For

- Candidate decomposes requirements before architecture.
- Candidate explains how retrieval, memory, tool state, and human approval interact.

### Follow-Up

How do you know whether a wrong answer came from retrieval, memory, the model, or a tool?

### Red Flags

- Uses multi-agent orchestration without a reason.
- Forgets citations, refusal behavior, or tenant boundaries.

## L4: Production

### Question

A customer says the Agent changed the wrong account. Walk through your incident response.

### Expected Answer

- Freeze or disable the risky action path.
- Inspect trace, prompt, retrieved context, tool arguments, authorization, and final response.
- Identify root cause category: data, retrieval, model, tool schema, permission, or prompt policy.
- Add a regression eval, rollback path, and postmortem action with owner and due date.

### Listen For

- Candidate leads with safety and containment.
- Candidate connects incident response to prevention controls.

### Follow-Up

What eval should block the next release if this could happen again?

### Red Flags

- Blames the model first.
- Has no rollback or regression prevention step.

## L5: Expert Patterns and Impact

### Question

What makes a reusable Agent pattern worth contributing to Agent-Top or open source?

### Expected Answer

- It solves a repeated problem across projects.
- It has stable inputs/outputs, explicit failure modes, safety checks, and validation.
- It is easier to maintain than framework-specific code.
- It comes with a Lab, docs, evals or traces, and a migration/deprecation story.

### Listen For

- Candidate separates durable pattern from framework detail.
- Candidate mentions maintenance cost and contributor readiness.

### Follow-Up

What evidence would convince you the pattern should graduate from a Lab into a framework or standard?

### Red Flags

- Contribution is just a framework wrapper.
- No failure modes, docs, tests, or migration story.

## Grading

- 0: vague or memorized answer.
- 1: correct concept, but missing production trade-off or failure path.
- 2: answer includes system boundary, trade-off, measurement, rollback or prevention, and one concrete example.

Pass guidance:

- L0-L1 screen: no 0 scores on baseline or safety questions.
- L2-L4 technical interview: at least 80% of answers score 2.
- L5 expert review: pattern question scores 2 and candidate provides evidence beyond usage.
