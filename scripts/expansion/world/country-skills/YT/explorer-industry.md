# YT Explorer Industry — 马约特数据中心行业/媒体/厂商发现方法论
# Mayotte Datacenter Enumeration via Operators, Connectivity Infrastructure, Trade Press, Vendors, and Division Query Patterns

日期 Date: 2026-08-12. 国家 Country: **YT Mayotte（马约特，法国海外省）**. 范围 Scope: 行业、运营商、目录、媒体与厂商视角的数据中心发现。`world-manifest.jsonl` 确认 YT 只有 **1 个分区 Division: Mayotte**；市镇与片区只作为 sub-locality。

可靠性分级 Reliability grades: **A** = 运营商/业主/政府/监管/开发金融机构/认证登记/海缆财团/云厂商官方来源直接证明具体主张。**B** = 有具名当事方、日期、地点的可靠本地或行业媒体。**C** = 目录站、市场平台、SEO 主机页、社交帖或没有设施级证据的聚合信息。目录数据可作为线索，但名称、地址、运营方、容量、认证都要回到一手来源复核。

---

## 0. 市场形态与已核实事实 Market Shape and Verified Facts

- **已确认公开设施**: **ITH Center / Information Technology Hosting SAS** 是马约特公开 colocation / housing 数据中心，位于 **Mamoudzou, Zone Industrielle de Kawéni**。官方运营方页 `https://www.ith.yt/` 称其为 “1er Datacenter Tier III Neutre dédié à la colocation de la région”，自 2022 年提供服务，容量口径为 80 bays。AFD 项目页 `https://www.afd.fr/fr/projets/construction-du-premier-data-center-de-mayotte` 确认项目为建设和运营马约特第一个 data center，位置 Mamoudzou，容量 **420 kW、76 bays、2 private suites**，2022-10-21 inaugurated。Banque des Territoires PDF 确认 ITH SAS 运营和约 10M EUR 总投资。
- **认证状态**: ITH 的 Tier III 是业主/项目/金融机构描述；本轮未在 Uptime/TIA/EPI 登记中核实证书 ID。记录为 `claimed/conception Tier III`，不要写 `certified Tier III`。
- **目录交叉验证**: DataCenterMap 现列 Mayotte/Mamoudzou 1 facility: ITH Center，地址 **629 Bd. Younoussa Bamana, BP 376, 97600 Mamoudzou**，并列 0.65 MW、350 sq.m.、2022。该目录为 C 级；可用于地址/容量差异提示，但不能覆盖 ITH/AFD/CDC 一手资料。
- **IXP/网络节点**: RENATER 官方确认 **MAYOTIX** 是 Mayotte 的 GIX/IXP，hosted in Mamoudzou on the Vice-Rectorate premises。它是交换点/PoP，不是 colocation DC，除非另有机房开放托管证据。
- **运营商**: ARCEP 2025-04-17 3.4-3.8 GHz 文件确认 Mayotte 牌照授予 **Orange、SRR、Telco OI**；Telco OI uses Only brand。2024 tender 中出现 Mayotte One，可作为候选/申请线索。目录中的 Free Mayotte/Telma Mayotte 不足以作为已核实本地 MNO 事实。
- **海缆/连接**: **LION2**（不是 FLY-LION2）、**FLY-LION3**、**Avassa** 是主要连接链。FLY-LION3 官方 Orange 页确认 Kaweni (Mamoudzou) landing and 4 Tbps system capacity；Avassa 由 Huawei Marine 新闻确认 260 km Comoros-Mayotte system with Comoros Telecom and Mayotte-based STOI。海缆容量不等于数据中心容量。
- **超大规模云区域**: AWS/Azure/GCP/OCI 官方区域页无 Mayotte region/local zone。本地 cloud/hosting 页面可代表服务，不代表 hyperscale cloud region。

---

## 1. 优先设施与基础设施扫描 Priority Facility and Infrastructure Sweep

| 线索 Lead | 来源路径 Source route | 位置处理 | 等级与行动 |
|---|---|---|---|
| **ITH Center / Information Technology Hosting SAS** | `ith.yt`; AFD project; Banque des Territoires/Caisse des Dépôts PDF; Annuaire Entreprises; DataCenterMap as C cross-check | Mayotte — Mamoudzou / Kaweni; possible directory address 629 Bd. Younoussa Bamana | **A confirmed facility**. Capture operator, address, 2022 inauguration/service, 420 kW/76 bays vs 80 bays discrepancy, claimed Tier III |
| **MAYOTIX** | RENATERIX official page; DataCenterMap IXP page; PeeringDB if accessible | Mayotte — Mamoudzou, Vice-Rectorate premises | **A IXP**, not DC. Use as connectivity/PoP lead |
| **Orange Mayotte** | `https://mayotte.orange.fr/portail/`; Orange group; ARCEP; BOAMP | Mamoudzou/Kaweni and island-wide network | A operator fact; only C/B DC lead unless facility evidence |
| **SRR / SFR Mayotte** | ARCEP decisions; Altice/SFR official pages; cable consortium references | Mamoudzou/Kaweni and island-wide network | A operator fact; cable/PoP lead |
| **Telco OI / Only** | `https://only.yt/`; `https://telco.re/`; ARCEP | Mayotte and Réunion-Mayotte network | A operator fact; PoP lead |
| **Mayotte One** | ARCEP 2024 tender dossier references | Island-wide candidate | Regulatory applicant/candidate only; do not treat as operating DC |
| **LION2 / FLY-LION3 / Avassa** | Orange, Huawei/Hengtong, Submarine Networks, TeleGeography, Comores Câbles | Mamoudzou/Kaweni/landing points | Connectivity facilities; not DC |
| **EDM / Longoni power infrastructure** | `electricitedemayotte.com`; CRE; DEAL/Géorisques | Koungou/Longoni and Mamoudzou | Power context; not DC without ICT/hosting evidence |
| **Government/hospital/municipal/bank customers** | AFD customer list; Mayotte Hebdo; BOAMP/PLACE; IEDOM | Mamoudzou-heavy | Demand and customer signals; facility only if address/operator evidence |

运营商与设施查询模板:
```text
"ITH Center" Mayotte ("colocation" OR housing OR "centre de données" OR datacenter OR "baies")
"Information Technology Hosting" Mayotte ("data center" OR "centre de données" OR AFD OR "Banque des Territoires")
"629 Bd. Younoussa Bamana" OR "Zone Industrielle de Kawéni" "ITH"
"Orange Mayotte" ("centre de données" OR "hébergement" OR cloud OR "salle serveur" OR NOC)
("SRR" OR "SFR Mayotte" OR "Telco OI" OR Only) Mayotte ("centre de données" OR "hébergement" OR "station d'atterrissement" OR NOC)
"Mayotte One" ARCEP Mayotte fréquences
```

---

## 2. 行业与媒体来源 Industry and Press Sources

| 来源 Source | URL | 用途 Use | 分级规则 |
|---|---|---|---|
| ITH Center | `https://www.ith.yt/` | 运营方、服务、容量、位置、Tier claim | A for self-described facility facts; certification claim still needs registry |
| AFD | `https://www.afd.fr/fr/projets/construction-du-premier-data-center-de-mayotte` | 项目、融资、容量 420 kW/76 bays、inauguration, customers | A |
| Banque des Territoires / Caisse des Dépôts | `https://www.banquedesterritoires.fr/` | ITH inauguration/financing; investment and operator | A |
| DataCenterMap | `https://www.datacentermap.com/mayotte/` | Directory cross-check, address/capacity seed | C unless matched to A sources |
| RENATER | `https://www.renater.fr/en/network/national-and-international/renaterix/` | MAYOTIX IXP | A |
| ARCEP | `https://www.arcep.fr/` | Operators, spectrum, observatories, cyclone recovery telecom context | A |
| Orange Mayotte | `https://mayotte.orange.fr/portail/` | Incumbent operator services | A for operator/service pages |
| Only / Telco OI | `https://only.yt/`; `https://telco.re/` | Operator services; Only brand | A for own service facts |
| Submarine Networks / TeleGeography | `https://www.submarinenetworks.com/`; `https://www.submarinecablemap.com/` | Cable landing seeds | B/B+; prefer Orange/Huawei/consortium pages for A |
| Huawei Marine / Hengtong | `https://www.huawei.com/en/news/2016/11/avassa-submarine-cable-project` | Avassa delivery and parties | A/B for vendor delivery fact |
| Mayotte Hebdo | `https://www.mayottehebdo.com/` | Local reporting on ITH customers, digital economy, resilience | B |
| Le Journal de Mayotte | `https://lejournaldemayotte.yt/` | Local business/digital reporting | B |
| Mayotte la 1ère | `https://la1ere.francetvinfo.fr/mayotte/` | Telecom, energy, cyclone recovery, public announcements | B |
| Linfo.re / Clicanoo / Imaz Press | `https://www.linfo.re/`; `https://www.clicanoo.re/`; `https://www.ipreunion.com/` | Réunion/Mayotte telecom and cable coverage | B |
| BOAMP / PLACE | `https://www.boamp.fr/`; `https://placee.marches-publics.gouv.fr/` | Hosting, cloud, PRA/PCA, network and facility procurement | A |
| Uptime/TIA/EPI | official registry URLs | Certification control | A |
| AWS/Azure/GCP/OCI | official region URLs | Hyperscale negative control | A |

媒体/行业查询模板:
```text
site:mayottehebdo.com "ITH Center"
site:mayottehebdo.com Mayotte (datacenter OR "centre de données")
site:lejournaldemayotte.yt Mayotte ("data center" OR "centre de données" OR ITH OR numérique)
site:la1ere.francetvinfo.fr/mayotte/ ("ITH" OR "datacenter" OR "centre de données" OR "câble sous-marin")
site:linfo.re Mayotte (Orange OR SFR OR Only OR "câble sous-marin" OR "centre de données")
site:datacenterdynamics.com Mayotte
site:datacenterdynamics.com "ITH Center"
site:submarinenetworks.com Mayotte ("LION2" OR "FLY-LION3" OR Avassa)
```

法语/英语关键词:
```text
"centre de données" | "data center" | datacenter | "salle des serveurs" | "salle serveur" | "salle informatique"
"hébergement de données" | hébergeur | housing | colocation | co-location | cloud | infogérance | "baie informatique"
"station d'atterrissement" | "câble sous-marin" | "point de présence" | backbone | NOC | GIX | IXP
"permis de construire" | ICPE | "déclaration préalable" | "étude d'impact"
"appel d'offres" | "marché public" | "avis de marché" | consultation | AO | CANUT
"groupe électrogène" | onduleur | UPS | climatisation | PUE | rack | m² | MW | MVA | kVA
```

---

## 3. 目录到一手的工作流 Directory-to-Primary Workflow

1. 从目录/平台获取种子：DataCenterMap、Baxtel、Cloudscene、datacenters.com、PeeringDB、IXP lists、AFNIC registrar lists、主机商页面。当前关键目录种子是 **ITH Center**；MAYOTIX 作为 IXP 种子。
2. 对每个种子回查一手来源：ITH/AFD/CDC/ARCEP/RENATER/BOAMP/PLACE/DEAL/Géorisques/Annuaire Entreprises。
3. 拆分事实字段：`facility_exists`, `operator`, `address`, `status`, `service`, `capacity_mw`, `bays`, `tier_claim`, `tier_certified`, `source_grade`。
4. 对冲突字段保留多来源：AFD 0.42 MW/76 bays 与 ITH 80 bays 同时保留；DataCenterMap 0.65 MW only C。
5. 仅当名称、地址、运营方和服务证明都对齐时合并记录；否则保留为 separate lead。

负向控制查询:
```text
"Mayotte" ("Uptime Institute" OR "TIA-942" OR "Tier III certified" OR "Tier 3 certified") "ITH"
site:baxtel.com Mayotte
site:cloudscene.com Mayotte "data center"
site:peeringdb.com "MAYOTIX"
site:peeringdb.com "ITH Center"
"Mayotte" ("AWS" OR Azure OR "Google Cloud" OR OCI OR "local zone" OR "edge location")
"Mayotte" ("cloud hosting" OR "dedicated server" OR VPS) -travel -SIM
```

---

## 4. 分区菜谱 Division Recipe

清单分区为 **Mayotte**。记录统一使用:

```yaml
division: Mayotte
country_code: YT
subnational_type: country
```

市镇/片区覆盖:

| 子位置 | 当前高价值线索 | 处理 |
|---|---|---|
| Mamoudzou / Kaweni | ITH Center; LION2/FLY-LION3 landing; operator PoPs; administrative/hospital clients | 最高优先级；所有设施记录优先核地址 |
| Mamoudzou / Vice-Rectorate | MAYOTIX | IXP/PoP only |
| Koungou / Longoni | EDM power plant, port, power/ICPE records | Power/logistics context; no DC unless new proof |
| Dzaoudzi / Pamandzi | Airport/old administrative center telecom rooms | Low-confidence facility leads only |
| Dembéni, Ouangani, Sada, Chirongui, Bandrélé, Acoua, M'tsangamouji, Mtsamboro, Bandraboua, Tsingoni, Chiconi, Bouéni, Kani-Kéli | municipal procurement, local IT rooms | mark no public DC unless procurement/permit evidence emerges |

通用分区查询:
```text
("Mayotte" OR Mahoré OR "976") ("ITH Center" OR "Information Technology Hosting" OR "centre de données" OR datacenter OR colocation)
(Mamoudzou OR Kaweni OR Kawéni) ("ITH" OR "data center" OR "centre de données" OR "baies" OR "hébergement")
(Mamoudzou OR Kaweni) ("station d'atterrissement" OR "câble sous-marin" OR LION2 OR "FLY-LION3" OR Avassa)
(Koungou OR Longoni) (centrale OR EDM OR port OR "groupe électrogène" OR ICPE)
(Dzaoudzi OR Pamandzi) (télécom OR serveur OR aéroport OR informatique)
```

---

## 5. 待验证种子记录 Seed Records

| Seed | Status | Capacity | Operator | Grade | Sources to use |
|---|---|---:|---|---|---|
| **ITH Center / ITH Datacenter** | Operating / inaugurated 2022; colocation/housing | AFD: 0.42 MW, 76 bays; ITH: 80 bays; DCM: 0.65 MW C-only | Information Technology Hosting SAS / ITH Center | **A** for facility; Tier certification not proven | ITH, AFD, Banque des Territoires, Annuaire Entreprises, DataCenterMap |
| **MAYOTIX** | Operating IXP/GIX | null | RENATER | **A** IXP, not DC | RENATERIX, PeeringDB/DataCenterMap cross-check |
| **LION2 Kaweni/Mamoudzou landing** | Operating submarine cable landing | cable capacity only; no DC capacity | consortium/operator to verify | A/B connectivity | Orange archives, Submarine Networks, TeleGeography |
| **FLY-LION3 Kaweni landing** | Cable landed 2019; operating status to refresh | 4 Tbps cable capacity, not DC capacity | Orange/SRR/Comores Câbles consortium | A connectivity | Orange press release, Comores Câbles |
| **Avassa Mayotte/STOI landing** | Delivered 2016 | cable capacity only | Comoros Telecom + STOI / parties to verify | A/B connectivity | Huawei/Hengtong, TeleGeography |
| **Orange/SRR/Telco OI network rooms** | Operator PoP/NOC leads | null | Orange, SRR, Telco OI | A operator fact; C facility lead | ARCEP, operator pages, BOAMP |
| **Mayotte One** | Regulatory applicant/candidate lead | null | Mayotte One | B/C until official operating proof | ARCEP 2024/2025 files |
| **EDM control rooms / Longoni plant** | Power infrastructure | not DC capacity | EDM | A power fact; not DC | EDM, CRE, DEAL, Géorisques |
| **Public-sector hosting demand** | Customers/procurement | null | municipalities, Département, CHM, SIM, others | A/B demand signal | AFD customer list, BOAMP/PLACE, Mayotte Hebdo |
| **Hyperscale cloud region** | Negative | null | AWS/Azure/GCP/OCI | A negative | official region pages |
| **Certified Tier facility** | Negative until certificate ID found | null | Uptime/TIA/EPI | A negative | certification registries |

---

## 6. 容量、可靠性与命名规则 Capacity, Reliability, Naming

- `capacity_mw`: For ITH, use **0.42** with source `AFD` unless a stronger owner technical sheet supersedes it. Store DataCenterMap 0.65 MW as `capacity_mw_alt_c: 0.65` or note-only.
- `bays`: Store both source-specific values: `76 bays + 2 private suites` from AFD, `80 bays` from ITH official page.
- `tier_certified`: `null` unless Uptime/TIA/EPI registry gives a certificate.
- `tier_claim`: `Tier III` / `conception Tier III` with ITH/AFD/CDC source.
- `status`: ITH may be `operational` based on 2022 inauguration and ITH “depuis 2022” service language.
- `address`: Prefer ITH/official source if exact address appears; DataCenterMap address is C but useful: `629 Bd. Younoussa Bamana, BP 376, 97600 Mamoudzou`.
- `division`: always `Mayotte`.
- `sub_locality`: e.g. `Mamoudzou / Kaweni`.

不得从以下推导容量:
- LION2/FLY-LION3/Avassa bandwidth.
- EDM plant capacity or grid documents.
- Procurement amount or financing amount.
- Claimed Tier language without certification registry.

刷新清单 Refresh checklist:
```text
ITH official site and news
AFD / Banque des Territoires / Caisse des Dépôts ITH pages
Uptime Institute / TIA / EPI registries
DataCenterMap / Baxtel / Cloudscene / PeeringDB
ARCEP Mayotte spectrum and observatory pages
BOAMP / PLACE Mayotte hosting, PRA/PCA, colocation, salle informatique tenders
DEALM / Géorisques ICPE and construction permits
Orange / SRR / Telco OI / Only official pages
Orange / Comores Câbles / Huawei submarine cable pages
Mayotte Hebdo / Le Journal de Mayotte / Mayotte la 1ère for customer and resilience updates
```
