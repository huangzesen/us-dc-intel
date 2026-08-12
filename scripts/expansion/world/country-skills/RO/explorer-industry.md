# RO Explorer Industry - Romania Datacenter Enumeration via Operators, Trade Press, Cloud/Edge, Colo, and County Query Patterns

Date: 2026-08-12. Scope: Romania (RO), 41 counties plus Bucuresti municipality. Focus angle: industry/operator/trade-press discovery that feeds official verification. Reliability grades: **A** = operator-owned current page or official cloud/interconnect page, **B** = established trade press, public-sector trade coverage, association/event source, or vendor case study, **C** = directory/market aggregator/unverified lead.

---

## 0. Romania-specific market frame

- Romania is not just Bucharest colocation. The strongest private cluster is **Bucuresti-Ilfov**, but enumeration must also track government cloud nodes, STS regional projects, energy-linked AI campuses, local hosting facilities, telecom legacy sites, university/research data centers, and public-institution disaster-recovery sites.
- The practical workflow is: **directory/trade/operator lead -> operator page or official cloud page -> city/county permits -> ANMAP environmental record -> SEAP/funding record -> grid/utility context**.
- Local-language search is decisive. Use `centru de date`, `centre de date`, `centru regional de date`, `cloud privat guvernamental`, `centru de procesare date`, `colocare`, `servere`, `racordare`, `grup electrogen`, and operator legal names.
- Treat old Romtelecom/Telekom Romania Communications/NCC Balcan-IX listings carefully. Telekom Romania Communications was acquired by Orange Romania in 2021, so many directory entries are legacy Orange/Telekom aliases rather than separate current operators.
- Equinix should be a negative/market-context check for Romania. Current official Equinix location pages checked did not show a Romania/Bucharest IBX market. Do not count Equinix Romania unless a new official Equinix page or acquisition announcement appears.

---

## 1. Industry, association, and trade-press sources

### 1.1 Romania event / association / market ecosystem

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| DataCenter Forum Romania | https://datacenter-forum.ro/en/home/ | Strong Romanian ecosystem source; sponsor/speaker lists reveal operators, consultants, contractors, energy vendors, and public-sector stakeholders. It has articles on Orange, market growth, power constraints, and national association debate. | B |
| Data Center Nation / DCA-type international event listings | Search `Romania data center forum operators NXDATA ClusterPower Portland Trust` | Useful for current names and panels; verify facility claims elsewhere. | C/B |
| CBRE Romania data-center service page | https://www.cbre.ro/ro-ro/servicii/tipuri-de-proprietati/centre-de-date | Market-advisory context and active real-estate interest; not a facility registry. | C |
| Knight Frank / DC Byte references via trade press | Queries around `Romania 40-45MW data center projects Knight Frank DC Byte` | Useful for anonymous pipeline scale; never count without location/developer or permit. | C/B |
| Panorama.ro analysis | https://panorama.ro/centre-de-date-impact-mediu-digitalizare/ | Good investigative context on public cloud, environmental filings, and utility statements; verify primary records. | B |
| Business Forum / Outsourcing Today / Energynomics | Examples: https://www.businessforum.ro/energy/20240402/romania-could-triple-its-data-center-market-in-three-years-148 , https://outsourcing-today.ro/?p=15336 , https://www.energynomics.ro/ | Useful for market sizing, AI/power themes, and ClusterPower/AIC/DataCenter Forum leads. | B/C |

### 1.2 Trade press to monitor

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Romania data center Bucharest ClusterPower NXDATA SANY Portland` | Best international source for Romanian project announcements: Portland Trust, ClusterPower/AIC, SANY Timis, Orange Timisoara solar, Resita municipal lead. | B |
| Profit.ro | https://www.profit.ro/ ; query `site:profit.ro "centru de date" STS Portland Microsoft` | Strong Romanian IT&C/business source; useful for permits, SEAP bids, STS and private developments. | B |
| Economica.net / Economedia / ZF / Romania Insider | Queries for `ClusterPower`, `Portland Trust`, `Microsoft Otopeni`, `centru de date Bucuresti` | Construction/business leads; verify official permits and operator pages. | B |
| Balkan Green Energy News | https://balkangreenenergynews.com/ ; query `Romania data center SANY DEER AI hub` | Energy-linked data-center projects and grid/power context, especially SANY and utility AI-hub ideas. | B |
| The Tech Capital / Baxtel News | Queries around `ClusterPower 200MW`, `AIC ClusterPower 800MW`, `Romania data center` | Useful international lead generation; verify with operator/official records. | B/C |
| Local press | `radiomures.ro`, `ramnicuvalceaweek.ro`, `graiul.ro`, `radioconstanta.ro`, local city news | Often first source for county council, industrial park, and public project approvals. Grade depends on named officials/docs. | B/C |

### 1.3 Directories and aggregators

| Source | URL | Use | Grade |
|---|---|---|---|
| Baxtel Romania | https://baxtel.com/data-center/romania | Good for current large-project leads and Bucharest map; also includes unverified planned projects. | C+ |
| Data Center Map Romania | https://www.datacentermap.com/romania/ | Good for older colo addresses, Orange/Telekom legacy, local hosters. Coverage/status can lag. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/romania | Useful for Kyndryl/Orange/other commercial listings; free listings may omit power/status. | C |
| Inflect | https://inflect.com/ | Address and carrier clues for Orange/WhiteHat and telecom facilities. Verify. | C+ |
| DC Hub / ColoMap / DataCenterCatalog / DataCenterPlatform | Facility seeds for regional small colo. Use as search pivots, not final proof. | C |
| PeeringDB | https://www.peeringdb.com/ | Active interconnection signal for IX/colo facilities; not complete facility census. | B/C |

---

## 2. Operator and project seed list

Operator pages are **A for self-described facility existence** and usually **B for capacity**, unless formal spec sheets/certifications are published. Directory/trade sources are leads until verified.

### 2.1 Bucuresti and Ilfov

- **NXDATA** - Romania's strongest neutral-colo seed. NXDATA-1 in Bucharest is listed by Google Cloud as Cloud Interconnect facility `NXDATA-1 Bucharest Romania (BU1)`; NXDATA-3 official site https://nxdata3.com locates BUH3 at 38 Bucharest Ring Road, Tunari, Ilfov, with 5 MW installed power and 3 MW IT power, opening target Q4 2026. Search NXDATA, NX-1, NX-3, BUH3, Tunari, ring road, `Google Cloud Interconnect`, `Bucharest Romania BU1`. Grade A/B.
- **GTS Telecom** - official page https://www.gts.ro/ro/data-center-romania says GTS has datacenters in Bucuresti and Cluj-Napoca built to Uptime Institute Tier III/TIA 942 standards; Bucharest is at Electromagnetica Business Park, Calea Rahovei 266-268, with 2 MW maximum installed power and 240 racks; Cluj has 500 kW and 60 racks. Grade A.
- **Voxility** - official page https://www.voxility.com/colocation-bucharest-romania describes Bucharest colocation; existing results identify IR2 on Dimitrie Pompeiu with 1 MW at launch. Search `Voxility IR2 Dimitrie Pompeiu`, `Bucharest colocation AI workloads`. Grade A/B.
- **Orange Romania / Orange Business / ex-Telekom Romania Communications / NCC Balcan-IX** - DataCenter Forum reports Orange owns major commercial data-center infrastructure in Romania, including Bucharest, Brasov, Cluj-Napoca and Timisoara; directories list Bucharest/Drumul Taberei and legacy NCC Balcan-IX sites. Use Orange official pages/press when available and treat old Telekom/Romtelecom as alias history. Grade B/C until official facility page found.
- **Portland Trust** - official page https://www.portlandtrust.cz/en/industrial/data-centers says it acquired three Bucharest sites and one Prague site for datacenter projects in various permitting stages. DCD and Romania Insider report a Bucharest permit for a 4-ha Preciziei-area data center; directories list DC1/Strada Releului and DC2/Bd. Timisoara/Preciziei, with 20-30 MW lead claims. Verify through PMB/Bucharest sector AC/CU registers. Grade B until official project detail/permit captured.
- **Microsoft / Azure** - DCD/Romania Insider reported Microsoft land in Otopeni in 2022, but official Azure geography pages checked did not list Romania. Treat as Ilfov/Otopeni permit-land lead, not an Azure region. Search Microsoft Romania, Otopeni, SPVs, land books, `certificat de urbanism`. Grade C/B until official or permit evidence.
- **Solidus Ai Tech** - Baxtel lists an 8 MW Bucharest carrier-neutral site targeting Q4 2026; needs operator/permit confirmation. Search Solidus, AITECH, Bucharest, `autorizatie de construire`. Grade C.
- **Kyndryl Romania** - directory listing places a Bucharest data center at Soseaua Orhideelor; verify with Kyndryl/operator page or local records. Grade C.
- **M247 / Euroweb / Digi / Vodafone / telecom POPs** - likely network/hosting nodes. Count only if marketed or permitted as datacenter/colo.

Bucuresti-Ilfov templates:

```text
"centru de date" Bucuresti NXDATA GTS Voxility Orange Portland Trust
"NXDATA-3" Tunari "Bucharest Ring Road" "5 MW"
"NXDATA-1" "Google Cloud Interconnect" "BU1"
"GTS Bucuresti" "Calea Rahovei" "2MW"
"Voxility IR2" "Dimitrie Pompeiu" "1 MW"
"Portland Trust" "centru de date" Bucuresti "Preciziei"
"Portland Trust" "Strada Releului" "centru de date"
"Microsoft" Otopeni "centru de date" "certificat de urbanism"
site:urbanism.pmb.ro "centru de date"
site:primarie3.ro "centru de date" OR "racordare la RED centru de date"
site:primariasector6.ro "centru de date" OR "Bd. Timisoara"
site:primariatunari.ro NXDATA OR "centru de date"
site:primariaotopeni.ro Microsoft OR "centru de date"
```

### 2.2 Government cloud, STS, and regional public projects

- **Cloudul Privat Guvernamental** - official ADR page https://adr.gov.ro/cpg states government cloud uses datacenters in Bucuresti, Timisoara/Giroc, Brasov/Cristian, and Sibiu, with two Tier IV and two Tier III by design. Grade A.
- **STS Sibiu / CDS II** - STS official announcement and Uptime Institute awards identify Sibiu. Grade A.
- **Centrul de Date Regional Sud-Muntenia** - ADR Sud-Muntenia and county pages describe an STS-led strategic project with Arges, Calarasi, Dambovita, Giurgiu, Ialomita, Prahova, Teleorman. Existing county pages indicate physical facility/site should be tracked in Prahova/Ploiesti, while partner counties are service beneficiaries. Grade A for project, A/B for exact site depending source.
- **North-West / Bistrita-type regional cloud** - investigative press reports environmental documents for a regional center near Bistrita; verify via ADR Nord-Vest, Bistrita-Nasaud county, and ANMAP. Grade B until official record captured.
- **Research/university/public institutions** - UBB Cluj SEAP, DANUBIUS-RO Murighiol/Tulcea, BNR Targu Jiu, MAI/Police/Academia Tehnica Militara/IGI references. Count as public/HPC/institutional facilities if scope includes non-commercial datacenters; otherwise tag separately.

Public-sector templates:

```text
"Cloudul Privat Guvernamental" "centre de date" Bucuresti Timisoara Brasov Sibiu
site:adr.gov.ro/cpg "centre de date"
site:sts.ro "centru de date" Sibiu OR Brasov OR Timisoara
"Centrul de Date Regional Sud-Muntenia" STS Ploiesti Prahova
site:2021-2027.adrmuntenia.ro "Centrul de Date Regional"
site:e-licitatie.ro "Centrul de Date Regional Sud-Muntenia"
"centru de date regional" "Bistrita" "acord de mediu"
"DANUBIUS-RO" Murighiol "centru de date"
"BNR" "Targu Jiu" "centru de date"
```

### 2.3 Dolj, Valcea, and Southwest energy-linked AI campuses

- **ClusterPower Mischii/Craiova** - Romanian business press reported the 2022 inauguration near Craiova/Mischii as a major AI/hyperscale technology campus with on-site power ambitions. DCD reported in Dec 2025 that AIC and ClusterPower announced an 800 MW AI data-center region across Mischii and Fauresti. Verify with ClusterPower/AIC official material, Dolj/Valcea permits, Transelectrica/Transgaz, and environmental records. Grade B until local official records captured; operator page/case studies can upgrade selected facts.
- **Fauresti / Valcea (FRS1)** - companion site in Valcea per Baxtel/local press/AIC-ClusterPower coverage; capacity and date claims need confirmation. Grade B/C.
- **Tema Energy** - Romanian datacenter contractor; official case studies include ClusterPower and mobile/modular datacenter projects. Use as vendor evidence, not necessarily operator evidence. Grade B.
- **Digital Cuisine Ramnicu Valcea** - operator EU-project page describes a new unit providing data-center services at Str. Gib Mihaescu 31. Grade A for company statement; verify AC/SEAP if needed.

Templates:

```text
"ClusterPower" Mischii Craiova "centru de date"
"ClusterPower" "AIC" "800MW" Romania
"ClusterPower" Fauresti Valcea "data center"
"Mischii" "Transelectrica" "centru de date"
"Mischii" "Transgaz" "centru de date"
site:primariamischii.ro "ClusterPower" OR "centru de date"
site:cjdolj.ro "ClusterPower" OR "centru de date"
site:primariafauresti.ro "centru de date" OR ClusterPower
"Digital Cuisine" "Gib Mihaescu" "centru de date"
```

### 2.4 Timis and western Romania

- **Government cloud Giroc/Timisoara** - ADR page says the Timisoara/Giroc government-cloud datacenter is one of the modern nodes. Verify exact locality through ADR/STS/ANMAP/AC.
- **SANY Timis/Uivar/Timisoara** - DCD, Balkan Green Energy News, and intellinews report a SANY hybrid energy project with a 70 MW datacenter component near Timisoara/Uivar. Treat as planned energy-linked project until official local filings appear. Grade B.
- **Orange Timisoara / NCC Balcan-IX** - DCD reported Orange solar panels on its Timisoara datacenter; directories list Orange Business Timisoara. Grade B/C.
- **Local hosters** - Dataplex Romania/Bunea Telecom, maghost, DDS Hosting, DataNode, ITPS, LiveHosting. Most are directory/operator-page seeds; verify by official pages and local records. Grade B/C.
- **Resita / Caras-Severin** - DCD reported municipal Resita plans; Resita Data site claims grid-adjacent land and ATR in progress. Treat as early planned lead; verify municipality/county/Transelectrica/ANMAP. Grade B/C.

Templates:

```text
"SANY" Timisoara "70 MW" "data center"
"SANY" Uivar "centru de date"
"Orange" Timisoara "data center" "panouri solare"
"DataNode" Timisoara "data center"
"Dataplex Romania" Timisoara "Calea Stan Vidrighin"
"maghost" Timisoara "data center"
"DDS" Timisoara "Strada Arinului"
"Resita Data" "ATR" "Transelectrica"
site:primariatm.ro "centru de date"
site:giroc.ro "centru de date" OR "Cloud Privat Guvernamental"
site:uivar.ro "SANY" OR "centru de date"
site:primaria-resita.ro "centru de date"
```

### 2.5 Cluj, Mures, and central/northwest Romania

- **GTS Cluj-Napoca** - official GTS page gives Liberty Technology Park, Strada Garii 21, 500 kW, 60 racks. Grade A.
- **DriverAI / Luna / Tetarom V** - 2026 press announced an 80 MW "quantum AI" data center in Luna, Cluj; PressOne raised strong caveats about litigation, lack of signed agreement, and operator track record. Treat as announced/speculative until official county/permit/electricity evidence appears. Grade B/C.
- **efect.RO Cluj** - directory listings identify a Cluj-Napoca facility; verify with operator records. Grade C.
- **Mures Industrial Park / Vidrasau** - Radio Mures/Agenda Constructiilor reported a county/industrial-park data center near Vidrasau/Ungheni/Mures with ~240 million lei estimate. Verify county council resolutions, industrial park SA, SEAP, ANMAP. Grade B.
- **TAZ IT Targu Mures** - operator announcement describes an EU/government/company-funded datacenter project. Grade A for company statement.
- **Bistrita-Nasaud regional datacenter** - Panorama says environmental documents were submitted for an 8,500 sqm regional datacenter near Bistrita. Verify through ANMAP and county/ADR. Grade B lead.
- **Bihor / Oradea HZone** - HZone official page says it operates its own datacenter in Oradea, Industrial Park 1 area. Grade A for existence.
- **Salaj / Tenaris Silcotub Zalau** - Datanet Systems says it modernized two Tenaris Silcotub data centers in Zalau. This is enterprise/institutional, not colo. Grade A/B.

Templates:

```text
"GTS Cluj-Napoca" "Strada Garii 21" "500kW"
"Liberty Technology Park" "centru de date" GTS
"DriverAI" Luna Cluj "80MW" "centru de date"
"Tetarom V" Luna "centru de date"
"Vidrasau" "Parcul Industrial Mures" "centru de date"
"TAZ IT" "Targu Mures" "datacenter"
"Bistrita" "centru de date" "8.500" "acord de mediu"
"HZone" Oradea "data center" "Calea Borsului"
"Tenaris Silcotub" Zalau "centrele de date"
```

### 2.6 East, South, and smaller regional colo/public leads

- **Iasi** - DataPark Miroslava official contact page describes its own datacenter at Strada Mihail Kogalniceanu 1; directories list Orange/NCC Balcan-IX Iasi. Grade A for DataPark, C for directory-only Orange until official corroboration.
- **Prahova / Ploiesti** - INVITE Systems official page describes Ploiesti backup/disaster-recovery datacenter; directories list OpticNet. Also likely host county for South-Muntenia Regional Data Center. Grade A/C.
- **Giurgiu** - Pidgin Host official page locates its datacenter in Bacu, Giurgiu County with dual feeds, UPS, diesel generators and carriers. Grade A.
- **Bacau / Braila / Buzau / Mehedinti** - WhiteHat Rotunda, WhiteHat Braila, Zoar Buzau, DATA ZYX Drobeta are mostly directory/PeeringDB/operator seeds; verify locally. Grade C unless operator page is available.
- **Harghita / Toplita** - Infinite Chain Toplita Technology Park appears in Baxtel with high capacity claims; find operator/local permit evidence before counting 50 MW as firm. Grade C/B.
- **Constanta / Galati** - Orange/Telekom legacy and solar-panel/colocation leads; verify with Orange or local records.
- **Tulcea** - DANUBIUS-RO Murighiol research infrastructure includes a data-center component; use research/public project records, not colo directories. Grade B/A depending source.

Templates:

```text
"DataPark" Miroslava "Strada Mihail Kogalniceanu 1" "data center"
"Orange Business" Iasi "NCC Balcan-IX"
"INVITE Systems" Ploiesti "data center" "backup"
"Centrul de Date Regional Sud-Muntenia" Ploiesti Prahova
"Pidgin Host" Bacu Giurgiu "data center"
"WhiteHat" Rotunda Bacau "data center"
"WhiteHat" Braila "Strada Mare 14"
"Zoar Online" Buzau "data center"
"DATA ZYX" Drobeta "data center"
"Infinite Chain" Toplita "technology park"
"Orange" Constanta "data center" "solar"
"Orange" Galati "NCC Balcan-IX"
"DANUBIUS-RO" Murighiol "data center"
```

---

## 3. Cloud, edge, and interconnect interpretation

- **Google Cloud**: official docs list Bucharest as a network edge/interconnect metro and `NXDATA-1 Bucharest Romania (BU1)` as a Cloud Interconnect facility. This is **A** for interconnect presence and an NXDATA seed, not proof of a Google-owned Romanian region.
- **AWS**: official AWS Region and Local Zone pages checked on 2026-08-12 did not list Bucharest/Romania. AWS has Bucharest office/engineering presence, but office presence is not facility evidence. Recheck official pages if a future `Bucharest Local Zone` rumor appears.
- **Azure/Microsoft**: official Azure geography page checked on 2026-08-12 did not list Romania. Microsoft/Otopeni land reports are useful Ilfov permit leads only.
- **Oracle/IBM/Alibaba/others**: treat Romanian offices, partners, or support centers as non-facility signals unless official region, interconnect, or local permit evidence appears.
- **Equinix**: official global locations checked do not show Romania; if directories or stale pages mention Equinix Romania, classify as likely unrelated/stale unless a new Equinix acquisition/IBX page appears.

Cloud/edge queries:

```text
site:docs.cloud.google.com "NXDATA-1 Bucharest Romania"
site:docs.cloud.google.com "Bucharest, Romania" "Cloud Interconnect"
site:aws.amazon.com "Bucharest" "Local Zone"
site:aws.amazon.com "Romania" "AWS Region"
site:azure.microsoft.com "Romania" "Azure region"
site:learn.microsoft.com "Romania" "Azure regions"
site:equinix.com "Romania" "data center" "Bucharest"
```

---

## 4. County-by-county industry sweep plan

Run counties in three passes.

### Pass 1 - high-probability physical facilities or active projects

```text
Bucuresti: NXDATA, GTS, Voxility, Orange, Portland Trust, Solidus, Kyndryl, Microsoft/Otopeni lead, Google Interconnect/NXDATA.
Ilfov: Tunari/NXDATA-3, Otopeni/Microsoft lead, Chiajna CH-Center, Bucharest ring-road spillover.
Dolj: ClusterPower Mischii/Craiova.
Valcea: ClusterPower Fauresti, Digital Cuisine Ramnicu Valcea.
Timis: Giroc government cloud, SANY/Uivar, Orange Timisoara, local Timisoara hosters.
Brasov: government cloud/Cristian, Orange Brasov, DEER modular lead.
Sibiu: STS CDS II, Comway.
Cluj: GTS, DriverAI/Luna, efect.RO, university/public HPC.
Mures: Vidrasau industrial-park project, TAZ IT.
Prahova: INVITE, OpticNet, South-Muntenia regional data-center site.
Iasi: DataPark, Orange Iasi.
Bihor: HZone Oradea.
Giurgiu: Pidgin Host Bacu plus South-Muntenia partner records.
```

### Pass 2 - public/research/enterprise or directory-only leads

```text
Bacau: WhiteHat Rotunda.
Braila: WhiteHat DC2.
Buzau: Zoar and South-East regional financing call.
Caras-Severin: Resita municipal/grid-adjacent lead, Tema Energy mobile datacenter reference.
Constanta: Orange Constanta, port/edge/fiber queries.
Galati: Orange/NCC Balcan-IX Galati.
Gorj: BNR Targu Jiu disaster-recovery lead.
Harghita: Infinite Chain Toplita.
Mehedinti: DATA ZYX Drobeta.
Maramures: Cloud Maramures county project.
Salaj: Tenaris Silcotub Zalau enterprise datacenters.
Tulcea: DANUBIUS-RO Murighiol research hub.
Teleorman: Class IT Outsourcing Alexandria plus South-Muntenia partner.
```

### Pass 3 - negative-control counties

For Alba, Arges, Bistrita-Nasaud, Botosani, Calarasi, Covasna, Dambovita, Hunedoara, Ialomita, Neamt, Olt, Satu Mare, Suceava, Vaslui, Vrancea and any county without a strong lead:

```text
"centru de date" "{county}" "autorizatie"
"centru de date" "{county seat}" "BIP"
"centru de procesare date" "{county seat}"
"camera servere" "{county seat}" "licitatie"
"centru de date" "{county}" "ANMAP"
"centru de date" "{county}" "SEAP"
"data center" "{county seat}" Romania
"colocation" "{county seat}" Romania
"cloud" "{county council}" "centru de date"
```

Do not mark "no projects" after English-only or directory-only searches. Require Romanian local-government and environmental queries.

---

## 5. Alias handling and duplicate controls

- **Orange / Telekom / Romtelecom / NCC Balcan-IX**: normalize facility lineage. A directory listing under Telekom Romania Communications may now belong to Orange Romania after the 2021 acquisition. Do not double-count old and new names at the same address.
- **Bucharest vs Ilfov**: many "Bucharest" market pages are physically in Ilfov localities such as Tunari, Otopeni, Chiajna, Voluntari, or other ring-road municipalities. Assign division by physical address, not market label.
- **South-Muntenia Regional Data Center**: record one physical facility in the host county once confirmed; record partner counties only as beneficiaries/partners if the data model supports non-physical project participation.
- **Government cloud nodes**: Bucuresti, Timis/Giroc, Brasov/Cristian, and Sibiu are separate physical nodes if confirmed by ADR/STS; avoid mixing them with the South-Muntenia regional data center.
- **Energy campuses**: ClusterPower, SANY, VLA Energy, and Resita-style leads may combine generation/BESS/industrial land with datacenters. Count the datacenter component only when named and status can be separated.
- **Directories**: Data Center Map, Baxtel, DC Hub and similar can duplicate facilities under slightly different names. Merge by address, operator, and carrier/IX references.

---

## 6. Upgrade path from lead to verified record

For every industry lead, try to capture at least two independent evidence types:

1. Operator/current owner page or official cloud/interconnect page.
2. Local AC/CU/PUZ/PUD or ANMAP environmental file.
3. SEAP/TED tender, public financing contract, or county council resolution.
4. Power/grid evidence: ATR, DSO/TSO reference, substation, requested MW.
5. Trade press only for timing, capacity, and pipeline context when official records are absent.

Suggested output fields:

```text
name
division
municipality/locality
physical_address
developer/operator/current_owner
legacy_operator_aliases
status
capacity_mw
power_source_or_grid_connection
source_urls
evidence_grade
evidence_date
notes
needs_official_permit_check
```

