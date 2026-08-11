# USDC-0014 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Company-reported under construction; no Aurora permit, council vote, power-on, or service record was located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 site work-construction：Edged 于 2025-11-14 发布 Aurora 第二设施 groundbreaking 新闻，称仪式发生在前一日；2026-06-05 Data Center Dynamics 报道第二栋已 topping out/结构完成。来源：https://edged.us/news/edged-us-expands-chicagoland-campus；https://www.datacenterdynamics.com/en/news/edged-tops-out-second-building-at-chicago-data-center-campus-illinois/
- capacity_mw 由 null 更新为 72；owner 由 null 更新为 Edged US；location 增补地址 2835 Bilter Road, Aurora, IL 60502。Edged Chicago 官方位置页列出 96MW campus、ORD01-1 24MW、ORD01-2 72MW，地址为 2835 Bilter Road。来源：https://edged.us/chicago
- 进度边界：DCD 报道 ORD01-2 已 fully pre-leased、计划 Q2 2027 live；这支持施工/结构完成，不支持 energized、partial live 或 full buildout。来源：https://www.datacenterdynamics.com/en/news/edged-tops-out-second-building-at-chicago-data-center-campus-illinois/
- 官方/local-gov 搜索：City of Aurora permits 页面说明 new construction requires permit，并指向 eTRAKiT；eTRAKiT public portal 可访问，但 permit/project search 在本次浏览中重定向至 login，未能核实该 second facility 的具体 permit、case、inspection、council vote 或 utility service record。来源：https://www.aurora.il.us/Property-Business/Permits；https://auro-trk.aspgov.com/etrakit/
- 冲突：未发现状态层级的实质冲突；容量存在 tracker 冲突，DataCenterMap 将 Edged Chicago ORD2 标为 48MW，与 Edged 官方 ORD01-2 72MW 不一致，未采纳 tracker 值。来源：https://www.datacentermap.com/usa/illinois/chicago/edged-ord2/
