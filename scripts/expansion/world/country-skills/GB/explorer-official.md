# GB Explorer Official — UK Datacenter Enumeration via Planning, Grid, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Scope: United Kingdom of Great Britain and Northern Ireland (GB/UK), 185 repo divisions covering nations, regions, counties, boroughs, and unitary authorities. Angle: **official/regulatory/cloud pipeline**. Reliability grades: **A** = official/primary source (planning register, DCO/NSIP, government/regulator, operator official page, cloud region docs), **B** = strong secondary/trade press or specialist directories with named sources, **C** = weak/aggregate/marketing-only or unverified community source.

---

## 0. UK-specific structural facts

- The UK has **no single complete national planning-register search for datacentres**. Facility enumeration is primarily a **local planning authority (LPA) exercise**: each council planning register has its own Idox/Uniform/Public Access/Agile UI and document store. England has some central helpers, but the application documents and decisions usually remain at council level.
- Large projects may now also surface through the **NSIP/DCO route**. Government written statement HCWS966 (2025-10-15) says data centres are prescribed projects capable of being directed into the NSIP consenting regime under Planning Act 2008 section 35. Treat the Planning Inspectorate/National Infrastructure Planning record as Grade A for projects that enter this route.
- Power is often the gating item. Demand connection queues are not as transparent as generation registers, but Ofgem, NESO, National Grid Electricity Transmission, DNO open-data portals, substation planning applications, and environmental permits can expose MW, grid-connection dates, or feasibility.
- Since September 2024 UK data centres have been designated **Critical National Infrastructure**. The Cyber Security and Resilience Bill factsheet says qualifying data-centre operators will have notification/security/resilience duties, with Ofcom expected as operational regulator. This is a future operator-registry lead, not yet a public facility census.
- Cloud regions are good **metro seeds**, not exact facility evidence. AWS, Azure, Google Cloud, OCI and others disclose UK regions/AZs but not physical addresses. Use cloud pages to seed likely metros (London/Slough/Hayes/Harlow/Hemel/Cardiff/Newport) and then confirm through planning/operator evidence.

---

## 1. Grade A official portals and how to use them

### 1.1 England local planning backbone

- **GOV.UK planning-register finder**: https://www.gov.uk/search-register-planning-decisions. Enter a postcode to identify the relevant council planning register. Use when the division is ambiguous or a project address is known.
- **Planning Portal LPA finder**: https://www.planningportal.co.uk/find-your-local-planning-authority. Search by LPA name or postcode; useful for routing repo divisions to the correct council.
- **Planning.data.gov.uk**: https://www.planning.data.gov.uk/ and API docs https://www.planning.data.gov.uk/docs. It provides planning/housing datasets for England and is improving application data coverage, but do not assume completeness for datacentres. Use as an index/map helper; confirm in the LPA register.
- **Greater London Planning Datahub**: https://planninglondondatahub.london.gov.uk/ and GLA explainer https://www.london.gov.uk/programmes-strategies/planning/digital-planning/planning-london-datahub. Grade A/B+ London-wide discovery feed; then open the borough register for plans, decision notices, energy statements, EIA screening, and committee reports.

Common LPA register keyword searches:
```
"data centre"
"data center"
"datacentre"
"data hall"
"server hall"
"critical infrastructure"
"digital infrastructure"
"hyperscale"
"co-location" OR "colocation"
"substation" "data centre"
"standby generators" "data centre"
"diesel generators" "data centre"
"battery energy storage" "data centre"
"Class B8" "data centre"
"Use Class E(g)(ii)" "data centre"
```

Status terms in planning registers:
```
EIA screening opinion
EIA scoping opinion
hybrid planning application
outline planning permission
reserved matters
full planning application
discharge of conditions
non-material amendment
section 73 variation
prior approval
committee report
decision notice
construction management plan
```

Data to extract from planning packs: application reference, address, applicant/SPV, floorspace sqm, number of data halls/buildings, IT load MW, utility import/MVA, backup generator count and rating, substation/grid connection, construction phasing, target energisation, EIA status, decision date, and appeal/DCO route if applicable.

### 1.2 Planning Inspectorate, appeals, and DCO/NSIP

- **Planning Inspectorate organisation page**: https://www.gov.uk/government/organisations/planning-inspectorate.
- **National Infrastructure Planning / Find a project**: start via Planning Inspectorate links or https://national-infrastructure-consenting.planninginspectorate.gov.uk/. Search `data centre`, applicant, county, and known campus names.
- **NSIP process guidance**: https://www.gov.uk/guidance/nationally-significant-infrastructure-projects-and-the-people-and-organisations-involved-in-the-process.
- **Data centre NSIP statement**: https://questions-statements.parliament.uk/written-statements/detail/2025-10-15/hcws966.
- **Planning appeals/call-ins**: use the Planning Inspectorate appeal/casework services and GOV.UK statements. UK datacentre projects can be decided by the Secretary of State after local refusal/call-in; treat decision letters and inspectors' reports as Grade A.

NSIP/DCO query templates:
```
site:national-infrastructure-consenting.planninginspectorate.gov.uk "data centre"
site:infrastructure.planninginspectorate.gov.uk "data centre"
site:gov.uk "section 35" "data centre"
site:gov.uk "Development Consent Order" "data centre"
site:questions-statements.parliament.uk "data centres" "National Infrastructure Planning"
```

### 1.3 Scotland, Wales, Northern Ireland planning

- **Scotland ePlanning**: https://www.eplanning.scot/ for submissions; local registers remain council-specific. Use council Public Access portals for searches and the **DPEA case search** for appeals/called-in cases: https://www.dpea.scotland.gov.uk/. DPEA case pages can contain data-centre proposals, application references, and decisions.
- **Wales Planning Portal / Planning Applications Wales**: https://www.planningportal.co.uk/wales/applications and https://planningportal.wales/app/landing-page. Local authority registers hold the public file. Also search Welsh Government decisions and DNS/major infrastructure changes: https://www.gov.wales/.
- **Northern Ireland Planning Portal**: https://planningregister.planningsystemni.gov.uk/simple-search and guidance at https://www.infrastructure-ni.gov.uk/articles/new-planning-portal. This is the central public register for Northern Ireland applications; search all NI councils directly here.

Nation-specific queries:
```
site:gov.scot "data centre" planning
site:dpea.scotland.gov.uk "Data Centre"
site:gov.wales "data centre" planning
site:planningregister.planningsystemni.gov.uk "data centre"
site:infrastructure-ni.gov.uk "data centre" planning
```

---

## 2. Power/grid and environmental evidence

### 2.1 Grid and energy sources

- **Ofgem data-centre connection reforms**: https://www.ofgem.gov.uk/consultation/proposed-data-centre-connection-reforms and press release https://www.ofgem.gov.uk/press-release/ofgem-acts-free-grid-capacity-tackling-speculative-data-centre-projects. Grade A for regulatory context; not a project census unless attachments list schemes.
- **NESO Data Portal**: https://www.neso.energy/data-portal. Use for system datasets and connections reform results: https://www.neso.energy/industry-information/connections-reform/connections-reform-results.
- **NESO TEC register**: https://www.neso.energy/data-portal/transmission-entry-capacity-tec-register and data file https://www.neso.energy/data-portal/transmission-entry-capacity-tec-register/tec_register. Primarily generation/transmission projects, not a complete demand queue; useful for colocated generation, grid reinforcements, or named substations.
- **Energy Networks Association connections data**: https://www.energynetworks.org/industry/connecting-to-the-networks/connections-data. Route to DNO open-data portals.
- DNO open data/high-value pages: UK Power Networks open data https://ukpowernetworks.opendatasoft.com/, National Grid DSO data centre page https://dso.nationalgrid.co.uk/resource-centre/data-centre, SSEN embedded register https://www.ssen.co.uk/our-services/tools-and-maps/embedded-capacity-register/, SP Energy Networks ECR https://www.spenergynetworks.co.uk/pages/embedded_capacity_register.aspx, Electricity North West ECR https://www.enwl.co.uk/Get-connected/network-information/Embedded-Capacity-Register/.

Power-query templates:
```
"{project/campus}" "MVA"
"{project/campus}" "MW" "grid connection"
"{project/campus}" "substation"
"{council}" "data centre" "132kV"
"{council}" "data centre" "National Grid"
"{council}" "data centre" "UK Power Networks"
"{council}" "data centre" "SSE" OR "SSEN" OR "SP Energy Networks"
site:ofgem.gov.uk "data centre" "connections queue"
site:neso.energy "data centre" "connections"
```

### 2.2 Environmental permits and planning documents

Large UK datacentres may have backup generator farms that trigger air-quality/environmental permitting evidence. Search Environment Agency/SEPA/NRW/NIEA and council documents:
```
"{project}" "environmental permit" "data centre"
"{project}" "Part B permit" generators
"{project}" "air quality assessment" "data centre"
"{project}" "noise assessment" "data centre"
"{project}" "energy statement" "data centre"
"{project}" "EIA screening" "data centre"
"{project}" "generator" "MW" "planning"
```

Grade these as A when the document is a council/government-hosted application document, permit, committee report, or decision notice. Trade press summaries of those documents are B unless the primary PDF is linked and checked.

---

## 3. Official cloud and operator seed lists

### 3.1 Hyperscale cloud regions (Grade A for region existence only)

| Provider | Official page | UK region signal | How to use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | `eu-west-2`, Europe (London), 3 AZs | Seed London/West London/Thames Valley searches; do not infer exact buildings. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://datacenters.microsoft.com/globe/ | UK South = London; UK West = Cardiff | Search Microsoft local project pages and LPAs around London, Eggborough/North Yorkshire, Newport/Cardiff. |
| Google Cloud | https://cloud.google.com/about/locations and Compute docs https://docs.cloud.google.com/compute/docs/regions-zones | `europe-west2` London, 3 zones | Seed London region; verify expansions via planning/local government. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | UK South (London), UK West (Newport/Cardiff); UK sovereign regions also London/Newport | Good Wales/Newport/Cardiff seed; facility location still hidden. |

Also check IBM Cloud, OVHcloud, Alibaba Cloud, Huawei Cloud, Salesforce/Workday/SAP regional pages when a named project or tenant appears, but treat cloud-region references as metro-level leads only.

### 3.2 Colo/operator official pages (Grade A for existence; capacity may be A-/B)

Priority UK operators and official pages:

| Operator | Official URL | High-yield metros/divisions |
|---|---|---|
| Equinix | UK https://www.equinix.com/data-centers/europe-colocation/united-kingdom-colocation; London https://www.equinix.com/data-centers/europe-colocation/united-kingdom-colocation/london-data-centers | Greater London, Slough, Manchester |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/london | London Docklands, City/West London, Slough/Thames Valley |
| Ark Data Centres | https://www.ark-d-c.com/ | Corsham/Wiltshire, Farnborough/Hampshire, Enfield, Acton, Longcross/Surrey |
| Kao Data | https://kaodata.com/locations/harlow/ and https://kaodata.com/about/ | Harlow/Essex, Slough, Northolt, Greater Manchester plan |
| VIRTUS | https://virtusdatacentres.com/locations and https://virtusdatacentres.com/ | Stockley Park/Hillingdon, Slough, Saunderton/Buckinghamshire, Hayes, Enfield |
| Telehouse | https://www.telehouse.net/data-centre-services/uk/london/ | London Docklands/Tower Hamlets, Blackwall |
| NTT Global Data Centers | e.g. https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/hemel-hempstead-4-data-center | Hemel Hempstead/Hertfordshire, Slough, Dagenham |
| Colt DCS | https://www.coltdatacentres.net/en-GB/our-locations/data-centre-locations-europe/london-4 | Hayes/Hillingdon; use LPA documents for expansions. |
| Yondr | https://www.yondrgroup.com/ | Slough/London campus |
| CyrusOne | https://cyrusone.com/locations/europe/ | Slough, London, future UK campus announcements |
| Pulsant | https://www.pulsant.com/colocation | Regional edge sites: Reading, Rotherham, Edinburgh, Newcastle, Manchester, Maidenhead, Croydon etc. |
| iomart | https://www.iomart.com/our-data-centres/ | Glasgow, Edinburgh, Manchester, Nottingham, London, Maidenhead |
| nLighten / Proximity | https://nlighten.eu/ and https://www.proximitydatacentres.com/ legacy | Edge facilities across English regions. |
| Stellium | https://stelliumdc.com/ | Cobalt Park/North Tyneside |

Operator-page workflow:
1. Record official facility/campus name and metro.
2. Search exact facility name plus council/LPA for planning references.
3. Search company/SPV name in Companies House: https://find-and-update.company-information.service.gov.uk/.
4. For public companies/REITs, check annual reports/investor decks for MW/lease status; use operator marketing capacity cautiously.

---

## 4. Query playbook

### 4.1 Discovery queries

Use Google/Bing with UK spelling variants:
```
"{division}" "data centre" planning
"{division}" "data center" planning
"{division}" datacentre
"{division}" "data hall"
"{division}" "hyperscale" "data centre"
"{division}" "digital infrastructure" "planning application"
"{division}" "AI data centre"
"{division}" "cloud region" "data centre"
"{division}" "substation" "data centre"
"{division}" "standby generators" "data centre"
```

Council-scoped:
```
site:{council-domain} "data centre"
site:{council-domain} "data center"
site:{council-domain} "datacentre"
site:{council-domain} "EIA screening" "data centre"
site:{council-domain} "committee report" "data centre"
site:{council-domain} "reserved matters" "data centre"
site:{council-domain} "planning application" "data centre" "MW"
```

Document-focused:
```
filetype:pdf "data centre" "Design and Access Statement" "{division}"
filetype:pdf "data centre" "Planning Statement" "{division}"
filetype:pdf "data centre" "Energy Statement" "{division}"
filetype:pdf "data centre" "Air Quality Assessment" "{division}"
filetype:pdf "data centre" "Noise Assessment" "{division}"
filetype:pdf "data centre" "Environmental Statement" "{division}"
```

### 4.2 Capacity extraction queries

```
"{project}" "IT load"
"{project}" "ITE load"
"{project}" "MW IT"
"{project}" "MVA"
"{project}" "power capacity"
"{project}" "data halls"
"{project}" "white space"
"{project}" "technical space"
"{project}" "generators"
"{project}" "132kV"
"{project}" "33kV"
```

Use hierarchy: council decision/application docs > operator official datasheet > listed-company/investor disclosure > trade press citing documents > directories.

---

## 5. Division enumeration strategy for 185 GB divisions

### 5.1 Always start by mapping division to LPA/search register

For each repo division:
1. Split nation prefix (`England -`, `Scotland -`, `Wales -`, `Northern Ireland -`) from authority/county name.
2. Search Planning Portal/GOV.UK by authority name; if the repo division is a county with districts, identify all lower-tier LPAs (e.g. Essex includes Harlow, Basildon, Chelmsford, Thurrock/Southend as separate unitaries where applicable).
3. Run LPA register keyword search for `data centre`, `datacentre`, `data center`, `data hall`, and `substation`.
4. Search web with `site:{council-domain}` templates and PDF templates.
5. Cross-check operator seed lists and known campus aliases.
6. Extract planning reference(s); do not rely on a news article without opening the council planning documents where available.

### 5.2 High-yield division clusters

- **Greater London and boroughs**: use GLA Planning Datahub plus borough registers. Focus Tower Hamlets/Docklands, Hillingdon/Hayes/Stockley Park, Ealing/Acton, Enfield, Brent/Park Royal, Hounslow, Dagenham/Barking, Croydon, Northolt/Ealing, Blackwall.
- **Slough / Berkshire / Thames Valley**: Slough Borough Council, Reading, Royal Borough of Windsor and Maidenhead, Wokingham, Bracknell Forest. Search Equinix, Yondr, CyrusOne, VIRTUS, SEGRO, GTR, Digital Realty, Microsoft, Oracle.
- **Hertfordshire / Buckinghamshire / Oxfordshire**: Hemel Hempstead/Dacorum, Watford, Iver/South Bucks, Saunderton, Bicester/Graven Hill, Faringdon. Search NTT, Greystoke, VIRTUS, major AI campus terms.
- **Essex / Harlow / Cambridge corridor**: Kao Harlow, Stansted/M11 corridor, Uttlesford/Harlow/Epping Forest. Search `Kao`, `Harlow campus`, `Nvidia Cambridge-1`, `London Road Harlow`.
- **North East / power-station redevelopment**: Northumberland/Cambois/Blyth, North Tyneside/Cobalt Park, Redcar and Cleveland/Teesworks. Planning and local economic-development pages are high-value; power and grid evidence is essential.
- **Yorkshire and East Midlands power sites**: North Yorkshire/Eggborough/Selby/Drax, Nottinghamshire/Cottam/Ratcliffe/Rufford, Lincolnshire and former industrial/power-station sites. Search former power station + data centre.
- **Wales**: Cardiff/Newport/UK West cloud signal, Bridgend/Neath Port Talbot, Wrexham. Use local registers and Welsh Government planning pages; search Oracle/Microsoft region evidence only as metro seed.
- **Scotland**: use each council register plus DPEA. Emerging hyperscale proposals may be power-led and rural; search `data centre wind farm`, `AI data centre`, `hyperscale`, `substation`, `renewable powered data centre`.
- **Northern Ireland**: central NI Planning Portal keyword sweep by council; expect fewer hyperscale facilities, but search `Belfast data centre`, `Lisburn`, `Craigavon`, `Derry/Londonderry`, `colocation`.

### 5.3 Low-yield/no-project handling

For rural authorities and islands, still run:
```
"{division}" "data centre"
"{division}" "datacentre"
"{division}" "colocation"
"{division}" "server room" "planning"
site:{council-domain} "data centre"
```
If no facility-grade evidence appears, output `no_projects: true`. Do not count ordinary office server rooms, telecom cabinets, exchange buildings, or university/Hospital IT-room refurbishments unless they are purpose-built data-centre facilities and the source supports that status.

---

## 6. Reliability grading and status rules

### 6.1 Evidence grades

| Source/data point | Grade |
|---|---|
| Council planning register application, committee report, decision notice, EIA screening/scoping, approved plans | A |
| Planning Inspectorate NSIP/DCO project page, Secretary of State decision letter, appeal inspector report | A |
| Ofgem/NESO/government consultation or policy documents naming project/context | A for regulatory fact; project grade only if project is named |
| Cloud provider official region docs | A for region existence; C for exact physical location unless separately confirmed |
| Operator official facility page/datasheet | A for existence; A-/B for capacity depending on specificity |
| Listed company annual report/investor deck | A for disclosed capacity/status |
| Trade press (DCD, Computer Weekly, Data Centre Magazine, Construction Enquirer, Place North West/Place Yorkshire etc.) | B, upgrade only when it links to checked primary planning documents |
| DataCenterMap, Baxtel, DC Atlas, Colo-X, OCOLO | B/C depending on detail; useful as discovery and capacity hints, not final proof for major projects |
| Local campaign maps, LinkedIn posts, PR-only announcements, consultant blogs | C unless they link to primary records |

### 6.2 Status normalization

- `announced`: press release, MoU, AI Growth Zone, land option, consultation website, no planning application yet.
- `planned`: EIA screening/scoping or submitted planning application, not yet approved.
- `approved`: planning permission/DCO granted, conditions/reserved matters may remain.
- `construction`: discharge of conditions, construction management plan, building-control/EPC evidence, operator says under construction, or reliable construction report.
- `operational`: operator official facility live, cloud/colo service page, commissioning/go-live announcement, or planning completion evidence.
- `rejected/cancelled`: refusal notice, appeal dismissal, withdrawn application, operator cancellation, or lapsed permission.

Only count full far-future campus MW when source explicitly says it is planned capacity; otherwise record phase MW and mention possible ultimate expansion in notes.

---

## 7. Practical UK pitfalls

- **Spelling variants matter**: UK sources use `data centre`, US vendors often use `data center`, and older sources use `datacentre`.
- **Same campus, many names**: a site may appear under operator, landlord, SPV, industrial estate, road name, and LPA reference. Deduplicate by address/campus and phase.
- **Planning use-class ambiguity**: applicants sometimes describe datacentres as warehousing/light industrial, `Class B8`, `E(g)(ii)`, or sui generis. Keyword search on generators/substations catches hidden cases.
- **Cloud region does not equal a facility**: never assign AWS/Azure/GCP/OCI to an address unless planning/operator evidence proves it.
- **Demand-queue numbers can be speculative**: Ofgem is explicitly targeting speculative data-centre grid applications. Treat grid-queue claims as leads unless backed by land/planning milestones.
- **Operator marketing capacity can be ultimate design load**: planning documents often separate utility import, gross electrical load, generator capacity, and IT load. Prefer IT/ITE load for `capacity_mw`.
- **Do not double count London metro**: Slough, Hayes, Harlow, Hemel Hempstead, Northolt, Enfield, Dagenham, Docklands and Reading are often marketed as "London" but belong to different repo divisions.

---

## 8. Recommended official-first workflow

1. For each of 185 divisions, resolve exact LPA/council planning register(s).
2. Run LPA keyword search for `data centre/datacentre/data center/data hall/hyperscale/substation/generators`.
3. Search council domain and PDFs with the templates above; capture application references and decision documents.
4. Check Planning Inspectorate/National Infrastructure Planning for section 35/DCO cases and appeals/call-ins.
5. Cross-check grid/power evidence: Ofgem/NESO context, DNO open data, planning energy statements, substations, environmental permit documents.
6. Seed with cloud and colo official pages, then pivot each operator/campus name back into planning records.
7. Use trade press/directories only to discover or fill gaps; final evidence grade should reflect the strongest checked source.
8. Output records in world schema: `{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`. Include planning reference in notes whenever found.
