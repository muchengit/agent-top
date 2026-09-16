---
title: RAG Evaluator Lab
capability_level: L3
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L3 Lab: RAG Evaluator

## Goal

Practice evaluating retrieval behavior with required sources and refusal cases.

## Prerequisites

- L3 RAG, memory, and observability concepts.
- Python 3.10+.

## Run

```bash
python -m unittest labs.l3.rag_evaluator.test_lab
```

## What This Lab Teaches

- Retrieval must be checked against required sources.
- Missing evidence can be handled by refusal.
- Eval cases need explicit expected behavior.

## Common Pitfalls

- Accepting any retrieved text as success.
- Forgetting no-answer cases.
- Confusing retrieval recall with final answer correctness.

## Self-Check

1. Why should a no-answer case be part of the eval set?
2. What is the difference between missing source and wrong source?
3. How would you extend this to measure citation quality?
