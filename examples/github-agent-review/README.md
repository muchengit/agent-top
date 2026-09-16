# GitHub Agent Review Exercise

This exercise gives you a fictional pull request review packet. No GitHub account, `gh` CLI, API token, or real repository is needed.

Goal: review the PR in a safe Agent order: status first, diff second, risk third, review comment last.

## Files

- [`pr-context.jsonl`](pr-context.jsonl): fictional PR, issue, checks, and diff metadata.
- [`review-template.jsonl`](review-template.jsonl): start your review notes here.

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

## Learning Outcomes

- Platform-native Agent review should check status, CI, diff, and issue context before commenting.
- A PR review is incomplete without identifying scope drift, failing checks, or missing tests.
- MCP tools should carry permission and audit context close to execution.
- The final review comment should state the smallest evidence needed to approve or request changes.

## Related Reading

- [`../../docs/en/concepts/implementation-guide.md`](../../docs/en/concepts/implementation-guide.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
