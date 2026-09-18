---
title: Vibe Coding Spec Lab
capability_level: L5
validated_date: 2026-09-18
tested_against: "python 3.10+"
---

# L5 Lab: Vibe Coding Spec

## Goal

Practice turning a vague idea into a prompt-ready spec. The Lab encodes the Vibe Coding one-sentence rule as deterministic checks: a spec is ready only when goal, interface, and acceptance are all present.

## Prerequisites

- Read the [Vibe Coding guide](../../../docs/en/vibe-coding/README.md).
- Python 3.10+.

## Run

```bash
python3 -m unittest labs.l5.vibe_coding_spec.test_lab
```

Expected output:

```text
Ran 5 tests
OK
```

## What This Lab Teaches

- A prompt-ready spec needs goal, interface, and acceptance.
- Vague or empty fields fail closed instead of producing a "looks plausible" prompt.
- The acceptance field should name a runnable command a reviewer can re-run.

## Common Pitfalls

- Treating a topic sentence as a goal: a goal states what must be true after the change.
- Forgetting the acceptance command: "it should work" is not a check.
- Expanding scope after the check is green: stop at the smallest passing change.

## Self-Check

1. Can you restate goal, interface, and acceptance in one sentence?
2. Does your acceptance name a command a reviewer can run?
3. What do you do when a field is empty — prompt anyway, or research first?
