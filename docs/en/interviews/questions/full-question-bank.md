---
title: L0-L5 Deep Interview Question Bank
validated_date: 2026-09-17
i18n-key: interviews-questions-full-question-bank
last-synced: 2026-09-17
---

# L0-L5 Deep Interview Question Bank

This is the all-level deep interview bank for Agent-Top. Each level includes a primary question, detailed scoring, production-grade answer expectations, follow-ups, red flags, and optional evidence checks.

The bank is grounded in the stable public sources listed below, but the durable test is whether the candidate can explain the system boundary, failure mode, and trade-off.

## Source Anchors

- ReAct paper: reasoning and acting interleaved, tool/action feedback, and hallucination grounding via retrieval.
- MCP specification: host/client/server roles, resources, tools, prompts, transport, schema validation, and error handling.
- LangGraph docs: explicit state, nodes, edges, conditional routing, checkpointing, human-in-the-loop, and durable execution.
- Langfuse docs: traces, observations, prompts, evaluators, sessions, datasets, and experiment reporting.
- OpenAI Agents docs: Agents, Handoffs, Guardrails, Tools, and Tracing for production agent systems.
- NIST AI Risk Management Framework: govern, map, measure, and manage AI risk across the lifecycle.

## Interview Usage

- 30-minute screen: ask one question from L0, L1/L2, and L4.
- 60-minute technical review: ask L1, L2, L3, and one L4 incident drill.
- 75-minute senior review: ask L3 design, L4 production, and L5 pattern/contribution.
- Expert review: require evidence outside the answer: traces, evals, postmortems, PRs, docs, or talks.

## Scoring

Score each answer from 0 to 3.

- 0: definitional or memorized, no system boundary.
- 1: correct concepts, but missing failure mode, trade-off, or production evidence.
- 2: explains concepts plus trade-offs, validation, and one realistic example.
- 3: explains concepts, trade-offs, failure taxonomy, measurement, rollback or prevention, and ties them to maintainable architecture.

## L0: Baseline Concepts

### Primary Question

A production Agent gives a wrong answer after a one-token prompt edit. Explain the prompt / system instruction / tool result / final response boundary and what you inspect first.

### What A Strong Answer Includes

- Prompt: the user-visible task, request, and variables for this turn.
- System instruction: stable role, policy, output contract, escalation behavior, and safety rules.
- Tool result: external evidence or state that may be stale, partial, malformed, permission-filtered, or inconsistent with another source.
- Final response: the user-visible output after formatting, redaction, citations, refusal handling, and policy enforcement.
- First inspection: a minimal failing trace showing request, system prompt, retrieved context, tool calls/results, model output, parser/finalizer behavior, latency, and cost.

### Deep Follow-Ups

- How do tokens affect cost, latency, and behavior? Why is character count not enough?
- How do you distinguish context overflow from model hallucination?
- How do you prevent a prompt edit from silently changing tool-call policy?
- How do you preserve prompt version, model version, and tool schema version in logs?

### Production Evidence

Ask for one tiny trace or prompt rewrite showing:

- Before/after prompt.
- System instruction version.
- Tool result source and timestamp.
- Final response.
- Root cause category.

### Red Flags

- Treats prompt, system instruction, and tool result as interchangeable text.
- Says “change the model” before inspecting trace and inputs.
- Cannot explain why tool output still needs validation.
- Confuses raw model output with final user response.

### Source-Informed Notes

ReAct teaches that reasoning, actions, and observations form an interleaved loop. The L0 answer should already show that this loop is not free text; it is a traceable sequence of prompts, observations, actions, and outputs.

## L1: Agent Components and Loop Control

### Primary Question

Design a minimal ReAct Agent in code terms: state, actions, observations, stop conditions, logs, and failure handling.

### What A Strong Answer Includes

- State includes goal, messages/context, available tools, observations, plan/next action, attempts, policy status, and cost/latency counters.
- Actions include answer, ask clarification, call tool, retrieve evidence, escalate, stop, and rollback/abort.
- Observations include tool success/failure, empty result, timeout, permission denial, schema mismatch, partial data, and duplicate repeated observation.
- Stop conditions include success, max steps, max cost/latency, repeated failure, ambiguity, policy violation, unsafe intent, and missing evidence.
- Logs include step number, plan/action, tool name, args hash, result summary, stop reason, prompt/model/tool schema versions, and trace ID.

### Deep Follow-Ups

- Why is a max step limit necessary, and what is the right failure behavior when it is reached?
- How do you handle a tool result that is valid JSON but semantically wrong?
- How do you prevent prompt injection from a retrieved document from changing tool policy?
- How do you decide between direct answer, tool call, clarification, and escalation?

### Production Evidence

Ask for a pseudocode sketch or Lab result where the Agent:

- Stops after repeated identical tool calls.
- Clarifies instead of guessing.
- Logs enough detail to reconstruct the decision.
- Does not execute a destructive action without approval.

### Red Flags

- Treats ReAct as just a prompt template.
- Has no stop condition or no failure budget.
- Sends full tool results directly to the model without size, privacy, or schema checks.
- Cannot separate model planning from tool execution.

### Source-Informed Notes

ReAct-style Agents combine reasoning traces with external actions. The key engineering question is not “does it think?” but “can the system observe actions, stop safely, and replay the trace?”

## L2: Framework, Tools, MCP, and Boundaries

### Primary Question

Design a reliable single-Agent tool layer with MCP-style tools, validation, permissions, failure taxonomy, and human approval.

### What A Strong Answer Includes

- Tool contract: name, description, input schema, output schema, timeout, retryability, risk level, required permissions, and audit requirements.
- MCP layering: host owns Agent policy; client manages server connection; server exposes resources/tools/prompts; transport can be stdio, SSE, streamable HTTP, or equivalent.
- Discovery: verify server health, tool list, prompts/resources, schema version, auth scopes, and capability changes.
- Invocation: validate inputs, enforce risk policy, call tool, classify errors, validate outputs, normalize evidence, and store trace.
- Risk classes: read-only, write reversible, write irreversible, payment-like, permission-changing, data-export, destructive, and policy-sensitive.
- Human approval: required for irreversible writes, high blast radius, permission changes, or ambiguous intent.

### Deep Follow-Ups

- How do you distinguish discovery failure, auth failure, schema mismatch, timeout, and application failure?
- How do you handle a server that returns valid output but from the wrong tenant?
- How do you rate-limit and retry without amplifying damage?
- How do you prevent a tool schema change from silently changing Agent behavior?
- How do you decide between framework orchestration and a plain SDK/plain loop?

### Production Evidence

Ask for a tool-call trace with:

- Tool name and schema version.
- Permission decision.
- Input validation result.
- Output validation result.
- Retry/timeout policy.
- Approval or audit record.

### Red Flags

- Lets model output call tools without validation.
- Treating MCP as “just another API” without schema, transport, and error handling.
- Confirms every action regardless of risk.
- Cannot explain schema mismatch or auth-scope failure.
- Uses a heavy framework when a small validated loop would be clearer.

### Source-Informed Notes

MCP specifies client/server capabilities and schema-validated messages. A strong candidate treats MCP as a governed tool boundary, not a shortcut for unvalidated function calls.

## L3: End-To-End System Design

### Primary Question

Design a customer support Agent with RAG, memory, tools, MCP-style actions, observability, evals, and human escalation.

### What A Strong Answer Includes

- Requirements: traffic, latency, accuracy, privacy, language/region, compliance, cost, audit, rollback, and support SLA.
- Trust boundaries: user, tenant, document corpus, ticket system, order system, human reviewer, and Agent runtime.
- Data flow: intake -> intent/policy check -> retrieval -> memory lookup -> tool routing -> answer synthesis -> validation/citations -> final response -> trace.
- Retrieval: scoped by tenant/user/time/version; includes chunking, ranking, filters, reranking, freshness, and abstention.
- Memory: separates short-term conversation state from long-term preferences/facts; includes TTL, owner, deletion, consent, conflict handling, and staleness checks.
- Tools: order lookup, ticket update, refund proposal, policy lookup, escalation, and write actions with approval.
- Evals: retrieval relevance/recall, answer support, citation correctness, refusal quality, tool accuracy, escalation accuracy, latency, cost, and safety.
- Observability: trace every prompt, retrieved source, memory read/write, tool call, decision, citation, final response, cost, and stop reason.

### Deep Follow-Ups

- How do you know whether the final answer came from RAG, memory, live tool state, or the model?
- How do you prevent one Agent from overwriting another Agent's decision or shared state?
- When should the system refuse, retrieve more, call a tool, or escalate?
- How do you handle conflicting policy documents and stale memory?
- How do you evaluate negative cases where no answer should be given?

### Production Evidence

Ask for a one-page design or whiteboard trace showing:

- Request.
- Retrieved docs with timestamps.
- Memory read/write decision.
- Tool call and result.
- Citation or refusal.
- Final answer.
- Eval/regression case added for a known failure.

### Red Flags

- Starts with “use multi-agent” without decomposition or ownership.
- Forgets tenant isolation, citations, refusal, or stale memory.
- Treats retrieval as “put everything into context.”
- No eval strategy before launch.
- No path for tool failure or human escalation.

### Source-Informed Notes

The strongest L3 answer maps the system like a trace. It names where evidence comes from, who owns the state, what can fail, and how the system proves the answer was correct and safe.

## L4: Production Reliability, Safety, and Operations

### Primary Question

A customer says the Agent changed the wrong account. Lead the incident response and define the release gate that prevents recurrence.

### What A Strong Answer Includes

- Containment: disable or route around the risky action path; freeze writes if data integrity is uncertain.
- Evidence collection: request ID, trace ID, prompt/system version, model version, retrieved context, memory, tool schema, tool args/results, authorization, user role, tenant, final response, and rollout metadata.
- Root cause categories: bad data, retrieval miss, stale memory, wrong tool schema, malformed output, permission bypass, model behavior change, parser/finalizer bug, prompt regression, rate/cost anomaly, or human approval gap.
- Communication: customer impact, internal severity, affected tenants, rollback status, next update time, and owner.
- Fix: patch code/prompt/schema/tool policy, add eval and trace field, add guardrail, and document postmortem with owner and due date.
- Prevention: release gate includes golden evals, safety evals, tool-schema contract tests, authorization tests, trace completeness, rollback plan, and canary/shadow deployment.

### Deep Follow-Ups

- What severity should this be, and why?
- What canary signal would have caught it before full rollout?
- How do you measure whether the guardrail is too strict or too weak?
- How do you handle model version changes as releases?
- How do you classify incidents around correctness, safety, data integrity, privacy, availability, and cost?
- How do you keep traces useful while avoiding sensitive data leakage?

### Production Evidence

Ask for a postmortem-style artifact with:

- Timeline.
- Root cause.
- Detection path.
- Customer/user impact.
- Rollback.
- Regression eval.
- Owner and due date.
- Non-goals and residual risk.

### Red Flags

- Blames the model without inspecting data, prompts, tools, or traces.
- Has no containment step.
- No rollback plan.
- No regression eval or prevention control.
- Treats observability as final logs rather than replayable traces.

### Source-Informed Notes

NIST AI RMF frames AI risk as govern, map, measure, and manage. The incident answer should map the failure, measure impact, contain risk, and manage the residual risk through evals and release gates.

## L5: Expert Patterns, Contribution, and Ecosystem Strategy

### Primary Question

Propose an original Agent pattern worth contributing to Agent-Top. Include contract, failure modes, evals, migration story, and evidence of impact.

### What A Strong Answer Includes

- Problem: a repeated failure or maintenance pain across systems, not just framework flavor.
- Pattern contract: inputs, outputs, state, tools, memory, stop conditions, safety boundaries, observability, and validation.
- Failure taxonomy: what can fail, how it is detected, and what fallback is used.
- Evals and traces: deterministic tests where possible, golden cases, negative cases, latency/cost baselines, and replayable trace fields.
- Adoption story: when to use it, when not to use it, migration from existing code, deprecation policy, and maintainer burden.
- Evidence: Lab, PR, talk, article, design review, external adoption, or measurable improvement.
- Spec-first drafting: state goal, interface, and acceptance in one sentence before prompting, using the [Vibe Coding workflow](../../vibe-coding/README.md).

### Deep Follow-Ups

- What did you reject, and why?
- What makes this a pattern rather than a framework wrapper?
- How do you prevent framework churn from making the pattern stale?
- How do you decide when a Lab should graduate to production guidance?
- How do you balance pattern abstraction against ease of understanding?
- What would convince maintainers not to accept this contribution?

### Production Evidence

Ask for one of:

- A Lab or PR with tests and docs.
- A pattern note with rejected alternatives and migration steps.
- A design review with trade-offs.
- A talk, article, or community artifact.
- A measurable result: fewer incidents, lower cost, better eval score, faster onboarding, or reduced manual review.

### Red Flags

- The contribution is just a framework example.
- No failure modes or negative cases.
- No migration or deprecation story.
- Claims L5 impact with only usage examples.
- Cannot explain maintainer burden or ecosystem fit.

### Source-Informed Notes

Strong L5 work borrows from mature projects without copying them. It keeps the pattern first, frameworks second, and proves value through tests, docs, traces, and contribution evidence.

## Deep Answer Checklist

A complete answer should include:

- System boundary.
- Trust boundary.
- Data or evidence path.
- Tool/action policy.
- Failure taxonomy.
- Stop or escalation condition.
- Observability and trace fields.
- Eval or regression case.
- Rollback or prevention.
- Trade-off and rejected alternative.
- One concrete example.

## Common Deep Follow-Up Bank

- What data would make this answer wrong?
- What is the cheapest safe rollback?
- Which trace field would reveal the root cause?
- What eval would block the bad release?
- What would you not automate even if the model is confident?
- What happens when the tool schema changes?
- What happens when memory and retrieval disagree?
- What happens when the user asks for an irreversible action?
- What metric would tell you the guardrail is too strict?
- What evidence would convince a maintainer this belongs upstream?

## Level-to-Evidence Mapping

| Level | Best Evidence |
| --- | --- |
| L0 | Prompt rewrite, tiny trace, token/context budget note |
| L1 | Minimal ReAct Lab, stop-condition test, tool ambiguity test |
| L2 | Tool schema contract, MCP failure taxonomy, approval trace |
| L3 | System design with RAG/memory/tools/escalation and eval matrix |
| L4 | Incident postmortem, regression eval, rollback plan, trace example |
| L5 | Original pattern, Lab/PR, migration story, external contribution |
