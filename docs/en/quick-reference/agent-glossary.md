---
title: Agent Glossary
validated_date: 2026-09-17
i18n-key: quick-reference-agent-glossary
last-synced: 2026-09-17
---

# Agent Glossary

Use this glossary when choosing terms for docs, Labs, interviews, and production incidents.
Each entry includes a one-sentence definition, why it matters, and the most common misuse
to avoid. Terms are grouped as Foundation, Production, and Decision terms.

## Foundation Terms

### Agent

- **Definition**: A system that uses an LLM, tools, memory, planning, and control loops to complete tasks.
- **Why it matters**: The Agent is the unit of deployment, evaluation, and incident review, so its boundaries define what you test and monitor.
- **Common misuse**: Calling any single LLM call an "Agent". A real Agent requires a loop, tools, or memory; a single call is just an LLM call.

### LLM

- **Definition**: The language model that generates text and reasoning inside the Agent.
- **Why it matters**: The LLM is a component, not the whole system; orchestration, tools, and evals determine reliability.
- **Common misuse**: Treating model quality as the only quality lever and ignoring retrieval, tool, and guardrail failures.

### Perception

- **Definition**: Turning user input, tool results, and retrieved context into usable state.
- **Why it matters**: Bad perception produces wrong plans even with a good model.
- **Common misuse**: Confusing perception with the raw prompt text instead of the parsed and typed state the planner actually uses.

### Planning

- **Definition**: Deciding the next action or reasoning step.
- **Why it matters**: Planning quality decides how many wasted or risky steps occur before completion.
- **Common misuse**: Treating planning as a single prompt instead of a structured decision with stop conditions and budgets.

### Action

- **Definition**: A tool call, retrieval request, message, or other system effect.
- **Why it matters**: Every action is a side effect that must be typed, permitted, and auditable.
- **Common misuse**: Using free-text actions that cannot be validated, permission-checked, or logged.

### Observation

- **Definition**: Evidence returned from a tool, retrieval, model, or environment.
- **Why it matters**: Observations drive the next planning step and must be trusted carefully.
- **Common misuse**: Believing tool output without checking status, format, or freshness.

### Control loop

- **Definition**: The cycle of perceive-plan-act-observe that keeps an Agent on task.
- **Why it matters**: It bounds how long the Agent runs and when it stops.
- **Common misuse**: Letting the loop run with no maximum steps or stop condition.

### Tool

- **Definition**: An external function or action with typed inputs and outputs.
- **Why it matters**: Typed contracts make calls safe, testable, and auditable.
- **Common misuse**: Exposing raw functions without validation, permissions, or error contracts.

### MCP

- **Definition**: A standard protocol for connecting LLM apps to MCP servers that expose tools, resources, prompts, schemas, and context.
- **Why it matters**: It standardizes tool integration and reduces bespoke glue code.
- **Common misuse**: Assuming MCP replaces evals, guardrails, or authentication.

### RAG

- **Definition**: Retrieval-augmented generation using retrieved sources.
- **Why it matters**: It grounds answers in current or private evidence.
- **Common misuse**: Calling any search-augmented call "RAG" without citations or a retrieval eval.

### Memory

- **Definition**: Context stored across turns or sessions.
- **Why it matters**: It makes multi-turn and multi-session behavior possible.
- **Common misuse**: Storing raw transcripts forever without retention, privacy, or summarization policy.

### Context window

- **Definition**: The maximum token span the model can attend to in one call.
- **Why it matters**: It limits how much retrieved and conversational context fits in a single request.
- **Common misuse**: Confusing context window with long-term memory.

### Embedding

- **Definition**: A dense vector representation of text used for similarity search.
- **Why it matters**: It powers semantic retrieval quality.
- **Common misuse**: Assuming a higher embedding dimension always means better retrieval.

### Retriever

- **Definition**: The component that selects candidate documents for a prompt.
- **Why it matters**: It decides recall before the model ever sees the context.
- **Common misuse**: Optimizing only the generator and ignoring retrieval failures.

### Guardrail

- **Definition**: A rule that prevents unsafe behavior.
- **Why it matters**: It turns policy into enforceable checks.
- **Common misuse**: Building guardrails only at the prompt level and skipping output checks.

### Eval

- **Definition**: A test that measures Agent behavior.
- **Why it matters**: It converts "it feels right" into a regression signal.
- **Common misuse**: Using a handful of happy-path examples and calling them an eval suite.

### Trace

- **Definition**: A record of prompts, tool calls, decisions, and outcomes.
- **Why it matters**: It is the raw material for debugging and postmortems.
- **Common misuse**: Logging only the final answer and losing the decision path.

### Rollback

- **Definition**: A path that restores known-safe behavior.
- **Why it matters**: It limits blast radius after a bad release.
- **Common misuse**: Believing a rollback exists without rehearsing it.

## Production Terms

### Contract

- **Definition**: A documented input/output/failure-mode agreement for an Agent or tool.
- **Why it matters**: It lets components change independently and tests run meaningfully.
- **Common misuse**: Documenting happy paths only and ignoring failure modes.

### Handoff

- **Definition**: Passing task state from one Agent or stage to another.
- **Why it matters**: It is the seam where context can be lost or leaked.
- **Common misuse**: Passing the whole transcript instead of a typed task state.

### Verifier

- **Definition**: A component or Agent that checks evidence and recommendations.
- **Why it matters**: It is the second set of eyes that catches hallucinated claims.
- **Common misuse**: Using the same model and prompt for both generation and verification.

### Supervisor

- **Definition**: An orchestrator that routes tasks to workers and enforces stop conditions.
- **Why it matters**: It centralizes policy, budget, and termination.
- **Common misuse**: Letting the supervisor become a bottleneck that re-plans every step.

### Human-in-the-loop

- **Definition**: A workflow where a human approves or reviews a risky step.
- **Why it matters**: It adds judgment where automation is not yet safe.
- **Common misuse**: Asking humans to approve every trivial step, which trains them to click through.

### Confidence

- **Definition**: The evidence strength behind an answer, not a substitute for verification.
- **Why it matters**: It helps route to confirmation or fallback.
- **Common misuse**: Treating a high confidence number as proof of correctness.

### Citation

- **Definition**: Evidence attached to a claim or answer.
- **Why it matters**: It makes claims checkable and audits possible.
- **Common misuse**: Attaching a source the model never actually used.

### Fallback

- **Definition**: A safe response when evidence, tool, or model behavior is insufficient.
- **Why it matters**: It keeps the user safe instead of forcing a best guess.
- **Common misuse**: Falling back to another ungrounded model answer.

### Idempotency

- **Definition**: Safe retry behavior for tools that may repeat effects.
- **Why it matters**: It prevents duplicate charges, emails, or writes on retry.
- **Common misuse**: Assuming all tools are naturally idempotent.

### Rate limit

- **Definition**: A cap on calls or tokens per time window.
- **Why it matters**: It protects cost and stability budgets.
- **Common misuse**: Treating rate limits as the only cost control.

### Timeout

- **Definition**: The maximum wait for a tool or model response.
- **Why it matters**: It keeps the loop from hanging forever.
- **Common misuse**: Setting a timeout but not a retry or fail-closed path.

### Regression Gate

- **Definition**: A release gate that blocks unsafe behavior from shipping.
- **Why it matters**: It makes safety a release property, not an aspiration.
- **Common misuse**: Gating on test count instead of behavior coverage.

### Blast Radius

- **Definition**: The range of users, data, or systems affected by a failure.
- **Why it matters**: It focuses design on containment and rollback.
- **Common misuse**: Ignoring third-party side effects such as emails or payments.

### Postmortem

- **Definition**: A blameless review that turns an incident into prevention actions.
- **Why it matters**: It turns failures into system improvements.
- **Common misuse**: Using postmortems to assign blame or to stop at "human error".

### Observability

- **Definition**: The ability to inspect live state: traces, metrics, and logs.
- **Why it matters**: It is how you debug production before users report it.
- **Common misuse**: Collecting logs that nobody can query or correlate.

### Audit log

- **Definition**: An append-only record of decisions and external effects.
- **Why it matters**: It provides accountability and incident reconstruction.
- **Common misuse**: Logging actions without the reasoning and tool results behind them.

## Decision Terms

### Fail closed

- **Definition**: Stop or refuse rather than continue with unsafe assumptions.
- **Why it matters**: It prevents wrong or harmful actions when evidence is missing.
- **Common misuse**: Failing closed on every uncertainty and blocking legitimate work.

### Trade-off

- **Definition**: An explicit comparison of accuracy, latency, cost, safety, and maintainability.
- **Why it matters**: It makes design choices reviewable.
- **Common misuse**: Hiding a cost or safety regression behind a latency win.

### Stable pattern

- **Definition**: A design idea that remains useful across frameworks.
- **Why it matters**: It keeps knowledge transferable between projects.
- **Common misuse**: Confusing a framework API with a pattern.

### Vibe Coding

- **Definition**: An AI-assisted workflow where you express intent in natural language, let a model draft, then review and run in a fast loop, with goal, interface, and acceptance stated before prompting.
- **Why it matters**: It removes typing friction without removing engineering judgment or the acceptance bar.
- **Common misuse**: Treating "vibe" as permission to skip specs, evals, or deterministic checks.

### Framework boundary

- **Definition**: Framework-specific API details that should stay isolated in Labs.
- **Why it matters**: It keeps pattern docs durable as frameworks evolve.
- **Common misuse**: Writing framework-specific docs and calling them framework-agnostic.

### Validated date

- **Definition**: The date when a doc or example was checked.
- **Why it matters**: It tells readers how fresh the guidance is.
- **Common misuse**: Updating the date without actually re-validating the content.

### Tested against

- **Definition**: The version or environment anchor for an executable example.
- **Why it matters**: It defines what the example is known to run on.
- **Common misuse**: Claiming "tested against" for code that was never executed.

## Review Questions

- Is every external action represented by a typed tool contract?
- Is there a verifier for evidence-heavy claims?
- Is there a refusal path when evidence is missing?
- Is there a rollback path for external side effects?
- Can this behavior be measured by an eval rather than guessed?
- Is the memory policy defined: what is stored, for how long, and who can read it?
- Is the failure mode fail closed, and is that path tested?
