# CF Explorer Industry - Central African Republic Datacenter Enumeration via Trade Press, Operators, Vendors, Directories, and Division Searches

Date: 2026-08-12. Country: **CF Central African Republic (RCA / Centrafrique)**. Scope: industry, operator, vendor, directory, and press-led discovery for CAR datacentres, with official verification routes for each lead. Division model: **17 divisions per world-manifest.jsonl**; use the normalization caveat in `explorer-official.md`.

This methodology was upgraded from draft to final quality with web verification on 2026-08-12. It is a country research guide, not a facility record.

Reliability grades:
- **A** = primary / official or owner source for the fact claimed: operator/vendor announcement, government/ministry page, ARCEP, IANA, AfDB/World Bank project document, official cloud-region page, Uptime certification.
- **B** = strong trade or local press: Agence Ecofin / Ecofin Agency, We Are Tech, RFI, Radio Ndeke Luka, RJDH, Oubangui Medias, Digital Business Africa, Data Center Dynamics, Developing Telecoms, Telecompaper, Ecomatin, Emergency Telecommunications Cluster.
- **C** = weak lead: datacenters.com, DataCenterMap, Cloudscene, PeeringDB, Baxtel, market reports, social posts, directory snippets, tender aggregators without original documents.
- **U** = searched negative / unverified absence.

---

## 0. Market frame

- CAR has a very thin data-centre market. DataReportal reported **616,600 internet users and 10.6% penetration in early 2024**; World Bank/ITU-series data put 2024 individual internet use around 13.8%. Most access is mobile or satellite, and fixed broadband remains minimal.
- Do not assume absence of all data-centre projects. Verified leads now include: **CAB-CAR national datacentre/Digital Training Centre in Bangui**, **GreenLine/SOCATEL Tier 3 plan**, **Huawei/government Tier III lead**, **Cybastion government data centers**, **ECCAS/PIDA CAR data-center plan**, **Orange Centrafrique Bangui data-centre/core-network facility**, and **ARCEP 80 TB institutional monitoring platform**.
- The operational-commercial-colocation baseline remains weak: no verified carrier-neutral commercial colo facility was found. Most records are government, telecom, planned, or institutional.
- **Bangui is the high-yield city.** Non-Bangui searches usually return fibre, power, government-office, bank, NGO, or telecom agency context rather than data-centre facilities.
- **Starlink is a connectivity service, not a facility.** Public reports say Starlink went live commercially in March 2026 after a December 2025 authorization/agreement and is managed locally by DEVEAG-Centrafrique. Use it only as demand/connectivity context.
- **Hyperscaler absence:** official AWS, Azure, Google Cloud, and OCI lists have no CAR public region. Treat these as A-grade absence checks.
- **Directories are leads only.** datacenters.com search results currently claim 2 CAR data centers/providers, but the page can be blocked/rate-limited and names must be captured and corroborated before use.

Core national query set:

```text
Central African Republic ("data center" OR datacenter OR "data centre") Bangui
Centrafrique ("centre de donnees" OR datacenter OR "data center") Bangui
"RCA" "centre de donnees" OR datacenter
"Bangui" "salle serveur" OR "salle informatique"
"Centrafrique" "cloud souverain" OR "cloud national"
"Centrafrique" hebergement serveur
"Central African Republic" "Tier III" OR "Tier 3" "data center"
"Socatel" "Tier 3" OR "Tier III" datacenter
"Centrafrique" datacenter Orange OR Telecel OR Moov OR SOCATEL
"Central African Republic" "national data centre" OR "Digital Training Centre"
```

---

## 1. High-signal industry and press sources

Use press to discover project names, dates, officials, vendors, and status language. Upgrade only after matching to owner, government, ARCEP, AfDB/World Bank, or certification evidence.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| GreenLine Technologies | https://greenline-tech.com/ | Owner/vendor source for SOCATEL mandate, USD 150M package, and Tier 3 data-center plan. | A for self-claims |
| Cybastion | https://www.cybastiontech.com/ | Owner/vendor source for April 2021 CAR government data-center signing. | A for self-claims |
| Agence Ecofin / Ecofin Agency | https://www.agenceecofin.com/ / https://www.ecofinagency.com/ | Best trade route for SOCATEL/GreenLine, Huawei, Starlink, operator recovery, fibre. | B |
| We Are Tech | https://www.wearetech.africa/ | Digital-infrastructure and government-cloud coverage. | B |
| Radio Ndeke Luka | https://www.radiondekeluka.org/ | CAR official interviews and local reporting; useful for GreenLine, Starlink, ARCEP. | B; A for direct official transcript claims only |
| RJDH | https://rjdh.net/ | Local launch coverage such as Starlink and ministry events. | B |
| Oubangui Medias | https://oubanguimedias.com/ | Local telecom and government-project coverage. | B |
| Digital Business Africa | https://www.digitalbusiness.africa/ | Huawei/Tier III government lead; Orange Centrafrique fire report; regional DC context. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Telecom/data-centre trade corroboration, especially Orange and regional market leads. | B |
| Developing Telecoms / Telecompaper | developingtelecoms.com / telecompaper.com | Operator and SOCATEL/GreenLine corroboration. | B |
| Emergency Telecommunications Cluster | https://www.etcluster.org/ | Operational resilience context after Orange/Bangui server-room fire. | B |
| DataReportal / World Bank Data | datareportal.com / data.worldbank.org | Internet adoption context only. | B/A depending source |
| Directories | datacenters.com, DataCenterMap, Cloudscene, PeeringDB, NSRC Africa data-centres map | Lead indexes only; require corroboration. | C |

Trade-press queries:

```text
site:agenceecofin.com Centrafrique "data center" OR datacenter OR "centre de donnees" OR SOCATEL OR Huawei
site:ecofinagency.com "Central African Republic" "data center" OR SOCATEL OR Starlink OR Orange
site:wearetech.africa Centrafrique datacenter OR "centre de donnees" OR numerique
site:radiondekeluka.org SOCATEL OR "Green Line" OR Starlink OR ARCEP OR datacenter
site:rjdh.net Starlink OR "economie numerique" OR datacenter
site:oubanguimedias.com SOCATEL OR Starlink OR "centre de donnees"
site:digitalbusiness.africa Centrafrique Huawei OR Orange OR datacenter OR "Tier III"
site:datacenterdynamics.com "Central African Republic" Orange OR "data center"
site:developingtelecoms.com "Central African Republic" SOCATEL OR Orange OR datacenter
site:telecompaper.com "Central African Republic" SOCATEL OR Orange OR "data centre"
```

Status-language interpretation:
- `protocole d'accord`, `memorandum d'entente`, `MoU`, `partenariat`, `mandat`, `ambition` = planned / negotiation. Do not mark construction.
- `lance la phase operationnelle` = partnership execution has begun; still not construction unless works/site are named.
- `pose de la premiere pierre`, `lancement des travaux`, `construction`, `chantier` = construction lead.
- `inaugure`, `mis en service`, `operationnel`, `lancement officiel` = operational only for the thing launched. Starlink/fibre service launch is not data-centre commissioning.
- `Tier 3` / `Tier III` = design or marketing claim unless Uptime/certifier evidence exists.

---

## 2. Operator and vendor sweep

| Entity | Main source route | Likely geography | Handling |
|---|---|---|---|
| **SOCATEL** | IANA .cf record; GreenLine; press; possible `socatel.cf` | Rue Guerillot, Bangui | .cf ccTLD manager and state incumbent. GreenLine plan includes new Tier 3 DC; planned only. IANA proves entity/address, not facility. |
| **GreenLine Technologies** | greenline-tech.com/news | Location unassigned national / Bangui likely | Official 18 Sep 2025 announcement: SOCATEL mandate, USD 150M, new Tier 3 DC. Search for 16 Jul 2026 operational-phase follow-up. |
| **AfDB / CAB-CAR** | MapAfrica, afdb.org, gouv.cf | Bangui / University of Bangui context | Strong official lead for national datacentre + Digital Training Centre in Bangui. Verify stage and contractor. |
| **Huawei** | Huawei domain, government domains, Digital Business Africa | Bangui / government | B-grade lead for public-administration Tier III national data centre. Needs primary corroboration. |
| **Cybastion Institute of Technology** | cybastiontech.com | National / Bangui inferred | Official vendor says April 2021 CAR ministers agreed to data centers. Stale; verify progress before counting as active. |
| **Orange Centrafrique** | Orange pages; Digital Business Africa; DCD; Developing Telecoms; Ecofin | Bangui | 2021 fire reports explicitly mention data centre/core network/radio installations. Treat as telco technical facility, not colo. |
| **Telecel Centrafrique** | operator pages, Telecel Group, ARCEP/press | Bangui | Mobile operator likely has core/server rooms; no public DC evidence found. |
| **Moov Africa Centrafrique** | Moov/Maroc Telecom pages; local press | Bangui | Mobile operator; MIA AI assistant service does not prove local hosting. |
| **DEVEAG-Centrafrique / Starlink** | RFI, RJDH, Radio Ndeke Luka, Starlink map/X | Bangui launch, national service | Connectivity only. Do not enumerate as facility. |
| **Banks / BEAC / MINUSCA / universities** | official pages and annual reports | Bangui / regional towns | Internal ICT/server rooms possible; count only with explicit data-centre language. |

Operator/vendor templates:

```text
"{operator}" Centrafrique "data center" OR datacenter OR "centre de donnees"
"{operator}" Bangui "salle serveur" OR "coeur de reseau" OR infrastructure
"{operator}" "RCA" cloud OR hebergement OR serveur
"{operator}" "Tier III" OR "Tier 3" "Central African Republic"
"Orange Centrafrique" "data centre" OR "coeur de reseau" OR incendie
"Telecel Centrafrique" datacenter OR "salle serveur"
"Moov Africa Centrafrique" datacenter OR serveur OR hebergement
"DEVEAG-Centrafrique" Starlink infrastructure Bangui
```

---

## 3. Directory and aggregator handling

| Directory / lead source | What it may provide | Caveats |
|---|---|---|
| datacenters.com CAR page | Search result states 2 CAR data centers/providers. | C until exact facility names and addresses are visible and corroborated; page may return 403/429. |
| DataCenterMap | Facility/country entries if any appear. | C; no robust CAR page confirmed. |
| PeeringDB | Network/facility/interconnection records. | C for facility discovery; proves network presence only. |
| Cloudscene / Baxtel | Provider/facility profiles. | C; often stale or quote-oriented. |
| NSRC Africa data-centres map | Open dataset / map of African data centres. | C unless matched to primary/operator evidence. |
| DevelopmentAid / UNDB / procurement aggregators | Tender leads. | C unless original buyer PDF is opened. |

Directory upgrade workflow:

1. Capture exact facility name, provider, address/locality, status, and any capacity.
2. Search exact name + Bangui/Centrafrique + operator.
3. Search owner domain, `site:gouv.cf`, `site:arcep.cf`, AfDB/World Bank, and local/trade press.
4. Search for power/cooling/certification (`groupe electrogene`, UPS, Tier, Uptime, racks, MW).
5. If no corroboration appears, keep as C or discard from final enumeration depending on project rules.

Directory templates:

```text
site:datacenters.com/locations/central-african-republic "Central African Republic"
site:datacentermap.com "Central African Republic" OR Bangui
site:peeringdb.com Bangui OR "Central African Republic"
site:cloudscene.com "Central African Republic" datacenter
site:baxtel.com "Central African Republic" datacenter
site:africa-datacentres.nsrc.org "Central African Republic" OR Bangui
"{facility-name-from-directory}" Bangui OR Centrafrique
```

---

## 4. Lead-specific verification recipes

### 4.1 CAB-CAR National Datacentre / Digital Training Centre

Use this as the first official confirmation route for any Bangui national data-centre record.

```text
site:mapafrica.afdb.org "Central Africa Fibre-Optic Backbone" "CAR Component" datacentre
site:afdb.org "P-CF-GB0-002" datacentre OR "Digital Training Centre"
site:gouv.cf "Dorsale-Fibre Optique" "Composante RCA"
"Universite de Bangui" "Digital Training Centre" datacentre
"Bangui University" "national data centre" "CAB"
```

Record as Bangui only if the source names Bangui / University of Bangui. Treat fibre routes through Ombella-Mpoko or Mambere-Kadei as connectivity context, not facilities.

### 4.2 GreenLine / SOCATEL Tier 3

```text
site:greenline-tech.com SOCATEL "Tier 3 data center"
"Greenline Technologies" SOCATEL "150 million" "Tier 3"
"Green Line" SOCATEL "16 juillet 2026" Bangui
site:radiondekeluka.org "Green Line" SOCATEL
site:agenceecofin.com SOCATEL Greenline "Tier 3"
site:gouv.cf SOCATEL Greenline "centre de donnees"
```

Record `planned` unless construction/commissioning evidence appears. Do not assign MW or Uptime certification from generic Tier III definitions.

### 4.3 Huawei / public administration Tier III lead

```text
site:digitalbusiness.africa Centrafrique Huawei "Tier III" "centre national de donnees"
site:gouv.cf Huawei "centre de donnees" OR datacenter
site:modernisation.gouv.cf Huawei "e-gouvernance" OR datacenter
site:huawei.com Centrafrique "data center" OR "digital government"
"Bangui" Huawei "modernisation numerique" "centre de donnees"
```

Keep B until a primary government/Huawei/procurement source appears. Check whether it overlaps CAB/PGNSP/Cybastion/GreenLine before creating a separate record.

### 4.4 Cybastion government data centers

```text
site:cybastiontech.com "Data Centers Soon to Rise in Central Africa Republic"
site:gouv.cf Cybastion datacenter OR "centre de donnees"
"Cybastion" "Henri-Marie Donda" "data centers"
"Cybastion Institute of Technology" "Central African Republic"
```

The Cybastion page is primary for the 2021 signing, but stale for current status. Search later Cybastion year-in-review and government pages; if CAR is absent from later project-progress lists, keep current status unknown/stale.

### 4.5 Orange Centrafrique Bangui data-centre/core-network facility

```text
"Orange Centrafrique" "data center" incendie
"Orange Centrafrique" "coeur de reseau" "centre de donnees"
site:digitalbusiness.africa "Orange Centrafrique" "data center"
site:developingtelecoms.com "Orange CAR" "data centre" "core network"
site:datacenterdynamics.com "Orange" "Central African Republic" "data center"
site:ecofinagency.com Orange "Central African Republic" resumes operations
```

This is a telco technical facility. If enumerated, use `developer=Orange Centrafrique`, `division=Bangui`, `capacity_mw=null`, notes explaining 2021 fire and service restoration. Do not classify as colocation.

---

## 5. Division-by-division industry search matrix

Use all 17 manifest divisions. The likely positive division is Bangui; all others require documented negative searches.

| Priority | Manifest division | Localities / seeds | Industry search focus |
|---|---|---|---|
| 1 | **Bangui** | Rue Guerillot, University of Bangui, Digital Training Centre, Digital CFD, ARCEP HQ, Orange HQ/core, ministry buildings, banks, airport area | CAB national datacentre, GreenLine/SOCATEL, Huawei, Cybastion, Orange, ARCEP, Starlink launch context |
| 2 | **Ombella-Mpoko** | Boali, Bimbo | Power context, Boali hydro, peri-Bangui infrastructure; no DC unless named |
| 2 | **Haute-Sangha / Mambere-Kadei** | Berberati | CAB Cameroon link, border POPs, telecom nodes |
| 3 | **Ouaka** | Bambari | Regional mobile/agency hub; negative expected |
| 3 | **Nana-Mambere** | Bouar | Mobile agencies, government ICT, fibre/admin searches |
| 3 | **Ouham** | Bossangoa | Regional telecom/admin searches |
| 3 | **Ouham-Pende** | Bozoum, Paoua legacy context | Telecom/admin searches |
| 3 | **Lobaye** | Mbaiki | Telecom/admin searches |
| 4 | **Basse-Kotto** | Mobaye | Negative search only unless named source appears |
| 4 | **Haute-Kotto** | Bria | Negative search; UN/bank/telecom context |
| 4 | **Haut-Mbomou** | Obo | Negative search |
| 4 | **Mbomou** | Bangassou | Negative search; bank/UN/telecom context |
| 4 | **Vakaga** | Birao | Negative search |
| 4 | **Bamingui-Bangoran** | Ndele | Negative search |
| 4 | **Sangha** | Sangha-Mbaere, Nola | Negative search; forestry/mining operators only if named |
| 4 | **Kemo-Gribingui** | Sibut/Kaga-Bandoro legacy | Negative search; beware current Kemo/Nana-Grebizi names |
| 4 | **Gribingui** | Kaga-Bandoro/Nana-Grebizi legacy | Negative search |

Universal division query set:

```text
"{division}" "centre de donnees" Centrafrique
"{division}" datacenter OR "data center" "Central African Republic"
"{locality}" "centre de donnees" OR datacenter OR "salle serveur"
"{locality}" Orange OR Telecel OR Moov OR SOCATEL "serveur"
"{locality}" "fibre optique" OR telecom OR "noeud"
"{locality}" banque serveur OR "salle informatique"
site:radiondekeluka.org "{locality}" numerique OR telecom
site:digitalbusiness.africa "{locality}" datacenter OR telecom
site:agenceecofin.com "{locality}" Centrafrique telecom OR fibre
```

---

## 6. Candidate grading examples

- **CAB-CAR National Datacentre / Digital Training Centre:** A for AfDB/government project inclusion; stage depends on latest AfDB/government status; no MW.
- **GreenLine / SOCATEL Tier 3:** A for GreenLine announcement of a planned Tier 3 data center and USD 150M investment; B for 2026 press describing operational-phase launch; planned until works are named.
- **Huawei government Tier III:** B from Digital Business Africa; upgrade only with government/Huawei/procurement source.
- **Cybastion government data centers:** A for Cybastion's 2021 signing claim; current status unknown/stale unless later progress found.
- **Orange Centrafrique:** B for press reports that its Bangui data centre/core network burned in 2021 and service later resumed; telco facility, not colo.
- **ARCEP 80 TB platform:** A from World Bank blog for institutional monitoring storage at ARCEP HQ; not a data-centre project.
- **Starlink / DEVEAG:** B/A service launch evidence; connectivity only.
- **datacenters.com 2 CAR data centers:** C until exact entries are visible and corroborated.

---

## 7. Output discipline

- Normalize every row to one of the 17 manifest divisions; keep current prefecture/locality in notes.
- Keep national planned leads separate unless a source explicitly says they are the same project.
- Do not upgrade from planned to construction based on MoU/partnership language.
- Do not assign Bangui to a project solely because the country capital is likely; use Bangui only when the source names Bangui or the event/facility context is a national government site in Bangui and note the inference.
- Do not count fibre routes, cloud services, satellite services, operator licences, or registry infrastructure as data centres.
- `capacity_mw` must stay null unless facility-specific MW/IT-load is published.
- For no-project prefectures, note targeted searches across data center/datacenter/centre de donnees/server farm/colocation/cloud region/hyperscale/AWS/Google/Microsoft/Meta/Equinix/Digital Realty/NTT/Orange/Huawei/GreenLine/SOCATEL/CAB terms.
- Current country-level summary as of 2026-08-12: **Bangui has several verified official/industry data-centre leads and institutional compute sites; no verified operational commercial colocation market; the other 16 manifest divisions remain negative for data-centre projects except fibre and power context.**
