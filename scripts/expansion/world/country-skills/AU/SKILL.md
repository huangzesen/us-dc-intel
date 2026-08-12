---
name: au-datacenter-methodology
location: scripts/expansion/world/country-skills/AU/SKILL.md
description: |
  Australia (AU) datacenter discovery & audit methodology — how to enumerate, verify, and update Australian datacentre projects at local-government-area (LGA) granularity (540 divisions grouped by state/territory). Australia has no national public datacentre registry: enumeration is a planning-approval exercise across state significant-development portals and hundreds of local council DA registers — NSW Planning Portal major projects/SSD, Planning Victoria Ministerial Permits Register (Clause 53.22 Utility Installation (Data Centre)), QLD Development.i / EDQ, WA Planning Online / DAP, PlanSA, ACT DA+ESO, NT Planning, Tas PlanBuild — joined to AEMO / network energy evidence (Transgrid, AusNet, Powerlink, ElectraNet, Western Power, TasNetworks, PWC NT), official cloud-region pages (AWS ap-southeast-2/4, Azure East/Southeast/Central, GCP australia-southeast1/2, OCI Sydney/Melbourne/Canberra), ACMA spectrum records, and operator pages (NEXTDC, AirTrunk, CDC, Macquarie, Equinix, Digital Realty, Global Switch/HMC, Telstra, Vocus, Leading Edge). Read this before running AU exploration/audit batches. Routes to explorer-official.md (planning/energy/ACMA/cloud) and explorer-industry.md (trade press/vendors/state planning workflows).
---

# AU · 澳大利亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：澳大利亚**没有**国家公共数据中心注册库；枚举主要是跨州级 significant development 门户与数百个地方议会 **DA（development application）注册** 的规划审批工作，并 join **AEMO/电网能源证据**、**官方云区域页**、**ACMA 频谱记录**与**运营商官方页**。
> 仓库 division 是 **LGA**（按州/领地分组），即使首发来源是州门户/运营商页/能源文件，也要把项目归到正确议会/市/郡。当前最高产出官方规划源：**NSW Planning Portal major projects（SSD）** 与 **Planning Victoria Ministerial Permits Register（Clause 53.22 `Utility Installation (Data Centre)`）**。
> 拼写：澳洲用 `data centre`，云/运营商材料常用 `data center`——两者都搜。本 skill 汇总两份探索报告（官方管线 + 行业发现），供澳大利亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：NSW SSD/VIC 部长许可/QLD Development.i/WA DAP/PlanSA/ACT ESO/NT/TAS 规划门户、AEMO 与各州输配电网、EPA 与备用发电机环境痕迹、ACMA 频谱、官方云区域页、运营商官方种子、LGA 工作流与提取字段 |
| `explorer-industry.md` | 行业/厂商发现：DCD/CRN/ARN/iTnews/AFR 媒体、运营商/开发商矩阵（NEXTDC、AirTrunk、CDC、Macquarie、Equinix、Digital Realty、Global Switch/HMC、Goodman、Stockland、Centuria、Insite DC、STACK、Leading Edge）、州/领地规划工作流与 LGA 查询配方、去重与分级陷阱 |

## 核心结构事实（框定每次搜索）

1. **无国家注册库**：枚举=三角验证：①运营商位置页，②州 significant development 门户 + LGA DA 注册，③DCD/CRN/ARN/iTnews/AFR 与 ASX 披露；再用 AEMO/电网、ACMA、EPBC 佐证。
2. **规划碎片化**：NSW 大项目多为 **SSD**（`SSD-########`，Development Type=Data Storage / high technology industry）；VIC 大项目多在部长许可注册的 Clause **53.22** 下（`Utility Installation (Data Centre)`，PA24/PA25/PA26 编号）；WA 高价值项目由 **DAP** 决定（可能写作 `Proposed Warehouses and Ancillary Structures`）；SA 走 PlanSA（+拟议 Data Centre and AI Infrastructure Act）；ACT 走 DA + **Environmental Significance Opinion (ESO)**。
3. **能源常是早期证据**：超大规模园区常以 large-load connection、变电站、输电或需求预测先出现——AEMO/电网源对**电力/电网事实**为 A，但源未具名数据中心/运营商/匹配规划申请时不得推断设施。
4. **云区域=metro 种子**（A=区域存在，C=精确选址）：AWS Sydney `ap-southeast-2`（3 AZ）+ Melbourne `ap-southeast-4`（3 AZ）；Azure Australia East=NSW、Southeast=VIC、Central/Central 2=Canberra；GCP Sydney `australia-southeast1` + Melbourne `australia-southeast2`；OCI Sydney `ap-sydney-1` + Melbourne `ap-melbourne-1` + Canberra 政府云（IRAP PROTECTED）。不揭示建筑。
5. **容量字段分开**：`IT load`/`critical IT load` ≠ `operational capacity` ≠ `power consumption` ≠ `MVA`（电网导入）≠ `connection capacity`；新闻 `350MW campus` 多为**最终园区容量**，非一期/运营 IT load。
6. **去重**：同一园区可有运营商代码（S7）、项目名（Project Atlas）、郊区（Eastern Creek）、LGA（Blacktown）、地主（Goodman/Stockland）、客户（Microsoft/OpenAI/TikTok）多重身份——按 `(operator/developer, campus/site address, phase)` 记录；郊区名≠LGA 名，必须经规划门户/议会注册核实。
7. **措辞伪装**：规划描述可能不用 `data centre` 而用 `data storage`、`utility installation`、`high technology industry`、`warehouse and ancillary structures`；购地/MoU/政策/“AI hub” 无设施范围不计为数据中心。

## 查询模式（复制粘贴模板见 explorer-official.md §6 与 explorer-industry.md §4/§5）

- 双拼写核心词：`data centre` `data center` `datacentre` `data storage` `data hall` `server farm` `hyperscale` `AI data centre` `high technology industry` `utility installation` `sovereign cloud` `substation` `MVA` `IT load` `backup generators` `liquid cooling`。
- 州门户：`site:planningportal.nsw.gov.au/major-projects/projects "data centre" "{LGA}"`、`site:planningportal.nsw.gov.au/major-projects/projects "data storage" "{suburb}"`、`site:planning.vic.gov.au "Utility Installation (Data Centre)"`、`site:planning.vic.gov.au "53.22" "data centre" "{suburb}"`、`site:developmenti.brisbane.qld.gov.au "data centre"`、`site:planning.wa.gov.au "data centre" "DAP"`、`site:plan.sa.gov.au "data centre" "Development Application Register"`、`site:planning.act.gov.au "data centre" "Environmental Significance Opinion"`。
- LGA/议会：`"{LGA}" "data centre" "development application"`、`site:{council-domain} ("data centre" OR "data storage" OR "hyperscale" OR "substation")`、`"{suburb}" ("MVA" OR "MW" OR "substation") "data centre"`。
- 能源：`"{project}" ("MW" OR "MVA") "grid connection"`、`site:aemo.com.au "data centre"`、`site:transgrid.com.au OR site:ausnetservices.com.au OR site:powerlink.com.au OR site:electranet.com.au OR site:westernpower.com.au "data centre"`。
- 云/超大规模：`"AWS" "data centre" "Sydney" "SSD"`、`"Microsoft" "Australia East" "data centre" "NSW"`、`"Google Cloud" "australia-southeast1" "data centre"`、`"Oracle" "Australian Government" "Canberra" "data centre"`、`"{provider}" "Australia" "data centre" "planning"`。
- 媒体：`site:datacenterdynamics.com/en/news/ Australia "data center" "{city}" "MW"`、`site:crn.com.au "{operator}" "data centre"`、`site:arnnet.com.au OR site:itnews.com.au "data centre" "{suburb}"`。
- 文档：`filetype:pdf "data centre" ("planning statement" OR "environmental impact statement" OR "MVA" OR "substation") "{state or LGA}"`。
- 生命周期动词：`announced/eyes/MoU/landbank`=线索（C/B）；`acquires site/files plans/SSD lodged/ministerial permit/DAP approval`=具体管线（B/A）；`approved/construction starts/breaks ground/opens/ready for service`=可计数（需主证据）；`contracted capacity`/`future pipeline`≠已建容量。

## 官方/监管管线要点（详见 explorer-official.md）

- NSW：Planning Portal major projects（https://www.planningportal.nsw.gov.au/major-projects/projects ）——搜 `data centre`/`data storage`/`SSD`，提取申请号/LGA/MW·MVA/GFA/变电站/决定日期/附件（EIS、规划说明、电气报告）；西悉尼（Blacktown 的 Marsden Park `SSD-70889211`、Eastern Creek Project Atlas `SSD-101067971`、Penrith 的 STACK SYD01 `SSD-82211208`、Erskine Park/Mamre Road/Kemps Creek）、北区（Ryde/Lane Cove：Macquarie Park、Julius Avenue `SSD-80018208`、Project Apollo `SSD-74069708`、Project Mars `SSD-82052708`）、Cumberland/Fairfield/Liverpool（Guildford West Project Pluto `SSD-69223466`）。
- VIC：Ministerial Permits Register（https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register ）——Clause 53.22 `Utility Installation (Data Centre)` 高产出（Port Melbourne、West Footscray/Tottenham、Cobblebank、Campbellfield/Plumpton 高 MVA 提案）；LGA：Maribyrnong/Brimbank/Hobsons Bay、Hume/Melton/Wyndham、Port Phillip、Monash/Kingston/Greater Dandenong、Greater Geelong。
- QLD：Development.i（Brisbane）、EDQ PDA、各 LGA DA 注册；WA：Planning Online/DAP（Gosnells/Maddington `DAP/25/02926` CDC）、DevelopmentWA 工业地；SA：PlanSA 注册（NEXTDC A1 211 Pirie Street 六层 DC）+拟议专门立法；ACT：DA + ESO（Beard 2 ESO 2026：三层 DC/12 个 data hall/84 MW；Fyshwick 11kV feeder 证据）；NT：NT Planning + Invest NT（Darwin D1/D2、Weddell 大型 AI 园区提案 C/B）；TAS：规划门户+议会注册（注意排除 “Australian Antarctic Data Centre” 等科研数据仓库假阳性）。
- 能源：AEMO（需求预测/大负荷规则/ISP，具名项目才算）、Transgrid/Ausgrid/Endeavour/Essential（NSW）、AusNet/CitiPower/Powercor/United/Jemena（VIC）、Powerlink/Energex/Ergon（QLD）、ElectraNet/SA Power Networks（SA）、Western Power/Horizon（WA）、TasNetworks（TAS）、Power and Water/Territory Generation（NT）；提取连接 MW/MVA、供电电压、变电站名、增容工程、通电日期、可再生 PPA。
- 环境：各州 EPA（空气/噪声/水/备用柴油发电机/冷却），A=规划当局/EPA/水务/议会托管文档。
- ACMA 频谱注册（RRL）：按 licensee 搜 Equinix/NEXTDC/AirTrunk/Macquarie/CDC/Digital Realty/Global Switch/Vocus 等——A 级电信证据，仅当 licensee/地址/规划记录把发射点与数据中心绑定才作设施证据。
- 运营商官方页（存在性 A，容量 B）：NEXTDC（S1-S7、M1-M4、P、A、CBR、D、SC、GE、PH——官方 20 个 AU 站点；ASX 披露高价值）、AirTrunk（SYD1-3/MEL1-2，官方 755+MW）、CDC（20 地点/8 园区/4 城+奥克兰；DCD 报 302 MW 运营/388 MW 在建；Infratil 披露）、Macquarie Data Centres（IC3 East/Super West、Macquarie Park 200 MW 扩展、Canberra bunker）、Equinix（SYD/MEL/PER/BRI/CBR/ADL，官方称 18 个 AU DC）、Digital Realty（Sydney 2 个 DC）、Global Switch/HMC（Sydney Ultimo 遗产园区，所有权变更需核实）、Telstra/Doma/Starwood（Minchinbury 西悉尼）、Vocus、Leading Edge（区域边缘）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，最佳开放源：NEXTDC S4/S7/D2/Geelong、AirTrunk MEL2、CDC Perth/Melbourne 555MW 合同、Macquarie IC3 Super West）、CRN（B，Data Centres Australia/AirTrunk/Insite DC）、ARN/iTnews/AFR/The Australian/InDaily（B/C，本地争议/购地/就职）、Data Centres Australia 行业协会（B，政策/会员：AirTrunk/AWS/CDC/Microsoft/NEXTDC/Equinix/Goodman/Schneider/STACK/TikTok）、法律/规划注释（Dentons/Ashurst 等，B 改革语境）、RenewMap/项目跟踪器（C/B）。
- 开发商/地主：Goodman、Stockland、Centuria、Insite DC、STACK、DigiCo、Firmus——多为土地/开发而非运营品牌，需规划或租户证据。
- 区域边缘：Leading Edge Data Centres、Field Solutions Group、区域 ISP——出现于当地媒体/议会纪要而非 DCD，单独归类。
- 目录源（C/B-）：Baxtel、DataCenterMap、OCOLO、Datacenters.com、Cloudscene——遗留 colo 地址与小型站点线索，容量/位置需运营商页或规划证据匹配。

## 来源分级

- **A** = 官方/一手：州规划门户申请/决定、LGA DA 注册、WA DAP 纪要、ACT ESO、PlanSA 注册、运营商官方位置页（存在/状态）、ASX/投资人披露（容量 A/B 看阶段细节）、云官方区域列表（区域级）、AEMO/电网文档（具名）、ACMA RRL（绑定设施时）、EPA/水务/议会托管环境文档。
- **B** = 强二级：DCD、CRN、ARN、iTnews、AFR/地产媒体（具名主文档时）、Data Centres Australia/法律规划注释、规划师/承包商具名 DA 案例。
- **C** = 弱线索：Baxtel/DataCenterMap/OCOLO/Datacenters.com/Cloudscene（未佐证）、LinkedIn/社媒/当地运动页、无主审批轨迹的新闻、投机投资评论。
- 状态语义：`announced/eyes/shortlisted/MoU/landbank`=线索；`acquires site/files plans/SSD lodged/ministerial permit/DAP approval`=具体管线；`approved/determination/construction starts/breaks ground/tops out/opens/ready for service`=可计数（主证据）；`contracted capacity`/`future pipeline`=非已建容量。
- 去重：保留官方申请号（`SSD-...`/`PA...`）作稳定锚；同一园区按 `(operator/developer, campus/site address, phase)` 记一条 campus 记录；`capacity_mw` 与容量口径（IT load/critical IT load/operational capacity/power consumption/MVA/connection capacity）分别入 notes。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=AU，divisions=540 LGA，按州/领地分组，如 `New South Wales - Blacktown`）。
2. **归一化 division**：拆出州 + LGA，按 trade/operator 命中建立郊区 watchlist。
3. **州门户优先**：NSW=Planning Portal/SSD；VIC=部长许可；QLD=Development.i+PDA；WA=Planning Online/DAP；SA=PlanSA；ACT=DA+ESO；NT=NT Planning+Invest NT；TAS=规划门户+议会注册。
4. **LGA DA/议会搜索**：`data centre`/`data center`/`data storage`/`utility installation`/`high technology industry`/`substation`/`backup generator`。
5. **运营商/云/媒体扫描**：NEXTDC、AirTrunk、CDC、Macquarie、Equinix、Digital Realty、Telstra、Global Switch/HMC、Goodman、Stockland、Centuria、Insite DC、STACK、Leading Edge + 云区域页 + DCD/CRN/ARN/iTnews。
6. **能源/状态验证**：AEMO/电网具名证据；容量按口径分别存储，`350MW campus` 记 planned/ultimate 而非运营 MW；无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核澳大利亚数据中心（540 LGA）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：AirTrunk MEL2 354MW+/悉尼 630MW+ 分阶段、CDC 555MW 合同与 Perth/Maddington 校区、Macquarie IC3 Super West 与 200 MW Macquarie Park 扩展、Global Switch 澳洲资产出售给 HMC 后的当前归属、NEXTDC D2/Geelong/PH1 状态、WA DAP 新校区（Gosnells Maddington）、SA 专门立法落地后 PlanSA 变化。
