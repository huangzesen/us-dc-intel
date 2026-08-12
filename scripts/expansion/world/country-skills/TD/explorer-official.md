# TD Explorer Official - Chad Datacenter Enumeration via PMICE, ARCEP, ADETIC, ANSICE, Power, Donors, and Cloud

Date: 2026-08-12. Country: **TD Chad**. Division model: **23 provinces**. Scope: official/regulatory/primary-source methodology for enumerating Chad data-center, telco-core, IXP, government-cloud, and public-sector micro-data-center facilities.

Reliability grades:
- **A** = primary source: ministry/agency statement, ARCEP/ADETIC/ANSICE/ARSE page, official operator page, signed decree/contract, donor project document, procurement notice, official cloud-region page, Uptime Institute certificate.
- **B** = strong secondary source: reputable trade/local press with named project, location, owner, component, date, or official statement quotation (Agence Ecofin, Digital Business Africa, Data Center Dynamics, Developing Telecoms, TechAfricaNews, WeAreTech.Africa, Alwihda Info, RFI, TchadInfos).
- **C** = weak lead: directories, generic vendor SEO pages, social posts, market-report snippets, unsourced "cloud in Chad" claims, hosting pages that do not disclose the physical facility.

---

## 0. Chad-specific structure facts

- Chad has **no national public data-center registry**. Enumeration is a joined-source exercise across PMICE project communications, ARCEP telecom licensing/market pages, ADETIC/ANSICE data-governance and certification pages, ARSE/utility power records, donor project files, telco/operator pages, and cloud-region lists.
- The market is **N'Djamena-led and state-led**. Outside the capital, expect PMICE fiber/transmission sites, public-institution micro data centers, ADETIC telecentres, and telco technical rooms rather than commercial colocation.
- Do **not** describe Chad as having no data centers. Verified leads include: a **2016 Tigo/Millicom modular communications/colocation data center** in N'Djamena (now in the Moov Africa Chad lineage after Tigo Chad was sold to Maroc Telecom), and the newer **PMICE National Data Center** in N'Djamena. What Chad lacks is a known hyperscaler region, international carrier-neutral colocation campus, or broad public colo market.
- PMICE is the main official anchor: the 2020 launch described a national data center, 1,200 km national fiber route plus 50 km GPON in N'Djamena, and 200 SOTEL 2G/3G/4G sites. Later 2026 reporting and ADETIC pages show the national DC building and equipment installed, with audit/certification and micro-DC interconnection still required before full official exploitation.
- Source language is overwhelmingly **French**. Search: `centre de donnees`, `data center`, `datacenter`, `salle serveurs`, `salle informatique`, `hebergement`, `colocation`, `micro data center`, `souverainete numerique`, `reception provisoire`, `mise en exploitation`, `certification`.
- Chad is landlocked. Serious facility claims should be checked against fiber backhaul through Cameroon/Nigeria corridors and power evidence. ARSE states electricity access remains very low, and TchadElec replaced SNE as the national public electricity company in July 2025; grid, generator, and solar/captive-power evidence are important validation signals.

---

## 1. Official/regulatory portals

### 1.1 PMICE and the telecom ministry

Primary/near-primary sources:
- Ministry site: `https://www.mpntic.gouv.td/` (availability varies; also check ministry social pages when the site is stale).
- Government/Primature: `https://www.primature.td/`.
- Presidency: `https://www.presidence-tchad.org/` and official social channels.
- PMICE launch coverage mirrored from Agence Ecofin: `https://www.capital-media.mu/2020/07/le-tchad-lance-la-modernisation-de-ses-infrastructures-de-communications-electroniques/`.
- DCD PMICE Phase I report: `https://www.datacenterdynamics.com/en/news/chad-invests-175m-in-national-data-center-and-networks/`.
- Digital Business Africa May 2026 PMICE verification report: `https://www.digitalbusiness.africa/pmice-le-tchad-accelere-les-verifications-autour-du-data-center-et-des-infrastructures-numeriques/`.

Verified PMICE components to extract:
- **National Data Center** - N'Djamena. 2020 launch plan: national data-center component on a planned 2,000 m2 site/building with three storeys. 2026 sources: physical building completed, digital equipment installed, audit/certification and final technical adjustments pending before full official operation. Huawei is the delivery contractor; Gulf/GOLF Consultancy is the control/supervision office in later reports.
- **National fiber** - 1,200 km route in the 2020 plan: Doba-Koumra-Sarh-Kyabe-Am Timan-Abeche-Am Zoer-Guereda-Iriba, plus 50 km GPON access in N'Djamena. DCD/press later summarize Phase I as 1,200 km fiber.
- **SOTEL modernization** - 200 2G/3G/4G sites, a core network, and subscriber-capacity expansion from 300,000 to 1,000,000 in the 2020 plan.
- **Micro data centers** - WeAreTech and Digital Business Africa report government-institution micro data centers: 100 micro DCs under the ANSICE/ADETIC/TECHSO certification initiative, with installed micro DCs awaiting final configuration/interconnection to the main DC.
- **200 transmission sites** - Digital Business Africa reports planned inspection/reception missions for the PMICE transmission sites.

PMICE query templates:

```text
site:mpntic.gouv.td PMICE "Data Center"
site:mpntic.gouv.td "centre de données" Tchad
site:primature.td PMICE "réception" OR "inauguration"
"PMICE" "Data Center national" "Huawei" "Tchad"
"PMICE" "Gulf Consultancy" OR "GOLF Consulting" "Tchad"
"Bobe Poka" PMICE "Data Center"
"réception provisoire" PMICE Tchad Sarh
"micro data centers" ADETIC ANSICE TECHSO Tchad
```

Grading: ministry/government/ADETIC/ANSICE releases are **A**; DCD/Digital Business Africa/Agence Ecofin are **B** unless the item is a directly linked or quoted official statement.

### 1.2 ARCEP Tchad - telecom regulator

Primary sources:
- ARCEP home: `https://www.arcep.td/`.
- ISP list: `https://arcep.td/fournisseurs_acces_internet.html`.
- Market observatory: `https://arcep.td/observatoire/` and `https://arcep.td/rapports.html`.
- Licence/application pages: `https://www.arcep.td/licence_exploitation.html`, `https://www.arcep.td/demandes.html`, `https://www.arcep.td/avis.html`.

Use ARCEP as the **operator universe** and market-evidence source. The ISP page lists authorized ISPs such as Albidey Net, Focon-Net, Global Technologies, IlNet, MICT Group, Miracle Telecom, Prestabist, Reindos Technologies, Tchad Broadband, Chad Technologies, T-Rex Net, Manano Telecom, ETS 3 Telecom, Ifotel, Chagra Telecom, Infotel-N'Djamena, Internet Solution for Africa, and Amanet. These are candidate N'Djamena server-room/hosting leads, not facility records by themselves.

ARCEP query templates:

```text
site:arcep.td "data center" OR "centre de données"
site:arcep.td "fournisseurs d'accès internet" "{operator}"
site:arcep.td "QoS" OR "qualité de service" Airtel Moov Sotel
site:arcep.td "SOTEL" "coeur du réseau" OR "transmission"
site:arcep.td "TCHADIX" OR "point d'échange"
```

### 1.3 ADETIC, .td registry, and TCHADIX

Primary sources:
- ADETIC: `https://adetic.td/`.
- Data Center category: `https://adetic.td/category/data-center/`.
- ADETIC audit/certification article: `https://adetic.td/audit-et-certification-du-data-center-national-ladetic-lansice-et-techso-group-en-mission-conjointe/`.
- .td registry: `https://registry.nic.td/`.

Verified official signals:
- ADETIC has a Data Center category and, on 12 February 2026, described an ADETIC/ANSICE/TECHSO-GROUP mission for audit and certification of the National Data Center. The same ADETIC article says Huawei and PMICE teams guided the visit, the audit covers physical and logical security, and the mission is a prerequisite to official exploitation.
- The same article mentions inspection of an **ADETIC backup site**. Treat this as an **A-grade backup/DR lead** but not as a full separate DC until location, capacity, and role are published.
- TCHADIX is the national Internet exchange point, formed as a G.I.E. under ADETIC's impulse. Alwihda reports its ordinary general assembly on 20 May 2026, nearly one year after creation, with the mission of local traffic exchange among ISPs/operators. Physical hosting location remains an open item.

ADETIC/TCHADIX queries:

```text
site:adetic.td "Data Center national"
site:adetic.td "site de backup"
site:adetic.td TECHSO ANSICE certification
site:adetic.td TCHADIX OR "point d'échange"
"TCHADIX" "G.I.E" "ADETIC"
"TCHADIX" N'Djamena "PeeringDB" OR "PCH"
```

### 1.4 ANSICE - cybersecurity and data protection

Primary source:
- ANSICE: `https://ansice.td/`.

ANSICE is the national cybersecurity, electronic-certification, and personal-data-protection authority. It is high-value for:
- National DC audit/certification and launch-readiness.
- State-data localization and protection statements.
- Cyber incident and resilience statements that name hosted systems or critical infrastructure.

Queries:

```text
site:ansice.td "Data Center" OR "centre de données"
site:ansice.td ADETIC TECHSO
"ANSICE" "Data Center national" "N'Djamena"
"ANSICE" "protection des données" "Data Center"
```

### 1.5 Power and environmental/power-adjacent evidence

Primary sources:
- ARSE: `https://arse.td/`.
- ARSE operator page: `https://arse.td/operateur-historique/`.
- ARSE licences/authorizations: `https://arse.td/licences-et-autorisations/`.

Verified power context:
- ARSE describes TchadElec as instituted in July 2025 to replace SNE as the public national electricity company.
- ARSE states national electricity access is extremely low, with rural access around 1-2%, and highlights mini-grid/solar programs. This makes power/captive-generation evidence central to facility validation.

Power queries:

```text
site:arse.td "data center" OR "centre de données"
site:arse.td "licence de production" "N'Djamena"
"Data Center national" Tchad "groupe électrogène" OR solaire OR "TchadElec"
"TCHADIX" "électricité" OR "groupe électrogène"
"SOTEL" "coeur du réseau" "énergie" OR "générateur"
```

### 1.6 Donor and procurement sources

Primary sources:
- World Bank Chad Digital Transformation Project P180000: `https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099090624105035738`.
- World Bank press release, 25 September 2024: `https://www.worldbank.org/en/news/press-release/2024/09/25/world-bank-increases-access-to-broadband-connectivity-in-chad`.
- World Bank ISR text: `https://documents1.worldbank.org/curated/en/099082425101022763/txt/P180000-aa0cb654-fd15-49e7-8296-f0b965e2e523.txt`.

PATN / Chad Digital Transformation Project is a demand-side and connectivity program, not yet a verified data-center construction record. It is **A** for project scope and procurement when using World Bank documents. Search procurement plans for government-cloud, digital-public-service platforms, cybersecurity, CERT, PKI, hosting, disaster recovery, and broadband infrastructure.

Queries:

```text
site:documents.worldbank.org Chad "Digital Transformation Project" "data center"
site:documents1.worldbank.org P180000 "data center" OR "cloud" OR "disaster recovery"
"P180000" Chad "procurement plan" "server" OR "hosting"
"PATN" Tchad "data center" OR "hébergement" OR "cloud"
```

### 1.7 Cloud-region official checks

Cloud-provider pages are **A** for region presence/absence. As of the checked official pages, there is **no Chad region or local zone** on AWS, Azure, Google Cloud, or Oracle OCI.

| Provider | Official source | Chad signal |
|---|---|---|
| AWS | `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html` | No Chad region; Africa listed as Cape Town (`af-south-1`). |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list` | No Chad region in public Azure regions list. |
| Google Cloud | `https://cloud.google.com/about/locations` | No Chad region. |
| Oracle OCI | `https://www.oracle.com/cloud/public-cloud-regions/` | No Chad public cloud region. |

Treat "AWS/Azure/GCP in Chad" claims as partner/customer/service-availability leads, not physical data-center records, unless the official region/local-zone page changes.

---

## 2. Official seed inventory

| Facility / project | Location | Status to use | Grade | Verification route |
|---|---|---|---|---|
| PMICE National Data Center | N'Djamena | Building and digital equipment installed; audit/certification and final technical adjustments pending before official exploitation in 2026 sources | A for ADETIC audit/certification existence; B for trade-press construction details | ADETIC, ANSICE, ministry/PMICE, Digital Business Africa, DCD |
| ADETIC backup site | Not yet public | Backup/DR lead inspected during TECHSO/ADETIC/ANSICE mission; capacity/location unknown | A lead, not a separate full DC until details published | ADETIC audit article |
| PMICE micro data centers | Government institutions, locations not fully published | Installed or planned micro DC estate; final configuration/interconnection pending | A/B depending on ADETIC/ANSICE vs press | ADETIC/ANSICE, WeAreTech, Digital Business Africa |
| PMICE 200 transmission sites | National route/provinces | Telecom transmission sites awaiting inspection/reception missions | B until official site list is published | PMICE/ministry, Digital Business Africa |
| SOTEL/Salam core modernization | N'Djamena plus national network | Telco core/network upgrade under PMICE; not commercial colo | A for program/operator role, B for technical detail | Ministry, ARCEP, SOTEL, PMICE launch |
| TCHADIX | N'Djamena likely, physical host not published | National IXP/G.I.E.; physical equipment host to identify | B until ADETIC/TCHADIX page or PeeringDB/PCH facility record | ADETIC, Alwihda, PeeringDB/PCH |
| 2016 Tigo/Millicom modular DC | N'Djamena | Communications/colocation data center, 374 m2, 400 kW IT load, built by Flexenclosure; now follow Moov Africa Chad lineage | B, A only if Moov/Maroc Telecom confirms current facility | DCD 2016, Millicom/Maroc Telecom transaction pages, ARCEP |

---

## 3. Province-by-province official enumeration

Run every province through official first, then press. Chad has 23 provinces under the 2024 administrative structure; use current province names and capitals.

Universal province query block:

```text
"{province}" Tchad ("PMICE" OR "fibre optique" OR "Data Center" OR "centre de données" OR "site technique")
"{capital}" Tchad ("PMICE" OR "fibre optique" OR "micro Data Center" OR "salle serveur")
site:mpntic.gouv.td "{capital}" OR "{province}"
site:adetic.td "{capital}" OR "{province}"
site:arcep.td "{capital}" OR "{province}"
site:arse.td "{capital}" OR "{province}"
```

| Province | Capital / main locality | Official enumeration focus |
|---|---|---|
| N'Djamena | N'Djamena | National DC, ADETIC backup site, TCHADIX host, Moov/Tigo 2016 DC, SOTEL/Airtel/Moov cores, ISPs, ministry/regulator facilities. |
| Barh El Gazel | Moussoro | PMICE transmission/fiber sites; ARCEP QoS/site failures; telecentre/agency ICT rooms. |
| Batha | Ati | PMICE pass-through/technical sites; ARCEP and ADETIC provincial mentions. |
| Borkou | Faya-Largeau | Low-probability sweep; satellite/telecom rooms only unless PMICE site list names it. |
| Chari-Baguirmi | Massenya | Capital-adjacent technical sites, fiber/power routes, possible government DR/support rooms. |
| Ennedi Est | Amdjarass | ADETIC telecentre precedent; possible provincial public ICT/server room; do not count as DC without evidence. |
| Ennedi Ouest | Fada | Low-probability sweep; telecom/power site evidence only. |
| Guera | Mongo | ADETIC telecentre precedent; PMICE route/technical-site sweep. |
| Hadjer-Lamis | Massakory | Capital-adjacent telecom/power sites; ARCEP and PMICE transmission sweeps. |
| Kanem | Mao | Low-probability sweep; fiber/telecom sites. |
| Lac | Bol | Telecom/satellite/fiber resilience leads; no commercial DC expected. |
| Logone Occidental | Moundou | Second-city telco and ISP technical rooms; PMICE/fiber endpoint queries. |
| Logone Oriental | Doba | PMICE route explicitly includes Doba; oil-region telecom/power rooms; no colo unless named. |
| Mandoul | Koumra | PMICE route explicitly includes Koumra; transmission/fiber and micro-DC sweeps. |
| Mayo-Kebbi Est | Bongor | ADETIC telecentre precedent; Cameroon/N'Djamena route checks. |
| Mayo-Kebbi Ouest | Pala | Low-probability sweep; telecom/power and institutional server rooms. |
| Moyen-Chari | Sarh | High-priority PMICE Phase I/inauguration/reception ceremony searches; route endpoint and technical-site evidence. |
| Ouaddai | Abeche | PMICE route explicitly includes Abeche; eastern corridor technical sites; ADETIC/public ICT rooms. |
| Salamat | Am Timan | PMICE route explicitly includes Am Timan; transmission/fiber site searches. |
| Sila | Goz Beida | Low-probability sweep; telecom/satellite/public-institution rooms. |
| Tandjile | Lai | Low-probability sweep; provincial telecom/power sites. |
| Tibesti | Bardai | Very low probability; satellite/telecom support sites only. |
| Wadi Fira | Biltine | ADETIC telecentre precedent; PMICE route includes Am Zoer/Guereda/Iriba; eastern corridor sweeps. |

---

## 4. Extraction and grading checklist

For each lead, extract:
- Facility/project name and aliases.
- Owner/operator/agency and program: PMICE, ADETIC, ANSICE, SOTEL, Moov/Tigo, Airtel, PATN, donor project.
- Type: national DC, backup/DR site, micro DC, IXP, telco core, commercial hosting/colo, institutional server room, transmission site.
- Province, city, arrondissement/address if published.
- Stage: planned, under construction, building complete, equipment installed, audit/certification, reception provisoire, inaugurated, operational, decommissioned.
- Physical metrics: m2, floors, racks, kW/MW IT load, redundancy/Tier/certification.
- Power: TchadElec/SNE grid, generators, solar/captive power, substation, fuel storage.
- Connectivity: national fiber route, SOTEL/Camtel/Cameroon link, IXP, operators, international transit.
- Contractor/supervisor/financier: Huawei, Gulf/GOLF Consultancy, TECHSO-GROUP, Flexenclosure, China/Eximbank, World Bank/IDA.
- Source URL, publication date, source type, and reliability grade.

Grade conservatively:
- ADETIC says "audit before official exploitation" means **not operational** until an A-grade launch/commissioning source appears.
- A hosting service page is **not** a physical data center unless it names an in-country site.
- A telco core can be counted as network infrastructure, but not as commercial colocation unless the operator markets colo/hosting from that facility.
- Aggregator-only records stay **C** until joined to an operator/regulator/official page.
