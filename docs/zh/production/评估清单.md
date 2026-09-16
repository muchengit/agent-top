---
i18n-key: production-evals-checklist
last-synced: 2026-09-16
validated_date: 2026-09-16
---

Agent 评估清单

Evals 是 Agent 行为发布门禁。

## 必测类别

### Golden Prompts

同一用户请求在模型或 prompt 变化后仍保持可接受行为。

### Tool Usage

- 正确工具。
- 必填参数。
- 无效参数拒绝。
- 危险工具需确认。
- Tool failures 显式处理。

### Retrieval

- 正确 source。
- 不滥用 irrelevant source。
- stale document 被检测或拒绝。
- no-answer case。

### Safety

- Prompt injection。
- Out-of-scope refusal。
- Sensitive data non-leak。
- Destructive action without approval 被阻断。

### 记忆

- 相关 preference 被使用。
- Stale preference 不被盲信。
- Sensitive data 不存储。

### Observability

- Trace 包含 request id、prompt version、tool calls、retrieved sources、final answer。
- Latency 和 token cost。
- Failure reason 与 empty answer 区分。

## 回归触发

Prompt、model、tool schema、retrieval source、memory policy、safety guardrail、router、orchestrator 变化都应重跑。

## 阻断发布

- Critical safety eval fail。
- Golden prompt fail。
- Destructive action without approval。
- Required trace field missing。
- Rollback plan missing。
- Cost/latency over threshold without approval。

