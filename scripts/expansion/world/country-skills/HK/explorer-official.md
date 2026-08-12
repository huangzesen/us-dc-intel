# HK Explorer Official - Hong Kong Datacenter Enumeration Methodology

Date reviewed: 2026-08-12. Country: **HK Hong Kong (HKSAR)**. Division model: **country** (single division from world-manifest.jsonl: **Hong Kong**). Scope: official, regulatory, statutory, land, planning, utility, procurement, government-data, and cloud-region sources for enumerating Hong Kong datacenter projects.

Reliability grades:
- **A** = primary / legally accountable source for the specific fact cited: Digital Policy Office (DPO), Innovation, Technology and Industry Bureau (ITIB), Town Planning Board (TPB), Planning Department (PlanD), Lands Department (LandsD), Buildings Department (BD), EMSD, EPD, OFCA, CLP Power, HK Electric, Companies Registry, HKEX filings, official cloud-region pages, operator-owned facility pages, official government press releases (info.gov.hk).
- **B** = reliable secondary source: Data Center Dynamics, SCMP, The Standard, RTHK, Mingtiandi, Reuters, Bloomberg, FT, Structure Research, Cushman & Wakefield, JLL, reputable contractor/consultant project pages that accurately describe a statutory process or named project.
- **C** = lead source only: aggregator directories (DataCenterMap, Baxtel, Cloudscene, datacenters.com), broker pages, market-research totals, event pages, social posts, job ads, unsourced lists.
- **U** = unsupported after checking. Keep U only as a temporary work-queue item and never count it as a facility.

**Grade rule:** a grade applies only to the fact the cited source supports. A cloud-region page is A for region existence, not for physical addresses. An operator page is A for facilities, addresses, status, and marketed capacity it publishes, but not for undisclosed site coordinates or audited delivered MW. A press article is B for the named project facts in that article. Aggregators remain C even when accurate. Government tender awards are A for the award fact but not for construction completion.

---

## 0. Hong Kong-Specific Structure Facts

- Hong Kong is a Special Administrative Region (HKSAR) of China with **no state/province tier**. The manifest division layer for HK is a single division: **"Hong Kong"**. For granular routing, use the **18 District Council districts** (official administrative layer: Central & Western, Wan Chai, Eastern, Southern, Yau Tsim Mong, Sham Shui Po, Kowloon City, Wong Tai Sin, Kwun Tong, Kwai Tsing, Tsuen Wan, Tuen Mun, Yuen Long, North, Tai Po, Sha Tin, Sai Kung, Islands) and street-level addresses. Always store `division="Hong Kong"` plus a `district` and `place/estate` field.
- **There is no public national datacenter registry.** Hong Kong also has no public planning-permission database that can be searched directly by use "data centre" end-to-end, but the Town Planning Board publishes planning applications (Sections 12A/16/17 of the Town Planning Ordinance) as open GIS data on DATA.GOV.HK, and the TPB Statutory Planning Portal (ozp.tpb.gov.hk) exposes applications and OZP notes. Enumeration must join: TPB applications, LandsD land sales/grants, BD building records (BRAVO), utility announcements, OFCA cable-landing and telecom licences, HKEX/Companies Registry filings, operator facility pages, and reputable press.
- The official promotion portal for datacenter development is **datacentre.gov.hk** (Data Centre Facilitation Unit, DPO), phone (852)2961 8030. It documents land-use statutory requirements, power supply, facilitation measures, and the Sandy Ridge Data Facility Cluster. Use it as A-grade for programme/policy facts, not for facility inventory.
- **Spelling:** Hong Kong government and local press write **"data centre"** (British spelling); Chinese-language sources use **數據中心 (traditional) / 数据中心 (simplified)**. Global operators and cloud pages often write "data center". Search both spellings and both Chinese forms.
- **Electricity is a two-utility duopoly with fixed franchise territories:** CLP Power supplies Kowloon and the New Territories (incl. Tseung Kwan O, Kwai Chung, Tsing Yi, Tsuen Wan, Sha Tin, Tai Po, Fanling/Sheung Shui, Tuen Mun, Yuen Long); HK Electric supplies Hong Kong Island and Lamma Island. The largest DC clusters (TKO, Kwai Chung, Tsuen Wan) sit in CLP territory; MEGA-i (Chai Wan) and Cyberport (Pok Fu Lam) sit in HK Electric territory. This split matters for grid-capacity, connection, and renewable-energy (REC) evidence trails.
- Hong Kong's DC market is one of the densest in APAC, but aggregate counts vary widely by scope and duplicate handling. Treat all market-size totals and directory counts as C-grade context until reconciled to facility-level A/B evidence.
- **Land tenure is leasehold.** DCs are developed on (a) government land sold/leased by the Lands Department (often with "data centre" use clauses), (b) industrial buildings converted under facilitation measures, or (c) private land. The first industrial land in Tseung Kwan O sold specifically for DC use was in 2013 (JLL research), followed by later TKO parcels (e.g., Wan Po Road site tendered ~2013-2014, won by SUNeVision for MEGA Plus) and the Sandy Ridge cluster (awarded March 2026).
- No moratorium equivalent to Singapore's exists: HK actively promotes DC growth. Policy anchors: 2023 Policy Address (Sandy Ridge change of use), 2024 Policy Address (10-hectare I&T/data-centre site expansion, AI Supercomputing Centre), 2024-25 Budget (HK$3bn AI Subsidy Scheme), Cyberport AISC operations from December 2024.

---

## 1. Official / Regulatory Pipeline

### 1.1 Digital Policy Office (DPO) - Data Centre Facilitation Unit and datacentre.gov.hk

Primary sources:
- DPO Data Centre Facilitation page: https://www.digitalpolicy.gov.hk/en/our_work/digital_infrastructure/industry_development/data_centre/
- Thematic portal "Developing Data Centres in Hong Kong": https://www.datacentre.gov.hk/ (incl. facilitation measures sub-pages such as https://www.datacentre.gov.hk/en/facilitation_measures/energy_efficiency.html)
- Sandy Ridge award press release, 2 Mar 2026: https://www.info.gov.hk/gia/general/202603/02/P2026030200249.htm
- news.gov.hk coverage of Sandy Ridge award: https://www.news.gov.hk/eng/2026/03/20260302/20260302_172856_632.html
- Green Data Centres Practice Guide (DPO): https://www.digitalpolicy.gov.hk/en/our_work/data_governance/policies_standards/green_data_centre/

Verified programme facts (A-grade for policy/programme):
1. The **Sandy Ridge Data Facility Cluster** (North District, east of Lo Wu, Northern Metropolis) is the flagship official DC land pipeline: 2023 Policy Address proposed change of use; EOI June-July 2024; 2024 Policy Address expanded the I&T site to ~10 hectares; RFI March-April 2025; open two-envelope tender 10 Oct - 31 Dec 2025; rezoning completed November 2025; **awarded 2 March 2026 to Hong Kong Range Intelligent Computing Technology Company Limited** on a 50-year land grant for a site of over 110,000 sq m; HK$23.8bn investment commitment within three years (RTHK); groundbreaking reported 28 March 2026 (China Daily Asia).
2. The DPO operates the Data Centre Facilitation Unit and the datacentre.gov.hk portal as one-stop support; use for statutory requirements, power-supply info, and facilitation measures.
3. DPO's Green Data Centres Practice Guide and BEAM Plus Data Centres (BEAM Society) are the green-building assessment trail (see 1.6).

Method: treat DPO/datacentre.gov.hk material as the controlling official trail for **policy, facilitation, and government land programmes**. The Sandy Ridge award is A-grade for the award/lease fact only; do not count it as an operational facility until completion/energisation evidence appears.

```text
site:digitalpolicy.gov.hk "data centre"
site:digitalpolicy.gov.hk "Sandy Ridge"
site:datacentre.gov.hk "data centre"
site:datacentre.gov.hk "facilitation"
"Data Centre Facilitation Unit" "Sandy Ridge"
"Sandy Ridge" "data facility cluster" Hong Kong
"Hong Kong Range Intelligent Computing Technology"
```

### 1.2 ITIB / Policy Address / LegCo - policy and ministerial trail

Primary sources:
- Innovation, Technology and Industry Bureau: https://www.itib.gov.hk
- ITIB "Hong Kong: The Facts - Innovation and Technology" factsheet (DC policy summary): https://www.itib.gov.hk/en/publications/HK_factsheets_I_T_EN.pdf
- Policy Address site: https://www.policyaddress.gov.hk
- LegCo (Hansard, Bills, committee papers): https://www.legco.gov.hk
- GovHK press releases: https://www.info.gov.hk/gia/general/ctoday.htm

Method:
- ITIB is A-grade for policy statements (e.g., Sandy Ridge tender launch/result, AI Supercomputing Centre strategy, 2024 Policy Address data-centre measures).
- LegCo Panel on Innovation, Technology and Industry papers and Finance Committee papers regularly discuss DC land supply, power capacity, and the Sandy Ridge programme; search the LegCo website by "data centre" and "數據中心".
- Ministerial speeches at DC groundbreakings/opening ceremonies are A-grade for the ceremony facts stated (use with care: a groundbreaking speech proves ceremony and announced plans, not live service).

```text
site:itib.gov.hk "data centre"
site:policyaddress.gov.hk "data centre" OR "數據中心"
site:legco.gov.hk "data centre" OR "數據中心"
site:info.gov.hk "Sandy Ridge" OR "data centre" "tender"
site:info.gov.hk "data centre" "groundbreaking"
"LegCo" "data centre" "Hong Kong" "land"
```

### 1.3 Town Planning Board / Planning Department - land use and planning permission

Primary sources:
- Town Planning Board: https://www.info.gov.hk/tpb
- TPB Statutory Planning Portal (interactive OZP + applications): https://www.ozp.tpb.gov.hk/
- TPB planning applications dataset (Sections 12A/16/17, GIS + data dictionary): https://data.gov.hk/en-data/dataset/tpd-tpb1-planning-applications-considered-by-the-tpb
- Digital planning data of statutory plans: https://data.gov.hk/en-data/dataset/tpd-tpb1-digital-planning-data-of-statutory-plans
- Planning Department: https://www.pland.gov.hk

Method:
1. Outline Zoning Plans (OZPs) control land use. Data centres are generally permitted uses (often "industrial" uses in Industrial / Other Specified Uses zones) or require planning permission under Section 16 TPO for non-conforming or special cases (e.g., plot-ratio relaxations, "Other Specified Uses" annotations, Green Belt applications).
2. Download the TPB planning-applications dataset and filter application `use` descriptions for "data centre" / "data center" / "數據中心" / "数据中心". Each application record carries plan/site info; combine with the TPB Portal map view for location.
3. Search OZP Notes for the relevant zones (e.g., "Industrial" (I), "Other Specified Uses" annotated "Data Centre" or "Information Technology") to know whether permission is needed.
4. Do not interpret a missing web result as absence of permission; TPB records are the best public proxy but are not a complete facility registry (many DCs operate under existing industrial uses without a Section 16 application).

```text
site:ozp.tpb.gov.hk "data centre" OR "數據中心"
"Town Planning Board" "data centre" "Section 16" Hong Kong
"Outline Zoning Plan" "data centre" "Industrial" Hong Kong
"Other Specified Uses" "Data Centre" Hong Kong OZP
site:data.gov.hk "planning applications" "data centre"
"plot ratio" "data centre" Hong Kong "Town Planning Board"
```

### 1.4 Lands Department - land sales, grants, lease conditions

Primary sources:
- Lands Department: https://www.landsd.gov.hk
- LandsD land sale / tender programme pages: https://www.landsd.gov.hk/en/land-disposal-transaction/land-sale.html and current tenders: https://www.landsd.gov.hk/en/whats-new/on-going-tenders.html
- Land Registry (titles/leases): https://www.landreg.gov.hk

Method:
- LandsD is the authority for government land disposal. DC-relevant history: first TKO industrial land for DC use sold 2013; Wan Po Road TKO Industrial Estate site tendered 2013-2014 (SCMP coverage; won by SUNeVision - MEGA Plus); Sandy Ridge Data Facility Cluster granted 2026 on 50-year lease.
- Search LandsD tender results, press releases, and lease conditions for "data centre" clauses. A lease with a DC use clause is A-grade for the land-disposal fact and site identity, not for building status.
- Land Registry titles can confirm ownership of private DC buildings (A-grade for ownership when retrieved); search by street address of a known facility.

```text
site:landsd.gov.hk "data centre" OR "數據中心"
site:landsd.gov.hk "Tseung Kwan O" "industrial estate" "tender"
site:landsd.gov.hk "Sandy Ridge"
"Lands Department" "data centre" "lease" Hong Kong
"Tseung Kwan O" "data centre" "land" "sold" Hong Kong
"{address}" "Land Registry" Hong Kong
```

### 1.5 Buildings Department - building control, GFA concessions, BRAVO records

Primary sources:
- Buildings Department: https://www.bd.gov.hk
- BD practice notes and circular letters (Sustainable Building Design, GFA concessions): https://www.bd.gov.hk/en/resources/codes-and-references/practice-notes-and-circular-letters/index.html
- BRAVO (Building Records Access and Viewing On-line): https://www.bd.gov.hk/en/resources/online-tools/BRAVO-online-building-records/index.html and https://bravo.bd.gov.hk

Method:
- BD issues consent to commence works and occupation permits. BRAVO lets you look up approved building plans by address - use it to confirm building existence, gross floor area, and number of storeys for a suspected DC address (A-grade for the building record fact).
- BD practice notes govern GFA concessions for green/sustainable features; DC fit-outs frequently rely on these. Use as process context.
- BD records do not label a building as a datacenter; join with operator/lease/press evidence.

```text
site:bd.gov.hk "data centre" OR "數據中心"
site:bd.gov.hk "gross floor area" "data centre"
"BRAVO" "{address}" Hong Kong
"occupation permit" "{address}" Hong Kong
```

### 1.6 EMSD / BEAM Society - energy efficiency, BEEO, FWCT, BEAM Plus Data Centres

Primary sources:
- EMSD: https://www.emsd.gov.hk
- Building Energy Efficiency Ordinance (BEEO, Cap. 610): https://www.emsd.gov.hk/beeo/en/mibec_beeo.html
- Fresh Water Cooling Towers Scheme (FWCT): https://www.emsd.gov.hk/en/energy_efficiency/fwct_scheme/
- BEAM Society Limited (BEAM Plus Data Centres): https://www.beamsociety.org.hk/en/
- HK Green Building Council BEAM Plus: https://www.hkgbc.org.hk/eng/beam-plus/introduction/

Method:
- Use BEAM Plus Data Centres certification as A-grade certification evidence when found on operator/BEAM pages; it is not proof of completion or live service unless stated.
- FWCT Scheme and BEEO are process context for cooling-water and building energy compliance; DC projects in HK typically rely on fresh-water cooling towers - a practical signal that a building is DC-fit.
- datacentre.gov.hk's energy-efficiency page (verified) lists these as the relevant HK programmes plus the DPO Green Data Centres Practice Guide.

```text
site:emsd.gov.hk "data centre" OR "數據中心"
site:emsd.gov.hk "Fresh Water Cooling Towers" "data centre"
"BEAM Plus" "Data Centres" "{operator}" Hong Kong
"Green Data Centres Practice Guide" Hong Kong
"BEEO" "data centre" Hong Kong
```

### 1.7 EPD / Fire Services - environmental and fire-safety permits

Primary sources:
- Environmental Protection Department: https://www.epd.gov.hk
- Fire Services Department: https://www.hkfsd.gov.hk

Method:
- Large DCs with on-site standby generators may trigger EPD air/noise permits and statutory environmental review for greenfield sites; search EPD for named projects. EPD is A-grade for a permit granted to a named site.
- Fire Services approvals are A-grade for building-safety certification but not publicly searchable by DC use; treat as process context.

```text
site:epd.gov.hk "data centre" OR "數據中心"
site:epd.gov.hk "{operator}" "Tseung Kwan O" OR "Kwai Chung"
"Environmental Permit" "data centre" Hong Kong "{site}"
"Fire Services" "data centre" "fit-out" Hong Kong
```

### 1.8 CLP Power / HK Electric - grid, power supply, RECs

Primary sources:
- CLP Power: https://www.clp.com.hk
- HK Electric: https://www.hkelectric.com

Method:
- There is no public registry of DC grid connections. Use utility sources for: franchise-territory determination (which utility supplies a given address), large-connection announcements, renewable-energy (REC) deals with DC operators, and grid-capacity statements.
- Verified A/B example: AirTrunk and CLP Power launched a first-of-its-kind HK renewable energy solution at AirTrunk's HKG1 in November 2022 matching Microsoft's DC electricity consumption with local RECs (AirTrunk release = A for the arrangement).
- Record which utility territory a facility sits in (Section 0) and search that utility's newsroom with the operator name.

```text
site:clp.com.hk "data centre" OR "數據中心"
site:clp.com.hk "{operator}" "renewable" OR "REC"
site:hkelectric.com "data centre" OR "數據中心"
"{operator}" "CLP" OR "HK Electric" Hong Kong "data centre"
"high voltage" "data centre" Hong Kong "{address}"
```

### 1.9 OFCA - telecoms, cable landing licences, interconnection

Primary sources:
- Office of the Communications Authority: https://www.ofca.gov.hk

Method:
- OFCA issues telecom licences and approves submarine cable landing facilities/works. Gazetted cable-installation notices (e.g., China Mobile International's SEA-H2X system from Tseung Kwan O, gazetted 2025-2026) are A-grade evidence of cable infrastructure and hint at DC/cable-landing clusters.
- OFCA statistics on licensed facilities and data traffic are A-grade for connectivity context, not facility counts.

```text
site:ofca.gov.hk "submarine cable" OR "海纜"
site:ofca.gov.hk "data centre" OR "數據中心"
"SEA-H2X" OR "Sihanoukville-Hong Kong" "submarine cable"
"gazette" "cable landing" Hong Kong "{operator}"
```

### 1.10 Companies Registry / HKEX / listed-company filings - entity and ownership trail

Primary sources:
- Companies Registry: https://www.cr.gov.hk
- ICRIS e-search: https://www.icris.cr.gov.hk
- HKEXnews (listed-company announcements): https://www.hkexnews.hk
- SUNeVision Holdings (SEHK: 1686) corporate pages: https://www.sunevision.com

Method:
- Use Companies Registry/ICRIS to resolve legal entities and SPVs behind DC brands (join key for tenders, leases, financing). A-grade for entity existence.
- Use HKEXnews for listed operators' annual results and asset disclosures. Verified example: SUNeVision (1686.HK, Sun Hung Kai Properties technology arm, HK's largest DC operator) states 280+ MW power capacity across 3 million sq ft GFA on its corporate site (A-grade for marketed portfolio).
- Listed DC/telecom plays to monitor: SUNeVision (1686), HKT (6823), HKBN (1310), PCCW (0008), CITIC Telecom International (1883).
- Annual reports are A-grade for portfolio composition and ownership; they usually disclose campuses (MEGA-i, MEGA Plus, MEGA Gateway, MEGA IDC, MEGA Two) rather than every sub-building.

```text
site:cr.gov.hk "{legal_entity}"
site:icris.cr.gov.hk "{legal_entity}"
site:hkexnews.hk "{operator}" "data centre"
site:sunevision.com "MEGA" "data centre"
"{operator}" "annual report" "data centre" Hong Kong "MW"
```

### 1.11 GovHK / DATA.GOV.HK / GeoInfo Map - geospatial and open data

Primary sources:
- GovHK: https://www.gov.hk
- Open data portal: https://data.gov.hk (incl. TPB planning applications, DPO Address Lookup Service, LandsD/BD datasets)
- GeoInfo Map (official map; addresses, districts, planning areas): https://www.map.gov.hk
- DPO Address Lookup Service (ALS) dataset: https://data.gov.hk/en-data/dataset/hk-dpo-als_01-als

Method:
- GeoInfo Map is the authoritative geocoder for HK addresses; record street/estate, district, and grid reference for every candidate facility.
- Use DATA.GOV.HK datasets (planning applications, address lookup) for bulk joins.

```text
"{address}" site:map.gov.hk
"{address}" "GeoInfo Map" Hong Kong
site:data.gov.hk "data centre" OR "數據中心"
```

### 1.12 Cloud-region official pages

Primary sources:
- AWS Regions/AZs: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations and Compute Engine regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones
- Oracle OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Alibaba Cloud global locations: https://www.alibabacloud.com/en/global-locations
- Tencent Cloud regions/zones: https://www.tencentcloud.com/document/product/213/6091
- Huawei Cloud global infrastructure: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html

Verified region facts (A-grade for region existence only):
- **AWS Asia Pacific (Hong Kong), `ap-east-1`** - launched 25 April 2019, 3 AZs (ap-east-1a/b/c) per AWS docs and launch coverage (AP News).
- **Microsoft Azure East Asia, region ID `eastasia`** - physical location Hong Kong SAR per Microsoft Learn region references.
- **Google Cloud Hong Kong, `asia-east2`** - official Compute Engine region/zones documentation lists Hong Kong zones. This is A-grade for cloud-region existence only, not for facility address or operator-owned campus evidence.
- **Alibaba Cloud China (Hong Kong)** - official global locations page lists 3 availability zones and 2014 release.
- **Tencent Cloud Hong Kong, `ap-hongkong`** - official region/zone tables list Hong Kong zones.
- **Huawei Cloud CN-Hong Kong** - official global infrastructure page lists Hong Kong, China with 4 AZs.
- **Oracle OCI: NO Hong Kong region** in the official OCI region list as of this review (closest: Singapore, Seoul, Tokyo, Osaka, Mumbai, Hyderabad). Do not count an OCI HK region.

Rule: cloud-region facts are A-grade for service-region existence only; they never identify campuses, addresses, districts, or MW. Do not map any cloud AZ to a physical district unless the vendor publishes a site-level source, which hyperscalers generally do not.

```text
"AWS" "ap-east-1" "Hong Kong" "Availability Zones"
"Azure" "eastasia" "Hong Kong"
"Google Cloud" "asia-east2" "Hong Kong"
"Alibaba Cloud" "Hong Kong" "region"
"Tencent Cloud" "Hong Kong" "region"
"Huawei Cloud" "Hong Kong" "region"
"Oracle Cloud" "Hong Kong" region - absence check
```

### 1.13 InvestHK / HKTDC / HKPC - investment promotion and market intelligence

Primary sources:
- InvestHK: https://www.investhk.gov.hk (sector pages incl. data centres / innovation & technology)
- HKTDC research: https://research.hktdc.com (industry reports incl. data centre / I&T)
- HKPC: https://www.hkpc.org (Sandy Ridge support statement 2 Mar 2026 = B-grade corroboration of the award)

Method:
- InvestHK case studies and sector pages are A-grade for government positioning claims but rarely provide facility addresses; use for investor-commitment corroboration.
- HKTDC research reports give market sizing (C-grade for counts, B-grade for described trends if sourced).

```text
site:investhk.gov.hk "data centre" OR "數據中心"
site:research.hktdc.com "data centre" Hong Kong
site:hkpc.org "data centre" OR "Sandy Ridge"
```

---

## 2. Search Vocabulary

English:

```text
"data centre" Hong Kong
"data center" Hong Kong
"datacenter" Hong Kong
"colocation" OR "colo" Hong Kong
"hyperscale data centre" Hong Kong
"AI data centre" OR "AI-ready" Hong Kong
"Internet data centre" OR "IDC" Hong Kong
"carrier hotel" Hong Kong
"cloud region" OR "availability zone" Hong Kong
"cable landing station" Hong Kong
"submarine cable" OR "undersea cable" Hong Kong
"Internet exchange" OR "IXP" OR "peering" Hong Kong
"Tier IV" OR "Tier 4" data centre Hong Kong
"planning permission" "data centre" Hong Kong
"Town Planning Board" "data centre"
"lease" "data centre" "Lands Department"
"industrial building" "data centre" "conversion" Hong Kong
"Northern Metropolis" "data centre"
"Sandy Ridge"
"Tseung Kwan O" "data centre"
"Kwai Chung" OR "Tsing Yi" "data centre"
"Tsuen Wan" "data centre"
"Tai Po" OR "Sha Tin" OR "Fo Tan" "data centre"
"Fanling" OR "Sheung Shui" OR "Yuen Long" OR "Tuen Mun" "data centre"
"Chai Wan" OR "Cyberport" "data centre"
"MW" "data centre" Hong Kong "{operator}"
"REC" OR "renewable" "data centre" Hong Kong
"BEAM Plus" "data centre" Hong Kong
```

Traditional Chinese (official HK usage; use 繁中 first, 简中 for mainland-operator press):

```text
數據中心 香港
數據中心 將軍澳
數據中心 葵涌
數據中心 荃灣
數據中心 大埔
數據中心 沙田
數據中心 粉嶺 上水
數據中心 柴灣
數據中心 數碼港
數據中心園區 香港
高可用數據中心 香港
海底電纜 香港 登陸點
互聯網交換中心 香港
沙嶺 數據中心
北部都會區 數據中心
```

Simplified Chinese (mainland operators/aggregators):

```text
数据中心 香港
数据中心 将军澳
香港 数据中心 新建
沙岭 数据中心
```

Status terms to combine:

```text
announces / launches / opens / operational / commissioned / in service
breaks ground / groundbreaking / topping out / under construction
land sale / tender / lease / grant / awarded / site selected
planning application / permission / rezoning / lease modification
ready for service / RFS / phased / fit-out
BEAM Plus / LEED / TIA-942 / Uptime Tier / PUE / liquid cooling
```

---

## 3. Per-Division Enumeration

Manifest division: **Hong Kong** (single division). Always store three fields:
- `division`: "Hong Kong"
- `district`: one of the 18 District Council districts
- `place_or_estate`: street/estate/industrial area (e.g., "Tseung Kwan O Industrial Estate", "Kwai Chung", "Goodman Global Gateway")

Hong Kong DC geography concentrates in a small number of industrial clusters. Use the following cluster-by-cluster approach inside the single division.

### 3.1 Tseung Kwan O Industrial Estate (Sai Kung district) - flagship cluster

Likely pattern: HK's largest hyperscale/colo cluster: SUNeVision MEGA Plus (299 Wan Po Road) and MEGA IDC; Digital Realty HKG10 (33 Chun Choi Street per Digital Realty); NTT FDC campus and Tai Po/FDC portfolio (operator page states FDC and TPDC together provide 10,000+ racks); HKEX new data centre (Tier IV NGDC); China Mobile International Global Network Center / China Mobile HK DC (3 Chun Cheong Street per aggregator); HKT SkyExchange TKO3 (2 Chun Yat Street per aggregator); China Telecom TKO DC; China Unicom TKO DC (SCMP-reported); Pacnet/Telstra TKO cable landing station (12 Chun Kwong Street); Towngas Telecom TGT DC 2. Watch for Global Switch/ESR/other new HK entries, but keep them C/U until an operator, statutory, or reputable press source confirms the facility.

```text
"Tseung Kwan O" "data centre" Hong Kong
"Tseung Kwan O Industrial Estate" "data centre"
"299 Wan Po Road"
"33 Chun Choi Street" "Digital Realty" OR "HKG10"
"NTT" "FDC" "Tseung Kwan O"
"HKEX" "data centre" "Tseung Kwan O"
"China Mobile" OR "China Telecom" OR "China Unicom" "Tseung Kwan O" "data centre"
"2 Chun Yat Street" OR "12 Chun Kwong Street" "cable landing"
"Global Switch" "Hong Kong" "data centre"
```

### 3.2 Kwai Chung / Tsing Yi (Kwai Tsing district) - dense colo corridor

Likely pattern: multi-tenant carrier-neutral colo in converted industrial buildings: Equinix HK2 and other Equinix leased IBX sites in the wider Tsuen Wan/Kwai Chung/TKO corridor; Digital Realty HKG11 (11 Kin Chuen Street, Kwai Chung per Digital Realty); Vantage Kwai Chung HKG3 (16-floor, 14 MW critical IT load per Vantage); CITIC Telecom Tower DC (CTM), ixTech DC (88 Container Port Road), Telin-operated facility, plus smaller operators.

```text
"Kwai Chung" "data centre" Hong Kong
"3 Shing Yiu Street" OR "Kerry Warehouse" "Equinix"
"Vantage" "Kwai Chung" "HKG3"
"11 Kin Chuen Street" "Digital Realty" OR "HKG11"
"88 Container Port Road" "data centre"
"CITIC Telecom Tower" "data centre"
"Kwai Tsing" "colocation" Hong Kong
```

### 3.3 Tsuen Wan (Tsuen Wan district) - connectivity corridor

Likely pattern: Equinix HK1 (Goodman Global Gateway, 168 Yeung Uk Road), Equinix HK4/HK5/HK6 (Tsuen Wan area; HK6 launched June 2026 per DCD), SUNeVision MEGA Gateway (Tsuen Wan, 7th SUNeVision DC), AirTrunk HKG1 nearby at Tsing Yi (22-28 Cheung Tat Road; converted 8-storey industrial building, 20+ MW, Microsoft anchor, opened 2020).

```text
"Tsuen Wan" "data centre" Hong Kong
"168 Yeung Uk Road" OR "Goodman Global Gateway" "Equinix"
"Equinix" "HK6" Hong Kong
"MEGA Gateway" "Tsuen Wan"
"AirTrunk" "HKG1" "Tsing Yi" OR "Tsuen Wan"
"22-28 Cheung Tat Road"
```

### 3.4 Tai Po (Tai Po district)

Likely pattern: NTT Tai Po Data Centre (TPDC, Tai Po Industrial Estate; one aggregator reference gives 2 Tai Chee Street - verify), plus other Tai Po Industrial Estate tenants.

```text
"Tai Po" "data centre" Hong Kong
"NTT" "Tai Po Data Centre" OR "TPDC"
"Tai Po Industrial Estate" "data centre"
```

### 3.5 Sha Tin / Fo Tan (Sha Tin district)

Likely pattern: SUNeVision MEGA Two (Fo Tan - "Mainland Telco & Internet Gateway" per iAdvantage), HKSTP-adjacent facilities, Science Park edge/enterprise DCs.

```text
"Fo Tan" "data centre" Hong Kong
"MEGA Two" OR "MEGA 2" "Fo Tan"
"Sha Tin" "data centre" Hong Kong
"Hong Kong Science Park" "data centre"
```

### 3.6 Chai Wan / Hong Kong Island (Eastern district) + Cyberport (Southern district)

Likely pattern: SUNeVision MEGA-i (Chai Wan) - the most-connected carrier hotel / telco hub on HK Island; Cyberport (Pok Fu Lam) hosts the AI Supercomputing Centre (AISC) plus enterprise DCs; other HK Island carrier hotels (North Point, Quarry Bay, Central) exist - search per address.

```text
"Chai Wan" "data centre" Hong Kong
"MEGA-i" OR "MEGA I" "Chai Wan"
"Cyberport" "data centre" OR "AI Supercomputing Centre"
"North Point" OR "Quarry Bay" OR "Central" "carrier hotel" Hong Kong
"HK Electric" "data centre" "Hong Kong Island"
```

### 3.7 Fanling / Sheung Shui (North district) - Sandy Ridge watchlist

Likely pattern: the Sandy Ridge Data Facility Cluster (awarded Mar 2026, 50-year grant, >110,000 sq m, HK$23.8bn commitment, groundbreaking Mar 2026) will become a major hyperscale/AI cluster; track tender milestones and tenant/build announcements. Also check Fanling/Sheung Shui industrial areas for existing facilities.

```text
"Sandy Ridge" "data centre" OR "data facility cluster"
"Fanling" OR "Sheung Shui" "data centre" Hong Kong
"Northern Metropolis" "data centre" Hong Kong
"Lo Wu" "data centre"
```

### 3.8 Tuen Mun / Yuen Long (Tuen Mun & Yuen Long districts)

Likely pattern: emerging secondary sites: Angelo Gordon 20 MW DC at 3 Kin Tai Street, Tuen Mun (planning-application-driven; Baxtel news), Tuen Mun Industrial Estate tenants, Yuen Long industrial pockets. Power/grid constraints keep these smaller, but watch planning applications.

```text
"Tuen Mun" "data centre" Hong Kong
"3 Kin Tai Street" "data centre"
"Angelo Gordon" "data centre" Hong Kong
"Yuen Long" "data centre" OR "colocation" Hong Kong
```

### 3.9 Other districts - sweep

Remaining districts (Yau Tsim Mong, Sham Shui Po, Kowloon City, Wong Tai Sin, Kwun Tong; Central & Western, Wan Chai; Islands incl. Lantau/Chek Lap Kok) - expect enterprise/edge/carrier-hotel density in Kowloon East (Kwun Tong) and occasional airport-adjacent sites; sweep with district-name queries and record `no_projects` only after a genuine search shows nothing.

```text
"Kwun Tong" OR "Kowloon Bay" "data centre" OR "colocation" Hong Kong
"Sham Shui Po" OR "Kowloon City" "data centre" Hong Kong
"Lantau" OR "Chek Lap Kok" "data centre" Hong Kong
"Wan Chai" OR "Admiralty" OR "Central" "data centre" Hong Kong
```

---

## 4. Known Official / Primary-Source Leads

These are anchors to seed enumeration, not a complete facility registry. Re-verify every URL and fact at review time.

| Item | District / place | Status / fact supported | Evidence | Grade |
| --- | --- | --- | --- | --- |
| Sandy Ridge Data Facility Cluster | North / Sandy Ridge (Lo Wu) | >110,000 sq m site awarded 2 Mar 2026 on 50-year grant to Hong Kong Range Intelligent Computing Technology Co Ltd; HK$23.8bn investment commitment in 3 years; groundbreaking reported 28 Mar 2026 | ITIB announcement; news.gov.hk 20260302; RTHK 20260303; China Daily Asia | A for award/lease; project status to be tracked |
| TKO first DC land sale (2013) | Sai Kung / TKO | First government industrial land in TKO sold for DC use in 2013; Wan Po Road TKO site tendered ~2013-14 (won by SUNeVision for MEGA Plus) | JLL research; SCMP property coverage | B (JLL), B/A for tender reports |
| SUNeVision MEGA Plus | Sai Kung / TKO | Flagship high-tier DC at 299 Wan Po Road, TKO; launched Oct 2017; part of MEGA Campus | SUNeVision/iAdvantage pages; DataCenterMap | A for facility/campus; C for sub-details |
| SUNeVision MEGA-i | Eastern / Chai Wan | Most-connected carrier hotel / telco hub; part of MEGA Campus; hosts HKIS-1/HKIS-2 cable landing | SUNeVision/iAdvantage pages; DCD | A for facility existence |
| SUNeVision MEGA Gateway | Tsuen Wan | 7th SUNeVision DC; opened (DCD coverage); connected via dark fibre (approx. 15,000 cross-connects claimed) | DCD; SUNeVision | A/B |
| Digital Realty HKG10 | Sai Kung / TKO | Digital Realty lists HKG10 at 33 Chun Choi Street, Tseung Kwan O, with 200,000 sq ft / 18,581 sq m | Digital Realty HK page | A for facility/address/space |
| Digital Realty HKG11 | Kwai Tsing / Kwai Chung | Digital Realty lists HKG11 at 11 Kin Chuen Street, Kwai Chung, with 228,000 sq ft / 21,182 sq m | Digital Realty HK page | A for facility/address/space |
| NTT Hong Kong FDC campus | Sai Kung / TKO | NTT identifies Financial Data Center and Tai Po Data Center portfolio; current page states FDC and TPDC together provide 10,000+ racks | NTT HK data-centre page | A for portfolio facts stated by NTT |
| NTT Tai Po Data Centre (TPDC) | Tai Po | Second NTT HK DC in the NTT portfolio | NTT HK data-centre page | A for existence; address requires separate confirmation |
| Telehouse Hong Kong (THHK) + THHK CCC | verify per facility | First Telehouse site in Greater China (2000); CCC (Cloud Computing Complex) since 2011; first HK DC with TIA Rated 4 claim | Telehouse pages | A for stated facts |
| Equinix HK1 | Tsuen Wan | Goodman Global Gateway, 168 Yeung Uk Road; Tsuen Wan area; liquid-cooling-capable | Equinix HK1 page | A |
| Equinix HK2 | Tsuen Wan/Kwai Chung corridor | Equinix lists HK2 as a Hong Kong data center in the Tsuen Wan area; street address should be confirmed on the specific HK2 page or another primary source | Equinix HK metro page; DataCenterMap lead | A for Equinix HK2 existence; C for aggregator address |
| Equinix HK6 (and HK3-HK5) | Tsuen Wan / TKO / Kwai Chung corridor | Equinix lists HK1-HK6; HK6 shown as scheduled/opening in 2026 on Equinix metro page | Equinix HK page; DCD for launch article | A for Equinix listing; B for press launch details |
| Vantage Kwai Chung HKG3 | Kwai Tsing / Kwai Chung | 16-floor Kwai Chung DC; 14 MW critical IT load; CLP power; Tier III design/construction and LEED Platinum claims | Vantage page (vantage-dc.com) | A for stated operator facts |
| AirTrunk HKG1 | Kwai Tsing / Tsing Yi | 22-28 Cheung Tat Road (aggregator); converted 8-storey industrial building; 20+ MW; Microsoft anchor; CLP REC deal Nov 2022; opened 2020 | AirTrunk releases; DCD | A for arrangement/capacity claims; address C until AirTrunk confirms |
| AirTrunk HKG2 | East New Territories (cluster TBD) | Scalable to 15+ MW; anchor delivery targeted mid-2024 | AirTrunk release (announcement) | A for announcement |
| China Mobile International Global Network Center | Sai Kung / TKO | CMI DC at TKO Industrial Estate; SEA-H2X cable installation from TKO gazetted | DataCenterMap; gazette/Bastille Post | A for gazette; C for facility specs |
| China Mobile HK DC | Sai Kung / TKO | 3 Chun Cheong Street, TKO Industrial Estate (~22 MW per aggregator) | DataCenterMap | C until CMI confirms |
| HKT SkyExchange TKO3 | Sai Kung / TKO | 2 Chun Yat Street | Aggregator listings | C until HKT confirms |
| HKEX new data centre | Sai Kung / TKO | Tier IV NGDC at TKO Industrial Estate | JRP project page; HKEX disclosures | B for project; A for HKEX ownership if filed |
| China Telecom TKO DC | Sai Kung / TKO | TKO data centre referenced in C&W APAC DC Update H2 2024 | C&W report | B/C |
| China Unicom TKO DC | Sai Kung / TKO | HK$3bn TKO DC (SCMP-reported) | SCMP via research literature | B |
| Angelo Gordon 20 MW DC | Tuen Mun | 3 Kin Tai Street, Tuen Mun; plot-ratio increase sought | Baxtel news (application-driven) | C until planning/operator source confirms |
| Cyberport AI Supercomputing Centre (AISC) | Southern / Cyberport | Phase 1 operations commenced Dec 2024 (1,300 PFLOPS claimed; NVIDIA H800); target 3,000 PFLOPS end-2025; HK$3bn AI Subsidy Scheme | Cyberport AISC pages; China Daily HK | A for official programme |
| HKEX/listed DC operators (1686, 6823, 1310, 0008, 1883) | n/a | Listed-company disclosure trail for DC portfolios and capex | HKEXnews | A for filings |
| AWS ap-east-1 | n/a | HK region, 3 AZs, launched 25 Apr 2019 | AWS docs; AP News | A for cloud region |
| Azure East Asia (eastasia) | n/a | HK-based Azure region | Microsoft Learn | A for cloud region |
| Alibaba / Tencent / Huawei HK regions | n/a | HK cloud regions listed by each vendor | Vendor pages | A for region existence |
| Google Cloud asia-east2 / Oracle OCI | n/a | Google Cloud lists Hong Kong (`asia-east2`) zones; Oracle OCI does not list a Hong Kong public cloud region | Vendor region lists | A for cloud-region existence/absence only |

Do not count policy targets, land grants, cloud AZ counts, IXP PoPs, or cable landing stations as datacenter facilities.

---

## 5. Validation Checklist

For every candidate row:
1. Confirm the source URL is live and the page actually states the claimed fact (review layer must click every A-grade URL).
2. Split facts by grade: existence, address, capacity, status, certification, ownership, cloud-region existence, district, and utility territory may each have different grades.
3. Geocode with GeoInfo Map (map.gov.hk) and record street/estate + 18-district assignment + CLP/HK Electric territory.
4. Join entity names through Companies Registry/ICRIS and HKEX filings before counting a branded facility.
5. For government-land projects (TKO, Sandy Ridge), track tender -> award -> rezoning -> construction -> energisation milestones separately.
6. For facility counts, use only A/B facility evidence. Aggregator totals are lead lists only (HK counts vary 56-120+ by scope).

---

## 6. Re-check Cadence

- **Monthly:** DPO/ITIB newsrooms; datacentre.gov.hk updates; Sandy Ridge construction milestones; info.gov.hk DC-related press releases; operator news pages.
- **Quarterly:** TPB planning-applications dataset re-download + filter; LandsD tender results; OFCA gazettes (cables); HKEXnews filings for 1686/6823/1310/0008/1883; cloud-region pages (Alibaba/Tencent/Huawei zone counts).
- **On milestones:** Sandy Ridge and any new government-land DC tenders (EOI/RFI/tender/award/groundbreaking/energisation); major operator openings (Equinix/Digital Realty/Vantage/AirTrunk/GDS).
- **Semi-annually:** re-run all operator and aggregator lead queries; re-check every C-grade facility lead and every boundary-sensitive district assignment.
- **Annually:** refresh 18-district mapping (stable, but re-verify street-level assignments after new roads/estates); refresh cloud-region lists and do not convert region/AZ changes into facility counts.

---

## 7. Red Flags

- A cloud region is not a physical facility list (AWS/Azure publish no HK addresses).
- A land grant/tender award (e.g., Sandy Ridge) is not proof of a completed building.
- Directory counts for HK vary wildly (56 to 120+ facilities) because they mix hyperscale, colo, edge, cloud, and duplicate entries; never quote them as a verified total.
- "MEGA Campus" is a marketing umbrella for several buildings; count each building only with its own evidence.
- Aggregator addresses (e.g., AirTrunk HKG1, Equinix HK2, China Mobile 3 Chun Cheong St) are frequently stale or approximated - always confirm on operator pages.
- Leasehold land and industrial-building conversions mean a facility's use class can change without a Section 16 application; absence of a TPB application is NOT evidence of absence of a DC.
- Google Cloud has an HK compute region (`asia-east2`); Oracle OCI does not list an HK public cloud region as of review. Any physical-facility claim still needs site-level evidence.
- Preserve original address/district/utility evidence; utility territory (CLP vs HK Electric) determines the power-capacity trail to follow.
