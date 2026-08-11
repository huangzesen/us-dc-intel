# USDC-0136 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Development/construction reported and covered by a utility service agreement; first service is unknown
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 “Development/construction reported and covered by a utility service agreement; first service is unknown” 调整为 `site work-construction as of 2026-08-11`。依据：City of Stillwater 项目页 2025-08-15 称 site prep continues 且 construction permits nearing completion；Google 2026-04-30 称 Stillwater 与 Muskogee data center campuses under construction；OG&E 2026-04-30 称将为 Muskogee/Stillwater 三个 Google data centers 供电，但 OCC 仍需正式批准协议。来源：
  - https://stillwaterok.gov/536/Projects
  - https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/oklahoma-energy-affordability-agreement/
  - https://www.oge.com/web/portal/-/200-press-release
- owner/location 补证：owner 从 null 更新为 `Google`。City of Stillwater 2025-03-12 公告确认 Google acquired land at the intersection of Perkins and Richmond Roads for future development of a data center campus；同一政府流程资料显示 project area 为 386.698 acres。来源：
  - https://stillwaterok.gov/m/newsflash/Home/Detail/332
  - https://stillwaterok.gov/DocumentCenter/View/3278/NOTICE-TO-THE-PUBLIC-OF-TWO-PUBLIC-HEARINGS-REGARDING-THE-STILLWATER-DATA-CENTER-ECONOMIC-DEVELOPMENT-PROJECT-PLAN
- 公司公告补证：将 2025-08-13 的 $9B Oklahoma investment 从媒体报道源替换为 Google 官方公告。Google 称该投资支持 new data center campus in Stillwater 与 Pryor 扩建。来源：
  - https://blog.google/company-news/inside-google/company-announcements/google-american-innovation-oklahoma/
- 地方流程补证：Stillwater Data Center Economic Development Project Plan 官方听证通知列明 2024-10-07 与 2024-11-04 两场 public hearings、six incentive districts、multi-phased data center development、private investment of $500,000,000 per phase。来源：
  - https://stillwaterok.gov/DocumentCenter/View/3278/NOTICE-TO-THE-PUBLIC-OF-TWO-PUBLIC-HEARINGS-REGARDING-THE-STILLWATER-DATA-CENTER-ECONOMIC-DEVELOPMENT-PROJECT-PLAN
- plat/building-permit 线索：The Stillwegian 2025-11-11 报道 Stillwater Planning Commission 于 2025-11-04 以 4-0 批准 Richmond Road and Highway 177 Addition final plat，覆盖 Lots 1, 2, and 7（202 acres），地址 1500 E. Richmond Road，并称 Lots 1 and 2 building permits had been approved。官方 CivicClerk event URL 可访问但需要 JavaScript，搜索摘要显示 City Council agenda item 为 “Acceptance of the final plat for Richmond Road & Highway 177 Addition in the General Industrial (IG) district at 1500 E. Richmond Road.” 因此 data.json 中将该项标注为 local-media supported / official agenda snippet corroborated，不作为可直接读取的 permit primary record。来源：
  - https://www.thestillwegian.news/planning-commission-advances-google-data-center-final-plat/
  - https://stillwaterok.portal.civicclerk.com/event/2323/files
- 电网/监管侧：OG&E data-center page 称已向 Oklahoma Corporation Commission 提出 large-load tariff，适用于至少 75 MW demand 的新客户等类别，预计 review schedule 约六个月；OG&E/Google 协议页称 Google data center ESA/Capacity Purchase Agreements 需 OCC 正式批准。来源：
  - https://www.oge.com/web/portal/og-e-data-centers
  - https://www.oge.com/web/portal/-/200-press-release
- capacity_mw 保持 null：City of Stillwater 项目页的 700 MW clean energy、OG&E tariff 的 75 MW applicability threshold、以及旧 baseline 的 900 MW planning context 均不能等同 Stillwater 项目 IT load；未找到官方项目 MW/IT-load 口径。
- 冲突/不足：未找到可直接读取的 Stillwater permit-number record、Payne County recorded plat 页面、OCC final approval/order、first-service/energization 证明。verified: true for owner/location/site-work-power-agreement facts; verified: false for capacity, energization, and permit-number specifics.
