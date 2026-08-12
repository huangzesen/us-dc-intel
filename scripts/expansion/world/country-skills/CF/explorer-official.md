# CF Explorer Official - Central African Republic Datacenter Enumeration via ARCEP, Ministry, SOCATEL, CAB, Donors, Energy, and Official Cloud Sources

Date: 2026-08-12. Country: **CF Central African Republic (RCA / Centrafrique)**. Division model: **17 divisions per world-manifest.jsonl**: Ouham, Bamingui-Bangoran, Bangui, Basse-Kotto, Haute-Kotto, Haut-Mbomou, Haute-Sangha / Mambere-Kadei, Gribingui, Kemo-Gribingui, Lobaye, Mbomou, Ombella-Mpoko, Nana-Mambere, Ouham-Pende, Sangha, Ouaka, Vakaga. Angle: official / regulatory / donor / public-project discovery for operational, planned, and institutional data-centre evidence.

This methodology was upgraded from draft to final quality with web verification on 2026-08-12. It is a country research guide, not a facility record.

Reliability grades:
- **A** = primary / official evidence for the exact fact: gouv.cf or ministry page, ARCEP official page/decision, IANA .cf delegation record, AfDB MapAfrica/project record, World Bank project document/blog, official operator or vendor announcement, Uptime Institute certification record, official hyperscaler region list.
- **B** = strong secondary evidence: Agence Ecofin / Ecofin Agency, We Are Tech, RFI, Radio Ndeke Luka, RJDH, Oubangui Medias, Digital Business Africa, Data Center Dynamics, Developing Telecoms, Telecompaper, Ecomatin, ETC/WFP, reputable local press or trade press with named actors and dates.
- **C** = weak lead only: datacenters.com, DataCenterMap, Cloudscene, PeeringDB, market reports, social posts, inaccessible snippets, tender aggregators without original buyer documents, local commentary without a named site.
- **U** = searched negative / unverified absence. Use only for no_projects rows after recording the search pattern.

---

## 0. CF-specific structural facts

- **Administrative coverage is a manifest constraint, not the current legal map.** Current CAR administration is reported as 20 prefectures plus Bangui after the 2020/2021 reform, but this project uses the 17 legacy/hybrid divisions in `world-manifest.jsonl`. Normalize records to the manifest division and keep the exact locality/prefecture named by the source in notes.
- **Manifest-to-current normalization:** `Haute-Sangha / Mambere-Kadei` = current Mambere-Kadei / Berberati corridor; `Sangha` = Sangha-Mbaere; `Kemo-Gribingui` = Kemo/Nana-Grebizi legacy area depending on locality; `Gribingui` = Nana-Grebizi/Gribingui area. Do not create new manifest divisions such as Mambere, Lim-Pende, Ouham-Fafa, Nana-Grebizi, or Kemo unless the manifest is updated.
- **Bangui dominates the facility search.** Confirmed and candidate data-centre or server-room evidence is in Bangui or location-unspecified national projects that should default to Bangui only when the source context supports it. Outside Bangui, expect fibre, power, administrative, or telecom-node context rather than data-centre facilities.
- **There are public data-centre project leads, but few proven operational facilities.** The strongest official lead is the AfDB/CAB-CAR component, whose MapAfrica text describes a Bangui urban loop including a national datacentre and Digital Training Centre. Other leads include GreenLine/SOCATEL Tier 3, Huawei/government Tier III, Cybastion government data centers, ECCAS/PIDA regional data-center plan, Orange Centrafrique's Bangui core/data-centre facility, and ARCEP's 80 TB monitoring platform.
- **Separate data centres from institutional compute.** ARCEP's 80 TB network-monitoring platform, SOCATEL .cf registry infrastructure, ministry server rooms, bank server rooms, and mobile operator core sites prove local compute, but they are not commercial colocation or national data-centre projects unless the source explicitly says `data center`, `datacenter`, or `centre de donnees`.
- **Connectivity is improving via fibre and satellite.** The government portal lists the CAB-CAR fibre backbone project as a major project co-financed by AfDB and the EU; Starlink commercial service launched in March 2026 after December 2025 approval. Connectivity services are not facility records.
- **Power is a gating constraint.** Bangui/Ombella-Mpoko power depends heavily on Boali hydro and diesel backup. Any MW-scale data-centre claim without gensets, UPS, grid interconnect, solar, or substation evidence should keep `capacity_mw=null` and a power caveat.
- **No hyperscaler cloud region in CAR.** AWS, Azure, Google Cloud, and OCI official region lists should be checked as A-grade absence evidence; do not convert an edge node, partner cloud, Outposts/Local Zone-style deployment, or satellite service into a CAR cloud region.

Core French and English vocabulary:

```text
centre de donnees
centre national de donnees
datacenter
data center
data centre
centre de calcul
salle serveur
salle informatique
salle blanche
hebergement / hebergement web
cloud / cloud souverain
infrastructure numerique
numerisation / digitalisation
identite numerique / e-gouvernance
fibre optique / dorsale a fibre optique
colocation / co-location
onduleur / UPS
groupe electrogene
poste electrique / transformateur
Boali / ENERCA
permis de construire
appel d'offres / marche public
agrement / licence
```

---

## 1. Primary official routes

### 1.1 ARCEP - regulator and licence trail

Primary source: **Autorite de Regulation des Communications Electroniques et de la Poste (ARCEP RCA)**, https://arcep.cf/.

Verified status on 2026-08-12: the official ARCEP portal is online but still a construction placeholder. It says the new institutional portal is being finalized and lists contact `contact@arcep.cf`, B.P. 1046 Bangui, tel. +236 21 61 56 51. Therefore, absence of online ARCEP decisions is **not** proof of absence.

Use ARCEP for:
- telecom/operator licences and `agrement` evidence;
- any authorization for Starlink, satellite services, cloud/hosting, data-hosting, or telecom equipment;
- operator market statistics and enforcement actions;
- official interviews by ARCEP leadership.

Important official/primary anchor:
- World Bank blog, 28 Oct 2025: under PGNSP, a new monitoring equipment suite was launched at ARCEP headquarters in Bangui in April 2024. The platform collects mobile-network data and has **80 TB of storage**. Treat as **A for institutional compute at ARCEP HQ** and **not a data-centre facility** unless another source uses data-centre language.

ARCEP query templates:

```text
site:arcep.cf agrement operateur
site:arcep.cf "centre de donnees" OR datacenter OR cloud
site:arcep.cf "liste des operateurs" OR licence
"ARCEP RCA" agrement operateur Centrafrique
"ARCEP" "Centrafrique" "Starlink" licence OR autorisation
"ARCEP" "Centrafrique" "centre de donnees" OR datacenter OR cloud
"ARCEP" "Bangui" "80 terabytes" OR "80 TB" OR stockage
"Benjamin Panze Sebasse" ARCEP Centrafrique
```

Extract: legal entity, licence/agrement class, decision date, address, services authorized, and any physical infrastructure. Grade A only for facts visible in ARCEP or another primary record.

### 1.2 Ministry / government portal

Primary routes:
- Government portal: https://www.gouv.cf/
- Telecom ministry link from government portal: `www.telecommunications.gouv.cf` (may be intermittent / unsafe to open directly in some tools)
- Related ministry domains: `modernisation.gouv.cf`, `finances.gouv.cf`, `plan.gouv.cf`, `energies.gouv.cf`

Verified official facts:
- gouv.cf lists **Projet Dorsale-Fibre Optique d'Afrique Centrale - Composante RCA** under `Les grands projets en cours d'execution` / major dossiers.
- The government CAB page says CAB-CAR is co-financed by AfDB and the EU and aims to reduce digital isolation through fibre access to Cameroon and Congo.
- The government composition page lists the Ministry of Posts and Telecommunications link; historic pages list Justin Gourna-Zacko, while 2026 press reports name Roger Andjalandji for the GreenLine/SOCATEL phase. Always date minister names.

Ministry query templates:

```text
site:gouv.cf "Projet Dorsale-Fibre Optique" "Composante RCA"
site:gouv.cf "centre de donnees" OR datacenter OR "centre national de donnees"
site:telecommunications.gouv.cf "centre de donnees" OR datacenter OR cloud
site:modernisation.gouv.cf "centre de donnees" OR "e-gouvernance"
site:finances.gouv.cf "datacenter" OR "centre de donnees" OR "Cybastion"
"Roger Andjalandji" "centre de donnees" OR datacenter OR SOCATEL
"Justin Gourna-Zacko" "Starlink" OR "identite numerique" OR datacenter
"RCA" "cloud souverain" "centre de donnees"
"PND 2024-2028" Centrafrique numerique datacenter
```

Grade A when the government/ministry names the project, site, stage, or financing. Keep `capacity_mw=null` unless MW/kVA/IT load is disclosed for the exact facility.

### 1.3 AfDB / CAB-CAR - national datacentre lead

Primary source: **AfDB MapAfrica project 46002-P-CF-GB0-002, Central Africa Fibre-Optic Backbone Project (CAB) - CAR Component**, plus the government CAB page.

Verified facts:
- AfDB MapAfrica search result text for the CAR component states the project includes a **local urban loop comprising a national datacentre (Datacentre) and a Digital Training Centre in Bangui**, tied to Bangui University / vocational-training context.
- gouv.cf independently confirms CAB-CAR as a government major dossier co-financed by AfDB and the EU, with fibre access to Cameroon and Congo.

Handling:
- This is the strongest official route for a **Bangui national datacentre / Digital Training Centre** record.
- Stage must be checked before final enumeration. If only MapAfrica/project design text is available, use `planned` or `construction` according to the latest project-status source; do not call it operational without commissioning evidence.
- Developer should be `Government of Central African Republic / African Development Bank / European Union` unless a construction contractor is found.
- `capacity_mw` remains null unless AfDB procurement/project docs publish electrical or IT-load data.

CAB / AfDB query templates:

```text
site:mapafrica.afdb.org "46002-P-CF-GB0-002"
site:afdb.org "P-CF-GB0-002" OR "Composante RCA" "datacentre"
site:gouv.cf "Projet Dorsale-Fibre Optique" "Composante RCA"
"CAB" "RCA" "datacentre" OR "centre de donnees"
"Dorsale-Fibre Optique" Centrafrique "centre de donnees"
"Universite de Bangui" "datacentre" OR "centre de donnees" OR "Digital Training Centre"
"Bangui University" "national data centre" "Central African Backbone"
```

### 1.4 SOCATEL / .cf registry / GreenLine

Primary source for SOCATEL entity: IANA .cf delegation record, https://www.iana.org/domains/root/db/cf.html.

Verified facts:
- IANA lists **Societe Centrafricaine de Telecommunications (SOCATEL)** as the .cf ccTLD manager at **Rue Guerillot, Bangui BP 939**; administrative contact is the Directeur General, with `dg-socatel@socatel.cf`.
- IANA also lists the technical contact as Centrafrique TLD B.V. in Amsterdam and .cf name servers in non-CAR address space. Therefore IANA is **A for SOCATEL identity/address/registry role**, but it does **not** prove a Bangui data centre.
- GreenLine Technologies official announcement dated 18 Sep 2025 says GreenLine received a mandate to privatize/revitalize/transform SOCATEL under an MoU signed in Casablanca and that the package includes a **new Tier 3 data center** and **USD 150M initial investment**.
- 2026 press reports from Agence Ecofin / Radio Ndeke Luka / Telecompaper / Developing Telecoms say the operational phase was launched in Bangui on 16 Jul 2026 with Minister Roger Andjalandji and GreenLine's Max/Massimiliano Sicari.

Handling:
- Grade **A for GreenLine's self-claimed mandate, Tier 3 plan, and USD 150M package** because it is an official vendor announcement.
- Grade **B for government-stage details** until a government/ministry/SOCATEL document is retrieved.
- Stage is **planned / early operationalization of partnership**, not built. No site address, racks, MW, certification, or construction permit has been found.
- Do not merge this with the AfDB/CAB national datacentre unless a source explicitly says they are the same asset.

SOCATEL query templates:

```text
site:socatel.cf datacenter OR "centre de donnees" OR cloud
site:gouv.cf SOCATEL GreenLine OR Greenline
"SOCATEL" "Greenline" "Tier 3" OR "Tier III" OR datacenter
"Greenline Technologies" "SOCATEL" "data center"
"Green Line" "SOCATEL" "150 millions" "centre de donnees"
"Societe Centrafricaine de Telecommunications" "Rue Guerillot" datacenter
site:iana.org/domains/root/db/cf.html SOCATEL
```

### 1.5 Public-sector digital governance / World Bank PGNSP

Primary route: World Bank project pages and documents for **P174620 Public Sector Digital Governance Project (PGNSP)** and related additional financing.

Verified facts:
- The World Bank approved a **USD 35M grant** for Public Sector Digital Governance in May 2022.
- The PGNSP-supported ARCEP monitoring platform launched at ARCEP HQ in Bangui in April 2024 with 80 TB of storage.
- Project documents should be searched for e-government hosting, disaster recovery, government cloud, identity, interoperability platform, and any data-centre component.

Handling:
- PGNSP is A-grade for institutional systems it finances.
- A server/storage platform is not automatically a data centre. Record as institutional compute unless the project document names a `data center`, `data centre`, or `centre de donnees`.

World Bank query templates:

```text
site:documents.worldbank.org "P174620" "Central African Republic" "data center"
site:documents.worldbank.org "P174620" "centre de donnees"
site:documents.worldbank.org "Central African Republic" "digital governance" "hosting"
site:documents.worldbank.org "Central African Republic" "disaster recovery" "government cloud"
"PGNSP" Centrafrique "centre de donnees" OR datacenter OR hebergement
"Public Sector Digital Governance Project" "Central African Republic" "data center"
```

### 1.6 Huawei / government administration modernization

Verified public lead:
- Digital Business Africa reported in May 2026 that Bangui is accelerating modernization of public administration with Huawei support and that the first component provides for a **Tier III national data centre**. This is **B** until corroborated by Huawei, gouv.cf, ministry, procurement, or financing documents.

Handling:
- Keep as a separate planned government lead unless official evidence says it is part of CAB, PGNSP, GreenLine/SOCATEL, or Cybastion.
- Search procurement and ministry pages before upgrading.

Query templates:

```text
site:gouv.cf Huawei "centre national de donnees" OR datacenter
site:telecommunications.gouv.cf Huawei datacenter OR "centre de donnees"
site:modernisation.gouv.cf Huawei "Tier III" OR datacenter
site:huawei.com Centrafrique "data center" OR "centre de donnees"
"Centrafrique" Huawei "Tier III" "centre national de donnees"
"Bangui" Huawei "modernisation numerique" datacenter
```

### 1.7 Cybastion public-sector data centers

Primary vendor source: Cybastion official news, 29 Apr 2021.

Verified facts:
- Cybastion says CAR's Finance/Budget, Economy/Planning/Cooperation, and Public Service ministers agreed in April 2021 to implement a **series of data centers** to be constructed by Cybastion Institute of Technology.
- The official Cybastion page says the project launched at an April 29 signing ceremony with EU and U.S. diplomatic presence.

Handling:
- Grade **A for Cybastion's self-claimed agreement/signing**, not for completion.
- Status is **unknown / stale planned** unless later official progress is found. Cybastion's 2025/2026 public materials highlight other African projects and do not clearly show CAR construction progress.
- Default division to Bangui only if the record must be assigned and the only known context is national-government signing; otherwise use country-level/location-unassigned notes.

Query templates:

```text
site:cybastiontech.com "Central Africa Republic" "data centers"
site:gouv.cf Cybastion "centre de donnees" OR datacenter
"Cybastion" "Central African Republic" "data centers"
"Cybastion Institute of Technology" Centrafrique "centre de donnees"
"Henri-Marie Donda" Cybastion datacenter
"Felix Moloua" Cybastion "data centers"
```

### 1.8 ECCAS / PIDA regional plan

Verified lead:
- OECD Africa's Development Dynamics 2025 cites ECCAS electronic-communications infrastructure planning and a **PIDA PAP2 initiative for six new data centers including one in the Central African Republic**. Treat as **B planning context** until the PIDA/ECCAS project fiche is opened.

Handling:
- Stage planned; site likely Bangui but unconfirmed. Do not duplicate with CAB/GreenLine/Huawei/Cybastion unless linked by source.

Query templates:

```text
site:pida.org "Central African Republic" "data center"
site:eccas.int "centre de donnees" Centrafrique
"PIDA PAP2" "Central African Republic" "data centers"
"CEEAC" "Centrafrique" "centre de donnees"
"ECCAS" "electronic communications" "data centers" "Central African Republic"
```

### 1.9 Energy and grid evidence

Primary routes: ENERCA and government energy pages.

Use:
- Boali hydro / Ombella-Mpoko and Bangui substations as power-context evidence.
- Search for gensets, UPS, substations, transformers, solar, cooling, diesel storage, and grid upgrade records tied to named data-centre projects.

Energy query templates:

```text
site:enerca-rca.com "centre de donnees" OR datacenter OR numerique
site:energies.gouv.cf Boali MW Bangui
"ENERCA" "Boali" "MW" "Bangui"
"{project}" ENERCA "groupe electrogene" OR onduleur OR transformateur
"{project}" Bangui "poste electrique" OR "groupe electrogene"
"RCA" datacenter energie solaire OR diesel OR UPS
```

### 1.10 Official hyperscaler / certification absence checks

Check these as A-grade absence/presence sources:

```text
AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
Google Cloud: https://cloud.google.com/about/locations
OCI: https://www.oracle.com/cloud/cloud-infrastructure/regions/
Uptime Institute: https://uptimeinstitute.com/tiers-certification/
```

Rules:
- CAR has no listed AWS/Azure/GCP/OCI public cloud region in the official lists checked on 2026-08-12.
- A `Tier 3` claim is not a certification unless Uptime or a named certifying body confirms it. Store GreenLine/Huawei/CAB Tier language as self-claimed/design-target unless certified.

---

## 2. Candidate handling table

| Lead | Division | Current handling | Grade |
|---|---|---|---|
| CAB-CAR National Datacentre / Digital Training Centre, Bangui | Bangui | Strong official project lead from AfDB MapAfrica + gouv.cf CAB page. Stage must be verified from latest project status; capacity null. | A for project inclusion; stage as found |
| GreenLine / SOCATEL Tier 3 Data Center | Bangui or location-unassigned national | Planned/partnership operationalization; GreenLine official announcement + 2026 press. No site/capacity/certification. | A for vendor announcement; B for government-stage press |
| Huawei Administration Digital Infrastructure / Tier III Government Data Centre | Bangui or location-unassigned national | Planned lead from Digital Business Africa; needs Huawei/gouv/procurement corroboration. | B |
| Cybastion government data centers | Bangui or location-unassigned national | Official vendor says April 2021 agreement/signing; no verified completion. | A for signing; C/U for current status |
| ECCAS/PIDA PAP2 CAR data center | Location unassigned, likely Bangui | Regional planning lead; verify PIDA/ECCAS fiche. | B until primary fiche |
| Orange Centrafrique Bangui data centre / core network | Bangui | 2021 fire reports explicitly mention data centre/core network; operational resumption reported. Treat as telecom technical facility, not colo. | B |
| ARCEP 80 TB monitoring platform | Bangui | Institutional server/storage room at ARCEP HQ. Not a data centre. | A for platform/storage |
| SOCATEL .cf registry infrastructure | Bangui/entity plus offshore technical contacts | IANA proves SOCATEL role/address; name servers/technical contact appear offshore. Not a data centre. | A for registry/entity |
| Starlink / DEVEAG | Countrywide service; Bangui launch | Connectivity service only; never a data-centre facility. | B/A depending source |
| datacenters.com CAR page | Unknown | Directory says 2 data centers/providers; names must be captured and corroborated. | C |

---

## 3. Prefecture-by-prefecture official search matrix

Run the universal query set for all 17 manifest divisions. For candidate national projects with no stated site, assign to Bangui only when the source context names Bangui or national-government facilities there; otherwise mark location unassigned in notes if schema permits.

| Manifest division | Current-name / locality note | Official search focus | Expected outcome |
|---|---|---|---|
| **Bangui** | Capital / commune | CAB national datacentre + Digital Training Centre; SOCATEL Rue Guerillot; ARCEP HQ; ministry/modernisation sites; Orange core/data-centre fire; Huawei/Cybastion/GreenLine national projects; banks; Digital CFD/University of Bangui | Primary facility and institutional-compute locus |
| **Ombella-Mpoko** | Boali, Bimbo | ENERCA/Boali power, fibre route, peri-Bangui infrastructure | Power/connectivity context; no standalone DC unless named |
| **Haute-Sangha / Mambere-Kadei** | Mambere-Kadei; Berberati | CAB Cameroon link, border telecom POPs | Fibre context; negative for DC unless named |
| **Lobaye** | Mbaiki | CAB/fibre, government admin, banks | Negative expected |
| **Nana-Mambere** | Bouar | Telecom agency, fibre/admin searches | Negative expected |
| **Ouham** | Bossangoa | Telecom/admin searches | Negative expected |
| **Ouham-Pende** | Bozoum | Telecom/admin searches | Negative expected |
| **Ouaka** | Bambari | Regional telecom hub, Orange agency/core resilience | Negative expected |
| **Haute-Kotto** | Bria | Admin/UN/bank/telecom searches | Negative expected |
| **Mbomou** | Bangassou | Admin/UN/bank/telecom searches | Negative expected |
| **Basse-Kotto** | Mobaye | Admin/telecom searches | Negative expected |
| **Haut-Mbomou** | Obo | Admin/telecom searches | Negative expected |
| **Vakaga** | Birao | Admin/telecom searches | Negative expected |
| **Bamingui-Bangoran** | Ndele | Admin/telecom searches | Negative expected |
| **Sangha** | Sangha-Mbaere; Nola | Forestry/mining operators, telecom/admin | Negative expected |
| **Kemo-Gribingui** | Kemo/Nana-Grebizi legacy; Sibut/Kaga-Bandoro context | Admin/telecom searches; be careful with reform names | Negative expected |
| **Gribingui** | Nana-Grebizi / Gribingui legacy | Admin/telecom searches | Negative expected |

Universal official-prefecture query set:

```text
"{prefecture}" "centre de donnees" Centrafrique
"{prefecture}" datacenter OR "data center" "Central African Republic"
"{prefecture}" "salle serveur" OR "salle informatique"
"{prefecture}" "fibre optique" OR "dorsale" OR "noeud"
"{prefecture}" "banque" "serveur"
"{prefecture}" "universite" informatique serveur
site:gouv.cf "{prefecture}" numerique OR "fibre optique"
site:telecommunications.gouv.cf "{prefecture}"
site:documents.worldbank.org "{prefecture}" "Central African Republic" digital
site:afdb.org "{prefecture}" Centrafrique "fibre" OR datacenter
```

---

## 4. Output discipline

- Use the 17 manifest divisions exactly. Do not add new division names even if sources use current prefectures; put current names in notes.
- Prefer French project names from official sources; include English aliases when trade sources use them.
- `capacity_mw` only from source-stated MW/IT-load for the exact facility. Put kVA, gensets, square metres, racks, or storage TB in notes.
- Keep `evidence_grade=A` only when the cited source is primary for the fact claimed. Vendor self-announcements are A for the vendor's claim, not for government completion.
- Do not count Starlink, fibre routes, operator licences, .cf registry records, or generic cloud services as data centres.
- Do not count ARCEP/SOCATEL/bank/operator server rooms as commercial facilities unless the source explicitly calls them a data centre.
- For stale planned projects, keep status `planned` or `unknown`; never infer construction from MoU/signing language.
- Mark `no_projects=true` only after running the universal templates plus operator/vendor/donor terms for that division.
- Country-level status as of 2026-08-12: **confirmed public data-centre leads are concentrated in Bangui; no verified operational commercial colocation market; several national/government planned or institutional facilities; non-Bangui divisions are negative except for fibre/power context.**
