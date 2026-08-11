# USDC-0150 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Reported by AP as a separate Crusoe/Microsoft expansion; no government approval or permit tying the two buildings and onsite plant to this project was found
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“仅 AP 报道、未找到政府许可关联”提升为 `site work-construction`。依据：Abilene 市政府公开的已执行税收减免清单列出 Resolution No. 249-2025、Phase 9、Phase 10 与 Abilene DC TPP electricity generation plant 协议；Resolution No. 249-2025 显示市议会已于 2025-12-04 批准 Lancium LLC / Abilene DC 9 LLC / Abilene DC 10 LLC / Abilene DC TPP LLC 对应的税收减免协议。来源：https://abilenetx.gov/2476/Tax-Abatements；https://www.abilenetx.gov/DocumentCenter/View/39460/Resolution-No-249-2025-Approving-a-Tax-Abatement-Agreement--Second-Abatement-Agreements-Lancium-Phases-9-10-Plant-PDF
- 公司公告补证：Crusoe 于 2026-03-27 宣布在 Abilene 建设 Microsoft 专用 900 MW AI factory campus，位于既有 Abilene AI factory infrastructure 相邻位置，包含 two new buildings 与 onsite power plant；公告称 land clearing and site preparation 已经 underway，第一栋楼预计 mid-2027 energized。来源：https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- capacity 更新：`capacity_mw` 记为 900 MW（Crusoe 公告的新 campus/onsite power generation 规模）。同一公告还披露两个新楼各 336 MW critical IT load，合计 672 MW IT load；全 Abilene site projected capacity 为 2.1 GW。来源：https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- owner/operator 更新：公开材料支持 Crusoe 为 developer/operator，Microsoft 为 announced customer/tenant；Abilene 市政府协议主体为 Lancium LLC、Abilene DC 9 LLC、Abilene DC 10 LLC、Abilene DC TPP LLC。来源：https://abilenetx.gov/2476/Tax-Abatements；https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- 第三方/媒体交叉验证：AP 2026-03-27 报道 Microsoft 接手 OpenAI 未继续推进的 Abilene expansion，项目为两个 AI factory buildings 与 onsite power plant，全部 Abilene building count 预计达到 10，总 computing capacity 约 2.1 GW。来源：https://apnews.com/article/ai-stargate-microsoft-openai-crusoe-oracle-f4f74c3a4617d8cfab5b933fc31ccc6e
- 多源冲突/口径差异：Crusoe 对新 campus 使用 900 MW site / 900 MW onsite generation 口径，同时给出两个楼各 336 MW critical IT load；AP 使用全园区 2.1 GW computing capacity 口径。本次 `capacity_mw` 采用新 campus 公告口径 900 MW，并在 data.json contradictions 中保留口径差异。
- 无法核实/证据不足：本次未找到可直接下载核验的 building permit/site plan，未能把 Phase 9/10/TPP 协议逐项映射到 Microsoft 两栋楼的具体地址、地块号、建筑面积或施工许可证号；状态中的 site prep/construction 仍主要来自 Crusoe 公司公告。
