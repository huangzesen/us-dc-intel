# USDC-0140 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Google's official location page confirms an operating The Dalles campus and continued regional investment
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“官方页面确认运营校园、未能证实扩建施工/投运”更新为“site work-construction / operating legacy campus”。依据：City of The Dalles 现行 Google Data Centers 页面称 Google 自 2006 年起在 The Dalles 运营数据中心，四栋楼分布在两个站点，第三个站点增加两栋楼；同页称 2025 年 former smelter site redevelopment 相关新 water/sewer infrastructure 已完工并转归市政府所有。来源：https://www.thedalles.gov/business/google_data_centers/index.php
- 新增 local-government 施工状态证据：2024-12-09 City Council minutes 中，Public Works Director 将 SIP 资金描述为 Google 新数据中心开发协议的一部分，并称 new data centers under construction；同段说明相关资金用于 water-system financials，不能等同于 building permit/CO/energization。来源：https://ormswd2.synergydcs.com/HPRMWebDrawer/Record/6866871/File/document
- 新增 SIP 收入治理证据：City of The Dalles EZ/SIP 页面称 2021 SIP agreement with Design, LLC 覆盖 up to two data centers receiving tax abatement for up to 15 years；2024-12-16 minutes 记录 Resolution 24-030 以 5-0 通过，用于 2021 SIP Agreement with Design, LLC 的税收/收入预算政策。来源：https://www.thedalles.gov/business/google_data_centers/ezandsipagreements.php 与 https://ormswd2.synergydcs.com/HPRMWebDrawer/Record/6866871/File/document
- 新增水基础设施事实：Google 于 2025-10-22 宣布与 City of The Dalles 完成 ASR system，并永久转让 ASR system 与 associated groundwater rights，称可为社区每年增加 over 100 million gallons；市政府水基础设施页面也称 Google 完成并转让两口 wells、two reservoirs、pump station、sanitary sewer lift station 等合计 $28.5M public infrastructure，并称 Google pays full water rates。来源：https://blog.google/company-news/outreach-and-initiatives/sustainability/the-dalles-oregon-water/ 与 https://www.thedalles.gov/business/google_data_centers/google_water_infrastructure_contributions.php
- 新增电力侧支持事实：Avangrid 于 2025-07-22 宣布与 Google 签署 Leaning Juniper IIB repower PPA，more than 100 MW 将支持 Google 在 The Dalles 的数据中心，Northern Wasco County PUD 将 deliver power；该数值作为 power supply/PPA 记录，不写入 capacity_mw。来源：https://www.avangrid.com/w/avangrid-announces-119-megawatt-repower-project-in-oregon
- URL 替换（2026-08-11）：上条 Avangrid 原始 URL（avangrid.com）在复核时返回 status 000（HTTP/2 INTERNAL_ERROR，HTTP/1.1 超时，且 avangrid.com 根页也无法访问），不是 404/403。已以 datacenterdynamics.com 的同一事实报道（验证可访问，HTTP 200）替换：https://www.datacenterdynamics.com/en/news/google-signs-ppa-with-avangrid-for-more-than-100mw-of-wind-energy-in-oregon/ 。data.json 中 actions 与 sources 已更新，原始 URL 保留于 history 与此备注。
- 新增当前 utility context：City of The Dalles 2026-08-10 seasonal water supply update 显示 city water system normal、no water restrictions、water demand within expected seasonal ranges、groundwater wells operating normally；该信息仅说明城市水系统状态，不证明 Google 扩建投运或容量。来源：https://www.thedalles.gov/news_detail_T4_R275.php
- capacity_mw 保持 null：未找到公开可信的 IT capacity MW、building-specific energization、certificate of occupancy 或 commissioning date。Avangrid >100 MW 是 PPA/energy supply support，不等同 IT load capacity。
- owner 更新：从 null 更新为 Google LLC / Alphabet subsidiaries，并注明 Design, LLC、Moraine Industries LLC 为 SIP/Alphabet 结构中出现的实体。来源：Oregon SIP records 与 City of The Dalles EZ/SIP 页面。
- 多源冲突：未发现直接冲突；主要限制是 public sources 对“第三站点两栋楼”未给出 building-level permit/CO/live-load 日期，Google PUE 表只列 The Dalles 和 The Dalles (2nd facility)，无法映射到第三站点。
- verified: true for refreshed public-source claims; verified: false for IT capacity, building-specific commissioning, and exact phase-to-tax-lot mapping because public evidence remains insufficient.
