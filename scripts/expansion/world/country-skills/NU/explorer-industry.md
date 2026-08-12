# NU Explorer Industry（行业/厂商源）- Niue 数据中心枚举方法

# NU Explorer Industry - Niue Datacenter Enumeration via Industry / Vendor Sources

日期 Date: 2026-08-12. 范围 Scope: Niue（NU）。Manifest 已核验 verified manifest entry: `{"country_code":"NU","country_name":"Niue","subnational_type":"country","divisions":["Niue"]}`. 行业枚举只能输出一个 division：`Niue`.

可靠性分级 Reliability grades: **A** = 运营商/厂商官方页、政府/监管文件、SOE 页面、官方公司注册处、官方云区域页、IANA、官方项目文件；**B** = 具名日期的区域/行业媒体、承包商案例、公开多边项目页、可信运营商访谈；**C** = 数据中心目录、海缆地图、PeeringDB/ASN 聚合、社交页、SEO 托管页、市场报告摘要。C 级只用于发现线索或负向控制。

## 0. 行业基线 Industry Baseline

- 本次核验未发现纽埃公开销售中性机架托管、商业 colocation、tiered datacenter、云区域或 hyperscale 容量。No public neutral colocation market was verified.
- 设施级行业信号集中在 Telecom Niue 与 Manatua。Telecom Niue 官方站提供 Personal/Business data, Fibre, 4G Wireless, ADSL, ICT Services 等服务入口，但未核验到公开 rack/colo/data-centre 产品页。
- Telecom Niue 是本地关键运营商。PaCSON profile 称 Telecom Niue 是 Niue 注册公司，2016 年公共事业 corporatisation 后由纽埃政府全资持有，并为固定/移动电话唯一服务商和主要互联网服务商；该资料可作 B/A-adjacent 支撑，但设施仍需 Telecom Niue/gov.nu 主源。
- Manatua 是行业上最重要的物理连接性资产。SubCom 2018 PDF 确认 Telecom Niue 是 Manatua 联合体成员，系统从 Apia 到 Toahotu，并有 Niue 等登陆/分支；Submarine Networks 记录 Manatua 连接 Samoa、Niue、Cook Islands、French Polynesia，且为 Niue 首次光纤连接。
- 2026-05-12 政府批准 Starlink/SpaceX 12 个月临时 Spectrum and Internet Communications Licence；Starlink 是 connectivity/resilience signal，不是 DC。
- .NU/IUSN 是数字经济背景。IANA 记录 .NU manager 为 The IUSN Foundation（Alofi），technical contact 为 The Internet Infrastructure Foundation（Sweden），registration services 为 Internetstiftelsen。不要把域名注册局或 DNS 误记为纽埃 DC。
- Tui-Samoa、SSCC、Apia、Tuasivi、Savai'i、Suva、Wallis & Futuna 是 Samoa/Fiji regional context；不计入 NU，除非有 A 级纽埃登陆证据。
- 负向先验很强：人口和小岛电网规模使商业 DC 市场概率极低。任何 "Niue VPS/cloud/dedicated server" 都必须先按 SEO/overseas hosting 误报处理。

## 1. Source Map And Grades

| Source | URL | Use | Grade |
|---|---|---|---|
| Telecom Niue | `https://telecomniue.com/` | 本地运营商、business ICT/fibre/4G/ADSL、网络公告、潜在 NOC/机房线索 | A for services; facility inference needs care |
| Government of Niue | `https://www.gov.nu/` | 政府公告、许可、招标、Manatua/Starlink/能源项目 | A |
| Niue Companies Office | `https://www.companies.gov.nu/` | 法律实体核验 | A legal existence, not facility |
| SubCom Manatua PDFs | `https://www.subcom.com/documents/Manatua-CIF-SubCom-final-19NOV2018.pdf`; `https://www.subcom.com/documents/2020/Manatua_Consortium_Confirms_Cable_Lay_Ops_Complete-FINAL-APPROVED_FOR_RELEASE-17FEB2020.pdf` | Manatua supplier/route/consortium | A/B |
| Submarine Networks | `https://www.submarinenetworks.com/en/systems/australia-usa/manatua`; `https://www.submarinenetworks.com/en/systems/australia-usa/tui-samoa` | cable route/date/capacity cross-check | B |
| SSCC | `https://www.ssccsamoa.com/` | Tui-Samoa and Samoa-side facility-access context | B/A for Samoa only; not NU facility |
| ADB Samoa Submarine Cable Project | `https://www.adb.org/projects/47320-001/main` | Tui-Samoa false-positive control | A/B for Samoa project |
| IANA .NU | `https://www.iana.org/domains/root/db/nu.html` | ccTLD delegation, IUSN/technical DNS split | A |
| IUSN / Internet Niue | `https://iusn.org/`; `https://internetniue.nu/` | .nu and island internet history | A/B for entity/history; not DC |
| Starlink | `https://www.starlink.com/map` plus gov.nu licence release | availability/licensing | A for connectivity, not DC |
| MFAT / SPC / PPA | `https://www.mfat.govt.nz/`; `https://devdata.mfat.govt.nz/`; `https://prdrse4all.spc.int/`; `https://www.ppa.org.fj/` | energy/connectivity projects, load context | A/B |
| Cloud regions | AWS/Azure/GCP/OCI official pages | NU public cloud absence | A negative |
| Directories | datacentermap.com, cloudscene.com, datacenters.com, submarinecablemap.com, PeeringDB | negative control / weak leads | C |

## 2. Operator And Vendor Sweep

### 2.1 Telecom Niue

行业相关性 Industry relevance: Telecom Niue is the only locally meaningful operator lead. Its official site has business services and ICT wording, and government releases tie it to fibre upgrades and new network sites. No official public colocation service was verified.

记录规则 Record rule: A Telecom Niue page can establish operator/service existence. A datacenter/colo record requires explicit language such as "data centre", "colocation", "rack", "hosting", "facility access", "customer equipment", "NOC" with a physical site or service boundary.

```text
site:telecomniue.com (business OR enterprise OR "ICT Services" OR hosting OR server OR cloud OR NOC OR switch OR colocation OR "data centre" OR "data center")
site:telecomniue.com (Manatua OR "landing station" OR "cable station" OR fibre OR fiber OR "network site" OR repeater OR Alofi OR Tuapa)
"Telecom Niue" ("data centre" OR "data center" OR colocation OR hosting OR "server room" OR NOC OR gateway OR switch)
"Telecom Niue" (Fortinet OR Cisco OR Huawei OR Alepo OR vendor OR upgrade OR "government network")
```

### 2.2 Manatua Cable And Cable-Adjacent Leads

Manatua is a `telecom_cable_station` lead, not a colocation facility by default. Search for facility-access evidence, RIO/FAA terms, wholesale interconnect, or customer equipment access before upgrading.

```text
"Manatua" Niue (Alofi OR landing OR "landing station" OR "cable station" OR RFS OR capacity OR fault OR repair)
"Manatua" ("facility access" OR FAA OR colocation OR interconnect OR "customer equipment" OR "meet me" OR "landing station access")
"Telecom Niue" Manatua (capacity OR wholesale OR "facility access" OR RIO OR interconnect)
site:subcom.com Manatua Niue
site:submarinenetworks.com Manatua Niue
```

### 2.3 IUSN / .NU Registry

行业相关性 Industry relevance: .NU creates a well-known Niue internet story but does not imply local hosting. IANA shows an Alofi manager and Sweden-based technical contact/name-server infrastructure.

```text
"IUSN" OR "Internet Users Society" Niue (registry OR ".nu" OR DNS OR server OR infrastructure OR WiFi OR revenue)
".nu" registry (Niue OR IUSN OR Internetstiftelsen) (server OR DNS OR infrastructure OR "data center" OR "data centre")
site:iana.org/domains/root/db/nu
site:iusn.org (DNS OR server OR infrastructure OR WiFi OR "Internet Niue")
```

Record as `dns_registry_context` or `public_wifi_context`; do not count as DC unless a primary source names a local facility that provides hosting/colo/compute to third parties.

### 2.4 Starlink And Satellite Providers

Starlink became officially licensed for a temporary 12-month trial in 2026; earlier reporting about unlicensed use must be time-scoped. Satellite signals are resilience/connectivity context only.

```text
Starlink Niue (availability OR coverage OR service OR license OR licence OR SpaceX OR spectrum) 2024..2026
site:gov.nu Starlink Niue
"Niue" (Kacific OR SES OR Intelsat OR satellite) (capacity OR contract OR broadband OR backup OR redundancy)
```

### 2.5 Enterprise / Public-Sector Server-Room Leads

Potential internal server-room leads include government departments, Niue Foou Hospital, schools, airport, utilities, bank/finance offices, BCN/TV Niue, and larger hotels. These are normally internal IT rooms and should not enter the DC list.

```text
"Government of Niue" (server OR "server room" OR "computer room" OR "data centre" OR "data center" OR backup OR DR)
"Niue" (hospital OR "Niue Foou" OR school OR airport OR bank OR "Television Niue" OR BCN) (server OR IT OR network OR "data centre" OR "data center")
"Alofi" ("server room" OR "computer room" OR NOC OR switch room OR hosting OR colocation)
```

Record as `enterprise_server_room_lead` only when the source names a physical room/site. Do not count as datacenter unless the source describes third-party hosting/colo or a nationally designated government DC.

### 2.6 Vendor / Contractor Sweep

High-value vendors: SubCom for Manatua; Sunergise for the 2026 Hikufenoga/Tamakautoga solar/BESS project; security/network vendors in Telecom Niue/government network upgrades (for example Fortinet case study evidence). Vendor cases are B unless paired with operator/government primary evidence.

```text
SubCom Manatua (Niue OR Alofi OR "landing station" OR cable)
"Niue" (Sunergise OR BESS OR "solar farm" OR "battery energy storage") (project OR contractor OR completion OR NPC)
"Niue" (Fortinet OR Cisco OR Huawei OR Alepo OR Nokia OR Ericsson) ("Telecom Niue" OR "government network" OR ICT OR security)
"Niue" (fibre OR fiber OR FTTH OR network) (contractor OR installer OR tender OR project)
```

## 3. Directories And Negative Controls

Run these as negative controls; C-grade directory absence is not proof, but it helps catch obvious market claims.

```text
site:datacentermap.com Niue OR Alofi
site:cloudscene.com Niue OR Alofi
site:datacenters.com Niue OR Alofi
site:peeringdb.com Niue OR "Telecom Niue"
site:submarinecablemap.com Manatua Alofi
"Niue" ("data center" OR "data centre" OR datacenter OR colocation OR "dedicated server" OR VPS OR "cloud hosting") -Starlink -"free wifi"
```

Treat overseas VPS/hosting offers as `seo_false_positive` unless they provide a physical Niue address and are independently anchored to Telecom Niue, Companies Office, or a government/utility source.

## 4. Enumeration Matrix

| Dimension | A-grade acceptance | B-grade use | C-grade use | Record rule |
|---|---|---|---|---|
| Commercial colo/hosting | Telecom Niue or another official local operator page naming colo/hosting/racks; government licence/project naming a DC | Named media or vendor case with address and operator | Directories/SEO only as leads | No A/B physical evidence = `no_market` |
| Cable landing | Telecom Niue/gov.nu/SubCom/consortium official evidence | Submarine Networks/TeleGeography/media | cable maps | `telecom_cable_station`; upgrade only with facility-access/customer-equipment evidence |
| Telecom core | Telecom Niue/gov.nu official service and network pages | vendor cases/interviews | ASN/PeeringDB | `telecom_network_lead`; not DC |
| Cloud providers | AWS/Azure/GCP/OCI official region pages | none for existence | marketing pages ignored | Official absence = `cloud_absence` |
| Energy/load | NPC/gov.nu/MFAT/SPC/PPA | vendor/media energy cases | maps | energy context only; required for large-load plausibility |
| Enterprise IT rooms | official institution docs | media/vendor cases | LinkedIn/social | lead only unless third-party facility service is explicit |
| .NU/IUSN/DNS | IANA/IUSN/Internetstiftelsen | reputable reporting | blogs/registrar marketing | DNS/registry context, not DC |

## 5. Division Coverage

Coverage is complete only if every retained record uses `division: "Niue"`. Village/location may be stored separately for geography, but division must not be expanded beyond the manifest.

Village search set: Alofi, Alofi North, Alofi South, Avatele, Hakupu, Vaiea, Liku, Lakepa, Mutalau, Namukulu, Hikutavake, Toi, Tuapa, Makefu, Tamakautoga, Hikufenoga/Tamakautoga near airport.

```text
"{Village}" Niue ("data center" OR "data centre" OR datacenter OR server OR hosting OR NOC OR fibre OR broadband OR "network site" OR solar OR BESS)
```

Default non-Alofi outcome: `no_projects`, unless an official/credible source names a specific telecom, utility, government ICT, or facility-access asset.

## 6. Final Grading Rules

- A 级可单独确立 entity/project/negative cloud-region facts，但 facility status 仍必须与来源措辞一致。
- B 级可佐证事件、供应商案例或媒体线索；不能单独把 "network upgrade" 升级为 DC。
- C 级永远不能单独建证。
- License/registration/service page != facility.
- Cable landing != datacenter.
- Satellite != datacenter.
- DNS registry != datacenter.
- Public cloud absence must be refreshed from official provider pages.
- Any upgrade from lead to facility must cite source URL, date observed, exact wording, operator, location, and why the record belongs to the single division `Niue`.
