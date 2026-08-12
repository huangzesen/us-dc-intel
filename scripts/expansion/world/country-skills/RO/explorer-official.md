# RO Explorer Official - Romania Datacenter Enumeration via Permits, Environment, Energy, Procurement, Regulator, and Cloud Sources

Date: 2026-08-12. Scope: Romania (RO), 41 counties plus Bucuresti municipality. Focus angle: official/regulatory-first enumeration for datacenter facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/operator source, **C** = weak aggregate/unverified lead.

---

## 0. Structural facts that shape Romania enumeration

- Romania has no single public national "data center registry". Build the census by joining **local construction permits**, **ANMAP/ANPM county environmental files**, **SEAP/SICAP procurement**, **Transelectrica and DSO connection evidence**, official government-cloud/regional-program pages, operator pages, and trade press.
- Construction permits are decentralized. The record unit is usually the municipality, city, commune, county council, or Bucharest sector. There is no Poland-style national construction search that reliably covers every data-center permit.
- Use Romanian search language first. Official files usually say `centru de date`, `centre de date`, `centru de procesare date`, `centru de servicii IT&C`, `camera servere`, `servere`, `colocare`, `cloud`, `infrastructura TIC`, `imobil cu destinatie speciala`, `racordare la RED/RET`, `post trafo`, `statie 110/20 kV`, `grup electrogen`, `UPS`, `climatizare`, `stingere incendiu cu gaz inert`.
- `Certificat de urbanism` (CU) is a planning/notice precursor, not a build right. Count a project as stronger only when there is an `autorizatie de construire` (AC), `acord de mediu` / `decizie etapa de incadrare`, procurement award, operator launch, or clear public owner announcement.
- Romanian public-sector datacenters matter: STS, ADR, county councils, ministries, universities/research institutes, BNR, utilities, and government cloud projects can produce large or strategic facilities that do not appear in commercial colo directories.
- Bucharest and Ilfov dominate the private pipeline, but official discovery must also cover Dolj, Valcea, Timis, Brasov, Sibiu, Cluj, Prahova, Iasi, Mures, Bihor, Constanta, Galati, Giurgiu, Teleorman, Tulcea, and other county-specific public projects.

Lifecycle vocabulary:

`PUZ/PUD/PUG / certificat de urbanism` < `solicitare acord de mediu / memoriu de prezentare` < `decizie etapa de incadrare / acord de mediu` < `autorizatie de construire` < `licitatie proiectare si executie` < `lucrari / receptie` < `punere in functiune / inaugurare / operational`

Recommended status rule:

- **Planned**: CU/PUZ/PUD, funding allocation, feasibility study, or non-binding public announcement.
- **Approved**: environmental decision, AC, or signed public financing/procurement contract.
- **Construction**: operator/trade/local authority says works started or a works contract is awarded.
- **Operational**: operator page, STS/government announcement, Uptime/PeeringDB/interconnect evidence, or public inauguration.

---

## 1. Romanian and English query patterns

### 1.1 Core Romanian terms

```text
centru de date
centre de date
datacenter OR data center
centru de procesare date
centru de prelucrare date
centru de servicii IT&C
camera servere OR sala servere
colocare OR colocation
cloud privat guvernamental
cloud regional
infrastructura TIC
centru regional de date
centru de date sustenabil
centru de date container
hub AI OR centru AI
supercomputer OR HPC
imobil cu destinatie speciala
racordare la RED centru de date
racordare la RET centru de date
post de transformare centru de date
statie 110/20 kV centru de date
grup electrogen centru de date
UPS centru de date
climatizare centru de date
stingere incendiu gaz inert centru de date
```

### 1.2 Permit, planning, and local-government queries

Substitute `{judet}`, `{municipiu}`, `{oras}`, `{comuna}`, `{sector}`, `{operator}`, `{legal_entity}`, `{address}`, `{parcel}`.

```text
"centru de date" "{judet}" "autorizatie de construire"
"centru de date" "{municipiu}" "certificat de urbanism"
"centru de date" "{comuna}" "PUZ" OR "PUD"
"centru de date" "{operator}" "autorizatie de construire"
"centru de procesare date" "{municipiu}" "registru autorizatii"
"racordare la RED" "centru de date" "{municipiu}"
"racordare la RET" "centru de date" "{judet}"
"grup electrogen" "centru de date" "{judet}"
"statie 110/20 kV" "centru de date" "{judet}"
site:{primarie-domain} "centru de date" "autorizatie"
site:{primarie-domain} "centru de date" "certificat de urbanism"
site:{judet-domain} "centru de date" "hotarare"
site:{judet-domain} "centru de date" "parteneriat" "STS"
filetype:pdf "centru de date" "autorizatie de construire" "{judet}"
filetype:pdf "centru de date" "certificat de urbanism" "{municipiu}"
```

### 1.3 Environmental, energy, and procurement queries

```text
site:anmap.gov.ro "centru de date" "{judet}"
site:anpm.ro "centru de date" "acord de mediu"
site:{county-code}.anmap.gov.ro "centru de date"
site:{old-county-apm}.anpm.ro "centru de date"
"centru de date" "decizia etapei de incadrare"
"centru de date" "memoriu de prezentare"
"centru de date" "Acord de mediu"
"centru de date" "ANMAP" "{judet}"
"centru de date" "ANPM" "{judet}"
site:e-licitatie.ro "centru de date" "{judet}"
site:e-licitatie.ro "centru de date" "proiectare si executie"
site:e-licitatie.ro "centru de date sustenabil"
site:e-licitatie.ro "Centrul de Date Regional"
site:transelectrica.ro "centru de date"
site:transelectrica.ro "racordare" "centru de date"
"centru de date" "Transelectrica" "MW"
"centru de date" "Rețele Electrice Muntenia" OR "Retele Electrice Muntenia"
"centru de date" "Distributie Energie Electrica Romania" OR DEER
"centru de date" "Distributie Oltenia"
```

### 1.4 English patterns

```text
"Romania" "data center" "building permit"
"Bucharest" "data center" "building permit"
"Romania" "data center" "environmental permit"
"Romania" "data center" "grid connection"
"Bucharest" "data center" "110/20 kV"
"Romania" "government cloud" "data centers" STS
"Romania" "regional data center" STS
"Romania" "data center" Transelectrica MW
"Bucharest" "AWS Local Zone" Romania
"Azure" Romania "datacenter region"
"Google Cloud" Bucharest "Interconnect"
```

---

## 2. Official / regulatory source backbone

### 2.1 Construction permits and planning

Primary surfaces:

- **Municipality/city/commune construction registers**. Examples verified during research: Constanta has a `Registrul de autorizatii in constructii` at https://primaria-constanta.ro/pagina-pmc/servicii-cetateni/urbanism/registrul-de-autorizatii-in-constructii/ and a searchable service at https://www.pmconline.ro/ServiciiOnline/RegistruAn.aspx ; Brasov has a searchable `Consultare Registru Autorizatii de Construire` at https://extranet.brasovcity.ro/Registratura/Urbanism/Consultare-Autorizatii-Construire.aspx ; Sibiu has `Consultare Registru Autorizatii de construire` at https://e-serviciielectronice.sibiu.ro/Registratura/RegistruUrbanism/?registru=AC ; Alba Iulia uses the same style at https://se.apulum.ro/Registratura/RegistruUrbanism/?registru=AC . **Grade A**.
- **Bucharest city and sector portals**. PMB urbanism front door: https://urbanism.pmb.ro/ ; Sector 3 publishes construction authorizations and certificates, with search evidence such as a 2025 certificate entry for `racordare la RED centru de date` in `CU_02.2025.pdf`. Start at https://www.primarie3.ro/index.php/primaria/autorizatii_constructii and search each sector. **Grade A**.
- **County councils and local councils**. Use `Monitorul Oficial al Judetului`, `registrul proiectelor de hotarare`, council meeting agendas, `HCL`/`HCJ` resolutions, and `documentatii urbanism`. Example: Ialomita County Council registry surfaced the South-Muntenia regional data-center association with STS. **Grade A**.
- **National geospatial/context portals**. Use ANCPI/eTerra/geoportal and local GIS only after a candidate address/parcel is known. Treat as context, not facility proof unless tied to an official permit.

Fields to capture from CU/AC/PUZ/PUD records:

- authority and document number/date;
- applicant / beneficiary / `titular`;
- work title (`obiectul solicitarii`, `descrierea lucrarilor`);
- address, cadastral number, land book, plot;
- validity and execution term;
- building function, height regime, built area, technical annexes;
- grid-related works, transformer station, `bransamente`, generators, cooling and fire-suppression clues.

Do not require exact phrase `centru de date`. Many real projects appear as `imobil cu destinatie speciala`, `spatiu tehnic`, `modernizare infrastructura IT`, `racordare la RED`, `post trafo`, or `amenajare tehnologica`.

### 2.2 Environment: ANMAP / ANPM and county agencies

Primary surfaces:

- ANMAP national site: https://anmap.gov.ro/ . In 2025 ANMAP replaced/absorbed the former ANPM public-facing structure; old county `anpm.ro` domains still appear in search and may redirect or remain indexed. **Grade A for current agency pages**.
- County environmental pages: search both new and old hostnames, for example `djmtr.anmap.gov.ro`, `apmb.anpm.ro`, `apmtm.anpm.ro`, `apmcluj.anpm.ro`, `apmph.anpm.ro`, etc. **Grade A** when a county agency page publishes a decision/memorandum.
- ANPM Atlas Explorer: https://atlas.anpm.ro/ . Useful for environmental datasets/context, not a complete data-center list. **Grade A context**.
- Ministry of Environment: https://mmediu.ro/ . Use for legal/process context and sensitive-area constraints. **Grade A**.

Environmental records are high-yield because datacenters trigger publishable clues: backup diesel generators, fuel storage, noise, air emissions, HVAC, batteries/UPS, water/cooling, and grid works. Capture:

- `memoriu de prezentare`, `decizia etapei de incadrare`, `acord de mediu`, `aviz de mediu`;
- project title, beneficiary, site, construction area;
- installed generator power, fuel tank sizes, cooling systems, noise mitigation;
- grid connection works and transformer/substation details.

Known official example: Teleorman county environmental page `djmtr.anmap.gov.ro` published `SC Class IT Outsourcing SRL - dezvoltare centru de asistenta IT international si centru de date... in Alexandria, Str. Turnu Magurele nr. 4`, corroborated by Alexandria's construction-permit register. Use this as the model for county ANMAP + city AC cross-check.

### 2.3 Energy and grid

Primary surfaces:

- Transelectrica: https://www.transelectrica.ro/ . **Grade A** for transmission-grid context and formal process.
- Transelectrica national transport network / RET context appears on pages explaining that RET is the national strategic electricity transport network above 110 kV. Use for grid geography and substation adjacency, not as a datacenter register.
- Transelectrica capacity-allocation process: https://www.transelectrica.ro/procesul-de-alocare-a-capacitatii-retelei-electrice . **Grade A for process**. The 2025/2026 allocation procedure mainly targets new production/storage sites >=5 MW; it matters when a datacenter project is paired with generation, BESS, or a private power plant.
- ANRE: https://www.anre.ro/ . **Grade A** for electricity connection rules and orders. Romanian grid connection is commonly discussed under `racordare`, `aviz tehnic de racordare` (ATR), `certificat de racordare`, and ANRE orders.
- Distribution operators: Retele Electrice Muntenia/Banat/Dobrogea (https://www.reteleelectrice.ro/), Distributie Energie Electrica Romania / DEER (https://www.distributie-energie.ro/), Delgaz Grid (https://delgaz.ro/), Distributie Oltenia (https://www.distributieoltenia.ro/), Premier Energy where relevant. **Grade A for process and public documents**.

Use energy evidence to find large projects, but separate fields carefully:

- `requested_connection_MW`, `ATR_status`, `connection_voltage`, `substation`, `DSO/TSO`;
- `generation_or_BESS_component` if the project is bundled with solar/BESS/gas;
- `datacenter_permit_status` and `operational_status`.

Caution: generation/storage grid auctions and ATR applications are not proof of a datacenter. For SANY, ClusterPower, VLA Energy, and Resita-type leads, verify whether the data-center component has separate permits/procurement/operator confirmation.

### 2.4 Public procurement: SEAP/SICAP, TED, and funding programs

Primary surfaces:

- SEAP/SICAP official portal: https://www.e-licitatie.ro/ . **Grade A** for Romanian public tenders, direct acquisitions, contract notices, market consultations, and annual procurement plans.
- TED: https://ted.europa.eu/ . **Grade A/B** for EU-noticed Romanian tenders; often easier to search in English once CPV/title is known.
- Autoritatea pentru Digitalizarea Romaniei (ADR): https://adr.gov.ro/ . **Grade A** for the Cloudul Privat Guvernamental project.
- ADR regional program pages, especially ADR Sud-Muntenia: https://2021-2027.adrmuntenia.ro/ . **Grade A** for regional strategic data-center projects.
- Ministry/research program pages: research.gov.ro, old.mcid.gov.ro, mfe.gov.ro, economie.gov.ro. **Grade A/B** depending on whether the page is current or archived.

High-yield SEAP terms:

```text
"centru de date"
"centru de date sustenabil"
"centru de date container"
"Centrul de Date Regional"
"Cloud Privat Guvernamental"
"proiectare si executie" "centru de date"
"amenajarea tehnologica" "centru de date"
"dotare centru de date"
"camera servere" "climatizare"
"grup electrogen" "UPS" "centru de date"
```

Known official/public-sector anchors:

- ADR's government-cloud page states the private government cloud uses modern datacenters in Bucuresti, Timisoara/Giroc, Brasov/Cristian, and Sibiu, with two Tier IV and two Tier III by design; it says the Cristian and Giroc datacenters were completed while Bucuresti and Sibiu were in completion status. Source: https://adr.gov.ro/cpg . **Grade A**.
- STS/Sibiu official page and Uptime Institute list `CDS II Sibiu` for Special Telecommunications Service. Sources: https://sts.ro/en/centrul-de-servicii-esentiale-it-c-al-sts-inaugurat-la-sibiu/ and Uptime awards pages. **Grade A**.
- ADR Sud-Muntenia describes the strategic `Centrul de Date Regional Sud-Muntenia` led by STS with county councils and value above EUR 47 million. Source: https://2021-2027.adrmuntenia.ro/proiectul-strategic-centrul-de-date-regional-sudmuntenia-in-linie-dreapta/article/273 . **Grade A**.
- County partners for South-Muntenia can produce duplicate county hits. If a source says the actual facility is in Ploiesti/Prahova, record participant counties as service beneficiaries, not separate physical facilities.

### 2.5 ANCOM and telecom regulator context

Primary surfaces:

- ANCOM main site: https://www.ancom.ro/ and press releases: https://www.ancom.ro/en/category/about-us/media-en/press-releases/ . **Grade A regulator context**.
- ANCOM is useful for telecommunications-market structure, numbering/spectrum, electronic communications rules, Digital Services Act coordinator context, significant-market-power decisions, and network/fiber context.
- ANCOM is **not** a datacenter permit registry. Use it to identify telecom operators and network infrastructure around Orange, DIGI, Vodafone, Telekom/Orange fixed network assets, GTS, Euroweb, M247, NXDATA-connected networks, and IX/peering facilities.

ANCOM queries:

```text
site:ancom.ro "centru de date"
site:ancom.ro "Orange Romania" "Telekom Romania Communications"
site:ancom.ro "DIGI Romania" "piata acces local"
site:ancom.ro "furnizori retele publice comunicatii electronice"
site:ancom.ro "infrastructura" "fibra optica" "{judet}"
```

Treat ANCOM evidence as supporting context unless a document directly names a data-center facility or telecom hosting node.

### 2.6 Official cloud-region and interconnect checks

Cloud pages prove logical service geography or network edge presence, not exact facilities.

| Provider | Official source | Romania signal as of 2026-08-12 | Enumeration use |
|---|---|---|---|
| AWS | AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; AWS Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | Official pages checked did **not** list Bucharest/Romania as an AWS Region or Local Zone. AWS has a Bucharest office per Amazon press, but office != datacenter. | Search `AWS Bucharest Romania Local Zone` only as a negative-control/currentness check. Do not count AWS Bucharest without an official AWS infrastructure page or local permit evidence. |
| Microsoft Azure | Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; Microsoft Datacenters: https://datacenters.microsoft.com/ | Official Azure geography page checked did **not** list Romania. Trade press reported Microsoft land/possible Otopeni plans, but no official Romania Azure region confirmation found. | Treat Microsoft/Otopeni as a permit/land lead only. Search Ilfov/Otopeni records for Microsoft/SPVs; do not count an Azure Romania region from trade rumor alone. |
| Google Cloud | Network edge locations: https://docs.cloud.google.com/vpc/docs/edge-locations ; Interconnect facilities: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities | Google lists Bucharest as a network edge metro and Cloud Interconnect facility `NXDATA-1 Bucharest Romania (BU1)`. No Romanian Google Cloud compute region found. | Grade A for Bucharest interconnect/edge. Use NXDATA-1 as a hard seed; do not infer a Google-owned Romanian region. |
| Oracle OCI | Public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ | No official Romania public OCI region found in checked list. | Office/partner pages are not facility evidence. |

---

## 3. Division-level official enumeration approach

Use every county name with both Romanian diacritics-free and local forms; for search consistency the manifest uses ASCII county names. For each county:

1. Query `site:{county/municipality domains} "centru de date"` plus `autorizatie`, `certificat de urbanism`, `PUZ`, `PUD`, `hotarare`, `registru autorizatii`.
2. Query county ANMAP/old ANPM hostnames for `centru de date`, `grup electrogen`, `UPS`, `statie 110/20`, `racordare`.
3. Query SEAP for the county, city, STS, university, county council, and local utilities.
4. Check DSO territory and power clues; escalate to Transelectrica when >=110 kV or bundled energy campus appears.
5. Cross-check operator/trade leads against official records before upgrading confidence.

Priority cluster strategy:

- **Bucuresti + Ilfov**: PMB UrbOnline, Sector 1-6 registers, Otopeni/Tunari/Chiajna/Voluntari/Magurele/Popesti-Leordeni/Chitila/Dragomiresti local portals, Retele Electrice Muntenia, ANMAP Bucuresti/Ilfov. Search NXDATA, Portland Trust, Voxility, GTS, Orange, Kyndryl, Solidus, Microsoft/Otopeni, `Bd. Timisoara`, `Preciziei`, `Releului`, `Dimitrie Pompeiu`, `Calea Rahovei`, `Tunari`, `Bucharest Ring Road`.
- **Dolj + Valcea**: ClusterPower/AIC/energy-campus records in Mischii/Craiova and Fauresti; Distributie Oltenia and Transelectrica/Transgaz context. Search gas plant, `200 MW`, `Mischii`, `Fauresti`, `hub tehnologic`, `centru AI`.
- **Timis**: Giroc/Timisoara government cloud, Orange/Telekom legacy, SANY/Uivar hybrid power + 70 MW data-center lead, local hosting facilities. Query Timisoara/Giroc/Uivar AC, ANMAP Timis, Retele Electrice Banat.
- **Brasov + Sibiu**: STS government cloud nodes in Cristian/Brasov and Sibiu, Orange Brasov, DEER modular data-center rumors. Query Brasov/Sibiu AC portals, STS, ADR, Uptime, ANMAP.
- **Cluj + Mures + Bistrita-Nasaud**: GTS Cluj, Luna/Tetarom V DriverAI lead, Vidrasau/Mures Industrial Park public project, North-West regional/public cloud claims, possible Bistrita environmental filings. Query county councils, Tetarom, industrial park, ADR Nord-Vest, ANMAP.
- **Prahova + South-Muntenia counties (Arges, Calarasi, Dambovita, Giurgiu, Ialomita, Prahova, Teleorman)**: South-Muntenia Regional Data Center led by STS; facility may be in Ploiesti/Prahova while other counties are partners. Avoid duplicate physical counts.
- **Iasi, Bihor, Constanta, Galati, Bacau, Braila, Mehedinti, Harghita, Salaj, Tulcea**: mostly operator/public/research leads. Use local permits/environment to upgrade directory entries.
- **Low-signal counties**: Alba, Botosani, Covasna, Hunedoara, Neamt, Olt, Satu Mare, Suceava, Vaslui, Vrancea and similar need negative searches with Romanian terms plus local authority domains; do not rely on English-only searches.

---

## 4. County query templates

Use these with county/municipality substitutions:

```text
"centru de date" "Alba" "autorizatie de construire"
"centru de date" "Arges" "Centrul de Date Regional Sud-Muntenia"
"centru de date" "Arad" "VLA Energy" "racordare"
"centru de date" "Bucuresti" "Sector 3" "racordare la RED"
"centru de date" "Otopeni" "Microsoft" "certificat de urbanism"
"centru de date" "Tunari" "NXDATA" "autorizatie"
"centru de date" "Bacau" "Rotunda" WhiteHat
"centru de date" "Oradea" HZone "Parcul Industrial"
"centru de date" "Bistrita" "acord de mediu"
"centru de date" "Brasov" STS Cristian "Cloud Privat Guvernamental"
"centru de date" "Cluj" "Liberty Technology Park" GTS
"centru de date" "Luna" "Tetarom V" DriverAI
"centru de date" "Constanta" Orange "panouri solare"
"centru de date" "Mischii" ClusterPower "Transelectrica"
"centru de date" "Galati" Orange "Brailei 41"
"centru de date" "Bacu" Giurgiu Pidgin
"centru de date" "Toplita" "Infinite Chain"
"centru de date" "Miroslava" DataPark
"centru de date" "Drobeta" "DATA ZYX"
"centru de date" "Baia Mare" "Cloud Maramures"
"centru de date" "Vidrasau" "Parcul Industrial Mures"
"centru de date" "Ploiesti" "Centrul de Date Regional Sud-Muntenia"
"centru de date" "Sibiu" STS "CDS II"
"centru de date" "Zalau" Tenaris "modernizeaza"
"centru de date" "Murighiol" DANUBIUS
"centru de date" "Timisoara" SANY "70 MW"
"centru de date" "Alexandria" "Class IT Outsourcing"
"centru de date" "Fauresti" ClusterPower
```

---

## 5. Reliability and counting rules

- **Grade A facility evidence**: operator official facility page; local AC/CU where project title matches a datacenter; ANMAP environmental decision naming a datacenter; SEAP contract/award for datacenter construction/equipment; STS/ADR/government-cloud official page; Uptime/official certification tied to named facility.
- **Grade B facility evidence**: DCD, Profit.ro, Economica, Balkan Green Energy News, Romania Insider, Business Forum, Panorama, DataCenter Forum, local press with named public officials, vendor case studies by contractors such as Tema Energy or Datanet.
- **Grade C leads**: Baxtel, Data Center Map, Datacenters.com, Inflect, DC Hub, ColoMap, DataCenterCatalog, generic market reports. Useful for address/operator seeds but upgrade with official/operator proof where possible.
- **Do not count**: cloud sales offices, software engineering offices, generic hosting companies without facility evidence, telecom POPs unless marketed as data centers, county participation in a regional cloud project unless the county hosts the physical facility, grid/generation projects where the data-center component is only speculative.

