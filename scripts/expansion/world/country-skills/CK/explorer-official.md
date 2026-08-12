# CK 官方源勘探方法｜Cook Islands Official-Source Datacenter Discovery Methodology

> **双语说明 Bilingual note**：正文以中文为主（Chinese-primary）；实体名、URL、查询模板保留英文以保证可检索性。
> 日期 Date：2026-08-12。范围 Scope：库克群岛 Cook Islands (CK) 数据中心、托管、政府 ICT、海缆、电信监管、电力与采购的官方源勘探。
> 仓库分区 Repo divisions（`world-manifest.jsonl`）：`country_code=CK`，`subnational_type=country`，`divisions=["Cook Islands"]`。CK 只有 **Cook Islands** 一个仓库分区；本方法在分区内按岛屿/站点细分。

## 0. 结论框架 Executive frame

- CK 是极小市场，但不能写成“零数据中心”。已核实的设施级线索包括：**Vodafone Cook Islands / Telecom Cook Islands 的数据托管与小型 data centre 能力**、**Office of the Prime Minister (OPM) 的 CIG Data Center colocation 采购/升级**、以及 **Avaroa Cable 的 Manatua 登陆/国际与国内批发互联资产**。
- **商业超大规模/大体量 colocation 缺席**：未见 AWS/Azure/GCP/OCI 公共云区域，未见 Cloudscene/DataCenterMap/Baxtel 等目录列出 CK 托管市场；但 Vodafone 的 Data Housing & Hosting、Cloud Services 与 Avarua/Aroa/Aitutaki 小型机房必须作为 `telco-hosting/data-centre` 线索记录。
- **海缆不是数据中心**：Manatua/Avaroa Cable 是互联锚点。只有来源明确指向机房、rack、hosting、data centre、government data center/colocation 时，才可入设施候选。
- **监管已核实**：现行电信监管主体为 **Competition & Regulatory Authority of the Cook Islands (CRA)**，官网 `https://cra.org.ck/`；CRA 说明自 2021-03-01 起电信为其管辖行业，依据 **Telecommunications Act 2019**。任何旧法或“电信专员过渡期”说法仅作历史或误差线索处理。
- **电力约束**：TAU/Te Aponga Uira 只服务 Rarotonga；CIIC 与 TAU 官方页将其列为 Rarotonga 发配售电公用事业。外岛电力多为小型混合微网。任何 MW 级 DC 宣称必须先找 TAU/ADB/许可/并网证据。

## 1. 已核实官方锚点 Verified official anchors

| 官方源 Source | URL | 用途 Use | 可靠性 |
|---|---|---|---|
| Government Procurement Portal / PPCI | https://procurement.gov.ck/ | 政府 tender/RFT/RFQ；OPM、MDA、国企采购入口。MFEM 页面说明 PPCI 由 Major Projects & Procurement Support Division 的 Procurement Team 管理。 | A |
| MFEM Procurement | https://www.mfem.gov.ck/procurement | PPCI 管理说明、采购政策入口、MDA tender 发布规则。 | A |
| OPM / PM Office | https://www.pmoffice.gov.ck/ | ICT、National Digital Strategy 2024-2030、Cyber Security Policy、National ICT Policy 2023-2027；政府 ICT 的主线。 | A |
| CRA | https://cra.org.ck/ | 电信监管、牌照、频谱咨询、Telecommunications Act 2019、Competition and Regulatory Authority Act 2019。 | A |
| CIIC | https://www.ciic.gov.ck/ | Crown entities/SOEs：Avaroa Cables Limited、TAU、机场、港口等关键基础设施。`ciic.gov.ck` 为当前核实域名。 | A |
| Avaroa Cables Limited | https://avaroacable.com/ | Manatua 运营、ACL 身份、容量、go-live、故障/修复公告；CK 海缆一手源。 | A |
| TAU / Te Aponga Uira | https://teaponga.com/ | Rarotonga 电力公司；`teaponga.com` 为当前核实域名。 | A |
| ADB Cook Islands Renewable Energy Sector Project | https://www.adb.org/projects/46453-002/main | 南组太阳能/储能项目、电力背景；非 DC 证据。 | A |
| PDEP / UNCDF reports | https://www.uncdf.org/pdep and https://mptf.undp.org/ | 数字支付、数据保护、数字 ID 等采购/技术援助；通常不是设施证据。 | A/B（UN/项目文件） |

## 2. 政府/采购发现 Government & procurement

已核实的高信号官方采购：

- **RFT - Data Centre Colocation**：`https://procurement.gov.ck/tender=3374`（页面编码也可能表现为 `tender%3D3374`）。OPM 于 2020-11-11 发布，目标是为 Cook Islands Government (CIG) Data Center 寻找 colocation service；联系人为 OPM ICT Director，地址 Avarua, Rarotonga；修订后 closing date 为 2020-12-09。记录为 `government-data-centre-colocation procurement`，状态 `tender published/closed`，A 级。
- **Hyper-Converged Infrastructure Implementation & Government ICT Network Upgrade Project**：`https://procurement.gov.ck/tender=3361`。OPM 于 2020-10-23 发布，目标是设计、实施、迁移并支持 CIG software-defined HCI and network；修订后 closing date 为 2020-11-20。记录为 `government-ICT/HCI upgrade procurement`，A 级，不单独证明新建 DC。
- **Aiscorp/OPM 后续说明**：`https://www.aiscorp.co.nz/news/press-release-email-upgrade-for-cook-islands-government` 引用 OPM 2022 新闻稿，称 2021-12 已升级 government centralised network and data centre colocation，且 Aiscorp 获 tender。Aiscorp 是承包商源，作为 B 级授标/交付线索；需要尽量回链 OPM/Cook Islands News 原文。

政府查询模板：

```text
site:procurement.gov.ck ("data centre" OR "data center" OR colocation OR "cloud" OR "ICT" OR "hyper-converged" OR HCI)
site:procurement.gov.ck "Office of the Prime Minister" ("data" OR ICT OR cloud OR network)
site:mfem.gov.ck (procurement OR tender OR PPCI) ("data centre" OR "data center" OR ICT OR cloud)
site:pmoffice.gov.ck ("National Digital Strategy" OR "National ICT Policy" OR cybersecurity OR "data centre" OR "data center" OR cloud)
"Cook Islands Government" ("data centre colocation" OR "CIG Data Center" OR "ITC network")
"Cook Islands" "Aiscorp" ("data centre" OR "data center" OR colocation OR "network infrastructure")
```

处理规则：

- RFT/RFQ 只证明 `tender published/closed`；除非有 award、completion 或 operating evidence，不得升级为 `operational`。
- “Government ITC network / HCI / Microsoft 365 / cloud” 默认是 ICT 平台或云迁移，不等于本地数据中心，除非来源明示 colocation、data center、rack、server room 或具体站址。
- CIG Data Center 记录的 `division` 固定为 `Cook Islands`，`island/site` 优先填 `Rarotonga, Avarua`；若合同文件未披露托管地点，地址字段写 `not publicly disclosed`。

## 3. 电信监管 Telecom regulator

现行核实结论：

- **CRA / Competition & Regulatory Authority of the Cook Islands** 是独立 statutory body；官网说明自 **2021-03-01** 起 telecommunications 在其管辖下。
- CRA 官网页列出 **Telecommunications Act 2019** 与 **Competition and Regulatory Authority Act 2019** 下载入口，并有 licensed service providers、universal access、second mobile operator licence、frequency plan 等监管材料。
- MFEM Telecommunications Reform 页面确认 2019 policy 与 2019 两部法律通过，并发布 Bernard Hill 作为 inaugural Chair 的材料。

监管查询模板：

```text
site:cra.org.ck (telecommunications OR licence OR license OR spectrum OR "frequency band plan" OR "universal access")
site:cra.org.ck ("VCI licence" OR "Telecommunications Act 2019" OR "Competition and Regulatory Authority Act 2019")
site:mfem.gov.ck "Telecommunications Reform" "Cook Islands"
"Competition and Regulatory Authority" "Cook Islands" (Vodafone OR Avaroa OR licence OR spectrum)
"Cook Islands" ("second mobile operator" OR "universal access plan" OR "frequency band plan")
```

分级：

- CRA/MFEM/Parliament/Crown Law 法律和监管文件为 A。
- PITA、PSDI、媒体关于 CRA 设立和运行状态为 B，除非直接引用官方文件。

## 4. Avaroa Cable / Manatua

已核实事实：

- **Avaroa Cables Limited (ACL)** 官网称其为 Cook Islands Government 的 Crown Corporate Entity，负责管理 CK 参与 Manatua Cable 项目并开展国际/国内批发连接商业化；CIIC 建立 ACL 并任命其董事会。
- CIIC Crown Enterprise 页面称 ACL 是 Manatua Cable Project 的 implementing entity；Manatua 为 3,600 km、two-fiber-pair system，连接 Samoa、Niue、Rarotonga、Aitutaki、Tahiti、Bora Bora；ready for service 为 **2020-07**。
- Submarine Networks 交叉列出六个登陆点：Tahiti、Bora Bora、Rarotonga、Aitutaki、Apia、Niue；RFS 为 **2020-07-22**。
- ACL 官网 live check 时有 Manatua repair/fault update。执行时必须确认当前 `operational / impaired / under repair` 状态；不要把历史 “100% operational availability since 2020” 当作当前状态。

海缆查询模板：

```text
site:avaroacable.com (Manatua OR "ready for service" OR fault OR repair OR Rarotonga OR Aitutaki)
site:ciic.gov.ck (Avaroa OR Manatua OR cable OR "Crown Enterprise")
"Manatua" ("Rarotonga" OR "Aitutaki" OR "Avarua" OR "Rutaki") ("ready for service" OR RFS OR landed OR repair)
site:submarinenetworks.com Manatua "Cook Islands"
"Avaroa Cable" (Vodafone OR VakaNet OR "wholesale connectivity" OR "domestic connectivity")
```

记录规范：

- `asset_class=cable-landing`，不是 `data-center`。
- CK 站点至少覆盖 **Rarotonga** 与 **Aitutaki**；Avarua/Rutaki/Aroa 等更细站名必须由来源支撑。
- 容量字段可记录 10 Tb/s per fibre pair，但仅作为 connectivity capacity，不写入 IT MW。

## 5. 电信与托管运营商 Telco and hosting operators

官方/半官方核实：

- **Vodafone Cook Islands / Telecom Cook Islands LTD trading as Vodafone Cook Islands**：官网 `https://www.vodafone.co.ck/`，About 页面说明服务包括 `ICT & Cloud Services, Data Housing & Hosting`；Business Cloud Services 页面列出 hosting/cloud、data storage、backup/recovery 等服务。该来源 A 级证明运营商提供托管/云服务，但不披露机房数量或具体技术规格。
- **Vodafone data centres**：Avarua、Aroa、Aitutaki 三个 purpose-built data centres 的说法来自 APAC Outlook 访谈文章；Aitutaki data centre upgrade 的尺寸、UPS、generator、air controls 等来自 Vodafone Cook Islands 官方 LinkedIn 帖。官网未在公开页面逐一列出三站，因此三站位置/规格按 B 或 A-social 处理，需复核。
- **VakaNet**：ACL 官网在故障公告中把 Vodafone Cook Islands 与 VakaNet 列为 customers；作为 ISP/批发客户线索，不自动记为数据中心。

运营商查询模板：

```text
site:vodafone.co.ck ("Data Housing" OR Hosting OR "Cloud Services" OR "data centre" OR "data center" OR Aitutaki OR Aroa)
site:vodafone.co.ck/business-cloud-services (hosting OR storage OR backup OR recovery)
"Vodafone Cook Islands" ("data centre" OR "data center" OR "rack space" OR "Data Housing" OR Aitutaki OR Aroa OR Avarua)
"Telecom Cook Islands LTD trading as Vodafone Cook Islands"
"VakaNet" "Cook Islands" (hosting OR "data centre" OR "data center" OR Manatua)
```

## 6. 电力 Power

已核实：

- CIIC 页面列出 **Te Aponga Uira (TAU)** 是 Rarotonga 的发电与配电主体，并称其为 Rarotonga 与 CK 的 critical infrastructure asset。
- TAU 官网 About 页面称其是 Rarotonga 的 electricity generator, distributor and retailer。
- ADB Renewable Energy Sector Project 覆盖 Cook Islands southern group solar PV plants；这是电力背景和外岛微网约束，不是 DC 证据。

电力查询模板：

```text
site:teaponga.com (capacity OR MW OR diesel OR solar OR battery OR tariff OR outage OR "Avatiu")
site:ciic.gov.ck ("Te Aponga Uira" OR TAU OR electricity OR power)
site:adb.org/projects "Cook Islands" "Renewable Energy Sector Project" (solar OR battery OR MW OR "southern group")
"Rarotonga" ("Avatiu" OR TAU) (MW OR diesel OR BESS OR solar)
"Aitutaki" OR "Mangaia" OR "Atiu" OR "Mauke" OR "Mitiaro" (solar OR battery OR diesel OR microgrid)
```

容量处理：

- 数据中心记录不得从电站 MW 推导 IT load。
- Vodafone/OPM 小型托管设施若无公开电力数据，`capacity_it_mw=null`、`power_caveat=small-island grid; no public IT-load evidence`。

## 7. 分区覆盖 Per-division coverage

仓库只要求一个分区：**Cook Islands**。执行时必须覆盖以下站点簇，所有记录的 `division` 均写 `Cook Islands`。

| 站点簇 Site cluster | 必查资产 | 当前判断 |
|---|---|---|
| Rarotonga - Avarua/Parekura | OPM ICT/CIG Data Center colocation、Vodafone HQ/data housing、CRA、政府采购 | P1；最高信号 |
| Rarotonga - Aroa/Rutaki/Avatiu | Vodafone Aroa data centre 线索、Manatua landfall/CLS、TAU/Avatiu power | P1；站址名称需逐条来源化 |
| Aitutaki / Arutanga | Manatua domestic landing、Vodafone Aitutaki data centre upgrade、机场/旅游 ICT | P1/P2；已非空 |
| Southern Group: Atiu/Mangaia/Mauke/Mitiaro | Vodafone offices/mobile、ADB solar/microgrid、无 DC 预期 | P2/P3；记录负向 |
| Northern Group: Penrhyn/Manihiki/Pukapuka/Rakahanga/Nassau | Vodafone offices/mobile、satellite/O3b、无 DC 预期 | P2/P3；记录负向 |
| Uninhabited/special: Takutea/Manuae/Palmerston/Suwarrow | 保护区/小型通信线索 | P3；通常 `no_projects` |

岛屿查询模板：

```text
"Rarotonga" OR "Avarua" ("data centre" OR "data center" OR colocation OR "Data Housing" OR hosting OR "server room")
"Aroa" "Cook Islands" "data centre" OR "data center"
"Aitutaki" "Vodafone" ("data centre" OR "data center" OR hosting OR UPS OR generator)
"Aitutaki" "Manatua" (landing OR cable OR fibre OR fiber)
"Mangaia" OR "Atiu" OR "Mauke" OR "Mitiaro" (Vodafone OR telecom OR internet OR satellite OR data)
"Penrhyn" OR "Manihiki" OR "Pukapuka" OR "Rakahanga" (Vodafone OR telecom OR internet OR satellite OR data)
```

## 8. 输出规范 Output normalization

每条候选至少保存：

- `name`, `aliases`, `operator`, `ultimate_parent`
- `division=Cook Islands`, `island/site`, `address_or_landmark`, `coordinates` if verified
- `asset_class`: `telco-hosting-data-centre`, `government-data-centre-colocation`, `government-ict-platform`, `cable-landing`, `telco-core`, `satellite-gateway`, `cloud-region-absence`
- `status`, `status_date`, `source_status_verb`
- `capacity_it_mw=null unless source states IT load`, `racks`, `floor_area`, `power_source`
- `connectivity`: Manatua/O3b/satellite/Vodafone/VakaNet as applicable
- `evidence_grade_by_field`, `source_urls`, `notes_on_uncertainty`

当前种子记录：

| 名称 Name | 岛屿/站点 | 资产类别 | 状态 | 证据分级 |
|---|---|---|---|---|
| CIG Data Center colocation / OPM ICT environment | Rarotonga, Avarua; exact host not public | government-data-centre-colocation | RFT 2020-11；承包商/OPM 新闻线索称 2021-12 upgraded | A for RFT; B for completion |
| OPM HCI and Government ICT Network Upgrade | Rarotonga/Avarua + national government network | government-ict-platform | RFT 2020-10/closed 2020-11 | A |
| Vodafone Cook Islands Data Housing & Hosting | Rarotonga/Aitutaki; exact facilities partly public | telco-hosting-data-centre | service advertised on Vodafone official site | A for service; B/A-social for site details |
| Vodafone Aitutaki Data Centre Upgrade | Aitutaki | telco-hosting-data-centre | completed 2021-09 per Vodafone LinkedIn | A-social/B; verify with official site if possible |
| Vodafone Avarua/Aroa/Aitutaki data centres | Rarotonga Avarua/Aroa; Aitutaki | telco-hosting-data-centre | reported operational in APAC Outlook | B |
| Manatua / Avaroa Cable landing assets | Rarotonga, Aitutaki | cable-landing | RFS 2020-07/2020-07-22; current fault status must be checked | A/B |
| CRA telecom regulator | Avarua/Rarotonga | regulator | telecommunications jurisdiction since 2021-03-01 | A |
| TAU / Te Aponga Uira | Rarotonga | power utility | operating | A; non-DC |
| Hyperscaler cloud regions | none in CK | cloud-region-absence | absent on official region pages | A |
| Public IXP | none found | IXP absence | PCH/PeeringDB show no CK local IXP found in live check | A/B absence indicator |

## 9. 可靠性分级 Reliability grades

- **A**：Cook Islands government/PPCI/MFEM/OPM/CRA/CIIC/TAU/ACL official pages; official procurement notices; official cloud region pages; PeeringDB/PCH for interconnection records.
- **B**：Aiscorp contractor release when it cites OPM; Submarine Networks/GeoCables; APAC Outlook/Developing Telecoms/commsupdate/RNZ/Cook Islands News/Islands Business with named operators and dates.
- **C**：market reports, SEO pages, generic vendor country dropdowns, directory pages, social posts not owned by the operator, tender mirrors.
- **U**：dead pages, uncited claims, source not accessible, or facts that cannot be tied to CK rather than Samoa/Niue/French Polynesia.

同一条记录可按字段分级：例如 Vodafone `service exists` 为 A，`three data centres in Avarua/Aroa/Aitutaki` 为 B，`Aitutaki building size` 为 A-social/B。

## 10. 更新节奏 Update cadence

- **月度**：PPCI/MFEM tenders；OPM ICT/Digital Strategy；CIIC/ACL notices；Vodafone CK business/cloud pages；CRA notices/orders。
- **季度**：PCH/PeeringDB、DataCenterMap/Cloudscene/Baxtel、AWS/Azure/GCP/OCI official regions、ADB/UN PDEP documents。
- **事件驱动**：Manatua fault/repair/RFS status；Vodafone ownership/branding；new operator licences；CIG data centre colocation award/renewal；Aitutaki/Rarotonga facility upgrades；any cloud/sovereign DC tender。
