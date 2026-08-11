# scripts/ · 数据管线 SKILL

> 职责：探索、合并、导出。所有脚本幂等、可复用；批量探索走 daemon，父 agent 统一 review 提交。

## 维护契约

1. **合并全源**（探索结果 → 统一中心）：`python3 scripts/merge_all_sources.py` —— 幂等；读 `scripts/expansion/**`（county-results + state-projects + discovery + americas），去重 → `merge-output/centers.jsonl` + `datacenters.db`
2. **导出 Astro 数据**：`python3 scripts/export_astro_data.py` —— 从 DB 生成 `astro/src/data/datacenters.json`（国家/州聚合、漏斗、年份、旗舰项目）
3. **生成 dc/ 骨架**：`python3 scripts/generate_skeleton.py` —— 从冻结 baseline 生成/刷新 `dc/<slug>/`（幂等，不覆盖 NOTES.md）
4. **探索批次**：`scripts/expansion/` 下按国家/地区放批次输入与结果；新国家先建二级行政区清单（`americas/americas-manifest.jsonl`）

## 派活模板（给探索 daemon 的任务书必备）

- 只读目标清单/路径（绝对路径）
- **NO-DELETION** 契约（绝不 rm/覆盖已有文件）
- 产出 = JSONL/文件 + 来源 URL + evidence_date + confidence
- 禁 git 写入；父 agent review 后统一提交

## 字段规范（每中心）

`country`、`subnational`（州/省/区）、`name`、`status`（announced/planned/approved/construction/operational/rejected/unknown）、`capacity_mw`、`developer`、`source_urls[]`、`evidence_date`、`evidence_grade`。

## 边界

- 不删除历史结果/输入；不清空 `merge-output/`；数据库重建前先备份

## 相关文件

- `SKILL.md`（顶层方法论/路由）· `ANATOMY.md`（结构地图）
- `scripts/merge_all_sources.py`（US 合并）· `scripts/merge_americas.py`（美洲合并）· `scripts/export_astro_data.py`（导出）· `scripts/generate_skeleton.py`（dc/ 骨架）
- `scripts/expansion/americas/explore-brief.md`（探索契约）· `scripts/expansion/americas/americas-manifest.jsonl`（清单）
- `datacenters.db`（SQLite 主库）· `merge-output/`（合并产物）· `astro/src/data/datacenters.json`（导出目标）
