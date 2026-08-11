# disc005 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-grid-queue.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 官方 TDLR TABS 记录确认 Amazon Data Services, Inc. 在 6000 TX-18, Fort Stockton, TX 79735 注册 Pecos County Data Center 三栋新建数据中心楼：
  - Building A：TABS2026026954，注册日期 2026-08-04，Current Status 为 Project Registered，计划 2026-08-01 开工、2026-12-01 完成，189,060 ft2，估算成本 300,000,000 美元。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026026954
  - Building B：TABS2026026955，注册日期 2026-08-04，Current Status 为 Project Registered，计划 2026-08-01 开工、2026-12-01 完成，189,060 ft2，估算成本 300,000,000 美元。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026026955
  - Building C：TABS2026026959，注册日期 2026-08-04，Current Status 为 Project Registered，计划 2026-08-01 开工、2026-12-01 完成，189,060 ft2，估算成本 300,000,000 美元。来源：https://www.tdlr.texas.gov/TABS/Projects/TABS2026026959
- 官方 TCEQ Records Online 的 Pacifico GW LLC Preliminary Determination Summary 确认 GW Ranch Energy Center 位于 Highway 18、Fort Stockton 以北约 17 miles，Permit Numbers 181033 / PSDTX1672 / GHGPSDTX255；项目描述为 Pecos County 绿地 35 台天然气简单循环机组、名义输出 5,000 MW，向 onsite AI data center 供电，且不能向本地公用事业配电系统售电或受电；允许 CO2e 排放 33,204,964.44 tpy。来源：https://records.tceq.texas.gov/cs/idcplg?IdcService=TCEQ_APD_SEARCH_GET_FILE&SearchID=15228583&searchType=External&xAPDParent=8069891
- Pacifico Energy 2026-01-26 公告称 GW Ranch 已获得 TCEQ air permit，许可 7.65 GW gas-fired power generation，项目总容量口径为 7.65 GW gas + 1.8 GW battery storage + 750 MWac solar，Phase 1 Gross Capacity 1 GW，Phase 1 First Power H1-2027。来源：https://www.pacificoenergy.com/post/pacifico-energy-secures-7-65-gw-power-generation-permit-for-gw-ranch-project
- Pacifico 项目页称 GW Ranch 是面向 hyperscale data centers 的 private-grid power generation campus；TCEQ approval 已到位，first power starting in Q1 2027，可到 2031 年扩展至 5+ GW；项目页另列 8,000+ acres。来源：https://www.pacificoenergy.com/gw-ranch
- Data Center Dynamics 2026-08-07 基于 TDLR 记录报道 Amazon Data Services 在 Pecos County 6000 TX-18 申报三栋 189,060 ft2 / 300,000,000 美元的数据中心楼，施工期为 2026 年 8 月至 12 月；该来源提示是否关联 Poolside Project Horizon 尚不清楚。来源：https://www.datacenterdynamics.com/en/news/amazon-files-to-develop-two-new-data-center-campuses-in-texas/
- The Verge 2026-08-08 报道 Amazon 已确认购买 Pecos County site 并计划从 GW Ranch 购电；Amazon 声明称该 planned data center campus 将由 new on-site generation 供电、不提高 Texas families 电价，并探索 solar、battery storage 与非饮用/非灌溉用水方案。来源：https://www.theverge.com/ai-artificial-intelligence/977124/amazon-data-center-worst-polluting-power-plant
- 状态更新：从自由文本“filed / permitted power campus; construction start reported for 2026; first power targeted 2027”规范为 `approved-permitted`。理由：TCEQ power-campus permit 已有官方记录，TDLR 三栋建筑为 Project Registered；TDLR 开工日是记录中的计划日期，不能单独证明现场已进入 `site work-construction`。
- 容量冲突/口径：`capacity_mw` 仍保留 7650，但解释为 Pacifico/TCEQ 许可 gross gas generation ceiling；TCEQ 技术摘要的 nominal output 是 5,000 MW，Pacifico 项目页称 over 5 GW deliverable/private-grid power，Amazon data-center IT load 未披露。
- 无法核实项：未找到 county/city 层面的 site plan、building permit 或 utility-service record；未能用官方来源核实 Amazon 数据中心实际 IT capacity、现场施工实况、Amazon 与 Pacifico 的最终购电合同容量。
