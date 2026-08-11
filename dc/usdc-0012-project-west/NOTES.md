# USDC-0012 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Announced/under review; the City expressly says the land-developer agreement does not approve or authorize a data center
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 `Announced/under review` 调整为 `local process`。官方记录显示 Norwalk 已批准与 IALCO Warren County Two, LLC 的开发协议，用于准备市界内物业以供潜在未来数据中心开发；但官方同时明确，未来运营方仍需提交 site plans，并遵守地方、州、联邦规则。因此本次不提升到 approved-permitted / construction。来源：
  - City agenda/minutes index（08/06/26 列表仍可访问，03/05/26 Agenda/Minutes 链接在同页）：https://www.norwalk.iowa.gov/government/agenda___minutes.php
  - 2026-03-05 City Council Agenda（列出开发协议 public hearing 与 IALCO Warren County Two, LLC）：https://cms5.revize.com/revize/norwalk/March%205%2C%202026%20Agenda.pdf
  - 2026-03-05 City Council Minutes（Resolution 26059 unanimously carried；未来 operator 需提交 site plans）：https://cms5.revize.com/revize/norwalk/03-05-26%20Minutes.pdf
- 补充早期地方程序证据：2025-01-13 Planning and Zoning minutes 将 proposed Norwalk project 命名为 Project West，约 300 acres，位于 Southwest Development Corridor，并建议通过 Norwalk Technology and Industry Overlay District（25-04，4-0）。来源：https://cms5.revize.com/revize/norwalk/government/boards_commissions_committees/Planning%20Commission/2025/01.13.2025%20P%26Z%20Minutes.pdf
- owner / developer 口径更新：官方会议纪要只确认 IALCO Warren County Two, LLC 是开发协议 counterparty；DCD 2026-03-16 报道称协议对象为 Tract，并称该 282-acre site 位于 Highway 28 以西、Delaware Street 以南。最终数据中心运营方/tenant 仍未由官方确认。来源：https://www.datacenterdynamics.com/en/news/city-council-in-norwalk-iowa-approves-potential-data-center-development-agreement-despite-public-concerns/
- 经济/公用事业口径补证：Norwalk 2026-03-03 官方说明称开发协议提供 400,000 GPD water capacity dedication，市方规划工业 reserve 为 650,000 GPD；称无 local tax incentives，fully built out 情形下预计 city 每年约 $5M property-tax revenue、全部 taxing entities 约 $15M。来源：https://www.norwalk.iowa.gov/news_detail_T5_R273.php
- 2026-07-13 mayor statement 将 Norwalk 西南边缘项目称为 underway，称约 half a billion dollars 注入本地经济、每年 $14M-$16M 新税收分给 city/school district/county，且无 local tax incentives；该声明仍未给出 MW、final operator、building permits 或 construction authorization。来源：https://www.norwalk.iowa.gov/news_detail_T5_R292.php
- capacity_mw：未找到可由官方确认的 MW 容量；保持 null。
- 多源冲突：媒体/trackers 有时写作 “approves data center project/plans”，但官方材料限定为 development agreement / property preparation / future separate approvals。本记录按官方口径保守处理。
- verified: true（对本次写入事实而言；MW 容量与最终 operator 仍未核实）
