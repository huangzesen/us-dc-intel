# USDC-0043 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Missouri DED's May 20, 2026 regional announcement describes planned Google/Meta-area investments, but does not identify a Meta parcel or site-specific project
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: unvalidated regional lead -> partial live. Meta's August 20, 2025 newsroom post, updated November 14, 2025, states that the Kansas City Data Center is operational and serving traffic; this supports live-service status but not full campus buildout. Source: https://about.fb.com/news/2025/08/metas-kansas-city-data-center/
- owner: null -> Meta Platforms, Inc. Meta's March 24, 2022 company announcement confirms Kansas City as Meta's newest data center, with more than $800 million investment, about 100 operational jobs, and more than 1,300 peak construction workers. Source: https://datacenters.atmeta.com/2022/03/hello-kansas-city/
- location: Kansas City/Clay County Northland lead -> Zone 3, Golden Plains Technology Park. Kansas City Ordinance No. 210841, passed September 23, 2021, approved the preliminary plat for Zone 3 on about 374.89 acres generally at the northwest corner of I-435 and US-169 with N.W. 128th Street as northern boundary. Source: https://clerk.kcmo.gov/LegislationDetail.aspx?GUID=B4B56878-A985-43D7-A86E-1C499DF6EC99&ID=5140162&Options=&Search=
- local process: Kansas City passed Committee Substitute for Ordinance No. 211119 on February 3, 2022, authorizing water/wastewater service and water-main agreements with Velvet Tech Services, LLC for Zone 3 of Golden Plains Technology Park. Source: https://clerk.kcmo.gov/LegislationDetail.aspx?GUID=88AC2B70-4145-4F7F-BC91-54D971154EA7&ID=5363240&Options=&Search=
- permitting: Missouri DNR issued de minimis construction air permit 042024-001 on April 9, 2024 for Velvet Tech Services LLC-Kansas City, Application/Project No. 2023-10-010, Site ID 047-0211, Kansas City, Clay County. Source: https://dnr.mo.gov/air/business-industry/air-permits/velvet-tech-services-llc-kansas-city-042024-001
- infrastructure follow-through: Kansas City Ordinance No. 240917, passed November 7, 2024, included Water Fund appropriations for "M-22-15, WME - Project Velvet" and related water-main replacement lines. Source: https://kansascity.legistar.com/LegislationDetail.aspx?From=RSS&FullText=1&G=D2E89A09-8736-4EFB-B4AE-572E0903BD5A&GUID=E9253B41-D5DF-44DA-AAE9-EB3438B0DFC1&ID=6890129
- capacity_mw remains null. Search found non-primary MW estimates and regulatory tariff thresholds involving large-load customers, but no primary Meta, Kansas City, Missouri DNR, or PSC source that states the Kansas City data center's actual MW capacity. Evidence gap retained rather than inferring capacity from tariff eligibility or third-party trackers.
- conflict/cleanup note: the prior May 20, 2026 Missouri DED Google/regional announcement is no longer used as the lead status evidence for this campus; it is retained only as regional context. No direct contradiction found among primary Meta, Kansas City, and Missouri DNR records.
- verified: true for owner, location, local process/permitting, and live-service status; verified: false for MW capacity and full-buildout status due to lack of primary evidence.
