# disc003 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-grid-queue.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 状态从笼统的 "definitive acquisition agreement; powered land site; construction expected to start in 2026" 更新为 "announced/acquired project company; pre-construction local process"。SEC 8-K 显示 Volt Texas, LLC 于 2026-07-02 与 HIF USA LLC 签署并同时完成 MAT 1177 LLC 交易；项目公司持有 Texas site 购地合同/相邻已拥有地块以及电力公司 LOA，涉及向 site 提供 2,000 MW power capacity。来源: https://www.sec.gov/Archives/edgar/data/1507605/000095014226002012/eh260804074_8k.htm
- 容量仍保留为 2,000 MW，但标注为 utility LOA / expected grid-capacity path，而非已并网容量。MARA/HIF 2026-07-09 公告称 site 超过 1,200 acres，预计 2027-10 前可取得 initial 1 GW grid capacity、2028-04 前可达 2 GW；公告同时称 phased construction expected to begin in 2026, contingent upon regulatory approvals。来源: https://ir.mara.com/news-events/press-releases/detail/1424/mara-signs-agreement-with-hif-to-acquire-strategic-powered-land-site-in-texas
- owner/控制结构补强：MARA 通过 Volt Texas LLC / MAT 1177 LLC 控制项目公司；Starwood Digital Ventures 是 development partner；HIF USA 的 retained minority interest 与后续 third-party HPC tenant lease 触发条件相关。来源: https://www.sec.gov/Archives/edgar/data/1507605/000095014226002012/eh260804074_8k.htm
- local-government-first 检索未发现 Matagorda County 页面、permit roster 或 commissioners court 页面直接点名 MARA / Volt Texas / MAT 1177 的施工许可或议程。Matagorda County Environmental Health 页面确认 county 要求 permits for all new construction、electrical service connections 等，因此本次未把状态提升为 approved-permitted 或 site work-construction。来源: https://www.matagordatx.gov/page/EnvironmentalHealth ; https://www.matagordatx.gov/page/Commissioners.Court
- Matagorda County EDC "Current Projects" 页面 current as of Q1 2026 仅概括 county project pipeline 与 confidential private-sector projects，未具体列出 MARA/Volt/MAT 1177。来源: https://mcedc.net/resources/current-projects/
- 冲突/陈旧信息：HIF Matagorda location page 仍称 Matagorda e-Fuels Facility "Fully permitted to begin construction" 且 "Power interconnect is secured"，但 2026-07-09 MARA/HIF 公告称 HIF will continue advanced fuels development plans on other sites，且 digital-infrastructure campus construction 仍 contingent upon regulatory approvals。该冲突保留在 data.json contradictions。来源: https://hifglobal.com/locations/matagorda ; https://ir.mara.com/news-events/press-releases/detail/1424/mara-signs-agreement-with-hif-to-acquire-strategic-powered-land-site-in-texas
- 行业媒体 DCD 于 2026-07-13 复核了 company announcement 的主要事实：Matagorda County powered site、>1,200 acres、1 GW by 2027-10、2 GW by 2028-04、Starwood partnership、construction expected this year subject to approvals。来源: https://www.datacenterdynamics.com/en/news/mara-acquires-1200-acre-texas-site-from-hif-usa-for-up-to-2gw-data-center-campus/
- 无法核实/证据不足：未找到公开 local-government permit/site-plan 文件直接证明 MARA campus 已获施工许可、已开工或已并网；未找到可公开核验的精确 parcel/address/coordinates；未找到已签署 third-party HPC tenant lease。
