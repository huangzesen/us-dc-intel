# USDC-0200 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Two related land-use tracks were located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 land-use approved/permitted, not construction: Powhatan County Board of Supervisors minutes confirm Newport Equities O-2025-31 and O-2025-32 were approved 5-0 on 2025-10-27, but the minutes also describe later site-plan detail work and pre-vertical-construction transportation improvements. Source: https://www.powhatanva.gov/AgendaCenter/ViewFile/Minutes/_10272025-1363
- County press release on 2025-10-29 confirms the 61.8-acre Newport approval follows the prior 120-acre approval and results in a combined 181-acre planned 2,000,000-square-foot data center campus. It also confirms utility-improvement proffers and CUP height relief up to 75 feet, with screened rooftop equipment up to 90 feet. Source: https://www.powhatanva.gov/DocumentCenter/View/9122/10292025-Press-Release---Data-Center
- capacity_mw set to 365 as developer/JLL-reported initial deployment. Official county minutes support a 300-400 MW demand range and state the applicant had a Dominion will-serve but no guarantee; JLL reports an initial 365 MW Dominion Energy deployment and on-site 500kV, 230kV, and 115kV transmission lines. Sources: https://www.powhatanva.gov/AgendaCenter/ViewFile/Minutes/_10272025-1363 ; https://www.jll.com/en-us/newsroom/powhatan-county-approves-180-acre-data-center-development
- owner/applicant updated from null to Newport Equities LLC / Province Group LLC. Powhatan identifies Newport Equities LLC as the applicant; JLL identifies Newport Equities LLC as an affiliate of Province Group LLC. Final operator/end user remains unverified. Sources: https://www.powhatanva.gov/AgendaCenter/ViewFile/Minutes/_10272025-1363 ; https://www.jll.com/en-us/newsroom/powhatan-county-approves-180-acre-data-center-development
- Permit check: Powhatan County commercial permit-log index listed 2026 monthly reports through June 2026. January-June 2026 logs were searched for LC West, Newport, Province, data center, Page Road, and tax-map identifiers; no project building permit entry was found in that published set. Source index: https://www.powhatanva.gov/211/Commercial-Permit-Log-Report
- No source conflict requiring `contradictions` entry: official 300-400 MW range and JLL 365 MW point estimate are consistent enough to treat 365 MW as developer-reported within the official range. Remaining evidence gaps: no verified building permit, certificate of occupancy, construction start, energized status, final utility interconnection record, signed end-user/operator, or direct Dominion project record.
