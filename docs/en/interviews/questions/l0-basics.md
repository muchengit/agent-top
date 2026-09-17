---
title: L0 Baseline Questions
validated_date: 2026-09-17
i18n-key: interviews-questions-l0-basics
last-synced: 2026-09-17
---

# L0 Baseline Questions

These questions screen the baseline concepts needed before any Agent loop, tool call, or framework decision.

## Question Bank

Four question types are covered: concept, implementation, debugging, and design.

### Concept

#### 1. What is the difference between a prompt and a system instruction?

**Answer points:**

- A prompt is the user-visible request or task; a system instruction sets role, constraints, output shape, and safety boundaries.
- System instructions should be stable across turns; prompts vary by user and task.
- A good answer names one failure mode from mixing them, such as leaking constraints or weakening safety.

**What the interviewer wants to hear:**

- Trade-off: keeping system behavior fixed makes debugging easier but rigid; letting prompts override system rules gives flexibility at the cost of safety.
- Production counterexample: copying a customer request verbatim into the system slot lets user-controlled text override your policy — prompt injection by accident.
- Data thinking: track how often a response violates format after a system prompt change; a 2-point format-failure jump after a wording edit is a signal, not noise.

**Bonus / Common mistakes:**

- Bonus: propose separating invariant rules (system) from task-specific instructions (user) and testing both independently.
- Mistake: claiming system instructions are "more important" than prompts; they are different layers with different trust and update cadence.

#### 2. Why does context window size matter?

**Answer points:**

- Context is a finite budget for instructions, history, tool results, and generated output.
- Larger context does not remove latency, cost, or irrelevant-noise risk; it shifts the trade-off.
- Overflow shows up as eviction, summarization, or degraded attention on the parts that matter.

**What the interviewer wants to hear:**

- Trade-off: bigger windows reduce truncation but increase cost per turn and often dilute attention, so retrieval and trimming still matter.
- Production counterexample: a 200k-token window filled with 180k tokens of stale logs produces worse answers than a trimmed 4k-token prompt with the relevant lines.
- Data thinking: measure effective context usage per turn; if your median request fills 90% of the window, the problem is retrieval, not the window size.

**Bonus / Common mistakes:**

- Bonus: mention "lost in the middle" degradation and putting critical evidence near the start or end of the context.
- Mistake: treating the context window as free memory and stuffing everything in "because it fits."

#### 3. Explain tokenization in plain language.

**Answer points:**

- Text is split into model tokens, not always words; punctuation, code, and multilingual text tokenize unevenly.
- Tokens drive cost, latency, and length limits; counting characters is not counting tokens.
- Do rough budgeting before exact provider math: a mental model of roughly 4 characters per token, then verify with the real tokenizer.

**What the interviewer wants to hear:**

- Trade-off: tokenizer efficiency varies by language; "I" is one token but a CJK character can be one or more, changing cost ratios across locales.
- Production counterexample: a Chinese-plus-English mixed prompt costs noticeably more than the same content in one language, and an emoji-heavy string can burn dozens of tokens.
- Data thinking: log token counts alongside request metadata so cost regressions are visible per feature, not only in the aggregate bill.

**Bonus / Common mistakes:**

- Bonus: mention that retries multiply token cost, so a 5% failure rate on a token-heavy flow is a measurable budget line.
- Mistake: quoting a fixed character-to-token ratio as if it were universal.

#### 4. What makes a good Agent system prompt?

**Answer points:**

- Clear task boundary, output format or stop condition, tool-use policy, and safety and escalation rules.
- Includes refusal or escalation behavior and an example or output contract.
- Avoids hidden assumptions and overlong instructions.

**What the interviewer wants to hear:**

- Trade-off: more instructions reduce ambiguity but consume context and can over-constrain the model; each added rule should earn its tokens.
- Production counterexample: a 3,000-token system prompt describing the whole company got worse tool-selection accuracy than a 300-token prompt with an explicit "when to call which tool" table.
- Data thinking: treat the system prompt as a hypothesis; A/B test prompt variants against a held-out eval set before shipping.

**Bonus / Common mistakes:**

- Bonus: version the system prompt and tie it to eval scores so changes are auditable.
- Mistake: writing a giant prompt "just in case" without measuring whether each rule changes behavior.

#### 5. What is the difference between model output and final user response?

**Answer points:**

- Raw model output may be transformed by post-processing: validation, formatting, redaction, or citation enrichment.
- Reasoning text must be separated from the final answer; tool output may be summarized or normalized.
- A trace should preserve both raw and final answer when debugging.

**What the interviewer wants to hear:**

- Trade-off: post-processing improves safety and consistency but adds latency and can hide model drift inside the pipeline.
- Production counterexample: a citation filter silently dropped the only correct source for a week before someone diffed raw vs final outputs and found the bug.
- Data thinking: sample a percentage of turns and measure the transformation rate (how often the final response differs from raw) to detect drift early.

**Bonus / Common mistakes:**

- Bonus: log a stable correlation ID that links raw output, final response, and tool results in one trace.
- Mistake: treating the model output and the user response as the same artifact and debugging the wrong layer.

### Implementation

#### 6. How do you debug a bad LLM response?

**Answer points:**

- Separate prompt, context, model, tool result, and parsing layers before changing anything.
- Start from logs, trace, sample input, and expected output; build a minimal reproducible case.
- Do not jump straight to "change the model."

**What the interviewer wants to hear:**

- Trade-off: a full trace is the fastest diagnosis but costs storage; sample tracing balances cost with debuggability.
- Production counterexample: a "hallucinating" answer was actually a stale cached tool result merged into context; the model was fine.
- Data thinking: classify failures by layer over a week of samples; if 70% are parsing errors, no model change will help.

**Bonus / Common mistakes:**

- Bonus: bisect by replaying the exact context with the same model and temperature to isolate nondeterminism.
- Mistake: tweaking the prompt without capturing the failing input, so the fix cannot be verified or regression-tested.

#### 7. When should an Agent answer directly instead of using a tool?

**Answer points:**

- Check whether the request needs live data, external action, or authority; stable facts or clarification can be answered directly.
- Tool calls are for current facts, permissions, or writes; escalate when the user needs certainty or safety review.
- Ambiguity and risk determine the default, not the feature name.

**What the interviewer wants to hear:**

- Trade-off: direct answers are cheap and fast but can go stale; tool calls are correct but add latency, cost, and failure surface.
- Production counterexample: an internal FAQ bot answered a salary question from memory to save a tool call and gave last year's number.
- Data thinking: track staleness windows per knowledge domain and route to tools when the last refresh exceeds the domain's freshness budget.

**Bonus / Common mistakes:**

- Bonus: define a "freshness policy" per data domain instead of a blanket tool-or-no-tool rule.
- Mistake: calling a tool for every request to look diligent, ignoring cost and latency.

#### 8. How do you make an LLM response deterministic enough for production tests?

**Answer points:**

- Set temperature to 0 for classification or parsing tasks where one answer is correct.
- Fix the prompt and context; freeze model and provider versions in tests.
- Use structured output or constrained decoding when available.

**What the interviewer wants to hear:**

- Trade-off: temperature 0 reduces variance but does not guarantee determinism across versions, kernels, or batching; it changes the distribution, not the dice.
- Production counterexample: two retries of the same request returned different JSON keys even at temperature 0 because the prompt had an underspecified output contract.
- Data thinking: run the same eval set N times and measure the edit distance between runs to quantify real variance before trusting a test.

**Bonus / Common mistakes:**

- Bonus: separate "must be exact" (JSON keys, tool names) from "can vary" (summaries) and apply different assertions to each.
- Mistake: asserting exact string equality on free-form prose and blaming the model for flaky CI.

### Debugging

#### 9. The Agent loop stops after one bad step. How do you debug it?

**Answer points:**

- Inspect the last model call: was the tool result malformed, the schema rejected, or the stop condition misconfigured?
- Replay the step with the exact context and trace the decision point.
- Check whether the failure is a parsing issue, a tool error, or a policy-based stop.

**What the interviewer wants to hear:**

- Trade-off: failing fast makes errors visible but can abort recoverable flows; retry policies trade latency for resilience.
- Production counterexample: a loop "stopped" because the model emitted a valid action with a trailing newline that a strict regex rejected; the fix was tolerant parsing.
- Data thinking: count stop reasons (completed, error, max steps, safety) per session to see which stop reason dominates.

**Bonus / Common mistakes:**

- Bonus: add a step-by-step replay tool that feeds the exact context back into the model for offline debugging.
- Mistake: restarting the loop from scratch and hoping it works instead of reproducing the failing step.

### Design

#### 10. Design a prompt-and-context strategy that keeps quality high as the conversation grows.

**Answer points:**

- Keep the system prompt small and stable; grow only the working memory that matters.
- Summarize or trim old turns, and move important facts into a structured state slot.
- Put the current task and most relevant evidence near the edges of the context.

**What the interviewer wants to hear:**

- Trade-off: full history preserves fidelity but costs tokens and dilutes attention; summarization loses detail but stays cheap and focused.
- Production counterexample: a long-running research assistant kept every turn, and accuracy dropped; switching to rolling summaries plus a "key facts" slot restored quality.
- Data thinking: measure quality on long conversations separately from short ones; a single average hides the degradation curve.

**Bonus / Common mistakes:**

- Bonus: define explicit eviction rules (age, importance, irrelevance) instead of "keep everything."
- Mistake: assuming a bigger model with a bigger window removes the need for context design.

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
