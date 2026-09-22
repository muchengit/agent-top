# Agent-Top 电子书打包调研

## 结论先行

推荐采用 **Markdown 单源 + EPUB 3** 的方案。当前项目缺少 Pandoc/Calibre 运行时依赖，因此已优先实现一个 **无第三方依赖的 Python 标准库构建器**，可直接生成 EPUB 3 与静态 HTML。

1. **EPUB 3**：面向电子阅读器、手机、平板，适合作为官方电子书主格式。
2. **HTML**：面向快速审阅、GitHub Pages 预览和内部培训分发。
3. **PDF**：已实现构建入口；默认在无额外引擎时生成有效的 fallback PDF，并额外输出 `.print.html` 供浏览器打印成完整 PDF。

不建议首发时依赖 Calibre/Kindle 专有格式。Kindle 可通过后续 `epub -> mobi/azw3` 转换支持，但应把 EPUB 作为版权格式和再生源。

## 已执行落地

已新增：

- `ebook/build_ebook.py`：无第三方依赖的双语电子书构建器。
- `ebook/README.md`：电子书构建说明。
- `ebook/en/how-to-use.md`、`ebook/en/appendix.md`：英文电子书使用指南与附录。
- `ebook/zh/how-to-use.md`、`ebook/zh/appendix.md`：中文电子书使用指南与附录。
- `docs-site/search.html`：新增电子书相关搜索入口。
- `.github/workflows/ci.yml`：CI 中增加电子书构建步骤。

构建命令：

```bash
python3 ebook/build_ebook.py
```

## 项目现状盘点

当前仓库适合作为电子书内容源：

- `docs/en/`：95 个 Markdown 文件，约 14,275 行，约 95,636 词级片段。
- `docs/zh/`：95 个 Markdown 文件，约 14,162 行，约 44,832 词级片段。
- `labs/`：60 个 Markdown 文件，可执行 Lab 教程。
- `examples/`：17 个 Markdown 文件，无 API Key 示例材料。
- `templates/`：47 个 Markdown 文件，贡献、评审、复盘等模板。
- 文档索引入口明确：`docs/en/README.md` 与 `docs/zh/README.md`。
- 中英双语文档结构基本对称，适合分成单语电子书或双语合订本。

当前本地环境未检测到 `pandoc` / `calibre` / `ebook-convert`，因此需要新增构建依赖或提供 Docker/CI 构建方式。

## 推荐电子书形态

### 方案 A：Agent-Top Practical Guide / 实践指南

**目标读者**：LLM Agent 入门到中级工程师。

**内容范围**：

- `README.md` / `README.zh-CN.md`
- `docs/en/l0-first-llm-call.md` 到 `docs/en/l5-custom-patterns.md`
- `docs/en/concepts/*`
- `docs/en/frameworks/framework-map.md`
- `docs/en/production/*`
- `docs/en/tutorials/practice-handbook.md`
- `labs/README.md` 与 L0-L5 README

**优点**：内容完整，学习路径清楚，适合正式对外发布。

**风险**：全量 docs 较多，首次读者可能觉得太长。

### 方案 B：Agent-Top Quick Start Ebook / 快速启动电子书

**目标读者**：想 1-2 天完成首个 Agent 项目的人。

**内容范围**：

- README 摘要
- L0-L2 教程
- ReAct、MCP、RAG 核心概念
- 3-5 个代表性 Lab
- 面试基础题与生产检查表

**优点**：阅读负担低，转化率和传播性更好。

**风险**：需要人工筛选和重写章节顺序，无法直接由目录自动生成。

### 方案 C：Bilingual Companion / 中英对照版

**目标读者**：团队培训、教学、开源贡献者。

**内容范围**：

- 英文主章节
- 中文对照章节
- 术语表
- 贡献流程与模板

**优点**：利用现有 `docs/en` 与 `docs/zh` 双语资产，体现开源治理质量。

**风险**：双语文档同步压力较大；当前仓库已有 `last-synced` 与 `validated_date` 机制，可复用。

## 推荐技术栈

### 首选：Pandoc

原因：

- 直接读取 Markdown。
- 支持 EPUB、PDF、HTML、DOCX 多格式输出。
- 可通过 `metadata.yaml` 和 `reference` 文件统一样式。
- CI 中易集成。
- 开源，命令式构建简单。

基础命令形态：

```bash
pandoc --resource-path=. \
  --epub-cover-image=assets/cover.jpg \
  --metadata-file=metadata-en.yaml \
  --toc --toc-depth=3 \
  --number-sections \
  --standalone \
  ebook-source-en.md \
  -o dist/agent-top-practical-guide-en.epub
```

PDF 需要 LaTeX 或 typst 引擎；如果环境不稳定，可采用 HTML + weasyprint/prince 的方案。

### 备选：Quarto

适合后续把 Lab 代码、测试输出、图片、表格做成更结构化的技术书。若项目已有 Jupyter/Python Lab，Quarto 更自然，但当前仓库主要是 Markdown + Python/多语言示例，不是首选。

### 备选：VitePress/MkDocs + 静态站点导出

当前已有 `docs-site/` 静态站点雏形。适合网页阅读，但不是电子书主路径。可把站点作为在线版，电子书作为离线版。

## 电子书信息架构建议

建议不要直接按仓库目录原样导出。推荐按学习路径重排：

1. **How to Use This Book**
2. **Agent-Top Capability Model L0-L5**
3. **L0: First LLM Call**
4. **L1: ReAct Agent Components**
5. **L2: Reliable Single Agent and MCP**
6. **L3: RAG, Memory, Observability**
7. **L4: Production, Evals, Safety, Cost**
8. **L5: Original Patterns and Open-source Contribution**
9. **Frameworks Map**
10. **Production Playbooks**
11. **Interviews and Portfolio**
12. **Labs and Examples**
13. **Templates and Governance**
14. **Glossary**
15. **Version Anchors and Maintenance Notes**

## 必要构建产物

建议新增：

- `ebook/en/source.md`：英文电子书入口。
- `ebook/zh/source.md`：中文电子书入口。
- `ebook/metadata-en.yaml`：英文元数据。
- `ebook/metadata-zh.yaml`：中文元数据。
- `ebook/styles/pandoc.css`：PDF/HTML 样式。
- `ebook/styles/reference.epub`：EPUB 样式模板。
- `assets/cover-en.jpg`：英文封面。
- `assets/cover-zh.jpg`：中文封面。
- `scripts/build_ebook.py`：构建脚本。
- `dist/ebooks/*.epub`：输出目录，加入 `.gitignore`。

## 元数据建议

英文：

```yaml
title: "Agent-Top: Practical Guide to Building LLM Agents"
author:
  - "Agent-Top Contributors"
date: "2026-09-18"
language: "en"
rights: "MIT License"
description: "A practice-first guide from first LLM calls to production-grade multi-agent systems."
cover-image: "assets/cover-en.jpg"
keywords:
  - "LLM agents"
  - "ReAct"
  - "MCP"
  - "RAG"
  - "evaluations"
```

中文：

```yaml
title: "Agent-Top：LLM Agent 开发实践指南"
author:
  - "Agent-Top Contributors"
date: "2026-09-18"
language: "zh"
rights: "MIT License"
description: "从第一次 LLM 调用到生产级多 Agent 系统的实践指南。"
cover-image: "assets/cover-zh.jpg"
keywords:
  - "LLM Agent"
  - "ReAct"
  - "MCP"
  - "RAG"
  - "评测"
```

## 版权与合规建议

- 仓库许可证为 MIT，电子书应明确保留许可证和版权说明。
- 在 PDF 首页、EPUB metadata、版权页均写入 MIT License。
- 若引用外部框架、论文、开源项目，保留链接和来源说明。
- 电子书中避免包含任何 API Key、私有 token、真实客户数据。
- Lab 代码应继续标注 `tested_against` / `validated_date`，这是 Agent-Top 的重要治理特征。

## 质量门禁

建议 CI 或本地脚本检查：

1. 源 Markdown 存在且非空。
2. 电子书目录链接全部有效。
3. `docs/en` 与 `docs/zh` 对应章节是否同步。
4. frontmatter 必填字段存在。
5. EPUB 可被 Pandoc 生成。
6. PDF 可被生成，或记录依赖缺失为 skip。
7. 输出文件大小、页数、章节数写入构建报告。

可复用现有检查：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## 实施路线

### Phase 1：最小可用电子书

- 选择英文或中文单语版。
- 编写 `source.md`，按学习路径 include 或合并核心文档。
- 生成 EPUB。
- 加入封面和版权页。

预计工作量：1-2 天。

### Phase 2：双语正式版

- 建立英文、中文两套 source。
- 添加术语表和版本说明。
- 添加 CI 构建脚本。
- 生成 EPUB + PDF。

预计工作量：3-5 天。

### Phase 3：增强版

- 添加截图、架构图、代码运行输出。
- 为面试和作品集部分增加练习答案。
- 增加 Kindle 转换或 Apple Books 兼容检查。
- 增加版本化发布：`v0.1.0`、`v0.2.0`。

预计工作量：1-2 周。

## 推荐决策

第一阶段建议选择 **方案 A + Pandoc + EPUB/PDF**，先做英文正式版，再基于现有 `docs/zh` 做中文同步版。

原因：

- 当前项目文档数量已经足够支撑一本实践指南。
- L0-L5 结构天然适合技术电子书。
- 仓库已有双语、Lab、Examples、Templates、治理机制，电子书能把这些资产变成可分发产品。
- Pandoc 是 Markdown 项目最低摩擦的电子书构建工具。
