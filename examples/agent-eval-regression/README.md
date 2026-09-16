# Agent Evaluation Regression Exercise

This exercise gives you a fictional prompt regression report. No API key, evaluation service, model call, or external benchmark is needed.

Goal: decide whether a prompt/tool/model change should launch, hold, or roll back.

## Files

- [`fixtures.jsonl`](fixtures.jsonl): fictional eval fixtures.
- [`runs.jsonl`](runs.jsonl): prompt-version results.
- [`regression-template.jsonl`](regression-template.jsonl): start your gate decisions here.

## Steps

1. Read one fixture and both runs.
2. Fill in:
   - `decision`: `launch`, `hold`, or `rollback`.
   - `reason`: one sentence explaining the regression or fix.
   - `required_evidence`: trace, source, test, or human review needed.
   - `owner`: `eval`, `prompt`, `data`, or `tooling`.
3. Compare with the answer key below.
4. Change one rule: any safety-critical fixture failure blocks launch. Which decisions change?

## Answer Key

| Fixture | Recommended decision | Reason |
| --- | --- | --- |
| fixture_1 | launch | v2 improves answer usefulness without dropping required evidence. |
| fixture_2 | hold | v2 changes the answer but does not record the new source version. |
| fixture_3 | rollback | v2 ignores a deleted user preference. |
| fixture_4 | rollback | v2 calls a write tool without explicit approval evidence. |

## Learning Outcomes

- Regression reports need dataset version, run metadata, pass/fail rules, and owner routing.
- Safety-critical regressions should block launch even when aggregate metrics improve.
- Prompt optimization should compare versions against fixtures, not rely on one demo response.
- A gate decision should include the smallest evidence needed to prove the fix.

## Related Reading

- [`../../docs/en/production/evals-playbook.md`](../../docs/en/production/evals-playbook.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
- [`../../docs/en/tutorials/open-source-inspirations.md`](../../docs/en/tutorials/open-source-inspirations.md)
