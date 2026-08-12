# MU Explorer Official - Mauritius Datacenter Enumeration via Government, Regulator, Planning, Energy, Certification, and Cable Sources

Date: 2026-08-12. Country: **MU Mauritius**. Division model: **12 manifest divisions**: Agalega Islands; Black River; Cargados Carajos Shoals; Flacq; Grand Port; Moka; Pamplemousses; Port Louis; Plaines Wilhems; Rodrigues Island; Riviere du Rempart; Savanne. Scope: official and primary-source methodology for identifying operational, under-construction, planned, institutional, and lead-stage datacentre facilities.

Reliability grades: **A** = official/primary source proves the specific claim (government page, regulator licence, local-authority planning record, public procurement, certification registry, Uptime/TIA/EPI record, utility record, operator primary page, official cloud-region page, cable-system owner/landing source, MIXP/PeeringDB for IXP/node evidence). **B** = reputable press/trade/vendor source with named parties, dates, locality, and a plausible route back to a primary actor. **C** = directories, marketplaces, SEO hosting pages, social posts, aggregates, or claims without facility/address evidence. Grade each field separately: a facility can be **A** for existence/certification but **C** for capacity.

---

## 0. Verified Baseline

- Mauritius is a small, telecom- and conglomerate-led market. Public datacentre evidence clusters in **Port Louis**, **Ebene/Reduit (Moka)**, **Arsenal/Terre Rouge (Pamplemousses)**, **Rose-Belle (Grand Port)**, **Quatre Bornes/Candos and Rose Hill (Plaines Wilhems)**. Treat broad market labels from directories as unreliable for division assignment.
- The 12-division sweep is complete for the manifest: nine mainland districts plus Agalega Islands, Cargados Carajos Shoals/Saint Brandon, and Rodrigues Island. The local-authority portal currently exposes mainland councils/districts only: Port-Louis, Beau-Bassin/Rose-Hill, Curepipe, Quatre-Bornes, Vacoas/Phoenix, Riviere Du Rempart, Pamplemousses, Moka, Flacq, Grand-Port, Savanne, Black River.
- Confirmed/strongly evidenced facilities and leads:
  - **Emtel Data Centre**, B11, Plaine des Papayes Road, Arsenal, **Pamplemousses**. EPI map lists ANSI/TIA-942-B Facility - Rated 3, expiry **23-09-2026**; TIA Online lists certificate **TIA942MU230924001**, awarded **2023-09-24**, expiring **2026-09-23**. Emtel's own page states Arsenal location, Tier-3 certified facility, 100% uptime since 2012, dual 1 MW transformers, N+1 generators, and direct access to METISS, SAFE, and LION/LION2. **A** for facility, address, TIA certificate, operator claims; capacity/load still record as operator claim unless the field schema supports claim source.
  - **Mauritius Telecom Rose Belle Data Centre / RBDC**, Rose-Belle, **Grand Port**. MT/my.t business and rbdc.mu state **1,500 sq m secured rack space, 400+ racks, 3 MW**. Uptime Institute country listing shows **Rose Belle Data Centre, Phase 1** for Mauritius Telecom with **Tier IV Certification of Design Documents** and **Tier IV Certification of Constructed Facility**. Grade **A** for Uptime-listed Tier IV certification and MT primary capacity page; **B/C** only where relying on directories.
  - **Mauritius Telecom Rose Hill Tier III / RHDC**, Rose Hill, **Plaines Wilhems**. my.t business ICT/BPO page says MT hosts services in **Rose Belle Tier IV Data Centre and Rose Hill Tier III Data Centre**. DatacenterPlanet has an RHDC listing, but keep RHDC as **A for MT-page existence/Tier III claim, C for directory address/details** until a dedicated MT or planning page is found.
  - **Bhumishq / Cybercity Data Centre**, Ebene, **Moka**. Uptime Institute Mauritius country listing shows **Bhumishq Teleserve LTD, Cybercity Data Centre, Ebene** with **Tier IV Certification of Design Documents**. DataCenterMap gives Mindspace Building, 45 Wall Street, 9th Floor, Ebene and 500 sq m. Grade **A** for Uptime design-certification existence in Ebene; **C** for directory address/capacity unless Bhumishq primary confirms.
  - **Rogers Capital Technology Services**, **Moka and Port Louis**. Rogers primary page states carrier-neutral data centres in **Ebene and La Tour Koenig** and MIXP connectivity hosted in the Ebene Data Centre. ICTA lists Rogers Capital under B.01 National Networking Services, C.04 ILD, and C.08 ISP. DataCenterMap gives Port Louis, Les Cascades, La Tour Koenig, and Ebene site/address seeds. Grade **A** for licence/operator and Rogers-stated Ebene/La Tour Koenig data-centre existence; **C** for directory-only Port Louis/Les Cascades details until primary pages or planning records confirm.
  - **Government Online Centre (GOC)**, likely **Port Louis**. MITCI states GOC has been a centralised government data centre since **May 2005**, with 80-rack capacity, g-Cloud, hosting, and server co-location. Grade **A**.
  - **Government Data Centre + sovereign cloud + disaster-recovery site**, national/TBD. MITCI home/Blueprint material and the public procurement portal/RFI **MITCI/RFI/01/2025-26** establish a government sovereign-cloud pipeline. Grade **A** for policy/procurement; **C/null** for location until award/site records appear.
  - **Harel Mallac Technologies / MCS Datacenter 02**, 18 Edith Cavell Street, **Port Louis**. DataCenterMap has address and operator; Telecom Review Africa reports Tier III. Grade **C** for directory address, **B** for trade press; seek Harel Mallac primary proof.
  - **BIRGER. Candos Recovery Centre / Quatre Bornes DC1**, Royal Road/Candos, **Plaines Wilhems**. BIRGER official site proves company/services only; DataCenterMap/ColocationM carry facility details. Grade **C/B** until BIRGER publishes a facility page or planning/licence evidence.
  - **Aphelion DC3**, Noah Wealth Center, JinFei Smart City, Terre Rouge, **Pamplemousses**. DataCenterMap/UPSTACK are the main facility evidence. Grade **C** unless Aphelion primary or BLUP evidence is found; do not assign to Port Louis just because the market page says Port Louis.
  - **CEB disaster-recovery centre**, TBD lead. Public procurement references to Microsoft data-centre/disaster-recovery licences are evidence of an internal DR need, not a commercial datacentre. Grade **B lead**.
- No hyperscaler public cloud region in Mauritius was found on official AWS, Azure, Google Cloud, or OCI region/location lists. Recheck official pages every run.
- Cable landings are connectivity infrastructure, not datacentres. Promote a landing to a DC only when server/colo/hosting evidence exists. The exception with explicit DC linkage is **METISS landing at/through Emtel's Arsenal DC**.

---

## 1. Official Source Routes

### 1.1 Planning and local government

Primary URLs:
- Portal of Local Authorities: https://la.govmu.org/
- BLUP services page: https://la.govmu.org/content.jsp?page=Services
- BLUP guide PDF: https://la.govmu.org/downloads/BLP%20GUIDE.pdf
- Ministry of Local Government and Disaster Risk Management: https://localgovernment.govmu.org/
- Government e-services: https://govmu.org/EN/Pages/eservices.aspx and https://mygov.govmu.org/
- Government Printing Department / Gazette route: https://gpd.govmu.org/ plus public notices at https://govmu.org/EN/Pages/PublicNotice.aspx and https://publicnotice.govmu.org/publicnotice/

Use **Building and Land Use Permit (BLUP)** and **Outline Planning Permission** records to prove parcel/address, use class, generator/substation/cooling equipment, building area, planning conditions, approval/refusal dates, and appeals. The Local Authorities portal states that local authorities determine BLUP and Outline Planning Permission applications under the Local Government Act 2011; public access may require council inquiry, procurement record, Gazette notice, or Freedom of Information request.

Planning query templates:
```text
site:la.govmu.org "data centre" OR "data center" OR datacentre OR "server room" OR telecom
site:gpd.govmu.org Mauritius "data centre" OR "server room" OR "telecommunications building"
"Building and Land Use Permit" Mauritius "data centre" OR "server room" OR "telecom"
"Outline Planning Permission" Mauritius generator OR UPS OR substation OR cooling
"centre de donnees" OR "salle de serveurs" OR "hebergement" Mauritius
"Ebene" OR "Cybercity" OR "Rose-Belle" OR Arsenal OR "Quatre Bornes" "Building and Land Use Permit"
```

Extract: application number, applicant/legal entity, exact parcel/address, division, local authority, development description, floorspace, power/generator/cooling details, decision status/date, conditions, appeal references, URL, capture date.

### 1.2 ICT regulator - ICTA

Primary URLs:
- ICTA: https://www.icta.mu/
- Commercial Licensees: https://www.icta.mu/licences-issued/
- Public notices: https://www.icta.mu/notice-47-2026/
- Tender notices: https://www.icta.mu/tender-notices/
- Public consultations: https://www.icta.mu/public-consultations/
- Consolidated directives: https://www.icta.mu/consolidated-icta-directives/

Relevant current licence signals from ICTA Commercial Licensees:
- **A Network Infrastructure Provider**: MultiCarrier (Mauritius) Ltd.
- **B.01 National Networking Services**: Atcomm Broadband Services Ltd; CEB Fibernet Co Ltd; Rogers Capital Technology Services Ltd; Kaldera Ltd.
- **B.02 International Networking Services**: Belgacom International Carrier Services Ltd; CEB Fibernet Co Ltd.
- **C.02 PSTN**: Emtel Ltd; Mauritius Telecom Ltd.
- **C.03 PLMN**: Cellplus Mobile Communications Ltd; Emtel Ltd; Mahanagar Telephone (Mauritius) Ltd.
- **C.04 ILD**: Air Communication Ltd; Altercom Ltd; Emtel Ltd; Kaldera Ltd; Mahanagar Telephone (Mauritius) Ltd; Mauritius Telecom Ltd; Equant Mauritius Holdings Ltd; Outremer Telecom Digital Solutions Ltd; Rogers Capital Technology Services Ltd.
- **C.08 ISP**: Atcomm Broadband Services Ltd; Bharat Telecom Ltd; Cellplus Mobile Communications Ltd; Emtel Ltd; Kaldera Ltd; Mahanagar Telephone (Mauritius) Ltd; Mauritius Telecom; Millenium Internet Exchange Ltd; Outremer Telecom Digital Solutions Ltd; Rogers Capital Technology Services Ltd.

Decision rule: ICTA licences prove authorised telecom/network/ISP status, not datacentre facilities. Use licensees as pivots into planning, operator pages, interconnection, and procurement. There is no dedicated public "datacentre operator" licence class on the current ICTA list.

ICTA queries:
```text
site:icta.mu "data centre" OR "data center" OR hosting OR "sovereign cloud"
site:icta.mu "Emtel" OR "Mauritius Telecom" OR "Rogers Capital" OR "CEB Fibernet"
site:icta.mu "ICT-USF" OR "universal service" "data centre"
site:icta.mu "Network Infrastructure Provider" "MultiCarrier"
```

### 1.3 Certification registries

Primary URLs:
- EPI Mauritius certified sites: https://www.epi-certification.com/sites/map/Mauritius
- TIA Online Emtel record: https://tiaonline.org/942-datacenter/emtel-data-centre/
- Uptime Institute Mauritius awards: https://uptimeinstitute.com/uptime-institute-awards/country/id/MU
- Uptime Rose Belle record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/rose-belle-data-centre-phase-1/784

Verified certification evidence:
- **Emtel Data Centre**: EPI/TIA ANSI/TIA-942-B Facility - Rated 3; cert **TIA942MU230924001**; active until **2026-09-23**.
- **Mauritius Telecom Rose Belle Data Centre, Phase 1**: Uptime country page lists **Tier IV Certification of Design Documents** and **Tier IV Certification of Constructed Facility**.
- **Bhumishq Teleserve LTD Cybercity Data Centre, Ebene**: Uptime country page lists **Tier IV Certification of Design Documents**.

Decision rule: a design certificate does not prove constructed/operational status; a constructed facility certificate proves the certified scope, not MW, racks, customers, or future expansions. Record certification body, certification type, tier/rating, award/expiry when available, and exact registry URL.

### 1.4 Government ICT, procurement, data protection, investment

Primary URLs:
- MITCI: https://mitci.govmu.org/mitci/
- Government Online Centre: https://mitci.govmu.org/mitci/government-online-centre/
- Central Informatics Bureau: https://cib.govmu.org/
- National Computer Board: https://ncb.govmu.org/
- Data Protection Office: https://dataprotection.govmu.org/
- Public Procurement Portal: https://publicprocurement.govmu.org/publicprocurement/
- MITCI sovereign cloud RFI notice: https://publicprocurement.govmu.org/publicprocurement/?p=4897
- EDB ICT sector: https://edbmauritius.org/ict
- EDB Blueprint summary: https://edbmauritius.org/mauritius-digital-transformation-2025-2029-a-bridge-to-the-future

MITCI's GOC page is direct Grade A evidence of a state data centre, 80-rack capacity, government cloud, hosting, and server co-location. The 2025-2029 Blueprint/RFI route is a Grade A pipeline source for a future Government Data Centre, sovereign cloud platform, and disaster-recovery site, but not yet a site-specific facility.

Government queries:
```text
site:mitci.govmu.org/mitci "Government Online Centre" "data centre"
site:mitci.govmu.org/mitci "Government Data Centre" OR "sovereign cloud"
site:publicprocurement.govmu.org "MITCI/RFI/01/2025-26" OR "Sovereign Cloud"
site:cib.govmu.org "data centre" OR hosting OR "disaster recovery"
site:ncb.govmu.org "data centre" OR "server hosting"
site:edbmauritius.org "data centre" OR "digital transformation" OR "ICT"
```

### 1.5 Energy, utilities, and environment

Primary URLs:
- Central Electricity Board: https://ceb.mu/
- CEB Fibernet: use CEB/ICTA records as entity pivots.
- Utilities Regulatory Authority: https://uramauritius.mu/
- Ministry of Energy and Public Utilities / EEMO: https://publicutilities.govmu.org/SitePages/Index.aspx
- Ministry of Environment: https://environment.govmu.org/

Use utility and environment records as corroboration for load, substations, transformers, standby generators, fuel storage, cooling, EIA/IEE conditions, or renewable supply. Do not create a DC record from power infrastructure alone. Emtel's operator page is currently the strongest primary power-detail source found: dual 1 MW transformers and N+1 generators.

Energy queries:
```text
site:ceb.mu "data centre" OR "data center" OR "disaster recovery" OR substation OR MVA OR kVA
site:uramauritius.mu "data centre" OR electricity licence OR tariff
"Mauritius" "data centre" EIA OR "environmental impact" generator OR substation
"CEB Fibernet" "data centre" OR "disaster recovery"
```

### 1.6 Submarine cable and IXP chain

| Asset | Best verified source route | Mauritius signal | Handling |
|---|---|---|---|
| SAFE | Submarine Networks / MT / DCD T4 context | Legacy MT cable; T4 planned to replace SAFE around end-of-life | Connectivity only. |
| LION/LION2 | Emtel and cable databases | Emtel claims direct DC access to LION/LION2 | Connectivity only unless linked to facility service. |
| MARS | TeleGeography Submarine Cable Map | Baie Jacotet/La Prairie area to Grand Baie, Rodrigues | Connectivity; Rodrigues lead, not DC. |
| T3 | Submarine Networks article | Landed at **Baie Jacotet** on 2023-03-24 | Savanne connectivity site only. |
| METISS | Emtel/EIN/Telecom Review/Submarine Networks | Emtel provided landing point at Arsenal data centre; 3,200 km system | DC-linked cable evidence for Emtel only. |
| T4 | DCD / Bloomberg-derived reporting | MT planned Africa-India-Singapore cable replacing SAFE | Pipeline; monitor landing site. |
| MIXP | https://www.mixp.org/ and PeeringDB IX 1508 | Mauritius Internet Exchange; Rogers page says MIXP hosted in Ebene DC; GOC node appears in PeeringDB | IXP, not DC; use as evidence for host facility/node. |

Cable queries:
```text
"Baie Jacotet" Mauritius T3 OR SAFE OR MARS "landing"
"METISS" Emtel "data centre" Arsenal Mauritius
"MARS" Mauritius Rodrigues "Grand Baie"
"Mauritius Telecom" T4 SAFE "2027"
"MIXP" Mauritius Ebene "Government Online Centre"
```

### 1.7 Hyperscaler absence checks

Official pages to recheck every refresh:
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- OCI: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Decision rule: reseller, partner, CDN, local zone, edge, VPS, or marketplace pages are not hyperscaler-region proof. Record "no official Mauritius region found" only after checking the official provider pages on the run date.

---

## 2. Per-Division Official Strategy

Run this workflow for **each** division, even if expected yield is none:
```text
"{division}" Mauritius "data centre" OR "data center" OR datacentre OR "server room"
"{division}" Mauritius telecom OR "landing station" OR "network operations" OR colocation
"{division}" Mauritius generator OR UPS OR substation OR cooling OR "backup power"
site:la.govmu.org "{division}" OR "{locality}" server OR data OR telecom
site:gpd.govmu.org "{division}" "data centre" OR telecom OR generator OR substation
site:ceb.mu "{division}" OR "{locality}" "data centre" OR substation
"{locality}" "centre de donnees" OR "salle de serveurs" OR hebergement
```

| Division | Official-first route | Current expected handling |
|---|---|---|
| Agalega Islands | Outer-islands government, MITCI/ICTA coverage, airport/jetty procurement | No public DC evidence found; mark none unless government/telecom room record appears. |
| Black River | Black River District Council BLUP, Cap Tamarin/Tamarin/Flic en Flac, EDB smart-city, CEB | No confirmed DC; keep smart-city/office developments as generic leads only. |
| Cargados Carajos Shoals | Outer-islands/Gazette, St Brandon references, telecom coverage | No public DC evidence found; do not infer from lodge/EEZ/marine facilities. |
| Flacq | Flacq District Council BLUP, Centre de Flacq, Deep River Beau Champ energy/solar context | No confirmed DC; search power/telecom/server-room records only. |
| Grand Port | Grand Port District Council BLUP, Rose-Belle/Gros Billot, airport/Plaine Magnien/Mon Tresor | **MT Rose Belle/RBDC** operational and Uptime Tier IV constructed/design certified; monitor government-data hosting and any expansion. |
| Moka | Moka District Council BLUP, Ebene Cybercity, Reduit, Telfair/Moka Smart City, MITCI/CEB offices | **Bhumishq Cybercity** Uptime Tier IV design; **Rogers Ebene DC/MIXP**; verify parcels around Cyber Tower 1, Mindspace, Wall Street. |
| Pamplemousses | Pamplemousses District Council BLUP, Arsenal, Terre Rouge/Riche Terre/JinFei, Baie du Tombeau | **Emtel Arsenal DC** TIA Rated 3; **Aphelion DC3** directory-only lead; METISS linked to Emtel; LION/Baie du Tombeau connectivity only. |
| Port Louis | Municipal council, MITCI/GOC, Rogers/Harel Mallac downtown addresses, Gazette, procurement | **GOC** Grade A; **Rogers Port Louis/Les Cascades** and **Harel Mallac/MCS** need primary/planning confirmation; MIXP GOC node is IXP evidence. |
| Plaines Wilhems | Municipal councils for Beau Bassin-Rose Hill, Curepipe, Quatre Bornes, Vacoas-Phoenix; Candos/Rose Hill | **MT Rose Hill Tier III/RHDC** lead from MT page; **BIRGER Candos** directory-led; search legacy exchanges and DR rooms. |
| Rodrigues Island | Rodrigues Regional Assembly, Port Mathurin, Grand Baie landing, MT/Emtel | MARS landing at Grand Baie is connectivity only; no public DC evidence found. |
| Riviere du Rempart | District Council, Grand Baie/La Croisette, tourism/business towers, ICTA coverage | No confirmed DC; low-yield sweep. |
| Savanne | Savanne District Council, Baie Jacotet/Bel Ombre, CEB/MT landing records | SAFE/MARS/T3 landing cluster at Baie Jacotet is connectivity only; no DC without server/colo evidence. |

---

## 3. Seed Records for Enumerators

| Seed | Division | Status | Capacity | Grade | Best evidence |
|---|---|---|---|---|---|
| Emtel Data Centre | Pamplemousses | Operational | dual 1 MW transformers claimed; IT load null unless schema records claim | A cert/address/operator | EPI map; TIA Online; Emtel business data-centre page; METISS press |
| MT Rose Belle Data Centre / RBDC | Grand Port | Operational | 1,500 sq m, 400+ racks, 3 MW on MT/my.t/RBDC pages | A | myt.mu colocation; rbdc.mu; Uptime Institute country/Rose Belle record |
| MT Rose Hill Tier III / RHDC | Plaines Wilhems | Operational/lead | null | A for MT claim; C for directory details | myt.mu ICT/BPO; DatacenterPlanet seed |
| Bhumishq Cybercity Data Centre | Moka | Operational/verify | null; 500 sq m directory claim | A for Uptime design cert; C for address/capacity | Uptime country page; DataCenterMap |
| Rogers Capital Ebene DC / MIXP host | Moka | Operational | null | A/B | Rogers primary page; MIXP; PeeringDB; ICTA |
| Rogers Capital La Tour Koenig DC | Port Louis market / verify boundary | Operational | null | A/C | Rogers primary says La Tour Koenig DC; DataCenterMap address |
| Rogers Capital Port Louis DC | Port Louis | Operational/verify | null | C plus A licence | DataCenterMap; ICTA; Rogers pivot |
| Rogers Capital Les Cascades DC | Port Louis | Operational/verify | null | C plus A licence | DataCenterMap; Rogers pivot |
| Harel Mallac / MCS Datacenter 02 | Port Louis | Operational/verify | null | B/C | DataCenterMap; Telecom Review Africa; Harel Mallac pivot |
| BIRGER Candos Recovery Centre | Plaines Wilhems | Operational/verify | null | C/B | DataCenterMap/ColocationM; BIRGER company site |
| Aphelion DC3 | Pamplemousses | Operational/verify | null | C | DataCenterMap/UPSTACK; JinFei/Riche Terre status press |
| Government Online Centre | Port Louis | Operational state DC | 80 racks on MITCI page | A | MITCI GOC page; PeeringDB/MIXP |
| New Government Data Centre + sovereign cloud + DR site | TBD | Planned/procurement | null | A policy/procurement; C location | MITCI Blueprint; Public Procurement RFI |
| CEB DR centre | TBD | Lead | null | B lead | CEB/public procurement searches |
| MIXP | Moka + Port Louis node | Operational IXP | n/a | A | MIXP; PeeringDB |

---

## 4. Decision Rules and Pitfalls

- **Correct the old draft caveat:** Uptime Institute **does** list Mauritius entries: MT Rose Belle has Tier IV Design Documents and Constructed Facility; Bhumishq Cybercity has Tier IV Design Documents. The absence caveat from the draft is obsolete.
- **Certification type matters.** Design certification is not the same as constructed certification. Emtel TIA/EPI is ANSI/TIA-942-B Facility Rated 3; MT Rose Belle is Uptime Tier IV design + constructed; Bhumishq is Uptime Tier IV design only in the current evidence.
- **District assignment must follow physical location.** Ebene/Reduit = **Moka**; Arsenal/Terre Rouge = **Pamplemousses**; Rose-Belle = **Grand Port**; Rose Hill/Candos/Quatre Bornes = **Plaines Wilhems**; Baie Jacotet = **Savanne**.
- **Cable landings are not DCs.** Baie Jacotet, Baie du Tombeau, Grand Baie Rodrigues, and Terre Rouge shore points remain connectivity records unless facility evidence exists. METISS has explicit Emtel DC linkage.
- **Licence lists are pivots, not facility registers.** ICTA proves telecom authorisation, not the presence of a datacentre.
- **Keep unknown capacity null.** Do not derive MW from tier, rack count, cable capacity, transformer size, or market forecasts. Store claimed values only with source and grade.
- **No deletion of leads during enumeration.** If a lead cannot be verified, retain it as a downgraded lead with the missing evidence named.
