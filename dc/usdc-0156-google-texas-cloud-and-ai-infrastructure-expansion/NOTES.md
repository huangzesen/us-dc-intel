# USDC-0156 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: State/company announcement for multiple campuses; county-level project split and approvals are not established
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从单一州/公司公告，提升为“Google/州公告 + Haskell County tax-abatement + TDLR project-registered construction filings”。仍未标记 energized / partial live / full buildout；TDLR 记录是 architectural-barriers project registration，不是投运证明。
- Google 官方来源确认：2025-11-14 Google 宣布 through 2027 在 Texas 投资 $40B，用于 cloud and AI infrastructure，包括 Armstrong 与 Haskell Counties 的新 data center campuses；Google Texas location page 当前还列出 Ellis County 既有 Midlothian/Red Oak，并把 Armstrong、Haskell、Pampa、Wilbarger列为新 campus counties。来源：https://blog.google/company-news/inside-google/company-announcements/google-american-innovation-texas/；https://datacenters.google/locations/texas/
- Haskell County 本地政府来源确认：county tax-abatement 页面列出 Homebound Data Center - Thelma (Google)、Homebound Group, LLC - Journey (Google)、Homebound Group, LLC - Quest (Google)，日期均为 2025-06-24；另列 Ascendant Site Solutions, LLC - Ranger (Google)，日期为 2026-04-27。来源：https://www.haskellcountytx.gov/page/haskell.Abatement
- Haskell TDLR 新增/补证：
  - THM1A / Data Center 1，TABS2025019833，10357 Loop Road, Haskell County，280,000 sq ft，$350M，start 2025-06-18，completion 2027-04-16，owner Homebound Group LLC，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2025019833
  - Journey 1A，TABS2026023821，1362 Red Creek Rd, Haskell County，285,282 sq ft，$400M，start 2026-04-01，completion 2027-08-21，owner Homebound Group LLC，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026023821
  - Journey 2A，TABS2026023839，1362 Red Creek Rd, Haskell County，210,420 sq ft，$400M，start 2026-06-23，completion 2027-10-27，owner Homebound Group LLC，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026023839
- Armstrong / Goodnight-Llano 补证：Google 官方只到 county-level campus；TDLR filings at 10001 Lima Rd, Claude, Armstrong County list GN DC1 LLC as owner and do not name Google as tenant. 已作为 B-grade linkage/caveat 记录，而非直接 Google-owned permit。
  - Llano Building 1，TABS2025026455，484,954 sq ft，$292M，start 2025-08-25，completion 2026-08-24，status Review Complete。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2025026455
  - Llano Building 2，TABS2025026470，484,954 sq ft，$292M，start 2025-08-25，completion 2026-08-24，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2025026470
  - Llano Building 3，TABS2026026002，805,308 sq ft，$500M，start 2026-05-25，completion 2026-08-01，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026026002
  - Llano Building 4，TABS2026026118，805,308 sq ft，$500M，start 2026-06-15，completion 2027-03-15，status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026026118
- capacity_mw 仍保留 null：Google 披露的 6,200 MW 是 Texas energy generation/capacity contracted to date，不是数据中心 IT/load capacity；Goodnight/Armstrong 的 >1GW 等数字来自 Aterio/DCD 等第三方，未写入 authoritative capacity_mw。行业参考来源：https://www.datacenterdynamics.com/en/news/google-linked-housebound-group-files-for-two-data-center-projects-in-haskell-texas/；https://www.datacenterdynamics.com/en/news/crusoe-files-for-two-more-data-centers-at-goodnight-campus-in-armstrong-county-texas/
- 冲突/不足：Haskell County 明确把 Homebound Thelma/Journey/Quest 标为 Google；Armstrong TDLR 仅列 GN DC1 LLC 且 tenant Not Assigned，因此 Armstrong site-level Google attribution remains inferred from Google's county announcement plus industry reporting. 未找到官方投运、CO、utility interconnection load MW 或 county-level permit approval proving energized/live status.
- 历史同步（fix pass）：data.json `history` 补充 2026-08-11 条目，分别记录 status_as_of_cutoff 与 owner 自 baseline（2026-07-16）以来的变更（old_value/new_value/reason），使 history 末条与当前 status_as_of_cutoff 一致（修复评审 issue：status/history 不匹配）。
