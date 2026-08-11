# USDC-0172 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: TCEQ draft federal operating-permit process reached a notice-and-comment hearing; final permit issuance and local construction records were not validated
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从仅验证到 TCEQ draft federal operating-permit hearing，提升为 `site work-construction / approved-permitted`（地方 permit/TDLR 施工注册已核实），但 TCEQ Title V O4790 仍单独标注为 pending/technically complete，不能视为最终 operating permit 或新增排放授权。来源：https://data.sanantonio.gov/dataset/building-permits；https://www.tceq.texas.gov/assets/public/permitting/air/reports/applications/titlev-pending-permits.html
- 地址补全为 5207 Rogers Road, San Antonio, TX 78251。TCEQ hearing notice、TDLR TABS 和 City permit rows 均指向该地址。来源：https://www.tceq.texas.gov/downloads/agency/decisions/hearings/notices/2026/2026-05-28-vantage-data-centers-tx21-llc-o4790-nch.pdf/@@download/file/2026-05-28-vantage-data-centers-tx21-llc-o4790-nch.pdf；https://www.tdlr.texas.gov/TABS/Projects/TABS2024005974
- TDLR TABS2024005974（登记日 2023-11-22）核实 TX21 Core and Shell +16MW Fit-Out：360,000 sf、$157.0M、新建、start 2023-12-11、completion 2025-06-01、current status Review Complete。capacity_mw 由 null 更新为 16，但仅代表该官方项目名中的 +16MW fit-out phase，未核实总 campus/TX2/TX22 MW。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2024005974
- City of San Antonio issued-permit dataset核实 TX21 interior finish-out permits：COM-IFO-PMT25-40500006（Level 2 Interior Finish Out，issued 2025-01-24）与 COM-IFO-PMT25-40500271（Level 1 Interior Finish Out，issued 2025-06-03），地址均为 5207 ROGERS RD。来源：https://data.sanantonio.gov/dataset/building-permits
- TDLR TABS2026003003（登记日 2025-10-09）核实 TX22 new construction：214,526 sf、$272.15M、start 2025-10-22、completion 2027-06-15、current status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026003003
- TDLR TABS2026006358（登记日 2025-11-19）核实 TX21 Tenant Fit-out：162,785 sf、$135.0M、start 2025-12-01、completion 2026-06-02、owner VANTAGE DATA CENTERS TX2 LLC、current status Project Registered。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026006358
- City current-year applications dataset核实 TX22/onsite-power local process：COM-PRJ-APP26-39800134（EXPRESS-Complex Plans-Tx22 Building，submitted 2026-01-24，duplicate row issued 2026-06-03，429,310 sf，$365.8M）；COM-PRJ-APP26-39800204（Stationary Power，submitted 2026-02-04，issued 2026-05-18，VoltaGrid）；MEP-TRD-APP26-33110651（VoltaGrid 123-TEMP Power，submitted 2026-04-20，issued 2026-04-21）。来源：https://data.sanantonio.gov/dataset/building-permits
- owner 更新：官方记录出现 Vantage Data Centers、Vantage Data Centers TX21 LLC、VANTAGE DATA CENTERS TX2 LLC 等实体名，均保留在 owner 字段；未将其视为冲突。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2024005974；https://www.tdlr.texas.gov/TABS/Projects/TABS2026006358；https://www.tceq.texas.gov/downloads/agency/decisions/hearings/notices/2026/2026-05-28-vantage-data-centers-tx21-llc-o4790-nch.pdf/@@download/file/2026-05-28-vantage-data-centers-tx21-llc-o4790-nch.pdf
- 冲突/不足：官方来源足以确认 construction/local-permit activity，但未找到官方 Certificate of Occupancy、full energization/full buildout、总 MW、最终 Title V O4790 issuance。第三方/媒体对 operational 或 partial operational 的描述未用于提升到 energized/full buildout。
