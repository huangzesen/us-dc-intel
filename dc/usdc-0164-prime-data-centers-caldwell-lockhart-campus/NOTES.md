# USDC-0164 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: TDLR registered two new shell buildings for future data-center use; no county/city approval or completed construction record was located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 `approved-permitted / development`：Caldwell County 官方材料确认 2024-03-12 通过 Prime Data Centers, LLC Reinvestment Zone #1（Order 06-2024），并在 2026-04-23 以 4 Ayes / 1 Oppose 批准 Lockhart Property, LLC 205.756 acres Development Agreement；TDLR 在 2026-05-05 注册 Prime Data Center AUS-01（TABS2026019473），但未找到官方 construction-start inspection、building permit、CO、utility energization 或 live-service 记录。来源：https://www.co.caldwell.tx.us/upload/page/0068/3.12.24%20Special%20Agenda%20Packet.pdf ; https://www.co.caldwell.tx.us/upload/page/0252/docs/Minutes/4.23.26%20Sealed%20Minutes.pdf ; https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026019473
- location/owner 补强：TDLR 记录列出 1395 Bob White Road, Lockhart, TX 78644，owner 为 Lockhart Property, LLC；Caldwell County highlights 将 Prime zone 描述为 FM 2720 at Bob White Road。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026019473 ; https://www.co.caldwell.tx.us/page/cc.highlights
- capacity_mw 从 null 更新为 384，标注为 owner/developer-reported planned critical IT load：Prime 当前 Austin AUS01 页面称 Lockhart campus 将交付 384MW critical across eight hyperscale data centers；AUS01 tech sheet称 205 acres、8 facilities、384MW critical IT load、2,000,000 sq ft、Bluebonnet Electric Cooperative、on-site substation、status Development。来源：https://primedatacenters.com/locations/austin/ ; https://primedatacenters.com/wp-content/uploads/2025/10/PDC_Austin_TechSheet_AUS01_01.pdf
- 记录冲突/口径差异：TDLR TABS2026019473 是两栋 380,000 sf shell buildings、总 760,000 sf、1395 Bob White Road；Prime AUS01 campus 是 3300 FM 2720、8 facilities、2,000,000 sf、384MW。当前判断为 building-level record 与 campus-level marketing/tech-sheet 口径差异，尚无法官方逐栋映射。
- 记录状态 caveat：Caldwell County highlights 使用 “constructing a turn-key data center campus” 表述，但会议纪要、TDLR 和县公告未提供开工检查、建筑许可、CO、并网或投运证据，因此未提升到 `site work-construction`。来源：https://www.co.caldwell.tx.us/page/cc.highlights ; https://www.co.caldwell.tx.us/page/article/1239 ; https://www.co.caldwell.tx.us/upload/page/0206/5.14.26%20Signed%20Resolution%2029-2026%20Regarding%20Est.%20of%20Addtl.%20Data%20Centers%20in%20Tx.pdf
- 行业媒体交叉核验：Data Center Dynamics 2026-05-13 报道 Prime filed with TDLR for two Lockhart buildings, each 380,000 sq ft, $400M investment, June 2026 start / September 2027 completion, and notes Prime had not officially announced the development at that time。来源：https://www.datacenterdynamics.com/en/news/prime-files-to-build-two-data-centers-outside-austin-texas/
