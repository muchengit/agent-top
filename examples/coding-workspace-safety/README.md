# Coding Workspace Safety Exercise

This exercise gives you fictional coding-Agent changes. No API key, IDE plugin, repository mutation, paid service, or real customer code is needed.

Goal: decide which changes should be applied directly, which require a patch review, and which need rollback or explicit approval.

## Files

- [`changes.jsonl`](changes.jsonl): fictional Agent changes.
- [`decisions.template.jsonl`](decisions.template.jsonl): start your own decision log here.

## Steps

1. Read one change.
2. Fill in:
   - `decision`: `apply_patch`, `review_patch`, `block`, or `rollback`.
   - `verification`: the smallest command or check that would prove the change.
   - `reason`: one sentence.
   - `follow_up`: rollback, test, or human approval if needed.
3. Compare your decisions with the answer key below.
4. Change one rule: every file write must create a reviewable patch first. Which decisions change?

## Answer Key

| ID | Expected decision | Verification | Why |
| --- | --- | --- | --- |
| add_unit_test | apply_patch | `python -m unittest tests.test_new_feature` | Test-only change with deterministic proof. |
| refactor_api_contract | review_patch | API contract review plus targeted tests | Public behavior may change; patch review reduces blast radius. |
| rewrite_migration | block | Migration dry-run and rollback plan | Database migrations are destructive without approval. |
| direct_prod_config | block | Config diff and change approval | Direct production config changes bypass review and rollback. |
| flaky_retry_loop | rollback | Retry count and latency assertions | Retry loop can hide failures and inflate cost. |

## Learning Outcomes

- Patch-first editing is safer than direct mutation.
- Every code-changing Agent step needs the smallest meaningful verification command.
- Destructive changes need approval, dry-run, and rollback.
- Coding-Agent decisions should be recorded as traceable evidence.

## Related Reading

- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/concepts/implementation-guide.md`](../../docs/en/concepts/implementation-guide.md)
