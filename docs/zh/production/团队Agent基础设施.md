---
title: 团队 Agent 基础设施
capability_level: L5
validated_date: 2026-09-17
i18n-key: production-team-agent-infrastructure
last-synced: 2026-09-17
---

# 团队 Agent 基础设施

生产指南是 Agent 系统的上线准备层。本指南把仓库中已有的个人专家证据扩展到团队层面：一个团队（而不只是个人）如何可靠地运行 Agent。

## 目标

在团队中运行 Agent，需要的性质与运行关键服务相同：

- 每个 Agent、prompt、tool 和 dataset 都有具名 owner 和至少两个备份。
- 每个变更都经过 review、eval 和 trace。
- 每个事故都能路由到负责团队，并变成 regression case。
- 任何人几天内就能完成 onboarding，因为权限、evals 和 runtime 都是预置好的。

个人专家路径证明一个人可以运行可靠的 Agent。本指南让这个性质不再依赖任何单一个人。

## 1. 所有权模型

分配明确的 owner，让任何模块都不依赖单一个人。

| 角色 | 职责 |
| --- | --- |
| Service owner | 对 Agent 的可用性、成本和发布决策负责 |
| Tool/catalog owner | 维护 tool 定义、风险分级和 allowlist |
| Eval owner | 维护一个或多个 Agent 的 golden、regression 和 safety 集 |
| Safety reviewer | 审查 destructive-action、permission-change 和 payment-like 路径 |
| On-call | 响应告警，把事故推进到解决或升级 |
| Rotating maintainers | 按固定轮换共享模块维护 |

- 每个模块至少有两个备份。
- 按固定节奏轮换维护者（例如每两周），避免知识集中。
- 备份必须是最近真实做过 review 或运行过变更的人，而不是纸面列名。

## 2. Agent 拓扑

有意识地选择 shared runtime 或 per-team runtime 模型。

- Shared runtime：一个 runtime 服务多个 Agent。成本低、运维简单，但爆炸半径共享，必须显式做 tenant isolation。
- Per-team runtimes：每个团队运行自己的 runtime。隔离更强、发布节奏独立，但运维成本更高。
- 从单个 shared runtime 开始，当隔离、发布节奏或成本核算要求时再拆分 runtime。

用一致的 namespace 命名所有资产，让路由、计费和 evals 都能识别 owner：

| 资产 | Namespace | 示例 |
| --- | --- | --- |
| Agent | `org/team/agent` | `acme/billing/refund-agent` |
| Prompt | `org/team/agent/prompt/name@version` | `acme/billing/refund-agent/prompt/main@2026-09` |
| Tool | `org/team/tool/name` | `acme/billing/tool/refund` |
| Dataset | `org/team/dataset/name@version` | `acme/billing/dataset/refund-golden@v3` |
| Eval | `org/team/agent/eval/name@version` | `acme/billing/refund-agent/eval/safety@v1` |

## 3. Tool 访问控制

把 tool 当作主要的安全和可靠性面。

- 维护单一 MCP server catalog：server、tool 列表、版本和 owner。
- 每个 Agent 强制执行 tool allowlist。不在 allowlist 中的 tool 不运行。
- 权限 scope 要收窄，不要用全局宽 token。

按风险分级所有 tool：

| 风险等级 | 示例 | 是否需要审批 |
| --- | --- | --- |
| Read-only | search、retrieve、read | 否 |
| Reversible write | draft、update、flag | 否，但记录审计 |
| Irreversible write | publish、replace、migrate | 是 |
| Payment-like | refund、charge、order | 是 |
| Permission change | grant、invite、role | 是，需要 safety review |
| Destructive | delete、purge、terminate | 是，需要 safety review + 确认 |

审批流程：

1. Agent 为动作申请带 scope 的一次性 token。
2. Reviewer 批准或拒绝并说明理由。
3. 执行写入审计日志，包含 request id。
4. Token 使用后立即过期，或短 TTL 过期。

- 每次 tool 调用都写入审计日志：谁、什么、何时、风险等级、决策和 trace id。
- 撤销必须即时生效且独立于 Agent runtime（撤销 token，而不是撤销 Agent）。

## 4. 模型与 Provider 策略

- 维护模型注册表：model id、provider、版本、能力、每 token 成本和支持的 fallback 顺序。
- 在代码和 CI 中固定 provider 与 SDK 版本。移动的依赖就是静默的行为变更。
- 显式定义 fallback 顺序（primary、第一 fallback、第二 fallback），并在 rollout 前评估 fallback 路径。
- 为每个 Agent 设置预算护栏：per-request、per-day 和 per-team 预算。在 gateway 层强制，而不是只在代码里。
- 成本记到具名 owner 和预算项，让成本异常能被路由而不是被忽略。
- rollout 前要求对新模型跑 refusal 和 safety evals。
- 用 canary 或 shadow 流量发布变更：

| 方式 | 流量 | 使用场景 |
| --- | --- | --- |
| Shadow | 0% 用户可见 | 离线对比日志和质量 |
| Canary | 5-25% | 真实流量验证且有界风险 |
| Full | 100% | evals、canary 和 rollback 都已验证 |

## 5. Eval 所有权

Evals 是发布门禁，必须像代码一样被拥有。

- 维护共享 golden 集：每个 Agent 必须通过的核心任务。
- 维护 regression 集：每个生产事故或失败都变成一个 case。
- 维护 safety 集：injection、destructive-action、refusal 和 permission-change 用例。
- 每个 eval 集都有 owner 和至少两个备份。
- 刷新节奏：按计划（例如每季度）以及依赖变更时重跑并 review 数据集。
- 发布门禁：只有 blocking evals 通过、预算在限额内、trace 完整时才能发布。
- 保存可回放 trace：dataset version、prompt version、model version、tool versions 和输出，任何结果都可以复现。

## 6. 可观测性与事故路由

- 发布每个 runtime 都必须输出的 trace contract：request、tool calls、retrieval、model 和 final answer 字段，schema 稳定。
- 定义严重级别：

| 级别 | 含义 | 响应 |
| --- | --- | --- |
| S1 | 生产 Agent 不可用或可能发生不安全动作 | 立即 page on-call |
| S2 | 质量下降或非关键路径受阻 | 工作时间内修复 |
| S3 | 小问题，无用户影响 | 记录并排期 |

- 每个 Agent 都有文档化的 on-call rotation 和负责团队。
- 按 namespace 路由事故：service owner 接收告警，并升级给 tool、eval 或 platform owner。
- Postmortem 政策：每个 S1 和 S2 在固定时间内产出 postmortem，包含 owner、due date 和 prevention action。
- Regression 预防：每个 postmortem 都产出一个新的 eval case、guardrail、trace field 或 rollback note。

## 7. 安全

- Secrets：存放在 secrets manager，运行时注入，按计划轮换，绝不写进 prompt 或镜像。
- Tenant isolation：在平台层强制团队之间和用户会话之间的隔离，而不是靠 prompt。
- PII redaction：traces 和日志默认脱敏 PII；原始数据只放在受控访问的存储中。
- 平台级 prompt injection 防御：把指令与数据分离，标记注入指令，并在 CI 中用 injection evals 测试。
- Destructive-action confirmation：每个 destructive、permission-change 或 payment-like 动作都需要人工确认步骤和 safety review。

## 8. Onboarding

新贡献者应在几天内完成安全的第一次贡献。

- 新贡献者 checklist：仓库访问、开发 runtime、本地 eval 运行、tool catalog 访问和具名 mentor。
- 权限开通：按角色授予最小 scope，并记录在访问清单中。
- First-issue 指引：给安全、边界清晰的 first issue 打标签，并链接到 eval 和 review 流程。
- Reviewer 轮换：每个模块至少两个 reviewer，配合轮换的 maintainer 覆盖。
- 非 Python Lab 维护：Labs 和工具链涉及 Node、Rust、Go 和 TypeScript；每种语言模块都要有具名 maintainer 和备份，让任何语言都不会无人负责。

## 9. 弃用

- 按固定政策淘汰 stale prompt、tool 和 model：announce、freeze、migrate、remove。
- 用 sync-required 工作流保持文档和示例与 API 变更一致：给变更打标签、开 sync issue、在 SLA 内更新镜像。
- 维护窗口：破坏性变更和迁移在公告的窗口内进行，并带 rollback 计划。

## 最小团队基础设施

在许多 Agent 上生产前，小团队至少要具备：

- 所有权清单：每个 Agent、tool、dataset 和 eval 都有 owner 和两个备份。
- 带风险分级和审批流程的 tool allowlist。
- 固定版本、fallback 顺序和预算护栏的模型注册表。
- 接入发布门禁的共享 golden、regression 和 safety evals。
- trace contract、on-call rotation 和事故路由。
- 审计日志和 secrets manager。
- 让新成员安全高效的 onboarding checklist。
- 带维护窗口的弃用政策。

缺少其中任何一项，团队就不具备让多个 Agent 上生产的条件，无论个人专家有多强。

## 相关页面

- Eval Playbook：[`evals-playbook.md`](评估与回归Playbook.md)
- Trace 契约：[`可观测性与Trace契约.md`](可观测性与Trace契约.md)
- 安全清单：[`安全清单.md`](安全清单.md)
- 生产指南索引：[`文档索引.md`](文档索引.md)
- Tool boundary 示例：[`../../../examples/mcp-tool-boundary/README.md`](../../../examples/mcp-tool-boundary/README.md)
- 可观测性示例：[`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md)
- Regression gate Lab：[`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md)
- 监督与事件响应 Lab：[`../../../labs/l5/supervision_incident_response/README.md`](../../../labs/l5/supervision_incident_response/README.md)
- Vibe Coding 规范 Lab：[`../../../labs/l5/vibe_coding_spec/README.md`](../../../labs/l5/vibe_coding_spec/README.md)
- Postmortem 模板：[`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md)
