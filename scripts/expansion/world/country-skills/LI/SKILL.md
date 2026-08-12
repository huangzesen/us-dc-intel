---
name: li-datacenter-methodology
location: scripts/expansion/world/country-skills/LI/SKILL.md
description: |
  Liechtenstein (LI) datacenter discovery & audit methodology — how to enumerate, verify, and update Liechtenstein datacenter projects at commune (Gemeinde) granularity (11 communes in the current manifest). Microstate with no public national datacenter register and no single national building-permit portal: enumeration combines national AHR building authority (eBaugesuch/Baubewilligung), each commune's Bauverwaltung surface, LKW (state utility) energy/telecom colocation records (Eschen Hub 37), AK telecom colocation/unbundling documents, Handelsregister entity checks, geodata, and local press (Vaterland, lie:zeit). Operator cluster in Vaduz/Schaan/Eschen/Balers: vestra (Eschen+Vaduz), SupraNet (Schaan+Eschen), SpeedCom (two LI DCs), Kyberna Balzers, ICT-Center Vaduz (directory-led). No hyperscaler cloud region. German-first queries (Rechenzentrum/Baugesuch/Baubewilligung/Kollokation). Read this before running LI exploration/audit batches. Routes to explorer-official.md (AHR/communes/LKW/AK/registers/cloud controls) and explorer-industry.md (operators/directories/press/commune strategy).
---

# LI · 列支敦士登数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：列支敦士登为**微型国家（11 市镇）**，无全国数据中心注册库、无单一全国建设许可门户；枚举组合国家 AHR 建设局（eBaugesuch/Baubewilligung）、各市镇 Bauverwaltung、LKW（国有电力与电信网络运营商）能源/电信 colocation 记录、AK 电信 colocation/解绑文件、Handelsregister 法人、geodata 与本地媒体。
> 分区模型：**11 Gemeinde**（Balzers, Eschen, Gamprin, Mauren, Planken, Ruggell, Schaan, Schellenberg, Triesen, Triesenberg, Vaduz）；行业证据指向 **Vaduz、Schaan、Eschen、Balzers** 为设施高概率区，其余为必跑低概率扫。
> 德语优先：`Rechenzentrum`/`Datacenter`/`Serverraum`/`Kollokation`/`Baugesuch`/`Baubewilligung`/`Baufreigabe`/`Inbetriebnahme`/`Trafostation`/`Netzanschluss`。
> 无 AWS/Azure/GCP/OCI 区域（官方页负面；邻近区域 Zurich/Frankfurt/Milan/Austria East 不等于 LI）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供列支敦士登探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：AHR（eBaugesuch/Baubewilligung、Formserver、Baugesetz）、11 市镇 Bauverwaltung 页、Statistikportal Bautätigkeit、Geodaten/OpenData、Handelsregister、AK 电信、LKW Kollokation Standortliste（Eschen Hub 37）与 TAL 解绑位置、LKW 年报、采购、云区域邻近控制、市镇逐镇策略与提取字段/证据规则 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子表（vestra/plus.li、SupraNet/QualityNet、SpeedCom/newsnet、LKW、Kyberna、ICT-Center Vaduz、FL1/Telecom LI、跨境瑞士/奥地利供应商）、目录交叉核查（DataCenterMap/DataCenter Catalog/Inflect/colo.exchange/PQ.hosting/DCHub/PeeringDB/WKL）、协会（proIT/Wirtschaftskammer/LIHK/Digital LI/FMA）、贸易媒体（Vaterland/Volksblatt 档案/lie:zeit/Landesspiegel）、云邻近、状态词汇与推荐枚举循环 |

## 核心结构事实（框定每次搜索）

1. **许可证据强度顺序**：`Baugesuch/Auflage`=线索；`Baubewilligung/Bewilligungsbescheid/Baufreigabe`=许可证据；`Bauabnahme/Inbetriebnahme/eroeffnet`/活跃官方服务页=运营证据；按原状态词记录。
2. **LKW/AK 是决定性佐证通道**：LKW 为国有电力+电信网络运营商，大型 DC 应留下电网/变压器/客户用电痕迹；AK/LKW Kollokation Standortliste（Eschen Hub/Hubstrasse 37、Schaanwald/Mauren 等）为官方网络接入 colocation 点（A），但**不自动等于商业数据中心**。
3. **运营商种子（A 服务存在，B/C 精确地址/规格）**：vestra ICT/plus.li（运营商声明 Eschen+Vaduz 双 DC；Vaduz Landstrasse 107；Eschen Hub 37 目录线索）、SupraNet/QualityNet（Schaan+Eschen 联合运营、约 200 m2 机架/笼/足迹、冗余供电/UPS/柴油/光纤；目录地址冲突 Wirtschaftspark 65 vs Im alten Riet 121）、SpeedCom/newsnet（运营商声明两个独立 LI 数据中心；WKL 地址 Im alten Riet 153 Schaan；Ruggell 条目未确认）、Kyberna（DataCenter Balzers，Fabrikstrasse 4，A 公司页/C 地址规格）、ICT-Center Vaduz（Schwefelstrasse 5A，目录 C 直至运营商/注册/许可源）、FL1/Telecom LI（托管/云/连接线索，无设施页，B 不计数）。
4. **Handelsregister 法人验证**：搜 `Rechenzentrum`/`Datacenter`/`Kollokation`/`Cloud`/`Server`；防名称碰撞。
5. **目录不可单独计数**：DataCenterMap 把 LI 归 Vaduz 市场（实际场址在 Balzers/Eschen/Schaan/可能 Ruggell）；目录 7 设施/5 运营商为 C 声称，仅作对账目标。
6. **状态词汇**：`Absicht/Planung/Projekt/Standortsuche/angekuendigt`=线索；`Baugesuch/Bauverhandlung/Baubewilligung/Baufreigabe`=许可；`Baustart/Inbetriebnahme/eroeffnet`+活跃服务页=运营；`abgelehnt/zurueckgezogen/sistiert/stillgelegt`=拒绝/退役。
7. **无超规模区域**：AWS（Zurich eu-central-2/Frankfurt/Milan）、Azure（Switzerland/Austria East）、GCP（Zurich/Milan/Frankfurt）、OCI（Zurich/Frankfurt）——均非 LI 设施；官方页仅 A 逻辑区域存在性。
8. **乡村市镇负面**：除非市镇/AHR 直接确认无记录，否则写“no public evidence found in sweep date”，不写确认缺席。

## 查询模式（复制粘贴模板见 explorer-official.md §2 / explorer-industry.md §1-§5）

- 许可/市镇：`"{Gemeinde}" "Rechenzentrum" "Baugesuch"`、`"{Gemeinde}" "Datacenter" "Baubewilligung"`、`site:{gemeinde-domain} Rechenzentrum Baugesuch`、`site:llv.li Rechenzentrum Baubewilligung OR Baufreigabe`、`filetype:pdf Liechtenstein Rechenzentrum Baubewilligung`。
- 能源/电网：`site:lkw.li Rechenzentrum OR Datacenter OR Kollokation`、`site:lkw.li Jahresbericht Rechenzentrum`、`"Liechtensteinische Kraftwerke" Rechenzentrum Netzanschluss`、`"LKW" "{Operator}" Anschlussleistung`。
- 电信：`site:llv.li "Amt fuer Kommunikation" Kollokation`、`"Hub 37" Eschen Kollokation`、`"Schaanwald" "Kollokation fuer alternative Betreiber"`。
- 注册/geodata/媒体：`site:handelsregister.li Rechenzentrum OR Datacenter OR Kollokation`、`site:vaterland.li "{Gemeinde}" Rechenzentrum OR Datacenter`、`site:lie-zeit.li "{Gemeinde}" Rechenzentrum OR Datacenter OR Baugesuch`。
- 运营商：`site:{operator-domain} (Liechtenstein OR Vaduz OR Schaan OR Eschen OR Balzers) ("data center" OR Datacenter OR Rechenzentrum OR Kollokation)`、`"{operator}" "{street}" ("data center" OR Rechenzentrum)`、`"{operator}" Handelsregister Liechtenstein`。
- 云控制：`("Liechtenstein" OR "Vaduz") ("AWS" OR Azure OR "Google Cloud" OR Oracle) ("region" OR "availability zone")`、`site:cloud.google.com Liechtenstein region`。

## 官方/监管管线要点（详见 explorer-official.md）

- AHR：国家建设局（llv.li，eBaugesuch、Formserver Bauvorhaben、Baugesetz/gesetze.li）；市镇 Bauverwaltung 参与（balzers/eschen/gamprin/mauren/planken/ruggell/schaan/schellenberg/triesen/triesenberg/vaduz 各镇页）。
- Statistikportal Bautätigkeit：聚合 AHR 签发 Baubewilligungen/Baufreigaben（工业/服务业项目，非 DC 专类）。
- LKW：官方站/年报（扫 `Rechenzentrum/Kollokation/Trafostation/Anschlussleistung/Grosskunde`）；Kollokation Standortliste 为官方网络接入点清单。
- AK：电信市场规则与 colocation/解绑材料（TAL Kupfer 位置）。
- Handelsregister（A 法人/SPV）；geodata/opendata（地块/分区校验）；采购（llv.li/市镇页面/官方渠道，A 办公/B 发现）。
- 计数规则：物理 DC 需 A/B 证据覆盖 地点+运营商+运营/许可状态；AK/LKW 电信 colocation 点按电信接入点处理；运营商页为自身主张 A，容量/冗余/开张日期须数据表或许可支撑才 A。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 协会：proIT（B IT 公司宇宙）、Wirtschaftskammer（B 成员/地址，含 SpeedCom）、LIHK（B-/C+）、Digital Liechtenstein（B 上下文）、FMA（A 监管/B 上下文，金融外包/数据驻留）、Uni LI（C+）。
- 媒体：Vaterland（B 主扫）、Volksblatt 档案（B 历史，2023 前）、lie:zeit（B）、Landesspiegel（B-/C+）、radio.li（C+）、瑞士/奥地利区域媒体（B-/C+）；供应商案例（B，如 SupraNet 现代化）。
- 目录（C）：DataCenterMap、DataCenter Catalog、Inflect、colo.exchange、PQ.hosting、DCHub、PeeringDB（B-/C）、WKL（B 地址支持）、local.ch/search.ch/yellowpages.li（C）。
- 目录对账规则：纯目录=lead/C/下一步运营商+市镇/AHR+geodata+LKW/AK；运营商页同镇确认=operating/service-stated（A 存在/B 细节）；市镇/AHR 许可=按措辞定 permit/construction/operating（A）。

## 已知设施/项目与证据状态

| 设施/项目 | 市镇 | 状态与证据 |
|---|---|---|
| vestra ICT / plus.li 双 DC | Eschen + Vaduz（Landstrasse 107） | A 运营商声明存在；精确地址/规格 B/C；市镇许可待补 |
| SupraNet / QualityNet 双 DC | Schaan + Eschen | A 运营商声明（约 200 m2 机架/笼）；目录地址冲突（Wirtschaftspark 65 vs Im alten Riet 121）；许许可待补 |
| SpeedCom / newsnet 两处 LI DC | Schaan（Im alten Riet 153）为主，Ruggell 未确认 | A 运营商声明两处；B WKL 地址；C 目录规格；第二址须确认 |
| LKW Kollokation / Eschen Hub 37 | Eschen（+Schaanwald/Mauren 等） | A 官方电信 colocation 点；按电信接入点分类，非自动商业 DC |
| Kyberna DataCenter Balzers | Balzers（Fabrikstrasse 4） | A 公司页；C 目录地址/规格；Balzers Bauverwaltung 待验 |
| ICT-Center Vaduz | Vaduz（Schwefelstrasse 5A） | C 目录线索；Handelsregister/Vaduz 许可前不计数 |
| Telecom Liechtenstein / FL1 | Vaduz（HQ Schaanerstrasse 1） | B 托管/云/连接线索；无设施页不计数 |

## 更新节奏

- 每批次：云区域季度控制、vestra/SupraNet/SpeedCom 官方页与地址更新、Kyberna/ICT-Center 一手源、LKW/AK colocation 清单变化。
- 季度：11 市镇负面扫回顾（Gamprin/Mauren/Planken/Ruggell/Schellenberg/Triesen/Triesenberg）、Handelsregister 新实体、本地媒体（Vaterland/lie:zeit）新 Baugesuch。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（11 市镇粒度）；本 skill 作为国家层参考注入。
