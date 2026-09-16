# Agent Design Review Workshop Notes

## 1. Scope

- Agent name:
- Author:
- Review date:
- Primary user:
- Business goal:
- Success metric:
- Non-goals:
- Denied actions:

## 2. Participants

| Role | Person | Notes |
| --- | --- | --- |
| Author |  |  |
| Challenger |  |  |
| Reviewer |  |  |
| Scribe |  |  |

## 3. Architecture Choice

- System shape: Single call / ReAct / RAG / Tool-using / Multi-agent
- Why this shape:
- Why not simpler:
- Why not larger:

## 4. Tool Risk Table

| Tool | Purpose | Risk | Permission | Confirmation | Audit Fields | Decision |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Read / Write / Destructive |  |  |  | Allow / Clarify / Block |

## 5. Evidence and Memory Rules

| Fact Type | Source | Freshness Rule | Citation Required | Conflict Rule |
| --- | --- | --- | --- | --- |
| User instruction | User turn | Current request | No | Current request wins |
| External state | Tool result |  |  | Tool result beats stale cache |
| Private knowledge | Retrieval |  |  |  |
| User preference | Memory |  |  |  |

## 6. Evaluation Gates

| Gate | Passing Condition | Owner |
| --- | --- | --- |
| Correctness |  |  |
| Safety |  |  |
| Tool use |  |  |
| Retrieval / memory |  |  |
| Cost / latency |  |  |
| Rollback |  |  |

## 7. Open Questions

- [ ] 
- [ ] 
- [ ] 

## 8. Review Result

- Verdict: Approve / Approve with conditions / Rework / Stop
- Required changes:
- Owners and due dates:
- Follow-up issues:
