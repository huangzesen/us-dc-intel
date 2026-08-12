# AS Explorer Industry — American Samoa 数据中心行业/媒体/厂商枚举方法

Date: 2026-08-12. Status: final source-verification pass. Scope: industry, media, operator, vendor, directory, and cloud/edge methodology for finding data centers and datacenter-like facilities in **AS — American Samoa（美属萨摩亚）**. Manifest check: `subnational_type="country"`, `divisions=["American Samoa"]`; all records use `division: American Samoa`.

Reliability grades: **A** = primary/operator/vendor/regulator/government/cloud-provider page; **B** = named trade press or local/regional media with date and actor detail; **C** = directory, map, PeeringDB/ASN aggregate, social media, SEO hosting page, or market-report snippet. C-grade evidence is discovery only.

---

## 0. Industry Baseline

- No verified neutral commercial colocation provider or hyperscale cloud region was found for American Samoa in this pass.
- The industry surface is telecom-heavy: **ASTCA** is the strongest operator lead; cable landing stations, NOCs, fiber circuits, and government broadband programs are more likely than commercial colo.
- 2026 changes matter: Le Vasa and SAS-2 create new cable-landing and regional-connectivity watchlists. Vendor/trade stories may call DXN a “data center” company, but the AS deliverable is a **cable landing station (CLS)** unless primary evidence says otherwise.
- Tutuila, especially Tafuna/Pago Pago/Fagatogo/Nu'uuli, is the only realistic facility geography. Manu'a, Swains, and Rose Atoll are connectivity-only unless strong contrary evidence appears.

---

## 1. Source Map and Grades

### 1.1 Primary / Operator / Official

| Source / player | URL | Use | Grade |
|---|---|---|---|
| ASTCA | https://www.astca.as/ ; https://www.astca.net/ redirects to `.as` | Incumbent/state telecom; fiber broadband, 5G, business services, Hawaiki circuits, RFP links. Search first for any hosting/colo/DC product. | A |
| ASTCA RFPs | linked from ASTCA footer, e.g. current `RFP ASTCA001-2026` link | Procurement clues for network equipment, CLS, power/cooling, generators, modular facilities. | A |
| ASG portal / press | https://www.americansamoa.gov/ ; https://www.americansamoa.gov/pressreleases ; linked `asgpressrelease.com` pages | Official digital-infrastructure, Le Vasa, SAS-2, BEAD/BCORD, and ASTCA project announcements. | A |
| ASG procurement | https://procurement.as.gov/ | Tenders/RFPs. Verified HTTP 200 by `curl -I -L`; browser extraction may be limited. | A |
| ASPA | https://www.aspower.com/ | Power feasibility and large-load validation. | A |
| FCC / docs.fcc.gov | https://www.fcc.gov/ ; https://docs.fcc.gov/ | Cable landing licenses/public notices; Le Vasa Tafuna CLS evidence. | A |
| NTIA / BEAD | https://www.ntia.gov/ and ASG BEAD press PDF | Broadband funding and community-anchor infrastructure; not DC by default. | A |
| Cloud official lists | AWS, Azure, Google Cloud, Oracle OCI official region/location pages | A-grade absence/presence check. No AS region string found in this pass. | A |

### 1.2 Media, Trade, and Directory Sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Samoa News | https://www.samoanews.com/ | Local reporting on ASTCA, DXN CLS contract, ASG procurement, power, cable, broadband. | B |
| Talanei / KHJ News | https://www.talanei.com/ ; KHJ surface under https://www.southseasbroadcasting.com/93khj/ | KHJ News is not `khjnews.com` (that host did not resolve in this pass). Use Talanei/KHJ podcasts and South Seas pages. | B/C |
| Samoa Observer | https://www.samoaobserver.ws/ | Regional Samoa/AS telecom coverage; watch Samoa-vs-AS contamination. | B |
| RNZ Pacific | https://www.rnz.co.nz/pacific | Regional telecom/broadband/policy reporting. | B |
| Islands Business | https://islandsbusiness.com/ | Pacific telecom/business coverage; Hawaiki/ASTCA context. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Trade coverage of DXN CLS contracts and Pacific cable work. | B |
| Telecompaper / SubTel Forum / subseacables.net | site-specific search | Vendor/trade summaries of Le Vasa/DXN and cable systems. | B/C |
| PITA | https://www.pita.org.fj/ | Pacific Islands Telecommunications Association; regional operator/event context. Verified HTTP 200. | B/C |
| PTC | https://www.ptc.org/ | Pacific telecom conference/member context. | B/C |
| APNIC / Internet Society | https://www.apnic.net/ ; https://www.internetsociety.org/ | ASN, routing, IX/cache, resilience context. | B/C |
| Submarine Networks | https://www.submarinenetworks.com/ | Cable system leads: ASH/SAS, Hawaiki, Manatua, Le Vasa. | B/C |
| Submarine Cable Map | https://www.submarinecablemap.com/ | Landing-route lead only. | C |
| DataCenterMap | https://www.datacentermap.com/ | Directory/negative-control search; may rate-limit (HTTP 429 observed). | C |
| Cloudscene | https://cloudscene.com/ | Directory/market lead; homepage HTTP 200, specific AS results require search/login behavior. | C |
| PeeringDB | https://www.peeringdb.com/ | ASN/facility/interconnection leads only; not facility proof. | C |
| LinkedIn / Facebook | operator/government pages | Photos, jobs, ceremonies, facility clues; verify against A/B sources. | C |

---

## 2. Operator, Vendor, and Enterprise Scan

### 2.1 ASTCA

ASTCA is the first industry/operator surface. Current official pages confirm local fiber broadband, mobile, business services, and Hawaiki circuits. They do not, by themselves, confirm a commercial colocation product.

Queries:

```text
site:astca.as (hosting OR colocation OR "co-location" OR "data center" OR "data centre" OR datacenter OR cloud OR backup OR NOC OR "server room")
site:astca.as (enterprise OR business OR government OR broadband OR fiber OR wireless OR "Hawaiki Circuits")
"ASTCA" ("data center" OR "data centre" OR datacenter OR Tafuna OR "Pago Pago" OR NOC) (rack OR colocation OR hosting OR "server room" OR "network operations")
"American Samoa Telecommunications Authority" ("annual report" OR budget OR audit OR RFP OR "cable landing station")
```

Record rules:

- `commercial_colo` only if ASTCA or a contract explicitly sells/uses AS-located rack/colo/hosting.
- `telecom_cable_station` for Le Vasa/Hawaiki/ASH/SAS/Manatua landing infrastructure.
- `telecom_core` for NOC/switch/core records without customer hosting.

### 2.2 Cable Landing Vendors and Contractors

High-yield vendor terms: DXN, SubCom, AP Telecom, Google/Starfish, Bulikula, Le Vasa, SAS-2, Hawaiki, Manatua, ASH/SAS.

Verified 2026 lead:

- FCC Le Vasa public notice: A-grade for planned Tafuna cable landing station/beach joint by ASTCA.
- ASG April/May 2026 press: A-grade for Google Le Vasa project survey/strategic roadmap and SAS-2 planning.
- DXN/trade press July 2026: B-grade for an ASTCA modular CLS contract, contract value around AUD 1m, and delivery/commissioning details. Treat as vendor confirmation of a CLS, not a commercial DC.

Queries:

```text
"DXN" ASTCA "American Samoa" ("cable landing station" OR CLS OR "Le Vasa")
"SubCom" OR "AP Telecom" "American Samoa" ("Le Vasa" OR "SAS-2" OR "cable")
"Google" OR Starfish OR Bulikula "American Samoa" ("Le Vasa" OR "cable landing" OR "landing station")
"American Samoa" ("modular data center" OR "prefabricated" OR "critical power" OR cooling) ASTCA
```

### 2.3 Government and Enterprise Server-Room Leads

These are not commercial DCs unless facility services are explicit. Capture as `enterprise_server_room` or `government_dc` only with physical-site evidence.

Targets:

- ASG IT/CIO/BCORD and procurement records.
- LBJ Tropical Medical Center.
- American Samoa Community College (ASCC).
- ASDOE / education network.
- Port Administration / Pago Pago Harbor and Pago Pago International Airport.
- Banks and financial services.
- Tuna/cannery operators and industrial facilities: StarKist, Chicken of the Sea, Tri Marine/Samoa Tuna Processors.

Queries:

```text
"American Samoa Government" (IT OR ICT OR "data center" OR "data centre" OR server OR "disaster recovery" OR cloud OR BCORD)
"LBJ Tropical Medical Center" "American Samoa" (server OR "data center" OR "data centre" OR network OR "disaster recovery")
"American Samoa Community College" OR ASCC (server OR "data center" OR "data centre" OR network OR ICT)
"Pago Pago International Airport" OR "Port of Pago Pago" (server OR "data center" OR IT OR network OR security)
"Bank of Hawaii" "American Samoa" ("data center" OR "data centre" OR "disaster recovery" OR server OR IT)
("StarKist" OR "Chicken of the Sea" OR "Samoa Tuna Processors" OR "Tri Marine") "American Samoa" (IT OR server OR network OR data)
```

---

## 3. Cloud, Edge, and Satellite Sweep

No public AWS/Azure/GCP/Oracle region was found for American Samoa on official region/location lists during this pass. Starlink/VSAT/satellite service is connectivity, not DC capacity.

| Provider / class | Search route | Classification |
|---|---|---|
| AWS | official regions/AZs and Local Zones; search AS + Outposts | `cloud_region_absent` unless official page changes. Outposts lead needs named on-prem site. |
| Microsoft Azure | official Azure regions list; Azure Stack search | `cloud_region_absent`; Azure Stack needs contract/site evidence. |
| Google Cloud | official locations; Google Pacific Connect / Bulikula / Le Vasa | Connectivity/cable context, not GCP region. |
| Oracle OCI | official public cloud regions | `cloud_region_absent`. |
| Starlink / Kacific / O3b / VSAT | availability, FCC, local resellers, ASG/ASTCA | `connectivity_only` unless a gateway/edge site is named. |

Queries:

```text
"American Samoa" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region" OR "Local Zone")
"American Samoa" ("AWS Outposts" OR "Azure Stack" OR "Google Distributed Cloud" OR "Oracle Cloud") ("data center" OR "on-premises" OR government)
"American Samoa" (Starlink OR Kacific OR VSAT OR O3b OR satellite OR "low earth orbit") (availability OR coverage OR license OR reseller OR gateway)
"American Samoa" (edge OR "edge computing" OR cache OR CDN OR "internet exchange" OR IXP)
```

---

## 4. Search Templates and Local Variants

Use English first. Add Samoan/local variants only to catch ASG bilingual pages and local press:

- Territory variants: `American Samoa`, `Amerika Samoa`, `Sāmoa Amelika`.
- Place variants: `Pago Pago`, `Pagopago`, `Fagatogo`, `Utulei`, `Tafuna`, `Nu'uuli`, `Nuuli`, `'Ili'ili`, `Iliili`, `Leone`, `Vaitogi`, `Futiga`, `Mapusaga`, `Malaeimi`, `Aua`, `Fagasa`, `Lauli'i`, `Laulii`, `Aoloau`, `Ta'u`, `Tau`, `Ofu`, `Olosega`, `Fitiuta`, `Swains Island`, `Rose Atoll`.
- Facility terms: `data center`, `data centre`, `datacenter`, `colo`, `colocation`, `co-location`, `hosting`, `server hosting`, `server room`, `backup`, `disaster recovery`, `NOC`, `IXP`, `cable station`, `landing station`, `CLS`, `switch`, `core network`, `facility access`.

National queries:

```text
("American Samoa" OR "Amerika Samoa" OR "Sāmoa Amelika") ("data center" OR "data centre" OR datacenter OR colocation OR "co-location" OR "server hosting" OR "managed hosting") -VPS -proxy
"American Samoa" (ASTCA OR "American Samoa Power Authority" OR StarKist OR "Bank of Hawaii" OR ASCC OR LBJ) (IT OR network OR server OR data OR "disaster recovery")
site:samoanews.com ("data center" OR "data centre" OR datacenter OR broadband OR cable OR ASTCA OR Starlink OR digital OR "Le Vasa")
site:talanei.com ("data center" OR "data centre" OR broadband OR ASTCA OR fiber OR internet OR "Le Vasa" OR "SAS-2")
site:datacenterdynamics.com "American Samoa" ("data center" OR "data centre" OR "cable landing station" OR DXN)
site:datacentermap.com "American Samoa" OR "Pago Pago"
site:cloudscene.com "American Samoa"
site:peeringdb.com "American Samoa" OR ASTCA
```

Place queries:

```text
"{place}" "American Samoa" (server OR hosting OR "data center" OR "data centre" OR colocation OR "cable station" OR "landing station" OR NOC OR fibre OR fiber OR broadband OR IXP)
"{place}" "American Samoa" (ASTCA OR "American Samoa Power Authority" OR power OR grid OR solar OR generator OR cable)
site:astca.as "{place}"
site:americansamoa.gov "{place}" (telecom OR broadband OR digital OR ICT OR "data")
```

---

## 5. Per-Division Industry Enumeration

| Manifest division | Geography | Expected industry finds | Media/vendor paths | Decision rule |
|---|---|---|---|---|
| American Samoa | Tutuila: Pago Pago/Fagatogo/Utulei/Tafuna/Nu'uuli/Iliili/Leone corridor | ASTCA network/core/CLS; government ICT; Le Vasa/SAS-2 vendor work; enterprise rooms in hospital, college, banks, port/airport, canneries | ASTCA, ASG, Samoa News, Talanei/KHJ, DCD, Telecompaper, SubTel, vendor releases, FCC | Promote only with physical facility + function + source grade. Cable/vendor module = `telecom_cable_station`, not `commercial_colo`. |
| American Samoa | Manu'a: Ta'u, Ofu, Olosega, Fitiuta | Fiber/mobile/BLAST/solar/microgrid connectivity; no DC expected | ASTCA coverage, ASG press, ASPA, local media | Default `connectivity_only` or `no_projects`. |
| American Samoa | Swains Island, Rose Atoll | Minimal remote communications; no DC expected | FCC/ASG/DOI/environmental records | Default `no_projects`; reject ambiguous hits. |

Coverage check: the manifest division “American Samoa” is covered exactly once; the geography rows are internal search aids.

---

## 6. Capture Fields

```text
name:
operator_or_owner:
division: American Samoa
town_or_site:
coordinates_or_address:
source_url:
source_date:
source_grade: A|B|C
facility_type: commercial_colo | government_dc | telecom_cable_station | telecom_core | enterprise_server_room | tower_edge | connectivity_only | false_positive
status: proposed | planned | procurement | under_construction | operational | discontinued | false_positive
basis_for_status:
capacity_or_power_claim:
power_evidence:
license_or_registry_anchor:
notes:
```

Promotion rules:

- `commercial_colo`: requires operator/contract evidence of AS-located rack/colo/hosting service.
- `government_dc`: requires ASG/ASTCA/federal source naming a government data center, site, and status.
- `telecom_cable_station`: cable landing station, CLS, beach joint, NOC, or core site without customer hosting.
- `connectivity_only`: fiber route, broadband coverage, tower, satellite, grant, cable capacity.
- `false_positive`: Samoa (WS) hits, offshore VPS/proxy pages, generic cloud resellers, or directory entries without local anchors.

---

## 7. Pitfalls

- **Samoa (WS) contamination** dominates regional searches. Apia, Tuasivi, SSCC, SamoaTel, Digicel Samoa, Vodafone Samoa, and Samoa MCIT are independent Samoa unless the article explicitly describes American Samoa-side infrastructure.
- **Vendor wording can mislead**: DXN is a modular data-center vendor, but its AS contract lead is a cable landing station.
- **Cloud language is often service-only**: “cloud”, “digital hub”, “data foundation”, and “data sovereignty” need a physical site before facility capture.
- **Directory absence is weak evidence**: DataCenterMap/Cloudscene/PeeringDB are C-grade. Empty or rate-limited results support triage only.
- **Power feasibility is mandatory**: large loads need ASPA or project-document support.

---

## 8. Refresh Instructions

Every refresh should re-run ASTCA official/RFP searches, ASG press/procurement searches, Samoa News and Talanei/KHJ media searches, DCD/vendor searches for DXN/SubCom/AP Telecom/Google cable work, FCC cable/public-notice searches, federal funding searches, ASPA power searches, directory checks, and official cloud-region absence checks. Only A-grade evidence should change facility status or overturn the no-commercial-colo baseline.
