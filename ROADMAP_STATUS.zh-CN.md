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
| 概念 | Done | `docs/en/concepts/`, 包括架构和多轮研究流程 |
| 框架地图 | Done | `docs/en/frameworks/framework-map.md` |
| 可执行 Lab | Done | `labs/l0` 到 `labs/l5`，包括补充 Lab |
| 详细教程 | Done | `docs/en/` 和 `docs/zh/` 覆盖 L0-L5 |
| 中文教程文件名 | Done | `docs/zh/` 下的中文镜像 |
| 面试资产 | Done | `docs/en/interviews/`, `docs/zh/interviews/` |
| 作品集路径 | Done | `docs/en/portfolio/projects.md` |
| 生产指南 | Done | `docs/en/production/`, `docs/en/quick-reference/production-checklist.md` |
| 案例研究 | Done | `docs/en/cases/` |
| 速查表 | Done | `docs/en/quick-reference/` |
| 双语文档结构 | Done | `docs/en/` + `docs/zh/` |
| 社区治理 | Done | `GOVERNANCE.md`, `CONTRIBUTING.md`, `CONTRIBUTING.zh-CN.md`, `docs/en/community/` |
| GitHub 标签配置 | Done | `.github/labels.yml` |
| 安全策略 | Done | `SECURITY.md`, `SECURITY.zh-CN.md` |
| CI 检查 | Done | `.github/workflows/ci.yml` |

## 健康目标

| 指标 | 目标 |
| --- | --- |
| 死链率 | < 1% |
| 双语同步 | <= 14 天 |
| 框架示例保鲜 | 过期阈值前 review |
| 审查覆盖 | 每个活跃模块 >= 2 个备份 |
| Lab 测试覆盖 | 35 个确定性 Lab 测试本地通过 |

## 下一步优先级

继续增加真实案例，维持双语 SLA，并在 API 变化时通过 `sync-required` 保持框架示例新鲜。
