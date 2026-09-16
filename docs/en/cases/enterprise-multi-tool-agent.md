---
title: Enterprise Multi-Tool Agent Case
validated_date: 2026-09-16
i18n-key: cases-enterprise-multi-tool-agent
last-synced: 2026-09-16
---

# Enterprise Multi-Tool Agent Case

## Scenario

A company Agent queries orders, updates tickets, checks policies, and sends customer messages.

## Architecture

```mermaid
flowchart TD
  User --> Router
  Router --> RiskClassifier
  RiskClassifier --> ToolGateway
  ToolGateway --> Policy
  ToolGateway --> OrderSystem
  ToolGateway --> Ticketing
  ToolGateway --> MessageAPI
  ToolGateway --> Verifier
  Verifier --> User
```

## Key Decisions

- Every tool has read, write, or destructive classification.
- Destructive actions require confirmation.
- Tool calls are logged with request ID and actor.
- Ambiguous tool arguments trigger clarification.
- Empty tool result is different from tool failure.

## Failure Modes

- User asks for a refund but lacks account context.
- Tool returns success for the wrong tenant.
- Message API succeeds but ticket update fails.
- Policy lookup is stale.

## Evaluation

Track:

- Correct tool selection.
- Permission-denied accuracy.
- Confirmation accuracy.
- Trace completeness.
- Tool failure recovery.

## Portfolio Narrative

I designed a tool-using Agent with explicit risk boundaries. The key was not making the model more powerful; it was constraining tool execution with permissions, validation, traces, and rollback.
