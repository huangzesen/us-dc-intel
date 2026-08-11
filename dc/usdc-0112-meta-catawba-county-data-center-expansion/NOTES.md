# USDC-0112 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 结论：未找到官方/地方政府来源可证实“Meta Catawba County data-center expansion”。本记录仍按 seed-only 保留，但 status 更新为 `not verified - likely seed conflation`，owner/capacity 继续留空。
- 官方反证：Catawba County 2022-11-09 公告称 Microsoft 计划在 Catawba County 分阶段投资至少 $1B，10 年内建设 4 个 datacenter，地点为 Conover、Hickory、Maiden，并创造至少 50 个就业岗位。来源：https://www.catawbacountync.gov/news/microsoft-to-invest-1b-in-technology-facilities-in-catawba-county/
- 官方近况：Catawba County 2026-06-23 联合声明再次确认该本地 data-center development 是 Microsoft 项目，并称 Catawba County 现有及在建 data-center sites 均由 City of Hickory 供水。来源：https://www.catawbacountync.gov/news/joint-statement-on-microsoft-data-center-development-in-catawba-county/
- 官方财报佐证：Catawba County FY2025 ACFR（2026-01-30 修订版）称 Microsoft 2022 年 11 月宣布 4 个 data centers，首个 data center 于 2024 年 4 月开工，Microsoft 继续探索追加投资。来源：https://catawbacountync.gov/site/assets/files/2544/acfr_2025_final_revised_01_30_2026.pdf
- Meta 官方来源：Meta 官方 U.S. data-center fleet 页面在 North Carolina 下只列 Forest City（$750M+ investment, 2010 break ground），未列 Catawba County/Claremont。来源：https://datacenters.atmeta.com/us-locations/
- Meta 在 Catawba County 的相关事实不是 data center：Catawba County EDC 2026-03-31 转发 Corning/Meta 公告，内容为 Corning 在 Hickory 扩建 optical cable manufacturing capacity，Meta 是 anchor customer，用于支持 AI data centers。来源：https://www.catawbaedc.org/post/corning-and-meta-celebrate-start-of-construction-on-cable-manufacturing-expansion-in-north-carolina
- 多源冲突：seed 将项目标为 Meta/Catawba data-center expansion；官方与地方政府来源显示 Catawba County data-center program 为 Microsoft，Meta 官方 NC data-center location 为 Forest City。未发现可覆盖该冲突的官方 Meta/Catawba data-center 证据。
- 无法核实项：未核实到 Meta-owned Catawba County/Claremont data-center 的容量、地块、许可、建设状态或 owner 证据；第三方页面中出现的 “Meta Catawba County AI Complex / Microsoft / 488 MW” 表述与官方来源冲突，未采纳为事实。
