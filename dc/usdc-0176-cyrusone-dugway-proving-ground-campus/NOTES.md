# USDC-0176 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Proposed/under review; Utah government material says Army exclusive negotiations began in March 2026 and environmental review is required before construction
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 announced / exclusive negotiations：U.S. Army 于 2026-03-26 conditionally selected CyrusOne for an Enhanced Use Lease data-center project at Dugway Proving Ground；the deal is not yet final, and USACE is expected to support lease negotiations and environmental review before construction. Source: https://www.army.mil/article/291360/army_reaches_conditional_agreement_with_private_industry_for_hyperscaled_data_centers
- 官方 fact sheet 补充：CyrusOne / Dugway Proving Ground, Utah planned operational date is 2029, and the selection is the first step toward a formal lease agreement while Army retains ownership of the land. Source: https://api.army.mil/e2/c/downloads/2026/03/27/03590778/data-center-eul-fact-sheet.pdf
- location/owner 补强：Army source identifies an approximately 1,201-acre Dugway Proving Ground site and describes CyrusOne as a portfolio company jointly held by funds managed by KKR and BlackRock. Source: https://www.army.mil/article/291360/army_reaches_conditional_agreement_with_private_industry_for_hyperscaled_data_centers
- capacity_mw 从 null 更新为 1000。Grand County / Utah public-notice inventory table lists "CyrusOne at Dugway Proving Ground" at 1,000 MW and PROPOSED; Cleanview also lists 1,000 MW, planned, and 1,201 acres. Sources: https://www.utah.gov/pmn/files/1444799.pdf and https://cleanview.co/data-centers/utah/2293/cyrusone-dugway-proving-ground
- 更正旧 action text：prior data.json action said 1,500 MW, but the visible Utah inventory row shows 1,000 MW for CyrusOne; 1,500 MW appears in the adjacent Antelope Data Center row. This is recorded as a contradiction/history item rather than silently dropped. Source: https://www.utah.gov/pmn/files/1444799.pdf
- Tooele County public information page corroborates current conditional status: the Dugway / CyrusOne arrangement is conditionally selected by the Army, and specific facilities would still go through additional approvals. The page does not show a visible last-updated date, so the evidence date is this refresh/access date. Source: https://growtooele.com/?page_id=226
- Current federal risk signal: Federal News Network reported on 2026-07-24 that House FY2027 defense-authorization language would add restrictions for data centers on DoD land, and Army officials said the measure could affect ongoing negotiations. No enacted approval/denial or project-specific construction milestone was found. Source: https://federalnewsnetwork.com/congress/2026/07/congress-ramps-up-scrutiny-of-pentagon-ai-data-center-plans/
- 未核实/证据不足：no Tooele County permit, executed Army lease, NEPA decision/FONSI/ROD, utility interconnection approval, construction start, or energized/operational evidence found in this refresh.
- verified: true for conditional selection, owner/backers, site acreage, proposed status, FY2029 IOC target, and approval caveats; verified: false for final permitted status, construction, interconnection, and any Army-confirmed MW capacity.
