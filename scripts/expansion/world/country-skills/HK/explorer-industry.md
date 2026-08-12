# HK Explorer Industry - Industry / Vendor / Trade-Press Discovery for Hong Kong Datacenters

Date reviewed: 2026-08-12. Country: **HK Hong Kong (HKSAR)**. Division model: **country** (single manifest division: **Hong Kong**; use the 18 District Council districts plus street/estate as the granular layer). Scope: industry, vendor, operator, trade-press, hyperscaler, interconnect, subsea-cable, and aggregator sources for discovering Hong Kong datacenter projects.

Reliability grades:
- **A** = primary source for the specific fact: operator facility page or press release, official cloud-region page, IXP/cable operator page, statutory filing, REIT/report, government/utility source.
- **B** = reputable trade/business press or contractor source with named project facts: Data Center Dynamics (DCD), SCMP, The Standard, RTHK, Mingtiandi, Reuters, Bloomberg, FT, W.Media, Capacity Media, Structure Research, Cushman & Wakefield, JLL, credible engineering/contractor releases.
- **C** = lead source only: DataCenterMap, Baxtel, Cloudscene, DataCenterJournal, datacenters.com, RebootMonkey, DC Hub, broker pages, market-research totals, job ads, event pages, social posts.
- **U** = unsupported; do not count until upgraded.

**Grade rule:** grade facts separately. A-grade operator pages support facility name, location, marketed capacity, and status when stated; they do not prove undisclosed addresses or audited delivered MW. Aggregator pages never become A-grade and should only drive follow-up searches. HK directory counts vary 56-120+ by scope - never treat them as verified totals.

---

## 0. Hong Kong Industry Search Model

Hong Kong has no public datacenter facility registry. Industry enumeration works best as a funnel:

1. Start with **operator facility pages and press releases** for named sites, addresses/estates, status, marketed MW, and certifications.
2. Use **official cloud-region pages** to confirm hyperscaler service-region presence (AWS `ap-east-1`, Azure `eastasia`, Google Cloud `asia-east2`, Alibaba Cloud China (Hong Kong), Tencent Cloud `ap-hongkong`, Huawei Cloud CN-Hong Kong) but do not infer physical sites; Oracle OCI has no HK public cloud region as of this review.
3. Use **trade press** for groundbreakings, financing, construction, tenant, and land-acquisition leads, then upgrade facts through operator/statutory sources.
4. Use **IXP, PeeringDB, and subsea-cable sources** to locate interconnect-heavy buildings and demand clusters (MEGA-i Chai Wan, TKO cable-landing corridor, Tsuen Wan/Kwai Chung colo corridor).
5. Use **aggregator directories** only as lead lists.

Important market geography: HK's strongest physical clusters are **Tseung Kwan O Industrial Estate** (SUNeVision MEGA Plus/MEGA IDC, Digital Realty HKG10, NTT FDC, HKEX, China Mobile/Telecom/Unicom, HKT, cable landing), **Kwai Chung/Tsing Yi** (Equinix HK2, Vantage HKG3, CITIC Telecom Tower, ixTech, Digital Realty HKG11), **Tsuen Wan corridor** (Equinix HK1/HK4-HK6, SUNeVision MEGA Gateway, AirTrunk HKG1 at Tsing Yi), **Chai Wan** (MEGA-i carrier hotel), **Tai Po** (NTT TPDC), **Fo Tan** (MEGA Two), **Cyberport** (AISC), plus emerging **Sandy Ridge (North)**, **Tuen Mun/Yuen Long**, and scattered enterprise/edge sites. Utility split: CLP supplies Kowloon + New Territories (most clusters); HK Electric supplies HK Island (MEGA-i, Cyberport).

Division mapping rule: geocode to address/estate first (GeoInfo Map, map.gov.hk), then assign the 18-district and utility territory. Flag boundary-sensitive entries (Tsuen Wan/Kwai Tsing boundary; TKO vs Sai Kung; Sha Tin/Fo Tan).

---

## 1. Search Vocabulary

English:

```text
data centre OR data center OR datacenter
colocation OR colo
hyperscale data centre
AI data centre OR AI-ready data centre
cloud region OR availability zone
Internet data centre OR IDC
carrier hotel
interconnection OR peering
edge data centre
sovereign cloud OR government cloud
data hosting OR managed hosting
rack space OR cage OR pod
MW OR MVA OR IT load
PUE OR power usage effectiveness
BEAM Plus OR LEED OR TIA-942 OR Uptime Tier
Sandy Ridge OR Northern Metropolis
groundbreaking OR breaks ground OR topped out OR RFS OR commissioned
tenant OR anchor OR pre-leased
land acquisition OR lease OR built-to-suit
cable landing station OR CLS
submarine cable OR undersea cable
Internet exchange OR IXP
fibre OR dark fibre OR cross-connect
```

Traditional Chinese (HK press/government):

```text
數據中心 香港
數據中心 將軍澳
數據中心 葵涌 荃灣
數據中心 大埔 沙田
數據中心 柴灣
數據中心 數碼港
數據中心園區
海底電纜 登陸
互聯網交換中心
沙嶺 數據中心
北部都會區
```

Simplified Chinese (mainland operators):

```text
数据中心 香港
香港 数据中心 新建
```

Status terms to combine:

```text
announces / launches / opens / operational / commissioned / in service
breaks ground / groundbreaking / topping out / under construction
ready for service / RFS / phased / fit-out
land sale / tender / lease / awarded / site selected
BEAM Plus / LEED / TIA-942 / Uptime Tier / PUE / liquid cooling
anchor tenant / pre-leased / hyperscaler tenant
```

---

## 2. Primary Operator Pipeline

High-priority operators with verified HK pages or project sources:

- SUNeVision Holdings (SEHK: 1686) / iAdvantage: https://www.sunevision.com and https://www.iadvantage.net (locations page lists MEGA-i Chai Wan, MEGA Plus TKO, MEGA Two Fo Tan, MEGA Gateway Tsuen Wan, MEGA IDC TKO, ONE and other assets; corporate site claims 280+ MW across 3M sq ft GFA)
- Equinix Hong Kong: https://www.equinix.com/data-centers/asia-pacific-colocation/china-colocation/hong-kong-data-centers (HK1 at Goodman Global Gateway, 168 Yeung Uk Road, Tsuen Wan; HK2 Kwai Chung; HK3-HK6 in corridor; HK6 launched June 2026 per DCD)
- Digital Realty Hong Kong: https://www.digitalrealty.com/data-centers/asia-pacific/hong-kong (HKG10 at 33 Chun Choi Street, Tseung Kwan O; HKG11 at 11 Kin Chuen Street, Kwai Chung; page lists 428k sq ft total colocation space across 2 DCs)
- NTT Hong Kong: https://www.ntt.com.hk/products-and-solutions/data-center (Financial Data Center and Tai Po Data Center; current page states FDC and TPDC together provide 10,000+ racks)
- Telehouse Hong Kong: https://www.telehouse.com/global-data-centers/asia/hong-kong-data-centers/ and https://www.telehouse.net/data-centre-services/hong-kong/ (THHK since 2000; THHK CCC since 2011, TIA Rated 4 claim)
- AirTrunk: https://airtrunk.com (HKG1 Tsing Yi/Tsuen Wan area, 20+ MW, Microsoft anchor, CLP REC deal; HKG2 East New Territories 15+ MW; second-HK-DC announcement URL: https://airtrunk.com/airtrunk-announces-second-hong-kong-data-centre-to-drive-digitalisation/)
- Vantage Data Centers Kwai Chung HKG3: https://vantage-dc.com/data-center-locations/apac/kwai-chung-hong-kong/ (16-floor Kwai Chung DC, 14 MW critical IT load, CLP power, Tier III and LEED Platinum claims)
- GDS Holdings (HK portfolio): several smaller HK DCs (100k-200k sq ft cumulative) plus leased sites per Mingtiandi/analyst commentary; verify GDS HK pages at review
- China Mobile International (Global Network Center, TKO Industrial Estate; SEA-H2X cable from TKO gazetted)
- HKT / PCCW (SkyExchange TKO3 at 2 Chun Yat Street per aggregator; HKT DC portfolio)
- CITIC Telecom CPC / CTM (CITIC Telecom Tower, Kwai Chung)
- HGC Global Communications (HK DC portfolio), HKBN (1310), Towngas Telecom (TGT DC 2, TKO)
- China Telecom Global (TKO DC), China Unicom Global (TKO DC, HK$3bn per SCMP)
- OneAsia Network (HKDCA-affiliated; OneAsia DC in HK), BDx (HKG-1 family), ixTech (88 Container Port Road, Kwai Chung), Telin (HK colo), HKCOLO and other small colos

Operators to search for HK presence/absence before counting: STT GDC, Global Switch (references suggest a TKO HK DC completed ~2024 - confirm on globalswitch.com), CyrusOne, Stack Infrastructure, Digital Edge, Empyrion, Yondr, EdgeConneX, Keppel (no HK DC known - confirm), Princeton Digital Group, Equinix-competitors. Keep them out of counted inventory until an HK facility or statutory/press trail is found.

Operator queries:

```text
site:sunevision.com "MEGA" "data centre"
site:iadvantage.net "MEGA" Hong Kong
site:equinix.com/data-centers/asia-pacific-colocation/china-colocation/hong-kong-data-centers "HK"
site:digitalrealty.com Hong Kong "HKG"
site:ntt.com.hk "data centre" OR "FDC"
site:telehouse.com Hong Kong data centre
site:airtrunk.com Hong Kong "HKG1" OR "HKG2"
site:vantage-dc.com Hong Kong "HKG3"
site:globalswitch.com Hong Kong data centre
"{operator}" Hong Kong "data centre" "ready for service"
"{operator}" Hong Kong "data centre" "BEAM Plus"
"{operator}" Hong Kong "data centre" "MW" "{cluster}"
```

---

## 3. Hyperscaler Presence

Official sources:
- AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones
- Oracle: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Alibaba Cloud: https://www.alibabacloud.com/en/global-locations
- Tencent Cloud: https://www.tencentcloud.com/document/product/213/6091
- Huawei Cloud: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html

Use these as A-grade evidence for service regions only:
- AWS Asia Pacific (Hong Kong) `ap-east-1`, 3 AZs, launched 25 Apr 2019.
- Azure East Asia `eastasia`, physical location Hong Kong SAR.
- Google Cloud Hong Kong `asia-east2` region (official Compute Engine regions/zones docs list Hong Kong zones).
- Alibaba Cloud China (Hong Kong) region (official global locations page lists 3 availability zones).
- Tencent Cloud Hong Kong `ap-hongkong` region (official region/zone docs list Hong Kong zones).
- Huawei Cloud CN-Hong Kong region (official global infrastructure page lists 4 AZs).
- Oracle OCI: no HK public cloud region in the official region list as of this review. Do not count.

Do not map cloud AZs to districts or physical addresses; AWS/Azure publish no HK facility addresses. Tenant reports (e.g., Microsoft as AirTrunk HKG1 anchor; RECs with CLP) are B-grade corroboration of colo demand, not evidence of a Microsoft-owned HK campus.

```text
"AWS" "ap-east-1" "Hong Kong" "Availability Zones"
"Azure" "eastasia" "Hong Kong"
"Google Cloud" "asia-east2" "Hong Kong"
"Alibaba Cloud" "Hong Kong" "region"
"Tencent Cloud" "Hong Kong" "region"
"Huawei Cloud" "Hong Kong" "region"
"{hyperscaler}" Hong Kong "data centre" "lease" OR "anchor"
```

---

## 4. Trade Press and Lead Sources

Reliable B-grade press / contractor sources:
- Data Center Dynamics (DCD): https://www.datacenterdynamics.com (search HK tag)
- South China Morning Post: https://www.scmp.com
- The Standard: https://www.thestandard.com.hk
- RTHK News: https://news.rthk.hk
- Mingtiandi: https://www.mingtiandi.com
- W.Media: https://w.media
- Capacity Media / Telecom Asia for cable and connectivity
- Reuters / Bloomberg / FT for financing and hyperscaler investments
- Contractor/consultant pages naming built projects: J. Roger Preston (HKEX TKO NGDC: https://jrpl.com/en/projects/detail/699/), WT Asia (Pacnet TKO DC), Aurecon, AECOM, Shielder (Global Switch TKO 2024 per https://shieldergroup.com/projects/ - verify)
- Research: Structure Research (https://www.structureresearch.net), Cushman & Wakefield APAC Data Centre Update (search exact report title because public viewer URLs change), JLL (https://research.jllapsites.com/hong-kongs-maturing-data-centre-market/)

Verified useful examples:
- DCD: SUNeVision opens MEGA Gateway (7th DC, Tsuen Wan): https://www.datacenterdynamics.com/en/news/sunevision-opens-new-data-center-in-tsuen-wan-hong-kong/
- DCD: Equinix launches sixth HK DC (June 2026): https://www.datacenterdynamics.com/en/news/equinix-launches-sixth-data-center-in-hong-kong/
- DCD: AirTrunk opens SG + HK DCs (HKG1 20+ MW, near Tsuen Wan): https://www.datacenterdynamics.com/en/news/airtrunk-opens-singapore-hong-kong-data-centers/
- DCD: Digital Realty begins work on second HK DC (HKG11): https://www.datacenterdynamics.com/en/news/digital-realty-begins-work-second-hong-kong-data-center/
- SCMP: SUNeVision to launch city's largest DC (TKO): https://www.scmp.com/tech/enterprises/article/2053003/tech-firm-sunevision-set-launch-citys-largest-data-centre
- Straits Times (2026): Chinese AI boom sends HK DC lease prices soaring: https://www.straitstimes.com/business/companies-markets/chinese-ai-boom-sends-hong-kong-data-centre-prices-soaring
- Mingtiandi: Sandy Ridge Northern Metropolis tender: https://www.mingtiandi.com/real-estate/data-centres/hong-kong-launches-tender-for-mega-sized-data-centre/
- Baxtel news: Angelo Gordon 20 MW Tuen Mun DC: https://baxtel.com/news/angelo-gordon-to-develop-a-20mw-data-center-in-hong-kong

Trade queries:

```text
site:datacenterdynamics.com Hong Kong "data centre" OR "data center"
site:scmp.com Hong Kong "data centre" OR "data center"
site:thestandard.com.hk "data centre" Hong Kong
site:mingtiandi.com "data centre" Hong Kong
site:w.media Hong Kong "data centre"
site:structureresearch.net Hong Kong data centre
site:cushwake.cld.bz "data centre" Hong Kong
"{operator}" Hong Kong "data centre" "groundbreaking"
"{operator}" Hong Kong "data centre" "green loan" OR "financing"
"{operator}" Hong Kong "data centre" "opened" OR "launched"
```

---

## 5. IXPs, Peering, and Subsea Cable Sources

IXP / peering sources:
- HKIX (Hong Kong Internet eXchange, operated by CUHK ITSC): https://www.hkix.net and https://cuhk.edu.hk/hkix/ (one of Asia's largest IXPs; ~300 member networks and multi-Tbps peak per 2025 references - treat member/traffic stats as B/C)
- HKIX PeeringDB org: https://www.peeringdb.com/org/94
- AMS-IX Hong Kong (PoP at MEGA-i since 2019): https://www.ams-ix.net (verify HK page at review)
- DE-CIX where-to-connect lookup: https://www.de-cix.net/en/services/where-to-connect (use this live lookup; the old `/en/locations/hong-kong` path does not resolve, so do not assume a current DE-CIX HK PoP without a current result)
- BBIX Hong Kong: https://www.bbix.net
- Equinix Internet Exchange / Fabric (HK1-HK6): https://www.equinix.com
- PeeringDB facility search (find which buildings host exchanges): https://www.peeringdb.com

Subsea cable sources:
- Submarine Networks Hong Kong stations: https://www.submarinenetworks.com/en/stations/asia/hongkong (Tong Fuk CLS on Lantau = terminal for FNAL/RNAL; Tseung Kwan O CLS at 12 Chun Kwong Street = Telstra/Pacnet-operated, EAC Network cables)
- TeleGeography Submarine Cable Map: https://www.submarinecablemap.com (HK landing points incl. Tong Fuk, Tseung Kwan O, Deep Water Bay, Chung Hom Kok, Ap Lei Chau area - verify each)
- SUNeVision cable landing stations HKIS-1 and HKIS-2 (per DCD)
- SEA-H2X (China Mobile International, TKO to Hainan-Hong Kong Express) gazetted 2025-2026; Sihanoukville-Hong Kong (SHV-HK, China Unicom) gazette references
- OFCA gazette trail: https://www.ofca.gov.hk

Use IX and cable sources to identify interconnect-rich buildings and demand clusters (MEGA-i Chai Wan; TKO industrial estate CLS corridor; Tsuen Wan/Kwai Chung colo corridor). Do not count IXP PoPs or cable landing stations as datacenters unless a separate DC source supports the facility.

```text
site:hkix.net "data centre" OR "MEGA"
site:peeringdb.com "Hong Kong" "{facility}"
site:de-cix.net "Hong Kong"
site:bbix.net "Hong Kong"
"HKIX" "MEGA-i" OR "Chai Wan"
"Tong Fuk" "cable landing station"
"Tseung Kwan O" "cable landing station"
"Deep Water Bay" "cable landing station"
"SEA-H2X" OR "SHV-HK" "submarine cable" Hong Kong
"HKIS-1" OR "HKIS-2" "SUNeVision"
```

---

## 6. Aggregator Directories

Lead lists only:
- DataCenterMap Hong Kong: https://www.datacentermap.com/hong-kong/hong-kong/ (lists ~75 facilities from ~35 operators; includes China Mobile HK 3 Chun Cheong St, TGT DC 2, MEGA Plus, etc.)
- Baxtel Hong Kong: https://baxtel.com/data-center/hong-kong (incl. Digital Realty HKG11, Telehouse CCC, Equinix HK1, AirTrunk HKG2 entries)
- Cloudscene Hong Kong: https://cloudscene.com (facility specs)
- datacenters.com Hong Kong: https://www.datacenters.com/locations/hong-kong (lead list only; re-check any AirTrunk or Digital Realty address against operator pages before use)
- DataCenterJournal / DC Hub: https://dchub.cloud/locations/hk
- RebootMonkey colocation list: https://www.rebootmonkey.com/en/colocation/hong-kong
- Colomap / gotcolo / ocolo for address-level leads

Use aggregators to find facility names, street addresses, and aliases, then confirm through operator, filing, government, or reliable press sources. Treat aggregator facility counts (56-120+ by directory) as C-grade market context only.

```text
site:datacentermap.com/hong-kong "{operator}"
site:baxtel.com "Hong Kong" "{operator}"
site:cloudscene.com Hong Kong "{operator}"
site:datacenters.com "Hong Kong" "{operator}"
site:dchub.cloud/locations/hk "{operator}"
"{operator}" "Hong Kong" "data centre" "{address}"
```

---

## 7. Per-Division Enumeration

Manifest division: **Hong Kong** (single division). Store `division="Hong Kong"` plus `district` (18 districts) and `place_or_estate`.

### 7.1 Tseung Kwan O Industrial Estate (Sai Kung)

Expectation: flagship hyperscale/colo cluster and cable-landing corridor. Known leads: SUNeVision MEGA Plus (299 Wan Po Road) + MEGA IDC; Digital Realty HKG10 (33 Chun Choi Street per Digital Realty); NTT FDC campus; HKEX NGDC (Tier IV); CMI Global Network Center; China Mobile HK DC (3 Chun Cheong Street per aggregator); HKT SkyExchange TKO3 (2 Chun Yat Street per aggregator); China Telecom and China Unicom TKO DCs; Telstra/Pacnet TKO CLS (12 Chun Kwong Street); Towngas Telecom TGT DC 2; Global Switch/ESR/other new HK leads should stay C/U until primary, statutory, or reputable press evidence confirms the facility.

```text
"Tseung Kwan O" "data centre" OR "data center" Hong Kong
"299 Wan Po Road" "MEGA Plus"
"33 Chun Choi Street" "Digital Realty" OR "HKG10"
"NTT" "FDC1" OR "FDC2" "Tseung Kwan O"
"HKEX" "data centre" "Tseung Kwan O"
"China Mobile" OR "China Telecom" OR "China Unicom" "Tseung Kwan O"
"2 Chun Yat Street" OR "SkyExchange"
"TGT" "Towngas" "Tseung Kwan O"
"Global Switch" "Hong Kong" "data centre"
```

### 7.2 Kwai Chung / Tsing Yi (Kwai Tsing)

Expectation: dense carrier-neutral colo corridor. Known leads: Equinix HK2 and nearby Equinix IBX sites; Digital Realty HKG11 (11 Kin Chuen Street, Kwai Chung per Digital Realty); Vantage HKG3 (16-floor, 14 MW critical IT load); CITIC Telecom Tower DC; ixTech (88 Container Port Road); Telin colo; AirTrunk HKG1 in West New Territories/Tsing Yi area (address from aggregators only); plus smaller operators from directory lists.

```text
"Kwai Chung" OR "Kwai Tsing" "data centre" OR "colocation" Hong Kong
"Equinix" "HK2" "3 Shing Yiu Street"
"Vantage" "HKG3" "Kwai Chung"
"11 Kin Chuen Street" "Digital Realty" OR "HKG11"
"CITIC Telecom Tower" "data centre"
"88 Container Port Road" "ixTech"
"AirTrunk" "HKG1" "22-28 Cheung Tat Road"
"Tsing Yi" "data centre" Hong Kong
```

### 7.3 Tsuen Wan (Tsuen Wan)

Expectation: connectivity corridor. Known leads: Equinix HK1 (Goodman Global Gateway, 168 Yeung Uk Road; liquid-cooling-capable), Equinix HK4/HK5/HK6 (HK6 launched Jun 2026), SUNeVision MEGA Gateway (7th DC, ~15,000 cross-connects claimed).

```text
"Tsuen Wan" "data centre" Hong Kong
"168 Yeung Uk Road" OR "Goodman Global Gateway"
"Equinix" "HK4" OR "HK5" OR "HK6" Hong Kong
"MEGA Gateway" "Tsuen Wan"
```

### 7.4 Tai Po (Tai Po)

Expectation: NTT Tai Po Data Centre (TPDC) in Tai Po Industrial Estate; other estate tenants. Address (2 Tai Chee Street per one aggregator) needs NTT confirmation.

```text
"Tai Po" "data centre" Hong Kong
"NTT" "Tai Po Data Centre" OR "TPDC"
"Tai Po Industrial Estate" "data centre" OR "colocation"
```

### 7.5 Sha Tin / Fo Tan (Sha Tin)

Expectation: SUNeVision MEGA Two (Fo Tan, "Mainland Telco & Internet Gateway"), HKSTP/Science Park-adjacent facilities, enterprise DCs.

```text
"Fo Tan" "data centre" Hong Kong
"MEGA Two" OR "MEGA 2" "Fo Tan"
"Sha Tin" OR "Science Park" "data centre" Hong Kong
```

### 7.6 Chai Wan / Hong Kong Island + Cyberport (Eastern / Southern)

Expectation: MEGA-i (Chai Wan) - HK's most-connected carrier hotel (HK Electric territory); Cyberport AISC (AI supercomputing, Phase 1 Dec 2024); other HK Island carrier hotels/enterprise DCs.

```text
"MEGA-i" OR "MEGA I" "Chai Wan"
"Chai Wan" "data centre" OR "carrier hotel" Hong Kong
"Cyberport" "AI Supercomputing Centre" OR "data centre"
"North Point" OR "Quarry Bay" "data centre" Hong Kong
```

### 7.7 Fanling / Sheung Shui / Sandy Ridge (North)

Expectation: Sandy Ridge Data Facility Cluster (awarded Mar 2026 to Hong Kong Range Intelligent Computing Technology Co; 50-year grant; >110,000 sq m; HK$23.8bn commitment) - major future hyperscale/AI cluster; plus existing Fanling/Sheung Shui industrial sites.

```text
"Sandy Ridge" "data centre" OR "data facility cluster"
"Hong Kong Range Intelligent Computing Technology"
"Fanling" OR "Sheung Shui" "data centre" Hong Kong
"Northern Metropolis" "data centre"
```

### 7.8 Tuen Mun / Yuen Long (Tuen Mun / Yuen Long)

Expectation: emerging secondary sites - Angelo Gordon 20 MW at 3 Kin Tai Street, Tuen Mun (application-driven); Tuen Mun Industrial Estate; Yuen Long pockets.

```text
"Tuen Mun" "data centre" Hong Kong
"3 Kin Tai Street" "Angelo Gordon"
"Yuen Long" "data centre" OR "colocation" Hong Kong
```

### 7.9 Other districts - sweep

Kowloon urban districts (Yau Tsim Mong, Sham Shui Po, Kowloon City, Wong Tai Sin, Kwun Tong), Central & Western, Wan Chai, Islands: expect enterprise/edge/carrier-hotel sites; sweep and record `no_projects` only after genuine search.

```text
"Kwun Tong" OR "Kowloon Bay" "colocation" Hong Kong
"Sham Shui Po" OR "Kowloon City" "data centre" Hong Kong
"Lantau" OR "Chek Lap Kok" "data centre" Hong Kong
"Central" OR "Wan Chai" "carrier hotel" Hong Kong
```

---

## 8. Known Industry / Operator Evidence Table

| Facility / project | District / place | Status / fact supported | Evidence | Grade |
| --- | --- | --- | --- | --- |
| SUNeVision MEGA-i | Eastern / Chai Wan | Most-connected carrier hotel; MEGA Campus hub; HKIS-1/HKIS-2 cable landing | SUNeVision/iAdvantage; DCD | A for existence |
| SUNeVision MEGA Plus | Sai Kung / TKO | Flagship DC, 299 Wan Po Road; launched Oct 2017 | SUNeVision; DataCenterMap | A/B |
| SUNeVision MEGA Gateway | Tsuen Wan | 7th DC opened; dark-fibre connected (~15,000 cross-connects claim) | DCD; SUNeVision | A/B |
| SUNeVision MEGA Two | Sha Tin / Fo Tan | Mainland telco/Internet gateway facility | iAdvantage locations page | A for existence |
| SUNeVision MEGA IDC | Sai Kung / TKO | MEGA Campus TKO facility | SUNeVision | A for existence |
| Equinix HK1 | Tsuen Wan | Goodman Global Gateway, 168 Yeung Uk Road; liquid-cooling-capable | Equinix HK1 page | A |
| Equinix HK2 | Tsuen Wan/Kwai Chung corridor | Equinix lists HK2 as a Hong Kong data center in the Tsuen Wan area; street address should be separately confirmed | Equinix page / DataCenterMap | A for existence; C for aggregator address |
| Equinix HK3-HK6 | Tsuen Wan / TKO / Kwai Chung corridor | Equinix lists HK1-HK6; HK6 shown as scheduled/opening in 2026 on Equinix metro page | DCD; Equinix | A for Equinix listing; B for press launch details |
| Digital Realty HKG10 | Sai Kung / TKO | Digital Realty lists HKG10 at 33 Chun Choi Street, Tseung Kwan O, with 200,000 sq ft / 18,581 sq m | Digital Realty | A for facility/address/space |
| Digital Realty HKG11 | Kwai Tsing / Kwai Chung | Digital Realty lists HKG11 at 11 Kin Chuen Street, Kwai Chung, with 228,000 sq ft / 21,182 sq m | Digital Realty | A for facility/address/space |
| NTT FDC campus (FDC1/FDC2) | Sai Kung / TKO | NTT identifies Financial Data Center and Tai Po Data Center portfolio; current page states FDC and TPDC together provide 10,000+ racks | NTT HK pages | A for NTT-stated portfolio facts |
| NTT Tai Po Data Centre | Tai Po | Second NTT HK DC in NTT portfolio | NTT HK | A for existence; address requires separate confirmation |
| Telehouse HK + THHK CCC | verify | Telehouse in HK since 2000; CCC since 2011; TIA Rated 4 claim | Telehouse pages | A for stated facts |
| AirTrunk HKG1 | Kwai Tsing / Tsing Yi | 20+ MW; Microsoft anchor; CLP RECs (Nov 2022); opened 2020 | AirTrunk; DCD | A for arrangement/capacity; address C |
| AirTrunk HKG2 | East NT (cluster TBD) | 15+ MW scalable; anchor delivery targeted mid-2024 | AirTrunk announcement | A for announcement |
| Vantage Kwai Chung HKG3 | Kwai Tsing | 16-floor Kwai Chung DC; 14 MW critical IT load; CLP power; Tier III design/construction and LEED Platinum claims | Vantage page | A for stated facts |
| GDS HK portfolio | verify per site | Several smaller HK DCs + leased sites | Mingtiandi/analyst | C until GDS confirms |
| China Mobile Int'l Global Network Center | Sai Kung / TKO | TKO Industrial Estate; SEA-H2X cable from TKO gazetted | DataCenterMap; gazette | A for gazette; C for facility |
| China Mobile HK DC | Sai Kung / TKO | 3 Chun Cheong Street (~22 MW per aggregator) | DataCenterMap | C |
| HKT SkyExchange TKO3 | Sai Kung / TKO | 2 Chun Yat Street | Aggregators | C |
| HKEX NGDC | Sai Kung / TKO | Tier IV NGDC at TKO Industrial Estate | JRP; HKEX | B for project |
| China Telecom TKO DC | Sai Kung / TKO | TKO DC | C&W APAC DC Update H2 2024 | B/C |
| China Unicom TKO DC | Sai Kung / TKO | HK$3bn TKO DC | SCMP | B |
| Towngas Telecom TGT DC 2 | Sai Kung / TKO | 5-floor, 22,000 sq m standalone building | DataCenterMap | C until TGT confirms |
| Telstra/Pacnet TKO CLS | Sai Kung / TKO | 12 Chun Kwong Street; EAC cables | Submarine Networks | A for CLS facts |
| Tong Fuk CLS | Islands / Lantau | FNAL/RNAL terminal | Submarine Networks | A for CLS facts |
| ixTech DC | Kwai Tsing / Kwai Chung | 88 Container Port Road | inflect/building listing | C |
| Angelo Gordon 20 MW DC | Tuen Mun | 3 Kin Tai Street; plot-ratio increase sought | Baxtel news | C until planning/operator source |
| Cyberport AISC | Southern / Cyberport | Phase 1 Dec 2024, 1,300 PFLOPS claim; 3,000 PFLOPS target | Cyberport; China Daily HK | A for official programme |
| Sandy Ridge Data Facility Cluster | North / Sandy Ridge | Awarded 2 Mar 2026; 50-yr grant; >110,000 sq m; HK$23.8bn commitment; groundbreaking Mar 2026 | ITIB; news.gov.hk; RTHK | A for award |
| HKIX | n/a | CUHK-operated IXP; MEGA-i/Cyberport PoPs | HKIX/CUHK; PeeringDB | A for IXP facts |
| AMS-IX / DE-CIX / BBIX HK PoPs | n/a | Exchange PoPs in HK DC buildings | Operator pages | A for PoP facts |
| AWS ap-east-1 / Azure eastasia / Google asia-east2 / Alibaba / Tencent / Huawei HK | n/a | Cloud service regions | Vendor pages | A for region existence only |
| Oracle OCI HK | n/a | Oracle OCI does not list a Hong Kong public cloud region as of review | Vendor region list | A for absence |

---

## 9. Update / Re-check Cadence

- **Monthly:** operator pages/newsrooms for SUNeVision, Equinix, Digital Realty, NTT, Telehouse, AirTrunk, Vantage, GDS, CMI, China Telecom/Unicom, HKT, HKBN, Towngas Telecom; DCD, SCMP, The Standard, Mingtiandi, W.Media.
- **Quarterly:** hyperscaler region pages (AWS/Azure/Google/Alibaba/Tencent/Huawei zone counts; re-check OCI for any HK entry); PeeringDB/IXP PoPs; BEAM Plus/TIA-942 claims; HKEXnews filings (1686, 6823, 1310, 0008, 1883); aggregator leads (DataCenterMap/Baxtel/datacenters.com).
- **On government-land events:** Sandy Ridge and any new DC tenders (EOI/RFI/tender/award/groundbreaking/energisation); re-check ITIB/DPO then operator announcements then press.
- **Semi-annually:** re-check every C-grade facility lead and every boundary-sensitive district/utility assignment.
- **Annually:** route all known addresses through GeoInfo Map; refresh cable-landing station lists (Submarine Networks / TeleGeography); refresh 18-district mapping.

---

## 10. Red Flags

- Cloud regions and AZs are not physical site counts; AWS/Azure publish no HK addresses.
- Cable landing stations and IXPs are infrastructure leads, not datacenter facilities unless separately supported.
- Operator facility IDs (HKG1, FDC1, TKO3) are not addresses; aggregator addresses are frequently stale/approximated.
- Marketed MW, committed MW, IT load, utility MVA, and delivered live capacity are different facts - keep separate fields.
- Aggregator totals for HK vary 56-120+ by inclusion rules; never quote them as a verified count.
- Sandy Ridge (awarded Mar 2026) is a land grant, not an operational facility; track milestones, not completions.
- Hong Kong's leasehold/industrial-conversion regime means a building can host a DC without any public planning application; absence of a TPB record is not absence of a facility.
- Preserve original place/district/utility evidence; boundary cases (Tsuen Wan/Kwai Tsing, TKO/Sai Kung, Fo Tan/Sha Tin) need GIS checks.

---

## 11. Expected Yield (Honest Scope Note)

- HK is a **major market**: expect a final A/B-grade facility inventory in the **60-120 facility range** (carrier-neutral colo + wholesale + hyperscale + enterprise), depending on how strictly duplicates/edge sites are excluded. Directory counts (56-120+) are C-grade context only.
- Roughly 60-70% of A/B facilities will sit in four clusters: Tseung Kwan O Industrial Estate, Kwai Chung/Tsing Yi, Tsuen Wan corridor, and Chai Wan/MEGA-i + Cyberport. Sandy Ridge will add multiple future pipeline entries (announced/planned/construction) from 2026 onward.
- Expect a long tail of small enterprise/edge colo sites across Kowloon urban districts and HK Island; these are C-grade unless operator/statutory evidence is found.
- Chinese-language press (SCMP Chinese, Ming Pao, HK01, The Standard Chinese edition, mainland operator releases) is essential for mainland-telco and AI-tenant news; English trade press covers the global operators.
- Duplication risk is high (campus vs building, brand vs legal entity, aggregator aliases) - dedupe by street address via GeoInfo Map before counting.
