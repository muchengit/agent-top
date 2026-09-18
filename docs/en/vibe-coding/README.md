---
title: Vibe Coding Guide
validated_date: 2026-09-18
i18n-key: vibe-coding-readme
last-synced: 2026-09-18
---

# Vibe Coding Guide

Vibe Coding is an AI-assisted workflow where the developer expresses intent in natural language, lets a model generate the first draft, and then reviews, runs, and refines it in a fast feedback loop. The label "vibe" is about removing friction from typing, not about removing engineering judgment.

This section is the reference for using Vibe Coding inside Agent-Top without losing determinism, evidence, or production judgment.

## Start Here

- Introduction: [What Is Vibe Coding?](what-is-vibe-coding.md)
- Method: [Spec-First Workflow](spec-first-workflow.md)
- Verification: [Run and Verify](run-and-verify.md)
- Guardrails: [Common Pitfalls](common-pitfalls.md)

## How It Maps to Agent-Top

- L0-L2: use vibe coding to explore framework APIs and small single-agent Labs, always with a runnable test.
- L3-L4: apply the spec-first workflow to system design, RAG, observability, and production gates.
- L5: treat each vibe-coded artifact as an evidence bundle with `validated_date` and `tested_against`.
- Examples and Labs stay deterministic and API-key-free; vibe coding changes how you write them, not the acceptance bar.

## The One-Sentence Rule

If you cannot state the goal, the interface, and the acceptance check in one sentence, you are not ready to prompt — you are still exploring. That is fine, but it is not yet vibe coding; it is research.
## Hands-On Lab

- [`labs/l5/vibe_coding_spec`](../../../labs/l5/vibe_coding_spec/README.md): a deterministic Lab that encodes the one-sentence rule as checks. Run it with:

```bash
python3 -m unittest labs.l5.vibe_coding_spec.test_lab
```

- Printable spec form: [`Vibe Coding Spec Template`](../../../templates/vibe-coding-spec-template.md) (中文镜像：[`VibeCoding规范模板.md`](../../../templates/VibeCoding规范模板.md)).
