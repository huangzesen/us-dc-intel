# US DC intel · 项目探索跟踪

## 目标
维护美国数据中心项目最宽口径超集：每个 county、每个开发商、互联网上所有蛛丝马迹形成的清单（Jason 3214/3224）。

## 数据源调研（已完成，2026-08-11 18:49Z）
- `scripts/expansion/source-research-trackers.jsonl` + `-summary.md`：Cleanview 1788 planned/369.9GW、Baxtel 5115 设施、FracTracker、dcmap.us 4800 设施、Data Center Knowledge 等
- `scripts/expansion/source-research-rtos.jsonl` + `-summary.md`：ERCOT/MISO/SPP/NYISO/CAISO/ISO-NE 队列全可抓，PJM 需 API key
- `scripts/expansion/source-research-news.jsonl` + `-summary.md`：州 EDO 公告页、DCK 月度、FAST-41

## 州级探索（已完成，10 州 / 419 项目）
`scripts/expansion/state-projects/<ABBR>-projects.jsonl`
AZ 34 / GA 47 / IL 47 / IN 55 / NC 40 / OH 33 / TX 35 / UT 39 / VA 41 / WA 48

## County 级探索（进行中）
- 全美 county 清单：`scripts/expansion/us-counties-all.tsv`（3,222 county，52 州，Census gazetteer）
- 批次文件：`scripts/expansion/county-batches/batch-000..322.tsv`（每 10 county）
- 结果：`scripts/expansion/county-results/<batch>-results.jsonl`
- 已派发：batch 000-029（30 daemon / 300 county）

## 下一步
1. county 探索铺满 322 批 → 合并去重（canonical ID + evidence_grade）
2. RTO/ISO 队列抓取（ERCOT 1906 / MISO 3806 / SPP 1029 / NYISO / CAISO / ISO-NE）
3. Baxtel/FracTracker/dcmap.us 全量
4. 全部入 repo dc/<slug>/ 目录
5. 重新聚合画图（planned 层反映真实存量）
