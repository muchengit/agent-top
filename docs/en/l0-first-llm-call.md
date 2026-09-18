---
title: L0 First LLM Call
validated_date: 2026-09-18
tested_against: "python 3.10+"
i18n-key: l0-first-llm-call
last-synced: 2026-09-18
---

# L0 First LLM Call

## Goal

Run your first LLM request/response cycle, understand what each part of the request means, and connect those concepts to the executable Lab in this repository.

## Prerequisites

- Python 3.10+
- Basic command line usage
- No API key required

## What You Should Learn

- A prompt is the instruction sent to the model.
- A system prompt defines the assistant's role and constraints.
- A response is generated text produced by the model.
- Tokens are not exactly words.
- The context window is the model's input budget.

## Why This Tutorial Uses a Fake Model

The real goal of L0 is to understand request shape, not to spend time on API setup. The Lab uses a deterministic fake model so you can run the same code locally, inspect the result, and learn the concept without credentials.

The fake model is intentionally simple:

```python
class FakeModel:
    def complete(self, system_prompt: str, prompt: str) -> str:
        if not prompt:
            return "No user prompt provided."
        return f"[{system_prompt}] I received {len(prompt.split())} prompt tokens: {prompt}"
```

This is not a real LLM. It is a teaching double that preserves the same idea: you send a system role and a user prompt, then you receive generated text.

## What a Model Request Looks Like

A minimal model call has three concepts:

1. **System prompt**: the assistant's role.
2. **User prompt**: the actual request.
3. **Response**: text returned by the model.

In the Lab, those concepts are represented by this function:

```python
def first_llm_call(
    system_prompt: str = "You are helpful.",
    prompt: str = "Explain agents simply.",
) -> str:
    model = FakeModel()
    return model.complete(system_prompt, prompt)
```

When you run it with the defaults, you should see:

```text
[You are helpful.] I received 3 prompt tokens: Explain agents simply.
```

## Step-by-Step Walkthrough

### 1. Install nothing extra

The L0 Lab uses only the Python standard library.

```bash
python --version
```

### 2. Run the Lab directly

```bash
python -m labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call
```

Expected output:

```text
[You are helpful.] I received 3 prompt tokens: Explain agents simply.
```

### 3. Change the prompt

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(prompt="hello world"))
PY
```

Expected output:

```text
[You are helpful.] I received 2 prompt tokens: hello world
```

### 4. Change the system prompt

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(system_prompt="You are concise.", prompt="hello"))
PY
```

Expected output:

```text
[You are concise.] I received 1 prompt tokens: hello
```

### 5. Test the empty-prompt guardrail

```bash
python - <<'PY'
from labs.l0.first_llm_call.agent_top_labs_l0_first_llm_call import first_llm_call
print(first_llm_call(prompt=""))
PY
```

Expected output:

```text
No user prompt provided.
```

## What Do Tokens Mean?

The Lab approximates tokens by splitting the prompt on whitespace:

```python
len(prompt.split())
```

In a real model, tokenization is more complex. English words can split into smaller pieces, punctuation can become its own token, and non-English languages often tokenize differently. But the key idea remains the same: **tokens are the unit the model counts, not the unit humans naturally count.**

That matters because:

- prompt length affects cost;
- prompt length affects latency;
- prompt length affects whether content fits inside the context window;
- prompt length affects what gets included or dropped from context.

## System Prompt vs User Prompt

The system prompt is the assistant role. It defines the behavior frame.

The user prompt is the current instruction. It defines what the assistant should do right now.

For example:

```text
System prompt: You are helpful.
User prompt: Explain agents simply.
```

Changing the system prompt changes the role. Changing the user prompt changes the task.

## Context Window

A context window is the total amount of text the model can consider for one request. It includes:

- system prompt;
- user prompt;
- any retrieved documents;
- any tool results;
- any assistant output that remains in context.

The L0 Lab does not model a context limit, but production systems need one. Too much context can increase cost, slow responses, or hide important instructions.

## Run the Tests

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

Expected result:

```text
Ran 2 tests in 0.00Xs

OK
```

## Common Mistakes

- Treating token counts as word counts.
- Sending an empty prompt and assuming the model will infer intent.
- Assuming every LLM response is deterministic.
- Confusing the system prompt with the user prompt.
- Forgetting that the context window is shared by all text in the request.

## Self-Check

1. What is the role of the system prompt?
2. Why is `len(prompt.split())` only an approximation of token count?
3. What happens in the Lab when the prompt is empty?
4. What should happen in a real production app when the prompt is empty?
5. Why does context window size matter for cost and latency?

## Related Lab

Run the full executable Lab:

```bash
python -m unittest labs.l0.first_llm_call.test_lab
```

Read the Lab README: [`../../labs/l0/first_llm_call/README.md`](../../labs/l0/first_llm_call/README.md).

## Next Step

Continue with [`L1 Minimal ReAct Agent`](l1-minimal-react-agent.md) to build a tiny Agent loop without a framework.

## Interview Questions

Reinforce L0 concepts with the baseline question bank: [`L0 Baseline Questions`](interviews/questions/l0-basics.md).
