---
title: Agent Evaluation Checklist
validated_date: 2026-09-16
---

# Agent Evaluation Checklist

Evals are the release gate for Agent behavior. They should prove correctness, safety, tool usage, retrieval quality, latency, and cost before rollout.

## Required Eval Categories

### Golden Prompts

- Same user request should produce acceptable behavior across model or prompt changes.
- Include examples for answer, clarification, refusal, and tool use.

### Tool Usage

- Correct tool selected.
- Required parameters present.
- Invalid parameters rejected.
- Dangerous tools require confirmation.
- Tool failures are handled explicitly.

### Retrieval

- Correct source is retrieved.
- Irrelevant source is not overused.
- Stale document is detected or refused.
- No-answer case is handled.

### Safety

- Prompt injection is rejected or contained.
- Out-of-scope request is refused.
- Sensitive data is not leaked.
- Destructive action is blocked without approval.

### Memory

- Relevant preference is used.
- Stale preference is not trusted blindly.
- Sensitive data is not stored when prohibited.
- Memory conflicts with user instruction are resolved safely.

### Observability

- Trace includes request id, prompt version, tool calls, retrieved sources, and final answer.
- Latency and token cost are captured.
- Failure reason is distinguishable from empty answer.

### Performance

- Latency p50 and p95 stay within budget.
- Cost per task stays within budget.
- Tool timeout budget is defined.
- Retry budget is defined.

## Regression Triggers

Re-run evals when any of these change:

- Prompt.
- Model version.
- Tool schema.
- Retrieval index or source.
- Memory policy.
- Safety guardrail.
- Router or orchestrator.
- Evaluation harness itself.

## Release Gate Policy

Block release when:

- A critical safety eval fails.
- A golden prompt fails on required user journey.
- Tool usage produces destructive action without approval.
- A required trace field is missing.
- Rollback plan is missing.
- Cost or latency exceeds threshold without approval.

Temporary exceptions require:

- Named owner.
- Written expiry date.
- Reason for exception.
- Monitoring plan.

## Reporting Template

```markdown
# Eval Report

## Scope
What changed?

## Dataset
Number of cases and categories.

## Results
- Correctness:
- Safety:
- Tool usage:
- Retrieval:
- Latency:
- Cost:

## Failures
- Failure class:
- Example:
- Root cause:
- Action item:

## Decision
Ship / block / canary / rollback.
```

## Good Eval Practices

- Keep negative cases.
- Keep stale-context cases.
- Keep destructive-action cases.
- Keep ambiguous user requests.
- Track eval drift over time.
- Make eval failures actionable.
