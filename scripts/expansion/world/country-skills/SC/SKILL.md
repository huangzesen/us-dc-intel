---
name: sc-datacenter-methodology
location: scripts/expansion/world/country-skills/SC/SKILL.md
description: |
  Seychelles (SC) datacenter discovery & audit methodology — how to enumerate, verify, and update Seychelles datacentre facilities at 27-district granularity. Seychelles has no datacentre registry: enumeration joins planning records (SPA/ePlanning, Gazette), communications regulation (SCRA, Communications Act 2023, 2026 licensing regulations), datacentre certification registries (TIA-942/EPI for Airtel Seychelles, Uptime Institute for Cable & Wireless Bon Espoir), government ICT/procurement (DICT, National Tender Board, Invest Seychelles, Data Protection Act 2023), energy/utility records (PUC/URC), submarine-cable connectivity (SEAS/Victoria, PEACE/Perseverance, 2Africa/North East Point), and cloud-region absence checks (no AWS/Azure/GCP/OCI region). Read this before running SC exploration/audit batches. Routes to explorer-official.md (planning/regulator/certification/energy/cable pipeline) and explorer-industry.md (operator seeds/trade press/directory verification/district recipes).
---

# SC · 塞舌尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：塞舌尔是**电信主导的极小岛国市场**，没有数据中心注册表；已确认的两座商业/运营者设施都靠认证注册表证明存在：**Airtel Seychelles Limited（Airtel House, Josephine Cafrine Road, Perseverance, Mahé）**——TIA/EPI 证明 ANSI/TIA-942-B Constructed Facility Rating Level 3（证书 TIA942SC221107001，2022-11-07 颁发，2025-11-06 到期，刷新前须核续期）；**Cable & Wireless Data Center 1 - Bon Espoir**——Uptime Institute 记 Anse Boileau，Seychelles Nation 记 2023-08-22 公告/2024-09-21 启用/2024-11-22 落成，SBC 记 Bon Espoir/Montagne Posee。
> 两设施均无公开 MW/机架/面积——默认 `capacity_mw: null`；无独立中立托管商、无超大规模区域；海缆登陆站默认是连接性设施，不是 DC。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供塞舌尔探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：SPA/ePlanning 规划许可、SCRA/Communications Act 2023/2026 牌照条例、TIA/EPI/Uptime 认证注册表、DICT/NTB/Invest Seychelles/Information Commission、PUC/URC/MACCE 能源、SEAS/PEACE/2Africa 海缆主源、云区域缺席核验、27 区工作流与种子表 |
| `explorer-industry.md` | 行业/厂商发现：运营者优先级扫描（Airtel/CWS/Intelvision/SCS）、认证与媒体源清单、目录到一手工作流、27 区配方、种子记录验证、容量与可靠性提取规则 |

## 核心结构事实（框定每次搜索）

1. **两座确认设施**：① Airtel Seychelles（TIA/EPI A 级地址+认证；Ericsson 2021 交钥匙搬迁/现代化公告；暂定记 **Ile Perseverance I**，除非地块证据区分 I/II）；② CWS Data Center 1 - Bon Espoir（Uptime A 级地点 Anse Boileau；媒体 B 级日期/300 万美元 capex；按 Anse Boileau 记，除非 SPA 地块另有边界）。
2. **认证 ≠ 容量**：TIA Rated 3/Uptime Tier 只是可靠性/认证证据；不得从认证、capex、海缆带宽或营销声称推断 MW/机架/面积；Airtel 证书 2025-11-06 到期——描述“当前认证”前必须复核续期状态。
3. **海缆链（连接性，非 DC）**：SEAS（WIOCC：1917 km 马埃-达累斯萨拉姆，Victoria 登陆站；历史 Beau Vallon 岸上接入）；PEACE（2022-03 登陆 Perseverance Island，2022 运营）；2Africa 塞舌尔支线（2023-04-20 Intelvision/Vodafone 登陆 North East Point，IFC 至多 2000 万美元融资）。有服务器/托管/colo 证据才升设施。
4. **监管**：SCRA（scra.sc）定义持牌运营者宇宙（facilities-based/services-based，Communications Act 2023 + 2026 SI 1/2026 牌照条例），不是完整设施注册表；SCRA 之前的基础设施查 DICT（ict.gov.sc）时代记录。
5. **规划管线**：SPA/ePlanning（eplanning.gov.sc）+ Gazette + monServis 是地址/地块/区/用途/发电机/冷却/变电站/批准/拒批/上诉的最佳一手源。
6. **政府/公共部门**：NTB（托管/服务器/灾备/政府 ICT 招标）、Invest Seychelles 官方把 **Data Centers 和 Submarine Cable Links** 列为 ICT 投资机会（A 级机会证据，非设施）、Information Commission（Data Protection Act 2023 / Act 24 of 2023）、SLA 商业牌照、FSA 金融实体（需求信号）。
7. **能源**：PUC/URC/MACCE 记录用于佐证大负载/变电站/备用发电/燃料储存/环评；有发电机≠DC。
8. **云缺席**：AWS/Azure/GCP/OCI 均无塞舌尔区域/本地分区（官方页每次刷新核验）；本地 VPS/托管/云转售仅服务证据。
9. **语言与噪音**：英语 + 法语（centre de données/salle de serveurs/hébergement/générateur de secours）；**`.sc` 污染**：必须带 Seychelles/运营者名/塞舌尔地名——裸 `SC data center` 会返回美国南卡罗来纳。
10. **区界是最大错误源**：Bon Espoir/Montagne Posee→Anse Boileau；North East Point→Anse Etoile/Glacis 跨界；Providence→Roche Caiman/Cascade/Plaisance/Pointe Larue 搜索空间；Perseverance I/II 两块区，未用地块证据不得复制记录。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §2-§4）

- 规划：`site:spa.gov.sc OR site:eplanning.gov.sc "data centre" OR "server room" OR "cable landing station"`、`"Bon Espoir" OR "Montagne Posee" OR "Perseverance" OR "Josephine Cafrine Road"`、`"Providence" OR "Roche Caiman" OR "New Port" OR "Ile du Port" OR "Victoria"`、`"centre de données" OR "salle de serveurs" OR "hébergement"`。
- 监管/法律：`site:scra.sc Seychelles "Cable & Wireless" OR Airtel OR Intelvision`、`site:scra.sc Seychelles "facilities-based" OR "services-based"`、`site:gazette.sc "Communications Act" "2023" Seychelles`、`site:ict.gov.sc Seychelles "data centre" OR hosting OR server`。
- 认证：`site:tiaonline.org/942-datacenter airtel-seychelles`、`site:epi-certification.com Airtel Seychelles Rated 3`、`site:uptimeinstitute.com "Data Center 1" "Bon Espoir"`。
- 政府/采购：`site:ntb.sc Seychelles "data centre" OR hosting OR "disaster recovery"`、`site:infocom.sc Seychelles "Data Protection Act"`、`site:investinseychelles.com "Data Centers" "Submarine Cable Links"`、`site:sla.gov.sc "Cable & Wireless" OR Airtel`。
- 能源：`site:puc.sc Seychelles "data centre" OR substation OR MVA`、`site:macce.gov.sc Seychelles generator OR "Bon Espoir" OR Perseverance`。
- 海缆：`"SEAS" "Seychelles" "Victoria" OR "Beau Vallon"`、`"PEACE cable" Seychelles Perseverance`、`"2Africa" Seychelles "North East Point" Intelvision Vodafone IFC`。
- 运营者：`"Airtel Seychelles" "Airtel House" "TIA-942"`、`"Cable & Wireless" "Bon Espoir" "Data Center 1"`、`"Intelvision" "Providence" hosting OR "data centre"`、`"Seychelles Cable Systems" SEAS OR PEACE "landing station"`。
- 媒体/目录：`site:nation.sc "Airtel" "data centre"`、`site:sbc.sc "Bon Espoir" "data centre"`、`site:seychellesnewsagency.com "data centre" Seychelles`、`site:datacenterdynamics.com Seychelles`、`site:datacentermap.com Seychelles`。
- 负控制：`"Seychelles" colocation OR "co-location" provider`、`"Seychelles" "AWS" OR Azure OR "Google Cloud" OR OCI`、`"SC" "data center" -Seychelles`。

## 官方/监管管线要点（详见 explorer-official.md）

- **SPA/ePlanning（A）**：提取申请号、申请人/法人、地块/地址、区、开发描述、面积、发电机/变电站/冷却细节、决定状态/日期、条件、上诉史、源 URL；Gazette 确认公告/法规/边界。
- **SCRA（A 运营者宇宙）**：从持牌人转向设施；牌照不是设施证据。
- **认证注册表（A，塞舌尔最干净的设施证据）**：TIA-942 页、EPI 页（Airtel 地址 + Rated 3 日期 + 续期）、Uptime（CWS Bon Espoir 项目/客户页）；证书证明认证设施与评级，不证明 MW/商业可用性/精确地块。
- **政府 ICT/投资/数据保护（A/B）**：NTB 招标、Invest Seychelles 机会页、Information Commission 数据保护框架、SLA 实体核验；金融部门只作需求信号。
- **能源/环境（A 佐证）**：PUC/URC/MACCE 大负载/变电站/备用发电/燃料/EIA；不得仅因发电机或电信供电就升级站点。
- **海缆（A/B 连接性）**：WIOCC SEAS 页（Victoria CLS）、Submarine Networks PEACE、2Africa/IFC North East Point；都按连接性基础设施处理。
- **云缺席（A）**：四家官方区域页每次刷新核验；本地转售/边缘仅服务证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营者种子**：Airtel（A 设施/地址/历史认证，续期待核）、CWS Bon Espoir（A Uptime、B 日期/capex）、CWS 遗留 Victoria 基础设施（B/C lead，地址待证）、Intelvision（ISP/2Africa 运营者已验证，专用 DC 未证实，Roche Caiman/Cascade/Plaisance 边界）、Seychelles Cable Systems/SEAS/PEACE（A/B 海缆）、政府/DICT 托管（C lead）、金融机房（C 需求信号）。
- **认证源（A）**：tiaonline.org、epi-certification.com、uptimeinstitute.com；Ericsson 新闻稿（A 厂商-客户项目声明，地址用 TIA/EPI/Airtel 核验）。
- **媒体（B+）**：Seychelles Nation（CWS 日期/capex、Airtel 认证故事）、SBC、Seychelles News Agency、Submarine Networks（B；引运营者/系统主源才 A）、DCD/Developing Telecoms/TechAfrica News/The Tech Capital（B）。
- **目录（C）**：DataCenterMap/Baxtel/Cloudscene/datacenters.com 仅种子；社交 C。
- **种子记录验证**：Airtel（A，运营）、CWS Bon Espoir（A，运营）、CWS Victoria 遗留（B/C）、Intelvision Providence（B/C）、SEAS/PEACE/2Africa（A 海缆，连接性）、India-Seychelles Centre for Excellence in ICT（Mont Fleuri，B 历史制度线索，Nation 2011 + UniSey/NTB/DICT 验证）。
- **容量提取**：记录认证机构/Tier/证书 ID/颁发与到期/ capex/启用日期/地址/区/运营者/客户类型/服务/海缆相邻性；不从 Tier、capex、海缆带宽、“world-class” 声称推断容量。

## 来源分级

- **A** = 官方/一手证明主张：规划/ePlanning 记录、Gazette/法律文书、SCRA/DICT/SIB/Information Commission/PUC/URC 页面、运营者官方页、TIA/Uptime 认证注册表、海缆系统/运营者页、云厂商官方区域页（缺席）。
- **B** = 可信媒体/贸易：Seychelles Nation、SBC、Seychelles News Agency、DCD、Developing Telecoms、Submarine Networks（非海缆拥有/运营者时）、Ericsson 之外的一般厂商稿。
- **C** = 目录/市场/SEO/社交/转载/无地址无设施证据的声称。
- **状态语义**：Airtel/CWS 均为运营设施（认证或启用证据）；CWS 遗留/Intelvision = lead；SEAS/PEACE/2Africa = 连接性站点；2011 印塞 ICT 卓越中心 = 历史制度线索；认证到期日期单独记录，与设施存在分开。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=SC，divisions=27 区）。
2. 种子：Airtel（TIA/EPI/Airtel 联系页）+ CWS Bon Espoir（Uptime/CWS/Nation/SBC）+ 海缆链（WIOCC/Submarine Networks/2Africa）+ Intelvision + 政府（DICT/NTB）。
3. 对每个区跑通用模板（英语+法语变体）+ 规划/媒体/目录域；高产区（Anse Boileau/Anse Etoile/Glacis/English River/Roche Caiman/Perseverance I-II）深扫。
4. 区界处理：Bon Espoir→Anse Boileau（除非 SPA 地块）；North East Point→Anse Etoile/Glacis 两边都扫；Providence 四区跨界搜索；Perseverance I/II 地块证据前不复制。
5. 目录到一手：目录种子 → 认证注册表/运营者官方域 → SPA/Gazette 地块 → 状态证据（启用/落成/认证/运营服务）；仅目录行保持 C。
6. 去重/状态：CWS “首个数据中心”营销不得压过 Airtel 更早的一手证据；海缆不记 DC；所有 27 区进扫描清单，无项目显式记 no_projects。
7. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无容量用 null；旧线索无法核验时保留为降级 lead 并注明缺失证据（NO-DELETION）。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核塞舌尔数据中心（27 区粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Airtel TIA-942 证书续期状态（2025-11-06 到期后）、CWS Bon Espoir 容量/客户、Intelvision 是否有独立 DC、2011 印塞 ICT 卓越中心现状、SPA/ePlanning 是否出现两设施地块记录、任何本地 VPS/托管是否对应物理设施。
