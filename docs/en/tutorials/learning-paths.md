---
i18n-key: tutorials-learning-paths
last-synced: 2026-09-17
validated_date: 2026-09-17
---

# Learning Paths

Learning paths connect Agent-Top tutorials, Labs, cases, quick references, and portfolio evidence. If you want to complete one concrete task before choosing a route, start with [`quick-navigation.md`](quick-navigation.md).

## Audience and Purpose

- **Primary audience**: learners who want a sequenced route from first LLM call to L5 expert evidence, and mentors who recommend the next step.
- **Purpose**: turn the tutorial tree into five concrete paths, each with explicit exit evidence.
- **Not for**: one-off questions. Use [`reference-map.md`](reference-map.md) or [`quick-navigation.md`](quick-navigation.md) instead.

## How to Use This Document

1. **Assess your evidence.** Check which exit evidence items you already have.
2. **Pick one path.** Finish it before starting another.
3. **Read first, then run.** Tutorials define the concepts; Labs prove them.
4. **Store evidence per path.** Keep one file per path with commands, outputs, and short explanations.
5. **Feed the portfolio.** Each path should produce at least one portfolio entry in [`../portfolio/projects.md`](../portfolio/projects.md).

## Beginner Path: From First Call to One Agent

1. Read [`../l0-first-llm-call.md`](../l0-first-llm-call.md).
2. Run [`../../../labs/l0/first_llm_call/README.md`](../../../labs/l0/first_llm_call/README.md).
3. Read [`../concepts/react-pattern.md`](../concepts/react-pattern.md).
4. Run [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md).
5. Add stop conditions and explain tool-result ambiguity.

Exit evidence:

- One LLM call explained in your own words.
- One ReAct loop run locally.
- One stop-condition explanation.

## Intermediate Path: Reliable Single Agent

1. Read [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md).
2. Run [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md).
3. Run [`../../../labs/l1/guardrail_helpers/README.md`](../../../labs/l1/guardrail_helpers/README.md).
4. Run [`../../../labs/l2/cost_aware_router/README.md`](../../../labs/l2/cost_aware_router/README.md).
5. Write a tool risk classification table.

Exit evidence:

- Tool allowlist.
- Destructive-action confirmation rule.
- Cost or latency-aware routing decision.

## System Path: RAG, Memory, Multi-Agent

1. Read [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md).
2. Read [`../concepts/multi-round-research-discussion.md`](../concepts/multi-round-research-discussion.md).
3. Run [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md).
4. Run [`../../../labs/l3/multi_round_research_discussion/README.md`](../../../labs/l3/multi_round_research_discussion/README.md).
5. Run [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md).

Exit evidence:

- Retrieval eval with required-source case.
- Refusal case for missing evidence.
- Multi-agent route assignment.

## Production Path

1. Read [`../l4-production.md`](../l4-production.md).
2. Read [`../production/evals-checklist.md`](../production/evals-checklist.md).
3. Read [`../production/safety-checklist.md`](../production/safety-checklist.md).
4. Run [`../../../labs/l4/production_postmortem/README.md`](../../../labs/l4/production_postmortem/README.md).
5. Run [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md).

Exit evidence:

- Release gate checklist.
- Incident postmortem with owner and due date.
- Rollback plan.

## Expert Path: Original Pattern

1. Read [`../l5-custom-patterns.md`](../l5-custom-patterns.md).
2. Read [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md).
3. Run [`../../../labs/l5/custom_pattern_lab/README.md`](../../../labs/l5/custom_pattern_lab/README.md).
4. Run [`../../../labs/l5/pattern_catalog/README.md`](../../../labs/l5/pattern_catalog/README.md).
5. Run [`../../../labs/l5/multilingual_pattern_lab/README.md`](../../../labs/l5/multilingual_pattern_lab/README.md).
6. Draft one reusable pattern with safety and verification.
7. Read [`industry-benchmark-and-l5-expert-path.md`](industry-benchmark-and-l5-expert-path.md) and package the work with [`../../../templates/l5-expert-evidence-template.md`](../../../templates/l5-expert-evidence-template.md).

Exit evidence:

- Pattern spec.
- Deterministic Lab.
- Failure-mode section.
- Reviewer-ready contribution notes.
- L5 expert evidence bundle with pattern, governance, evidence, and influence rubric scores.

## Choosing a Path

- **Time-boxed learner**: beginner path in one week, then intermediate.
- **Production engineer**: production path after the system path.
- **Framework author**: expert path, then package with the L5 evidence template.
- **Mentor**: use the exit evidence to place a learner on the next path.

## Common Mistakes and How to Avoid Them

- **Skipping exit evidence** — evidence is what makes a path complete. Do not start the next path until you can show it.
- **Hopping between paths** — paths are cumulative. Pick one and finish before switching.
- **Reading without running** — Labs exist so claims are testable. Run each one locally.
- **Ignoring safety Labs** — guardrail and safety material appears early for a reason; skip it and you will have to relearn it during production.

## Measurable Indicators

- **Completion**: exit evidence for the current path exists.
- **Depth**: each completed Lab has a written explanation, not just a pass.
- **Transfer**: you can run a related case from [`../cases/README.md`](../cases/README.md) without the Lab instructions.
- **Portfolio growth**: each path feeds one entry in [`../portfolio/projects.md`](../portfolio/projects.md).

## Realistic Evidence Example

```markdown
# Intermediate Path Evidence

## Tool Allowlist
- `read_file` — allow, read-only.
- `write_file` — confirm before destructive overwrite.
- `delete_file` — deny by default; requires approval.
- `run_shell` — allow only with explicit allowlist.

## Confirmation Rule
Any tool that can destroy data requires a human confirmation with the exact
target path and a suggested backup command.

## Routing Decision
Small lookups go to the low-latency model; multi-step reasoning goes to the
higher-cost model only when the task needs planning.
```

## Between Paths

- **Beginner → Intermediate**: only when the ReAct loop and stop conditions are explained, not just run.
- **Intermediate → System**: only when the tool risk table exists and one routing decision is justified.
- **System → Production**: only when a retrieval eval and a refusal case exist.
- **Production → Expert**: only when a release gate, postmortem, and rollback plan exist.
- **Expert → Contribution**: package the pattern with the L5 evidence template and open a PR.

## Next Actions Checklist

- [ ] Pick one path based on your current evidence.
- [ ] Read the listed tutorials before running the Labs.
- [ ] Run every Lab locally and record the commands.
- [ ] Produce the exit evidence for the path.
- [ ] Write a short explanation for each completed Lab.
- [ ] Add the resulting project or pattern to your portfolio.

## Path Map at a Glance

| Path | Tutorials | Labs | Exit Evidence |
| --- | --- | --- | --- |
| Beginner | `l0-first-llm-call`, `react-pattern` | `first_llm_call`, `minimal_react_agent` | LLM explanation, ReAct loop, stop condition |
| Intermediate | `l2-single-agent-mcp` | `single_agent_mcp`, `guardrail_helpers`, `cost_aware_router` | allowlist, confirmation rule, routing decision |
| System | `l3-rag-memory-observability`, `multi-round-research-discussion` | `rag_evaluator`, `multi_round_research_discussion`, `multi_agent_supervisor` | retrieval eval, refusal case, route assignment |
| Production | `l4-production`, `evals-checklist`, `safety-checklist` | `production_postmortem`, `regression_gate` | release gate, postmortem, rollback plan |
| Expert | `l5-custom-patterns`, `agent-system-architecture` | `custom_pattern_lab`, `pattern_catalog`, `multilingual_pattern_lab` | pattern spec, deterministic Lab, L5 bundle |

## Mentor Notes

- **Assess, do not assign by level.** Ask the learner which exit evidence they already have, then pick the next path.
- **Demand evidence in writing.** A Lab that passed once is not enough; require a short explanation in the learner's own words.
- **Use the portfolio as the audit trail.** The portfolio index should link each project back to the path that produced it.
- **Pair the expert path with community review.** A pattern is not expert-level until a reviewer can re-run it.

## Troubleshooting Common Stalls

- **ReAct loop never terminates** — revisit stop conditions and tool-result ambiguity before adding more tools.
- **Eval score stays flat** — check that the negative cases actually reach the retrieval step instead of failing early.
- **Postmortem has no owner** — an incident without an owner and due date is not complete evidence.
- **Pattern rejected in review** — the most common cause is a missing failure-mode section; add one before resubmitting.

## Related Quick References

- [`lab-command-cheatsheet.md`](../quick-reference/lab-command-cheatsheet.md)
- [`production-checklist.md`](../quick-reference/production-checklist.md)
- [`architecture-patterns.md`](../quick-reference/architecture-patterns.md)
