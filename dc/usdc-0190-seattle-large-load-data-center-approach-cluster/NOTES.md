# USDC-0190 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 `no status` / `null` 更新为 `local process / regulatory pause`。Seattle City Council 于 2026-06-09 通过 CB 121214（后为 Ord 127447），对新建、扩建或变更用途为数据中心的申请设置紧急 moratorium；Legistar 记录显示 Mayor 于 2026-06-11 签署。官方页面同时说明该 moratorium 覆盖电力容量超过 20 MVA 且需不间断供电的数据中心。来源：https://council.seattle.gov/2026/06/09/city-council-passes-emergency-data-center-moratorium-and-policy-framework/ ；https://seattle.legistar.com/LegislationDetail.aspx?GUID=86F14A6D-9247-4BB5-839E-0A26937BFD3C&ID=8032163&Options=&Search=
- 2026-06-09，Seattle City Council 同日采用 Resolution 32204，要求/承诺研究数据中心对电网容量和可靠性、水、费率、土地使用、就业/经济和公共健康的影响；Legistar 记录显示 Mayor 于 2026-06-12 签署。来源：https://seattle.legistar.com/LegislationDetail.aspx?GUID=8DD7E93C-942B-4CA0-8931-BB3456ABF8A2&ID=8031795&Options=&Search=
- 2026-07-21，Seattle City Council 通过 CB 121231（后为 Ord 127473）；Legistar 记录显示 Mayor 于 2026-07-22 签署。该条例建立 City Light 新零售费率表，并为用电需求构成 new large load 的数据中心建立新客户类别和服务条件。来源：https://seattle.legistar.com/LegislationDetail.aspx?G=FFE3B678-CEF6-4197-84AC-5204EA4CFC0C&GUID=D3BD92B3-29A0-476F-A287-416888D43E7E&ID=8071043&Options=&Search= ；https://seattle.legistar.com/MeetingDetail.aspx?G=FFE3B678-CEF6-4197-84AC-5204EA4CFC0C&GUID=E0BD2B85-68E0-4FC5-A21B-322D798FF44B&ID=1429315&Options=&Search=
- City Light 于 2026-06-12 发布 New Large Data Center Load Policy 说明：新建或扩建且电力服务请求达到 10 MVA 以上的数据中心将进入新费率类别，采用成本基础费率、客户承担基础设施和相关成本、服务队列和需求响应要求；该政策适用于 City Light 全服务区，包括 Seattle 市外部分 King County/邻近城市服务区。来源：https://powerlines.seattle.gov/2026/06/12/getting-ahead-of-data-center-power-demands/
- capacity 更新：`capacity_mw` 从 `null` 更新为 `249`，但这是“当前媒体报道仍活跃的请求容量”，不是官方 permit/energization 容量。官方 Seattle Council/City Light 材料确认原始 approach cluster 是四家公司、五个大型数据中心、合计最大需求 369 MW。Seattle Times 转引/地方报道称一名未具名开发商退出，Sabey 随后撤回其 Tukwila campus 68 MW 请求，剩余 Equinix 和 Prologis 的三个提案合计 249 MW。来源（官方 369 MW）：https://council.seattle.gov/2026/04/30/councilmembers-introducing-moratorium-on-data-centers-in-seattle/ ；https://council.seattle.gov/2026/06/09/city-council-passes-emergency-data-center-moratorium-and-policy-framework/ 。来源（249 MW/退出/主体）：https://www.govtech.com/products/data-center-developers-pull-seattle-plans-amid-opposition ；https://www.spokesman.com/stories/2026/may/01/2-data-center-developers-pull-seattle-plans-amid-o/ ；https://www.everettpost.com/state-news/new-seattle-data-centers-could-spike-electric-rates/
- owner 更新：`owner` 从 `null` 更新为媒体报道仍活跃的 `Equinix` 与 `Prologis`。Sabey 和一名未具名开发商列入 history/contradictions 为已退出；未在可访问官方 city 记录中找到各家公司与项目地址的正式申请记录。
- 冲突/限制：官方记录确认 369 MW 原始合计与政策动作，但未命名所有开发商、未给出项目地址、未确认 249 MW 当前活跃容量；部分行业转述出现 389 MW，低于官方/地方来源优先级，本次保留官方 369 MW。未核实到项目级 land-use approval、building permit、construction start、utility interconnection/energization、commissioning 或 operating evidence。
- verified: false。原因：政策/监管状态有官方证据；但 active-proposer 身份、Sabey 68 MW 退出、剩余 249 MW、具体 site/parcel 均依赖媒体/二级来源，尚未由可访问的官方 permit/service record 证实。
