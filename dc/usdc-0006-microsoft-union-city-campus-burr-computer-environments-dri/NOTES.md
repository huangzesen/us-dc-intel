# USDC-0006 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Georgia DCA record supports a Microsoft-related DRI approval/reporting trail for a proposed three-phase campus
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 proposed/local-process 证据更新为 `site work-construction`。Union City 2026-07-21 官方新闻页称 Stonewall Tell Road 沿线 Microsoft data center 已在施工中，且为超过 2 million square feet、$1.8 billion 项目；未发现 CO、energization、partial-live 或 full-buildout 记录。来源：https://www.unioncityga.gov/News-articles/No-longer-Mayberry-Union-Citys-population-is-booming-Local-leaders-like-Vince-Williams-are-working-to-shape-future-growth
- 位置/项目身份补强：Development Authority of Fulton County 2024-06-25 minutes 将 Project Steamboat 描述为位于 4810 Stonewall Tell Road, Union City 的三栋 hyperscale data-center campus，最高 $1.842 billion taxable revenue bonds，开发期预计 Q3 2024 至 2029/2030，三期需在 2032 前完成。来源：https://www.developfultoncounty.com/uploads/meetings-and-minutes_338_1970884577.pdf
- 县级基础设施动作补强：Fulton County BOC item 25-0016 于 2025-01-08 批准 EdgeconneX ATL11, LLC 向 Fulton County dedication 47,729 sq ft sewer easement，用于 Stonewall Tell Road # R, Union City 的 EDCATL11 Project；staff text 称新 sewer service line connections 在 Land Disturbance Permit 前需确认 county ownership interests。来源：https://fulton.legistar.com/LegislationDetail.aspx?GUID=F2C32E8C-CBD7-4538-A3A3-44C2EC2F3125&ID=7082619&Options=&Search=  附件：https://fulton.legistar.com/View.ashx?GUID=385F83EF-A160-43C8-B52B-144975ED64C9&ID=13651351&M=F
- 城市会议纪要补强：Union City 2025-12-16 council minutes 在另一个 TA Realty data-center rezoning hearing 中记录 staff 表述 Stonewall Tell 上 currently 1 data center。该表述作为状态上下文，不视为 project-specific permit/CO。来源：https://www.unioncityga.gov/files/assets/city/v/1/clerkmgrcouncilmayor/documents/agendas-amp-min/12-16-25-regular-council-meeting-minutes.pdf
- capacity_mw 更新为 324 MW，但标为 reported / not official-permit-confirmed：AJC 2024-07-17 报道称 development team news release 给出 campus capacity 324 MW；本轮未在官方 county/city records 中找到 MW capacity。来源：https://www.ajc.com/news/business/new-details-revealed-about-microsofts-18b-data-center-near-atlanta/X7FTPDSJGNAZVNF34XSHTPXS2Y/
- owner/end-user 更新：Fulton sewer easement exhibit 将 EdgeconneX ATL11 LLC 标为 owner/grantor；Union City 官方新闻和区域媒体将项目称为 Microsoft data center/end-user。将 owner 字段写为 EdgeconneX ATL11 LLC + Microsoft end-user caveat。
- 冲突/注意：Fulton Legistar item 25-0016 的 summary/background 将 EDCATL11 误称为 residential development，但 item title、easement attachment、DAFC minutes、Union City 2026 page 均指向 Stonewall Tell data-center project；本轮按 boilerplate/carryover error 处理并写入 contradictions。
- 未核实项：未发现公开 building permit、certificate of occupancy、utility interconnection approval、energization、partial-live 或 full-buildout 记录；324 MW 仍不是官方许可记录值。
