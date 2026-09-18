---
i18n-key: community-agent-community-lab
last-synced: 2026-09-18
validated_date: 2026-09-18
---

Agent Community Lab

Agent Community Lab 是轻量共学形式，把一个教程、Lab 或架构主题变成有产出的小组 session。

## 格式

一个 session 应回答一个问题：

> 参与者能在 session 结束时构建、解释或改进什么？

建议时长：

- 60 到 90 分钟。
- 一个 host。
- 一个主题。
- 一个 runnable Lab 或简短 docs review。

## 建议节奏

- 双周教程发布 session。
- 月度面试练习 session。
- 双周论文或文章讨论 session。
- 季度路线图或生产回顾 session。

这些 session 补充主内容树，但不应替代它。

## Session 角色

| 角色 | 职责 |
| --- | --- |
| Host | 主持议程、控制时间、记录决策。 |
| Contributor | 提出一个小改动、翻译、Lab 或回答。 |
| Reviewer | 检查准确性与可维护性。 |
| Observer | 观察阻塞点与后续 issue。 |

## Session 类型

### Tutorial Walkthrough

主题是新教程或 Lab 时使用。

产出：

- 参与者能运行 Lab。
- Host 指出一个常见困惑点。
- 团队决定文档是否需要 follow-up patch。

### Interview Practice

主题是面试准备时使用。

产出：

- 讨论一道题，附 STAR 与 trade-off 记录。
- 新增或改进了 1 个 follow-up 问题。
- session 指回相关能力层级。

### Paper or Article Digest

主题是外部文章、论文或教程时使用。

产出：

- 提炼稳定概念。
- 把稳定概念与框架特定细节分开。
- 只有在帮助仓库时才加对比说明。

### Production Retrospective

主题是 postmortem、evals、observability 或 rollback 时使用。

产出：

- 把失败模式讲清楚。
- 识别一个预防控制。
- 提出 checklist 或模板更新。

## 贡献规则

- 纯文档改动用 `docs-only`。
- 可运行 Lab 改动用 `lab`。
- 双语缺口用 `translation-needed` 或 `sync-required`。
- 除非贡献很小，否则避免同一人同时当作者和 reviewer。

## Session Notes Output

结束时发布简短记录，包含：

- 主题。
- 一页总结。
- 可运行命令或相关 Lab。
- 后续 issue 或 PR。
- 文档是否需要更新。

使用模板：

- [`../../templates/community-lab-template.md`](../../../templates/community-lab-template.md)

## Health Checks

好的 Agent Community Lab session 应：

- 保持范围小。
- 产出一个具体 artifact。
- 保持 pattern-first。
- 除非模式稳定，否则避免框架 churn。
- 给下一位贡献者留下清晰任务。
