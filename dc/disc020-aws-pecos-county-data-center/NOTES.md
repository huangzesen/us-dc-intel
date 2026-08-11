# disc020 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-secondary-markets.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 官方 TDLR TABS 记录确认 Amazon Data Services, Inc. 为 PECOS COUNTY DATA CENTER 的 owner，地址为 6000 TX-18, Fort Stockton, TX 79735，Pecos County；Buildings A/B/C 分别对应 TABS2026026954、TABS2026026955、TABS2026026959，均为 2026-08-04 注册、Current Status 为 Project Registered、Type of Work 为 New Construction、Scope 为 new data center building。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026026954
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026026955
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026026959
- 三栋楼每栋 TDLR 记录均列示 189,060 sq ft、estimated cost $300,000,000、Start Date 2026-08-01、Completion Date 2026-12-01；合计已知建筑面积 567,180 sq ft、估算造价 $900,000,000。来源同上。
- TDLR 记录列出 design firm 为 M. Arthur Gensler & Associates, Inc.，RAS/filing contact 为 Meghan Simecek，tenant 未分配。来源同上。
- TCEQ Records Online 的 Pacifico GW LLC Preliminary Determination Summary（permit numbers 181033, PSDTX1672, GHGPSDTX255）将 GW Ranch Energy Center 定位为 Highway 18 approximately 17 miles north of Fort Stockton, Pecos County，并说明该天然气电厂 nominal output 为 5,000 MW，will provide electricity for an on-site AI data center，且 initially 不连接 local utility distribution system。来源：https://records.tceq.texas.gov/cs/idcplg?IdcService=TCEQ_APD_SEARCH_GET_FILE&SearchID=15228583&searchType=External&xAPDParent=8069891
- Pacifico Energy 项目页/新闻稿称 GW Ranch 获 TCEQ approval，配置 up to 7.65 GW gas、1.8 GW battery storage、up to 750 MWac solar；first power 目标为 Q1 2027，1 GW online in 2028，5+ GW by 2031。来源：
  - https://www.pacificoenergy.com/gw-ranch
  - https://www.pacificoenergy.com/post/pacifico-energy-secures-7-65-gw-power-generation-permit-for-gw-ranch-project
- Cleanview 2026-08-07 报道称 Amazon confirmed to Cleanview it acquired the GW Ranch site and plans to build an AI data center campus powered by on-site natural gas generation; Cleanview also reports land clearing visible in 2026-07-24 satellite imagery. This is treated as high-value secondary evidence, not as an official Amazon release. 来源：https://newsletter.cleanview.co/p/scoop-amazon-is-behind-one-of-the
- Data Center Dynamics 2026-08-07 independently summarized the three Fort Stockton TDLR filings and reported the site is approximately 11 miles north of Fort Stockton. 来源：https://www.datacenterdynamics.com/en/news/amazon-files-to-develop-two-new-data-center-campuses-in-texas/
- 本次状态调整：从 “TDLR filed; construction listed for August-December 2026” 规范为 “local process - TDLR TABS project registered for Buildings A-C; listed construction schedule 2026-08-01 to 2026-12-01; no official site-work or energized evidence found”。原因：TDLR 当前状态仅为 Project Registered，未找到地方 building permit、inspection、certificate of occupancy、utility interconnection 或官方现场施工证据。
- capacity_mw 仍保留为 null：TDLR/TCEQ/Pacifico/Cleanview 均未披露数据中心 IT load。GW Ranch 的 5,000 MW nominal output / 7.65 GW gas nameplate 属于相关电力基础设施，不等同于 data center capacity_mw。
- 多源冲突/口径差异：TCEQ 记录写 nominal output 5,000 MW；Pacifico/Cleanview 使用 up to 7.65 GW gas/nameplate。已在 data.json 的 related_infrastructure 与 contradictions 分开记录。
