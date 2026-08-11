# disc019 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-secondary-markets.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 状态刷新：从“TDLR filed; construction listed for August 2026-April 2027”调整为“local process - TDLR Project Registered”。原因：TDLR 是官方来源，但各记录的 Current Status 仍为 Project Registered；虽列出 August 1, 2026 开始日期，未找到独立施工开工/现场作业证据。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027103
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027104
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027105
- 官方 TDLR 核实 Horizon Junction 三个数据中心建筑：
  - Building B：TABS2026027103，1762 County Road 241，189,060 sq ft，$300,000,000，Start Date 2026-08-01，Completion Date 2027-04-01，Registration Date 2026-08-05，Owner AMAZON DATA SERVICES, INC，Design Firm M. ARTHUR GENSLER & ASSOCIATES, INC.。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027103
  - Building C：TABS2026027104，1774 County Road 241，189,060 sq ft，$300,000,000，Start Date 2026-08-01，Completion Date 2027-04-01，Registration Date 2026-08-05，Owner AMAZON DATA SERVICES, INC，Design Firm M. ARTHUR GENSLER & ASSOCIATES, INC.。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027104
  - Building D：TABS2026027105，1782 County Road 241，189,060 sq ft，$300,000,000，Start Date 2026-08-01，Completion Date 2027-04-01，Registration Date 2026-08-05，Owner AMAZON DATA SERVICES, INC，Design Firm M. ARTHUR GENSLER & ASSOCIATES, INC.。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026027105
- 官方 TDLR 另有 Horizon Junction Building M（水楼）：TABS2026027106，1768 County Road 241，4,067 sq ft，$2,000,000，Start Date 2026-09-01，Completion Date 2027-09-01，Registration Date 2026-08-05，Owner AMAZON DATA SERVICES, INC。来源：https://www.tdlr.texas.gov/TABS/Search/Print/TABS2026027106
- 相关但未并入 canonical 规模：TDLR TABS2026025594 是 1752 County Road 241 的 CONFIDENTIAL DATA CENTER / BUILDING A，Owner 同为 AMAZON DATA SERVICES, INC，189,060 sq ft，$300,000,000，Registration Date 2026-07-20，Start Date 2026-08-01，Completion Date 2027-04-01。该记录在地址、业主、规模、工期上与 Horizon Junction 相邻/相似，但官方项目名不是 Horizon Junction；因此记录为 related_projects，不把 Building A 计入 Horizon Junction 三栋 B/C/D。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026025594
- 行业媒体交叉核实：Data Center Dynamics 于 2026-08-07 报道 Amazon Data Services filed with TDLR to develop Horizon Junction facilities B/C/D in Floydada, each 189,060 sq ft and $300M, with construction set for August 2026-April 2027; DCD also指出地块位于 Floydada County Club，且未有关于球场关闭或附近新开发的公开公告。来源：https://www.datacenterdynamics.com/en/news/amazon-files-to-develop-two-new-data-center-campuses-in-texas/
- 地方公共过程/政策背景：Floyd County Record 于 2026-08-04 刊载 Floyd County Commissioners Court open letter，称 county 对 data center development 的监管权限有限，并表示若考虑 Chapter 312 tax abatement，只会考虑满足 air-cooled system 与自备运营电力能力两项要求的发展。来源：https://www.floydcountyrecord.com/2026/08/04/floyd-county-commissioners-court-addresses-data-center-in-open-letter/
- 多源冲突/待核实：
  - All Ag News 于 2026-08-05 称 proposed Amazon campus could include seven data-center buildings across roughly 485 acres；本次只在官方 TDLR 中核实到 Horizon Junction B/C/D 三栋数据中心、Building M 水楼，以及相邻但项目名为 CONFIDENTIAL DATA CENTER 的 Building A。七栋与 485 acres 尚未由官方公开文件核实。来源：https://www.allagnews.com/texas-county-uses-incentives-to-steer-data-centers/
  - 未找到公开 MW 容量、并网队列、utility service/interconnection 记录、正式 county/city permit approval、或现场施工证据；capacity_mw 维持 null。
