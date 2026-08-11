# USDC-0189 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `approved-permitted`; capacity_mw remains `null`.
- Official SEPA record found: Washington Department of Ecology SEPA Register record 202403581 lists City of Quincy as lead agency, file `SEPA 2024-008`, document type `ODNS/NOA`, issued 2024-08-19, comments due 2024-09-02, for `MWH08 Data Center`. Source: https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202403581
- Scope/location from City of Quincy ODNS/NOA: Microsoft Corporation applied 2024-05-29 for a 455,000-square-foot, two-story industrial data center on the existing Microsoft MWH campus, including backup-power generator facilities, parking, fuel storage, and infrastructure improvements. ODNS/NOA location is 1515 Port Industrial Way, parcel 042009305. Source: https://apps.ecology.wa.gov/separ/Main/SEPA/Document/DocumentOpenHandler.ashx?DocumentId=183345
- Ecology Facility/Site record found for `MWH08 Data Center`, FS ID 100002672, at 1500 Port Industrial Way, Quincy, WA 98848, GIS 47.237071 / -119.878668. It lists Construction Stormwater General Permit interaction `WAR313961` with start date 2024-08-28. Source: https://apps.ecology.wa.gov/facilitysite/FacilitySite/FacilitySiteReport/100002672
- Ecology PARIS facility summary as of 2026-08-11 shows Construction Stormwater General Permit `WAR313961` version 1 effective 2024-10-07 to 2025-12-31 and version 2 effective 2026-01-01 to 2030-12-31; version 2 is active. PARIS also shows all-time counts of 2 violations/triggers, 0 inspections, and 0 enforcements, but this refresh did not retrieve detailed violation/trigger pages. Source: https://apps.ecology.wa.gov/paris/FacilitySummary.aspx?FacilityId=100002672
- Renewal NOI dated 2025-06-24 lists Navix Engineering as permittee/project engineer, Microsoft as site contact and site owner, total site/project size 179.87 acres, disturbed area 36.7 acres, estimated project start date 2024-12-01, estimated completion date 2027-07-01, and discharge to three infiltration ponds. Source: https://apps.ecology.wa.gov/paris/DownloadDocument.aspx?id=565083
- Ecology renewal coverage letter dated 2025-11-19 confirms WAR313961 permit coverage effective 2026-01-01 and expiring 2030-12-31. Source: https://apps.ecology.wa.gov/paris/DownloadDocument.aspx?id=601683
- Conflict/normalization note: SEPA/ODNS uses 1515 Port Industrial Way and parcel 042009305; Ecology Facility/Site and PARIS use 1500 Port Industrial Way with nearby coordinates. Treated as the same MWH08 campus/project, but both address variants were preserved in `data.json`.
- Evidence limits: no official IT/electrical capacity MW located; no official energized, partial-live, full-buildout, or vertical-construction completion evidence located; City SmartGov portal was found but no specific building permit record was retrieved in this refresh.
