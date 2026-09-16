---
title: Production Checklist
validated_date: 2026-09-16
---

# Production Checklist

## Before Release

- [ ] Auth and permissions are defined.
- [ ] Tool allowlist and risk classification exist.
- [ ] Destructive actions require confirmation.
- [ ] Safety evals pass.
- [ ] Golden prompts pass.
- [ ] Trace fields are present.
- [ ] Rollback plan is documented.
- [ ] Cost and latency budgets are set.
- [ ] Incident owner is named.

## During Incident

- [ ] Disable risky action path.
- [ ] Freeze writes if needed.
- [ ] Inspect traces.
- [ ] Identify root cause.
- [ ] Add regression eval.
- [ ] Document postmortem.

## After Incident

- [ ] Fix owner and due date assigned.
- [ ] Rollback tested.
- [ ] Evals updated.
- [ ] Documentation updated.
- [ ] Follow-up monitored.
