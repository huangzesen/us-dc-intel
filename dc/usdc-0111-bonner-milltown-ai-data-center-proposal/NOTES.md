# USDC-0111 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Missoula County announced interim zoning to pause new or expanded data centers outside city limits, and the county’s public information page records the July 9 hearing/action context
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“county interim-zoning pause / withdrawal reported”改为“inactive / withdrawn”。Missoula County 的 Bonner Data Center 项目页记录，Mike Heisey（拟使用建筑的业主）已从 Krambu special exception application 中撤回签名，并且 County 明确写明 “This development means the project will not move forward.” 来源：https://missoulacountyvoice.com/bonner-data-center
- location 补证：官方项目页将拟议项目地址列为 9314 Bonner Miller Road，并说明其位于原 mill / planer building，property zoned Industrial Center, Heavy。来源：https://missoulacountyvoice.com/bonner-data-center
- capacity_mw 补证：官方项目页列出 initial phase 约 7 MW，未来可能扩至 29 MW（site currently available capacity estimate）。本次将其记录为 withdrawn proposal capacity，非批准/在建容量。来源：https://missoulacountyvoice.com/bonner-data-center
- local-process timeline 补证：County 项目页列出 2026-03-25、2026-04-28、2026-05-11、2026-06-01 多轮 special exception application / sufficiency review，最终第五版仍为 “deemed incomplete”，Expected hearing postponed until further notice。来源：https://missoulacountyvoice.com/bonner-data-center
- moratorium 保持并补强：County Data Center Interim Zoning 页面 2026-07-10 更新称 commissioners 于 2026-07-09 voted to establish a moratorium on permitting new or expanded data centers outside city limits，effective 2026-07-09 through 2027-07-08 or replacement zoning。来源：https://missoulacountyvoice.com/data-center-interim-zoning
- withdrawal date：官方 Bonner 项目页未在可见文本中给 withdrawal update 标明日期；Montana Free Press 与 Missoula Current 均在 2026-07-06 报道 property owner / application withdrawal，本次用 2026-07-06 作为 action date，并在 data.json access_caveat 标明该日期来自 local reporting。来源：https://montanafreepress.org/2026/07/06/property-owner-of-proposed-bonner-data-center-backs-out/ 与 https://missoulacurrent.com/bonnder-data-center/
- conflict / caveat：capacity 存在口径差异。官方 County 项目页为 7 MW initial / 29 MW potential site capacity；Montana Free Press 2026-05-21 报道 application 提及 full buildout 可能随最终可用电力与市场需求 ramp up to 100 MW。本次以官方 7/29 MW 作为可核实 proposal capacity，将 100 MW 视为 applicant/projected tail，不作为批准容量。来源：https://missoulacountyvoice.com/bonner-data-center 与 https://montanafreepress.org/2026/05/21/missoula-panel-highlights-data-center-concerns/
- evidence limits：未找到 final land-use approval、zoning compliance permit、building permit、construction start、energization 或公开 utility interconnection approval；status 不应标为 approved-permitted / construction / energized。
- verified: true（核心状态、地址、7/29 MW 容量、local-process posture 与 moratorium 均有官方 county source；withdrawal 日期由 2026-07-06 local reporting 补足，已在 data.json 中标注 caveat）。
