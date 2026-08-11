# USDC-0159 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：`null` / no status -> `site work-construction`。City of El Paso states the December 2023 Meta agreement was approved, phase 1 is under way, and a 2026 City release says the existing Meta project is already under construction. Meta's July 28, 2026 announcement also describes the El Paso campus as currently under construction.
  - https://www.elpasotexas.gov/data-centers/
  - https://www.elpasotexas.gov/assets/Press-Releases/2026.04.02-NEWS-RELEASE_City-of-El-Paso-Continues-Community-Engagement-on-Data-Center-Policy-Framework.pdf
  - https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/
- location 补证：City describes the site as approximately 1,000 acres in Northeast El Paso, north side of Stan Roberts Sr. Avenue and west of U.S. Highway 54. The City road-improvement packet states Wurldwide LLC owns approximately 1,038.948 acres at that location. TDLR TABS2026017750 gives the project address as 7001 Stan Roberts Sr, El Paso, TX 79934.
  - https://www.elpasotexas.gov/data-centers/
  - https://www.elpasotexas.gov/assets/Documents/CoEP/Data-Centers/Memo-Seafox-Stan-Roberts-Development-Packet.pdf
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026017750
- permit / construction package：TDLR TABS2026017750, registered 2026-04-15, lists Project Seafox / Seafox Addition as new construction with start date 2025-11-01, completion date 2029-02-28, estimated cost $289M, "Review Complete" status, 12 new buildings, 5 owner substations, and site work on approximately 600 acres / 25,943,100 sq ft.
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026017750
- capacity 更新：`capacity_mw` set to 1000 with basis note. Meta says the campus will have 1 gigawatt of compute capacity and expects to begin bringing capacity online in 2028. This is recorded as compute capacity, not independently confirmed utility interconnection load.
  - https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/
  - https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-New-Strategic-Venture-with-BlackRock-to-Develop-Data-Center-in-El-Paso/default.aspx
- owner / financing 更新：TDLR lists Wurldwide LLC as project owner. Meta and BlackRock announced a venture to develop and own the campus; funds managed by BlackRock are to own 80% and Meta 20%, with Meta leasing the entire campus and serving as initial sole occupant.
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026017750
  - https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/
- power / utility note：City states generation-unit filings are under PUCT review and that the electric utility is seeking approval for a 366 MW natural-gas installation called the McCloud plant. This is not counted as the data center's `capacity_mw`; it is recorded as proposed supporting generation.
  - https://www.elpasotexas.gov/data-centers/
- water note：City's resource hub lists phased water allocations: Tier I average/max 100,000/300,000 GPD, Tier II 750,000/1,000,000 GPD, Tier III average/max 1.5M/2.5M GPD. Meta says it will restore 200% of water consumed by the El Paso data center to local watersheds.
  - https://www.elpasotexas.gov/data-centers/
  - https://datacenters.atmeta.com/2025/10/hello-el-paso/
- 多源冲突 / stale figures：City resource hub still describes the META project as $1.5B and cites approximately 1,800 construction jobs / at least 50 permanent roles. Meta's July 2026 announcement says over $10B from Meta, approximately $14B total development costs for the venture, more than 4,000 construction jobs at peak, 300 operational jobs, and over 2,300 workers already onsite. City draft policy framework also cites approximately $10B. Treat the $1.5B / 1,800 / 50 figures as older or incentive-threshold/resource-hub figures until the City updates its hub.
  - https://www.elpasotexas.gov/data-centers/
  - https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/
  - https://www.elpasotexas.gov/assets/Documents/CoEP/Data-Centers/Draft-Data-Center-Policy-Framework-updated.pdf
- verified: true for identity, location, local approval, construction status, TDLR construction package, owner/venture facts, and the 1 GW compute-capacity claim. Evidence caveat: utility/generation approvals remain under review, and compute capacity should not be treated as confirmed delivered/energized load.
