# disc026 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-secondary-markets.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 状态从 `planned; potential moratorium under city discussion` 细化为 `local process; proposed project with Prichard data-center moratorium public hearing scheduled`。WALA 报道 2026-07-23 Prichard City Council 讨论了针对新数据中心 permit 的临时 moratorium，Council President Traci Hale 提出 resolution，moratorium 将持续 480 天且可续期；截至该报道，Council 尚未投票，可能在下一周投票。来源：https://www.fox10tv.com/2026/07/24/prichard-city-council-considers-moratorium-data-centers/
- Lagniappe 于 2026-07-30 报道，moratorium 表决因一则“已有实体提交数据中心申请”的信息而中断；Council 随后投票决定就 proposed moratorium 在 2026-08-13 举行 public hearing。该报道同时称 Edged 已数月争取在 Prichard 建设约 $93M 数据中心，但未能确认该申请是否由 Edged 提交。来源：https://www.lagniappemobile.com/news/prichard/vote-on-prichard-data-center-falls-apart/article_4211104f-b442-495e-a691-160fd5a65b84.html
- 项目 sponsor 站点确认 Project Gateway 是 Edged US 正在评估的 Prichard proposed data center campus，拟建 8MW、57,000 SF 建筑，包含 data hall 和小型办公室；披露约 $93M private investment、150-200 construction jobs、20 permanent full-time positions、约 18 个月建设期、closed-loop waterless cooling，以及“project details remain subject to permitting, infrastructure availability, customer requirements, and regulatory approvals”。来源：https://projectgatewayal.com/
- DCD 于 2026-08-10 报道该项目位于 214 Telegraph Road、near Africatown，计划约 $93M、约 8MW，场址此前为 911 data center，若获准可最早在 2026 年底破土；DCD 也将其描述为 primarily networking hub，supporting internet and communications infrastructure。来源：https://www.datacenterdynamics.com/en/news/alabama-city-considers-data-center-moratorium-could-kill-edged-project/
- MEJAC 2026-05-26 社区记录提供了 local context：拟议地址为 214 Telegraph Road, Prichard, AL 36610，parcel 多数位于 Prichard、约 11% 位于 City of Mobile；其记录称 Mobile 一侧为 R-1 Single-Family Residential，Data Processing/Hosting/Data Centers 并非允许用途，但若 Edged 将 footprint 保持在 Prichard 境内，该 Mobile 侧限制可能不适用。来源：https://www.mejacoalition.org/2026/05/26/africatown-data-center/
- 多源冲突：capacity_mw 暂保留 8MW，因为 sponsor 当前项目站点和 2026-08-10 DCD 报道均为 8MW；MEJAC 2026-05-26 记录基于较早社区讨论称 proposed Prichard operation 只需 6MW。该差异已写入 data.json 的 contradictions。
- 官方/地方政府核实情况：Alabama Department of Revenue 官方页面确认 Mobile County appraisal/assessment records 的 official portal 为 Mobile County Citizen Access Portal（https://mobile.capturecama.com/），但本轮未能通过可抓取页面直接核实 214 Telegraph Road 的 parcel 记录；Prichard 官方站点在本轮抓取中呈现疑似被劫持/污染内容，未作为项目事实来源。来源：https://www.revenue.alabama.gov/property-tax/county-offices-appraisal-assessment-records/
- 证据不足/待核实：未找到可访问的一手 City of Prichard agenda/minutes、permit application、site plan、zoning determination 或 utility interconnection/service record；无法确认 2026-07-30 报道中的“已提交申请”是否即 Edged/Project Gateway。
