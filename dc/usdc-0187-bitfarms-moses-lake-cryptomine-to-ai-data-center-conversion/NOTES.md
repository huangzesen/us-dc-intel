# USDC-0187 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `approved-permitted`. 依据：Washington Ecology SEPA register 显示 City of Moses Lake file `PLN2025-0092` 已在 2025-12-05 发布 ODNS/NOA-M，并在 2026-01-20 发布 DNS；Keel 2026-05-11 称 Moses Lake 等 near-term sites 已 secured zoning approvals，2026-08-10 称 priority sites nearing full permitting。来源：https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202505050 、https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202600272 、https://investor.bitfarms.com/news-releases/news-release-details/keel-infrastructure-reports-first-quarter-2026-results 、https://investor.bitfarms.com/news-releases/news-release-details/keel-infrastructure-reports-second-quarter-2026-results
- capacity_mw: `null` -> `18`. Bitfarms 2025-11-13 公告称 Washington 现有 18 MW Bitcoin mining facility 将转换为 HPC/AI，供应协议覆盖 18 MW gross capacity，目标 2026-12 完成。来源：https://investor.bitfarms.com/news-releases/news-release-details/bitfarms-announces-plans-conversion-washington-site-hpcai
- location 补齐：7906 Randolph Rd NE, Moses Lake, WA 98837；坐标 47.196874, -119.293090；parcel 090969105、090969104、090969103、090969102、090969109、090969108。来源：Washington Ecology SEPA records 202505050/202600272：https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202505050 、https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202600272
- project scope 补齐：Grant Node Development Binding Site Plan Amendment, Conditional Use Permit, demolition and construction of 60,000 sq ft server farm；City Planning Commission 2026-01-28 agenda 描述为 60,000 +/- sq ft data center/server farm in Heavy Industrial zone, 6 acres at SW corner of Tyndall Road NE and Randolph Road NE。来源：https://www.cityofml.com/AgendaCenter/ViewFile/Agenda/_01282026-937
- owner/applicant 补齐：Keel Infrastructure Corp. 为 Bitfarms successor issuer/ultimate parent；local applicant 在 SEPA register 中列为 Backbone Mining LLC。来源：https://investor.bitfarms.com/news-releases/news-release-details/keel-infrastructure-reports-first-quarter-2026-results 、https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202600272
- latest activity: 2026-08-10 Keel 称已接收 Moses Lake 首批 Vertiv modules，开始执行三处 priority sites 的 final fiber contracts，并已完成 U.S. Bitcoin mining operations decommissioning in preparation for HPC site construction。该证据说明 pre-construction/procurement 正在推进，但不足以单独升级为 `site work-construction`。来源：https://investor.bitfarms.com/news-releases/news-release-details/keel-infrastructure-reports-second-quarter-2026-results
- 多源冲突：未发现实质冲突。地方/州记录确认 permit/SEPA process；公司披露确认 18 MW 和最新推进。行业/劳务 listing 中出现 Turner Construction / Grant Node OneCore Data Center，但非官方或业主来源，未用于提升状态。
- 无法核实/证据不足：未找到 City of Moses Lake CUP final decision/minutes 或 building permit issuance 的可访问官方页面；未找到 utility interconnection/PPA public record for this specific site。本次不标记 construction/energized。
- verified: true（status/capacity/location/owner 均由可访问官方或业主来源支持；construction/energized 未确认）。
