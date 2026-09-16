---
title: Agent 设计审查 Workshop
validated_date: 2026-09-17
i18n-key: concepts-design-review-workshop
last-synced: 2026-09-17
---

# Agent 设计审查 Workshop

用这个 Workshop 在 45 分钟内审查一个 Agent 想法。

## 角色

- Author：说明方案。
- Challenger：挑战边界和失败场景。
- Reviewer：检查证据、安全、运维。
- Scribe：记录决策和 owner。

## 输入

- 一页系统目标。
- 用户和 tenant 模型。
- Tool 列表及 read/write/destructive 标签。
- 数据源和 freshness 规则。
- 已知失败案例。
- 当前或拟定的 eval plan。

## 45 分钟流程

| 时间 | 活动 | 输出 |
| --- | --- | --- |
| 5 分钟 | 说明任务和 non-goals | 一句话成功指标 |
| 10 分钟 | 画架构和数据流 | 最小系统图 |
| 10 分钟 | 审查 tools、MCP、权限 | 风险表 |
| 10 分钟 | 审查 memory、evidence、hallucination | source precedence 规则 |
| 5 分钟 | 审查 evals 和发布门禁 | pass/fail 条件 |
| 5 分钟 | 决定下一步 | Approve、conditions、rework 或 stop |

## 最容易改进设计的问题

- 系统能否安全地说“我不知道”？
- 哪个动作不可逆？
- 两个工具冲突时怎么办？
- 哪些 claim 必须有 citation？
- 哪些 trace fields 能证明事故路径？
- 哪些变更必须支持 rollback？
- 模型 confidence 下降时会怎样？

## 输出模板

```markdown
# Review Result

- Verdict: Approve / Approve with conditions / Rework / Stop
- Success metric:
- Architecture choice:
- Tool risk decisions:
- Required evidence:
- Eval gates:
- Rollback path:
- Owners and dates:
```

## 相关页面

- 审查清单：[`Agent设计审查清单.md`](Agent设计审查清单.md)
- 实施手册：[`核心Agent实施手册.md`](核心Agent实施手册.md)
- 系统蓝图：[`Agent系统蓝图.md`](Agent系统蓝图.md)
