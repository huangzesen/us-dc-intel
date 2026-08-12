# SC Explorer Official — Seychelles Datacenter Enumeration via Planning, Communications, Energy, Data Protection, and Public-Sector Sources

Date: 2026-08-12. Country: **SC Seychelles**. Division model: **27 districts** from `world-manifest.jsonl`: Anse aux Pins, Anse Boileau, Anse Etoile, Au Cap, Anse Royale, Baie Lazare, Baie Sainte Anne, Beau Vallon, Bel Air, Bel Ombre, Cascade, Glacis, Grand Anse Mahe, Grand Anse Praslin, La Digue, English River, Mont Buxton, Mont Fleuri, Plaisance, Pointe Larue, Port Glaud, Saint Louis, Takamaka, Les Mamelles, Roche Caiman, Ile Perseverance I, Ile Perseverance II. Angle: **official / regulatory / primary-source methodology** for finding operational, under-construction, planned, and institutional datacentre facilities.

Reliability grades: **A** = official/primary source that proves the relevant claim (planning/ePlanning record, Gazette/legal instrument, SCRA/DICT/SIB/Information Commission/PUC/URC page, operator official page, TIA/Uptime certification registry, cable-system/operator page, cloud-provider official region page). **B** = reputable press/trade source with named parties, dates, and places (Seychelles Nation, SBC, Seychelles News Agency, DCD, Developing Telecoms, Submarine Networks when not the cable owner/operator). **C** = directories, marketplaces, SEO hosting pages, social posts, republished press, or claims without address/facility evidence.

---

## 0. Verified national baseline

- Seychelles is a small island market. Datacentre-relevant infrastructure is concentrated on **Mahé**, especially Victoria/port areas, Perseverance, Providence/Roche Caiman/Cascade, and Bon Espoir/Montagne Posee. Praslin and La Digue may have telecom PoPs but no public dedicated DC evidence found in this pass.
- Two commercial/operator datacentres are confirmed from primary evidence:
  - **Airtel Seychelles Limited, Airtel House, Josephine Cafrine Road, Perseverance, Mahé**. TIA/EPI prove an **ANSI/TIA-942-B Constructed Facility, Rating Level 3** certificate for this address, certificate `TIA942SC221107001`, awarded 2022-11-07 with expiry shown as 2025-11-06. Because that expiry is before the 2026-08-12 methodology date, treat certification currency as a refresh check even if registry snippets still show status text such as active. Ericsson announced the 2021 turnkey relocation/modernisation of Airtel Africa Seychelles network/core services into a new Seychelles data center. Assign to **Ile Perseverance I** only if no better parcel/district evidence is found; otherwise use the ePlanning/parcel district.
  - **Cable & Wireless (Seychelles) Limited, Data Center 1 - Bon Espoir / Bon Espoir Data Centre**. Uptime Institute lists the project as **Data Center 1 - Bon Espoir**, client Cable & Wireless (Seychelles) Limited, location **Anse Boileau, Seychelles**. Seychelles Nation reported the Bon Espoir DC announcement on 2023-08-22, launch on 2024-09-21, and inauguration on 2024-11-22; SBC says the site is at Bon Espoir, Montagne Posee. Treat the district as **Anse Boileau** unless SPA/ePlanning proves a different boundary assignment.
- Capacity is not public for either facility. Do not infer MW, racks, sqm, or IT load from certification, capex, cable bandwidth, or marketing claims. Use `capacity_mw: null` unless an explicit primary source states capacity.
- No independent carrier-neutral colocation provider and no AWS/Azure/GCP/OCI Seychelles cloud region were confirmed. Recheck official cloud-region pages during each refresh because reseller pages and edge/connectivity offers are common false positives.
- Landing stations and cable heads are **connectivity infrastructure**, not datacentres by default. Promote them to facility records only if a source says they host servers/colo/cloud or there is a planning/operator record for a data hall.

---

## 1. Official and primary sources

### 1.1 Planning and building permits

Primary route:
- Seychelles Planning Authority: https://www.spa.gov.sc/
- ePlanning portal: https://eplanning.gov.sc/Landing.aspx
- monServis / eGov gateway: https://www.monservis.sc/ and https://egov.sc/
- Official Gazette: https://www.gazette.sc/

Use SPA/ePlanning for address, parcel, district, building use, generators, cooling plant, telecom rooms, substations, approvals, refusals, appeals, and planning conditions. Gazette notices can confirm public notices, statutory instruments, development decisions, or legal boundary references.

Planning query terms:
```text
"data centre" OR "data center" OR datacentre
"server room" OR "server farm" OR "ICT facility" OR "network operations centre"
"telecommunications equipment" OR "telecom building" OR "cable landing station"
"backup generator" OR "standby generator" OR UPS OR substation OR cooling
"Bon Espoir" OR "Montagne Posee" OR "Perseverance" OR "Josephine Cafrine Road"
"Providence" OR "Roche Caiman" OR "New Port" OR "Ile du Port" OR "Victoria"
"North East Point" OR "Beau Vallon" OR "landing station"
"centre de données" OR "salle de serveurs" OR "hébergement" OR "générateur de secours"
```

Extract from each record: application number, applicant/legal entity, parcel/address, district, development description, floor area if stated, generator/substation/cooling details, decision status/date, conditions, appeal history, and source URL/file.

### 1.2 Communications regulator and telecom law

Primary route:
- Seychelles Communications Regulatory Authority (SCRA): https://scra.sc/
- Communications Act 2023: Gazette PDF at `gazette.sc/sites/default/files/2023-04/Act 3 - 2023 - Communications Act 2023.pdf`
- Communications (Licensing) Regulations 2026, S.I. 1 of 2026: National Assembly page and Gazette supplement, January 2026.
- Legacy telecom role: Department of Information Communications Technology (DICT): https://ict.gov.sc/

SCRA establishes the authorised-operator universe and licence classes. Use it to pivot from licensees to facilities; it is not a complete facility register. The Communications Act 2023 defines facilities-based and services-based operator concepts; the 2026 licensing regulations are the current licence framework. For pre-SCRA infrastructure, search DICT-era records and operator announcements.

Queries:
```text
site:scra.sc Seychelles "Cable & Wireless" OR Airtel OR Intelvision
site:scra.sc Seychelles "facilities-based" OR "services-based" OR licence OR license
site:gazette.sc "Communications Act" "2023" Seychelles
site:gazette.sc "Communications (Licensing) Regulations" "2026"
site:ict.gov.sc Seychelles "data centre" OR "data center" OR hosting OR server
```

### 1.3 Datacentre certification registries

These are Grade A for the certification/address claim and often the cleanest facility evidence in Seychelles.

- TIA-942 registry: https://tiaonline.org/942-datacenter/airtel-seychelles-limited/ confirms Airtel Seychelles Limited at Airtel House, Josephine Cafrine Road, Perseverance, with ANSI/TIA-942-B Constructed Facility Rating Level 3 certification metadata. Recheck current status because the certificate date range found in this pass ends 2025-11-06.
- EPI certified clients: https://www.epi-certification.com/sites/details/1053 confirms the Airtel address and Rated 3 certificate dates; use it to verify whether renewal has been posted.
- Uptime Institute awards: https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-1--bon-espoir/2230 and client page `/client/cable--wireless-seychelles-limited/1316` confirm CWS **Data Center 1 - Bon Espoir**, location Anse Boileau, Seychelles.

Certification caveat: certification proves the certified facility and reliability tier/design/construction status shown by the registry. It does **not** prove MW capacity, commercial availability, or exact parcel boundaries.

### 1.4 Government ICT, investment, data protection, and procurement

Primary routes:
- DICT: https://ict.gov.sc/ for e-government, national ICT policy, government systems, and historic telecom administration.
- National Tender Board: https://www.ntb.sc/ for hosting, server, disaster recovery, NOC, and government ICT tenders.
- Seychelles Investment Board / Invest in Seychelles ICT page: https://investinseychelles.com/key-sectors/ict officially lists **Data Centers** and **Submarine Cable Links** as ICT opportunities.
- Information Commission: https://www.infocom.sc/data-protection/ for the Data Protection Act 2023 framework; Gazette Act 24 of 2023 is the primary legal text.
- Seychelles Licensing Authority: https://www.sla.gov.sc/ and Business Licence Search via eGov/intra.egov.sc for entity validation.
- Financial Services Authority: https://fsaseychelles.sc/ for financial-sector entities that may create hosting demand, not facility evidence by itself.

Queries:
```text
site:ntb.sc Seychelles "data centre" OR "data center" OR hosting OR server OR disaster recovery
site:ict.gov.sc Seychelles hosting OR "data centre" OR "e-government" OR server
site:infocom.sc Seychelles "Data Protection Act" OR registration OR processor
site:investinseychelles.com "Data Centers" "Submarine Cable Links"
site:sla.gov.sc "Cable & Wireless" OR Airtel OR Intelvision
```

### 1.5 Energy, utilities, and environment

Primary routes:
- Public Utilities Corporation: https://www.puc.sc/
- Utilities Regulatory Commission: https://urc.sc/
- Ministry of Agriculture, Climate Change and Environment / energy-environment portfolios: https://macce.gov.sc/
- Environment/LWMA routes for generator, waste, and EIA corroboration.

Use energy records as corroboration for large electrical loads, substations, standby generation, fuel storage, or environmental conditions. Do not promote a site solely because it has a generator or telecom power connection.

Queries:
```text
site:puc.sc Seychelles "data centre" OR "large power" OR substation OR MVA OR kVA
site:urc.sc Seychelles electricity licence OR tariff OR substation
site:macce.gov.sc Seychelles generator OR "backup power" OR EIA OR "Bon Espoir" OR Perseverance
"Seychelles" "data centre" generator OR UPS OR cooling OR substation
```

### 1.6 Submarine cable primary/connectivity chain

| Cable / system | Best sources | Seychelles signal | Enumeration handling |
|---|---|---|---|
| **SEAS / Seychelles East Africa System** | WIOCC SEAS page; EIB/AfDB project documents; Gazette/DICT/press for historic local notices | WIOCC states SEAS is a 1,917 km cable from Mahé/Seychelles to Dar es Salaam and that the Seychelles cable landing station is in **Victoria**. Older ESIA/press material references a **Beau Vallon** shore approach/landing. | Record both: Victoria CLS/operator-site evidence and Beau Vallon shore-approach history. Do not call it a datacentre without server/colo evidence. |
| **PEACE / SSC-II** | Submarine Networks, SCS/DICT/AfDB/EIB material, Seychelles Nation | Submarine Networks reported PEACE landed at **Perseverance Island** in early March 2022 and was expected RFS in May; Seychelles Nation later reported operational/commercial service in 2022. | Treat as a Perseverance cable/landing lead. It may support Airtel/CWS/SCS network sites but is not a DC record by itself. |
| **2Africa Seychelles branch / ISCS** | 2Africa official site, Submarine Networks, IFC project material, Intelvision/Vodafone references, Seychelles Nation | Intelvision/Vodafone landed 2Africa at **North East Point** on 2023-04-20; Nation reported expected live date around September 2023; IFC financing up to US$20m is for the branch. | District boundary can be Anse Etoile or Glacis; assign only after parcel/boundary confirmation. Keep as connectivity infrastructure unless hosting evidence appears. |

Cable queries:
```text
"Seychelles" "landing station" Victoria OR "cable landing station"
"SEAS" "Seychelles" "Victoria" OR "Beau Vallon"
"PEACE cable" Seychelles Perseverance
"Seychelles Cable Systems" PEACE "Perseverance"
"2Africa" Seychelles "North East Point" Intelvision Vodafone IFC
```

### 1.7 Official cloud-region absence checks

Check the official pages on every refresh:
- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of this methodology pass, none lists a Seychelles cloud region/local zone. Record local reseller/VPS/cloud pages as service evidence only unless a hyperscaler official page names Seychelles.

---

## 2. Division coverage workflow

Run the universal workflow for **each of the 27 manifest districts**. The district list below is the coverage checklist; every district must be either assigned a verified project/lead or explicitly marked no public project found.

| District | Search priority | Official-first route |
|---|---:|---|
| Anse aux Pins | Medium | Bon Espoir boundary cross-check; SPA/ePlanning, Gazette, PUC |
| Anse Boileau | High | CWS Bon Espoir / Montagne Posee; Uptime confirms Anse Boileau; SPA parcel check |
| Anse Etoile | High | North East Point / 2Africa boundary cross-check; SPA coastal records |
| Au Cap | Medium | Bon Espoir boundary cross-check; telecom/generator permits |
| Anse Royale | Low | Generic SPA/Gazette/PUC sweep |
| Baie Lazare | Low | Generic SPA/Gazette/PUC sweep |
| Baie Sainte Anne | Medium | Praslin telecom PoPs, fibre rollout, cable centres; no DC without primary evidence |
| Beau Vallon | Medium | SEAS historic shore approach; distinguish shore cable from Victoria CLS |
| Bel Air | Medium | Victoria CBD/government/banking server-room leads |
| Bel Ombre | Low | Generic SPA/Gazette/PUC sweep |
| Cascade | Medium | Providence / airport-industrial boundary checks, telecom sites |
| Glacis | High | North East Point / 2Africa boundary cross-check |
| Grand Anse Mahe | Low | Generic SPA/Gazette/PUC sweep |
| Grand Anse Praslin | Medium | Praslin telecom PoPs; no DC without primary evidence |
| La Digue | Medium | Telecom PoPs/fibre rollout; no DC without primary evidence |
| English River | High | Victoria/New Port/Ile du Port, CWS/SEAS/PEACE/SCS legacy infrastructure |
| Mont Buxton | Low | Victoria fringe; generic government/telecom sweep |
| Mont Fleuri | Medium | UniSey/ISCEICT historical institutional data-centre lead; NTB/UniSey validation |
| Plaisance | Medium | Providence boundary, telecom and enterprise ICT sites |
| Pointe Larue | Medium | Airport/industrial/Freeport telecom and power records |
| Port Glaud | Low | Generic SPA/Gazette/PUC sweep |
| Saint Louis | Medium | Victoria CBD, CWS HQ/legacy exchange, banks/government |
| Takamaka | Low | Generic SPA/Gazette/PUC sweep |
| Les Mamelles | Low | Greater Victoria fringe; generic sweep |
| Roche Caiman | High | Providence Industrial Estate, Intelvision HQ/hosting leads |
| Ile Perseverance I | High | Airtel DC; TIA/EPI certification renewal check; PEACE landing; Airtel House parcel check |
| Ile Perseverance II | High | Airtel/PEACE boundary cross-check; do not duplicate Ile Perseverance I record |

District universal query template:
```text
"{district}" "Seychelles" "data centre" OR "data center" OR datacentre OR "server room" OR "salle de serveurs"
"{district}" "Seychelles" telecom OR "landing station" OR "cable station" OR "network operations"
"{district}" "Seychelles" generator OR UPS OR substation OR cooling OR "backup power"
site:spa.gov.sc "{district}" server OR data OR telecom OR generator
site:gazette.sc "{district}" "data centre" OR telecom OR generator OR substation
site:ntb.sc "{district}" hosting OR server OR "disaster recovery"
```

---

## 3. Facility seed list for enumerators

This is a seed list, not the final census. Reverify each record during district enumeration and preserve null capacity where no explicit capacity source exists.

| Seed | Preferred district assignment | Status | Grade | Best evidence path |
|---|---|---|---|---|
| Airtel Seychelles Limited data centre | Ile Perseverance I unless parcel says II | Operational | A | TIA registry; EPI registry and renewal status; Airtel contact address; Ericsson 2021 launch; Nation/SNA/SBC for public opening/use |
| Cable & Wireless Data Center 1 - Bon Espoir | Anse Boileau | Operational | A | Uptime Institute project/client pages; Nation 2023/2024 articles; SBC Bon Espoir/Montagne Posee item; SPA parcel |
| CWS legacy Victoria exchange/server facilities | English River / Saint Louis / Bel Air / Mont Fleuri, verify address | Lead only | B/C until primary | CWS corporate/legacy docs, SPA/Gazette, SCRA/DICT, cable records |
| Intelvision Providence hosting/network infrastructure | Roche Caiman or Cascade/Plaisance boundary, verify | Lead only | B/C until primary | Intelvision official address/services, SCRA/SLA, 2Africa material, SPA Providence records |
| SEAS cable landing infrastructure | Victoria/English River plus Beau Vallon shore history | Connectivity site | A for cable, not DC | WIOCC SEAS, EIB/AfDB ESIA/project docs, SPA/coastal records |
| PEACE landing infrastructure | Perseverance district to verify | Connectivity site | A/B for cable, not DC | Submarine Networks; SCS/DICT/AfDB/EIB; Nation operational article |
| 2Africa North East Point landing | Anse Etoile or Glacis, verify | Connectivity site | A/B for cable, not DC | 2Africa, IFC, Submarine Networks, Intelvision/Vodafone, Nation |
| India-Seychelles Centre for Excellence in ICT data-centre lead | Mont Fleuri | Historical/institutional lead | B until current official proof | Nation 2011 article; UniSey/ISCEICT/NTB validation |
| Government/DICT hosting | Victoria districts, verify | Internal lead | C until tender/facility proof | DICT, NTB, eGov, Gazette |

---

## 4. Pitfalls and decision rules

- **District boundaries are the biggest error source.** Bon Espoir/Montagne Posee is now best assigned to Anse Boileau because Uptime says Anse Boileau, but still verify parcel-level SPA records. North East Point straddles Anse Etoile/Glacis search space. Providence spans common-search usage across Roche Caiman/Cascade/Plaisance/Pointe Larue. Perseverance has two districts; use parcel evidence before duplicating records.
- **Marketing chronology conflicts.** CWS press called Bon Espoir a national first in 2023, but Airtel has primary 2021/2022 facility and 2022 TIA certification evidence. Record each facility independently.
- **Certification grade is not capacity.** TIA Rated 3 and Uptime/Tier references are reliability/certification evidence only; always record certificate dates and renewal status separately from facility existence.
- **Press can name real facilities but is not always Grade A.** Nation, SBC, SNA, DCD, Developing Telecoms, and Submarine Networks are usually Grade B unless they are reproducing a primary registry/operator page that is separately cited.
- **Cable landing stations are not datacentres.** Keep cable records in notes/connectivity unless server/hosting/colo evidence is explicit.
- **Avoid `.sc` pollution.** Always include `Seychelles`, an operator name, or a Seychelles place name; plain `SC data center` returns South Carolina.
- **No deletion in enumeration.** If an old lead cannot be verified, retain it as a lead with downgraded grade and a note naming the missing evidence rather than silently dropping it.
