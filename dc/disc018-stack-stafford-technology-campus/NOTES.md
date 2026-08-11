# disc018 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-hyperscaler.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 状态从笼统的 `under construction` 规范化为 `site work-construction`：DCD 于 2026-05-26 报道 STACK 已完成 Stafford Technology Campus 首栋楼外部结构 / topping out，且项目团队已记录 425,000+ 工时、移动 300 万立方码土方、完成 4,000 英尺挡墙。来源：https://www.datacenterdynamics.com/en/news/stack-tops-out-first-building-at-1gw-data-center-campus-in-stafford-county-virginia/
- 容量从 `1000` MW 更新为 `1100` MW：STACK 当前 STC campus 页面列示 1.1GW、500 acres、four sub-campuses、six 300MW substations。证据日期：2026-08-11 抓取。来源：https://www.stackinfra.com/locations/americas/northern-virginia/stc/
- 补充地方政府规划/审批证据：Stafford County 的 Stafford Technology Campus zoning reclassification 页面列明 RC23154931，位置在 Richmond Highway / Sage Lane / State Shop Road / Eskimo Hill Road 一带，523.94 acres，拟开发约 5.5 million square feet 的 data and computer services center uses。证据日期：2026-08-11 抓取。来源：https://staffordcountyva.gov/government/departments_p-z/planning_and_zoning/stafford_technology_campus_zoning_reclassification.php
- 补充地方政府当前 approved-site/ grandfathering 证据：Stafford County data centers 页面称 2025-12-02 通过 O25-29(R)，对 2025-10-21 及以前获 Board reclassification/CUP/site-plan approval 的项目 grandfathering，名单包括 Stafford Technology Campus；同页 approved sites 表列 STC 为 5,800,000 sq. ft. / 20 buildings。来源：https://staffordcountyva.gov/government/departments_p-z/planning_and_zoning/data_centers/index.php
- 补充 Stafford IWR 当前申请证据：application 25156486（process date 2025-05-28）为 `DATA CTR - STAFFORD TECH CAMPUS` 的 rezoning classification and proffer amendment，portal 显示 Permit Status: Final；项目经理 review 同时记录该 application falls within O25-29R grandfathering language，且 applicant response 称原 rezoning 的 square footage remains unchanged at 5.808 million square feet。来源：https://hello.stafford.va.us/plan?apnum=25156486
- 补充联邦湿地/水域许可证据：USACE Norfolk District public notice NAO-2022-02671 于 2026-02-16 发布，applicant 为 SI NVA07CAMPUS, LLC，项目区约 537 acres，Phase I previously authorized under 22-SPGP；overall project described as approximately 4.5 million square feet, 21 data center buildings, and six substations, with listed wetland/stream impacts。来源：https://www.nao.usace.army.mil/Media/Public-Notices/Article/4401717/nao-2022-02671-stafford-technology-center-stafford-virginia/
- 冲突/需保留：容量与楼栋/面积口径不完全一致。County approved-sites table 为 5.8M sq. ft. / 20 buildings；STACK press/DCD 为 1+GW / 19 data centers；STACK current campus page 为 1.1GW；USACE permit notice 为约 4.5M sq. ft. / 21 buildings。当前 data.json 采用业主当前容量页的 1.1GW，并在 contradictions 中保留多源差异。
- 仍无法核实：未找到可公开核验的 Dominion interconnection queue 条目或正式 energized/partial-live 证据；因此不升级到 energized、partial live 或 full buildout。
