---
title: Production Checklist
validated_date: 2026-09-16
i18n-key: quick-reference-production-checklist
last-synced: 2026-09-16
---

# Production Checklist

Use this checklist before release, during incidents, and after postmortems.

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
- [ ] PII handling and data retention are documented.
- [ ] Rate limits and retry budgets are defined.
- [ ] Model/provider failure fallback is tested.
- [ ] Regression gate blocks safety and eval failures.
- [ ] Human escalation path is documented.

## During Incident

- [ ] Disable risky action path.
- [ ] Freeze writes if needed.
- [ ] Inspect traces.
- [ ] Identify root cause.
- [ ] Add regression eval.
- [ ] Document postmortem.
- [ ] Notify stakeholders with blast radius.
- [ ] Capture before/after evidence from traces and logs.
- [ ] Confirm rollback or mitigation is effective.

## After Incident

- [ ] Fix owner and due date assigned.
- [ ] Rollback tested.
- [ ] Evals updated.
- [ ] Documentation updated.
- [ ] Follow-up monitored.
- [ ] Preventive guardrail added.
- [ ] Action items linked from postmortem.
