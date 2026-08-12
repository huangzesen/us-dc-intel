# AS Explorer Official — American Samoa 数据中心官方/监管枚举方法

Date: 2026-08-12. Status: final source-verification pass. Scope: official/regulatory methodology for enumerating data centers and datacenter-like ICT/telecom facilities in **AS — American Samoa（美属萨摩亚）**. Manifest check: `country_code="AS"`, `subnational_type="country"`, `divisions=["American Samoa"]`; there is exactly one manifest division, so all confirmed records must use `division: American Samoa`.

Reliability grades: **A** = official/primary source (government/regulator/SOE/operator official page, FCC/NTIA/USAC/SAM/USAspending/DOI record, cloud-provider official region list, official project/contract record); **B** = strong secondary/trade/local press with named actors and dates; **C** = directory/map/social/SEO/market-report snippet/unverified lead only.

---

## 0. Official Baseline

- American Samoa is a small U.S. territory with a limited island grid and a telecom market dominated by the state-owned **American Samoa Telecommunications Authority (ASTCA)**. Expect the datacenter surface to be small and visible through telecom, cable-landing, government procurement, and utility records.
- No verified A-grade evidence was found for a neutral commercial colocation market or hyperscale/public-cloud region in American Samoa. Treat that as a working negative baseline, not as a permanent fact.
- The strongest official facility class is **telecom cable landing / core network infrastructure**, especially ASTCA assets around Tafuna/Pago Pago. These are not commercial data centers unless a primary source explicitly confirms colocation, rack hosting, cloud, or customer data-center service in American Samoa.
- 2026 update: official/FCC and government sources show new **Le Vasa** and **SAS-2** cable work. This strengthens the telecom-infrastructure watchlist, but it does not by itself prove commercial DC capacity.

---

## 1. Verified Official Anchors

| Anchor | Verified URL | Grade | Datacenter relevance |
|---|---|---:|---|
| ASTCA official site | https://www.astca.as/ ; legacy https://www.astca.net/ redirects to `.as` | A | Operator confirms fiber broadband, 5G, business services, and Hawaiki circuits; use for operator/service evidence. No public colo/DC product page confirmed in this pass. |
| ASTCA RFP surface | ASTCA footer links current RFPs from https://www.astca.as/ | A | Watch for cable landing station, network core, modular facility, generator/cooling, and IT infrastructure procurements. |
| ASG portal | https://www.americansamoa.gov/ | A | Official press, general memoranda, notices, jobs, agency routing. |
| ASG procurement | https://procurement.as.gov/ | A | Official procurement endpoint; `curl -I -L` returned HTTP 200. Search tenders/RFPs directly and via search engines. |
| Secretary of American Samoa | https://www.osas.as/ | A | Executive orders and legal records. EO 002-1998 establishes ASTCA from the former Office of Communications. |
| ASPA power utility | https://www.aspower.com/ | A | Official American Samoa Power Authority site; use for grid/large-load feasibility, rates, notices, and power projects. |
| FCC cable/licensing records | https://www.fcc.gov/ and document host https://docs.fcc.gov/ | A | FCC DA-26-578A1 (2026) states ASTCA will construct the Le Vasa cable landing station and beach joint in Tafuna, and will own/operate the Le Vasa system after construction. |
| USAC | https://www.usac.org/ | A | Universal Service / high-cost / E-rate funding and deployment commitments for telecom infrastructure. |
| SAM.gov | https://sam.gov/ | A | Federal procurement notices and awards that may mention AS telecom/ICT/data-center work. |
| USAspending | https://www.usaspending.gov/ | A | Federal awards to ASG, ASTCA, ASPA, DOI/NTIA programs, or named contractors. |
| DOI Office of Insular Affairs | https://www.doi.gov/oia | A | Capital improvement and technical-assistance grants for U.S. territories. |
| NTIA | https://www.ntia.gov/ | A | BEAD/Digital Equity/Broadband records. ASG announced NTIA approval of **$37.56m BEAD funding** on 2025-11-21 for broadband and community-anchor upgrades. |
| Hawaiki / BW Digital | https://www.hawaiki.co.nz/ redirects to https://www.bw-digital.com/ | A/B | Current owner/site context for Hawaiki; use with ASTCA/FCC for AS-side ownership/landing facts. |
| Submarine Networks | https://www.submarinenetworks.com/ | B/C | Useful cable system summaries for ASH/SAS, Hawaiki, Manatua, and Le Vasa; verify against FCC/ASTCA/ASG before facility promotion. |
| Submarine Cable Map | https://www.submarinecablemap.com/ | C | Route/landing lead only. |
| Cloud provider region lists | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/ | A | No “American Samoa” entry found on these official pages in this pass. |

---

## 2. Official / Regulatory Backbone

### 2.1 Telecom Regulation and State Operator

American Samoa is a U.S. territory, so telecom and submarine-cable licensing is heavily visible through the **FCC**, while ASTCA is the local state-owned telecom operator.

- ASTCA official pages show consumer/business mobile, broadband, landline, TV, FirstNet, and business services; the home page describes fiber internet and data services across inhabited islands and links to Hawaiki circuits.
- The Secretary of American Samoa site hosts executive-order records establishing ASTCA. Use this as A-grade institutional evidence, not as facility evidence.
- FCC submarine cable documents are critical. For Le Vasa, FCC DA-26-578A1 is A-grade evidence that ASTCA will construct the cable landing station and beach joint in **Tafuna** and own/operate the system after construction.
- ASG 2026 press releases identify ASTCA as lead agency for regional digital infrastructure, including Le Vasa and SAS-2 planning.

Queries:

```text
site:astca.as ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR NOC OR "server room" OR "cable landing" OR "landing station" OR "Hawaiki Circuits")
site:astca.as (Hawaiki OR Manatua OR ASH OR SAS OR "Le Vasa" OR "SAS-2" OR Bulikula OR Google)
site:docs.fcc.gov "American Samoa" ASTCA ("cable landing station" OR "landing station" OR Tafuna OR "Le Vasa")
site:fcc.gov "American Samoa" ASTCA ("submarine cable" OR "cable landing license" OR "universal service" OR broadband)
site:osas.as ASTCA OR "American Samoa Telecommunications Authority"
```

### 2.2 ASG Procurement, Press, and Budget

- Use `https://procurement.as.gov/` as the procurement endpoint. It is real and returned HTTP 200 in this pass.
- Use `https://www.americansamoa.gov/pressreleases`, notices, general memoranda, and linked `asgpressrelease.com` pages for official project announcements.
- 2026 ASG press releases to monitor: Google Le Vasa Cable Project, AP Telecom/SubCom visits, SAS-2 execution roadmap, BEAD/BCORD broadband implementation, and any FY27 Fono budget hearings for ASTCA.
- Government terms such as “digital hub”, “digital sovereignty”, “data dashboard”, or “data foundation” are not facility evidence unless they name a physical site, build, contract, or equipment.

Queries:

```text
site:procurement.as.gov ("data center" OR "data centre" OR datacenter OR "server" OR "network" OR "cable landing" OR "generator" OR cooling OR "ICT")
site:americansamoa.gov ("data center" OR "data centre" OR datacenter OR ICT OR broadband OR "digital infrastructure" OR "Le Vasa" OR "SAS-2")
site:asgpressrelease.com ("Le Vasa" OR "SAS-2" OR ASTCA OR "digital infrastructure" OR "data center" OR "data centre")
"American Samoa Government" (procurement OR RFP OR tender OR budget OR Fono) ("data center" OR datacenter OR "IT infrastructure" OR broadband OR ASTCA)
```

### 2.3 Federal Funding and Contract Records

Use U.S. federal systems because AS projects often flow through federal grants, universal service, and territorial infrastructure programs.

- **NTIA/BEAD**: ASG announced NTIA approval of $37.56m BEAD funding on 2025-11-21. This is broadband/community-anchor infrastructure, not a DC by default.
- **FCC/USAC**: search for ASTCA high-cost, E-rate, broadband deployment, and submarine cable filings.
- **SAM.gov/USAspending**: search both award descriptions and recipients; words like “data center” may refer to managed IT, disaster recovery, or federal service delivery outside AS.
- **DOI OIA** and **USDA Rural Development/RUS**: useful for capital-improvement and telecom financing records.

Queries:

```text
site:sam.gov "American Samoa" ("data center" OR datacenter OR "IT services" OR broadband OR telecom OR ASTCA)
site:usaspending.gov "American Samoa" (ASTCA OR "American Samoa Telecommunications" OR "Office of Procurement" OR broadband)
site:ntia.gov "American Samoa" (BEAD OR broadband OR "Digital Equity" OR "middle mile" OR "community anchor")
site:doi.gov/oia "American Samoa" (grant OR "capital improvement" OR broadband OR telecommunications OR "data")
site:usac.org "American Samoa" (ASTCA OR "high-cost" OR broadband OR deployment OR E-rate)
site:rd.usda.gov "American Samoa" (ASTCA OR broadband OR telecommunications)
```

### 2.4 Power and Large-Load Validation

**American Samoa Power Authority (ASPA)** is the utility anchor for any serious data-center load. The official site is `https://www.aspower.com/`.

- Any >0.5 MW data-center claim should have ASPA connection, generation, fuel, substation, tariff, or public-notice evidence.
- Be careful with “ASPA”: it may also refer locally to port/airport contexts; use the full name **American Samoa Power Authority** in queries.
- For Tutuila, search Tafuna, Satala, Pago Pago, Tafuna plains, Fagatogo, Nu'uuli, Iliili, and Leone. For Manu'a, expect microgrid/solar/telecom coverage rather than DCs.

Queries:

```text
site:aspower.com ("data center" OR "data centre" OR datacenter OR "large load" OR substation OR generator OR "power purchase")
"American Samoa Power Authority" ("data center" OR "data centre" OR "large load" OR MW OR substation OR "power purchase")
"American Samoa Power Authority" (Tafuna OR Satala OR "Pago Pago" OR "Manu'a" OR grid OR solar OR diesel OR battery)
```

---

## 3. Cable Landing and Connectivity Infrastructure

Landing stations are the highest-probability “facility-like” official records in AS. Record them as `telecom_cable_station` or `telecom_core` unless hosting/colo/DC service is explicitly confirmed.

| System / project | AS signal | Evidence route | Classification rule |
|---|---|---|---|
| ASH / SAS | Pago Pago / American Samoa-Hawaii and Samoa-American Samoa cable history; older system records and FCC context | FCC, ASTCA, Submarine Networks, legacy ASH records | Connectivity/cable station only unless current ASTCA source names hosted services. |
| Hawaiki | ASTCA owns/uses AS branch capacity; ASTCA site advertises Hawaiki circuits; regional press confirms AS branch context | ASTCA, Hawaiki official, University of Hawaii/PIREN, Islands Business | Connectivity/backbone; not DC. |
| Manatua | Regional Polynesian cable context involving Pago Pago/American Samoa | Official/operator pages where available; Submarine Networks/Map for leads | Connectivity only unless ASTCA/FCC names a facility. |
| Le Vasa | 2026 FCC public notice says ASTCA will construct Tafuna cable landing station and beach joint; ASG press identifies Google Le Vasa Cable Project and survey/landing work | FCC DA-26-578A1, ASG press, ASTCA RFPs, vendor announcements | Planned/under-construction cable landing facility; do not call commercial DC. |
| SAS-2 | ASG 2026 press sets planning and budget timeline with ASTCA/MCIT; mentions physical landing requirements | ASG press and later Fono/procurement records | Planned cable project; no facility until site/contract/permit is named. |

Queries:

```text
"American Samoa" (Hawaiki OR Manatua OR ASH OR "American Samoa-Hawaii" OR SAS OR "SAS-2" OR "Le Vasa" OR Bulikula) ("landing station" OR "cable station" OR "landing point" OR Tafuna OR "Pago Pago")
site:docs.fcc.gov "American Samoa" ("Le Vasa" OR "Bulikula" OR "cable landing station")
site:submarinenetworks.com "American Samoa" (Hawaiki OR Manatua OR ASH OR SAS OR "Le Vasa")
site:submarinecablemap.com "Pago Pago" OR "American Samoa"
site:astca.as (Hawaiki OR Manatua OR ASH OR SAS OR "Le Vasa" OR landing)
```

---

## 4. Cloud Region Absence Checks

As of the 2026-08-12 pass, official AWS, Azure, Google Cloud, and Oracle OCI region/location pages had no “American Samoa” match. This is A-grade evidence for absence from current public-region lists, but not evidence that no private edge appliance exists.

Queries:

```text
"American Samoa" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region")
"American Samoa" (hyperscale OR "public cloud" OR "sovereign cloud" OR "data residency" OR "AWS Outposts" OR "Azure Stack" OR "Google Distributed Cloud")
```

Classification:

- `cloud_region_absent`: official provider region/location lists show no AS.
- `edge_or_appliance_lead`: only if a primary provider/customer contract names AS-located hardware.
- `service_resale_only`: cloud/hosting marketing with no AS physical facility.

---

## 5. Per-Division Enumeration

Manifest division coverage is complete with one row: **American Samoa**. The place-level rows below are search aids only; they are not extra divisions.

| Manifest division | Place-level sweep | Expected official finds | Priority official routes | Record rule |
|---|---|---|---|---|
| American Samoa | Tutuila: Pago Pago, Fagatogo, Utulei, Tafuna, Nu'uuli/Nuuli, Iliili/'Ili'ili, Leone, Vaitogi, Futiga, Mapusaga, Malaeimi, Aua, Fagasa, Lauli'i/Laulii, Aoloau | ASTCA telecom/core/cable landing facilities; ASG ICT; procurement; Le Vasa/SAS-2 landing work; government/enterprise server rooms | ASTCA, ASG, procurement.as.gov, FCC, USAC, SAM/USAspending, ASPA | Use `telecom_cable_station`/`telecom_core` unless source confirms DC/colo/government DC function. |
| American Samoa | Manu'a: Ta'u/Tau, Ofu, Olosega, Fitiuta | Broadband, fiber, mobile, microgrid/solar, BLAST/coverage assets | ASTCA coverage/service pages, ASG press, ASPA, FCC/USAC | Default `connectivity_only` or `no_projects`; no DC expected. |
| American Samoa | Swains Island, Rose Atoll | Minimal communications context only | FCC, ASG, DOI/OIA, environmental/federal records | Default `no_projects`; reject DC hits unless A-grade source names a physical facility. |

Territory-level query:

```text
("American Samoa" OR "Amerika Samoa" OR "Sāmoa Amelika") ("data center" OR "data centre" OR datacenter OR colocation OR "co-location" OR hosting OR "server room" OR "cable station" OR "landing station" OR NOC OR IXP)
("American Samoa" OR "Amerika Samoa") (ASTCA OR "American Samoa Power Authority" OR "Office of Procurement" OR Fono OR BCORD) ("data center" OR broadband OR ICT OR "IT infrastructure")
"American Samoa" (procurement OR RFP OR tender OR grant OR award) ("data center" OR datacenter OR ICT OR broadband OR "cable landing")
```

Place query:

```text
"{place}" "American Samoa" ("data center" OR "data centre" OR datacenter OR hosting OR colocation OR "server room" OR NOC OR "cable station" OR "landing station")
site:astca.as "{place}"
site:americansamoa.gov "{place}" (telecom OR broadband OR ICT OR "data center" OR "data centre" OR "Le Vasa" OR "SAS-2")
"{place}" "American Samoa" (ASTCA OR "American Samoa Power Authority" OR power OR grid OR solar OR generator)
```

---

## 6. False Positives and Promotion Rules

- **Samoa (WS) contamination**: Apia, Tuasivi, SSCC, SamoaTel, Digicel Samoa, Vodafone Samoa, and MCIT usually refer to independent Samoa, not AS. Only retain when the record clearly identifies American Samoa-side infrastructure.
- **Cable landing is not a data center**: Hawaiki, ASH/SAS, Manatua, Le Vasa, and SAS-2 evidence starts as `telecom_cable_station` or `connectivity_only`.
- **Operator/service is not a facility**: ASTCA business services, Hawaiki circuits, mobile, fiber, FirstNet, and broadband prove service availability, not commercial colo.
- **Procurement wording needs original-text review**: “data center” in SAM.gov/ASG/federal awards may mean managed IT, backup, software, or off-island services.
- **Power claims require ASPA evidence**: AS grid scale makes large MW claims implausible without utility records.
- **Directory/SEO pages stay C**: VPS, proxy, cloud hosting, or “American Samoa hosting” pages without local operator/address evidence are false-positive leads.

Promotion thresholds:

- `commercial_colo`: operator or contract explicitly sells AS-located racks/colo/hosting and names or anchors the facility.
- `government_dc`: ASG/ASTCA/federal source names a government data center, status, and place.
- `telecom_cable_station`: cable landing station, beach joint, CLS, NOC, or core site without customer hosting evidence.
- `enterprise_server_room`: bank, hospital, school, port, cannery, or agency internal IT room with physical-site evidence.
- `connectivity_only`: cable route, tower, VSAT, Starlink, fiber coverage, broadband grant.

---

## 7. Refresh Instructions

On every refresh, recheck: ASTCA site/RFPs, ASG press and procurement, FCC cable/public-notice records, USAC high-cost/E-rate records, SAM.gov/USAspending, NTIA/BEAD, DOI OIA, ASPA utility notices, four cloud-region lists, and cable sources for Le Vasa/SAS-2/Hawaiki/ASH/SAS/Manatua. Update the “no commercial colo / no hyperscale region” baseline only when new A-grade evidence changes it.
