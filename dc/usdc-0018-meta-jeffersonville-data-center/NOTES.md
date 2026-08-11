# USDC-0018 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `site work-construction`。依据：IEDC/River Ridge 2024-01-25 官方公告称 Meta 在 2024-01 开始建设、预计 2026 年运营；Jeffersonville Planning and Zoning 的 2024 Annual Report（2025-01 发布）称 2024 年 River Ridge 最大新闻包括 Meta data center groundbreaking。来源：
  - https://iedc.in.gov/events/news/details/2024/01/25/gov.-holcomb-announces-meta-to-build-an-800m-data-center-campus-in-indiana
  - https://www.riverridgecc.com/news/article/gov-holcomb-announces-meta-to-build-an-800m-data-center-campus-in-indiana
  - https://cityofjeff.net/wp-content/uploads/2025/01/2024-Annual-Report.pdf
- location/site scale: 补充 River Ridge Commerce Center、Jeffersonville、619-acre campus、nearly 700,000-square-foot facility。City of Jeffersonville 2024-01-25 本地公告确认 $800M、619 acres、nearly 700,000 sq ft、peak construction jobs >1,200、100 tech jobs；Meta 同日项目页确认 nearly 700,000 sq ft、>$800M investment、约 100 operational jobs、peak construction >1,250。来源：
  - https://cityofjeff.net/2024/01/25/meta-announces-800m-jeffersonville-data-center/
  - https://datacenters.atmeta.com/2024/01/hello-jeffersonville/
- land/entity evidence: River Ridge 2024-04-10 年度经济影响新闻称 2023-12 River Ridge transferred 619 acres to Meta Platforms, Inc.，first phase 为 $800M data center；Indiana State Board of Accounts 发布的 RRDA 2023 audit 称 2023 new investments included 623.20 acres by Blocke, LLC。已在 data.json 记录为 owner/entity 备注与 acreage contradiction，等待 deed/parcel packet 复核。来源：
  - https://www.riverridgecc.com/news/article/river-ridges-economic-impact-on-southern-indiana-tops-2.9-billion-in-2023
  - https://www.in.gov/sboa/WebReports/85126A.pdf
- incentives/utility: IEDC 2024-01-25 官方公告称 IEDC committed a 35-year data center sales-tax exemption for minimum $800M eligible capital, with additional five-year periods per further $800M eligible investment up to 50 years; it also states Jeffersonville and RRDA offered additional incentives and Duke Energy was an enabling partner. EEI July 2026 large-load report lists Duke Energy / Meta / Jeffersonville, IN as an $800M data center project but gives no MW for this project. 来源：
  - https://iedc.in.gov/events/news/details/2024/01/25/gov.-holcomb-announces-meta-to-build-an-800m-data-center-campus-in-indiana
  - https://www.eei.org/-/media/Project/EEI/Documents/Issues%20and%20Policy/List%20of%20Large%20Customer%20Projects%20and%20Tariffs
- capacity_mw: 保持 `null`。本次没有找到官方/local-government MW 容量。第三方/行业来源存在冲突：datacenter.fyi lists 407 MW construction；interconnection.fyi lists 250+ MW for Meta - Jeffersonville；Helm contractor page says 150 MW hyperscale facility；另有 Blocke LLC/Meta <10 MW or 2.985 MW record，可能是不同 permit/interconnection record。未提升到主字段。来源：
  - https://www.datacenter.fyi/public-record/meta-jeffersonville-646ed5d7
  - https://www.interconnection.fyi/data-center/project/646ed5d7
  - https://www.helmgroup.com/projects/jeffersonville-data-center/
  - https://www.interconnection.fyi/data-center/project/meta-85e684f0
- current local context: LPM 2026-08-04 报道 Jeffersonville City Council approved a one-year data-center moratorium to update the UDO. 未找到同等官方 ordinance packet；该报道未证明既有 Meta 项目被暂停或变更，因此不改变本项目 status。来源：
  - https://www.lpm.org/news/2026-08-04/jeffersonville-approves-1-year-data-center-moratorium
- 未核实项：Clark County/Jeffersonville building permit number、site-plan/case number、final street address/parcel list、official MW/utility service capacity、actual energized/operational date。
- verified: true for official facts above; verified: false for capacity_mw, permit/case numbers, and exact operational timing.
