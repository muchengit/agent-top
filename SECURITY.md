# Security Policy

Agent-Top is a learning repository. Do not commit real secrets, tokens, production datasets, private traces, or customer data.

## Reporting Vulnerabilities

Report sensitive issues privately through the repository security contact configured by maintainers. Do not open public issues for secrets, credential leaks, or exploit details.

## Lab Safety

- Labs should run locally without API keys.
- Tool examples should model side effects instead of calling real production systems.
- Destructive examples must include confirmation or guardrail explanations.
- Framework-specific code must include `validated_date` and `tested_against`.

## Contributing Secure Examples

Include:

- Auth or permission boundary.
- Input validation.
- Output validation where relevant.
- Tool allowlist or classification.
- Rate, cost, and token limits.
- Rollback or recovery path.
- Observability notes.
- Redaction guidance for logs.

## Incident Handling

If an issue affects published guidance:

1. Mark the affected content as risky.
2. Add or update the correction.
3. Add regression tests or eval notes where relevant.
4. Record the follow-up in a postmortem-style issue or PR.
