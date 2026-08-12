# PH Explorer Industry - Philippines Datacenter Enumeration Methodology

Date: 2026-08-12. Scope: Philippines datacenter enumeration through operators, colo providers, cloud infrastructure, interconnection, cable landing stations, industry bodies, trade press, and market databases. Use this file for discovery and industry validation, then corroborate with official trails in `explorer-official.md`.

Reliability grades:

- **A** = operator/government/regulator/utility/planning-EIA/exchange/annual-report/official cloud page.
- **B** = established trade or Philippine business press with named project facts, or contractor/developer releases with named scope.
- **C** = directories, broker snippets, conference agendas, social posts, reposted MoUs, market reports without source detail, or unsourced facility lists.

Current regional frame: enumerate against **18 PSGC regions**. The Negros Island Region (NIR) was created by RA 12000 and appears in PSA PSGC updates; Bacolod/Negros Occidental, Negros Oriental, and Siquijor should be assigned to NIR for current records.

## 0. Philippines Industry Search Model

There is no complete public facility registry. Build the industry census by triangulating:

1. **Operator pages and newsrooms**: VITRO/ePLDT, Equinix, STT GDC Philippines, Converge, DITO, SpaceDC, EdgeConneX, DAMAC/EDGNEX, Flow/A-Flow, Beeinfotech, Eastern Communications, PT&T, and local hosting/managed-service providers.
2. **Official cross-checks**: LGU permits, NTC DTIP/VAS/PTE records, DENR-EMB ECC/CNC, utility/ERC/NGCP power evidence, PEZA/BOI incentives, and DICT/GovCloud records.
3. **Interconnection evidence**: PHOpenIX, PhIX, GetaFIX, GIX/NIGX, AMS-IX Manila, BBIX Philippines, PeeringDB, Cloudscene, DataCenterMap, Baxtel, datacenters.com, ocolo, colomap, and operator carrier lists.
4. **Trade and business press**: DCD, W.Media, PNA, BusinessWorld, Inquirer, Philstar, Manila Bulletin, Manila Standard, BusinessMirror, Rappler, Reuters/AP, Bilyonaryo, ABS-CBN, GMA, contractor releases.

Practical geography:

- **NCR**: mature colo/interconnection hub: Makati, Pasig, Taguig/BGC, Quezon City/Fairview, Parañaque, Muntinlupa/Alabang, Pasay/MOA.
- **CALABARZON**: hyperscale growth corridor: Laguna/Sta. Rosa, Cavite/General Trias, Rizal/Cainta, Batangas/Nasugbu and industrial estates.
- **Central Luzon**: Clark/Angeles, New Clark City/Tarlac, Subic, Bataan, Bulacan, Aurora/Baler cable landing.
- **Central Visayas**: Cebu City/Mandaue/Lapu-Lapu after excluding NIR components.
- **Davao Region**: Davao City, Digos cable landing, Davao Light service area.
- **NIR / Western Visayas / Northern Mindanao / Ilocos-CAR / Cagayan Valley**: regional edge, BPO, cable-landing, government and disaster-recovery leads.

Always resolve "Manila" or "Greater Manila" marketing labels to the physical city/province. Cainta is Rizal/CALABARZON; Sta. Rosa is Laguna/CALABARZON; General Trias is Cavite/CALABARZON; Clark is Pampanga/Central Luzon; Baguio is CAR; Bacolod is NIR.

## 1. Query Vocabulary

Core terms:

```text
data center / data centre / datacenter
colocation / colo / carrier-neutral
hyperscale / AI-ready / AI data center / GPU-as-a-Service
cloud region / availability zone / local zone / Direct Connect
carrier hotel / interconnection / peering / internet exchange / IXP
edge data center / disaster recovery / DR site
green data center / renewable-powered data center
sovereign cloud / GovCloud
data hosting / managed hosting / bare metal
wholesale colocation / retail colocation
```

Filipino/Taglish variants:

```text
data center / datacenter
malaking data center
pasilidad ng data
serbisyo ng cloud
kolokasyon
internet exchange
cable landing station / landing ng cable
```

Status and evidence words:

```text
announces / launches / opens / ready for service / commercial operation / operational
groundbreaking / breaks ground / topped out / under construction
delivered / energized / dedicated substation
land acquisition / acquires land / built-to-suit / lease
anchor tenant / hyperscaler tenant / NVIDIA
power secured / Meralco / PSA / MW / MVA
PEZA / BOI / SIPP / NTC / VAS / DTIP / ECC / CNC
MoU / memorandum of understanding / investment pledge
```

## 2. Operator Landscape

Treat this as a seed list, not a final inventory. Capacity and status move quickly; pull current official pages before storing MW.

### 2.1 Telco and Incumbent-Anchored Colo

| Operator | Facility and evidence anchors | Regions | Grade |
|---|---|---|---|
| **VITRO / ePLDT / PLDT Group** | Official VITRO/ePLDT pages list the portfolio. Known sites include VITRO Makati 1/2, VITRO Pasig, VITRO Parañaque, VITRO Sta. Rosa in Pulong Santa Cruz, Laguna, VITRO Cebu 1 and 2, and a planned/announced Cavite site. VITRO Sta. Rosa is officially positioned as an AI-ready hyperscale facility with dedicated substation and 50MW-class public claims. | NCR, CALABARZON, Central Visayas | A for official pages; B for press on capacity |
| **STT GDC Philippines** | Globe/Ayala/STT platform. Official pages cover Makati/Manila legacy sites, STT Cavite, STT Davao, and STT Fairview. STT Fairview 1 was announced as ready for service in Q2 2025; full Fairview campus target is 124MW IT capacity. | NCR, CALABARZON, Davao | A |
| **Converge ICT** | Fiber operator with data-center and cable-landing roles. Known/lead sites include Pasig/Reliance IT Center, Clark/internal infrastructure, Parañaque hyperscale plans, and Davao/Baler cable-landing ecosystem. | NCR, Central Luzon, Davao | A/B |
| **DITO Telecommunity** | DITO Clark Super Core Data Center / Clark Global City NOC/R&D campus and carrier infrastructure. | Central Luzon | A/B |
| **Eastern Communications / ETPI** | Legacy international carrier with enterprise cloud/connectivity and possible carrier-hotel roles; verify facility specifics through NTC, PeeringDB, and operator pages. | NCR | B |
| **PT&T** | Legacy carrier/data services; use as telecom/interconnection seed, not confirmed colo unless facility source is found. | NCR | B/C |
| **Globe / Innove / STT GDC JV links** | Globe datacenter assets were part of the STT GDC Philippines platform; Globe/Innove also matter for CLS and enterprise connectivity. | NCR, CALABARZON, Davao | A/B |

### 2.2 Carrier-Neutral and Hyperscale Entrants

| Operator | Facility and evidence anchors | Regions | Grade |
|---|---|---|---|
| **Equinix Philippines** | Equinix completed acquisition of three TIM data centers in Manila in June 2025. Official release names MN1, MN2, MN3, more than 1,000 cabinets, and land for expansion; it also says these sites host main Manila IXs. | NCR | A |
| **SpaceDC** | MNL1 campus in Cainta, Rizal; marketed as a large green hyperscale campus. Verify current status and MW from SpaceDC/JLL/operator pages and EMB/LGU evidence. | CALABARZON | A/B |
| **EdgeConneX** | Manila/MNL01 appears in directories and market materials. Require operator page or official trail before storing exact site details. | NCR | B/C |
| **Flow / A-Flow (Flow Digital Infrastructure + Ayala Land)** | Laguna datacenter development reported by DCD/industry press and linked to Ayala Land/Flow platform. Upgrade only with operator, LGU, EMB, or utility records. | CALABARZON | B |
| **DAMAC Digital / EDGNEX** | Laguna AI datacenter announcement in 2026 is a major lead, but treat as planned/MoU-stage until LGU/EMB/utility/PEZA/BOI/operator facility evidence appears. | CALABARZON | B/C |
| **Evolution Data Centres + Megawide** | Philippine 69MW-type project references appear in developer/industry press; location and permit status require confirmation. | TBD | B/C |
| **Digital Edge / Yondr and other named entrants** | Mentioned in market commentary without stable, named PH facility evidence. Use only as search seeds. | TBD | C |

### 2.3 Smaller Colo, Hosting, and Edge Providers

Use directories and PeeringDB to seed, then verify with official pages and NTC/VAS:

```text
Beeinfotech "The Hive"
Bayan / Sky / Radius Telecom
Now Telecom / Now Corporation
Multisys / local cloud hosts
RackCorp Philippines
PHOpenIX facility participants
PeeringDB "Manila" "Philippines"
```

## 3. Hyperscaler and Cloud Presence

| Provider | Official PH status as of 2026-08-12 | Search strategy | Grade |
|---|---|---|---|
| **AWS** | Manila Local Zone exists; Direct Connect exists near/in ePLDT Makati infrastructure and AWS announced 100G expansion in Makati in 2025. No full AWS Philippines Region in official region list. | Search Local Zone, Direct Connect, ePLDT/VITRO Makati 2, carrier-hotel partners, Taguig/BGC/Makati latency nodes. | A for AWS pages; B/C for physical address if not official |
| **Microsoft Azure** | No public Azure Philippines Region in official region list. Microsoft PH AI/digital-infra announcements are not region evidence. | Search official Azure region list, Microsoft PH newsroom, DICT/BSP/DBM/DTI partnerships. | A for no-region check; B/C for plans |
| **Google Cloud** | No Google Cloud Philippines Region in official locations list and no Google-owned PH datacenter in Google's datacenter-location list. | Search official locations, Google PH talks, Apricot/Baler cable and PLDT/Converge connectivity. | A for official lists; B/C for talks |
| **Oracle OCI** | No OCI Philippines Region in official region list. | Search only official OCI future-region announcements. | A for official no-region check; C for rumors |
| **Local sovereign/enterprise cloud** | PLDT/VITRO, Converge, DITO, Eastern, Globe/STT, and GovCloud-accredited CSPs may host government/enterprise cloud workloads. | Cross-check DICT GovCloud accreditation and operator facility pages. | A/B |

Cloud queries:

```text
"AWS Local Zone" Manila
"AWS Direct Connect" Makati Philippines
"AWS" "ePLDT" "Makati" "Direct Connect"
"Azure" "Philippines" "region"
"Microsoft Philippines" "data center"
"Google Cloud" "Philippines" "region"
"Google" "Philippines" "data center" talks
"Oracle" "Philippines" "cloud region"
"GovCloud" "{operator}" "DICT"
```

## 4. Interconnection Ecosystem

Interconnection sources expose carrier hotels and candidate facilities, but many do not publish exact suite/building details.

IXPs and peering:

- PHOpenIX: `https://phopenix.net/`
- AMS-IX Manila: `https://www.ams-ix.net/mnl/`
- BBIX Philippines POP list: `https://bbix.com.ph/locations/`
- PhIX, GetaFIX, GIX/NIGX, PHNET CORE, PCTA-IX, BayanTel/Globe/Converge exchange points.
- PeeringDB, Cloudscene, DataCenterMap, Baxtel, datacenters.com for discovery.

Cable landing stations and subsea anchors:

- PLDT: Batangas, La Union and other landing/backbone roles.
- Globe/Innove: Batangas/Cavite landing roles.
- Converge: Baler/Aurora and Davao City roles, including Bifrost ecosystem.
- DITO, PT&T, ETPI/Eastern, G. Telecoms/iGSAT: license/landing seeds.
- Systems/leads: Bifrost, Apricot, Echo, TPU, PLCN, Candle, AUG, ALC, SEA-H2X, ADC, and related systems. Verify landing city and operator from cable-system/operator/NTC sources.

Interconnection queries:

```text
"{operator}" "cable landing" Philippines
"Bifrost" "Davao" "cable landing"
"Apricot" "Baler" OR "Digos"
"TPU" "Claveria" "Cagayan"
"Candle" "Nasugbu" "Batangas"
"PHOpenIX" "{facility}"
"AMS-IX Manila" participants
"BBIX Philippines" "locations"
site:peeringdb.com "Manila" "Philippines"
"{facility_name}" "IXP" "Manila"
```

Grade: A for official IXP/operator/NTC/cable-system pages; B for credible telecom press; C for crowd-sourced directory rows.

## 5. Industry Bodies, Events, and Market Reports

- **Data Center Association of the Philippines (DCAP)**: `https://dcap.ph/`. Use for operator membership, advocacy, and macro capacity targets. PNA reported DCAP's 1GW-by-2029 target and major investment framing; use as B-grade market context unless DCAP itself publishes the exact member/facility data.
- **Go Digital Pilipinas / Go Digital Philippines**, IBPAP, PE2, foreign chambers, and NEDA/DICT events: useful for demand and policy context, not facility proof.
- **Events**: DCD>Connect Manila, W.Media summits, Datacloud, Philippine data center conferences. Agendas are C-grade leads unless accompanied by a named project release.
- **Market reports**: Arizton, ResearchAndMarkets, Cushman & Wakefield, JLL, Structure Research. Use counts and MW ranges as market context only; do not import facility lists without verification.

Queries:

```text
site:dcap.ph members OR "{operator}"
"Data Center Association of the Philippines" "{operator}"
"DCAP" "1 GW" "2029"
"DCAP" "473 MW"
"DCD>Connect" Manila "data center"
"W.Media" "Philippines" "data center"
"JLL" "Philippines" "data center" "SpaceDC"
```

## 6. Trade Press and Databases

High-value secondary sources:

```text
site:datacenterdynamics.com Philippines "data center"
site:w.media "Philippines" "data center"
site:bworldonline.com "data center" "Philippines"
site:business.inquirer.net "data center"
site:mb.com.ph "data center" "Philippines"
site:manilastandard.net "data center"
site:businessmirror.com.ph "data center"
site:pna.gov.ph "data center" Philippines
site:reuters.com "Philippines" "data center"
site:rappler.com "data center" Philippines
site:abs-cbn.com "data center" Philippines
site:gmanetwork.com "data center" Philippines
```

Contractor/developer search:

```text
"First Balfour" "data center" Philippines
"EEI" "data center" Philippines
"D.M. Consunji" "data center"
"Megawide" "data center" Philippines
"Ayala Land" "data center" "Laguna"
"Bouygues" "VITRO" "Sta. Rosa"
"{contractor}" "{operator}" "data center"
```

Directory search:

```text
site:baxtel.com "Philippines" "data center"
site:datacentermap.com "Philippines" "data center"
site:cloudscene.com "Manila" "data center"
site:datacenters.com "Philippines" "colocation"
site:peeringdb.com "Philippines" "facility"
```

Upgrade rule: directory data remains C until an operator/official source confirms the facility name, operator, and city.

## 7. Region-by-Region Industry Strategy

### NCR

Confirmed/lead clusters: VITRO Makati 1/2, VITRO Pasig, VITRO Parañaque, Equinix MN1/MN2/MN3 ex-TIM, STT GDC Makati/Manila, STT Fairview, Converge Pasig, AWS Local Zone/Direct Connect ecosystem, EdgeConneX/Beeinfotech/directory leads.

```text
"VITRO Makati" OR "VITRO Pasig" OR "VITRO Parañaque"
"Equinix" "MN1" OR "MN2" OR "MN3" "Philippines"
"Equinix" "TIM" "Manila" "data centers"
"STT GDC" "Makati" OR "Fairview"
"Fairview" "124MW" "data center"
"Converge" "Pasig" "data center"
"EdgeConneX" "Manila" OR "MNL01"
"Beeinfotech" "The Hive"
"AWS Direct Connect" "Makati" "ePLDT"
"Manila" "carrier hotel" "IX"
```

### CALABARZON

Confirmed/lead clusters: VITRO Sta. Rosa, SpaceDC MNL1/Cainta, STT Cavite/General Trias, Flow/A-Flow Laguna, DAMAC/EDGNEX Laguna lead, Batangas/Nasugbu cable/industrial estate leads, possible ePLDT Cavite expansion.

```text
"VITRO Sta. Rosa" OR "VITRO Santa Rosa"
"Pulong Santa Cruz" "data center"
"SpaceDC" "MNL1" OR "Cainta"
"STT Cavite" OR "General Trias" "data center"
"A-Flow" OR "Flow Digital" "Ayala" "Laguna"
"DAMAC" OR "EDGNEX" "Laguna" "data center"
"Batangas" "data center" "industrial estate"
"Nasugbu" "cable landing" "data center"
"Carmona" OR "Calamba" OR "Biñan" OR "Cabuyao" "data center"
```

### Central Luzon

Clusters: DITO Clark Super Core DC, Clark Global City, New Clark City/BCDA ICT-infra leads, Subic/SBMA, Bataan/AFAB, Bulacan industrial parks, Baler/Aurora cable landing.

```text
"DITO" "Clark" "Super Core" "data center"
"Clark Global City" "data center"
"New Clark City" "data center" "BCDA"
"Subic" OR "SBMA" "data center"
"AFAB" OR "Bataan" "data center"
"Bulacan" "data center" "Meralco"
"Baler" "Converge" "cable landing"
"Aurora" "data center" "cable landing"
```

### Central Visayas

Current scope excludes Negros Oriental and Siquijor, now NIR. Focus on Cebu/Mandaue/Lapu-Lapu/Bohol.

Clusters: VITRO Cebu 1 and 2, Cebu IT Park, Cebu Business Park, Mandaue, Mactan/Lapu-Lapu carrier and DR nodes, VECO power.

```text
"VITRO Cebu" OR "ePLDT Cebu"
"Mandaue" "data center"
"Cebu IT Park" "colocation" OR "data center"
"Cebu Business Park" "data center"
"Lapu-Lapu" OR "Mactan" "data center"
"Cebu" "data center" "VECO"
"Bohol" "data center" DICT
```

### Davao Region

Clusters: STT GDC Davao, Globe legacy assets, Converge Davao/Bifrost cable landing, Digos/Apricot, Davao Light, Davao Global Township/industrial leads.

```text
"STT GDC" "Davao"
"Davao" "data center" "Globe"
"Davao" "data center" "Converge" OR "Bifrost"
"Digos" "Apricot" "cable landing"
"Davao" "colocation"
"Davao Light" "data center"
```

### Negros Island Region

Clusters/leads: Bacolod BPO/edge, Dumaguete/Negros Oriental education/BPO/edge, Siquijor low-probability government/edge.

```text
"Bacolod" "data center"
"Negros Occidental" "data center"
"Dumaguete" "data center"
"Negros Oriental" "data center"
"Siquijor" "data center"
"Negros Island Region" "data center"
"Bacolod" "colocation"
```

### Western Visayas

Current scope excludes Negros Occidental/Bacolod, now NIR. Focus on Iloilo, Aklan, Antique, Capiz, Guimaras.

Clusters: Iloilo City, Iloilo Business Park, MORE Power, BPO/edge.

```text
"Iloilo" "data center" "MORE Power"
"Iloilo Business Park" "data center"
"Iloilo" "colocation"
"Western Visayas" "data center" "DICT"
"Aklan" OR "Capiz" OR "Antique" OR "Guimaras" "data center"
```

### Ilocos Region and CAR

Clusters: La Union cable landings, San Fernando/Luna, Baguio/Camp John Hay North Luzon Data Center, regional government/edge.

```text
"La Union" "cable landing" "data center"
"San Fernando" "La Union" "data center"
"Luna" "La Union" "cable landing"
"Baguio" "data center" "John Hay"
"North Luzon Data Center" "DICT"
"Cordillera" "data center"
```

### Cagayan Valley

Clusters: Claveria/Cagayan trans-Pacific cable landing, Tuguegarao regional/edge.

```text
"Claveria" "Cagayan" "cable landing"
"TPU" "Claveria" "Cagayan"
"Tuguegarao" "data center"
"Cagayan Valley" "data center" DICT
```

### Northern Mindanao

Clusters: Cagayan de Oro/CEPALCO, Phividec, Iligan, government/edge.

```text
"Cagayan de Oro" "data center" CEPALCO
"CDO" "data center" "colocation"
"Phividec" "data center"
"Iligan" "data center"
"Northern Mindanao" "data center" DICT
```

### Lower-Density Regions

Use government/telco/edge/DR queries for Bicol, Eastern Visayas, Zamboanga Peninsula, Soccsksargen, Caraga, BARMM, and Mimaropa.

```text
"Naga" OR "Legazpi" "data center"
"Tacloban" OR "Leyte" "data center"
"Zamboanga" "data center"
"General Santos" OR "Koronadal" "data center"
"Butuan" OR "Surigao" "data center"
"Cotabato City" OR "BARMM" "data center"
"Puerto Princesa" OR "Palawan" "data center"
"Calapan" "data center"
"{region}" "data center" "DICT"
"{city}" "colocation" OR "data center" "PLDT" OR "Globe" OR "Converge" OR "DITO"
```

## 8. Practical Enumeration Workflow

1. Seed operators from section 2, DCAP/member references, IXP participants, and cloud infrastructure pages.
2. Normalize entities: brand, SEC/legal entity, NTC registration holder, PEZA/BOI enterprise, SPV/landowner, and facility brand.
3. Resolve geography to current PSGC region, province, city/municipality, barangay, and industrial park.
4. Pull industry evidence: operator page first, then trade press, then directories.
5. Cross-check official trails from `explorer-official.md`: LGU, EMB, utility/ERC/NGCP, PEZA/BOI, NTC, DICT, NPC.
6. Check interconnection: IXP, PeeringDB, cable landing, Direct Connect/cloud on-ramp, carrier list.
7. Assign status and grade; do not store planned MW as operating MW.

Minimum industry record fields:

```text
operator_brand
legal_entity
facility_name / campus_code
region_current
province
city_or_municipality
barangay_or_industrial_park
marketed_MW
IT_load_MW
cabinets_or_racks
status: proposed | MoU-only | permit-stage | under-construction | ready-for-service | operating | cancelled
anchor_tenant_or_AI_signal
interconnection: IXPs | CLS | Direct Connect | PeeringDB | carriers
source_type: operator | press | directory | event | market-report
confidence_grade: A | B | C
official_trails_pulled: LGU | EMB | utility | PEZA/BOI | NTC | DICT | NPC
source_urls
source_dates
```

## 9. Red Flags and Caveats

- Current regional coverage is 18 regions. Do not use old 17-region templates without adding NIR.
- "Manila" is a metro label. Resolve it to Makati, Pasig, Taguig, Quezon City, Parañaque, Muntinlupa, Pasay, etc.
- MoUs are not facilities. DAMAC/EDGNEX and similar announcements need LGU/EMB/utility/PEZA/BOI/operator evidence before upgrade.
- Directory counts vary and often lag acquisitions. Equinix/TIM, STT/Globe, and VITRO branding changes can duplicate records.
- MW claims must distinguish planned campus capacity, IT load, utility load, and operating phase.
- Subsea cable landing stations are not datacenters unless separately evidenced.
- Cloud Local Zone, Direct Connect, or edge node presence is not a full cloud region.
- NTC VAS/DTIP registration is entity evidence, not a building address.
- Power constraints and grid connection timelines can delay apparently announced campuses.
