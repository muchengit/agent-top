# Coding Task Navigation Exercise

This exercise adapts the task-first navigation pattern seen in mature coding-agent tutorial collections. It teaches learners to start from a concrete request, choose the smallest useful entry point, identify the expected artifact, verify the result, and state a stop condition.

## Files

- [`task-entries.jsonl`](task-entries.jsonl): task-first entries.
- [`requests.jsonl`](requests.jsonl): learner requests.
- [`task-map.template.jsonl`](task-map.template.jsonl): template for your answers.

## JSONL Shape

Each line is one JSON object: `task-entries.jsonl` records `entry_id`, `task`, `entry_point`, `expected_artifact`, `verification`, and `stop_condition`; `requests.jsonl` records `request_id`, `request`, and `answer_entry_id`; `task-map.template.jsonl` starts with `request_id` and blank `entry_id`, `entry_point`, `expected_artifact`, `verification`, and `stop_condition`.

## Steps

1. Read one request.
2. Pick the best task entry from `task-entries.jsonl`.
3. Fill `task-map.template.jsonl` with:
   - `entry_id`
   - `entry_point`
   - `expected_artifact`
   - `verification`
   - `stop_condition`
4. Compare with the answer key below.
5. Change one rule: no task may have more than one expected artifact. Which entries need splitting?

## Answer Key

| Request ID | Entry ID | Best entry point |
| --- | --- | --- |
| request_1 | mcp_tool_boundary | `docs/en/l2-single-agent-mcp.md`, `examples/data-source-policy/README.md`, and `labs/l2/single_agent_mcp/` |
| request_2 | memory_vs_evidence | `examples/memory-vs-evidence/README.md`, `docs/en/concepts/long-term-memory.md`, and `docs/en/concepts/rag-memory-mcp-flow.md` |
| request_3 | patch_review_safety | `examples/coding-workspace-safety/README.md`, `docs/en/concepts/implementation-guide.md`, and `templates/postmortem-template.md` |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [nav reference material](../../docs/en/tutorials/quick-navigation.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- A task-first index should lead directly to an artifact the learner can produce.
- Verification should be specific, such as tests, a decision log, or a reviewable trace.
- Stop conditions prevent tutorial bloat and make progress measurable.
- Skills teach how to do a workflow; MCP exposes tools; plugins package capabilities; connectors add account context.

## Related Reading

- [`../../docs/en/tutorials/quick-navigation.md`](../../docs/en/tutorials/quick-navigation.md)
- [`../../docs/en/tutorials/open-source-inspirations.md`](../../docs/en/tutorials/open-source-inspirations.md)
- [`../coding-workspace-safety/README.md`](../coding-workspace-safety/README.md)
