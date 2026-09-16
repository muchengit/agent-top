# Model Gateway Evidence Exercise

This exercise uses fictional gateway decisions. No API key, gateway, model provider, or local inference server is needed.

Goal: decide whether model routing evidence is complete enough for release, rollback, or cost investigation.

## Files

- [`gateway-decisions.jsonl`](gateway-decisions.jsonl): fictional model gateway decisions.

## Steps

1. Read each decision event.
2. Identify whether evidence is complete enough for a release decision.
3. Mark the owner: `release`, `runtime`, `model`, `tool`, or `budget`.
4. Decide the next action: `release`, `block`, `warn`, `degrade`, or `postmortem`.
5. Add one missing field for each blocked or warned event.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Route lacks provider/model | model | trace_field + block |
| Fallback used without fallback provider | runtime | trace_field + rollback |
| Budget decision is `block` but retry continued | budget | postmortem + rollback |
| Runtime timeout lacks latency evidence | runtime | trace_field |

## Learning Outcomes

- A model call is a release decision when it changes cost, latency, safety, or fallback behavior.
- Gateway evidence must include the actual model hit, not only the intended model.
- Fallback, retry, rate limit, and budget decisions need replayable fields.
- Inference runtime metrics complement prompt traces; neither replaces the other.

## Related Reading

- [`../../docs/en/production/cost-stability-operations.md`](../../docs/en/production/cost-stability-operations.md)
- [`../../docs/en/production/observability-trace-contract.md`](../../docs/en/production/observability-trace-contract.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)
