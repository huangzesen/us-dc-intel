# USDC-0117 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `announced`。NJFX 于 2025-12-02 公告称 10 MW high-density AI data hall 已完成 Basis of Design，预计 1.25 PUE、8 MW usable IT load；同时称已执行 utility load letter，并以 300 万美元 deposit 支撑，目标 2026 年底供电。来源：https://njfx.net/njfx-advances-campus-for-ai-infrastructure/
- capacity_mw: `null` -> `10`；新增 `capacity_it_mw: 8`。该容量来自 NJFX 2025-12-02 公司公告，PR Newswire 同步转发相同事实。来源：https://www.prnewswire.com/news-releases/njfx-advances-campus-for-ai-infrastructure-302630765.html
- owner: `null` -> `NJFX`；location 补充为 1410 Wall Church Road, Wall Township, NJ 07719。Submarine Networks 2020-08-07 资料列明 NJFX cable landing station campus 为 64,800 sq ft Tier 3 CLS colocation facility，地址为 1410 Wall Church Road，并说明其邻近 Tata 1400 Wall Church Road CLS。来源：https://www.submarinenetworks.com/en/stations/north-america/usa-east/njfx-cable-landing-station-campus
- local-government evidence: Wall Township 2015-05-04 Planning Board minutes 记录 PB #4-2015 NJFX, LLC, Block 270 Lot 32, 1400 Wall Church Rd, Preliminary & Final Major Site Plan materials；2017-08-24 Township resolution 授权 NJFX Campus LLC developer agreement for site plan approval；2026-02-10 check register 记录 B270 L32.01 NJFX, LLC escrow/in-house professional services 139.25 美元。来源：https://www.wallnj.gov/AgendaCenter/ViewFile/Minutes/05042015-318 ; https://www.wallnj.gov/DocumentCenter/View/14385/17-0824-Developers-agreement-NJFX-Campus-LLC ; https://www.wallnj.gov/DocumentCenter/View/17437/26-0201-Certification-of-Funds
- power / technical milestone: NJFX 2025-05-15 称其在 annual electrical permit 下安装、测试并投用额外 power capacity，包括 ASTS units、transformers、UPS systems、battery cabinets；同文称 first floor is being designed to support a 4.5 MW liquid-cooled data hall，second floor supports up to 40 kW/rack air-cooled densities。来源：https://njfx.net/today-njfx-installs-new-n1-mw-block-of-power-ready-for-service-rfs/
- conflict retained: 2025-05-15 NJFX 文案为 4.5 MW liquid-cooled first-floor hall，2025-12-02 NJFX 文案为 10 MW hall / 8 MW IT load。本次按较新的 2025-12-02 公告作为 current announced scope，4.5 MW 保留为 earlier phase/history。
- evidence limits: 本轮未找到公开 Wall Township planning/permit 记录能直接证明 10 MW AI hall 已获批、开工、并网或 energized；2026 escrow record 仅能证明 NJFX parcel 有 escrow/professional-services activity，不能单独归因到 AI hall。`verified: false`，原因是 utility load letter、deposit、end-2026 power-delivery target 仍为公司披露，缺少 utility/local-government 独立文件。
