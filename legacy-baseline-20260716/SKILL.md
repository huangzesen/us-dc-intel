# legacy-baseline-20260716/ · 冻结基线 SKILL

> 职责：2026-07-16 冻结的数据中心基线（原始 bytes 只读，来自衡枢 codex 的 208 masters 清单）。

## 维护契约

- **只读**：不修改本目录任何文件；如需引用，复制到别处再改
- 参考文件：`national_master_inventory.json`（208 masters = 185 详细 + 23 seed-only；SHA `2113de4b…`）、`dedupe_ledger.json`、`county_decision_register.json`、`gantt_rows+methodology`、`source_conflict_audit.json`、`completeness_appendix.json`、`final/build_report.py` + HTML/PDF
- 新数据进入 `dc/` 与 `datacenters.db`，**不回写**本基线

## 边界

- 不删、不改、不重排 baseline 原始 bytes；基线记录历史事实，迁移/修订另行归档

## 相关文件

- `legacy-baseline-20260716/` 内：`national_master_inventory.json`（208 masters）、`dedupe_ledger.json`、`county_decision_register.json`、`gantt_methodology.md`、`source_conflict_audit.json`、`completeness_appendix.json`、`build_report.md`
- `dc/<slug>/`（新数据入口）· `datacenters.db`（主库）· 顶层 `SKILL.md`/`ANATOMY.md`
