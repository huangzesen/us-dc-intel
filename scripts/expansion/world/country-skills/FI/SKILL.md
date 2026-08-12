---
name: fi-datacenter-methodology
location: scripts/expansion/world/country-skills/FI/SKILL.md
description: |
  Finland (FI) datacenter discovery & audit methodology — how to enumerate, verify, and update Finland datacenter projects at region/maakunta + municipality (kunta) granularity. Finland has no single public national datacenter permit register: construction evidence is municipal (kaavoitus/asemakaava/yleiskaava zoning, rakennusvalvonta, rakennuslupa → from 2025 rakentamislupa, council agendas, tontinluovutus/maankäyttösopimus), the highest-yield national discovery source is YVA environmental assessment on ymparisto.fi (large campuses surface via backup generation, fuel storage, substations, cooling, IT-teho/kokonaissähköteho disclosures, e.g. Espoo/Vihti/Kirkkonummi/Pyhäjoki/Kouvola-Hyperco/Järvenpää), Lupapiste/julkipano permit notices, Fingrid + DSO/district-heating (Fortum/Helen/Vantaa Energy/Lahti Energia) grid and hukkalämpö evidence, Traficom/NCSC-FI NIS2 context, cloud-region pages (Microsoft Southern Finland region announced/building; Google Hamina europe-north1; no AWS/OCI Finland region), and operator pages. Read this before running FI exploration/audit batches. Routes to explorer-official.md (municipal/YVA/grid/cloud/operator) and explorer-industry.md (FDCA/Business Finland/trade press/vendor seeds/region matrix).
---

# FI · 芬兰数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：芬兰**没有**全国公开的数据中心许可注册库；建筑证据在**市政层**（`kaavoitus`/`asemakaava`/`yleiskaava` 规划、`rakennusvalvonta` 建筑监督、`rakennuslupa`（2025 起 `rakentamislupa`）、市议会议程、`tontinluovutus`/`maankäyttösopimus`），而**全国最高产出的官方发现源是 ymparisto.fi 的 YVA 环评页**（备用发电、燃料储存、变电站、冷却、`IT-teho`/`kokonaissähköteho` 常触发评估并披露业主/市镇/区域/IT load/总电气负荷）。
> 电网证据是核心：Fingrid 主网 + 区域 DSO/市能源公司（Fortum/Helen/Vantaa Energy/Lahti Energia 等）的 `sähköasema`/`verkkoliityntä`/`hukkalämpö`/`kaukolämpö`；云区域只是 metro/区域种子（Microsoft 南芬兰区域宣布/在建，Google Hamina 官方 DC；AWS/OCI 无芬兰区域）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供芬兰探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：市政规划/建筑许可（Lupapiste/julkipano、Helsinki 实例）、YVA/ELY 环评（Espoo/Vihti/Kirkkonummi/Pyhäjoki/Kouvola-Hyperco/Järvenpää 实例与提取清单）、Fingrid 并网/主网发展计划/DSO 与供热、Traficom/NCSC-FI NIS2、云区域（Microsoft/Google/AWS/OCI）、运营商种子（Equinix/Telia/Elisa/Digita/Hetzner/Verne/atNorth/DayOne/Hyperco）、19 区路由表、记录 schema 与置信规则 |
| `explorer-industry.md` | 行业/厂商发现：FDCA/Business Finland/政府/Fingrid 语境、Ryhti/Lupapiste 流程、DCD/Data Center Forum/Yle/Rakennuslehti/Kauppalehti 等贸易与本地媒体、目录（DataCenterMap/Baxtel/PeeringDB）、运营商/开发商种子（Verne-Ficolo/Glesys/Equinix/Telia/Elisa/Google/Microsoft/AWS/OCI/Nebius/Hyperco/DayOne/Polarnode/FCDC/Pure DC/QTS/XTX/CSC/YIT/AmpTank/ASP DC/Compute Nordic 等）、逐区查询配方、云区域处理、快速验证清单 |

## 核心结构事实（框定每次搜索）

1. **无全国许可库**：以市镇为建筑许可操作单元（区域议会只管战略用地规划）；2025 建筑法词汇起 `rakennuslupa` 与 `rakentamislupa` 都要搜。
2. **YVA 是大型园区的最佳官方发现源**：`site:ymparisto.fi datakeskus "{kunta}"`；实例：Espoo 数据中心区（Microsoft 3465 Finland Oy，约 28 ha）、Vihti（约 60 ha，Nummela 附近）、Kirkkonummi（备选与备用发电机细节）、Pyhäjoki（披露 IT 功率/总电气功率/备用发电机燃料功率）、Kouvola-Hyperco（Koria）、Järvenpää；提取 `Hankkeesta vastaava`、`Hankealue`、备选（VE0/VE1/VE2）、建筑数、`IT-teho`、`kokonaissähköteho`、`varavoimageneraattorit`、燃料功率/罐容、ELY 机关、`Dnro`、状态（`vireillä`/`päättynyt`/`perusteltu päätelmä annettu`）。
3. **市政规划先于建筑许可**：搜 `datakeskus`/`konesali`/`palvelinkeskus`/`pilvipalvelukeskus` + `asemakaava`/`kaavamuutos`/`tontinluovutus`/`maankäyttösopimus`/`rakentamislupa`；Lupapiste 公共公示（`julkipano.lupapiste.fi`）可见许可通知/决定（`LP-...` ID）。
4. **电网/余热是交叉核对**：Fingrid 并网阶段/Grid Scope 地图/主网发展计划 2026-2035（A）；按地区 DSO 与市能源公司（Uusimaa: Fortum/Helen/Vantaan Energia/Caruna；Päijät-Häme: Lahti Energia；Kymenlaakso: KSS/Haminan Energia；Pirkanmaa: Tampereen Energia/Elenia）；50 MW+ 站点必须搜 `hukkalämpö`/`kaukolämpö`/`sähköasema`/`110 kV`/MVA。
5. **云区域=区域种子（A），非设施地址**：Microsoft 宣布/建设南芬兰数据中心区域（Espoo/Kirkkonummi/Vihti，Fortum 余热伙伴）；Google 官方 Hamina 园区 + GCP `europe-north1`；AWS 官方表无芬兰区域（Helsinki 仅 Local Zone/边缘）；OCI 无芬兰公共区域。
6. **Traficom/NCSC-FI（A，语境）**：NIS2/Cybersecurity Act（2025-04-08 生效）下数字基础设施监督与实体登记义务、电信运营商登记——用于法律名称/运营商联系/关键基础设施语境，不作设施地址推断。
7. **主集群**：Uusimaa（Microsoft 三镇 + Equinix HE1-HE7/Telia HDC Valimotie 15,000 m2/24 MW/Digita Pasila/Hetzner Tuusula/Nebius Mäntsälä 75 MW）、Kymenlaakso（Google Hamina + Hyperco/TikTok Koria + DayOne Kouvola）、Päijät-Häme（DayOne Lahti Kiveriö）、Pohjois-Pohjanmaa（Glesys/Trevian Oulu 至 300 MW、AmpTank Utajärvi 100 MW、Pyhäjoki YVA、Google Muhos 购地）、Kainuu（XTX Kajaani、CSC/LUMI）、Ostrobothnia（FCDC Vaasa Kuriiritie 已批、Microsoft Vaasa/Mustasaari 初购）、South Karelia（Nebius Lappeenranta Pajarila 310 MW）、Kanta-Häme（QTS Forssa 150 ha）、Satakunta（ASP DC Pori 300-400 MW）、South Savo（Mikkeli 集群）。
8. **容量语义**：`IT-teho`（IT load）≠ `kokonaissähköteho`（总电气）≠ 备用发电机燃料功率 ≠ 园区营销 MW；DayOne 芬兰平台 281 MW 跨 Lahti/Kouvola、Verne/Ficolo/Glesys 在 Tampere/Pori 易主、Hyperco Koria/TikTok 与 DayOne Kouvola 可能指相邻阶段——去重注意。

## 查询模式（复制粘贴模板见 explorer-official.md §1 / explorer-industry.md §2）

- 芬语核心词：`datakeskus` `konesali` `palvelinkeskus` `pilvipalvelukeskus` `tekoälydatakeskus` `tekoälytehdas` `kolokaatio` `rakennuslupa` `rakentamislupa` `rakennusvalvonta` `kaavoitus` `asemakaava` `kaavamuutos` `tonttivaraus` `maanvuokrasopimus` `kiinteistökauppa` `YVA` `ympäristölupa` `varavoimageneraattori` `polttoaineteho` `sähköasema` `muuntamo` `verkkoliityntä` `kantaverkko` `110 kV` `400 kV` `hukkalämpö` `kaukolämpö` `liittymisteho` `generaattori`。
- 规划/许可：`"{kunta}" "datakeskus" "asemakaava"`、`"{kunta}" "datakeskus" "rakennuslupa"`、`"{kunta}" "datakeskus" "rakentamislupa"`、`site:{municipality-domain} datakeskus asemakaava`、`site:{municipality-domain} datakeskus rakennuslupa`、`filetype:pdf "datakeskus" "asemakaavan selostus"`、`site:julkipano.lupapiste.fi datakeskus`。
- YVA：`site:ymparisto.fi datakeskus "{kunta}"`、`site:ymparisto.fi "YVA" "datakeskus"`、`site:ymparisto.fi "IT-teho" "datakeskus"`、`site:ymparisto.fi "kokonaissähköteho"`、`"{operator}" "datakeskus" "YVA"`、`"{kunta}" "datakeskus" "ympäristölupa"`。
- 电网：`"{kunta}" "datakeskus" "sähköasema"`、`"{kunta}" "datakeskus" "verkkoliityntä"`、`"{kunta}" "datakeskus" "110 kV" OR "400 kV"`、`"{operator}" "{kunta}" "hukkalämpö" OR "kaukolämpö"`、`site:fingrid.fi datakeskus`、`site:{dso-domain} datakeskus sähköasema`。
- 英文/瑞典语：`"Finland" "data center" "building permit"`、`"Southern Finland" Microsoft datacenter region`、`"Hamina" Google data center`；双语市镇用 `datacenter`/`serverhall`/`bygglov`/`detaljplan`/`miljökonsekvensbedömning`/`fjärrvärme`。
- 行业：`site:datacenterdynamics.com Finland "data center" {operator}`、`site:yle.fi datakeskus {kunta|operator}`、`site:rakennuslehti.fi datakeskus rakennuslupa`、`site:fdca.fi datakeskus`、`site:businessfinland.fi "data center" Finland`、`site:datacentermap.com/finland {city}`。
- 风险/取消：`"{project}" (valitus OR peruttu OR keskeytetty OR rauennut OR hylätty OR hallinto-oikeus)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **市政（A）**：Lupapiste/julkipano、Helsinki/Espoo/Kirkkonummi/Vihti 实例（Microsoft Hepokorpi 购地+规划生效、Kirkkonummi 两期 `rakentamislupa` 与 `aloittamisoikeus`、`meluilmoitus`）；提取 `LP-...` ID、法律实体/SPV、地块、`asemakaava` 生效日期、建筑数/面积/备用电源/燃料罐、`aloittamisoikeus` 决定、供热伙伴。
- **YVA/ELY（A）**：ymparisto.fi YVA 页 + 按 ELY 区域的 YVA 决定页（Etelä-Pohjanmaa/Keski-Pohjanmaa/Pohjanmaa 等）；大型园区最先在此出现。
- **电网（A）**：Fingrid 并网阶段/Grid Scope/主网发展计划 2026-2035/新闻；Energiavirasto 能源监管；Metsähallitus 国家土地/选址路线图（A-/B+）；政府吸引数据中心措施（A 政策）。
- **Traficom/NCSC-FI（A，语境）**：NIS2 监督页/实体登记/网络安全法新闻/电信运营商登记。
- **贸易/协会**：FDCA（B+/A-，成员生态）、Business Finland 数据中心地图（A-/B+，种子清单）、DCD（B）、Data Center Forum（B-/C+）、Yle（B）、Rakennuslehti（B-/C+）、Kauppalehti/Talouselämä/Tekniikka&Talous（C+/B-）、市经济发展机构（Business Pori/Miksei Mikkeli/Invest in Kainuu/GigaVaasa，A/B 当市属）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商/开发商种子（A=存在/B=容量）**：Equinix（芬兰五家，约 7,750 m2，HE1-HE7）、Telia HDC（Valimotie 3-5，15,000 m2/24 MW IT）、Elisa（Espoo/Turku-Raisio）、Digita（Pasila）、Hetzner Finland（Tuusula）、Verne/Ficolo 遗留（The Air/The Rock，Tampere/Pori 已售 Glesys）、Glesys（Tampere/Pori）、atNorth（FIN02/FIN04 系）、Google（Hamina 园区，Kajaani/Muhos/Vaala 购地线索）、Microsoft（南芬兰区域，Espoo/Kirkkonummi/Vihti + Vaasa/Mustasaari 潜在）、Nebius（Mäntsälä 75 MW → Lappeenranta 310 MW AI factory）、Hyperco（Kouvola Koria/TikTok，Vilppulantie 96）、DayOne（Lahti Kiveriö + Kouvola，281 MW）、Polarnode（Lappeenranta/Kuopio/Heinola/Pori/Nokia/Keminmaa 多项目）、FCDC Corp（Vaasa Kuriiritie 已批、Lahti/Valkeakoski/Rovaniemi）、Pure DC/SDC（Seinäjoki SJK01）、QTS/Blackstone（Forssa 150 ha）、XTX Markets（Kajaani 10 亿+ 欧元）、CSC（Kajaani LUMI/LUMI-AI，公共 HPC 单独枚举）、YIT（Kuopio Hepomäki/Kontiolahti/Liminka 开发）、AmpTank（Utajärvi 100 MW + 电池）、ASP DC（Pori 300-400 MW）、Compute Nordic/Regant/Aurora Core/Orka（Mikkeli Visulahti/Pellos/EcoSairila）。
- **目录（C+ 种子）**：DataCenterMap、Baxtel、Datacenters.com/DC Atlas/Cloudscene/Inflect、PeeringDB（B/C 活跃互连）。
- **状态语义（芬语）**：`tonttivaraus`/`aiesopimus`/`esisopimus`/`suunnittelee`=意向；`kaavoitus`/`asemakaava`/`OAS`/`kaavaluonnos`/`kaavaehdotus`=规划中；`hyväksytty asemakaava`/`lainvoimainen`=规划已批未建；`rakennuslupa`/`rakentamislupa`/`lupapäätös`/`aloittamisoikeus`=已许可/在建启动；`maanrakennustyöt alkavat`/`louhinta`/`rakentaminen alkaa`/`harjannostajaiset`=在建；`käyttöönotto`/`toiminnassa`/运营商页上线=运营；`valitus`/`peruttu`/`keskeytetty`/`rauennut`/`hylätty`=上诉/取消。

## 来源分级

- **A** = 官方/一手：市政许可/决定、`ymparisto.fi` YVA、Fingrid/政府/监管页、运营商官方设施页（存在/位置）、官方云区域/社区页（Microsoft Local/Google datacenters）。
- **B** = 强二级：FDCA/Business Finland 地图、点名运营商/地点的可信贸易媒体、带位置/容量的承包商案例、市经济发展机构（市属时 A/B）。
- **C** = 弱/聚合：目录、市场报告片段、LinkedIn/社交、无出处博客；云区域/AZ 不映射物理设施；电网队列/能源站点营销/Business Finland 土地清单不作项目。
- **容量规则**：优先运营商/市镇 MW；区分 IT load 与电网/电气功率；50 MW+ 须电力/供热交叉核对；目录 MW 与推断园区总量默认 C。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=FI，divisions=区域/市镇）。
2. 建种子：运营商官方页（Equinix/Telia/Elisa/Google/Microsoft/Nebius/Hyperco/DayOne/Polarnode/FCDC/Pure DC/QTS/XTX/ASP DC）+ YVA 搜索（`site:ymparisto.fi datakeskus`）+ FDCA/Business Finland。
3. 对每个区域：先 `site:ymparisto.fi datakeskus "{maakunta}"`，再最大市镇，再本地能源/电网名；跑三遍：①运营商/开发商种子 ②市政项目/会议（kaavoitus/rakennuslupa/rakentamislupa/tonttivaraus）③电网/供热（Fingrid/DSO/hukkalämpö/kaukolämpö/sähköasema）。
4. 对每个命中捕获：项目/设施名、运营商/申请人/SPV、来源类型（运营商页/市政规划/建筑许可/YVA/电网/Traficom/贸易媒体）、状态（operating/under construction/permitted/zoning approved/YVA/announced）、日期、容量字段（IT MW/总电气 MW-MVA/备用燃料 MW/建筑数/公顷/毛面积）、电力/供热字段（变电站/电压/DSO-TSO/供热伙伴）。
5. 去重：Microsoft 南芬兰区域跨 Espoo/Kirkkonummi/Vihti；DayOne 平台跨 Lahti/Kouvola；Verne/Ficolo/Glesys 所有权变更（Tampere/Pori）；Hyperco Koria 与 DayOne Kouvola 相邻阶段；云区域 ≠ 多设施。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核芬兰数据中心（区域/市镇粒度，Uusimaa/Kymenlaakso/Päijät-Häme 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Microsoft 南芬兰区域各镇（Espoo/Kirkkonummi/Vihti）许可进度、Nebius Lappeenranta Pajarila 310 MW 建设、Google Hamina 扩建与 Muhos/Vaala/Kajaani 购地、Hyperco Koria 二期、DayOne Lahti Kiveriö 完工、QTS Forssa 许可、ASP DC Pori、XTX Kajaani 一期、Pure DC Seinäjoki SJK01、FCDC Vaasa 与 Microsoft Vaasa/Mustasaari 后续。
