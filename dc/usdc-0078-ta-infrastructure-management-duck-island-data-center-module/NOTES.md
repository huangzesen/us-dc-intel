# USDC-0078 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Pilot land-use application; later installation, operation, and construction completion were not verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 application-only 改为 approved-permitted temporary pilot；另记录 Petroleum News 对 AOGCC 2025-03-13 决定的报道称模块已安装但尚未接电。未找到后续 energized / partial live / full buildout 证据。来源：https://www.petroleumnews.com/story/2025/01/05/news/state-oks-sdi-data-center-land-use-permit/40541.html ，https://www.petroleumnews.com/story/2025/03/23/news/aogcc-approves-hilcorp-non-custody-transfer-meter-for-pilot/40674.html
- capacity_mw 更新：官方 Alaska DNR public notice 与申请附件均说明模块包含 1.4 MW bitcoin mining computers；这是计算负载/模块规模，不是大型 AI campus。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=217467 ，https://aws.state.ak.us/OnlinePublicNotices/Notices/Attachment.aspx?id=151373
- owner 更新：TA Infrastructure Management LLC 为 land-use permit applicant/developer；Hilcorp Alaska LLC 为现有发电设备所有方和 Duck Island/Endicott 场地方。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=217467 ，https://www.northernjournal.com/arctic-bitcoin-hilcorp-tech-firm-aim-to-test-north-slope-data-center/
- permit/metering 补证：Petroleum News 2025-01-05 报道 Alaska DNR Division of Oil and Gas 的 2024-12-19 permit approval；2025-03-23 报道 AOGCC 条件批准 Hilcorp 对第三方 data-center pilot 使用 non-custody transfer meters，且若超过 5 年需升级至 custody-transfer standards。来源：https://www.petroleumnews.com/story/2025/01/05/news/state-oks-sdi-data-center-land-use-permit/40541.html ，https://www.petroleumnews.com/story/2025/03/23/news/aogcc-approves-hilcorp-non-custody-transfer-meter-for-pilot/40674.html
- 无法核实项：未在公开索引中检索到 DNR 2024-12-19 approval letter 原文或 AOGCC 2025-03-13 order 原文；AOGCC 数据页说明 orders/document images 为公开数据服务，但具体文档检索入口在本次刷新中触发浏览器挑战。来源：https://www.commerce.alaska.gov/web/aogcc/data.aspx
- 多源冲突：未发现；各来源均指向小型、临时、bitcoin-mining pilot，而非 hyperscale/AI data center。
