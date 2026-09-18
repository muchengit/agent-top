---
title: 部署卫生 Lab
capability_level: L4
validated_date: 2026-09-18
i18n-key: l4-deployment-hygiene
last-synced: 2026-09-18
tested_against: "python 3.10+"
---

# L4 Lab：部署卫生

## 目标

把可观测性完整性、成本预算与发布门禁检查合并为一次确定性部署决策，并给出 deploy、defer 或 block 的明确理由。

## 前置条件

- L4 生产系统概念。
- Python 3.10+.

## 运行

```bash
python -m unittest labs.l4.deployment_hygiene.test_lab
```

## 本 Lab 教授的内容

- 部署卫生是一次合并决策，而不是三个独立意见。
- 缺失关键 trace 字段与未配置告警会阻止部署。
- 只有缺少回滚预算时，超成本才会阻止部署。

## 常见陷阱

- 把部分 trace 覆盖当作硬性阻止而不是推迟。
- 把缺少回滚预算与超成本混淆。
- 在告警配置前批准部署。

## 自检

1. Which hygiene failure blocks immediately, and which only defers?
2. Why does a rollback budget change a cost decision?
3. How would you add latency p95 to this assessment?

## 双语说明

英文镜像位于 [`README.md`](README.md)，使用相同 `i18n-key`。修改本 Lab 时请保持两份镜像同步。
