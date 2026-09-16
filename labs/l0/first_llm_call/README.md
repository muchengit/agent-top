---
title: First LLM Call
capability_level: L0
validated_date: 2026-09-16
tested_against: "python 3.10+"
---

# L0 Lab: First LLM Call

## Goal

Understand the basic request/response shape of an LLM call without requiring an API key.

## Prerequisites

- Python 3.10+
- Basic comfort with Markdown and terminal commands

## Run

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

## What to Learn

- A model request includes a prompt.
- A response contains generated text.
- Tokens are not exactly equal to words.
- A system prompt sets the assistant role.
- Context window limits the total text the model can process.
