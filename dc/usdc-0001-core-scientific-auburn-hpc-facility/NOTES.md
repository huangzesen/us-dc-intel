# USDC-0001 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Announced/early development
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 Announced/early development 调整为 Site work/construction evidence located。依据是 ADEM 官方 eFile/permit-application 页面已列出 CORE SCIENTIFIC AUB1 / 1571 WEST SAMFORD AVENUE AUBURN / WATER-CONSTRUCTION STORMWATER，以及 2026-02-18、2026-06-25、2026-07-08 NOI 记录；区域 permit 报道另列 2026-02-19 Auburn $55,000,000 building permit。尚未找到 CO、utility energization、commissioning 或 full buildout 公开记录。
- capacity 更新：`capacity_mw` 由 null 更新为 50。Core Scientific 当前 Auburn 1 页面列出 Total Power Capacity: 50 MW、Campus Footprint: 6 acres、Total Square Feet: 39,202，地址为 1571 W Samford Ave。2025-02-19 Core Scientific / Made in Alabama 公告中的 16 MW 保留为 launch capacity，不视为与 50 MW total power capacity 冲突。
- owner/operator 更新：`owner` 由 null 更新为 Core Scientific operator/lessee。Core 2025-02-19 公告称其 leased the building and planned an option to purchase；本次未核实产权转移，因此不写成 fee owner。
- 新增官方/一手事实：
  - 2021-02-16 Auburn City Council minutes: Resolution No. 21-042 approved conditional use for industrial use (data center), Apollo Conditional Use, at 1571 West Samford Avenue. URL: https://api2.auburnalabama.org/ePacket/2220/file/5802
  - 2026-08-11 accessed ADEM permit applications: BRASFIELD AND GORRIE LLC / CORE SCIENTIFIC AUB1 / 1571 WEST SAMFORD AVENUE AUBURN / LEE / WATER-CONSTRUCTION STORMWATER. URL: https://adem.alabama.gov/permit-applications?page=1
  - 2026-08-11 accessed ADEM eFile Master ID 55376: NOI records for Brasfield and Gorrie LLC, Lee County, permit numbers ALR10C7R4 and ALR10C87N, dated 2026-02-18, 2026-06-25 and 2026-07-08. URL: https://app.adem.alabama.gov/eFile/Results.aspx?MasterID=55376
  - 2026-06-12 City of Auburn archived-news search result: temporary closures at 1571 West Samford Avenue on June 8, 15, 17, 23, 29 and July 1 & 8 as oversized delivery trucks access the site. URL: https://www.auburnal.gov/news/archived/
- 新增公司/州与区域来源：
  - 2025-02-19 Core Scientific announcement: Auburn HPC facility at 1571 W Samford Ave, housed in existing AUBix facility, 16 MW launch capacity, $135M initial investment, expected total investment above $400M, lease and planned option to purchase. URL: https://investors.corescientific.com/news-events/press-releases/detail/107/core-scientific-announces-expansion-into-auburn-alabama-with-new-high-performance-computing-facility
  - 2025-02-19 Made in Alabama announcement: confirms existing AUBix location, 16 MW launch, $135M initial/$400M expected investment, employee retention/growth targets. URL: https://www.madeinalabama.com/2025/02/core-scientific-bringing-high-performance-computing-operation-to-auburn/
  - 2026-02-23 The Bama Buzz permit report: $55M building permit for Core Scientific data center in Auburn; Brasfield & Gorrie listed as lead contractor. URL: https://thebamabuzz.com/55-million-core-scientific-facility-in-auburn-among-15-new-high-dollar-building-permits/
  - 2026-08-11 accessed Core Scientific Auburn 1 facility page: 50 MW total power capacity, 6 acre campus, 39,202 square feet, 1571 W Samford Ave. URL: https://corescientific.com/high-density-data-centers/auburn-al/
- contradictions: none requiring `contradictions[]`; 16 MW is launch capacity from 2025 announcements, while 50 MW is current company-published total power capacity.
- evidence gaps: public Auburn primary building-permit record for the reported $55M permit not located; ADEM PDF viewer documents are indexed but browser access requires session/cookie handling; no energization/CO/commissioning/full-buildout record located.
- verified: true for address, operator/lessee status, company-published capacity, and construction-stormwater/site-work evidence; false for energization/full-buildout because no public proof was located.
