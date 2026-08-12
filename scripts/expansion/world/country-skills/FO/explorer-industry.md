# FO Explorer Industry — 法罗群岛数据中心行业侧发现 (Industry / Trade-Press / Vendor Discovery)

Status: Final. Last reviewed: 2026-08-12. Scope: Faroe Islands (FO). Repo division model: **country**; manifest divisions (1): `Faroe Islands`.

用途 (Purpose)：从运营商、IT 服务商、行业媒体、厂商案例、网络数据库、采购线索和聚合器发现法罗群岛数据中心/hosting 候选。行业侧线索不得直接进入设施表；必须回到 `explorer-official.md` 用 A/B 证据确认。

## 0. 行业侧结构性事实 (Industry-Side Structure Facts)

- 法罗群岛市场很小，未发现公开规格的 hyperscale 或大型第三方 colocation campus。更可靠的画像是：本地 IT hosting / managed infrastructure provider + 电信机房 + 政府/金融关键系统机房。
- Repo division 只有 `Faroe Islands`。行业发现仍按 Streymoy、Eysturoy、Norðoyar、Vágar、Sandoy、Suðuroy 六个覆盖区域做 watch，但最终不要生成子 division。
- 当前 strongest leads 是 **Elektron**、**Nema Hýsing**、政府 `datacenter B` UPS 采购线索、以及 FT/NET/FARICE/SHEFA 的连接性基础设施。
- 连接性卖点真实存在：FARICE-1 通过 Funningsfjørður 接入法罗并服务 Torshavn；SHEFA-2 连接 Torshavn、设得兰/奥克尼和苏格兰。但 cable landing station/PoP 不等于数据中心。
- 电力背景真实存在：SEV 是主要电力提供者，2024 年可持续电力生产占 56.6%；2030 年 100% 可再生目标是 market context，不是项目证据。
- 聚合器和 IP/BGP 数据库会出现 `DataCenter`、`NEMA Datacenter`、`Elektron DataCenter` 等网络标签。这些只说明 IP/ASN 用途或反欺诈分类，不能单独确认物理商业 DC。

## 1. 行业检索词表 (Industry Search Vocabulary)

```text
# Faroese
"hýsing" / "hýsingartænastur" / "Nema Hýsing"
"samhýsing" / "skipanarrakstur" / "KT-rakstur"
"servarar" / "serverrúm" / "datacenter" / "data miðstøð"
"KT-trygd" / "trygdaravrit" / "netloysnir"
Elektron / Nema / Føroya Tele / FT / NET / Talgildu Føroyar / KT Landsins
FARICE-1 / SHEFA-2 / sjókaðal / kaðal
```

```text
# Danish / English
Faroe Islands data center / data centre / datacenter
Færøerne datacenter / hosting / it-drift / serverrum
managed hosting / hybrid cloud / private cloud / colocation
submarine cable / cable landing station / IXP / peering / PoP
UPS / generator / B22 / government datacenter
```

## 2. 可靠性分级 (Reliability Grades)

- **A** — 运营商/官方/一手来源直接证明该事实：Elektron/Nema/FT/NET 自家页面或年报、Keypsportal、Skráseting、SEV、Farice/SHEFA、Fjarskiftiseftirlitið、Lógasavn、市镇许可。
- **B** — 可信行业/厂商/媒体来源，具名公司、日期、状态：HPE customer story、DCD、Capacity、KVF、Portal、Dimmalætting、Sosialurin、Norðlýsið、Computerworld DK、Version2、Energiwatch、Nordregio、e-Governance Academy。
- **C** — 聚合、自报、网络标签或弱线索：PeeringDB、Pulse、BGP.HE.net、IP2Location、Scamalytics、Submarine Cable Map、DataCenterMap、Baxtel、LinkedIn、Wikipedia、市场报告摘要。
- **Lead only** — 不足以确认设施，只能生成待核候选。

分级只针对所附事实。例：Elektron 年报能 A 级证明其 hosting 和服务器数量；HPE 能 B 级证明其基础设施升级；BGP `Elektron DataCenter` 标签仍为 C。

## 3. 运营商/来源骨架 (Operator and Source Backbone)

### 3.1 Hosting / Managed Infrastructure

- **Elektron** — https://elektron.fo/ 。当前最强本地 hosting 线索。自家页面列 `Hýsing`、`Netloysnir`、`KT-trygd`；2022 年报说明其服务与 hýsing 部门 24/7 提供 hosting、managed solutions、backup/network/security services，并管理约 1,500 servers。HPE 2025 案例描述其从 VMware 迁移到 Hyper-V/HPE infrastructure，以支持 mission-critical public and financial services。分类：confirmed hosting provider / managed IT platform；设施地址和机房规格未公开到足以标注独立 DC campus。
- **Nema / Nema Hýsing** — https://www.nema.fo/ 。Nema 的 data-processing agreement for `Nema Hýsing` 明示物理数据存储在 Føroyar；Nema 新闻/页面提到 hýsing 管理员安全、2FA 等。分类：confirmed hosting service；物理设施位置、规模、冗余等级待核。PDF: https://www.nema.fo/wp-content/uploads/2023/06/Databehandleraftale_NEMA_Hysing.pdf 。
- **Føroya Tele / FT / NET** — https://www.ft.fo/ 与 https://www.net.fo/ 。FT/NET 是关键电信和光纤基础设施方，地址 Klingran 3, FO-188 Hoyvík。当前公开页面未确认独立商业 colocation/data center 产品；行业侧只保留为 telecom facility/network lead。
- **政府 IT / Talgildu Føroyar / KT Landsins** — https://www.talgildu.fo/english/english/ 。Keypsportal 有政府 `datacenter B` UPS 采购线索；需回查采购主体、建筑 B22、用途和是否为 government internal computer room。

### 3.2 电信、IXP、网络数据库 (Telecom, IXP, Network Databases)

- **Fjarskiftiseftirlitið** — https://www.fjarskiftiseftirlitid.fo/fo/fjarskifti/fjarskiftisveitarar 。用于运营商许可发现，不是设施来源。
- **PeeringDB / Pulse** — https://www.peeringdb.com/advanced_search?country=FO ，https://pulse.internetsociety.org/en/ixp-tracker/country/FO/ 。C 级自报/聚合，适合发现互联点和设施名称后回查。
- **BGP/IP sources**：BGP.HE.net、IP2Location、Scamalytics 可能显示 `Elektron DataCenter`、`NEMA Datacenter` 或 DCH 分类。只作为 C 级网络用途线索；不能直接导入为物理设施。

### 3.3 连接性来源 (Connectivity Sources)

- **Farice** — https://farice.is/network/ 和 https://farice.is/company-history/ 。A 级电缆事实：FARICE-1、DANICE、ÍRIS；FARICE-1 通过 Funningsfjørður branch 接入法罗，并有 Torshavn service point。
- **SHEFA** — https://www.shefa.fo/elbowroom/ ，https://www.shefa.fo/connecting-islands/ 。A/B 级电缆事实；TeleGeography map 可作 C/B 级交叉验证。
- **DCD / SubTel / Capacity / TeleGeography**：用于电缆故障、升级和新 cable plan 监控。不要把 cable resilience 报道解读为 DC 建设。

### 3.4 行业媒体与本地媒体 (Trade and Local Press)

优先检查：

```text
KVF: https://kvf.fo/
Portal: https://portal.fo/
Dimmalætting: https://dimma.fo/
Sosialurin: https://sosialurin.fo/
Norðlýsið: https://nordlysid.fo/
DCD tag: https://www.datacenterdynamics.com/en/tags/faroe-islands/
Computerworld DK / Version2 / Ingeniøren / Energiwatch
Nordregio connectivity reports
e-Governance Academy digital ID case
HPE customer stories
```

本地媒体可能更早报道政府 IT、金融 IT、海缆故障或电力项目；行业媒体更可能报道 5G、电缆和厂商案例。无官方/运营商回证时保持 B/lead。

### 3.5 聚合器与认证 (Aggregators and Certifications)

仅用于发现名称：

```text
https://www.datacentermap.com/faroe-islands/
https://baxtel.com/
https://baxtel.com/map
https://www.datacenters.com/locations/faroe-islands
https://www.peeringdb.com/advanced_search?country=FO
https://bgp.he.net/
https://www.ip2location.com/
```

Uptime Institute、ISO 27001、EN 50600、SOC 等认证只有在认证库或资产方页面出现时才可定级。Elektron 自家新闻称 ISO certified（2024）时，可 A 级记录“公司认证声明”，但不能自动推出 facility tier。

## 4. 查询模板 (Query Templates)

```text
# Elektron
site:elektron.fo "hýsing"
site:elektron.fo "servarar"
site:elektron.fo "Ársfrásøgn" "hýsing"
site:elektron.fo "ISO"
"Elektron" "Faroe Islands" "HPE"
"Elektron" "managed environments"
"Elektron DataCenter" "Faroe Islands"

# Nema
site:nema.fo "Nema Hýsing"
site:nema.fo "hýsing"
site:nema.fo "datacenter"
site:nema.fo "2 factor authentication" "hýsing"
"NEMA Datacenter" "Faroe Islands"
"Nema Hýsing" "Føroyar"

# FT / NET / telecom
site:ft.fo "server"
site:ft.fo "datacenter"
site:ft.fo "SHEFA"
site:net.fo "Klingran 3"
site:fjarskiftiseftirlitid.fo "Føroya Tele"
site:fjarskiftiseftirlitid.fo "Nema"

# Government IT / procurement
site:keypsportal.fo "datacenter"
site:keypsportal.fo "datacenter B"
site:keypsportal.fo "UPS"
site:keypsportal.fo "hýsing"
site:keypsportal.fo "Talgildu Føroyar"
site:talgildu.fo "datacenter"
site:talgildu.fo "hýsing"
"datacenter B" "B22" "Føroyar"

# Local/trade press
site:kvf.fo "datacenter"
site:kvf.fo "hýsing"
site:portal.fo "datacenter"
site:sosialurin.fo "Elektron" "hýsing"
site:nordlysid.fo "datacenter"
site:datacenterdynamics.com "Faroe Islands"
site:computerworld.dk "Færøerne" "datacenter"
site:version2.dk "Færøerne" "datacenter"

# Connectivity
site:farice.is "FARICE-1" "Torshavn"
site:shefa.fo "SHEFA-2"
"SHEFA-2" "Torshavn"
"Faroe Islands" "PeeringDB" "IXP"
```

## 5. 枚举矩阵 (Enumeration Matrix)

| 覆盖区域 | 预期活动 | 行业发现方法 |
|---|---|---|
| Streymoy | Light | 核心区域。查 Elektron、Nema、FT/NET、Talgildu Føroyar、Keypsportal、Tórshavn/Hoyvík 地址、FARICE/SHEFA Torshavn service/landing。 |
| Eysturoy | None/watch | FARICE-1 branch at Funningsfjørður 是连接性线索；查 Runavík/Fuglafjørður/Eysturkommuna 工业、SEV、电信网络。 |
| Norðoyar | None/watch | 查 Klaksvík/Norðlýsið/Nema presence；任何 `datacenter` 网络标签需回查资产方和地点。 |
| Vágar | None/watch | 查机场通信、Vágar/Sørvágur 工业用地、SEV；机场 IT room 不自动计 DC。 |
| Sandoy | None/watch | 隧道后年度扫描 local media、SEV、municipal permits。 |
| Suðuroy | None/watch | 查 SEV storage/grid、Tvøroyri/Vágur local permits；能源项目不等于 DC。 |

## 6. 行业侧确认来源/线索表 (Industry Source and Lead Table)

| 来源/候选 | Repo division | 覆盖区域 | 行业证据 / 分级 | 处理方式 |
|---|---|---|---|---|
| Elektron hosting / managed infrastructure | Faroe Islands | Streymoy/Tórshavn | A：Elektron 自家 hýsing 页面和年报；B：HPE 2025 case。 | 可作为 confirmed hosting provider；不标注公开 DC campus，除非找到设施地址/许可/规格。 |
| Nema Hýsing | Faroe Islands | Streymoy / Klaksvík lead | A：Nema Hýsing DPA states physical data in Føroyar；C：IP/BGP labels。 | 可作为 confirmed hosting service；设施位置/规模待核。 |
| Government `datacenter B` UPS procurement | Faroe Islands | likely Streymoy | A：Keypsportal procurement exemption line。 | Government internal data-center/server-room lead；回查 B22 building and owner before facility row expansion。 |
| FT/NET Klingran 3 network facilities | Faroe Islands | Streymoy/Hoyvík | A：FT/NET own pages for address/network role；no current public colo page found。 | Telecom/network facility lead only。 |
| FARICE-1 / SHEFA-2 | Faroe Islands | Eysturoy/Streymoy | A：Farice/SHEFA official pages；C/B：TeleGeography map。 | Connectivity only; not DC。 |
| PeeringDB / Pulse FO | Faroe Islands | National | C：self-reported/aggregated。 | Name discovery only;回查运营商。 |
| DataCenterMap/Baxtel/DataCenters.com country pages | Faroe Islands | National | C/U：often sparse or generated。 | Only use as lead discovery; no direct import。 |
| Hyperscaler public cloud region | Faroe Islands | National | A：AWS/Azure/GCP/Oracle official region pages show no FO region as of 2026-08-12。 | Record negative; recheck semi-annually。 |

## 7. 需谨慎的线索 (Caution Rules)

- **FT hosting assumption**：旧草稿把 FT 作为 Tórshavn hosting/DC lead，但当前 FT/NET 页面未确认公开商业 colocation/data-center 产品。保留为电信/网络设施线索，不作为 confirmed DC。
- **Network labels**：`Elektron DataCenter`、`NEMA Datacenter`、`DCH` 等 IP/BGP 标签不等于实地 facility。必须找运营商页面、年报、采购、许可或电力证据。
- **Government rooms**：`datacenter B`、UPS、Oracle/Linux support 等采购可证明政府 IT infrastructure 线索，但不等同商业 DC。
- **Cable landing stations**：Torshavn/Funningsfjørður landing/service points 是连接性基础设施；不计为 DC。
- **Renewable power narratives**：SEV 2030 green goal、wind/storage projects、cool climate narratives 只是市场背景；不能作为项目存在证据。
- **LinkedIn job titles**：Datacenter Technician 等个人资料只作 C 级线索。

## 8. 更新/复核节奏 (Update Cadence)

- **每月**：Elektron、Nema、FT/NET、Keypsportal、SEV、DCD Faroe tag、本地媒体。
- **每季**：PeeringDB/Pulse、BGP/IP labels diff、Fjarskiftiseftirlitið operator list、Farice/SHEFA updates。
- **每半年**：Elektron/Nema annual reports and policy PDFs、Skráseting records、hyperscaler official region pages、certification databases。
- **年度**：六个覆盖区域完整负向扫描，并把所有行业 leads 回写到 `explorer-official.md` 的确认/观察表。
