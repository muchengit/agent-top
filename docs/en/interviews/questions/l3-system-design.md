---
title: L3 System Design Questions
validated_date: 2026-09-17
i18n-key: interviews-questions-l3-system-design
last-synced: 2026-09-17
---

# L3 System Design Questions

These questions check whether the candidate can design, debug, and evaluate agent systems in production terms: component boundaries, failure isolation, cost and latency, and evidence-based decisions. Four question types are covered: concept, implementation, debugging, and design.

## Question Bank

### Concept

#### 1. When should a system use multi-agent versus single-agent?

**Answer points:**

- Prefer multi-agent when decomposition improves clarity, privilege isolation, or specialization, and when independent verification adds real value.
- Prefer single-agent when the task is small, latency is tight, or coordination cost exceeds reliability gain.
- Add verification agents only when an independent check detects errors that a single loop would miss.
- Define the handoff contract before adding a second agent: message schema, ownership, and error semantics.

**What the interviewer wants to hear:**

- Trade-off: multi-agent multiplies failure surface (who answers for a wrong handoff?) and token cost; two agents can be more expensive and less reliable than one well-structured loop.
- Production counterexample: a "planner, writer, reviewer" pipeline degraded because the reviewer rewrote correct work; collapsing to one agent with checkpoints and a review gate fixed quality and cut cost.
- Data thinking: measure marginal value per added agent (quality gain per token spent); if the second agent adds less than its cost, cut it.

**Bonus / Common mistakes:**

- Bonus: decide by failure domain — state complexity, parallelism, and specialization — not by hype.
- Mistake: using "multi-agent" as a buzzword without defining handoff contracts or accountability.

#### 2. How do you know whether the final answer came from RAG, memory, or live tool state?

**Answer points:**

- Require provenance metadata: each claim is tagged with its source type, source id, and timestamp.
- Enforce a grounding check that marks claims unsupported by retrieved or tool evidence.
- Separate stores: memory (user facts) must not mix with knowledge (documents) or live state (tool results).

**What the interviewer wants to hear:**

- Trade-off: provenance costs storage and prompt tokens but makes every answer auditable and every incident replayable.
- Production counterexample: an answer cited a cached doc while billing state had changed; without source tags nobody could tell which layer was stale.
- Data thinking: track source-mix metrics — the share of answers grounded in docs vs tools — so you can see freshness problems before users complain.

**Bonus / Common mistakes:**

- Bonus: emit a machine-readable citation payload per answer, not just visible text.
- Mistake: assuming the model only uses the context you gave it.

### Implementation

#### 3. Design a RAG + memory + MCP data flow.

**Answer points:**

- Normalize the query (language, entities, PII stripping) before any retrieval or tool call.
- Hybrid retrieval: BM25 plus embeddings with a reranker, scoped by document ACLs and tenant.
- Memory lookup: durable user facts separate from knowledge docs; memory is read-only in generation unless a curation agent updates it.
- Tool layer via MCP: a registry of tools with schemas, auth, timeouts, and rate limits; call tools only when the question requires live state.
- Generation with provenance, then a verification step that rejects unsupported claims.

**What the interviewer wants to hear:**

- Trade-off: live tool calls are authoritative but slow and expensive; cached docs are cheap but stale. Distinguish "tool call mandatory" (billing, account settings) from "retrieval is enough" (documentation, how-to).
- Production counterexample: the model answered "your current plan" from a cached doc while the billing API had already changed — fluent, cited, and wrong.
- Data thinking: track retrieval recall@k, answer support (faithfulness), citation accuracy, and a freshness-gap metric (document version time minus query time).

**Bonus / Common mistakes:**

- Bonus: confidence-based abstention when grounding is weak.
- Mistake: merging memory and knowledge into one vector store, leaking personal facts across users.

#### 4. How do you design multi-agent communication without deadlocks or decision overwrites?

**Answer points:**

- Use typed messages with IDs and versioned schemas; every message is idempotent so retries are safe.
- Assign a single writer per resource: the refund agent owns payment state, the ticket agent owns ticket state, others read only.
- Make decisions immutable events: a resolved refund is appended, not a mutable field a second agent can overwrite.
- Detect cycles: an orchestrator with a hop limit, per-message TTL, and cycle detection prevents infinite delegation.
- Apply timeouts and circuit breakers: a tool exceeding its budget is retried at most N times with backoff, then escalated.

**What the interviewer wants to hear:**

- Trade-off: an orchestrator centralizes coordination but becomes a bottleneck and SPOF; peer-to-peer distributes load but complicates ordering and debugging.
- Production counterexample: two agents both observe a ticket as "unassigned" and both attempt a refund — without a single-writer rule the second overwrites the first or double-executes.
- Data thinking: instrument message counts, retry rates, conflict events, and time-to-consensus; a conflict rate that grows with ticket volume indicates a missing single-writer rule, not a prompt problem.

**Bonus / Common mistakes:**

- Bonus: event sourcing for decisions, deterministic tie-breaking, and tests that assert exactly-once execution.
- Mistake: at-least-once delivery without idempotency, so retries become duplicates.

### Debugging

#### 5. Debug: the agent answers "current plan" from a stale doc instead of live billing state.

**Answer points:**

- Reproduce from the trace: replay the exact prompt, retrieved chunks, tool calls, and final answer.
- Generate hypotheses: stale cache, retrieval relevance, a schema mismatch that hid the tool, a missing freshness policy, or a prompt that biases toward docs.
- Verify each: replay the tool call live, compare document timestamps with query time, and check whether the grounding check ran.
- Fix at the root: make live-state questions mandate a tool call (policy, not prompt), add freshness metadata to chunks, keep verification on.
- Add a regression eval case and alert on the freshness-gap metric.

**What the interviewer wants to hear:**

- Trade-off: caching cuts cost and latency but trades freshness; never let a prompt instruction be the only barrier between the model and stale data.
- Production counterexample: the team "fixed" this by adding "always use the tool for plan questions" to the prompt — it worked on one eval case and failed on the next paraphrased question two weeks later.
- Data thinking: add a freshness-gap metric and a source-mix metric; the incident was visible in both before any user complained.

**Bonus / Common mistakes:**

- Bonus: show provenance in the UI ("answer source: doc v3, 2026-08-01") so users can see staleness.
- Mistake: blaming the model without inspecting the pipeline — the model did exactly what the context allowed.

#### 6. How do you evaluate a retrieval agent before launch?

**Answer points:**

- Build a versioned golden set from production logs: queries with required facts, negative cases, ambiguous cases, and injection attempts.
- Measure retrieval in isolation (recall@k, MRR, precision@k) and end-to-end answer quality (support, citation accuracy, refusal correctness).
- Track latency and cost per query alongside quality.
- Gate CI: the eval runs on every prompt or retrieval change, and regressions block merge.

**What the interviewer wants to hear:**

- Trade-off: small hand-labeled sets are accurate but sparse; large auto-labeled sets cover more but inherit label noise. Use both.
- Production counterexample: an eval set built only from happy paths misses that the agent confidently answers outside its corpus.
- Data thinking: measure false acceptance and false refusal separately; slice by language, tenant, and topic, and watch the long tail.

**Bonus / Common mistakes:**

- Bonus: golden set versioning tied to docs releases, plus a red-team suite.
- Mistake: measuring retrieval quality but not answer support, so you cannot tell a retrieval bug from a generation bug.

### Design

#### 7. Design a multi-agent customer support system.

**Answer points:**

- Clarify intent, permissions, and boundaries first: which actions are autonomous, which need confirmation, which always escalate.
- Route at a gateway: classify intent and risk, then dispatch to specialized agents (retrieval, tool execution, escalation, memory) with a typed handoff contract.
- Use confidence thresholds and fallbacks: low-confidence intent goes to a generalist or a human, never to a high-risk tool.
- Enforce guardrails before tool execution: allowlisted tools, parameter validation, idempotency keys, policy check per action.
- Keep memory scoped: session memory for the current ticket, durable customer memory only with opt-in and PII boundaries.
- Trace everything: prompt, chunks, tool calls, decisions, and evaluation outcomes must be replayable.
- Budget explicitly: small model for routing, expensive reasoning only on complex tickets, caching stable retrieval.

**What the interviewer wants to hear:**

- Trade-off: a single generalist agent is simpler and cheaper but widens the blast radius of one bad prompt; many single-purpose agents add coordination cost and debugging pain. Show the middle ground and justify it with ticket volume and error data.
- Production counterexample: one agent holding every tool (refund, account delete, email send) lets a single mis-route cause harm; the opposite failure is a 12-agent architecture where context is re-fetched five times and a failure is untraceable.
- Data thinking: name metrics before architecture — resolution rate without human, escalation rate, first-contact resolution, p95 latency per route, cost per ticket, guardrail false-positive rate — and A/B the router behind a flag.

**Bonus / Common mistakes:**

- Bonus: idempotency keys on every mutating tool call; human handoff carries the full trace.
- Mistake: no permission boundary — the same agent that answers questions can also approve refunds.

#### 8. How do you eliminate single points of failure in an agent system?

**Answer points:**

- Enumerate SPOFs: one LLM provider, one MCP gateway, in-memory orchestration state, a single vector store, synchronous call chains.
- Redundancy with intent: a second model provider or routing fallback; read replicas for retrieval; a standby tool gateway.
- Durable orchestration state: persist decisions and in-flight steps so a crashed worker resumes instead of restarting the conversation.
- Decouple with queues: async processing with retries and a DLQ so a slow tool does not block the whole request.
- Define degraded modes explicitly: LLM down means canned answers plus human queue; tool down means refusal with a clear message, never a guess.

**What the interviewer wants to hear:**

- Trade-off: dual-provider redundancy roughly doubles some variable cost; the decision must map to an SLO, not to fear.
- Production counterexample: "everything depends on the orchestrator" — one pod crash drops every active conversation because state lives in memory.
- Data thinking: measure failover latency in p95 and the availability contribution of each dependency; spend redundancy budget where the availability gap is largest.

**Bonus / Common mistakes:**

- Bonus: timeout budgets and circuit breakers, degraded-mode end-to-end tests, a dependency map in the runbook.
- Mistake: redundant compute but a single state store, so failover restarts conversations from scratch.

## Follow-Up Bank

- How do you prevent one agent from overwriting another agent's decision?
- How do you tell whether the final answer came from RAG, memory, or live tool state?
- What makes a multi-agent system unsafe?
- What do you do when retrieval is correct but the answer is wrong?
- Which dependency would you fail over first, and why?

## Common Red Flags

- Splitting agents before data shows a single loop is the bottleneck.
- Treating high relevance scores as proof.
- No freshness policy for live-state questions.
- Shared mutable state with no owner.
- No idempotency keys on mutating tool calls.

## Portfolio Evidence

For L3, acceptable evidence is:

- A multi-agent design doc with component boundaries, error isolation, and cost/latency budget.
- An eval report with recall@k, answer support, and refusal correctness on a versioned golden set.
- A post-incident replay showing root cause and the regression test that prevents recurrence.
