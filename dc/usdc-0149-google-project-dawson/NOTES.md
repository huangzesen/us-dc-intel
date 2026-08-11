# USDC-0149 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `site work-construction`。Dorchester County Economic Development 在 2025-10-13 称 Google 的两个 Dorchester County 数据中心园区已处于 active construction；Google 2025-10-13 官方博客称其 2026-2027 年 South Carolina 投资将继续建设 Dorchester County 两个新站点。来源：
  - https://www.dorchesterforbusiness.com/news/google-expands-investment-in-dorchester-county/
  - https://blog.google/company-news/inside-google/company-announcements/google-american-innovation-south-carolina/
- owner: `null` -> `Google`。South Carolina Governor / Commerce 2024-09-26 公告确认 Google 将在 Dorchester County 建设两个新数据中心园区，其中一个位于 Ridgeville 的 Pine Hill Business Campus；Dorchester County fact sheet 复述同一事实。来源：
  - https://governor.sc.gov/news/2024-09/google-grows-south-carolina-footprint-new-dorchester-county-operations-expansion
  - https://web.archive.org/web/20260729100110/https://www.dorchestercountysc.gov/business/data-center-fact-sheet (Wayback capture 2026-07-29 of Dorchester County fact sheet; live URL returns HTTP 403 to automated fetchers)
  - https://datacenters.google/locations/south-carolina/
- location county: `Berkeley` -> `Dorchester`。seed/SKILL 中的 Berkeley County 与官方当前证据冲突；官方州/县/Google/PSC 证据均将 Ridgeville / Pine Hill Business Campus / Project Dawson 放在 Dorchester County。Berkeley County 在州公告中对应 Google 另一个 Moncks Corner / Mount Holly Commerce Park expansion，不是本条 Project Dawson。来源：
  - https://governor.sc.gov/news/2024-09/google-grows-south-carolina-footprint-new-dorchester-county-operations-expansion
  - https://web.archive.org/web/20260729100110/https://www.dorchestercountysc.gov/business/data-center-fact-sheet (Wayback capture 2026-07-29 of Dorchester County fact sheet; live URL returns HTTP 403 to automated fetchers)
  - https://dms.psc.sc.gov/Attachments/Matter/c7acfa51-279d-4898-9aa6-50cac971c2e9
- utility / power milestone: SC PSC Docket 2023-379-E 显示 Dominion Energy South Carolina 与 Mallard, LLC / Project Dawson 的 electric service contract；合同 public version 列出 premises/service address 为 Ridgeville Research Center Drive 附近的 TMS 150-00-00-199 与 157-00-00-001。PSC Docket 2024-91-E / Order No. 2024-358 于 2024-05-28 批准 Dawson 230 kV Substation 和 Canadys-Dawson 230 kV line work 的 like-facility determination。来源：
  - https://dms.psc.sc.gov/Web/Dockets/Detail/118825
  - https://dms.psc.sc.gov/Attachments/Matter/c7acfa51-279d-4898-9aa6-50cac971c2e9
  - https://dms.psc.sc.gov/Web/Dockets/Detail/118947
  - https://dms.psc.sc.gov/Attachments/Order/5385de10-0598-4a95-b52d-2d5eb5bbd21d
- latest utility status: Dominion 2026-06-30 quarterly update says Dawson Substation Phase 1 was energized on 2025-10-07; Phase 2 construction is complete except system protection checkouts; transmission pole delivery delay moved project completion from 2026-10-01 to 2026-12-31. This is utility infrastructure status only, not proof that the data center is operational. 来源：
  - https://dms.psc.sc.gov/Attachments/Matter/6dd77535-82b1-4818-bb6c-f7cf41bb3413
- capacity_mw: still `null`。PSC filings confirm substantial load and 230 kV infrastructure, but public contract capacity/demand values are redacted; no official MW capacity was found in this refresh.
- conflicts: baseline/SKILL Berkeley County location conflicts with current official sources and is recorded in `contradictions`; capacity remains unresolved due to redactions.
- URL swap (2026-08-11 fix pass): the live Dorchester County fact sheet URL https://www.dorchestercountysc.gov/business/data-center-fact-sheet returns HTTP 403 to automated fetchers (Akamai WAF blocks non-browser clients; the whole www.dorchestercountysc.gov domain returns 403 from this environment, verified 2026-08-11). The page itself exists and is indexed; content confirmed via search snippet and Wayback capture (Google $3.3B South Carolina announcement 2024-09-26; two Dorchester County campuses at Pine Hill Business Campus, Ridgeville and Winding Woods Commerce Park, St. George). Replaced the URL in data.json `sources.urls` and in the citations above with the Wayback Machine capture https://web.archive.org/web/20260729100110/https://www.dorchestercountysc.gov/business/data-center-fact-sheet (captured 2026-07-29, HTTP 200 verified). Live official corroboration of the same facts: https://www.dorchesterforbusiness.com/news/google_breaks_ground/ (HTTP 200 verified 2026-08-11).
