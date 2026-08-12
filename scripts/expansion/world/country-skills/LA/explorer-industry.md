# LA Explorer Industry - Laos Datacenter Operator and Trade-Press Discovery

Date: 2026-08-12. Scope: commercial operators, government-cloud vendors, telco/ISP hosting, cloud-region absence checks, trade press, aggregators, and project-tracker methodology for Laos datacenter enumeration. Use with `LA/explorer-official.md`; official/regulatory evidence takes precedence over this file.

Reliability grades:
- **A** = operator-primary page, company announcement/filing, official cloud-region list, KPL/MTC/InvestLaos source, utility/SEZ primary source.
- **B** = established trade press or reputable business press with named parties, dates, and project facts.
- **C** = aggregator, directory, SEO page, market-report snippet, job ad, social-only post, or stale page. Discovery only.

---

## 0. Laos Market Model

- Laos is a very small datacenter market. The confirmed public facility/service evidence is concentrated in **Vientiane Capital**: government eco/National Data Center infrastructure, GDMS/National Cloud, Unitel Cloud, LaoDC, and telco/ISP hosting/server rooms.
- There is no confirmed hyperscale public cloud region in Laos. Nearby regional options are Thailand, Singapore, Malaysia, Vietnam/Hanoi-Ho Chi Minh footprints from local operators, Hong Kong, and China depending on provider and compliance needs.
- Treat `cloud`, `server rental`, `hosting`, `IDC`, `National Data Center`, and `data center` carefully. In Laos these labels may describe a government platform, telco server room, virtual-server product, modular government facility, feasibility study, or a true colocation facility.
- Most provincial leads will be **SEZ opportunity or telecom coverage**, not datacenter projects. Require named operator/project evidence before adding a province facility.
- Keep online gambling/scam compounds, crypto-mining farms, tower colocation, and normal enterprise server rooms separate from datacenter rows unless the database has explicit non-standard categories.

---

## 1. Confirmed and High-Value Operator / Vendor Seeds

| Entity | Role | Public DC/cloud signal | Status to record | Grade |
|---|---|---|---|---|
| **MTC / National Data Center / LANIC** | Regulator, government hosting, national data infrastructure | MTC site links LANIC `.la`, server rental/hosting, ICT service licensing, and digital-economy publications; KPL names the National Data Center under MTC in 2025 AI-infrastructure MoU | Government platform / regulator / pipeline | A |
| **Lao PDR Energy Efficient Datacenter Project** | Government-operated eco datacenter | IIJ says Lao PDR's first government-operated eco datacenter was completed in Vientiane on 2016-11-29; Toyota Tsusho/JCM confirm Lao-Japan JCM registration and modular/energy-efficient design | Operational government datacenter precedent; current operational role needs re-check | A |
| **GDMS / Global Digital Management Solutions** - `https://www.global-dms.com/` | Sovereign/national cloud and datacenter services | GDMS says it has a 10-year strategic partnership with MTC, operates/enhances one National Data Center, and extends National Cloud infrastructure across both National Data Centers | Operational sovereign cloud/vendor claim; primary vendor, not ministry confirmation | B+ |
| **Unitel Cloud / Star Telecom** - `https://ucloudserver.unitel.com.la/` | Telco cloud services | Unitel Cloud page lists cloud computing, backup, DDoS protection, WAF, cloud storage, and contact address at Nongbone Road, Phonxay Village, Saysettha District, Vientiane Capital | Operational cloud/hosting service; facility specs unpublished | A for service/address, C for physical DC specs |
| **LaoDC** - `https://laodc.com/` | Private colocation/hosting | LaoDC page states it has its own datacenter in Vientiane Capital with redundant fiber rings, redundant power, emergency diesel generators, solar plant, and hosting/dedicated/virtual server services | Operational private datacenter claim; verify current certifications/customers separately | A for operator claim, B/C for capacity/quality |
| **Phounphonnakhone Co., Ltd. / Phongsavanh Group** | National Data Centre feasibility partner | Vientiane Times reports MTC partnership/feasibility study for National Data Centre and Government Data Exchange System; Xinhua mirrors the topic | Pipeline / feasibility only | B unless MTC/KPL document found |
| **Silicon Tech Park (Lao) Sole Co., Ltd.** | AI infrastructure / AI SEZ developer lead | KPL confirms 2025-05-30 MoU with MTC National Data Center for feasibility study on green-energy AI infrastructure and >150 ha AI SEZ in Vientiane capital area | Pipeline / MoU only | A for MoU event, C/B for eventual project until approved |
| **Lao Telecom (LTC)** | Incumbent telecom operator | Likely internal network/server facilities and enterprise services; no public facility-level DC specs found in this pass | Telecom internal lead | C unless official hosting/DC page found |
| **ETL** | Telecom operator | Likely internal facilities; no public facility-level DC specs found | Telecom internal lead | C |
| **T-Plus Laos** | Telecom operator | Likely internal facilities; no public facility-level DC specs found | Telecom internal lead | C |
| **Best Telecom** | Telecom/5G entrant and tower/backhaul lead | OCK/Bursa-linked press in 2024 says OCK signed a 15-year tower leasing agreement with Best Telecom for Laos 5G rollout | Connectivity lead, not DC | B for tower deal, C/none for DC |
| **Planet Online / Planet Computers** | ISP/hosting lead | Appears in telecom/ISP market references; verify any live hosting/colo page before adding | Small hosting/ISP lead | C |

Primary URLs to preserve in registry notes:

```text
https://mtc.gov.la/
https://kpl.gov.la/En/detail.aspx?id=91710
https://www.vientianetimes.org.la/freefreenews/freecontent_189_Ministry_y25.php
https://www.iij.ad.jp/en/news/pressrelease/2016/1130.html
https://www.toyota-tsusho.com/english/press/detail/170920_004027.html
https://www.jcm.go.jp/jc/projects/la001/
https://www.global-dms.com/empowering-laos-how-gdms-is-building-the-nations-digital-future/
https://www.global-dms.com/10-year-partnership-for-leed-datacenter/
https://ucloudserver.unitel.com.la/
https://ucloudserver.unitel.com.la/Home/Contact
https://laodc.com/
```

---

## 2. Hyperscaler / Foreign Cloud Absence Checks

As of this rewrite, no official global-infrastructure page confirms a Laos public cloud region or availability zone for the major hyperscalers. Verify quarterly from official pages only:

```text
AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
Microsoft Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
Google Cloud: https://cloud.google.com/about/locations
Oracle Cloud Infrastructure: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
Alibaba Cloud: https://www.alibabacloud.com/global-locations
Tencent Cloud: https://www.tencentcloud.com/document/product/213/6091
Huawei Cloud: https://www.huaweicloud.com/intl/en-us/about/global.html
```

Record result as:

```text
provider = AWS/Azure/GCP/OCI/Alibaba/Tencent/Huawei
country = Laos
status = no_public_region_found
source_grade = A
nearest_regions = Thailand/Singapore/Malaysia/Hong Kong/China as applicable
checked_date = 2026-08-12
```

Do not treat reseller pages, partner clouds, or CDN/edge POPs as physical Laos regions unless the provider's official global-infrastructure page names Laos.

---

## 3. Trade Press and Aggregator Sweep

| Source | Search route | Use | Grade |
|---|---|---|---|
| **KPL** | `site:kpl.gov.la/En "data center" Laos` | Official state-media confirmation of MTC/National Data Center announcements | A |
| **Vientiane Times** | `site:vientianetimes.org.la "data centre" Laos` | Official-adjacent English daily; useful for MTC seminars, MoUs, feasibility studies | B, sometimes A-adjacent for state announcements |
| **Xinhua / China.org.cn mirrors** | `site:english.news.cn Laos "national data center"` | Useful for China-facing state-media mirrors of Lao government announcements | B |
| **Laotian Times / Open Development Laos mirrors** | `site:laotiantimes.com Laos "data center"`, `site:laos.opendevelopmentmekong.net "LaoDC"` | Discovery for LaoDC and local tech/infrastructure stories | B/C depending on original sourcing |
| **DataCenterMap** | `https://www.datacentermap.com/laos/` | Cross-check count/location; currently lists Laos data centers only in Vientiane | C |
| **Datacenters.com / Cloudscene / PeeringDB** | country and Vientiane searches | Discovery for providers, addresses, ASNs, exchanges | C unless operator-linked |
| **W.Media / Data Center Dynamics / Capacity / Telecom Review / Developing Telecoms** | site-scoped `Laos data center` searches | Regional context, telecom/cloud leads, Vietnam-Laos projects | B/C; verify with primary pages |
| **Vietnam press** | `VietnamPlus`, `VietNam News`, `Viettel` sources | Unitel/Viettel and Vietnam-Laos data-platform cooperation | B |
| **Chinese-language sources** | `老挝 数据中心`, `万象 数据中心`, `磨丁 数据中心` | China-linked SEZ, BRI, railway-corridor, AI, and smart-city leads | B/C until official Laos/operator confirmation |
| **Facebook/social pages** | MTC, KPL Lao, provincial administrations, operators | Many Lao announcements appear first on social | C unless official page plus document image/date/party names |

High-yield templates:

```text
"Laos" "data center" "Vientiane"
"Laos" "data centre" "National Data Centre"
"LaoDC" "Vientiane" colocation
"Unitel Cloud" "Nongbone" "Saysettha"
"GDMS" "National Cloud" Laos
"Global Digital Management Solutions" "National Data Centers" Laos
"Silicon Tech Park" Laos "AI" "data center"
"Phounphonnakhone" "National Data Centre"
"Phongsavanh" "government data exchange"
"Lao PDR Energy Efficient Datacenter Project"
"IIJ" "Lao PDR" "datacenter" Vientiane
"Toyota Tsusho" Laos datacenter JCM
老挝 数据中心 万象
老挝 国家数据中心
老挝 人工智能 数据中心
```

---

## 4. Project Tracker Seed Rows

These are seed rows for the registry. Verify again before publishing, especially if the registry requires current operating status, MW, rack count, ownership, or exact coordinates.

| Project / facility | Parties | Location | Evidence | Registry status | Grade |
|---|---|---|---|---|---|
| Lao PDR Energy Efficient Datacenter Project / government eco datacenter | Lao government, IIJ, Toyota Tsusho, AMZ Group/JCM participants | Vientiane | IIJ completion announcement 2016-11-29; Toyota/JCM project registration | Operational precedent; current status unknown | A for completion/existence |
| National Cloud / National Data Centers | MTC + GDMS | Vientiane, exact sites not public | GDMS says it operates/enhances one National Data Center and extends National Cloud across both centers | Operational vendor/government-cloud platform claim | B+ until ministry page confirms details |
| Unitel Cloud | Star Telecom / Unitel | Nongbone Road, Phonxay Village, Saysettha District, Vientiane Capital | Unitel Cloud official pages list services and contact address | Operational cloud service; physical DC specs unpublished | A for service/address, C for facility specs |
| LaoDC | LaoDC | Vientiane Capital; historic groundbreaking in Hatxaykhao village near Vientiane | LaoDC official page says own datacenter in Vientiane; Open Development/Laotian Times mirror reports 2018 groundbreaking as first licensed private DC | Operational operator claim; license/current certification needs verification | A/B |
| Green-energy AI infrastructure + AI SEZ | MTC National Data Center + Silicon Tech Park (Lao) | Vientiane capital area; proposed SEZ >150 ha | KPL 2025-06-03 article for 2025-05-30 MoU | MoU / feasibility / pipeline | A for MoU, not operational |
| National Data Centre + Government Data Exchange System | MTC + Phounphonnakhone Co., Ltd. / Phongsavanh Group | likely Vientiane, not fixed publicly | Vientiane Times 2025 article; Xinhua mirror | Feasibility / pipeline | B |
| LANIC server rental/hosting | LANIC under MTC link path | Vientiane / government network; exact facility not public | MTC home links server rental/hosting service via LANIC | Government hosting service lead | A for service, C for facility details |
| Lao Telecom / ETL / T-Plus internal server rooms | Telecom operators | mostly Vientiane HQ/network nodes | telecom market/operator evidence; no public DC specs found | Telecom-internal lead only | C |
| Best Telecom / OCK 5G tower rollout | Best Telecom + OCK | multiple cities/provinces | OCK/press 2024 tower leasing agreement | Connectivity/tower lead; not DC | B for tower deal |
| Savan-Seno SEZ ICT/datacenter opportunity | SEZ authority / potential investors | Savannakhet | InvestLaos official SEZ page confirms location, utilities, corridor role | SEZ opportunity; no confirmed DC tenant | A for SEZ, no DC row without tenant |
| Boten Beautiful Land SEZ ICT opportunity | SEZ/developer | Louang Namtha | InvestLaos official page lists post/telecommunication among project categories | SEZ opportunity; no confirmed DC tenant | A for SEZ |
| Golden Triangle SEZ telecom/internet/compute leads | SEZ/developer and tenants | Bokeo | InvestLaos official page lists post/telecommunication/internet; crime/crypto/scam reports are not DC evidence | Non-standard compute/SEZ lead only | A for SEZ, C for unverified compute |

---

## 5. Province and SEZ Industry Sweep

Run the official sweep in `explorer-official.md` first, then use these industry pivots.

- **Vientiane Capital**: exhaustive operator search. Query Unitel Cloud, LaoDC, GDMS, LANIC, Lao Telecom, ETL, T-Plus, Best Telecom, Planet Online, Saysettha Development Zone, VITA Park, Thatluang Lake, Long-Thanh Vientiane, Dongphosy, `Vientiane AI SEZ`, `Nongbone Road`, `Hatxaykhao`.
- **Savannakhet**: search Savan-Seno, Savan Park, East-West Economic Corridor, logistics/ICT tenants, EDL high-load notices, and Vietnamese/Thai border connectivity. No confirmed DC tenant in this pass.
- **Bokeo**: search Golden Triangle SEZ, Kings Romans, Ton Pheung, internet/telecom tenants, 5G, crypto mining, and scam-infrastructure reports. Keep crime/scam/mining leads separate from datacenter rows.
- **Louang Namtha**: search Boten, Mohan-Boten border, China-Laos Railway, Chinese-language smart-city/cloud/data terms. No confirmed DC tenant in this pass.
- **Champasak**: search Pakse, Pakse-Japan SEZ, Vangtao/Phonthong, Lao-Service Industrial Park, Mahanathi Sithandone, EDL, telecom/ISP hosting.
- **Khammouan**: search Thakhaek SEZ, logistics corridor, Vietnam rail/port links, industrial park ICT tenants.
- **Louangphabang**: search Luangprabang SEZ, tourism/government digital projects, telecom edge sites.
- **Viangchan / Vientiane Province**: search Phonhong, Vang Vieng, spillover from Vientiane Capital, substations/industrial parks; distinguish province from capital in every row.
- **Attapu, Bolikhamxai, Houaphan, Oudomxai, Phongsali, Salavan, Xaignabouli, Xekong, Xiangkhouang, Xaisomboun**: one-pass annual sweep by English/Lao province name plus `data center`, `cloud`, `hosting`, `server`, `ສູນຂໍ້ມູນ`, `ຄລາວ`, and Chinese if border-linked. Expect no confirmed DC.

---

## 6. Normalization and De-Duping Rules

- Normalize **Vientiane Capital** separately from **Viangchan / Vientiane Province**. Do not place Vientiane Capital facilities into the manifest province `Viangchan`.
- Normalize **MTC**, **MPT**, and older **MOST** references by project date. Use the source-era ministry name in notes and current `MTC` in the normalized regulator field.
- Normalize **National Data Center**, **National Data Centre**, `NDC`, and Lao `ສູນຂໍ້ມູນແຫ່ງຊາດ` as the MTC National Data Center entity unless the source clearly names a private facility.
- Normalize **Louang Namtha/Luang Namtha**, **Louangphabang/Luang Prabang**, **Khammouan/Khammouane**, **Xaignabouli/Xayabury/Sainyabuli**, **Xiangkhouang/Xiengkhouang**, **Bolikhamxai/Bolikhamsai**, **Phongsali/Phongsaly**, **Xekong/Sekong**, **Attapu/Attapeu**.
- Treat **LEED Datacenter** carefully: in Laos sources it can mean the energy-efficient datacenter project or a branded/translated reference to the government digital datacenter, not necessarily a LEED-certified commercial facility. Capture the exact source wording and avoid assuming USGBC LEED certification unless a certificate is found.
- Do not duplicate GDMS National Cloud rows with the 2016 IIJ/Toyota government eco datacenter unless a source explicitly connects them.

---

## 7. Publication Rules

- Publish a facility as confirmed only with an official/operator/utility/SEZ source identifying a location and a datacenter/hosting/cloud function.
- Publish MoUs and feasibility studies as `planned` or `feasibility` with date and parties; never count them as operational MW/racks.
- Leave capacity fields blank or `n/a` when not published. Laos sources rarely disclose MW, racks, tier, floor area, or power redundancy.
- If the only evidence is DataCenterMap or a directory, create a `lead` row or verification note, not a final facility row.
- If a row is a telecom tower/backhaul project, crypto-mining site, online-gambling/scam compound, or generic server room, use a non-standard category or exclude it from the core datacenter count.
