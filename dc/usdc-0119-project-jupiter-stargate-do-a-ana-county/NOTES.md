# USDC-0119 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Project Jupiter remains a proposed/under-review project with unresolved scope and status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 `local process / under regulatory hearing`。NMED public notices 当前列出 Yucca Growth Infrastructure, LLC - YGI Microgrid (Project Jupiter) NSR application received 2026-04-27、Completion Letter 5.27.2026、Application 10883 revisions、2026-07-29 draft permit materials、modeling review report、以及 2026-09-14 amended hearing notice；这些均不是 final air permit。来源：https://www.env.nm.gov/public-notices/
- NMED OPF docket 确认为 `AQB 26-57(P): Yucca Growth Infrastructure, LLC - YGI Microgrid (Project Jupiter)`，但 docket 页面正文为 lazy-loaded 标题层，具体命令/材料仍需逐 PDF/短链核实。来源：https://www.env.nm.gov/opf/docketed-matters/
- 2026-07-16 NMED scheduling order 曾设置 2026-10-19 public hearing、2026-10-01 technical testimony deadline、2026-10-12 rebuttal deadline；NMED public notices 后续列出 `Amended Notice of Hearing-9.14.2026_English`，因此 hearing date 记录为冲突/可能已改期。来源：https://www.env.nm.gov/opf/wp-content/uploads/sites/13/2026/07/2026-07-16-AQB-26-57-Scheduling-Order-filed.pdf 与 https://www.env.nm.gov/public-notices/
- 2026-08-05 NMED hearing officer order 要求各方在 2026-08-11 前回应 New Energy Economy 的 dismiss/continue motion，并要求 YGI/NMED 说明是否存在可合法取得的约 400 MMcf/d gas supply、是否 appeal State Land Office denial、是否有 alternative pipeline/fuel route、Application 10883 是否仍可按 proposed 构建、以及是否能在 reasonable time 完成。来源：https://www.env.nm.gov/opf/wp-content/uploads/sites/13/2026/07/2026-08-04-AQB-26-57-Order-Briefing-Dismissal-filed.pdf
- 相关 pipeline：BLM ePlanning 的 Green Chile Natural Gas Pipeline 页面列出 NEPA status completed、NEPA completion/FONSI 2026-04-27、decision date 2026-05-01、applicant Transwestern Pipeline Company, LLC、约 16 miles 24-inch buried natural-gas pipeline across BLM-administered public lands、La Mesa / Doña Ana County。此为 related fuel infrastructure，不等同于 data-center campus approval。来源：https://eplanning.blm.gov/Project-Home/?id=97AD7851-F93F-F111-88B3-001DD802F839
- 相关 pipeline 冲突仍在：New Mexico State Land Office 2026-07-15 press release 与 2026-07-14 letter 再次拒绝 Energy Transfer 对两个 ROW 与一个 business lease 的 reconsideration，涉及 Project Jupiter pipeline 的 state trust land segment；NMED 2026-08-05 order 也把该 denial 作为燃气供给/constructibility 问题。来源：https://www.nmstatelands.org/2026/07/15/commissioner-garcia-richard-again-denies-request-to-run-portion-of-project-jupiter-pipeline-through-state-lands/ 与 https://www.nmstatelands.org/wp-content/uploads/2026/07/2026-07-14-Letter-re-Informal-Request-for-Reconsideration_Final.pdf
- capacity_mw 保持 `null`：官方材料可确认的是 pending air-permit/microgrid 与 pipeline fuel-supply records；未找到 final data-center IT capacity、energized load、CO、commissioning 或 county building/site permit。
- owner 更新为 evidence-qualified：Yucca Growth Infrastructure, LLC 是当前 NMED Air Quality Construction Permit Application 10883 applicant；ultimate data-center owner/tenant 未在官方地方政府记录中独立确认。
- verified: true for listed official/public-source facts; verified: false for final permit/construction/energization/capacity because no confirming record was located.
