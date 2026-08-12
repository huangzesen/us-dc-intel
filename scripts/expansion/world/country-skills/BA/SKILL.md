---
name: ba-datacenter-methodology
location: scripts/expansion/world/country-skills/BA/SKILL.md
description: |
  Bosnia and Herzegovina (BA) datacenter discovery & audit methodology — how to enumerate, verify, and update BA datacenter projects across the 3 manifest divisions (Federation of BiH, Republika Srpska, Brcko District). There is no national datacenter registry and no unified building-permit database: enumeration joins state-level telecom (RAK) / energy (DERK, FERK, RERS) regulation, cantonal (FBiH) and municipal (RS) and District (BD) planning permits, e-Nabavke public procurement, operator pages (BH Telecom, HT Eronet, m:tel, Integra, LANACO, Globalhost), and trade press. Read this before running BA exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (industry/vendor discovery).
---

# BA · 波黑数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：波黑**没有**全国数据中心注册库，也**没有**统一的国家建筑许可数据库，不能按单一门户方式枚举。
> 波黑枚举靠**三套法律/许可体系拼接**：联邦（FBiH）10 州 + 市镇许可、塞族共和国（RS）市政许可、布尔奇科特区（BD）特区许可；电信牌照在国家层 RAK，电力牌照分属 DERK（国家）/FERK（FBiH）/RERS（RS）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供波黑探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：RAK 运营商宇宙、DERK/FERK/RERS 电力许可、FBiH FMPU + 10 州矩阵、RS 部委/市政（含西里尔）、BD 特区许可、环境许可、e-Nabavke 采购、云区域负面清单 |
| `explorer-industry.md` | 行业/厂商发现：运营商与设施种子（BH Telecom/HT Eronet/m:tel/Integra/LANACO/Globalhost）、贸易媒体（Klix/Avaz/Nezavisne/Glas Srpske/SeeNews/BIRN 等）、协会与目录、BCS+西里尔查询模板、分区枚举配方、容量与状态提取 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库/无统一许可库**：建筑许可在 FBiH 州级、RS 市级、BD 特区级签发；电信牌照在国家层（RAK），电力牌照分 DERK/FERK/RERS。单一门户查无 ≠ 项目不存在。
2. **三个行政体 = 三个法律体系**：FBiH（10 州，~79 市，无统一 e-permit 门户，须轮询州部委与市政）、RS（一个规划部委，多数许可由市政 Odjeljenje 签发；旧 `vladars.net` 跳转 `vladars.rs`；eDozvola 地址须枚举时从 `vladars.rs`/市政页确认）、BD（单一自治单位，经特区政府规划与不动产事务局 `ppipo.bdcentral.net`）。
3. **高置信物理线索 = 小型电信/政府/公用事业导向**：BH Telecom Data Centar（萨拉热窝，A，灾备+托管）、HT Eronet Data Centar（莫斯塔尔，A，地理冗余）、LANACO Technology Center/Data Center（巴尼亚卢卡，B）、Globalhost Data Center（Novi Travnik，B）；Integra Data Centar（巴尼亚卢卡）与 m:tel Virtual Data Center 为线索/服务，需地址/许可确认后才能计数。
4. **生命周期词汇分三套**：FBiH `prostorni plan < urbanistička saglasnost/lokacijska informacija < građevinska dozvola < upotrebna dozvola`；RS `prostorni plan < lokacijski uslovi < građevinska dozvola < upotrebna dozvola`；BD `prostorni plan Distrikta < građevinska dozvola < upotrebna dozvola`。
5. **语言：BCS 为主 + 西里尔变体**：`data centar`、`centar podataka`、`podatkovni centar`、`kolokacija`、`telehousing`、`server sala`/`serverska sala`、`građevinska dozvola`、`urbanistička saglasnost`、`upotrebna dozvola`、`ekološka dozvola`；RS 内容需西里尔（`центар података`、`грађевинска дозвола`）。
6. **超大规模负面检查**：AWS/Azure/GCP/OCI 官方区域表均无波黑公共区域；本地 `cloud`/`VPS`/`Virtual Data Center`/“sovereign cloud”（含 BH Telecom–AWS 2025 MoU）为本地托管/边缘服务，不构成区域证据。
7. **容量语义**：波黑来源极少公布 MW——保留披露代理量（平方米、机架数、Tier/ISO 认证、UPS/发电机/消防范围、KM/EUR 项目金额、招标范围），不得编造容量；BH Telecom 灾备地位以招标/年报取数。
8. **采购是 A 级意图/范围证据**：e-Nabavke（ejn.gov.ba）+ 集中采购 ISCN（ecjn.gov.ba）覆盖全部公共实体；区分纯设备采购与 `radovi`/`izgradnja`/`adaptacija prostora za servere` 建筑施工。
9. **FBiH 高产出城市**：萨拉热窝（BH Telecom DC）、莫斯塔尔（HT Eronet）、Novi Travnik（Globalhost）、图兹拉（大学概念）、泽尼察（钢厂提案）；RS 以巴尼亚卢卡为枢纽（m:tel/Telekom Srpske、Integra、Lanaco、RS 政府），次级 Bijeljina/Doboj/Prijedor/Istočno Sarajevo/Trebinje；BD 预期仅 0-2 内部/市政服务器机房。
10. **来源分级 A/B/C**：A=许可/监管记录/官方运营商页/政府采购/政府会议材料/云官方页；B=SeeNews/BIRN/Klix/Avaz/Nezavisne/Glas Srpske/Capital/Akta/SEEbiz/btw.media 等具名媒体；C=目录（DataCenterMap/Datacenters.com/Cloudscene/PeeringDB 作目录时）、SEO/托管页、转售商云/VPS 页、无政府行动的政治提案。

## 常用查询模板（详见 explorer-official.md §1、§2 / explorer-industry.md §1、§4）

- 官方站内：`site:rak.ba ("registar operatora" OR "data centar")`、`site:derk.ba ("data centar" OR "registar")`、`site:ejn.gov.ba "data centar"`、`site:ecjn.gov.ba "data centar"`、`site:fbihvlada.gov.ba "data centar"`、`site:fmpu.gov.ba "urbanistička saglasnost"`、`site:vladars.rs "data centar"`、`site:vladars.rs "центар података"`、`site:vlada.bdcentral.net "data centar"`。
- 许可模板：`site:{municipal-domain} "{operator}" "građevinska dozvola"`、`site:{municipal-domain} "data centar"`、`"{municipality}" "urbanistička saglasnost" "data centar"`、`"{municipality}" "upotrebna dozvola" "{operator}"`。
- 能源：`site:derk.ba "licenca" "{entity}"`、`"data centar" "trafostanica" "BiH"`、`"data centar" "priključna snaga" "BiH"`。
- 运营商：`"{operator}" BiH "data centar"`、`"{operator}" "kolokacija" BiH`、`site:{operator-domain} "data centar"`；定向串：`"BH Telecom" "Data Centar" "Sarajevo"`、`"HT Eronet" "data centar" "Mostar"`、`"Lanaco" "data centar"`、`"Globalhost" "data centar" "Novi Travnik"`。
- 西里尔：`"Република Српска" "центар података"`、`"грађевинска дозвола" "Република Српска"`。
- 变体处理：`Brčko OR Brcko`、`Istočno Sarajevo OR Istocno Sarajevo`、`Željezara OR Zeljezara`。
- 容量：`"{facility}" "MW" OR "MVA" OR "kW"`、`"{facility}" "m2" OR "kvadrata"`、`"{facility}" "Tier III" OR "ISO 27001"`、`"{facility}" "protivpožarni"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 国家级：RAK（运营商注册/牌照/市场报告，A；门户可能超时，用搜索/缓存回退）、Vijeće ministara（国家数字化决策）、IDDEEA（国家身份/CIPS 关键 IT 设施线索）、Službeni glasnik BiH（公报，另查 FBiH/RS 公报）、e-Nabavke（采购）。
- FBiH：FMPU（联邦意义项目的 urbanistička saglasnost/lokacijska informacija）、Vlada FBiH、10 州规划部委（每州自有法律与部委）、市政许可服务（萨拉热窝各市、莫斯塔尔、图兹拉、泽尼卡、比哈奇为高产出目标）。
- RS：`vladars.rs`（规划/建筑/生态部委 + 数字化部委 MNTRI）、市政 Odjeljenje、RERS（RS 电力）、e-permitting 若存活（枚举时核实）。
- BD：`vlada.bdcentral.net` + `ppipo.bdcentral.net`（规划与不动产事务局）+ e-Nabavke 签约主体；JP "Komunalno Brčko" 出现在 DERK 交易商注册。
- 能源：DERK（国家输电/交易商注册 PDF）、FERK（FBiH）、RERS（RS）、Elektroprenos/NOSBiH（输电规划上下文）、各实体 DSO（EPBiH、EPHZHB、ERS 系）——能源记录仅作选址/容量上下文，不单独推断设施。
- 环境：FBiH `okolišna dozvola`（联邦环境部 fmoit.gov.ba）+ 州级 LEK；RS `ekološka dozvola`；BD 特区环境部门。
- 云：官方区域表负面；BH Telecom–AWS sovereign cloud MoU（2025-06）为本地托管/边缘安排。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 现实产出约 8-15 条记录：少数运营商托管/数据中心站点 + 电信内部网络机房 + 公共部门内部微机房 + 少量规划/提案州级项目（RS 州数据中心、图兹拉大学、泽尼卡提案、BH Telecom 模块化 DC、BH Telecom–AWS）。
- 贸易媒体 B 级：Klix、Avaz、Nezavisne novine、Glas Srpske、Oslobođenje/FENA/Federalna、Capital.ba/Akta.ba/SEEbiz/SeeNews、BIRN、btw.media/telecomrevieweurope/capacityglobal、DCD、US trade.gov 国别指南（上下文）。
- 协会/目录：RS/FBiH 商会、Foreign Trade Chamber、BITO（C）、DataCenterMap BiH（~4 条，C）、Datacenters.com（C）、PeeringDB（C）、Cloudscene/Inflect/LinkedIn（C）。
- 集成商佐证：`"Schneider Electric" "data centar" "BiH"`、`"Vertiv" "data centar" "BiH"`、`"Rittal" OR "APC" OR "Eaton" "server sala" "BiH"`——仅作 B/C 佐证，需运营商/许可确认。
- 目录到一手验证流程：目录种子 → 运营商官网精确串 → 本地媒体 → e-Nabavke/招标 → 政府门户/数字化部委 → RAK 注册确认 → 仍仅目录则记 C 并注明缺失证明。
- 陷阱：`data centar` 可能指零售电脑店/机构机房/电信网络设施/云服务产品/真托管设施——捕获设施类型，不合并；电信交换托管 ≠ 商业托管；旧目录时代条目需一手确认。

## 来源分级

- **A** = 签发许可（州/市/特区或 FMPU）、RS 部委决定、DERK/FERK/RERS 牌照或决定、RAK 记录、官方运营商数据中心/招标页、政府会议材料或官方采购文件、云官方区域页。
- **B** = SeeNews、BIRN、Klix、Avaz、Nezavisne、Glas Srpske、Capital、Akta、SEEbiz、btw.media、telecomrevieweurope、capacityglobal、Bloomberg Adria 及具名媒体转述的公司声明。
- **C** = DataCenterMap、Datacenters.com、Cloudscene、PeeringDB（作目录）、LinkedIn、SEO/托管页、转售商云/Virtual Data Center、无政府行动的政治提案。
- **意图/范围 ≠ 运营状态**：可行性研究、MoU、政治提案为意图证据，须有许可/招标/施工/移交/开业证据方可升级；MoU（如 BH Telecom–AWS）不构成新设施。

## 维护注意（更新纪律）

- **更新节奏**：每次枚举前核实动态门户——RS e-permit 地址（`edozvola.vladars.net` 曾 DNS 失效）、RAK 可达性、市政许可 URL；季度重查云区域官方列表并记录检查日期。
- **来源验证**：FBiH 无统一 e-permit 库，市政站点多为扫描 PDF（需 OCR）/年度索引/无发布——按州预算时间；拉丁/西里尔与变音符变体全查；新旧建筑程序并存（遗留记录 `odobrenje za građenje` 不丢弃）。
- **不删除纪律（NO-DELETION）**：只创建自己的结果文件与 skill 文件；不修改/删除 explorer 源文件与其他工作产物；新证据以新增 + 分级并存方式记录，不覆盖旧证据。
