# USDC-0052 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Microsoft's May 2026 official construction update states construction was continuing at the Boyd Farms site, with foundations, underground utilities, slabs, electrical vaults, sewer, stormwater, water
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 保持/明确为 `site work-construction`。Microsoft Local 的项目页（Construction update May 2026）称 Boyd Farms site 仍在施工，内容包括 foundations、underground utilities、slab work、electrical vaults、sewer/stormwater/water/fire-protection utilities、telecommunications 与 medium-voltage work；未发现 CO、energized IT load 或 service date。Source: https://local.microsoft.com/blog/boyd-farms-datacenter-construction-update/
- 新增地方政府 corroboration。Catawba County 于 2026-06-23 发布 joint statement，确认 2022 年宣布的 Microsoft Catawba County 项目为 10 年内四个数据中心、最低 10 亿美元 phased development，并称本地数据中心项目处于 existing 或 under construction；该声明覆盖 Catawba County 项目整体，不是 Boyd Farms 单站 CO/并网证明。Source: https://www.catawbacountync.gov/news/joint-statement-on-microsoft-data-center-development-in-catawba-county/
- 新增联邦许可线索。USACE Wilmington District public notice SAW-2023-00665 的索引结果记录 Microsoft 于 2023-05-15 申请 Department of the Army authorization，关联 Boyd Farm Data Center-CLT 10 near Maiden, Catawba County；直接 curl 访问 public notice 页被站点拒绝，本次未找到 final permit decision。Source: https://www.saw.usace.army.mil/Missions/Regulatory-Permit-Program/Public-Notices/Year/2023/?Page=5
- owner 由 null 更新为 `Microsoft Corporation`。Sources: https://local.microsoft.com/blog/boyd-farms-datacenter-construction-update/ ; https://www.catawbacountync.gov/news/joint-statement-on-microsoft-data-center-development-in-catawba-county/
- location 补充为 off Zeb Haynes Road，约 292 acres north of W. Maiden Road and west of Zeb Haynes Road。Sources: https://local.microsoft.com/blog/boyd-farms-datacenter-construction-update/ ; https://charlotteregion.com/news/microsoft-to-invest-1-billion-in-technology-facilities-in-catawba-county/
- capacity_mw 由 null 更新为 `240`，但标注为 planned/filed critical-load estimate。Aterio 2026-07-15 analysis 称 USACE filings for Boyd Farm/Lyle Creek/Stover North each show five 48 MW data-center buildings，即 Boyd Farms 约 240 MW critical IT load；未发现 Microsoft/County/Duke/CO/energization 记录确认 delivered capacity。Source: https://www.aterio.io/blog/microsoft-catawba-county-810mw-data-center-restart-north-carolina
- 冲突/不足：没有发现 Boyd Farms 的建筑 CO、final inspection、utility energization、IT load service date 或 Microsoft 官方 MW；240 MW 仅作为规划/filing-backed 估计保存。
