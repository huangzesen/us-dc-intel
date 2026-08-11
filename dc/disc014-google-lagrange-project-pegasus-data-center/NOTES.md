# disc014 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-hyperscaler.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 官方补证：Georgia DCA DRI #4797（PRL2）显示提交地方政府为 LaGrange，项目名 PRL2，开发商/申请人为 KDC，当前状态为 “Request for Comments Made”，初始表提交日期 2026-07-22，补充表提交日期 2026-07-24，Request for Comments 日期 2026-07-28，预计流程完成日期 2026-08-27。来源：https://apps.dca.ga.gov/DRI/AppSummary.aspx?driid=4797
- 位置/范围更新：DCA 初始表将 PRL2 定位在 411 Pegasus Parkway（Tax Parcel ID No. 0592000004），描述为现场已有一栋数据中心建筑，后续阶段为约 470,000 sq ft 数据中心建筑；本阶段预计 2029 完成。来源：https://apps.dca.ga.gov/DRI/InitialForm.aspx?driid=4797
- 容量更新：DCA 补充表列出该项目 estimated peak connected electrical load 为 350 MW，能源供应商为 MEAG，水供应商为 City of LaGrange，预计用水 2-4 MGD，污水 0.2-0.6 MGD，估值 $1B，FTE 40-60。`data.json.capacity_mw` 由 null 更新为 350，并标注为官方 PRL2 peak connected load，不等同于已并网 IT load。来源：https://apps.dca.ga.gov/DRI/AdditionalForm.aspx?driid=4797
- 状态更新：原状态 `announced/under construction` 规范化为 `site work-construction`。依据是 Atlanta News First 2026-04-04 报道 LaGrange Fire Department 到 411 Pegasus Parkway 的 Google data center site 救援屋顶施工伤员，DCD 2026-07-27 亦称首栋 building work is ongoing，同时 DCA PRL2 处于 regional review 评论阶段。来源：https://www.atlantanewsfirst.com/2026/04/04/construction-worker-badly-injured-google-data-center-site-lagrange/；https://www.datacenterdynamics.com/en/news/google-files-to-expand-data-center-campus-in-lagrange-georgia/；https://apps.dca.ga.gov/DRI/AppSummary.aspx?driid=4797
- Google 官方核实：Google 数据中心 Georgia 页面列出 2026 年宣布在 LaGrange, Georgia 开发新 data center；该页未给出容量、地址或施工状态细节。来源：https://datacenters.google/locations/georgia/
- 多源冲突/口径差异：容量存在 350 MW、400 MW、50 MW 三种口径。DCA 官方 PRL2 表为 350 MW estimated peak connected electrical load；Cleanview 列 400 MW planned capacity；DCD/Baxtel 记载 Thor 早期第一栋约 50 MW、最终 400 MW 目标。当前采用 350 MW 作为官方可核实容量口径，400 MW 保留为 eventual-campus tracker/media context。来源：https://cleanview.co/data-centers/georgia/2257/project-pegasus-google-lagrange；https://www.datacenterdynamics.com/en/news/google-confirms-plans-for-data-center-in-lagrange-georgia/；https://baxtel.com/data-center/google-project-pegasus
- 多源冲突/口径差异：用地面积存在 270 acres 与 420 acres 两种公开说法。DCD/Baxtel 记载 Thor acquired 270-acre site；AJC/Cleanview 记载 420-acre site。当前在 `data.json.site.acreage_reported` 同时保留，待后续从 property/permit/site-plan 记录厘清 parcel 与 broader campus 边界。来源：https://www.datacenterdynamics.com/en/news/google-confirms-plans-for-data-center-in-lagrange-georgia/；https://www.ajc.com/business/2026/04/what-is-georgias-project-pegasus-tech-giant-unveils-8-billion-answer/；https://cleanview.co/data-centers/georgia/2257/project-pegasus-google-lagrange
- 无法核实/证据不足：未找到可公开确认的已并网日期、IT load、PUE、冷却方案、最终 campus buildout MW、Google 与 KDC/业主之间的完整法律关系，或 PRL2 之外各 phase 的 permit/CO 明细。
