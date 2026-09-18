# GitHub Agent Review Exercise

This exercise gives you a fictional pull request review packet. No GitHub account, `gh` CLI, API token, or real repository is needed.

Goal: review the PR in a safe Agent order: status first, diff second, risk third, review comment last.

## Files

- [`pr-context.jsonl`](pr-context.jsonl): fictional PR, issue, checks, and diff metadata.
- [`review-template.jsonl`](review-template.jsonl): start your review notes here.

## JSONL Shape

Each line is one JSON object: `pr-context.jsonl` records `pr_id`, `issue`, `ci`, `diff_scope`, `tests`, and `risk`; `review-template.jsonl` starts with `pr_id` and blank `decision`, `order`, `risk`, and `comment`.

## Steps

1. Read the PR context.
2. Fill in:
   - `decision`: `approve`, `request_changes`, or `needs_more_evidence`.
   - `order`: the checks you would inspect in order.
   - `risk`: the main safety, quality, or scope risk.
   - `comment`: one review comment for the PR.
3. Compare with the answer key below.
4. Change one rule: review must read failing CI before diff. Does the decision change?

## Answer Key

| PR | Recommended decision | Main reason |
| --- | --- | --- |
| pr_1 | needs_more_evidence | CI is still running, so diff review cannot decide safety yet. |
| pr_2 | request_changes | The PR changes auth handling without linking the issue that requested the change. |
| pr_3 | approve | Checks pass, diff is small, tests cover the bug, and the issue scope matches. |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [review reference material](../../docs/en/cases/enterprise-multi-tool-agent.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- Platform-native Agent review should check status, CI, diff, and issue context before commenting.
- A PR review is incomplete without identifying scope drift, failing checks, or missing tests.
- MCP tools should carry permission and audit context close to execution.
- The final review comment should state the smallest evidence needed to approve or request changes.

## Related Reading

- [`../../docs/en/concepts/implementation-guide.md`](../../docs/en/concepts/implementation-guide.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
