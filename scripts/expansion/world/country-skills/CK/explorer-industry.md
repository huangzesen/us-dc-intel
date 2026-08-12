# CK 行业源勘探方法｜Cook Islands Industry-Source Datacenter Discovery Methodology

> **双语说明 Bilingual note**：正文以中文为主（Chinese-primary）；行业媒体、运营商、目录、查询模板保留英文。
> 日期 Date：2026-08-12。范围 Scope：库克群岛 Cook Islands (CK) 数据中心、托管、海缆、电信、云与互联网交换的行业/媒体/厂商源勘探。
> 仓库分区 Repo divisions：`world-manifest.jsonl` 确认 CK 只有 **Cook Islands** 一个分区；行业枚举按 Rarotonga、Aitutaki、Pa Enua 站点簇下沉，但输出 `division` 固定为 `Cook Islands`。

## 0. 行业判断 Industry frame

- CK 不是常规商业 colocation 市场，但存在小型、运营商驱动的数据托管能力。行业侧最重要的修正是：**APAC Outlook 2022 访谈称 Vodafone Cook Islands 有 Avarua、Aroa、Aitutaki 三个 purpose-built data centres，并提供 rack/hosting/IaaS 能力**；Vodafone 官方站也列出 `ICT & Cloud Services, Data Housing & Hosting`。
- **政府需求通过本地托管/网络升级体现**：PPCI 的 2020 `RFT - Data Centre Colocation` 与 HCI/ITC network upgrade 是政府侧最高信号；Aiscorp 2022 发布稿称 CIG centralised network and data centre colocation 已在 2021-12 升级。
- **Manatua/Avaroa Cable 是互联锚点**：Rarotonga 和 Aitutaki 均为 CK 登陆点。海缆设施可作为 `cable-landing`，不得直接算作 DC。
- **无公开 hyperscale/cloud region/IXP**：AWS、Azure、Google Cloud、Oracle 的官方 region pages 未列 CK；PCH/PeeringDB live check 未见 CK 本地 IXP。PeeringDB 有 AS10131 Telecom Cook Islands 在 Equinix Sydney 的 public peering，这说明境外互联而非 CK IXP/DC。
- **电力限制现实**：Rarotonga 由 TAU 供电，外岛多为小型混合系统；Vodafone/政府托管设施应按 small-island telco/enterprise hosting，而不是 MW-scale DC。

## 1. 高信号行业源 High-signal industry sources

| 来源 Source | URL/检索面 | 用途 Use | 分级 |
|---|---|---|---|
| Vodafone Cook Islands official site | https://www.vodafone.co.ck/ and `/business-cloud-services` | Data Housing & Hosting、Cloud Services、业务服务存在性。 | A |
| Vodafone Cook Islands LinkedIn | https://www.linkedin.com/company/vodafone-cook-islands/ | Aitutaki data centre upgrade 等 operator-owned social evidence；可作站点/规格线索。 | A-social/B |
| APAC Outlook | https://www.apacoutlookmag.com/company-profiles/566-vodafone-cook-islands | 三个 data centres、rack space/IaaS、O3b/Manatua 背景；为访谈型行业媒体。 | B |
| Aiscorp | https://www.aiscorp.co.nz/news/press-release-email-upgrade-for-cook-islands-government | CIG email/network/data centre colocation upgrade；承包商引述 OPM。 | B |
| Submarine Networks | https://www.submarinenetworks.com/en/systems/australia-usa/manatua | Manatua landing/RFS/capacity/consortium cross-check。 | B |
| GeoCables | https://geocables.com/ | Manatua 地理和系统状态交叉核对；路径可能变化，站内搜。 | B |
| commsupdate / Developing Telecoms / RNZ Pacific | https://www.commsupdate.com/; https://developingtelecoms.com/; https://www.rnz.co.nz/international/pacific-news | 电信自由化、Vodafone/ACL/Manatua deal、运营商变更。 | B |
| Cook Islands News | https://www.cookislandsnews.com/ | 本地政府 ICT、招标、基础设施报道；引用官方时可回链。 | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | 免费 DC 行业扫面；预计少命中，适合验证未来项目。 | B |
| PeeringDB / PCH | https://www.peeringdb.com/; https://www.pch.net/ixp/dir | IXP/facility/interconnection 检查；缺席只能作为 absence indicator。 | A/B |
| DataCenterMap / Cloudscene / Baxtel | https://www.datacentermap.com/; https://cloudscene.com/; https://baxtel.com/ | 目录检查；预计 CK 空白或无直接国家页。 | C |
| BuddeCom / generic market reports | search by `Cook Islands telecoms broadband` | 市场背景和历史所有权；不可作设施证明。 | C |

## 2. 运营商与设施线索 Operator/facility leads

### 2.1 Vodafone Cook Islands / Telecom Cook Islands

已核实行业与运营商信号：

- Vodafone 官网 About 页面称其提供 mobile、internet、WiFi、business connectivity，并列出 `ICT & Cloud Services, Data Housing & Hosting`。
- Vodafone Business Cloud Services 页面列出 `Hosting & Cloud Services for Business`，含 Email、Cloud PABX、Data Storage、Website、backup/recovery 等服务。该页证明托管/云服务存在，但未披露具体数据中心站址、racks、MW。
- APAC Outlook 访谈称 Vodafone 有 **Avarua、Aroa、Aitutaki** 三个 purpose-built data centres，提供 rack space/entire racks，并支撑 business/government IaaS；该位置/能力为 B 级行业证据。
- Vodafone 官方 LinkedIn 帖称 **Aitutaki Data Centre Upgrade** 新建 10m x 5m building，含 redundant UPS、backup generator、24x7 monitored security cameras、redundant air environmental controls、structured cabling，2021-09 完成。该事实为 operator-owned social evidence，记录时标 `A-social/B`，执行时仍应寻找官网/新闻稿备份。

查询模板：

```text
site:vodafone.co.ck ("Data Housing" OR "Hosting" OR "Cloud Services" OR "Data Storage" OR "data centre" OR "data center")
"Vodafone Cook Islands" ("data centre" OR "data center" OR "rack space" OR "entire racks" OR IaaS)
"Vodafone Cook Islands" "Aitutaki Data Centre Upgrade"
"Vodafone Cook Islands" ("Avarua" OR "Aroa" OR "Aitutaki") ("data centre" OR "data center")
"Telecom Cook Islands LTD trading as Vodafone Cook Islands" (hosting OR cloud OR "data")
```

### 2.2 CIG / OPM government colocation

行业侧应把政府采购与承包商发布稿串联：

- PPCI `RFT - Data Centre Colocation` 是 A 级采购证据。
- PPCI HCI/ITC Network Upgrade 是 A 级 ICT platform/network procurement。
- Aiscorp 2022 release 称 previous government ITC environment built in 2012，centralised network and data centre colocation upgraded in 2021-12，并说明 Aiscorp 获 tender。此处不公开托管地点，不能假定在 Vodafone 其中某站，除非找到合同/OPM 原文。

查询模板：

```text
"CIG Data Center" OR "Cook Islands Government Data Center" colocation
"Cook Islands Government" "data centre colocation"
"Cook Islands Government" "centralised network and data centre colocation"
"Aiscorp" "Cook Islands" ("data centre" OR "data center" OR colocation OR "ITC network")
site:cookislandsnews.com "email upgrade" "Cook Islands Government" Aiscorp
```

### 2.3 Avaroa Cable / Manatua

- ACL official 与 CIIC official 是 A 级；Submarine Networks/GeoCables/commsupdate/Developing Telecoms 是 B 级。
- CK landing points 至少包括 **Rarotonga** 与 **Aitutaki**。若来源只写 Avarua/Rutaki，应保留该站名但不覆盖 Aitutaki。
- 当前状态需每次 live-check：ACL 官网可能发布 cable fault/repair updates；行业目录的 `ready for service` 不一定反映当天故障。

查询模板：

```text
"Manatua" ("Cook Islands" OR Rarotonga OR Aitutaki OR Avaroa) ("ready for service" OR RFS OR fault OR repair)
"Avaroa Cable" ("Vodafone Cook Islands" OR VakaNet OR wholesale OR "domestic connectivity")
site:submarinenetworks.com Manatua "Rarotonga" "Aitutaki"
site:geocables.com Manatua "Cook Islands"
site:developingtelecoms.com "Avaroa Cable" "Vodafone Cook Islands"
```

## 3. 云与 IXP Cloud and IXP discovery

### 3.1 Hyperscaler/public cloud

截至 2026-08-12 live check，AWS、Azure、Google Cloud、Oracle Cloud 官方 regions pages 未列 CK region。记录为 `cloud-region-absence`，不要把 Australia/New Zealand serving region 写成 CK facility。

```text
site:aws.amazon.com/about-aws/global-infrastructure/ "Cook Islands"
site:learn.microsoft.com/en-us/azure/reliability/regions-list "Cook Islands"
site:cloud.google.com/about/locations "Cook Islands"
site:oracle.com/cloud/public-cloud-regions/ "Cook Islands"
"AWS" "Cook Islands" ("Local Zone" OR "Wavelength" OR "edge location")
"Azure" "Cook Islands" ("region" OR "edge" OR "data center")
```

### 3.2 IXP/peering

- PCH IXP directory live check did not show CK in the accessible country list.
- PeeringDB has AS10131 / Telecom Cook Islands public peering at **Equinix Sydney** and no local interconnection facilities visible in the public page. This is overseas peering, not CK IXP.

```text
site:peeringdb.com "Cook Islands" ("Exchange" OR "Facility" OR IXP OR AS10131)
site:pch.net/ixp "Cook Islands"
"Cook Islands" ("internet exchange" OR IXP OR peering)
"AS10131" ("Cook Islands" OR Vodafone OR "Telecom Cook Islands")
```

## 4. 目录与市场报告 Directory checks

目录站可用于查漏，但 CK 小型运营商设施很可能未入库：

```text
site:datacentermap.com "Cook Islands"
site:cloudscene.com "Cook Islands" ("data centers" OR "data centres" OR Vodafone)
site:baxtel.com "Cook Islands" "data center"
"Cook Islands" ("colocation" OR "colo" OR "data centre") -"Cayman" -"Christmas"
"Cook Islands" ("hosting" OR "IaaS" OR "cloud services") Vodafone
```

处理：

- 目录空白不是绝对 absence proof；只能与官方/运营商/采购缺席合用。
- 泛市场页、SEO 咨询页、国家下拉菜单命中一律 C/U，除非给出 CK 具体设施名、地址、运营商、状态。

## 5. 枚举矩阵 Enumeration matrix

| 站点簇 Site cluster | 商业托管 | 政府 DC/云采购 | 海缆登陆站 | 电信核心/托管 | 卫星/O3b | IXP | 云区域 | 优先级 |
|---|---|---|---|---|---|---|---|---|
| Rarotonga - Avarua/Parekura | Vodafone Data Housing & Hosting；Avarua DC 线索 | CIG Data Center colocation；HCI/ITC upgrade | Manatua/Rarotonga | Vodafone HQ/core | O3b per APAC Outlook | 未见 | 缺席 | P1 |
| Rarotonga - Aroa/Rutaki/Avatiu | Aroa DC 线索 | 无公开新建 DC | Manatua landfall/CLS 线索；TAU/Avatiu power | Vodafone network | O3b/satellite | 未见 | 缺席 | P1 |
| Aitutaki/Arutanga | Vodafone Aitutaki DC upgrade | 无 | Manatua domestic landing | Vodafone office/core | O3b/satellite | 未见 | 缺席 | P1/P2 |
| Southern Group: Atiu/Mangaia/Mauke/Mitiaro | 未见 | 无 | 无 | Vodafone offices/mobile | satellite/O3b | 未见 | 缺席 | P2/P3 |
| Northern Group: Penrhyn/Manihiki/Pukapuka/Rakahanga/Nassau | 未见 | 无 | 无 | Vodafone offices/mobile | satellite/O3b | 未见 | 缺席 | P2/P3 |
| Takutea/Manuae/Palmerston/Suwarrow | 未见 | 无 | 无 | 无/极小 | emergency/satellite only | 未见 | 缺席 | P3 |

每轮必须为非命中簇记录 `no_projects`，避免后续误以为未查。

## 6. 已知候选 Known candidates

| 名称 Name | 岛屿/站点 | 资产类别 Asset class | 状态 Status | 最佳证据 |
|---|---|---|---|---|
| Vodafone Cook Islands Data Housing & Hosting | Rarotonga + national service | telco-hosting-data-centre | 官网列出服务；无公开 MW/rack 数 | Vodafone official A |
| Vodafone Avarua Data Centre | Rarotonga, Avarua | telco-hosting-data-centre | APAC Outlook 称 operational/purpose-built | B |
| Vodafone Aroa Data Centre | Rarotonga, Aroa | telco-hosting-data-centre | APAC Outlook 称 operational/purpose-built；需独立复核 | B |
| Vodafone Aitutaki Data Centre | Aitutaki | telco-hosting-data-centre | Vodafone LinkedIn 称 2021-09 upgrade completed；APAC Outlook 交叉 | A-social/B |
| CIG Data Center Colocation | Rarotonga/Avarua probable; host not public | government-data-centre-colocation | 2020 RFT；2021-12 upgrade per Aiscorp/OPM release | A procurement; B delivery |
| CIG HCI / ITC Network Upgrade | Government network | government-ict-platform | 2020 RFT; not standalone DC | A |
| Manatua / Avaroa Cable Rarotonga landing | Rarotonga | cable-landing | RFS 2020-07/2020-07-22; current status live-check | A/B |
| Manatua / Avaroa Cable Aitutaki landing | Aitutaki | cable-landing | RFS 2020-07/2020-07-22 | A/B |
| Public IXP in CK | none found | IXP | no local IXP found in PCH/PeeringDB check | absence indicator |
| Hyperscaler public cloud region in CK | none | cloud-region | absent from AWS/Azure/GCP/OCI region lists | A absence |

## 7. 可靠性与假阳性 Reliability and false positives

- **A**：operator official site、government procurement/OPM/MFEM/CRA/CIIC/ACL/TAU pages、official cloud region pages、PeeringDB/PCH for listed interconnection facts。
- **A-social/B**：operator-owned LinkedIn/Facebook posts；可用于站点线索和状态，但重要字段应尽量找官网备份。
- **B**：APAC Outlook, Aiscorp, Submarine Networks, GeoCables, commsupdate, Developing Telecoms, RNZ, Cook Islands News。
- **C**：SEO consulting pages、market reports、generic vendor pages with only country dropdowns、unverified directory pages。
- **U**：dead links、unattributed claims、把 Cook Islands 与 Cook County/Cayman/Christmas Island 混淆的结果。

假阳性清单：

- `data center` 在联合国电子政务统计语境中可能指“数据门户/统计数据库”，不是机房。
- Manatua、O3b、Starlink、Kacific、WiFi hotspot 是 connectivity，不是 data centre。
- Vodafone Group global DC/cloud references 不等于 CK 设施；只接受 `Vodafone Cook Islands` 或本地站点证据。
- Avaroa（公司）与 Avarua（首都/镇）必须分开。

## 8. 更新节奏 Update cadence

- **月度**：Vodafone CK site/news/LinkedIn；PPCI tenders；Aiscorp/Cook Islands News/OPM follow-ups；ACL fault/repair notices。
- **季度**：APAC Outlook/commsupdate/DCD/RNZ/Developing Telecoms sweep；PeeringDB/PCH；DataCenterMap/Cloudscene/Baxtel；official hyperscaler regions。
- **事件驱动**：Manatua outage/restoration；new operator licence；Vodafone facility expansion；CIG colocation renewal/award；National Digital Strategy implementation procurement；any sovereign cloud/data-residency tender。
