---
title: L5 Lab：监督与事件响应
capability_level: L5
validated_date: 2026-09-18
i18n-key: l5-supervision-incident-response
last-synced: 2026-09-18
tested_against: "python 3.10+"
---

# L5 Lab：监督与事件响应

## 目标

为多 Agent 集群构建确定性的生产监督器：聚合 worker 心跳与事件报告，决定继续、升级、暂停还是回滚，并产出带负责人与回滚目标的行动计划。

## 前置条件

- L4：具备 trace 完整性与发布门禁的生产化 Agent 系统。
- Python 3.10+
- 熟悉多 Agent 调度与可观测性契约。

## 运行

```bash
python -m unittest labs.l5.supervision_incident_response.test_lab
```

## 本 Lab 教授的内容

- 监督是确定性状态机，而不是另一段 LLM 对话。
- 事件响应需要负责人、回滚目标和明确决策。
- 关键事件与宕机 worker 会改变发布姿态。

## 常见陷阱

- 在超过阈值前把 warning 当作信息级别处理。
- 单个 trace 家族受影响时回滚整个集群。
- 忘记已解决事件应从 open 集合中移除。

## 自检

1. When does a supervisor choose rollback instead of escalation?
2. Why should action items carry a rollback target?
3. How would you add a human-approval step before rollback?

## 双语说明

英文镜像位于 [`README.md`](README.md)，使用相同 `i18n-key`。修改本 Lab 时请保持两份镜像同步。
