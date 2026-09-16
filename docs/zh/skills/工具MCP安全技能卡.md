---
title: 工具与 MCP 安全技能卡
validated_date: 2026-09-16
i18n-key: skill-card-tool-mcp-safety
last-synced: 2026-09-16
---

# 工具与 MCP 安全技能卡

## 技能名称

- English: Tool and MCP Safety
- 中文：工具与 MCP 安全边界
- Level: L2-L4

## 目标

帮助工程师通过受控边界暴露外部动作，包括 validation、permissions、confirmation、traces 和 rollback。

## 适用场景

- Agent 可以读取或写入外部状态。
- Tool call 有 side effects。
- 需要考虑 permissions、idempotency 或 audit。
- 需要解释 tool call 为什么失败，同时不泄露敏感数据。

## 不适用场景

- 任务是纯单次 LLM 回答。
- Tool 只读，且 blast radius 可忽略。
- 你只是在学 prompt formatting。

## 核心知识

- Tool contract：inputs、outputs、errors、side effects。
- read/write/destructive 风险分类。
- MCP 边界：host/client/server 模型、tools/resources/prompts、schemas、transport、auth、audit。
- MCP 本身不是权限系统；permissions 和 audit 应在 gateway、server 或 policy layer 里实现。
- Confirmation 和 human-in-the-loop routes。
- Idempotency、retries、rollback。

## 实践证据

- Lab: [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md)
- Case: [`../cases/企业多工具Agent案例.md`](../cases/企业多工具Agent案例.md)
- Project artifact: 带 risk table 和 audit fields 的 tool gateway design note。

## 审查问题

1. 执行前如何分类 tool call？
2. Tool result 为空但不是 error 时应怎么处理？
3. 如何防止同一个 destructive action 执行两次？

## 常见失败模式

- 把 model output 当作授权决策。
- 记录敏感 request payloads。
- Write tool 已成功但响应解析失败后继续 retry。
- Audit log 缺少 tenant 或 actor context。

## 生产备注

- 使用 gateway 做 validation、permissions 和 audit。
- 把 rate limits 和 mutation gates 放在 tool execution 附近。
- Side-effecting tools 优先使用 idempotency keys。
- 为 denied、retried、partially successful calls 添加 regression evals。

## 相关链接

- Tutorial: [`../L2可靠单Agent与MCP.md`](../L2可靠单Agent与MCP.md)
- Template: [`../../../templates/Agent技能卡模板.md`](../../../templates/Agent技能卡模板.md)
