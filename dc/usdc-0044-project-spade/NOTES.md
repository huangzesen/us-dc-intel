# USDC-0044 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Missouri DED and Google's current location material identify a planned/in-development data center in Montgomery County/New Florence
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: 从 announcement / in-development 上调为 `approved-permitted / pre-construction`。理由：Montgomery County 项目页公开列出 Project Spade Site Plan / FAQ / road-opening materials；Google、Missouri DED、项目页、行业追踪与公开记录报道共同确认 New Florence/Montgomery County 项目已进入本地行政审查/许可材料阶段。仍未找到 CO、energization、commissioning、service record 或 full operation 证据。
  - https://mcmo.us/google/
  - https://ded.mo.gov/press-room/google-deepens-missouri-roots-15-billion-community-investment-montgomery-county
  - https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Press_Release__Google_Deepens_Missouri_Roots.pdf
- owner: 从 `null` 更新为 `Google`。Google 2026-05-20 press release 称其在 New Florence/Montgomery County 的新 data center；Project Spade 项目页称 Greater Montgomery County Economic Development Council is working with Google。
  - https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/missouri-programs/
  - https://www.projectspade-missouri.com/
- scope/current project page: Project Spade 当前项目页称 campus will use closed-loop, non-evaporative air cooling, construction anticipated late 2026, with 2 initial data-center buildings plus support buildings, 300 local jobs, no water for cooling, and water limited to domestic uses during initial phases.
  - https://www.projectspade-missouri.com/
- water/environment: Project site added/links a Water Risk Assessment Summary for the Cambrian-Ordovician Aquifer, completed Q1 2026. Memo reports low chronic depletion risk and no curtailment events, but high current/future water-scarcity ratios and high risk of more intense precipitation events. This is project technical material, not a permit approval or operating-withdrawal record.
  - https://www.projectspade-missouri.com/documents/water-risk-memo-cambrian-ordovician-aquifer.pdf
- DNR permitting context: Missouri DNR says it does not regulate data centers specifically, but requires applicable air/water/waste permits; before a facility is built, land disturbance permit is required if one or more acres will be disturbed; water discharge permits include monitoring/reporting requirements. DNR also says it does not regulate water amount/usage except out-of-state exporting and major-user annual reporting.
  - https://dnr.mo.gov/data-e-services/centers
  - https://dnr.mo.gov/data-e-services/missouri-gateway-environmental-management-mogem
- local/permit evidence caveat: Search found county page materials, but `mcmo.us` did not directly open from shell/browser during refresh. Accessible public-records reporting describes Montgomery County Planning & Zoning administrative review dated 2025-11-17/18, permitted-by-right treatment in Commercial zoning, site plan/grading/stormwater/water/wastewater/Ameren-MISO documentation, and MDNR permit MORA29107 for Project Lumberjack / Part of Project Spade at 580 Tree Farm Road, covering 23.04 acres and valid until 2027-02-07. Because the direct MDNR permit record was not independently retrieved, this is retained with an access caveat rather than treated as fully direct official text.
  - https://mcmo.us/google/
  - https://annafarrar.substack.com/p/what-project-spade-really-is
- capacity: Official Google/DED sources do not disclose Project Spade MW. Google says it has contracted for more than 1 GW of new generation capacity in Missouri and is supporting more than 500 MW additional capacity with Ameren, but those are broader Missouri energy commitments. DCD reports Project Spade as targeting 1.2 GW on a 934-acre Related Digital plot; Baxtel lists Ameren as utility provider and 934-acre lot. `capacity_mw` remains `null`; 1.2 GW is retained as a non-official capacity claim.
  - https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Press_Release__Google_Deepens_Missouri_Roots.pdf
  - https://www.datacenterdynamics.com/en/news/google-pledges-15bn-investment-in-new-florence-missouri/
  - https://baxtel.com/data-center/google-project-spade-campus
- conflicts: Current project page says 2 initial buildings; public-records/industry tracker material describes 3 large primary buildings or earlier site-plan scale. Treat 2-building scope as current project-facing plan, with 3-building/site-plan descriptions preserved as conflict/context until county plan sheets are directly rechecked.
  - https://www.projectspade-missouri.com/
  - https://www.datacentermap.com/usa/missouri/st-louis/project-spade-dc1/
  - https://annafarrar.substack.com/p/what-project-spade-really-is
- verified: false. Core Google/DED/project-site facts are verified; local administrative-review and MDNR permit-specific details remain caveated because direct county/MDNR documents were not fully retrievable in this refresh.
