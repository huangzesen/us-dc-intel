# USDC-0121 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 结论：从 seed-only 提升为已核实的 `partial live / operational colocation` 记录。CoreWeave 官方 2021-06-12 公告称其通过 Switch 的 Las Vegas Tier 5 data center 开设 Las Vegas data center，服务 VFX、Machine Learning、AI、Batch Processing、Pixel Streaming 等工作负载。来源：https://www.coreweave.com/blog/coreweave-opens-new-data-center-in-las-vegas-opening-specialized-cloud-capabilities-for-west-coast-firms
- 当前 AI 部署补证：CoreWeave 2024-11-26 发布 GB200 NVL72 live demo，并称 Switch 是其 data center partner；2025-07-03 又发布 GB300 NVL72 bring-up，称该部署与 Dell Technologies、Switch、Vertiv 协作完成。Switch 同页说明该 GB300 部署运行在 Rob Roy's EVO AI Factories，并称此前 2024-11 的 GB200 安装也 hosted within Switch's AI Factories。来源：https://www.coreweave.com/blog/coreweave-unleashes-the-power-of-the-nvidia-gb200-nvl72-a-glimpse-into-the-future-of-ai；https://www.coreweave.com/blog/coreweave-leads-the-way-with-first-nvidia-gb300-nvl72-deployment；https://www.switch.com/coreweave-deploys-industry-first-nvidia-gb300-nvl72-in-switchs-ai-factory-solution/
- Switch Las Vegas campus context：Switch 官方 Las Vegas page 称 The Core in Las Vegas will have up to 495 MW upon completion，并列出 100% renewable energy、up to 2MW per cabinet、100% power uptime guarantee 等 campus-level claims。此为 Switch campus claim，不等同于 CoreWeave 专属容量。来源：https://www.switch.com/las-vegas/
- 地方政府记录：Clark County 2026-04-08 zoning minutes 批准 UC-26-0105-I I5 MOUNTAIN, LLC，内容包括 public utility structures、data center with electric substation and ancillary structures、rerouted aboveground utility lines/new utility poles，地点为 Enterprise 内 south of Serene Avenue and east of Decatur Boulevard，面积 55.10 acres；配套 TM-26-500027 一并批准。该官方记录未命名 CoreWeave，因此只作为 nearby/local data-center approval context，不作为 CoreWeave-owned campus 或 CoreWeave MW 容量证据。来源：https://clark.legistar.com/View.ashx?GUID=5417716B-964D-4C41-BC27-5E19D388798C&ID=1403437&M=M
- 字段更新：`status_as_of_cutoff` 由 null 更新为 `partial live / operational colocation as of 2026-08-11`；新增 `evidence_grade: B`；`owner` 由 null 更新为 `CoreWeave deployment/customer; underlying Las Vegas facility/campus operated by Switch`；`seed_only` 由 true 改为 false。
- 容量：`capacity_mw` 保持 null。第三方 tracker 有 CoreWeave Las Vegas MW 数字，但本轮未找到 CoreWeave、Switch 或 Clark County 对 CoreWeave 专属容量的官方确认。
- 冲突/限制：CoreWeave/Switch 官方来源足以证明 Las Vegas/Switch operational deployment 和 AI-factory relationship；Clark County 来源足以证明当地 data-center/public-utility land-use approval；两者不能合并推断为 CoreWeave 自有 campus expansion、专属 MW、building permit issued、construction start 或 energization。
