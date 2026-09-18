---
title: Spec-First Workflow
validated_date: 2026-09-18
i18n-key: vibe-coding-spec-first
last-synced: 2026-09-18
---

# Spec-First Workflow

## Principle

Prompt quality is a direct function of spec quality. Write the spec before the prompt.

## A Good Spec Contains

- **Goal**: what should be true after the change.
- **Scope**: files or components in and out.
- **Interface**: inputs, outputs, and error behavior.
- **Acceptance**: the exact check that must pass.
- **Constraints**: what the change must not break.

## Example

Weak prompt:

> "Add a search endpoint."

Strong prompt:

> "Add a `GET /search?q=...` endpoint to the existing FastAPI app. It queries the vector store, returns up to 10 results with `{id, score, source}`, and returns `400` for an empty query. Acceptance: `pytest tests/api/test_search.py` passes and the trace includes the retrieval sources."

## Workflow Steps

1. **One sentence**: restate the goal in one sentence. If you cannot, research first.
2. **Write the spec**: fill the five fields above, even for a one-file change.
3. **Prompt the diff**: ask for a concrete patch, not a discussion.
4. **Review the diff**: verify scope matches the spec; reject unrelated changes.
5. **Run the acceptance check**: the same command a reviewer would run.
6. **Refine with evidence**: on failure, paste the actual error and the failing input, not "it does not work."
7. **Stop when green and small**: resist adding "just one more thing" after the check passes.

## When to Skip the Spec

- One-line typo fixes where the diff is self-evident.
- Mechanical renames with a compiler or formatter confirming them.

## When the Spec Is the Wrong Tool

- Open-ended research ("explore what patterns exist") — do this outside the change loop.
- Architecture decisions with no objective check — write a design note instead of a prompt.
## Template

Use the printable form: [`Vibe Coding Spec Template`](../../../templates/vibe-coding-spec-template.md) (中文镜像：[`VibeCoding规范模板.md`](../../../templates/VibeCoding规范模板.md)).
