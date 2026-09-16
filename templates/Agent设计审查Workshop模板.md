# Agent 设计审查 Workshop 记录模板

## 1. 范围

- Agent 名称：
- 作者：
- 审查日期：
- 主要用户：
- 业务目标：
- 成功指标：
- Non-goals：
- 禁止动作：

## 2. 参与者

| 角色 | 人 | 备注 |
| --- | --- | --- |
| Author |  |  |
| Challenger |  |  |
| Reviewer |  |  |
| Scribe |  |  |

## 3. 架构选择

- System shape: Single call / ReAct / RAG / Tool-using / Multi-agent
- 为什么这样选：
- 为什么不选更简单方案：
- 为什么不选更复杂方案：

## 4. 工具风险表

| Tool | 用途 | Risk | 权限 | 确认 | 审计字段 | 决策 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | Read / Write / Destructive |  |  |  | Allow / Clarify / Block |

## 5. 证据和记忆规则

| 事实类型 | 来源 | Freshness 规则 | 是否 citation | 冲突规则 |
| --- | --- | --- | --- | --- |
| 用户指令 | User turn | 当前请求 | 否 | 当前指令优先 |
| 外部状态 | Tool result |  |  | 工具结果优先于 stale cache |
| 私有知识 | Retrieval |  |  |  |
| 用户偏好 | Memory |  |  |  |

## 6. 评估门禁

| Gate | 通过条件 | Owner |
| --- | --- | --- |
| Correctness |  |  |
| Safety |  |  |
| Tool use |  |  |
| Retrieval / memory |  |  |
| Cost / latency |  |  |
| Rollback |  |  |

## 7. 未决问题

- [ ] 
- [ ] 
- [ ] 

## 8. 审查结果

- Verdict: Approve / Approve with conditions / Rework / Stop
- 必须修改：
- Owner 和 due date：
- Follow-up issues：
