---
title: L5 Custom Patterns
validated_date: 2026-09-18
tested_against: "python 3.10+"
i18n-key: l5-custom-patterns
last-synced: 2026-09-18
---

# L5 Custom Patterns

## Goal

Design a reusable Agent pattern that has stable inputs, outputs, safety checks, verification, and clear failure modes. After the tutorial, package the work with [`tutorials/industry-benchmark-and-l5-expert-path.md`](tutorials/industry-benchmark-and-l5-expert-path.md) and [`../../templates/l5-expert-evidence-template.md`](../../templates/l5-expert-evidence-template.md).

## Why L5 Matters

L4 proves you can run production systems. L5 proves you can improve how other teams build systems.

An L5 contribution is not a bigger app. It is a smaller, repeatable pattern that others can adopt without copying fragile implementation details.

## Prerequisites

- L0 through L4 completed.
- You have seen at least one production-style Agent system.
- You can run the L5 Lab locally.
- Python 3.10+.

## What Counts as a Pattern

A pattern should answer these questions:

- What problem does it solve?
- What inputs does it require?
- What outputs does it guarantee?
- What checks run before execution?
- What verification happens after execution?
- How does it fail safely?
- Who can maintain it?

If a pattern cannot answer these questions, it is probably just project-specific code.

## Pattern Example: Verifiable Action

A useful L5 starting point is the `VerifiableActionPattern`. It turns an action request into a small plan before any side-effecting tool runs.

The pattern has three phases:

1. `clarify`: validate request shape and missing fields.
2. `execute`: call the tool through a controlled gateway.
3. `verify`: run an eval probe or verification step before reporting success.

The pattern stops before execution if a safety rule matches the request.

## Follow-Along

### Step 1: Inspect the Pattern Boundary

Read the Lab:

- [`../../labs/l5/custom_pattern_lab/README.md`](../../labs/l5/custom_pattern_lab/README.md)
- [`../../labs/l5/custom_pattern_lab/agent_top_labs_l5_custom_pattern_lab.py`](../../labs/l5/custom_pattern_lab/agent_top_labs_l5_custom_pattern_lab.py)

The Lab defines two result objects:

- `PlanStep(intent, tool, rollback_hint)`.
- `PatternResult(steps, stop_reason)`.

This is intentionally small. L5 patterns should be easy to reason about before they are powerful enough to become frameworks.

### Step 2: Run the Lab

From the repository root:

```bash
python -m unittest labs.l5.custom_pattern_lab.test_lab
```

Expected result:

```text
Ran 2 tests in ...
OK
```

The tests prove two important behaviors:

- Safe requests produce a three-step plan.
- Requests matching a safety rule stop with `blocked_by_safety_rule`.

### Step 3: Study the Safe Path

The safe path returns:

- `intent="clarify"`, `tool="validator"`, `rollback_hint="remove unclear fields"`.
- `intent="execute"`, `tool="tool_gateway"`, `rollback_hint="restore previous state"`.
- `intent="verify"`, `tool="eval_probe"`, `rollback_hint="disable path"`.

The key lesson is that execution is not enough. Every risky action needs a rollback hint and a verification step.

### Step 4: Study the Blocked Path

When a request contains a configured safety rule, the pattern returns:

```python
PatternResult((), "blocked_by_safety_rule")
```

This is important because blocking must happen before tool execution. A safety check after a destructive action is too late.

### Step 5: Define Your Own Pattern

Write a one-page pattern spec:

```markdown
# Pattern Name

## Problem
One sentence.

## Inputs
- Required input 1
- Required input 2

## Outputs
- Guaranteed output 1
- Failure output

## Safety Checks
- Check that runs before execution

## Execution
- Step 1
- Step 2

## Verification
- Verification after execution

## Failure Modes
- Failure mode and safe response

## When Not to Use
- Context where the pattern is a bad fit
```

A good pattern has boundaries. It should say when not to use it.

### Step 6: Validate the Pattern

Before sharing a pattern, run these checks:

- It works for at least two different examples.
- It has at least one blocked or failed path.
- It names the owner for each step.
- It includes rollback or safe degradation.
- It includes verification, not only generation.
- It can be maintained by a contributor who did not write it.

### Step 7: Prepare an Open-Source Contribution

To turn a pattern into an open-source contribution:

1. Add a Lab with deterministic tests.
2. Add a short tutorial with expected outputs.
3. Mark version anchors with `validated_date` and `tested_against`.
4. Avoid framework-specific code unless the pattern is explicitly framework-specific.
5. Include failure modes and common misuse.
6. Link the pattern to the L0–L5 capability model.

A contribution is ready for review when the reviewer can understand the pattern without reading private production code.

### Step 8: Run the Full Repository Checks

From the repository root:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

All checks should pass before proposing the pattern as documentation or Lab content.

## Common Mistakes

- Calling a framework wrapper a pattern.
- Naming the pattern before defining its boundaries.
- Hiding failure modes inside the happy path.
- Performing safety checks after execution.
- Requiring too much production context to understand.
- Leaving verification optional.
- Skipping examples where the pattern should not be used.

## Pattern Readiness Rubric

Score the pattern from 0 to 4:

- 0: One-off prompt or script.
- 1: Reusable idea, but no stable contract.
- 2: Has inputs, outputs, and one failure mode.
- 3: Has safety, verification, rollback, and tests.
- 4: Adopted by at least two examples, documented, tested, and maintainable.

A strong L5 artifact is usually at least a level 3 pattern.

## Self-Check

1. What are the stable boundaries of a reusable Agent pattern?
2. Why should safety checks run before execution?
3. How would another contributor maintain this pattern?
4. What evidence proves the pattern is reusable beyond one project?
5. When should a pattern become a framework instead of a pattern?

## Related Assets

- [`../../labs/l5/custom_pattern_lab/README.md`](../../labs/l5/custom_pattern_lab/README.md)
- [`../../templates/article-template.md`](../../templates/article-template.md)
- [`../../templates/lab-template.md`](../../templates/lab-template.md)
- [`portfolio/personal-agent-portfolio.md`](portfolio/personal-agent-portfolio.md)
- [`portfolio/open-source-impact-guide.md`](portfolio/open-source-impact-guide.md)
- [`agent-top-concrete-framework.md`](agent-top-concrete-framework.md)

## Interview Questions

Reinforce L5 concepts with the pattern question bank: [`L5 Pattern Questions`](interviews/questions/l5-patterns.md).
