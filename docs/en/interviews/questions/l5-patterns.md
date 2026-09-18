---
title: L5 Pattern Questions
validated_date: 2026-09-18
i18n-key: interviews-questions-l5-patterns
last-synced: 2026-09-18
---

# L5 Pattern Questions

These questions check whether the candidate can define standards and produce external impact: original patterns, architecture trade-offs, open-source contribution, and vertical expertise evidence. Four question types are covered: concept, implementation, debugging, and design.

## Question Bank

### Concept

#### 1. What makes a reusable Agent pattern valuable?

**Answer points:**

- It solves a repeated problem across contexts, not a one-off task.
- It has stable inputs and outputs and explicit failure modes.
- It includes safety and verification as first-class parts.
- It is easier to maintain than framework-specific code.
- It comes with an eval set that proves when it helps and when it does not.

**What the interviewer wants to hear:**

- Trade-off: a pattern that is too abstract is unfalsifiable; too concrete is not reusable. The value is in the boundary you draw and the evidence you attach.
- Production counterexample: a "memory pattern" that is really a database wrapper adds ceremony without addressing freshness or privacy; the valuable version defines when memory is written, read, and forgotten.
- Data thinking: a pattern should carry its own success metric — where it improved accuracy, latency, or cost by how much.

**Bonus / Common mistakes:**

- Bonus: explain when a pattern should become a framework (when the same boundaries are needed in many places).
- Mistake: naming a library as a "pattern" without defining the problem it abstracts.

#### 2. How do you evaluate whether to build a framework or use an existing one?

**Answer points:**

- Build only when existing frameworks hide a recurring problem or make failure modes unclear.
- Use existing frameworks when they cover state, tooling, observability, and ecosystem needs.
- Keep framework code isolated and version-anchored (`tested_against`).
- Test adoption and maintenance cost before committing.

**What the interviewer wants to hear:**

- Trade-off: frameworks buy batteries but cost control; hand-rolled code is transparent but you pay for every feature.
- Production counterexample: a team built a "lightweight framework" that was just the existing SDK plus a config layer; the abstraction hid version skew and cost more than it saved.
- Data thinking: measure time-to-ship and time-to-debug for both paths on the same task before deciding.

**Bonus / Common mistakes:**

- Bonus: define the exit condition — when the abstraction is more expensive than the framework it wraps.
- Mistake: framework tribalism, choosing by brand instead of failure modes.

### Implementation

#### 3. How do you design an original pattern for a repeated problem?

**Answer points:**

- Start from a concrete failure you have seen twice or more.
- Extract the invariant: what must always be true (grounding, idempotency, permission check).
- Define the boundary: inputs, outputs, and what the pattern refuses to do.
- Implement it in the simplest form, then evaluate on a golden set.
- Document the trade-off and the anti-patterns to avoid.

**What the interviewer wants to hear:**

- Trade-off: an original pattern should be more than a rename; it must change a measurable outcome.
- Production counterexample: a "verification gate" pattern that was just a prompt instruction added no value until it became a code gate with its own eval set.
- Data thinking: show the before/after on accuracy, latency, or cost from the pattern's own eval.

**Bonus / Common mistakes:**

- Bonus: publish the pattern with a case study and open-source evidence.
- Mistake: inventing terminology for a standard practice and calling it original.

#### 4. How do you prevent framework churn from destroying your docs and evals?

**Answer points:**

- Isolate framework-specific code in Labs and examples, not in concept docs.
- Anchor every framework example with `tested_against` and `validated_date`.
- Keep principle text independent of framework APIs.
- Re-run the eval set on every framework upgrade; treat version changes as release events.
- When a framework deprecates, mark docs deprecated and link replacements before archiving.

**What the interviewer wants to hear:**

- Trade-off: version pinning protects reproducibility but delays adoption; CI checks balance both by detecting lag automatically.
- Production counterexample: a tutorial that referenced a renamed SDK function silently rotted for two quarters; a CI freshness check caught it only after the version anchor was added.
- Data thinking: track doc-version-to-SDK-version lag as a metric; alert when it exceeds a threshold.

**Bonus / Common mistakes:**

- Bonus: a scheduled job that probes framework examples and opens sync-required issues.
- Mistake: rewriting principle docs every time a framework changes — that is churn, not maintenance.

### Debugging

#### 5. Debug a pattern failure in production: the "verify-then-act" gate was bypassed.

**Answer points:**

- Replay the trace: find which code path skipped the gate and why.
- Check whether the gate is a code enforcement or a prompt suggestion.
- Look for paths that share the same handler: preview, confirm, and execute may share code that weakens the boundary.
- Fix by making the gate structural (separate handlers, separate permissions, explicit state machine).
- Add a regression test that tries every bypass path.

**What the interviewer wants to hear:**

- Trade-off: structural gates are safer but more code; prompt gates are cheap but advisory. The failure mode decides which you need.
- Production counterexample: the gate passed in tests because the test called the happy-path handler; the bypass was in a different handler that shared the same permission check.
- Data thinking: track gate hit rate versus bypass attempts; a bypass attempt that succeeds is a P0.

**Bonus / Common mistakes:**

- Bonus: fuzz the gate with every state transition to prove it cannot be skipped.
- Mistake: patching the prompt and declaring the pattern fixed.

#### 6. How do you prove vertical expertise (finance, healthcare, etc.) through evidence?

**Answer points:**

- Build a domain eval set: regulatory cases, edge cases, and refusal cases specific to the vertical.
- Show measured results: accuracy, false refusal, and false acceptance on that set.
- Document domain constraints: compliance, audit, data residency, and explainability requirements.
- Publish a pattern or case study that transfers to other teams.
- Get external validation: PRs, talks, papers, or adoption.

**What the interviewer wants to hear:**

- Trade-off: vertical expertise costs time and data access; the evidence is what separates claims from demonstrated ability.
- Production counterexample: a resume that says "healthcare AI" without a single regulatory edge case or eval result; the evidence is the eval set and the incident history.
- Data thinking: show numbers — how many domain cases, what pass rates, what false-refusal cost, what audit outcomes.

**Bonus / Common mistakes:**

- Bonus: a public artifact (blog, paper, open-source lab) that others can verify.
- Mistake: listing domain keywords without measurable outcomes.

### Design

#### 7. Design a pattern that prevents double-execution in agent tool calls.

**Answer points:**

- Require an idempotency key on every mutating tool call.
- Make the key derivable from request context (user, action, entity, dedup window).
- Store executed keys with TTL; on retry, return the original result instead of re-executing.
- Add a post-execution verification step that confirms the side effect happened exactly once.
- Test with retry storms and concurrent calls.

**What the interviewer wants to hear:**

- Trade-off: idempotency costs storage and key design but eliminates the worst failure class in agent systems (double side effects).
- Production counterexample: a payment-adjacent call timed out, the agent retried, and the action executed twice because the tool was not idempotent.
- Data thinking: measure the timeout-to-success ratio — calls that failed but whose side effect happened — to decide when retry is safe.

**Bonus / Common mistakes:**

- Bonus: require every state-changing MCP tool to accept an idempotency key.
- Mistake: assuming a timeout means the action did not happen.

#### 8. Design a decision framework for when a pattern becomes a framework or a standard.

**Answer points:**

- Count the number of independent adopters and contexts.
- Measure the maintenance cost of the pattern as duplicated code.
- Define the contract: schemas, semantics, failure modes, and versioning.
- Decide the governance: who reviews changes, how versions are released, how deprecation works.
- Ship the standard with tests and examples, not just documentation.

**What the interviewer wants to hear:**

- Trade-off: standardizing early locks in mistakes; standardizing late multiplies migration cost. The trigger is evidence of repeated, identical boundaries.
- Production counterexample: two teams built the same tool-boundary code three times before a shared MCP-style standard; the third team paid the cost of the first two.
- Data thinking: track the duplication metric — how many copies of the same pattern exist — to justify standardization.

**Bonus / Common mistakes:**

- Bonus: make the standard a living artifact with versioned examples and a migration guide.
- Mistake: writing a standard with no implementation, tests, or deprecation path.

## Follow-Up Bank

- When should a pattern become a framework?
- How do you prove a pattern is not just a rename?
- What is your exit condition for a hand-rolled framework?
- How do you migrate docs when a framework deprecates?
- Which dependency would you standardize first, and why?

## Common Red Flags

- Pattern claims without eval evidence.
- Framework tribalism instead of measured failure modes.
- Framework-specific code mixed into principle docs.
- No version anchors or freshness checks.
- Standards without implementation, tests, or deprecation path.

## Portfolio Evidence

For L5, acceptable evidence is:

- An original pattern with a case study, eval set, and before/after metrics.
- An open-source PR, paper, or talk that others can verify.
- A vertical-domain eval report showing regulatory and edge-case coverage.
- A standard or framework contribution with versioning and migration guide.

## Related Tutorials

Study the matching tutorial before or after this question bank: [`L5 Custom Patterns`](../../l5-custom-patterns.md).
