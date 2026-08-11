# USDC-0108 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Early/incomplete proposal; no construction
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “Early/incomplete proposal; no construction” 细化为 “Local process / moratorium; no construction”。官方 Scarborough 临时数据中心 moratorium 条文显示，moratorium 适用于 2026-04-01 当日或之后提交的任何数据中心申请，并在有效期内禁止镇方接受、处理或行动于数据中心相关审批；条文称通过后立即生效、期限 180 天。来源：https://scarboroughmaine.community.diligentoneplatform.com/document/686e0a56-2a49-42e2-baa3-3cfd924b870d/
- 官方会议记录入口补证：Scarborough Diligent portal 显示 2026-06-03 Town Council Regular Meeting，并关联公开议程文档；该页面可作为 June 3 council meeting context，但未在可见 HTML 中给出 roll call。来源：https://scarboroughmaine.community.diligentoneplatform.com/Portal/MeetingInformation.aspx?Id=405
- 地方媒体补证：WGME 2026-06-03/2026-06-04 报道称 Town Council 于 2026-06-03 通过 data center moratorium，moratorium 为 180 天、立即生效，并 retroactively applies to proposals submitted on or after 2026-04-01；同篇称 Scarborough Technology Park 为 Daniel Dickinson 提交的 52-acre、140,000 sq ft data-center plan，且 town officials said the April proposal was incomplete/rejected. 来源：https://wgme.com/news/local/scarborough-town-council-to-vote-on-proposed-data-center-moratorium
- 项目细节补证：Maine Public 2026-05-06 报道称 Daniel Dickinson 于 2026-04 提交 Scarborough High Technology Industrial Park master-plan application，包含 two-story data-processing building、natural gas-fed solid oxide fuel cells、closed-loop water cooling，位置为 Maine Turnpike 以西约 52 acres；同篇称 Scarborough planning office late April rejected application as incomplete，缺少 aquifer/historic-site、utility service、noise/odor/traffic 等材料。来源：https://www.mainepublic.org/climate/2026-05-06/scarborough-considers-data-center-pause-after-development-proposal
- Portland Press Herald 2026-05-28 报道确认：Town Council was scheduled to vote on 2026-06-03; moratorium would retroactively apply to applications on or after 2026-04-01; developer Daniel Dickinson submitted the April 20 master plan, and local officials rejected it as incomplete. 来源：https://www.pressherald.com/2026/05/28/scarborough-to-vote-on-data-center-moratorium/
- capacity_mw 仍为 null：公开来源只给出 140,000 sq ft building / 52-acre site / fuel-cell and cooling concept，没有可核实 MW load 或 IT capacity。
- owner 从 null 更新为 reported developer/landowner Daniel Dickinson；未核实到 data-center operator/tenant 或最终项目公司。
- 多源冲突：未发现实质冲突。此前 “incomplete” vs “rejected as incomplete” 语言差异保留为同一事实链；官方可见文件未给出 roll call。
