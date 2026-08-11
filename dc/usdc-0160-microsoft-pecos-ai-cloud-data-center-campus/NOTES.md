# USDC-0160 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Microsoft announced the site; no local/state approval or construction-permit record was located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“announced; no local/state approval or construction-permit record located”更新为“local process”。依据是 Microsoft 已于 2026-06-22 正式宣布 Pecos datacenter campus，且相关 Energy Forge One/Project Kilby 发电侧已有 TCEQ、Texas Register、Texas Comptroller JETI、Reeves County ESD 公开流程记录；截至本次刷新，未找到数据中心建筑许可或开工记录。来源：https://blogs.microsoft.com/blog/2026/06/22/powering-the-next-wave-of-ai-expanding-capacity-with-our-new-datacenter-in-pecos/；https://www.tceq.texas.gov/agency/decisions/hearings/events/public-meeting-energy-forge-one-llc-181895-psdtx1684-and-ghgpsdtx260；https://www.sos.state.tx.us/texreg/pdf/backview/0515/0515ia.pdf；https://comptroller.texas.gov/economy/development/prop-tax/jeti/application-details.php?id=J0022；https://rcesd.org/app/uploads/2026/02/RCESD2_Notice-of-Public-Hearing-Energy-Forge-One-2026-03-25.pdf
- capacity_mw 更新：由 null 更新为 2000（Microsoft 2026-06-22 官方博客称 Pecos datacenter campus will expand global datacenter capacity by approximately 2 GW）。来源：https://blogs.microsoft.com/blog/2026/06/22/powering-the-next-wave-of-ai-expanding-capacity-with-our-new-datacenter-in-pecos/
- owner 更新：由 null 更新为 Microsoft Corporation；Chevron 2026-06-22 公告称 Energy Forge One LLC 与 Microsoft 签署 20 年 PPA，为 Microsoft-operated data center 提供 dedicated electricity。来源：https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center
- actions 新增：2025-10-17 TCEQ air permit application submitted；2026-03-25 Reeves County ESD No. 2 tax abatement hearing notice；2026-05-05 Texas Register/TCEQ notice issuance；2026-06-10 TCEQ public meeting；2026-06-22 Microsoft announcement；2026-06-22 Chevron power-agreement announcement；2026-07-24 Texas Comptroller JETI agreement posted。来源同上。
- 多源口径说明：Microsoft 的约 2 GW 是数据中心 capacity；Chevron 的约 2.67 GW 是 Project Kilby 发电 capacity；Reeves County ESD 2026-03-25 notice 中的 1-2 GW 是较早/地方激励流程里的 dedicated-power 范围。三者对应资产和时间点不同，本次不将 2.67 GW 或 1-2 GW 覆盖为数据中心 IT load。
- 未能核实项：未找到 Pecos/Reeves County 数据中心建筑许可、site plan approval、construction start、energization 或 operational go-live 的一手公开记录。
