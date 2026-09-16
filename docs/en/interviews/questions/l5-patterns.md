---
title: L5 Pattern Questions
validated_date: 2026-09-16
i18n-key: interviews-questions-l5-patterns
last-synced: 2026-09-16
---

# L5 Pattern Questions

## 1. What makes a reusable Agent pattern valuable?

Expected answer:

- It solves a repeated problem across contexts.
- It has stable inputs and outputs.
- It defines failure modes.
- It includes safety and verification.
- It is easier to maintain than framework-specific code.

Listen for:

- Pattern boundaries.
- Reusability beyond one project.
- Anti-framework tribalism.

Follow-up:

- When should a pattern become a framework?

## 2. How do you evaluate whether to build a framework or use an existing one?

Expected answer:

- Build only when existing frameworks hide a recurring problem or make failure modes unclear.
- Use existing frameworks when they cover state, tooling, observability, and ecosystem needs.
- Keep framework code isolated and version-anchored.
- Test for adoption and maintenance cost.

Listen for:

- Maintenance awareness.
- Ecosystem judgment.
- Version and dependency risk.

Follow-up:

- What evidence would convince you the framework is no longer worth maintaining?

## 3. Design a pattern for high-risk tool execution.

Expected answer:

- Classify risk by reversibility, blast radius, and data sensitivity.
- Run preflight checks before execution.
- Require confirmation or approval for destructive actions.
- Emit audit logs.
- Include rollback or compensation.
- Verify after execution.

Listen for:

- Safety before execution.
- Auditability.
- Verification after action.

Follow-up:

- What does a good rollback hint look like for a payment tool?

## 4. How do you prevent framework churn from destroying documentation?

Expected answer:

- Separate stable concepts from framework-specific examples.
- Keep framework code in Labs.
- Add `validated_date` and `tested_against`.
- Automate stale detection and sync-required labels.
- Archive deprecated content with replacement links.

Listen for:

- Anti-staleness process.
- Documentation architecture.
- Maintainer sustainability.

Follow-up:

- How would you explain a pattern to both beginners and maintainers?

## 5. What kind of open-source contribution proves expert-level Agent capability?

Expected answer:

- A pattern, Lab, or framework contribution with tests and docs.
- A production-relevant example with failure modes.
- A maintainer-ready PR with clear trade-offs.
- A paper, talk, or standard-setting contribution when relevant.

Listen for:

- Evidence of influence, not just usage.
- Ability to teach and maintain.
- Contribution quality.

Follow-up:

- What would you cut from your contribution to make it easier to maintain?
