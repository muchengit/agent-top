---
title: 路线状态
validated_date: 2026-09-16
---

# 路线状态

## 当前状态

| 模块 | 状态 | 证据 |
| --- | --- | --- |
| 仓库基础 | Done | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore` |
| 具体框架 | Done | `docs/en/agent-top-concrete-framework.md` |
| 概念 | Done | `docs/en/concepts/`, 包括架构、MCP、多 Agent 调度、长期记忆、模型幻觉、Plan 决策、核心概念深挖来源和核心 Agent 实施手册 |
| 框架地图 | Done | `docs/en/frameworks/framework-map.md` |
| 可执行 Lab | Done | `labs/l0` 到 `labs/l5`，包括补充 Lab |
| 任务优先入口 | Done | `docs/en/tutorials/quick-navigation.md`、`docs/zh/tutorials/快速导航卡.md`、`examples/agent-decision-trace/` |
| 详细教程 | Done | `docs/en/` 和 `docs/zh/` 覆盖 L0-L5 |
| 中文教程文件名 | Done | `docs/zh/` 下的中文镜像 |
| 面试资产 | Done | `docs/en/interviews/`, `docs/zh/interviews/`, 含 STAR 回答范例 |
| 作品集路径 | Done | `docs/en/portfolio/projects.md`、个人 Agent 作品集、开源影响力指南 |
| 生产指南 | Done | `docs/en/production/`、成本稳定性运行手册、生产速查表 |
| 案例研究 | Done | `docs/en/cases/` |
| 速查表 | Done | `docs/en/quick-reference/` |
| Agent 技能体系 | Done | `docs/en/skills/README.md`、`docs/zh/skills/Agent技能指南.md`、`templates/agent-skill-card-template.md` |
| 双语文档结构 | Done | `docs/en/` + `docs/zh/` |
| 社区治理 | Done | `GOVERNANCE.md`, `CONTRIBUTING.md`, `CONTRIBUTING.zh-CN.md`, `docs/en/community/` |
| GitHub 标签配置 | Done | `.github/labels.yml` |
| 安全策略 | Done | `SECURITY.md`, `SECURITY.zh-CN.md` |
| CI 检查 | Done | `.github/workflows/ci.yml` |
| 可复用模板 | Done | `templates/`，含 Agent 设计模板和 postmortem 模板 |

## 健康目标

| 指标 | 目标 |
| --- | --- |
| 死链率 | < 1% |
| 双语同步 | <= 14 天 |
| 框架示例保鲜 | 过期阈值前 review |
| 审查覆盖 | 每个活跃模块 >= 2 个备份 |
| Lab 测试覆盖 | 39 个确定性 Lab 测试本地通过 |

## 下一步优先级

继续增加真实案例，维持双语 SLA，并在 API 变化时通过 `sync-required` 保持框架示例新鲜。
