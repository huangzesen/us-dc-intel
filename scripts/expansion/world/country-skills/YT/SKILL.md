---
name: yt-datacenter-methodology
location: scripts/expansion/world/country-skills/YT/SKILL.md
description: 马约特数据中心查询方法论：唯一 Mayotte 分区，ITH Center 为已确认运营的本地 colocation 数据中心（Tier III claim 非 certified），海缆/IXP/电力仅作连接与背景，容量冲突保留多来源口径。Mayotte datacenter methodology: single Mayotte division, ITH Center confirmed operating local colocation DC (Tier III claim not certified), cable/IXP/power are connectivity and context only, capacity conflicts keep multi-source figures.
---

# YT · 马约特数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对马约特（Mayotte, YT）数据中心设施证据的发现、核实、分级与多来源冲突处理。官方线覆盖法律/行政公报、公共采购与发展金融（AFD/CDC）、电信监管（ARCEP/运营商）、认证与云区域负向、电力/能源/环境（EDM/CRE/DEAL）、海缆登陆站；行业线覆盖运营商/连接基础设施/贸易媒体/目录到一手的工作流与分区查询模式。核心事实以双语标注，容量与 Tier 主张按来源口径分别保存。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | Préfecture/RAA/Légifrance/CNIL/DEALM/Géorisques、AFD ITH 项目/Banque des Territoires/BOAMP/PLACE、ARCEP/Orange/SRR/Telco OI/RENATERIX、Uptime/TIA/EPI + 云区域负向、EDM/CRE/EDF SEI、LION2/FLY-LION3/Avassa |
| explorer-industry.md | 行业/厂商/媒体发现 | ITH Center/MAYOTIX 优先扫描、运营商（Orange/SRR/Telco OI/Mayotte One）、目录到一手工作流、媒体（Mayotte Hebdo/Le Journal/La 1ère/Linfo.re）、容量/可靠性/命名规则、分区查询模式 |

## 核心结构事实

1. **行政区划模型**：manifest 确认 `{"country_code":"YT","country_name":"Mayotte","subnational_type":"country","divisions":["Mayotte"]}`——仅 **1 个分区 Division: Mayotte**；任何记录的 `division` 必须写 Mayotte，Mamoudzou、Kaweni、Koungou 等仅作市镇/片区字段。
2. **注册库现状**：马约特并非“无公开数据中心”。本轮核实到 **ITH Center / Information Technology Hosting SAS** 是公开运营的本地 colocation / housing 数据中心，位于 Mamoudzou / Kaweni（Zone Industrielle de Kawéni）。除此外未确认其他 carrier-neutral 或 hyperscale 数据中心。
3. **法律与监管**：适用法国监管链——Préfecture de Mayotte（`mayotte.gouv.fr`）+ RAA、Légifrance、CNIL、DEALM（`mayotte.developpement-durable.gouv.fr`，不是 deal-mayotte 域）、Géorisques/ICPE；电信监管为法国 ARCEP；不存在独立的 Mayotte regulator，不要寻找。运营商以 ARCEP 2025-04-17 3.4-3.8 GHz 牌照为准：**Orange、SRR、Telco OI**（各 120 MHz、15 年）；2024 tender 出现 **Mayotte One** 可记录为监管申请/候选线索；目录中的 “Free Mayotte / Telma Mayotte” 未获 ARCEP 确认，应降级为噪声，除非有 ARCEP 或公司官方证据。
4. **互联与云**：RENATER 官方确认 **MAYOTIX** 是 Mayotte 的 GIX/IXP，hosted in Mamoudzou on the Vice-Rectorate premises——交换点/PoP，不是默认数据中心。海缆：**LION2**（不是 FLY-LION2）连接 LION 至 Mayotte 与 Mombasa，Mayotte landing 历史上报在 Kaweni/Mamoudzou；**FLY-LION3** 官方 Orange 页确认 Moroni 与 Mamoudzou 之间 400 km cable、landing stations at Kaweni (Mamoudzou) 和 Moroni、consortium Orange/SRR/Comores Câbles、planned service Q3 2019、capacity 4 Tbps；**Avassa** Huawei Marine/Hengtong 交付新闻确认 Comoros Telecom 与 Mayotte-based carrier STOI 于 2016 签约、260 km 系统连接 Grande Comore、Anjouan 与 Mayotte。海缆容量不等于数据中心容量。AWS/Azure/GCP/OCI 官方区域页无 Mayotte region/local zone（A 级负向）；本地主机或 cloud resale 不等于 hyperscale region。
5. **设施/项目种子**：ITH Center / Information Technology Hosting SAS（Mayotte — Mamoudzou / Kaweni，运营中 colocation/housing data center，inaugurated 2022-10-21；AFD 项目页确认 “construction et exploitation du premier data center de Mayotte”、受益方 ITH Center、Mamoudzou、AFD 融资 3,000,000 EUR、项目起始 2020-11-06、容量 **420 kW / 76 baies informatiques / 2 suites privées de 8 baies**；ITH 官方页 `ith.yt` 自称 “1er Datacenter Tier III Neutre dédié à la colocation de la région”、自 2022 提供服务、口径 80 baies；Banque des Territoires PDF 确认 ITH SAS 运营、总投资近 10M EUR、BT 1.3M EUR fonds propres、AFD 与 Crédit Agricole Réunion-Mayotte 合计 7.5M EUR loans/bridge；DataCenterMap 列 0.65 MW / 350 sq.m. / 地址 629 Bd. Younoussa Bamana, BP 376, 97600 Mamoudzou，C 级补充）。MAYOTIX（Mamoudzou，Vice-Rectorate premises，A IXP 非 DC）；LION2/FLY-LION3/Avassa landing（Kaweni/Mamoudzou，A/B 连接设施非 DC）；Orange/SRR/Telco OI network rooms（A 运营商频谱事实；C 设施线索）；EDM control/SCADA rooms 与 Longoni 电厂（Koungou/Longoni，A 电力事实；不是 DC）；政府/医院/市政托管采购（客户/用例线索，A if BOAMP/PLACE 或官方采购；无地址/运营商则不建设施）；AWS/Azure/GCP/OCI local region（负向，A）；Uptime/TIA/EPI certified facility（ITH 证书 ID 未核实，A 负向当登记检索过）。
6. **语言与词汇**：中文为主、英文补充；法语关键词：`centre de données`、`data center`、`salle des serveurs`、`salle serveur`、`salle informatique`、`hébergement de données`、`hébergeur`、`colocation`、`baie informatique`、`station d'atterrissement`、`câble sous-marin`、`point de présence`、`permis de construire`、`ICPE`、`appel d'offres`、`marché public`、`groupe électrogène`、`onduleur`、`PUE`；本地变体：Mahoré/Mahorais/Mahoraise、976、Grande-Terre、Petite-Terre、Kawéni/Kaweni、Dzaoudzi、Pamandzi；状态词：operational / inaugurated / in service since 2022 / planned / under construction / negative。
7. **可靠性分级**：A=官方/一手来源直接证明具体主张（政府、监管机构、公共开发金融机构、运营方官网、采购公告、认证登记、海缆财团或云厂商官方页）；B=具名当事方、日期、地点的可靠媒体/行业媒体；C=目录站、聚合页、SEO 主机页、社交帖、无地址或无设施证据的说法。媒体转述官方表态不得自动升级为 A；需同时保存被转述的一手 URL。
8. **计数与去重规则**：ITH Center 是已确认运营设施（A for existence/location/operator/financing/capacity from AFD/ITH/CDC；Tier certification 未独立核实）；Tier III 只写 `tier_claim: "Tier III / conception Tier III"`，不得写 `certified Tier III`，除非 Uptime/TIA/EPI 登记给出证书 ID；容量冲突保留来源口径——`capacity_mw` 用 AFD 的 **0.42 MW**（除非更强业主技术文件覆盖），DataCenterMap 0.65 MW 存为 `capacity_mw_alt_c` 或 note-only；`bays` 同时保存 AFD 76 bays + 2 suites 与 ITH 80 bays；海缆带宽（LION2/FLY-LION3/Avassa）、EDM 电厂容量或电网文件、采购金额或融资额、未登记的 Tier 表述均不得推导容量；海缆与 IXP 不是 DC（LION2/FLY-LION3/Avassa/MAYOTIX 都是连接设施/PoP 线索，只有出现服务器托管/colo/机房运营证据才可升级）；运营商名单以 ARCEP 为准；Free/Telma 目录说法降级为噪声；发电机、UPS、冷却、PUE、ICPE 能佐证设施属性，但单独的电力设施不等于 DC；不要重复草稿错误——Mayotte 已有公开 ITH Center，不能再写“未确认任何公开数据中心”；LION2 不是 FLY-LION2。

## 常用查询模板

```text
site:mayotte.gouv.fr/Publications/Recueil-des-actes-administratifs "ITH"
site:mayotte.gouv.fr/Publications/Recueil-des-actes-administratifs "Information Technology Hosting"
site:mayotte.gouv.fr Mayotte ("centre de données" OR "data center" OR datacenter OR "salle informatique")
site:mayotte.developpement-durable.gouv.fr Mayotte (ICPE OR "permis de construire" OR "étude d'impact") ("centre de données" OR "groupe électrogène" OR onduleur)
site:georisques.gouv.fr Mayotte ITH
site:legifrance.gouv.fr Mayotte ("communications électroniques" OR "zone non interconnectée" OR "commande publique")
site:cnil.fr Mayotte (hébergeur OR "hébergement de données" OR ITH)
site:afd.fr Mayotte ("data center" OR datacenter OR "centre de données" OR ITH)
site:banquedesterritoires.fr Mayotte ITH datacenter
site:boamp.fr Mayotte ("hébergement" OR "colocation" OR "centre de données" OR "salle informatique" OR infogérance)
site:placee.marches-publics.gouv.fr Mayotte ("hébergement" OR "sauvegarde" OR "plan de reprise" OR "centre de données")
site:mayotte.fr ("marchés publics" OR "appel d'offres") (informatique OR hébergement OR télécommunications)
site:annuaire-entreprises.data.gouv.fr "Information Technology Hosting"
site:annuaire-entreprises.data.gouv.fr "ITH Center"
Mayotte "6311Z" "annuaire-entreprises.data.gouv.fr"
site:arcep.fr Mayotte (Orange OR SRR OR "Telco OI" OR "Mayotte One") fréquences
site:arcep.fr Mayotte ("observatoire" OR "marché mobile" OR "réseaux fixes" OR "très haut débit")
site:mayotte.orange.fr Mayotte ("centre de données" OR "hébergement" OR cloud OR "salle serveur")
site:only.yt Mayotte ("centre de données" OR hébergement OR réseau OR "station d'atterrissement")
site:telco.re Mayotte ("centre de données" OR hébergement OR réseau OR "station d'atterrissement")
site:renater.fr MAYOTIX Mayotte Mamoudzou
site:uptimeinstitute.com/uptime-institute-awards Mayotte
site:uptimeinstitute.com/uptime-institute-awards "ITH Center"
site:uptimeinstitute.com/uptime-institute-awards "Information Technology Hosting"
site:epi-certification.com/sites/list Mayotte
site:epi-certification.com/sites/list "ITH"
"ITH Center" ("Uptime Institute" OR "TIA-942" OR certification)
"Mayotte" ("AWS Region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "local zone")
site:electricitedemayotte.com Mayotte (Longoni OR centrale OR réseau OR "appel d'offres" OR MVA OR kVA)
site:cre.fr Mayotte ZNI (PPE OR tarif OR capacité OR qualité)
site:mayotte.developpement-durable.gouv.fr Mayotte (ICPE OR "groupe électrogène" OR "stockage d'énergie")
"ITH Center" Mayotte (énergie OR "groupe électrogène" OR onduleur OR PUE OR "420 kW")
("LION2" OR "LION 2") Mayotte Kaweni landing station Orange
"FLY-LION3" Mayotte Kaweni Mamoudzou Orange SRR "Comores Câbles"
"Avassa" Mayotte STOI "Comoros Telecom" Huawei
Mayotte "câble sous-marin" (résilience OR redondance OR Chido OR nouveau)
("Mayotte" OR "976" OR "{commune}") ("centre de données" OR "data center" OR datacenter OR "salle de serveurs" OR "salle informatique")
("Mayotte" OR "{commune}") ("hébergement" OR "colocation" OR "baie informatique" OR "plan de reprise" OR "sauvegarde")
("Mayotte" OR "{commune}") ("station d'atterrissement" OR "câble sous-marin" OR backbone OR NOC OR "point de présence")
site:boamp.fr Mayotte "{commune}" (informatique OR télécommunications OR hébergement OR infogérance)
site:mayotte.gouv.fr "{commune}" (numérique OR informatique OR câble OR marché)
site:mayotte.developpement-durable.gouv.fr "{commune}" (ICPE OR "permis de construire" OR "groupe électrogène")
"ITH Center" Mayotte ("colocation" OR housing OR "centre de données" OR datacenter OR "baies")
"Information Technology Hosting" Mayotte ("data center" OR "centre de données" OR AFD OR "Banque des Territoires")
"629 Bd. Younoussa Bamana" OR "Zone Industrielle de Kawéni" "ITH"
"Orange Mayotte" ("centre de données" OR "hébergement" OR cloud OR "salle serveur" OR NOC)
("SRR" OR "SFR Mayotte" OR "Telco OI" OR Only) Mayotte ("centre de données" OR "hébergement" OR "station d'atterrissement" OR NOC)
"Mayotte One" ARCEP Mayotte fréquences
site:mayottehebdo.com "ITH Center"
site:mayottehebdo.com Mayotte (datacenter OR "centre de données")
site:lejournaldemayotte.yt Mayotte ("data center" OR "centre de données" OR ITH OR numérique)
site:la1ere.francetvinfo.fr/mayotte/ ("ITH" OR "datacenter" OR "centre de données" OR "câble sous-marin")
site:linfo.re Mayotte (Orange OR SFR OR Only OR "câble sous-marin" OR "centre de données")
site:datacenterdynamics.com Mayotte
site:datacenterdynamics.com "ITH Center"
site:submarinenetworks.com Mayotte ("LION2" OR "FLY-LION3" OR Avassa)
"Mayotte" ("Uptime Institute" OR "TIA-942" OR "Tier III certified" OR "Tier 3 certified") "ITH"
site:baxtel.com Mayotte
site:cloudscene.com Mayotte "data center"
site:peeringdb.com "MAYOTIX"
site:peeringdb.com "ITH Center"
"Mayotte" ("AWS" OR Azure OR "Google Cloud" OR OCI OR "local zone" OR "edge location")
"Mayotte" ("cloud hosting" OR "dedicated server" OR VPS) -travel -SIM
("Mayotte" OR Mahoré OR "976") ("ITH Center" OR "Information Technology Hosting" OR "centre de données" OR datacenter OR colocation)
(Mamoudzou OR Kaweni OR Kawéni) ("ITH" OR "data center" OR "centre de données" OR "baies" OR "hébergement")
(Mamoudzou OR Kaweni) ("station d'atterrissement" OR "câble sous-marin" OR LION2 OR "FLY-LION3" OR Avassa)
(Koungou OR Longoni) (centrale OR EDM OR port OR "groupe électrogène" OR ICPE)
(Dzaoudzi OR Pamandzi) (télécom OR serveur OR aéroport OR informatique)
```

## 官方/监管管线要点（详见 explorer-official.md）

- 法律/行政公报/规划许可一手入口：Préfecture de Mayotte（`mayotte.gouv.fr`）、RAA、Légifrance、CNIL、DEALM（`mayotte.developpement-durable.gouv.fr`）、Géorisques/ICPE；提取字段：文本号/日期、发布机关、地址或市镇、主体 SIREN/SIRET、许可/决定类型、是否涉及机房/发电/冷却/燃料、原文 URL/PDF。
- 公共采购与发展金融：AFD ITH 项目页、Banque des Territoires/Caisse des Dépôts、BOAMP、PLACE、Département de Mayotte（`mayotte.fr` Marchés publics）、data.gouv.fr、Annuaire des Entreprises；AFD/CDC/ITH 官方资料可确认 ITH Center 存在、位置、融资、容量口径、运营状态；BOAMP/PLACE 采购公告可证明客户采购托管、备份、PRA/PCA、机房维护或网络互联需求，不得仅凭 “hébergement web” 推断物理 DC；企业登记确认法人/地址/APE，不等同于设施运营，除非公司名与设施证据对齐。
- 电信监管与运营商：ARCEP、ARCEP 2025 Mayotte 3.4-3.8 GHz PDF、Orange Mayotte（`mayotte.orange.fr/portail/`）、SRR/SFR Mayotte / Altice Outremer（经 ARCEP 与官方页核验）、Telco OI / Only（`only.yt`、`telco.re`）、RENATERIX/MAYOTIX；当前监管事实最低名单为 Orange, SRR, Telco OI；Mayotte One 记录为监管申请/候选线索，需进一步确认是否商用；Free/Telma 未获 ARCEP 确认不进入已核实运营商名单；MAYOTIX 是 IXP/PoP 线索，记录为 connectivity facility，不作 DC。
- 数据中心认证与云区域控制：Uptime Institute awards、TIA-942 certified / EPI list、四大云官方区域页；无登记证书只能写 `claimed/conception Tier III`，不得写 `certified Tier III`；云厂商区域页无 Mayotte 是 A 级负向事实；本地主机或 cloud resale 不等于 hyperscale region。
- 电力、能源、环境：EDM 官方（`electricitedemayotte.com`）、在线门户（`espace-client.edm.yt`）、CRE、EDF SEI、DEALM/Géorisques；电力/ICPE 记录可佐证 ITH 或其他设施的备用电源、冷却、燃料存储、许可状态；Longoni 电厂、EDM 控制中心、SCADA 机房是电力基础设施线索，没有托管/服务器/地址证据前不计为数据中心。
- 海缆登陆站：LION2（连接设施，不要写 FLY-LION2，非 DC）；FLY-LION3（400 km Moroni-Mamoudzou、Kaweni 和 Moroni landing、Orange/SRR/Comores Câbles、planned service Q3 2019、4 Tbps，连接设施，Kaweni 是 ITH/telecom proximity lead）；Avassa（260 km Comoros-Mayotte、Comoros Telecom + STOI、2016 交付，连接设施非 DC）。
- 分区覆盖流程：清单分区只有 Mayotte；执行枚举时将全岛拆成市镇/片区，确保每个区域都有“已核实项目/线索/未发现”的结果——Mamoudzou/Kaweni（高，确认 ITH Center，Kaweni 另有 LION2/FLY-LION3 landing leads，MAYOTIX hosted in Mamoudzou）、Koungou/Longoni（中，电力/港口线索，未发现公开 DC）、Dzaoudzi/Pamandzi（中低，电信/机场机房线索，未发现公开 DC）、其余 13 个市镇（低，未发现公开 DC，逐次刷新采购与规划记录）。
- 陷阱与决策规则：不要重复草稿错误（Mayotte 已有公开 ITH Center，不能写“未确认任何公开数据中心”；LION2 不是 FLY-LION2）；Tier III 诚实写法（claim/conception 支持，证书 ID 前不写 certified）；容量冲突保留来源口径（AFD 420 kW/76 bays A 级项目资料、ITH 官网 80 bays A 级运营方资料、DataCenterMap 0.65 MW C 级目录补充）；海缆与 IXP 不是 DC；运营商名单以 ARCEP 为准；法国海外省监管链（Légifrance/Préfecture RAA/ARCEP/CRE/DEAL/BOAMP/PLACE），不要寻找独立 Mayotte regulator；公共采购高价值（BOAMP/PLACE 的 hosting/sauvegarde/PRA/PCA/colocation/salle informatique 公告可能揭示 ITH 客户、政府机房迁移或新项目）；电力证据的边界（发电机、UPS、冷却、PUE、ICPE 佐证设施属性，单独电力设施不等于 DC）；刷新项（ITH 官方、AFD/CDC、Uptime/TIA/EPI、云区域、ARCEP、BOAMP/PLACE、DEAL/Géorisques、Mayotte 2024-2026 气旋恢复/海缆韧性新闻）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态与已核实事实：ITH Center / Information Technology Hosting SAS 是马约特公开 colocation/housing 数据中心（Mamoudzou, Zone Industrielle de Kawéni）；ITH 官方页自称 “1er Datacenter Tier III Neutre dédié à la colocation de la région”，自 2022 提供服务，容量口径 80 bays；AFD 项目页确认 420 kW、76 bays、2 private suites、2022-10-21 inaugurated；Banque des Territoires PDF 确认 ITH SAS 运营和约 10M EUR 总投资；认证状态：Tier III 是业主/项目/金融机构描述，本轮未在 Uptime/TIA/EPI 登记核实证书 ID，记录为 claimed/conception Tier III；目录交叉验证：DataCenterMap 现列 Mayotte/Mamoudzou 1 facility（ITH Center，629 Bd. Younoussa Bamana, BP 376, 97600 Mamoudzou，0.65 MW，350 sq.m.，2022），C 级，可用于地址/容量差异提示但不能覆盖一手资料；MAYOTIX 是交换点/PoP 不是 colocation DC；运营商 ARCEP 2025-04-17 确认 Orange、SRR、Telco OI（Telco OI uses Only brand）；Mayotte One 为候选/申请线索；Free Mayotte/Telma Mayotte 不足以作为已核实本地 MNO 事实；LION2/FLY-LION3/Avassa 是主要连接链，海缆容量不等于数据中心容量；AWS/Azure/GCP/OCI 官方区域页无 Mayotte region/local zone。
- 优先设施与基础设施扫描：ITH Center（A confirmed facility，捕获运营商、地址、2022 inauguration/service、420 kW/76 bays vs 80 bays 差异、claimed Tier III）；MAYOTIX（A IXP 非 DC，作 connectivity/PoP lead）；Orange Mayotte（A 运营商事实，仅 C/B DC lead 除非设施证据）；SRR/SFR Mayotte（A 运营商事实，cable/PoP lead）；Telco OI/Only（A 运营商事实，PoP lead）；Mayotte One（仅监管申请/候选，不当作运营 DC）；LION2/FLY-LION3/Avassa（连接设施非 DC）；EDM/Longoni 电力基础设施（电力背景，无 ICT/hosting 证据不是 DC）；政府/医院/市政/银行客户（AFD customer list、Mayotte Hebdo、BOAMP/PLACE、IEDOM——需求与客户信号，设施仅在地址/运营商证据时成立）。
- 行业与媒体来源：ITH Center（A for self-described facility facts；认证主张仍需登记）、AFD（A）、Banque des Territoires/Caisse des Dépôts（A）、DataCenterMap（C 除非与 A 匹配）、RENATER（A）、ARCEP（A）、Orange Mayotte（A for operator/service pages）、Only/Telco OI（A for own service facts）、Submarine Networks/TeleGeography（B/B+，优先 Orange/Huawei/consortium 页 A）、Huawei Marine/Hengtong（A/B for vendor delivery fact）、Mayotte Hebdo（B）、Le Journal de Mayotte（B）、Mayotte la 1ère（B）、Linfo.re/Clicanoo/Imaz Press（B，Réunion/Mayotte telecom 与 cable 覆盖）、BOAMP/PLACE（A）、Uptime/TIA/EPI（A）、AWS/Azure/GCP/OCI（A）。
- 目录到一手的工作流：从目录/平台获取种子（DataCenterMap、Baxtel、Cloudscene、datacenters.com、PeeringDB、IXP lists、AFNIC registrar lists、主机商页面；当前关键目录种子是 ITH Center，MAYOTIX 作 IXP 种子）→ 对每个种子回查一手来源（ITH/AFD/CDC/ARCEP/RENATER/BOAMP/PLACE/DEAL/Géorisques/Annuaire Entreprises）→ 拆分事实字段（facility_exists、operator、address、status、service、capacity_mw、bays、tier_claim、tier_certified、source_grade）→ 对冲突字段保留多来源（AFD 0.42 MW/76 bays 与 ITH 80 bays 同时保留；DataCenterMap 0.65 MW only C）→ 仅当名称、地址、运营方和服务证明都对齐时合并记录，否则保留为 separate lead。
- 分区查询模式：division 统一 Mayotte（country_code YT，subnational_type country）；Mamoudzou/Kaweni 最高优先（ITH Center、LION2/FLY-LION3 landing、operator PoPs、行政/医院客户）；Mamoudzou/Vice-Rectorate 只有 MAYOTIX（IXP/PoP only）；Koungou/Longoni 电力/港口背景（无新证据则无 DC）；Dzaoudzi/Pamandzi 机场/旧行政中心电信机房（低置信设施线索）；其余市镇（Dembéni、Ouangani、Sada、Chirongui、Bandrélé、Acoua、M'tsangamouji、Mtsamboro、Bandraboua、Tsingoni、Chiconi、Bouéni、Kani-Kéli）标记 no public DC，除非采购/许可证据浮现。
- 容量、可靠性与命名规则：`capacity_mw` 用 AFD 的 0.42（来源 AFD），除非更强业主技术文件覆盖；DataCenterMap 0.65 MW 存为 `capacity_mw_alt_c: 0.65` 或 note-only；`bays` 同时保存 76 bays + 2 private suites（AFD）与 80 bays（ITH）；`tier_certified: null` 除非登记给证书；`tier_claim: Tier III / conception Tier III`（ITH/AFD/CDC 来源）；`status`：ITH 可写 operational（2022 inauguration + ITH “depuis 2022”）；`address` 优先 ITH/官方来源，DataCenterMap 地址是 C 但有用；`division` 始终 Mayotte；`sub_locality` 例如 Mamoudzou / Kaweni。不得从 LION2/FLY-LION3/Avassa 带宽、EDM 电厂容量或电网文件、采购金额或融资额、未登记的 Tier 表述推导容量。
- 刷新清单：ITH 官方站与新闻、AFD/Banque des Territoires/Caisse des Dépôts ITH 页、Uptime/TIA/EPI 登记、DataCenterMap/Baxtel/Cloudscene/PeeringDB、ARCEP Mayotte 频谱与 observatory 页、BOAMP/PLACE Mayotte hosting/PRA/PCA/colocation/salle informatique 招标、DEALM/Géorisques ICPE 与建筑许可、Orange/SRR/Telco OI/Only 官方页、Orange/Comores Câbles/Huawei 海缆页、Mayotte Hebdo/Le Journal de Mayotte/Mayotte la 1ère 客户与韧性更新。

## 维护注意（更新纪律）

- 每次更新重查：ITH 官方、AFD/CDC、Uptime/TIA/EPI、AWS/Azure/GCP/OCI、ARCEP、BOAMP/PLACE、DEAL/Géorisques、Mayotte 2024-2026 气旋恢复/海缆韧性新闻。
- 状态动词驱动：任何 `commissioned`、`RFS`、`ready for service`、`inaugurated`、`certified`、`awarded`、`installed` 字样触发重新分级；ITH 若出现 Uptime/TIA/EPI 证书 ID 立即把 `tier_claim` 升级为 `tier_certified`。
- 容量纪律：任何新容量/地址/运营商披露与 AFD/ITH 口径冲突时保留多来源并标注等级，不合并、不换算、不覆盖一手来源。
