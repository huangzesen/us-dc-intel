# TZ Explorer Industry - Tanzania Datacenter Discovery

Date: 2026-08-12. Scope: Tanzania datacenter enumeration from industry media, local press, operator/developer pages, vendor case studies, cloud-region announcements, interconnection/cable records, and region-level search patterns. Use this with `explorer-official.md`: press discovers leads; official sources decide status, location, and reliability.

Reliability grades:
- **A** = official/primary: operator facility page, government/regulator page, TCRA/NEMC/TANESCO/EWURA/TISEZA/eGA/PDPC document, official cloud-provider location page, Uptime Institute certification/award record.
- **B** = strong secondary: DCD, W.Media, Connecting Africa, Developing Telecoms, Capacity, ITWeb Africa, TanzaniaInvest, Daily News/The Citizen/Guardian business reporting, Africa Data Centres Association, credible vendor/finance case study, TIX/PeeringDB/Submarine Cable Map for network-node presence.
- **C** = weak lead: aggregator/directory entry, social post, LinkedIn claim, market-report teaser, investment-promotion copy, or MoU without later project evidence.

Grade each claim separately. Example: an operator page can be A for facility existence, a DCD article B for phase/capacity/status, and a directory C for street address.

---

## 0. Tanzania market frame

- Tanzania is a small but emerging datacenter market concentrated in **Dar es Salaam**. The priority commercial/operator seeds are **Raxio TZ1**, **Wingu Africa Tanzania**, **NIDC/TTCL**, **Vodacom Business**, **Tigo/Yas**, **Airtel**, and smaller ISP/hosting operators such as **Aptus** and **Flashnet**.
- Current high-confidence operator posture:
  - **Raxio Tanzania / TZ1**: official Raxio page says launch in **2026**, outskirts of Dar es Salaam, carrier-neutral Tier III facility, **800 racks**, **4,000 m2**, **6 MW IT power**. Press in July 2026 repeats the same core specifications.
  - **Wingu Africa Tanzania**: official Wingu page confirms Tanzania operations and carrier-neutral colocation/interconnection/cloud-connect services. Press and directories place the facility in Dar es Salaam/Mbezi, with phase 1 live from 2022 and 2025 expansion toward **3 MW**; verify facility capacity through Wingu primary material where possible.
  - **NIDC/TTCL**: official NIDC pages state Government of Tanzania constructed the National Internet Data Center in 2015; NIDC is described as a Tier-III Dar es Salaam facility with cloud/colocation services.
- Government/pipeline clusters:
  - **Dodoma**: eGA/government shared data-centre infrastructure, national ICT systems, and possible planned national data-centre items. Use eGA and ministry `.go.tz` records before press.
  - **Zanzibar Urban/West (Mjini Magharibi)**: Zanzibar e-government and planned data-centre/MoU leads. Keep Oman Data Park and other Zanzibar items as planned/C-B leads unless procurement/construction/operation is verified.
  - **Pwani/Coast (Kibaha/Kwala)**: SEZ/industrial-park watch area; not a datacenter until a named facility appears.
- International connectivity is a discovery hook, not facility proof. Tanzania has Dar es Salaam cable evidence for **EASSy**, **SEACOM**, **SEAS**, and **2Africa**. 2Africa Tanzania activation was reported in 2024, so treat it as a current cable/connectivity lead. **DARE1** southward extension is planned for ready-for-service around 2028 and should remain a future lead.
- Cloud: no official AWS, Azure, Google Cloud, or Oracle OCI public region is in Tanzania as of 2026-08-12. Kenya and South Africa region announcements are useful demand/latency context only.
- Search both English and Swahili: `data centre`, `data center`, `datacentre`, `colocation`, `co-location`, `carrier-neutral`, `Tier III`, `Uptime`, `MW`, `racks`, `white space`, `sovereign cloud`, `government cloud`, `data localisation`, `NICTBB`, `landing station`, `kituo cha data`, `kituo cha kuhifadhi data`, `hifadhi ya data`, `seva`, `chumba cha seva`, `mkongo wa taifa wa mawasiliano`.

Key sources checked during this rewrite:
- Raxio Tanzania: https://www.raxiogroup.com/data-centres/tanzania/
- Wingu Africa: https://www.wingu.africa/
- Wingu news: https://www.wingu.africa/news
- NIDC about/history: https://nidc.co.tz/about and https://nidc.co.tz/history
- TCRA licences and public DC specification: https://www.tcra.go.tz/services/licenses and https://www.tcra.go.tz/tcra-tovuti/2025/mamlaka-website/documents/minimum-technical-specs/en_1748239940_MINIMUM_TECHNICAL_SPECIFICATIONS_FOR_PUBLIC_DATA_CENTER_1_1032107643381814476641029946369102376331747724695814_a576d69b16.pdf
- eGA Data Center Standards: https://www.ega.go.tz/pdf-viewer?file=https%3A%2F%2Fwww.ega.go.tz%2Fuploads%2Fstandarddocuments%2Fsw-1773257204-FINAL+Reviewed_Data+Center+Standards+and+Guidelines+for+Public+Institutions-18.2.2026.pdf
- DCD Tanzania/Raxio/Wingu/Zanzibar items: https://www.datacenterdynamics.com/en/news/
- W.Media Raxio TZ1 article: https://w.media/raxios-tz1-to-add-6-mw-and-800-racks-to-tanzanias-data-center-market/
- Developing Telecoms Wingu expansion: https://developingtelecoms.com/telecom-technology/data-centres-networks/18213-wingu-starts-second-phase-of-data-centre-expansion-in-tanzania.html
- Submarine Cable Map Dar es Salaam: https://www.submarinecablemap.com/landing-point/dar-es-salaam-tanzania
- Airtel/2Africa activation coverage: https://www.submarinenetworks.com/en/systems/asia-europe-africa/2africa/airtel-activates-2africa-cable-linking-kenya%2C-tanzania%2C-and-south-africa
- DARE1 extension coverage: https://www.submarinenetworks.com/en/systems/asia-europe-africa/dare1/djibouti-telecom-announces-dare1-route-extension

---

## 1. Industry and trade press sources

Use press to discover aliases, project names, launch dates, funding, capacity, and status verbs. Then verify with operator, TCRA, NEMC, council/Tausi, TANESCO/EWURA, eGA, TISEZA, Uptime, or cloud-provider sources.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ plus searches for Tanzania, Dar es Salaam, Raxio, Wingu, Zanzibar | Best global industry feed for Raxio TZ1, Wingu expansion, NIDC historical articles, DARE1/cable context, Zanzibar MoU leads. | B |
| W.Media | https://w.media/ | Raxio TZ1 July 2026 specs: 6 MW, 800 racks, 4,000 m2, Dar outskirts, launch year. | B |
| Connecting Africa | https://www.connectingafrica.com/ | East Africa cloud, cable, Raxio/Oracle/iXAfrica regional items. | B |
| Developing Telecoms | https://developingtelecoms.com/ | Wingu Dar expansion; DARE1 extension; telco/cable developments. | B |
| Capacity Media / TechAfrica News / CIO Africa / ITWeb Africa / The Exchange Africa / TechCabal | https://www.capacitymedia.com/ , https://techafricanews.com/ , https://cioafrica.co/ , https://itweb.africa/ , https://theexchange.africa/ , https://techcabal.com/ | Secondary leads for connectivity, cloud, financing, and regional digital-infrastructure projects. | B/C |
| TanzaniaInvest | https://www.tanzaniainvest.com/ | Investment, TCRA licence counts, TISEZA/SEZ updates, telecom market context. | B |
| Daily News / The Citizen / IPP Media / Business Times / TanzaniaInsight / InAfrika | https://dailynews.co.tz/ , https://www.thecitizen.co.tz/ , https://ippmedia.co.tz/ , https://tanzaniainsight.com/ , https://inafrika.co.tz/ | Local government announcements, Zanzibar/Dodoma data-centre leads, Wingu local features, telecom and budget items. | B/C |
| Africa Data Centres Association | https://africadca.org/ | Association/member announcements; Wingu financing announcement. | B |
| TIX / PeeringDB / Submarine Cable Map / Submarine Networks | http://tix.or.tz/ , https://www.peeringdb.com/ , https://www.submarinecablemap.com/ , https://www.submarinenetworks.com/ | IXP, facility/interconnect, cable landing and activation leads. Use only for network-node presence unless facility details are explicit. | B for presence |
| Aggregators: DataCenterMap, Baxtel, OCOLO, ColoMap, datacenters.com, Inflect, colo.exchange | Search by country/city/operator | Useful for discovering older telco/ISP/enterprise sites and addresses, especially Vodacom, Tigo, Aptus, NIDC, Wingu. | C; B- only when directly backed by a cited primary source |
| Vendor/integrator case studies | Schneider Electric, Vertiv, Huawei, ZTE, Caterpillar, Siemens/Siemon, electrical contractors, finance banks | Can prove construction/equipment delivery or expansion milestones. | B/C depending specificity |

Trade-press query templates:
```text
site:datacenterdynamics.com/en/news/ Tanzania "data center"
site:datacenterdynamics.com/en/news/ "Raxio" Tanzania
site:datacenterdynamics.com/en/news/ "Wingu" Tanzania
site:w.media/ "Raxio" "TZ1" Tanzania
site:developingtelecoms.com Wingu Tanzania "data centre"
site:connectingafrica.com Tanzania "data centre" OR "data center"
site:tanzaniainvest.com Tanzania "data centre" OR "data center" OR TCRA
site:dailynews.co.tz "data centre" OR "kituo cha data" Zanzibar OR Dodoma
site:thecitizen.co.tz Wingu OR Raxio OR "data centre"
"Tanzania" "data centre" "Tier III" "Dar es Salaam"
"Tanzania" "data center" "MW" "racks"
```

Status verbs:
- `announces`, `plans`, `MoU`, `agreement`, `expected`, `set to` = planned/intent.
- `land acquired`, `breaks ground`, `starts construction`, `financing secured`, `phase begins` = pipeline/under construction if source is credible.
- `opened`, `launched`, `operational`, `ready for service`, `hosts customers`, `constructed facility certified` = operational candidate; verify with operator/Uptime/TCRA.
- `designed`, `Tier III standard`, `Tier III compliant` = design/marketing language; do not call it Uptime certified unless Uptime or the operator explicitly says certification and ideally an award record is found.

---

## 2. Operator and developer sweep

| Operator / developer | Official / primary URL | Tanzania region/locality signals | Research handling |
|---|---|---|---|
| Raxio Tanzania / TZ1 | https://www.raxiogroup.com/data-centres/tanzania/ | Dar es Salaam outskirts; launch 2026 | A for Raxio's own existence/capacity/status claim; B for W.Media/DCD coverage. Verify TCRA NFL/public DC compliance, NEMC, LGA permits, TANESCO 33 kV, and Uptime award. |
| Wingu Africa Tanzania | https://www.wingu.africa/ and https://www.wingu.africa/news | Dar es Salaam; Mbezi lead from press/directories | A for Wingu Tanzania operation and service claims; B for 2025 expansion/3 MW articles unless Wingu primary page confirms details; C for directory addresses/rack counts until corroborated. |
| NIDC / TTCL | https://nidc.co.tz/ , https://www.ttcl.co.tz/ | Dar es Salaam | A for NIDC existence/history/services. DCD 2016 utilisation story is B historical context. Verify with TTCL/TCRA/eGA/PeeringDB. |
| Vodacom Business Tanzania | https://www.vodacom.co.tz/ | Dar es Salaam and Dodoma leads | Directories list Laibon Road and Lusinde Road; use as C leads until official business page/TCRA/council evidence confirms. |
| Tigo / Yas Tanzania | https://www.yas.co.tz/ | Dar es Salaam telco-core and possible data-centre/hosting leads | Search both `Tigo` and `Yas`; distinguish telco core from commercial colo. |
| Airtel Tanzania / Airtel Telesonic | https://www.airtel.co.tz/ | Dar es Salaam cable/network lead; 2Africa landing/activation | Relevant for cable and telco infrastructure. Do not count Nxtra Kenya or Airtel Africa regional DC programme as Tanzania facilities. |
| eGA / MICIT / public institutions | https://www.ega.go.tz/ and ministry/government `.go.tz` | Dodoma, Dar es Salaam, Zanzibar leads | A for eGA standards/strategy; facility-level status requires exact government/procurement/operator source. |
| Zanzibar government / Oman Data Park / Silicon Zanzibar leads | Zanzibar government, ZIPA, DCD, local press | Zanzibar Urban/West, Fumba/Zanzibar City | Treat 2022 Oman Data Park MoU and later government priority statements as planned leads until construction/operation evidence appears. |
| Zantel, Halotel, Smile, CBN, Sasatel, Simbanet, Liquid, Flashnet, Aptus | Operator sites + TCRA | Dar es Salaam, Zanzibar, regional POPs | Good for telco/ISP hosting leads. Count only physical hosting/colo facilities, not retail/service offices. |
| Banks/enterprise | BoT, CRDB, NMB, DSE filings, tender pages | Dar es Salaam; DR in Dodoma/Mwanza/Arusha possible | Usually private enterprise DC/DR. Grade B/C unless official tender/annual report gives site and function. |

Operator query templates:
```text
"Raxio TZ1" "launch" Tanzania
"Raxio Tanzania" "6 MW" "800 racks" "4,000"
"Raxio" Tanzania TCRA OR NEMC OR TANESCO OR "33kV"
"Wingu Africa" Tanzania "Dar es Salaam"
"Wingu" Tanzania "phase 2" OR "3MW" OR "3 MW"
"Wingu" Tanzania Uptime OR "Tier III"
"NIDC" OR "National Internet Data Center" Tanzania colocation OR cloud
"TTCL" Tanzania "data centre" OR "data center"
"Vodacom Tanzania" "data centre" OR "data center" OR "cloud"
"Tigo" OR "Yas" Tanzania "data centre" OR "hosting"
"Airtel Tanzania" "2Africa" "data centre" OR "landing"
"Zanzibar" "Oman Data Park" "data center"
```

---

## 3. Official verification pivots from press

Every press/operator lead should be joined against one or more official surfaces:

| Channel | URL / route | How to use | Grade |
|---|---|---|---|
| TCRA licence register | https://www.tcra.go.tz/services/licenses | Search Telecommunications & Internet licensees and certificates; extract legal name, licence type, number, dates, address/town. | A |
| TCRA public DC specification | TCRA/TS013 PDF under `tcra.go.tz/.../minimum-technical-specs/` | Confirms public DC technical/specification regime and definitions; not a facility list. | A |
| NEMC/PMS | https://eia.nemc.or.tz/ and https://www.nemc.or.tz/ | Search EIA/EA project titles, proponents, ESIA PDFs/notices. | A |
| LGA/Tausi permits | https://tausi.tamisemi.go.tz/ plus council sites | Building permits and occupancy certificates for physical construction. | A when record found |
| EWURA/TANESCO | https://www.ewura.go.tz/ and https://www.tanesco.co.tz/ | Utility connection, generation/registration/licensing, substation/feeders, PPAs. | A |
| TISEZA | https://www.tiseza.go.tz/ | Investment registration, incentives, SEZ/EPZ instruments, Kwala/other zone leads. | A |
| eGA/government | https://www.ega.go.tz/ and `.go.tz` ministry/Zanzibar sites | Government DC standards, shared infrastructure, Dodoma/Zanzibar project status. | A |
| PDPC/PDPA | https://pdpc.go.tz/ | Data-protection registration and cross-border-transfer context; demand signal. | A for legal context |
| Uptime Institute | https://uptimeinstitute.com/uptime-institute-awards/list | Verify Tier Certification of Design Documents, Constructed Facility, or Operational Sustainability. | A for certification |
| Cloud provider pages | AWS/Azure/GCP/Oracle official locations | Verify absence/presence of hyperscale regions. | A |

Official-search templates:
```text
site:tcra.go.tz "{operator}" licence
site:tcra.go.tz "{operator}" "Network Facilities"
site:nemc.or.tz "{operator}" OR "{project}" EIA
site:eia.nemc.or.tz "{operator}" OR "{project}"
site:tanesco.co.tz "{operator}" "33kV" OR MVA OR substation
site:ewura.go.tz "{operator}" OR "{project}" "MW"
site:tiseza.go.tz "{operator}" OR "data centre" OR "Kwala"
site:ega.go.tz "data centre" OR "data center" OR "cloud"
site:go.tz "{region}" "data centre"
"{operator}" "building permit" "{council}"
```

---

## 4. Search patterns

### 4.1 English discovery templates

```text
"{region}" Tanzania ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks OR "IT load")
"{region}" Tanzania ("data centre" OR "data center") ("opened" OR launched OR operational OR construction OR "breaks ground")
"{region}" Tanzania (colocation OR "carrier-neutral" OR hyperscale OR "Tier III" OR Uptime)
"{region}" Tanzania ("cloud region" OR "sovereign cloud" OR "government cloud" OR "data localisation")
"{region}" Tanzania (substation OR NICTBB OR "landing station" OR EASSy OR SEACOM OR "2Africa" OR DARE1) "data"
"{industrial park OR SEZ}" Tanzania "data centre" OR "data center"
"{operator}" "{region}" Tanzania "data centre"
```

Capacity/status pivots:
```text
"{project}" ("MW" OR "IT load" OR MVA OR racks OR sqm OR "square metres" OR "white space")
"{project}" ("phase one" OR "phase 1" OR "phase two" OR expansion OR "second phase")
"{project}" (EIA OR NEMC OR "building permit" OR "Network Facility Licence" OR TCRA OR Uptime)
"{project}" ("opened" OR operational OR "goes live" OR "ready for service" OR launched)
```

### 4.2 Swahili secondary checks

Use Swahili mainly for government/telco/local-press discovery; verify with primary documents before counting.

```text
"{region}" "kituo cha data"
"{region}" "kituo cha kuhifadhi data"
"{region}" "chumba cha seva"
"{region}" "hifadhi ya data"
"{region}" "mkongo wa taifa wa mawasiliano"
"Zanzibar" "kituo cha data"
"Dodoma" "kituo cha data" eGA
"Dar es Salaam" "kituo cha data" Wingu OR Raxio OR NIDC
```

Do not count a Swahili/local hit as a commercial datacenter unless it identifies a physical facility, operator/developer, compute/hosting purpose, and project stage.

---

## 5. Region-level enumeration method

For each of the 31 regions, run four passes:

1. **Commercial press/vendor pass**: region + main towns + `data centre/data center/datacentre/colocation/Tier III/cloud` plus Swahili terms.
2. **Operator pass**: Raxio, Wingu, NIDC, TTCL, Vodacom, Tigo/Yas, Airtel, Halotel, Zantel, Aptus, Flashnet, eGA.
3. **Official pass**: TCRA register town check, NEMC/PMS, LGA/Tausi, TANESCO/EWURA, eGA/ministry `.go.tz`, TISEZA for SEZ regions.
4. **Interconnection/aggregator pass**: TIX, PeeringDB, Submarine Cable Map, Submarine Networks, DataCenterMap, Baxtel, OCOLO, ColoMap. Verify before grading above C/B-.

### 5.1 Priority region clusters

| Region | Main towns/localities | Developer/operator seeds | Query notes |
|---|---|---|---|
| Dar es Salaam | Kinondoni, Ilala, Ubungo, Temeke, Kigamboni; Old Bagamoyo Rd, Mbezi, Laibon Rd, Posta/City Centre | Raxio TZ1, Wingu, NIDC/TTCL, Vodacom, Tigo/Yas, Airtel, Aptus, Flashnet, TIX, EASSy/SEACOM/SEAS/2Africa | Highest density. Resolve status and exact locality through operator, TCRA, NEMC, council/Tausi, TANESCO, Uptime, and interconnection records. |
| Dodoma | Dodoma City, Mtumba, Nzuguni, Chamwino | eGA/government DCs, Vodacom lead, national ICT/government-cloud leads | Search eGA standards/strategy, ministry `.go.tz`, Dodoma CC/Tausi, TCRA, TANESCO, local press. |
| Zanzibar West / Mjini Magharibi | Zanzibar City, Stone Town, Fumba | Zanzibar government planned DC, Oman Data Park MoU, Zantel, ZIPA/Silicon Zanzibar | Keep planned vs operational separate. Search Zanzibar government/e-government, ZIPA, TCRA, local press. |
| Pwani / Coast | Kibaha, Kwala, Bagamoyo, Mkuranga | Kwala SEZ/industrial park, dry port/fibre/power corridor | Watch TISEZA/NEMC/TANESCO/council for named DC tenants; SEZ land alone is not a facility. |
| Arusha | Arusha City | Telco core, banks/enterprise, EAC/NGO institutional IT | Likely negative for commercial colo; search councils and operator names. |
| Mwanza | Mwanza City, Nyamagana, Ilemela | Telco core, banks/enterprise, NICTBB node | Low probability; search annual reports/tenders and TCRA. |
| Kilimanjaro | Moshi | Telco/enterprise | Negative expected unless provider hosting emerges. |
| Mbeya, Morogoro, Tanga | Regional capitals | Telco core, banks, NICTBB/fibre corridors | Check for edge/DR facilities, not just POPs. |
| Mtwara | Mtwara town/port | DARE1 future landing lead, SEZ/port/fibre | Future cable lead only unless facility source appears. |
| Lindi, Ruvuma, Iringa, Kagera, Kigoma, Rukwa, Shinyanga, Singida, Tabora, Manyara, Geita, Katavi, Njombe, Simiyu, Songwe | Regional capitals | Telco POPs, government ICT, banks | Use universal recipe and record negatives. |
| Pemba North/South, Zanzibar North/South | Wete, Chake-Chake, Mkokotoni, Koani | Zanzibar government/telco POPs; possible shared government ICT | Search official Zanzibar names and Swahili; expect negative outside Urban/West. |

### 5.2 Exact 31-region quick queries

```text
Arusha Tanzania "data centre" OR "data center" OR datacentre
"Dar es Salaam" Tanzania (Raxio OR Wingu OR NIDC OR TTCL OR Vodacom OR Tigo OR Yas OR Airtel) "data centre"
Dodoma Tanzania (eGA OR Vodacom OR "national data centre" OR "government cloud") "data centre"
Geita Tanzania "data centre" OR "data center" OR datacentre
Iringa Tanzania "data centre" OR "data center" OR datacentre
Kagera Tanzania "data centre" OR "data center" OR datacentre
Katavi Tanzania "data centre" OR "data center" OR datacentre
Kigoma Tanzania "data centre" OR "data center" OR datacentre
Kilimanjaro OR Moshi Tanzania "data centre" OR "data center" OR datacentre
Lindi Tanzania "data centre" OR "data center" OR datacentre
Manyara Tanzania "data centre" OR "data center" OR datacentre
Mara Tanzania "data centre" OR "data center" OR datacentre
Mbeya Tanzania "data centre" OR "data center" OR datacentre
Morogoro Tanzania "data centre" OR "data center" OR datacentre
Mtwara Tanzania "data centre" OR "data center" OR "landing station" OR DARE1
Mwanza Tanzania "data centre" OR "data center" OR datacentre
Njombe Tanzania "data centre" OR "data center" OR datacentre
Coast OR Pwani OR Kibaha OR "Kwala SEZ" Tanzania "data centre" OR "data center"
Rukwa Tanzania "data centre" OR "data center" OR datacentre
Ruvuma Tanzania "data centre" OR "data center" OR datacentre
Shinyanga Tanzania "data centre" OR "data center" OR datacentre
Simiyu Tanzania "data centre" OR "data center" OR datacentre
Singida Tanzania "data centre" OR "data center" OR datacentre
Songwe Tanzania "data centre" OR "data center" OR datacentre
Tabora Tanzania "data centre" OR "data center" OR datacentre
Tanga Tanzania "data centre" OR "data center" OR datacentre
"Pemba North" OR "Kaskazini Pemba" Tanzania "data centre" OR "data center"
"Pemba South" OR "Kusini Pemba" Tanzania "data centre" OR "data center"
"Zanzibar North" OR "Kaskazini Unguja" Tanzania "data centre" OR "data center"
"Zanzibar South" OR "Kusini Unguja" Tanzania "data centre" OR "data center"
"Zanzibar West" OR "Mjini Magharibi" OR "Zanzibar Urban West" Tanzania "data centre" OR "data center" OR "e-Government"
```

---

## 6. Hyperscaler and cloud-region handling

Cloud-provider pages prove region/service existence, not physical addresses. No official provider location page shows a Tanzania hyperscale public cloud region as of 2026-08-12.

| Provider | Official/primary URL | Tanzania signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Tanzania Region; Africa includes Cape Town. | Tenant/edge/partner lead only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Tanzania region; South Africa North/West are listed; Kenya/East Africa was announced with G42. | Do not count Tanzania facility without official Tanzania region or local facility source. |
| Google Cloud | https://cloud.google.com/about/locations | No Tanzania region; Johannesburg is Africa region. | Tenant/edge lead only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Tanzania region; Johannesburg and Kenya/Nairobi coming/listed. | Tanzania workloads may use Kenya/SA or local colo; no TZ facility inference. |
| Local/sovereign cloud | eGA, NIDC, Raxio, Wingu, telcos | Tanzania-hosted government/private cloud and colo services. | Map services to facilities and grade by source. |

Cloud query templates:
```text
"Tanzania" "cloud region" (AWS OR Azure OR "Google Cloud" OR Oracle)
"Tanzania" "sovereign cloud" OR "government cloud"
"Tanzania" "cloud services" NIDC OR eGA OR Raxio OR Wingu
"Tanzania" "data localisation" "cloud"
```

---

## 7. Evidence grading and pitfalls

### 7.1 Grade per data point

- **A**: official operator page; TCRA licence or technical specification; NEMC/EIA; council/Tausi permit or occupancy certificate; EWURA/TANESCO record; eGA/government document; TISEZA instrument; PDPC/legal text; Uptime award; official cloud-provider location page.
- **B**: DCD, W.Media, Connecting Africa, Developing Telecoms, Capacity, ITWeb Africa, TanzaniaInvest, credible local business press, Africa Data Centres Association, vendor/finance case study, PeeringDB/TIX/cable-map presence.
- **C**: DataCenterMap/Baxtel/OCOLO/ColoMap/datacenters.com entries, social posts, LinkedIn posts, market-report excerpts, old MoUs, uncited capacity snippets.

### 7.2 Tanzania-specific pitfalls

- **Raxio status**: official page now says launching 2026. Older articles used earlier launch years. Keep evidence date and status verb.
- **Wingu capacity**: official Wingu site confirms Tanzania operations and services; 3 MW/phase-2 details are mostly press/directory leads unless supported by Wingu primary pages.
- **Uptime wording**: `Tier III certified`, `Tier III designed`, `Tier 3`, and `Tier III standard` are not equivalent. Use Uptime Institute awards when possible.
- **2Africa correction**: current industry/cable evidence shows Tanzania/Dar es Salaam involvement and 2024 activation of the Kenya-Tanzania-South Africa segment.
- **Cable/IXP ambiguity**: cable landing stations and IXPs are network nodes, not datacenters unless colocated hosting space is explicitly described.
- **Telco core vs commercial colo**: Vodacom/Tigo/Yas/Airtel/Halotel/Zantel facilities are telecom infrastructure unless marketed or documented as colocation/hosting/cloud.
- **Government data-centre ambiguity**: local press may use "data centre" for GIS/statistics/SOC/server-room functions. Count only facilities with compute/hosting/cloud/shared-infrastructure role.
- **SEZ land != facility**: Kwala and other SEZ announcements are site-selection leads, not built datacenters.
- **Capacity units**: IT MW, facility MW, utility MVA, racks, m2, and phase buildout are not interchangeable.
- **Data-localisation claims**: PDPC/PDPA and sector rules are demand context; they do not prove a facility exists.

### 7.3 Minimum record fields

- canonical facility/campus name and aliases;
- physical region, district/council, locality/road/plot/SEZ;
- owner/operator/developer/local SPV;
- facility type and customer model;
- status and evidence date;
- capacity with exact units and phase;
- source URLs and evidence grade by field;
- notes on planned-vs-built, certification wording, and whether the site is commercial, government, telco-core, enterprise-only, IXP, or cable landing.

---

## 8. Recommended Tanzania discovery order

1. Start with Dar es Salaam operator pages: Raxio TZ1, Wingu, NIDC/TTCL, Vodacom, Tigo/Yas, Airtel, Aptus/Flashnet.
2. Pull DCD, W.Media, Developing Telecoms, Connecting Africa, TanzaniaInvest, Daily News/The Citizen for each seed; capture exact status verbs and evidence dates.
3. Verify through TCRA, TCRA/TS013, NEMC/PMS, LGA/Tausi, TANESCO/EWURA, eGA/government, TISEZA, PDPC, and Uptime.
4. Add Dodoma government/eGA and Zanzibar government/Oman Data Park leads with explicit planned/operational status.
5. Sweep Pwani/Kwala and Mtwara/cable leads as future/SEZ/cable watch areas.
6. Complete the exact 31-region negative sweep using the templates above, with official Zanzibar names included.
