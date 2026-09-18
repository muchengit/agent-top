---
title: Multilingual Support
capability_level: Example
validated_date: 2026-09-18
tested_against: "routing and fallback drill over synthetic language events"
---

# Multilingual Support Exercise

This exercise uses fictional multilingual customer-service sessions. No API key, translation service, or external connector is needed.

Goal: decide how to route a request to the right language pipeline, keep cross-language memory consistent, and fall back safely when a language is unsupported or low-confidence.

## Files

- [`routing-decisions.jsonl`](routing-decisions.jsonl): language routing decisions with confidence, fallback, and refusal outcomes.
- [`memory-events.jsonl`](memory-events.jsonl): cross-language memory read/write events and consistency checks.

## JSONL Shape

Each line is one JSON object with a stable `event`, `trace_id`, `locale`, `detected_language`, `confidence`, `supported`, `memory_scope`, `decision`, and `next_action`. Optional fields such as `fallback_language` and `refusal_reason` appear only when relevant.

## Steps

1. Read each routing decision.
2. Identify whether the detected language is supported and the confidence is high enough to proceed.
3. Decide the next action: `route`, `fallback`, `clarify`, `refuse`, or `escalate`.
4. For memory events, check that cross-language entries use the same memory scope and do not overwrite one another.
5. Add one missing field for each blocked or refused event.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Low-confidence language detection | routing | clarify + fallback |
| Unsupported language without fallback | routing | refuse + escalate |
| Memory write in a different scope than the read | memory | align scope + re-verify |
| Cross-language duplicate without conflict resolution | memory | dedupe + reconcile |

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root. To practice a different policy, change one routing rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Language routing is a release decision when it changes model, memory, or refusal behavior.
- Cross-language memory needs a stable scope so users do not lose context when switching languages.
- Unsupported languages need an explicit fallback or refusal, never a silent wrong-language reply.
