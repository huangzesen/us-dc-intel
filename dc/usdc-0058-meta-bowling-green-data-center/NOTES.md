# USDC-0058 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `site work-construction`。依据：Meta 已于 2025-04-09 正式宣布 Bowling Green Data Center；Middleton Township/Meta 2026 项目信息称现场有 significant activity；OPSB 2026-02-03 公告称 Liames 正在建设 adjacent data center campus；Middleton Township 2026-07-07 分区听证记录显示 Liames 地块已有建筑物被拆除且仍在处理数据中心相关分区事项。
- owner: `null` -> `Meta Platforms, Inc. / Liames, LLC`。Meta 官方宣布该项目为 Meta-owned and operated data center；OPSB 公告称 Liames, LLC 将消纳 Apollo Power Generation Facility 的电力且 Liames 正在建设相邻 data center campus。
- capacity_mw: `null` -> `180`，但标记为需继续核实。Ryan Grissinger tracker 将 180 MW 标为 peak IT demand / Meta-stated；本次检索到的 Meta 官方公告只确认 715,000 sq ft，OPSB 只确认相邻 Apollo 350 MW gas + ~120 MW BESS，不等同于数据中心 IT 容量。
- location 增补：Middleton Township, Wood County；相邻 Apollo 设施位于 Mercer Road 与 Middleton Pike / SR 582 附近。Meta 官方公告只给出 Middleton Township；OPSB 公告提供相邻电源设施交叉口。
- 新增 milestone：
  - 2025-04-09: Meta company announcement，715,000 sq ft、>$800M、约 100 个运营岗位、峰值建设工人超 1,000。Source: https://datacenters.atmeta.com/2025/04/hello-bowling-green/
  - 2026-01-08: Middleton Township 发布 Meta 给 trustees 的项目信息信，涵盖 water/energy/air/construction/jobs。Source: https://www.middletontownship.com/bowling-green-data-center-project-and-community-impact-information/ ; PDF: https://www.middletontownship.com/wp-content/uploads/2026/01/Meta-Middleton-Township-Letter-010726.pdf
  - 2026-02-03: OPSB 批准 Apollo Power Generation Facility，350 MW behind-the-meter natural gas generation + ~120 MW BESS，服务 adjacent Liames data center campus。Source: https://content.govdelivery.com/accounts/OHPUC/bulletins/4077fa5
  - 2026-07-07: Middleton Township Trustees 批准 Liames Application 2026041，将 13 个地块由 A-1/R-4 改为 M-1 Light Industrial；记录同时说明 WCPC 2026-06-02 推荐批准、MTZC 2026-06-10 建议否决。Source: https://www.middletontownship.com/wp-content/uploads/2026/07/07072026_specialrezoning.pdf
- 补充来源：
  - Williams Apollo project page lists OPSB filings and project timeline categories for Apollo Power Generation / pipelines / laydown yard. Source: https://www.williams.com/expansion-project/apollo-power-generation-project/
  - Third-party tracker for 180 MW / expected July 2027 / phase 4: https://ryangrissinger.com/issues/data-centers/OH-DC-0049
- 冲突/注意：
  - Middleton Township 文章写 Meta 于 2026-01-07 提交信，但 PDF 文本显示 "January 7, 2025"，且信内引用 2025-04-09 之后的公告；本次按 township 2026-01-08 发布上下文处理为 PDF 日期笔误。
  - `capacity_mw=180` 不是本次找到的官方 Meta/OPSB 直接字段；保留为第三方 tracker 报告值。不要把 Apollo 350 MW 发电容量误写成数据中心 IT load。
  - Apollo power/gas/air permit chain 与数据中心本体不同：OPSB 350 MW approval 说明 data center 的 power-readiness，但不代表数据中心已 energized 或 operational。
- 无法核实/证据不足：
  - 未找到 Meta 官方披露的 IT MW、正式投运日期或 phased energization 日期。
  - 未核验 Ohio EPA final PTI/PTIO、Title V application、Apollo North/South pipeline dockets 的完整原始 docket 内容；PUCO/DIS case pages通过浏览器返回 request rejected。
- verified: true for owner/location/status progression and official/local milestones above; verified: false for official IT capacity and official in-service date.
- evidence_grade 由 `A-` 细化为 `A- for status/location/owner and official/local-process milestones; B for capacity_mw`：180 MW 仅来自第三方 tracker（https://ryangrissinger.com/issues/data-centers/OH-DC-0049 ）转述的 Meta-stated peak IT demand，官方 Meta 公告（https://datacenters.atmeta.com/2025/04/hello-bowling-green/ ）与 OPSB 记录（https://content.govdelivery.com/accounts/OHPUC/bulletins/4077fa5 ）均未发布数据中心 IT-load，故容量维度保留为需继续核实的 tracker 值（verified: false）并降级为 B；其余字段证据级别不变。
