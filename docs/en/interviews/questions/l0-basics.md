---
title: L0 Baseline Questions
validated_date: 2026-09-17
i18n-key: interviews-questions-l0-basics
last-synced: 2026-09-17
---

# L0 Baseline Questions

These questions screen the baseline concepts needed before any Agent loop, tool call, or framework decision.

## Questions

### 1. What is the difference between a prompt and a system instruction?

Listen for:

- A prompt is the user-visible request or task.
- A system instruction sets role, constraints, output shape, and safety boundaries.
- The candidate can give a small example.

Good answer points:

- System instructions should be stable across turns.
- Prompts can vary by user and task.
- A good answer names one failure mode from mixing them, such as leaking constraints or weakening safety.

### 2. Why does context window size matter?

Listen for:

- Context is a finite budget for instructions, history, tool results, and generated output.
- Larger context does not remove latency, cost, or irrelevant-noise risk.
- Candidate can connect context limits to prompt trimming, summarization, and retrieval.

Good answer points:

- Explain what gets evicted or summarized.
- Explain how overflow shows up in practice.
- Mention that relevant evidence should be closer to the task when possible.

### 3. Explain tokenization in plain language.

Listen for:

- Candidate can explain that text is split into model tokens, not always words.
- They know tokens affect cost, latency, and length limits.
- They can explain why counting characters is not the same as counting tokens.

Good answer points:

- Example with punctuation, code, or multilingual text.
- Tie token cost to prompt length and retry cost.
- Mention rough budgeting before exact provider math.

### 4. What makes a good Agent system prompt?

Listen for:

- Clear task boundary.
- Output format or stop condition.
- Tool-use policy.
- Safety and escalation rules.

Good answer points:

- Includes refusal or escalation behavior.
- Includes an example or output contract.
- Avoids hidden assumptions and overlong instructions.

### 5. How do you debug a bad LLM response?

Listen for:

- Candidate separates prompt, context, model, tool result, and parsing layers.
- They ask for logs, trace, sample input, and expected output.
- They do not jump straight to “change the model.”

Good answer points:

- Start with one failing example.
- Compare expected vs actual output.
- Propose a minimal reproducible case before broader tuning.

### 6. When should an Agent answer directly instead of using a tool?

Listen for:

- Candidate checks whether the request needs live data, external action, or authority.
- They recognize ambiguity and risk.
- They mention when direct answers can still be okay.

Good answer points:

- Direct answer for stable facts or clarification.
- Tool call for current facts, permissions, or writes.
- Escalate when the user needs certainty or safety review.

### 7. What is the difference between model output and final user response?

Listen for:

- Candidate knows raw model output may be transformed by post-processing.
- They can mention validation, formatting, redaction, or citation enrichment.
- They separate reasoning text from final answer.

Good answer points:

- Final response can add citations or strip unsafe text.
- Tool output may be summarized or normalized.
- Trace should preserve both raw and final answer when debugging.

## Follow-Up Bank

- Ask for one concrete example of a prompt that was too vague.
- Ask for one example of a prompt that was too strict.
- Ask how they would reduce token cost without losing answer quality.
- Ask what they would inspect first if a response changes after a small prompt edit.
- Ask how they would explain context limits to a non-technical teammate.

## Common Red Flags

- Treats context window as unlimited.
- Cannot tell prompt, system instruction, and tool result apart.
- Assumes token count equals character count.
- Jumps to model choice without examining prompt or context first.
- Gives a polished definition but no debugging path.

## Portfolio Evidence

For L0, acceptable evidence is:

- A short prompt rewrite with before/after notes.
- A one-page explanation of context limits and trade-offs.
- A tiny trace showing input, context, tool result, and final response.
