---
title: Multi-Round Research Discussion Lab
capability_level: L3
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L3 Lab: Multi-Round Research Discussion

## Goal

Practice a multi-round research and discussion workflow: plan a search, select evidence, ask for clarification, and decide when to answer.

## Prerequisites

- L3 RAG, memory, and observability concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l3.multi_round_research_discussion.test_lab
```

## Workflow

1. Clarify the question when the user request is ambiguous.
2. Search and rank candidate sources by relevance, freshness, and trust.
3. Select only evidence-bearing sources.
4. Ask the user or search again when evidence is stale or missing.
5. Answer only when the evidence is sufficient.

## What This Lab Teaches

- A discussion is not just multiple LLM calls; it is evidence management.
- Freshness and trust are part of source ranking.
- Refusal and clarification are valid outcomes.

## Common Pitfalls

- Treating the first retrieved result as sufficient.
- Answering before clarifying a vague question.
- Ignoring stale evidence.
- Mixing retrieval confidence with answer correctness.

## Self-Check

1. Why should freshness affect source priority?
2. When should the system ask the user for clarification?
3. How would you add citation quality to this lab?
