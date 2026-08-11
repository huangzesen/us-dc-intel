# USDC-0077 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Proposed and in preliminary state-lease review; construction, final lease, and operating status were not verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 local process / preliminary state-lease review：Alaska DNR Division of Oil and Gas 于 2026-05-12 对 ADL 422741 作出 Preliminary Decision，拟向 STAK Energy Corporation 提供 50-year negotiated lease；该记录是 preliminary decision，不是 Final Finding and Decision、executed lease、entry authorization、construction permit 或运营证明。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=223817
- 官方位置/范围补证：DNR notice 称拟租赁 715.4 acres，位于 Dalton Highway 附近、约 Deadhorse 以南 26 miles；DNR Preliminary Decision PDF 进一步描述为 Dalton Highway Milepost 390 以西约 1 mile。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=223817；https://aws.state.ak.us/OnlinePublicNotices/Notices/Attachment.aspx?id=161957
- 公示时间线更新：DNR 于 2026-06-17 因 significant public interest 延长 public comment period，评论截止从原 2026-06-15 延至 2026-07-17 4:30 PM AKDT。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=224224
- capacity_mw 从 null 更新为 1000，标注为 proposed/official-record figure：DNR public-record revised application/development plan（rev. 2026-03-12）称 on-site natural gas generation system will provide approximately 1 GW；同一官方记录中的 Preliminary Decision 又描述 gas-fired generation system designed to produce 1-3 GW，因此 1000 MW 仅作 best-supported proposed initial/plan figure，不代表 operating capacity。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/Attachment.aspx?id=162057；https://aws.state.ak.us/OnlinePublicNotices/Notices/Attachment.aspx?id=161957
- owner 从 null 更新为 STAK Energy Corporation，依据 DNR ADL 422741 notice。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=223817
- proposed footprint/detail 补证：DNR Preliminary Decision 描述约 640-acre gravel pad、1.8-mile gravel access road、约 7.1 million cubic yards gravel fill、behind-the-meter on-site consumption，pipeline component 不在当前 lease application 内且需 separate application/public process。来源：https://aws.state.ak.us/OnlinePublicNotices/Notices/Attachment.aspx?id=161957
- 未核实项：未找到 Final Finding and Decision、最终 lease issuance、DOT access-road permit、ADEC PSD/air permit、USACE Section 404 authorization、pipeline right-of-way authorization、construction start、energization 或 operations 的官方证据。
