# USDC-0173 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Proposed/under planning in Utah government inventory; no Iron County approval, permit, parcel, or utility record located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 “Proposed/under planning” 调整为 `approved-permitted`。Iron County Planning Commission 在 2026-06-04 批准 Antelope Data Center 的 Conditional Use Permit，motion 为 6 票赞成、0 票反对、1 票弃权；该结论来自 2026-07-06 发布的 approved minutes。来源：https://www.utah.gov/pmn/files/1457855.pdf
- 位置/地块补证：官方 agenda 与 minutes 均将项目描述为沿 Antelope Springs Road、约 8 miles west of Iron Springs Road、Cedar City, UT，APN E-0825-0000-0000（All of SEC 36, T34S, R14W, SLB&M），约 640 acres。来源：https://www.utah.gov/pmn/sitemap/notice/1085723.html 与 https://www.utah.gov/pmn/files/1457855.pdf
- capacity_mw 更新：以 Iron County/Utah Public Notice 材料中的 on-site “Data Center Power Plant” scalable natural-gas generation up to 1.5 GW at full buildout 计，更新为 1500 MW。该值表示项目拟建满负荷电源规模，不等于已并网负荷或 utility allocation。来源：https://www.utah.gov/pmn/sitemap/notice/1085723.html
- owner/developer 更新：官方 CUP 材料列 Applicant 为 Pronghorn Development, LLC；未在官方县材料中核实最终运营商/tenant，因此 owner 字段标注为 developer/applicant 并保留运营商未知 caveat。来源：https://www.utah.gov/pmn/sitemap/noticehistory/295689.html 与 https://www.utah.gov/pmn/files/1457855.pdf
- 建设状态 caveat：approved minutes 中县方说明 “The data center will not begin any building construction for at least 2 years”；本次未发现 building permit、state air approval、水权完成、utility interconnection/energization 证据。来源：https://www.utah.gov/pmn/files/1457855.pdf
- 冲突/时效问题：Iron County 的 Proposed Data Center Information 页面仍写 “Scheduled for Planning Commission review” 且指向 2026-06-04 meeting，页面状态落后于 Utah Public Notice approved minutes；data.json 已将此记录在 contradictions。来源：https://ironcountyut.gov/planning/data-center-projects 与 https://www.utah.gov/pmn/files/1457855.pdf
- 其他官方背景：Iron County 页面称 County Commission 于 2026-05-26 adopted 180-day moratorium for new land-use applications related to data centers/data-center power plants/solar power plants；该 moratorium 不改变 Antelope CUP 已在 2026-06-04 被 Planning Commission grant 的事实。来源：https://ironcountyut.gov/planning/data-center-projects
- 修正（2026-08-11 复核）：data.json actions[0].result_status 曾误引 cited source，称州级 inventory 将 Antelope 列为 1,000 MW；经核对 Grand County Planning Commission data-center staff report 的 Addendum A（Utah Data Center Inventory, status as of May 2026），实际列为 Antelope Data Center / Nr. Cedar City (Iron Co.) / Pronghorn Development LLP / **1,500 MW / PROPOSED**。已修正 result_status 为 1,500 MW 并在 data.json history 追加记录。来源：https://www.utah.gov/pmn/files/1444799.pdf
