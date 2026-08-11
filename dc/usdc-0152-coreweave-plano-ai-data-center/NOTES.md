# USDC-0152 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `partial live / expansion fit-up registered as of 2026-08-11`。依据：CoreWeave 2023-07-25 公告称 Plano facility 预计 2023-12-31 fully operational；但 2026 年官方记录显示 1000 Coit Road 仍有 replat 与 Phase 3 fit-up 注册，故不标为 full buildout。来源：https://www.prnewswire.com/news-releases/coreweave-opens-new-texas-data-center-to-expand-access-to-high-performance-gpus-301884897.html ; https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026023537 ; https://content.civicplus.com/api/assets/ac54ba65-bc6a-4347-92d9-239d91767bd3
- 官方/local-gov 补证：Plano City Council 2023-07-24 approved CoreWeave, Inc. tax-rebate agreement for 2024-2031；背景说明 CoreWeave 将在 1000 Coit Road, Plano, TX 75075 占用至少 454,421 gross square feet，用作 data center，并增加至少 $1.6B business personal property。来源：https://plano.novusagenda.com/agendapublic/CoverSheet.aspx?ItemID=8487&MeetingID=3420
- 官方协议附件补证：Coreweave Tax Rebate Agreement 要求 by Commencement Date lease and Occupy at least 454,421 square feet at 1000 Coit Road and use the real property as a data center；by 2024-12-31 add at least $800M BPP improvements；by 2025-12-31 total BPP improvements at least $1.6B。来源：https://plano.novusagenda.com/agendapublic/AttachmentViewer.ashx?AttachmentID=17906&ItemID=8487
- 2026 当前官方记录：City of Plano Planning Department Development Review List printed 2026-08-06 lists R2026-025, BAC COIT, Block 1, Lot 1R, address 1000 Coit Rd, description "Data center on one lot on 23.8 acres located at the southeast corner of Coit Road and Jomar Drive", owner 1000 Coit Road LLC, applied 2026-06-18. 来源：https://content.civicplus.com/api/assets/ac54ba65-bc6a-4347-92d9-239d91767bd3
- 2026 当前 state record：TDLR TABS2026023537, registered 2026-06-23, project "Koala - Fit Up Phase 3", facility "Coit Road Data Center", 1000 Coit Rd, Plano, privately funded renovation/alteration, 9,419 sf shell-space data-center fit-up plus supporting infrastructure/site improvements, estimated cost $136M, start 2026-09-11 and completion 2027-12-02, owner Lincoln Property Company. 来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026023537
- owner/operator: `owner` 从 null 更新为 Lincoln Property Company / 1000 Coit Road LLC listed in official 2026 records as owner/site owner; CoreWeave, Inc. as tenant/operator named in 2023 Plano agreement and company announcement。来源同上。
- capacity_mw: 保持 null。未找到官方 MW；第三方容量冲突：datacenter.fyi 报 13.75 MW / 8.25 MW IT load；DataCenterMap 标题报 30 MW；LoopNet 对底层 1000 Coit Road facility 描述为 13+ MW available now, expandable to 24 MW。来源：https://www.datacenter.fyi/public-record/coreweave-0d7f2259 ; https://www.datacentermap.com/usa/texas/dallas/coreweave-plano/ ; https://www.loopnet.com/Listing/1000-Coit-Rd-Plano-TX/27162588/
- verified: true for address, local approval, incentive obligations, 2026 replat listing, and TDLR fit-up registration; verified: false for exact MW capacity and direct proof of full buildout/energized state.
