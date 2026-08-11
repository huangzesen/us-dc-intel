# USDC-0103 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Proposed/under development, with no verified construction
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 `local process / approved-permitted, with no verified construction`。官方记录确认 2021 年 Chapter 121A 本地审批/推荐路径，但本次未找到施工、建筑许可、CO、并网、ISO-NE formal queue、或 full buildout 证据。来源：
  - https://www.cityofwestfield.org/DocumentCenter/View/10541/Planning-Board-recommendation-on-Servistar-LLC-application-for-Data-Center
  - https://www.cityofwestfield.org/AgendaCenter/ViewFile/ArchivedAgenda/_10182021-2046
- owner 从 `null` 更新为 `Servistar Realties LLC`。2021 City Council Finance Committee agenda 将申请人列为 Servistar Realties, LLC，并列出 10 栋、2.74 million square feet、155.49 acres 与项目地块。来源：
  - https://www.cityofwestfield.org/AgendaCenter/ViewFile/ArchivedAgenda/_10182021-2046
- location 补充项目区/地块描述：Servistar Industrial Way、Campanelli Drive、Ampad Road、Egleston Road 附近，靠近 Westfield-Barnes Regional Airport。来源：
  - https://www.cityofwestfield.org/AgendaCenter/ViewFile/ArchivedAgenda/_10182021-2046
  - https://www.cityofwestfield.org/DocumentCenter/View/10541/Planning-Board-recommendation-on-Servistar-LLC-application-for-Data-Center
- capacity_mw 从 `null` 更新为 evidence-qualified reported value：274 MW full buildout。Boston Globe 2026-07-14 报道该项目 fully built out would require 274 MW；本次未在官方 city record 中找到 MW 容量，因此 data.json 标为 `reported_full_buildout_not_permit_confirmed`。来源：
  - https://www.bostonglobe.com/2026/07/14/business/westfield-data-center-backlash-healey/
- 新增 2026-06 City-hosted applicant fact sheet：closed-loop cooling、DC cooling near-zero potable water、non-cooling 5,000-10,000 GPD、WG&E independent customer / isolated island transmission-grid service claims。标注为 applicant claims，不视为 utility approval。来源：
  - https://www.cityofwestfield.org/DocumentCenter/View/17988/Servistar-Data-Center-Campus-Water-Energy-Fact-Sheet
- 新增 2026-06-25 state incentive risk：Governor Healey announced Massachusetts would pause accepting data-center sales/use-tax exemption applications until stronger guardrails are in place. 这是 statewide policy/incentive context，不是 Servistar-specific denial。来源：
  - https://www.mass.gov/news/governor-healey-halts-data-center-tax-incentive-and-calls-for-strict-guardrails-to-protect-ratepayers-environment-public-health
- 新增 2026-07-06 local moratorium context：Westfield City Council official agenda listed second reading/final passage of zoning ordinance relative to a moratorium on data centers；local media reported final approval/confirmation of the 12-month moratorium. 未找到 official minutes 或 signed ordinance text；Boston Globe 报道称该 moratorium would not prevent the already-approved Servistar project from going forward, so this is recorded as policy/process risk rather than construction-stop evidence. 来源：
  - https://www.cityofwestfield.org/AgendaCenter/ViewFile/Agenda/_06182026-8546
  - https://www.cityofwestfield.org/AgendaCenter/ViewFile/Agenda/_07062026-8585
  - https://thereminder.com/local-news/hampden-county/westfield/westfield-city-council-approves-data-center-moratorium/
  - https://www.bostonglobe.com/2026/07/14/business/westfield-data-center-backlash-healey/
- 冲突/不足：
  - Moratorium scope: official agenda confirms the final-passage item and media reports approval, but official minutes/signed ordinance text were not located. Media says it does not stop already-approved Servistar; local testimony reported unresolved prerequisites such as permit acceptance, property purchase, and ISO-NE formal consideration.
  - Capacity: 274 MW is media-reported; official materials reviewed here confirm 10 buildings and 2.7-2.74 million square feet but not a permitted MW.
  - Construction/energization: no current first-party construction, building permit, CO, or utility energization record located.
