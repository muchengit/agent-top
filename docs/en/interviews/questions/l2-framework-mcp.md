---
title: L2 Framework and MCP Questions
validated_date: 2026-09-18
i18n-key: interviews-questions-l2-framework-mcp
last-synced: 2026-09-18
---

# L2 Framework and MCP Questions

These questions test framework judgment, MCP protocol reasoning, and reliability engineering for a single production Agent.

## Question Bank

Four question types are covered: concept, implementation, debugging, and design.

### Concept

#### 1. How do you choose between a graph orchestration framework and a lightweight SDK?

**Answer points:**

- Use graph orchestration when state, cycles, checkpoints, and human review matter.
- Use a lightweight SDK when the flow is small, mostly linear, and easier to debug.
- Prefer the simplest framework that makes failure modes explicit.

**What the interviewer wants to hear:**

- Trade-off: orchestration frameworks buy checkpoints and recoverability at the price of indirection and debugging overhead; SDKs stay transparent but make you hand-roll state and retries.
- Production counterexample: a team migrated a linear three-step RAG flow into a graph framework, and step count tripled; the win was durable checkpoints only after they actually needed crash recovery.
- Data thinking: count how often a flow must resume after a crash or human interrupt; that frequency, not the feature list, decides whether the orchestration tax is worth it.

**Bonus / Common mistakes:**

- Bonus: name the concrete framework feature that forces the decision, such as durable checkpointing or human-in-the-loop pause points.
- Mistake: choosing a framework for brand familiarity or demos instead of a measured failure mode.

#### 2. What is MCP, and what problem does it solve?

**Answer points:**

- MCP standardizes how Agents discover, connect to, and invoke capabilities over a protocol.
- It separates tool, resource, and prompt server definitions from the Agent runtime.
- It replaces N ad hoc API integrations with one protocol for tool discovery, schemas, and auth.

**What the interviewer wants to hear:**

- Trade-off: a standard reduces integration cost and enables reuse, but adds a protocol layer, discovery overhead, and a versioning surface you must maintain.
- Production counterexample: a company with 40 bespoke tool integrations could not share tools across teams; MCP-style servers cut per-application integration work, but only after investing in one auth and naming convention.
- Data thinking: before adopting, count integrations, maintenance hours, and how often tools change shape; standards pay off when the matrix is large and shared.

**Bonus / Common mistakes:**

- Bonus: mention that MCP is a protocol for the Agent-tool boundary, not an agent framework, and that transport, auth, and versioning still need design.
- Mistake: treating MCP as a magic layer that removes the need for schema quality and safety reviews.

#### 3. How do you choose among graph orchestration, multi-agent, and lightweight approaches?

**Answer points:**

- Graph orchestration suits complex, resumable, human-reviewed flows.
- Multi-agent suits independent specialists with clear handoffs, but adds coordination cost.
- Lightweight SDKs or plain loops suit small linear flows where transparency beats machinery.

**What the interviewer wants to hear:**

- Trade-off: multi-agent multiplies failure surface (who answers for a wrong handoff?) and token cost; two agents can be more expensive and less reliable than one well-structured loop.
- Production counterexample: a pipeline with "planner, writer, reviewer" agents degraded because the reviewer rewrote correct work; collapsing to one agent with checkpoints and a review gate fixed quality and cut cost.
- Data thinking: measure marginal value per added agent (quality gain per token spent); if the second agent adds less than its cost, cut it.

**Bonus / Common mistakes:**

- Bonus: decide by failure domain: state complexity, parallelism, and specialization, not by hype.
- Mistake: using "multi-agent" as a buzzword without defining handoff contracts or accountability.

### Implementation

#### 4. What is a good tool boundary for an Agent?

**Answer points:**

- A tool should have one clear job with typed and validated inputs and outputs.
- Side effects should be explicit; errors must be distinguishable from empty results.
- Destructive actions require confirmation or approval and return enough metadata to audit.

**What the interviewer wants to hear:**

- Trade-off: coarse tools reduce round trips but make outputs unwieldy and failure noisy; fine tools are composable but cost more model steps.
- Production counterexample: a "manage everything" tool made the model cancel a subscription when the user asked to pause it; splitting read, update, and cancel into separate tools with explicit scopes fixed it.
- Data thinking: track misuse rate per tool and let that drive boundary changes, not intuition.

**Bonus / Common mistakes:**

- Bonus: give every tool a documented effect contract: inputs, side effects, and what "done" means.
- Mistake: returning a valid response with wrong data — the hardest failure to detect because it looks like success.

#### 5. How do you stop a single Agent from being unreliable in production?

**Answer points:**

- Add code-enforced stop conditions, validated schemas, and retry and time-out policies outside the model.
- Add guardrails for destructive actions and alerting on stop-reason and failure distributions.
- Make every step replayable with the exact inputs and outputs for post-mortem.

**What the interviewer wants to hear:**

- Trade-off: reliability controls improve behavior but reduce flexibility; every guardrail costs latency and can block legitimate cases.
- Production counterexample: a parser that rejected any schema deviation made the Agent look broken for a week until the team measured that 60% of "failures" were one missing optional field.
- Data thinking: track reliability as distributions (stop reasons, retries, tool errors) and alert on shifts, not on single failures.

**Bonus / Common mistakes:**

- Bonus: separate "hard reliability" (crash, hang, budget) from "soft quality" (wrong answer) and monitor them differently.
- Mistake: promising a fixed success rate while logging nothing that can explain a single failure.

#### 6. MCP server integration fails. How do you debug it?

**Answer points:**

- Check server availability and transport first, then schema and capability discovery.
- Check auth and permissions, then inspect the first tool call logs.
- Classify the failure: discovery, invocation, timeout, permission, or output parsing.

**What the interviewer wants to hear:**

- Trade-off: broad timeouts hide slow servers behind vague failures; tight timeouts cause flaky false alarms on bursts — pick per-capability budgets.
- Production counterexample: a "server down" alert was actually a schema version mismatch: the server served tools the client had cached under an old version, and every call failed validation.
- Data thinking: log protocol-level error codes and latency percentiles per server; a latency P99 shift usually precedes the first user-visible failure.

**Bonus / Common mistakes:**

- Bonus: add a health probe plus a round-trip test through the real tool call path for production visibility.
- Mistake: debugging the application layer while the transport or capability discovery is the actual failure.

#### 7. How do you handle a tool that returns valid data but wrong results?

**Answer points:**

- Detect the difference between schema-valid and semantically correct output.
- Add expected-range checks, cross-checks with a second source, or freshness checks.
- Surface the signal to the Agent as an explicit "unverified" state and escalate for review.

**What the interviewer wants to hear:**

- Trade-off: full verification doubles cost and latency; sampling verification catches systemic bugs without taxing every call.
- Production counterexample: a currency tool returned correct-shaped data in the wrong currency unit; schema validation passed for months until a cross-check with a second provider exposed it.
- Data thinking: track the mismatch rate between cheap checks (type, range, unit) and ground truth on a sample; a nonzero mismatch rate means you need an always-on spot check.

**Bonus / Common mistakes:**

- Bonus: add source and timestamp fields to every tool result so downstream verification is possible.
- Mistake: treating schema validation success as data correctness.

### Debugging

#### 8. An MCP tool call times out in production. How do you debug it?

**Answer points:**

- Confirm whether the timeout is client-side, transport, server-side, or downstream of the tool.
- Check latency percentiles, retry behavior, and whether the tool actually executed despite the timeout.
- Add idempotency keys so retries do not double-execute side effects.

**What the interviewer wants to hear:**

- Trade-off: retries fix transient failures but make non-idempotent tools dangerous; timeouts bound latency but leave "did it run?" ambiguous.
- Production counterexample: a payment-adjacent call timed out, the Agent retried, and the action executed twice because the tool was not idempotent.
- Data thinking: measure the timeout-to-success ratio (call failed but side effect happened) to decide when retry is safe.

**Bonus / Common mistakes:**

- Bonus: require every state-changing MCP tool to accept an idempotency key.
- Mistake: assuming a timeout means the action did not happen.

#### 9. How do you make an MCP integration failure visible in production?

**Answer points:**

- Expose health probes, structured protocol error codes, and latency percentiles per server.
- Log the full round trip: request, transport, response, and the exact schema used.
- Alert on rate shifts (error rate, P99 latency) instead of individual failures.

**What the interviewer wants to hear:**

- Trade-off: rich logs make diagnosis instant but cost storage; sample heavy payloads and keep full metadata.
- Production counterexample: an integration "worked in staging but failed in prod" because prod used a different transport and auth path; the fix was a prod parity test that exercised the real protocol.
- Data thinking: track schema version per call alongside error codes so version-skew failures are attributable.

**Bonus / Common mistakes:**

- Bonus: build a canary call that runs the real tool path on a schedule.
- Mistake: alerting on raw error counts and waking people for a single noisy user retry.

### Design

#### 10. Design a guardrail strategy for an Agent that touches external systems.

**Answer points:**

- Enforce policy in code, not just in the prompt: allowed actions, allowed targets, rate limits, and approval gates.
- Classify risk by reversibility, blast radius, and data sensitivity.
- Emit audit logs with correlation IDs and verify after execution.

**What the interviewer wants to hear:**

- Trade-off: strict code gates are safe but add friction; permissive ones ship fast but leak risk — tune by risk class, not globally.
- Production counterexample: a "safe" approval widget was bypassed because the same UI element served both preview and confirm for different action types; separating confirm contracts per action class closed it.
- Data thinking: track guardrail trigger, override, and bypass-attempt rates as product metrics, not just security metrics.

**Bonus / Common mistakes:**

- Bonus: make the guardrail the outer ring and the system prompt an inner convenience, never the only barrier.
- Mistake: relying on a refusal prompt for actions with irreversible consequences.

#### 11. Design a decision framework for when to move a flow from a single Agent to graph orchestration or multi-agent.

**Answer points:**

- Choose by measured signal: crash-resume frequency, human-review points, parallelism opportunities, and per-agent specialization gains.
- Keep the flow in a single Agent until replay, checkpointing, or review needs are proven.
- Define handoff contracts and accountability before splitting.

**What the interviewer wants to hear:**

- Trade-off: splitting improves modularity and parallelism but raises coordination, token, and debugging cost.
- Production counterexample: a report pipeline split into researcher and writer agents produced contradictory sections until a shared fact-state plus a review gate was added.
- Data thinking: compare quality and cost per flow variant on the same eval set; choose on the numbers, not on the architecture diagram.

**Bonus / Common mistakes:**

- Bonus: run the "one Agent with checkpoints" baseline first and measure the gap before adopting any framework.
- Mistake: splitting agents before data shows a single loop is the bottleneck.

## Follow-Up Bank

- What framework feature would force you to choose graph orchestration over a plain loop?
- How would you make an MCP integration failure visible in production?
- What approval workflow would you design for a high-risk support action?
- When is a single Agent with checkpoints better than a multi-agent design?
- How do you verify a tool result that is schema-valid but semantically wrong?

## Common Red Flags

- Chooses frameworks or multi-agent setups on hype instead of measured failure modes.
- Treats MCP as an agent framework rather than a protocol for the tool boundary.
- Trusts the prompt for safety-critical enforcement.
- Treats schema validation as proof of data correctness.
- Has no replay path or stop-reason data for the Agent in production.

## Portfolio Evidence

For L2, acceptable evidence is:

- A framework selection note that maps measured system needs to a concrete choice.
- An MCP server with a health probe, structured error codes, and a full round-trip trace.
- A single-Agent reliability report covering stop reasons, retries, and guardrail metrics.

## Related Tutorials

Study the matching tutorial before or after this question bank: [`L2 Single Agent with MCP`](../../l2-single-agent-mcp.md).
