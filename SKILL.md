# GRIDWATCH · 全球数据中心建设情报库 — 顶层方法论 SKILL

> 灵台方法论：应需而化、善假于物、学而不殆、群而不孤、去芜存菁。
> 本库是**可自维护**的情报项目：任何 agent 读此文件后即可接手，任何更新都走 git、可追溯。

## 一 · 项目是什么

维护全球（当前**美洲**起步）在建/规划数据中心的可更新情报库：

- 每个**国家/地区**按**二级行政区**探索（US=county、CA=省/地区、MX=州、BR=州、AR=省……）
- 每个中心一条结构化记录（`data.json`）+ 看护契约（`SKILL.md`）+ 历次更新（`NOTES.md`）
- 汇总进 `datacenters.db`（SQLite）+ `merge-output/centers.jsonl`，驱动看板与正式站
- 正式站：`astro/`（Astro 静态站，GRIDWATCH 设计），部署于 https://xhelio.ai/datacenters/

## 二 · 结构地图（去哪个文件夹查什么）

| 想做什么 | 入口 |
|---|---|
| 顶层导航/代码地图 | `ANATOMY.md` |
| 查某中心最新状态 | `dc/<slug>/SKILL.md` → `data.json` → `NOTES.md` |
| 数据管线/脚本 | `scripts/SKILL.md` → `scripts/` |
| 探索批次与原始结果 | `scripts/expansion/`（county-batches / county-results / state-projects / americas） |
| 合并/数据库 | `scripts/merge_all_sources.py` → `datacenters.db` + `merge-output/` |
| 静态看板渲染 | `kanban/SKILL.md` → `kanban/render_kanban.py` |
| 正式站（Astro） | `astro/SKILL.md` → `astro/` |
| 设计文档 | `design/SKILL.md` → `design/` |
| 冻结基线（7/16） | `legacy-baseline-20260716/SKILL.md` → `legacy-baseline-20260716/` |

## 三 · 怎么更新（给任何接手的 agent）

1. `git pull`（或 clone 本 repo）
2. 读 `ANATOMY.md` 定位模块；读目标文件夹 `SKILL.md` 的「维护契约」
3. 探索/刷新：派 daemon，任务书必须含 **NO-DELETION** 契约 + 目标路径 + 来源 URL + 禁 git 写入
4. 合并：`python3 scripts/merge_all_sources.py`（幂等）→ 更新 `datacenters.db`
5. 构建：`kanban/render_kanban.py` 或 `astro/` 内 `npm run build`
6. 提交：`git add` + commit（message 含 country/division/变化摘要）；部署需另行授权

## 四 · 国家/地区探索规范

- 每个国家/地区先建**二级行政区清单**（`scripts/expansion/americas/americas-manifest.jsonl`）
- 按行政区逐个探索（宁多勿漏），产出 JSONL → 合并去重 → 入库
- 字段规范（每中心）：`country`、`subnational`（州/省/区）、`name`、`status`、`capacity_mw`、`developer`、`source_urls`、`evidence_date`、`evidence_grade`
- **evidence vs projected 分开；announced 不当 construction；缺证据标 grade，不臆造**

## 五 · 边界（不可妥协）

- 不删除任何已有文件/目录（含 baseline 原始 bytes）；清理需 Jason 明确授权
- 不把 announced 当 construction；不改算枢 workspace；对外发布需 Jason 另行授权
- 公开发布物（HTML/评论）不得含内部路径（/Users/、scratch/、daemons/、logs/ 等）
- 每个文件夹都有自己的 `SKILL.md` 与职责，跨模块改动先读 `ANATOMY.md` 找 owner
