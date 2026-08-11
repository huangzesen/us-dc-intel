# USDC-0105 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Stalled/on hold; construction was not verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 维持/强化为 stalled/on hold：2026-06-12 Maine Public 报道 Jay Town Manager Shiloh LaFreniere 的说法，Sentinel Data Centers 已通知 JGT2 Redevelopment “at this point” 不继续推进；JGT2 正与其他潜在方沟通，项目当前 on hold，future plans undetermined。未找到 replacement operator、construction start、CO、utility interconnection、energization 或 service 证据。来源：https://www.mainepublic.org/climate/2026-06-12/developer-halts-plans-for-data-center-at-former-jay-paper-mill
- 同一 on-hold 事实由 2026-06-11/06-12 Sun Journal 本地报道交叉确认：报道称 former Androscoggin Mill / Riley Road 方案为 $550M，Sentinel 不打算继续，原 tentative July groundbreaking 不再作为有效施工证据。来源：https://www.sunjournal.com/2026/06/11/plan-for-data-center-in-jay-suffers-setback-2/
- capacity_mw 从 null 更新为 82，但仅作为 proposed initial demand：2026-03-25 Sun Journal 引述 Tony McDonald/JGT2 称 initial demand 约 82 MW，未来扩容取决于 regional grid review；未找到 interconnection/service 记录，因此不是 energized load。来源：https://www.sunjournal.com/2026/03/25/developer-of-data-center-for-jay-mill-seeks-exemption-to-proposed-state-law/
- owner/operator 字段补证：JGT2 Redevelopment LLC 为报道中的 mill owner/developer；Sentinel Data Centers 是 planned operator/partner，但 2026-06 已退出/表示不继续。来源：https://www.mainepublic.org/climate/2026-06-12/developer-halts-plans-for-data-center-at-former-jay-paper-mill
- state-policy 官方背景补证：2026-04-24 Governor Mills 官方 release 记录 veto LD 307，理由包括 bill 未给 Jay former Androscoggin Mill project carveout；同 release 称该项目为 $550M、under contract、received several permits，但未列 permit number。来源：https://www.maine.gov/governor/mills/news/governor-mills-announces-decision-ld-307-2026-04-24
- 2026-04-29 Governor Mills 官方 release 记录签署 executive order 建立 Maine Data Center Advisory Council，且 Legislature sustained LD 307 veto；该政策动作不等同于 Jay 项目批准。来源：https://www.maine.gov/governor/mills/news/governor-mills-signs-executive-order-establish-maine-data-center-advisory-council-2026-04-29
- local process 补证：本地报道称 Jay Select Board 在 2026-03-24 左右支持让 Town Manager 与 JGT2 起草给 Governor Mills 的 exemption/support letter；这只是 support/policy action，不是 site-plan approval。来源：https://www.sunjournal.com/2026/03/25/developer-of-data-center-for-jay-mill-seeks-exemption-to-proposed-state-law/
- 多源 caveat/冲突：Governor release 称项目 had received several permits；但 Sun Journal 同期称开发方认为因利用 existing industrial structure 不需要 Jay Planning Board approval/no zoning changes，本轮未定位 permit list、permit numbers、building permit、utility record 或 CO。该项已写入 data.json contradictions。
- Current tracker check：Cleanview 当前 Maine list 仍列 Jay Androscoggin Mill Data Center 为 82 MW、Expected Year TBD、Developer JGT2 Redevelopment；作为行业 tracker 参考，不优先于 June on-hold local evidence。来源：https://cleanview.co/data-centers/maine
- verified: true（限于本轮结论：on-hold/stalled、proposed 82 MW、JGT2/Sentinel 关系、LD 307 官方政策背景均有可访问来源；permit/utility/construction/energization 仍为未核实项）。
