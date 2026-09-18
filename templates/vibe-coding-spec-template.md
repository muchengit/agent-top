---
title: Vibe Coding Spec Template
i18n-key: vibe-coding-spec-template
last-synced: 2026-09-18
validated_date: 2026-09-18
---

# Vibe Coding Spec

Fill this in before writing a prompt. If a field is empty, you are still exploring — do research first.

## Goal

What must be true after the change? State it in one sentence.

## Scope

- In scope:
- Out of scope:

## Interface

- Inputs:
- Outputs:
- Error behavior:

## Acceptance

The exact check that must pass — the same command a reviewer would run:

```bash
# e.g. python3 -m unittest labs.lX.lab_name.test_lab
```

## Constraints

What must not break:

## Refine Notes

Paste the actual error and failing input, not "it does not work".

- Round 1 failure:
- Round 1 fix:
- Round 2 failure:
- Round 2 fix:

## Review Record

- Diff reviewed by:
- Unrelated changes reverted:
- Evidence kept (test / trace / eval):
