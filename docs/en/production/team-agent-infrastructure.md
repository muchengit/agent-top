---
title: Team Agent Infrastructure
capability_level: L5
validated_date: 2026-09-17
i18n-key: production-team-agent-infrastructure
last-synced: 2026-09-17
---

# Team Agent Infrastructure

Production guides are the readiness layer for Agent systems. This guide extends the individual-expert evidence in the repository to the team level: how a team, not just an individual, runs reliable Agents.

## Goal

A team that runs Agents in production needs the same properties as a team that runs a critical service:

- Every Agent, prompt, tool, and dataset has a named owner and at least two backups.
- Every change is reviewed, evaluated, and traceable.
- Every incident can be routed to an owning team and becomes a regression case.
- Anyone can onboard in days, not months, because permissions, evals, and runtimes are pre-provisioned.

The individual-expert path proves that one person can run a reliable Agent. This guide makes that property independent of any single person.

## 1. Ownership Model

Assign explicit owners so no module depends on one person.

| Role | Responsibilities |
| --- | --- |
| Service owner | Accountable for the Agent's availability, cost, and release decisions |
| Tool/catalog owner | Maintains tool definitions, risk classes, and the allowlist |
| Eval owner | Maintains golden, regression, and safety sets for one or more Agents |
| Safety reviewer | Reviews destructive-action, permission-change, and payment-like paths |
| On-call | Responds to pages and drives the incident to resolution or escalation |
| Rotating maintainers | Share module maintenance on a fixed rotation |

- Every module needs at least two backups.
- Rotate maintainers on a fixed schedule (for example, every two weeks) so knowledge does not concentrate.
- Backups must have made a real review or run change recently, not just been listed on paper.

## 2. Agent Topology

Choose a shared-runtime or per-team-runtime model deliberately.

- Shared runtime: one runtime serves many Agents. Lower cost and simpler ops, but blast radius is shared and tenant isolation must be explicit.
- Per-team runtimes: each team runs its own runtime. Stronger isolation and independent release cadence, at higher operational cost.
- Start with one shared runtime and split runtimes when isolation, release cadence, or cost accounting demands it.

Name everything with a consistent namespace so routing, billing, and evals can identify the owner:

| Asset | Namespace | Example |
| --- | --- | --- |
| Agent | `org/team/agent` | `acme/billing/refund-agent` |
| Prompt | `org/team/agent/prompt/name@version` | `acme/billing/refund-agent/prompt/main@2026-09` |
| Tool | `org/team/tool/name` | `acme/billing/tool/refund` |
| Dataset | `org/team/dataset/name@version` | `acme/billing/dataset/refund-golden@v3` |
| Eval | `org/team/agent/eval/name@version` | `acme/billing/refund-agent/eval/safety@v1` |

## 3. Tool Access Control

Treat tools as the main security and reliability surface.

- Maintain a single MCP server catalog: server, tool list, version, and owner.
- Enforce a tool allowlist per Agent. No tool runs unless it is allowlisted.
- Define permission scopes narrowly, not per-user wide tokens.

Classify every tool by risk class:

| Risk class | Examples | Approval needed |
| --- | --- | --- |
| Read-only | search, retrieve, read | No |
| Reversible write | draft, update, flag | No, but audited |
| Irreversible write | publish, replace, migrate | Yes |
| Payment-like | refund, charge, order | Yes |
| Permission change | grant, invite, role | Yes, safety review |
| Destructive | delete, purge, terminate | Yes, safety review + confirmation |

Approval workflow:

1. Agent requests a scoped, one-time token for the action.
2. Reviewer approves or rejects with a reason.
3. Execution is logged to the audit log with the request id.
4. The token expires after use or after a short TTL.

- Write every tool call to the audit log: who, what, when, risk class, decision, and trace id.
- Revocation must be immediate and independent of the Agent's runtime (revoke the token, not the Agent).

## 4. Model And Provider Policy

- Maintain a model registry: model id, provider, version, capabilities, cost per token, and supported fallback order.
- Pin provider and SDK versions in code and CI. A moving dependency is a silent behavior change.
- Define fallback order explicitly (primary, first fallback, second fallback) and evaluate the fallback path before rollout.
- Set budget guardrails per Agent: per-request, per-day, and per-team budgets. Enforce at the gateway, not only in code.
- Charge costs to a named owner and budget line so cost surprises are routed, not ignored.
- Require refusal and safety evals against the new model before rollout.
- Roll out changes with canary or shadow traffic:

| Method | Traffic | Use when |
| --- | --- | --- |
| Shadow | 0% user-visible | Comparing logs and quality offline |
| Canary | 5-25% | Confidence from real traffic with bounded risk |
| Full | 100% | Evals, canary, and rollback are proven |

## 5. Eval Ownership

Evals are the release gate, and they must be owned like code.

- Maintain shared golden sets: core tasks every Agent must pass.
- Maintain regression sets: every production incident or failure becomes a case.
- Maintain safety sets: injection, destructive-action, refusal, and permission-change cases.
- Give every eval set an owner and at least two backups.
- Refresh cadence: re-run and review sets on a schedule (for example, quarterly) and whenever a dependency changes.
- Release gates: a change ships only when blocking evals pass, budgets are within limits, and traces are complete.
- Store replayable traces: dataset version, prompt version, model version, tool versions, and outputs, so any result can be reproduced.

## 6. Observability And Incident Routing

- Publish a trace contract that every runtime must emit: request, tool calls, retrieval, model, and final answer fields with a stable schema.
- Define severity levels:

| Severity | Meaning | Response |
| --- | --- | --- |
| S1 | Production Agent unusable or unsafe action possible | Page on-call immediately |
| S2 | Degraded quality or blocked non-critical path | Fix within business hours |
| S3 | Minor issue, no user impact | Track and schedule |

- Run a documented on-call rotation with an owning team per Agent.
- Route incidents by namespace: the service owner receives the alert and escalates to tool, eval, or platform owners.
- Postmortem policy: every S1 and S2 gets a postmortem with owner, due date, and prevention action within a fixed window.
- Regression prevention: every postmortem produces a new eval case, guardrail, trace field, or rollback note.

## 7. Security

- Secrets: store in a secrets manager, inject at runtime, rotate on a schedule, and never bake into prompts or images.
- Tenant isolation: enforce isolation between teams and between user sessions at the platform level, not in prompts.
- PII redaction: redact PII in traces and logs by default; keep raw data only in access-controlled stores.
- Prompt injection defense at the platform level: separate instructions from data, flag injected instructions, and test with injection evals in CI.
- Destructive-action confirmation: require a human confirmation step and a safety review for every destructive, permission-change, or payment-like action.

## 8. Onboarding

A new contributor should reach a safe first contribution in days.

- New contributor checklist: repo access, dev runtime, local eval run, tool catalog access, and a named mentor.
- Permission provisioning: grant the minimum scopes the role needs, recorded in the access list.
- First-issue guidance: label safe, well-scoped first issues and link them to the eval and review workflow.
- Reviewer rotation: require at least two reviewers per module with rotating maintainer coverage.
- Non-Python Lab maintenance: Labs and tooling span Node, Rust, Go, and TypeScript; each language module needs a named maintainer and backups so no language becomes unowned.

## 9. Deprecation

- Retire stale prompts, tools, and models on a fixed policy: announce, freeze, migrate, remove.
- A sync-required workflow keeps docs and examples aligned when APIs change: label the change, open the sync issue, and update mirrors within the SLA.
- Maintenance windows: schedule destructive changes and migrations in announced windows with rollback plans.

## Minimum Team Infrastructure

Before many Agents run in production, a small team must have at least:

- An ownership list: every Agent, tool, dataset, and eval has an owner and two backups.
- A tool allowlist with risk classes and an approval workflow.
- A model registry with pinned versions, fallback order, and budget guardrails.
- Shared golden, regression, and safety evals wired into a release gate.
- A trace contract and an on-call rotation with incident routing.
- An audit log and a secrets manager.
- An onboarding checklist so new members are productive safely.
- A deprecation policy with maintenance windows.

If any of these is missing, the team is not ready to run many Agents in production, no matter how good the individual experts are.

## Related Pages

- Eval playbook: [`evals-playbook.md`](evals-playbook.md)
- Trace contract: [`observability-trace-contract.md`](observability-trace-contract.md)
- Safety checklist: [`safety-checklist.md`](safety-checklist.md)
- Production guides index: [`README.md`](README.md)
- Tool boundary example: [`../../../examples/mcp-tool-boundary/README.md`](../../../examples/mcp-tool-boundary/README.md)
- Observability example: [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md)
- Regression gate Lab: [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md)
- Postmortem template: [`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md)
