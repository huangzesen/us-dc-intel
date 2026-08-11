# USDC-0028 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: A company filing describes a 150 MW site and planned expansion to 300 MW in 2025–2027; the accessible government record establishes the county/city permit framework but no project-specific building, u
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status/capacity 更新：从“公司披露 150 MW、2025-2027 规划扩至 300 MW但缺项目级政府证据”收敛为“Calvert City / Paducah-Calvert City 150 MW operating facility；300 MW 扩建仍未证实为获批、开工、CO、并网或建成”。来源：Core Scientific Calvert City facility page（page modified 2026-04-16, 150 MW / 15 acres / 60,000 sf / 1035 Shar-Cal Rd）https://corescientific.com/high-density-data-centers/calvert-city-ky/；Core Scientific 2025 Form 10-K（filed 2026-03-02, TVA gross utility power capacity 150 MW for Paducah-Calvert City, Kentucky）https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001628280-26-013305/core-20251231.htm
- owner/location 补证：Core site gives 1035 Shar-Cal Rd, Calvert City, KY 42029；SEC collateral schedule identifies the Calvert City real property as 35.6193 acres at 1035 Shar Cal Rd. held in fee by American Property Acquisition, LLC, in the Core Scientific ownership chain. 来源：https://corescientific.com/high-density-data-centers/calvert-city-ky/；https://www.sec.gov/Archives/edgar/data/1839341/000119312523058334/d411824dex101.htm
- local-government check：City of Calvert City forms page（modified 2026-07-01）lists planning/zoning, conditional use, variance, floodplain development, highway-oriented commercial development criteria, zoning compliance, zoning ordinance/map amendment, and commercial-industrial water/sewer service forms, but no searchable/project-specific Core Scientific expansion permit or approval was located there. 来源：https://calvertcityky.gov/forms/
- company portfolio check：Core Q2 2026 release（released 2026-07-28）reports AMD/leased capacity and one Kentucky facility, but does not allocate new capacity to Calvert City or confirm expansion above 150 MW. 来源：https://investors.corescientific.com/news-events/press-releases/detail/139/core-scientific-announces-second-quarter-2026-results
- 多源冲突/限制：older company planning deck referenced a planned 300 MW expansion for 2025-2027, while current Core site and 2025 Form 10-K still show 150 MW for the Kentucky facility. Treat 300 MW as projected/unverified until a project-specific government approval, construction filing, utility record, or updated company site/SEC filing confirms otherwise.
