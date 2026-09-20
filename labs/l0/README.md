---
title: L0 Labs
capability_level: L0
validated_date: 2026-09-18
---

# L0 Labs


中文版：[`README.zh-CN.md`](README.zh-CN.md)

## Goal

Run the first LLM call and learn the basic request/response shape, prompt, system prompt, and context-window concepts without requiring an API key.

## Prerequisites

- Python 3.10+
- Basic Markdown and terminal comfort

## Labs in This Level

- [`first_llm_call`](first_llm_call/README.md): first LLM call shape and terminology with a deterministic test.

## Run

```bash
python -m unittest discover -s labs/l0 -p "test_*.py"
```

## Common Pitfalls

- Treating tokens as words. Tokens are model-specific chunks of text.
- Assuming one prompt always produces one deterministic answer.
- Forgetting that empty prompts can produce undefined or unsafe behavior.

## Self-Check

1. What is the role of a system prompt?
2. Why are tokens not the same as words?
3. What could go wrong if the prompt is empty?
