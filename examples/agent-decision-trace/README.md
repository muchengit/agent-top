# Agent Decision Trace Exercise

This exercise gives you fictional tool calls and decision points. No API key, external service, or paid connector is needed.

Goal: decide which tool calls an Agent may execute, which need clarification, and which should be blocked.

## Files

- [`tool-calls.jsonl`](tool-calls.jsonl): fictional tool-call scenarios.
- [`decision-log.template.jsonl`](decision-log.template.jsonl): start your own trace here.

## JSONL Shape

Each line in `tool-calls.jsonl` is one JSON object: `id`, `tool`, `args`, and `evidence`. `decision-log.template.jsonl` lines start with the same `id` and blank `decision`, `risk`, `reason`, and `required_evidence` fields for you to fill in.

## Steps

1. Read one scenario at a time from `tool-calls.jsonl`.
2. Copy the matching line into `decision-log.template.jsonl` and fill in:
   - `decision`: `allow`, `clarify`, or `block`.
   - `risk`: `read`, `write`, or `destructive`.
   - `reason`: one sentence.
   - `required_evidence`: what must be verified before execution.
3. Compare your decisions with the answer key below.
4. Change one rule: for example, make all writes require approval. Rerun the decisions and note which outcomes change.

## Answer Key

| ID | Expected decision | Why |
| --- | --- | --- |
| read_user_profile | allow | Read-only, scoped, actor and user are present. |
| delete_user_account | block | Destructive and irreversible without explicit confirmation. |
| send_email_unknown_sender | clarify | Missing sender and recipient intent are ambiguous. |
| refund_large_order | block | Money movement needs permission and human approval. |
| update_status_ticket | allow | Small write with idempotent update and audit fields. |
| summarize_docs_no_source | clarify | Needs citation or explicit source before factual claims. |

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Tool risk classification.
- Clarification versus automatic action.
- Permission and audit reasoning.
- Evidence requirements before factual or destructive actions.

## Related Reading

- [`../../docs/en/tutorials/quick-navigation.md`](../../docs/en/tutorials/quick-navigation.md)
- [`../../docs/en/concepts/implementation-guide.md`](../../docs/en/concepts/implementation-guide.md)
- [`../../docs/en/skills/README.md`](../../docs/en/skills/README.md)
