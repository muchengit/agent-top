---
title: What Is Vibe Coding?
validated_date: 2026-09-18
i18n-key: vibe-coding-what-is
last-synced: 2026-09-18
---

# What Is Vibe Coding?

## Definition

Vibe coding is a style of software development where the developer works with an AI assistant through natural-language instructions and fast iterations: prompt, read the diff, run the checks, refine. The model writes most of the first draft; the developer owns the goal, the review, and the verification.

## What It Is Not

- It is not "type a wish and ship it."
- It is not a license to skip tests, lint, or evidence.
- It is not a replacement for understanding your system.
- It is not only for prototypes; the same loop scales to production changes when the acceptance bar is explicit.

## The Core Loop

1. **Specify**: write the goal, inputs, outputs, and acceptance check in one or two sentences.
2. **Generate**: let the assistant produce the first draft or a concrete patch.
3. **Review**: read the diff as if a stranger wrote it. Check scope, assumptions, and hidden side effects.
4. **Run**: execute the deterministic checks (unit tests, compile, lint, smoke).
5. **Refine**: iterate on failures with targeted prompts, not vague ones.
6. **Record**: keep the evidence — tests, traces, evals — so the result is reviewable later.

## Why It Works

- Removes typing friction and boilerplate, so energy goes to design and review.
- Makes the inner loop (write -> run -> fix) short enough to explore alternatives.
- Produces a reviewable diff, which is the same artifact a senior engineer would ask for.

## Why It Fails

- When the spec is vague, the loop degrades into random mutation.
- When verification is missing, "looks plausible" replaces "proven."
- When the developer stops reading the diff, the assistant's confident mistakes become the product's bugs.

## Relationship to Agent-Top

Agent-Top's Labs and Examples are deterministic and runnable. Vibe coding fits as the workflow used to build and extend them: the acceptance bar (tests pass, links valid, bilingual mirrors in sync) does not change.
