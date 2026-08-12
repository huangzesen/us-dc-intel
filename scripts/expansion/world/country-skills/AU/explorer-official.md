# AU Explorer Official - Australia Datacenter Enumeration via Planning, Energy, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Country: **AU Australia**. Division model in the world manifest: **local government areas grouped by state / territory**. Angle: **official / regulatory / cloud pipeline** with emphasis on Australian planning permits, AEMO / network energy evidence, official cloud-region pages, official colo operator footprints, and ACMA spectrum records.

Reliability grades:
- **A** = primary / official / legally accountable source: state planning portal, local council DA register, state significant development record, government / regulator / AEMO / network document, official cloud-region page, official operator facility page, ASX filing or annual report.
- **B** = strong secondary source: trade press, specialist data-centre press, planner / contractor case study that names a DA or project, reputable local press citing planning files.
- **C** = weak lead: directories, unsourced maps, job ads, generic marketing, community posts, or press articles with no primary approval trail.

---

## 0. Australia-Specific Structural Facts

- Australia has **no national public datacentre registry**. Enumeration is mainly a planning-approval exercise across state significant-development portals and hundreds of local council DA registers.
- The repo divisions are LGAs, so every project must be bucketed to the correct council / shire / city, even when the first source is a state portal, operator page, or energy document.
- NSW and Victoria are currently the highest-yield official planning sources. NSW Planning Portal major projects exposes many data-centre SSD records with MW, application number, LGA, status, documents, and agency submissions. Victoria's Ministerial Permits Register exposes fast-track Clause 53.22 / utility-installation data-centre permits and decisions.
- AEMO and electricity network sources are critical because hyperscale campuses often appear as large-load connection, substation, transmission, or demand-forecast evidence before full public facility disclosure. Treat energy sources as **A** for power / grid facts, but do not infer a datacentre unless the source names datacentres, the operator, or a matching planning application.
- Cloud regions and availability zones are **A-grade proof of a provider's regional market presence**, not exact building evidence. Use them as metro seeds for Sydney, Melbourne, Canberra, and Brisbane/Perth/Adelaide edge searches.
- Australian spelling uses `data centre`, but `data center` appears in cloud/operator material. Always search both.

---

## 1. Grade A Planning and Development Portals

### 1.1 New South Wales

Primary sources:
- NSW Planning Portal major projects search: https://www.planningportal.nsw.gov.au/major-projects/projects
- Example SSD record, Project Mars Data Centre: https://www.planningportal.nsw.gov.au/major-projects/projects/project-mars-data-centre
- Example SSD record, Marsden Park Data Centre: https://www.planningportal.nsw.gov.au/major-projects/projects/marsden-park-data-centre
- Example SSD record, STACK SYD01 Data Centre, Erskine Park: https://www.planningportal.nsw.gov.au/major-projects/projects/stack-syd01-data-centre-erskine-park

Workflow:
1. Search the major projects portal for `data centre`, `data center`, `data storage`, `data hall`, `server`, `hyperscale`, and known operator names.
2. Open every SSD page and extract application number, status, LGA, address, applicant / proponent, development type, capacity MW / MVA, GFA, substation details, determination date, and attachments.
3. Download or open planning PDFs where possible: EIS, planning statement, architectural plans, ESD report, electrical infrastructure report, water / wastewater, air quality, noise, and agency submissions.
4. Cross-check the LGA council DA tracker for related works, early works, subdivision, road works, modification applications, or local approvals below SSD threshold.

High-yield NSW LGAs / clusters:
- Western Sydney: Penrith, Blacktown, Cumberland, Parramatta, Liverpool, Fairfield, Camden, Campbelltown, The Hills. Search `Eastern Creek`, `Erskine Park`, `Marsden Park`, `Horsley Park`, `Kemps Creek`, `Greystanes`, `Guildford West`, `Macquarie Park`.
- Inner / North Sydney: Sydney, Ryde, Willoughby, North Sydney, Lane Cove. Search `Alexandria`, `Ultimo`, `Artarmon`, `Macquarie Park`, `Lane Cove West`.
- Regional / industrial leads: Newcastle, Wollongong, Central Coast, Dubbo, Wagga Wagga, Port Macquarie-Hastings. Use council DA registers plus local economic-development pages.

NSW query templates:
```
site:planningportal.nsw.gov.au/major-projects/projects "data centre" "MW"
site:planningportal.nsw.gov.au/major-projects/projects "data storage" "Local Government Areas"
site:planningportal.nsw.gov.au/major-projects/projects "{operator}" "Data Centre"
"{NSW LGA}" "data centre" "development application"
"{suburb}" "data centre" "SSD"
"{project}" "SSD-" "data centre"
```

### 1.2 Victoria

Primary sources:
- Planning Victoria ministerial permits search / register: https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register
- Example ministerial permit PA2403014: https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register/ministerial-permits/2b5ec06b-0b35-ef11-8e4e-002248969b00
- Example ministerial permit PA2504019: https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register/ministerial-permits/76685df6-baaf-f011-bbd2-6045bdc32df2
- Example ministerial permit PA2403452: https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register/ministerial-permits/1ea17bd8-75be-ef11-b8e8-002248938a9c

Workflow:
1. Search the ministerial permits register for `data centre`, `data center`, `utility installation`, `53.22`, operator names, and power terms like `MVA`.
2. Capture planning permit ID, responsible authority / LGA, address, application received date, public notice date, decision, decision date, proposal text, and linked documents.
3. Pivot to the local council register for amendments, construction management plans, complaints, secondary permits, and delegated reports.
4. Search Victorian Government investment pages for official announcements, but use them as project-context unless they link to approvals.

High-yield Victoria LGAs / clusters:
- Melbourne west and north: Hume, Hobsons Bay, Maribyrnong, Brimbank, Wyndham, Melton, Whittlesea, Merri-bek. Search `Tullamarine`, `Craigieburn`, `West Footscray`, `Brooklyn`, `Laverton North`, `Spotswood`, `Campbellfield`, `Plumpton`.
- Inner / port / enterprise: Melbourne, Port Phillip, Yarra, Monash, Greater Dandenong, Kingston.
- Regional edge / growth: Greater Geelong, Wodonga, Ballarat, Bendigo, Shepparton, Horsham.

Victoria query templates:
```
site:planning.vic.gov.au/planning-approvals/ministerial-permits-register/ministerial-permits "data centre"
site:planning.vic.gov.au/planning-approvals/ministerial-permits-register/ministerial-permits "53.22" "Data Centre"
site:planning.vic.gov.au "Utility Installation (Data Centre)"
"{Victorian LGA}" "data centre" "planning permit"
"{suburb}" "data centre" "MVA"
```

### 1.3 Queensland

Primary sources:
- Queensland planning online services landing page: https://www.planning.qld.gov.au/planning-framework/planning-online-services
- State Assessment and Referral Agency / development assessment guidance: https://www.planning.qld.gov.au/planning-framework/development-assessment
- Economic Development Queensland applications and approvals: https://www.edq.qld.gov.au/applications-approvals/
- Brisbane Development.i: https://developmenti.brisbane.qld.gov.au/
- Gold Coast Development.i: https://www.goldcoast.qld.gov.au/Planning-building/Find-development-applications

Workflow:
1. For Brisbane / Gold Coast / Sunshine Coast / Moreton Bay / Ipswich / Logan / Redland, start with the council DA register. Brisbane and Gold Coast have Development.i interfaces.
2. Check EDQ if the site is inside a Priority Development Area.
3. Check SARA / state referral material for projects involving state transport corridors, high-voltage infrastructure, coastal matters, airports, or major hazards.
4. Cross-check Powerlink / Energex / Ergon evidence for substation and high-load connections.

Queensland query templates:
```
"{Queensland LGA}" "data centre" "development application"
"{Queensland LGA}" "data center" "material change of use"
"{suburb}" "data centre" "Development.i"
site:developmenti.brisbane.qld.gov.au "data centre"
site:edq.qld.gov.au "data centre"
site:planning.qld.gov.au "data centre" "SARA"
```

### 1.4 Western Australia

Primary sources:
- WA Planning Online portal: https://planningonline.dplh.wa.gov.au/
- WA significant development applications: https://www.planning.wa.gov.au/significant-development-pathway/significant-development-applications
- Development Assessment Panels information: https://www.wa.gov.au/organisation/department-of-planning-lands-and-heritage/development-assessment-panels

Workflow:
1. Search WA Planning Online and the significant development pathway for high-value data-centre DAs.
2. Search Development Assessment Panel agendas / minutes for `data centre`, `data center`, `technology`, `utility`, `substation`, and operator names.
3. Pivot to local councils for exact LGA records: Perth, Canning, Gosnells, Armadale, Belmont, Swan, Kwinana, Rockingham, Stirling, Joondalup, Mandurah, Karratha, Port Hedland.
4. Cross-check Western Power and Horizon Power documents for power supply, substation, and large-customer works.

WA query templates:
```
site:planning.wa.gov.au "data centre"
site:planningonline.dplh.wa.gov.au "data centre"
site:wa.gov.au "Development Assessment Panel" "data centre"
"{WA LGA}" "data centre" "development application"
"{suburb}" "data centre" "DAP"
```

### 1.5 South Australia

Primary sources:
- PlanSA development applications: https://plan.sa.gov.au/development_applications
- PlanSA planning and development system: https://plan.sa.gov.au/
- SA Government investment / industry pages: https://www.invest.sa.gov.au/

Workflow:
1. Search PlanSA for `data centre`, `data center`, `AI factory`, `server farm`, `battery`, `substation`, `utility`, `hyperscale`, and named developers.
2. For Adelaide metro facilities, search City of Adelaide plus neighbouring council registers and operator pages.
3. For large energy-led campuses, pivot through ElectraNet, SA Power Networks, renewable-energy project material, and local council consultation.

High-yield SA LGAs / clusters:
- Adelaide, Port Adelaide Enfield, West Torrens, Charles Sturt, Salisbury.
- Coorong / Tailem Bend and Murraylands energy-led projects.
- Goyder / Bundey and other transmission-adjacent rural proposals.

SA query templates:
```
site:plan.sa.gov.au "data centre"
site:plan.sa.gov.au "AI factory"
"{SA LGA}" "data centre" "development application"
"{project}" "ElectraNet" "data centre"
"{suburb}" "data centre" "PlanSA"
```

### 1.6 Tasmania

Primary sources:
- PlanBuild Tasmania: https://www.planbuild.tas.gov.au/
- Tasmanian Planning Commission: https://www.planning.tas.gov.au/

Workflow:
1. Use PlanBuild to identify the responsible council and planning scheme constraints.
2. Search council DA registers for Hobart, Glenorchy, Clarence, Launceston, Devonport, Burnie, George Town, Northern Midlands, and industrial / energy corridors.
3. Cross-check TasNetworks and renewable / hydro-powered computing proposals.

Tasmania query templates:
```
site:planbuild.tas.gov.au "data centre"
site:planning.tas.gov.au "data centre"
"{Tasmania LGA}" "data centre" "planning"
"{suburb}" "server farm" Tasmania
```

### 1.7 Northern Territory

Primary sources:
- NT Development Applications Online: https://www.ntlis.nt.gov.au/planning/lta.dar.list
- NT Planning Commission: https://planningcommission.nt.gov.au/
- Development Consent Authority: https://dipl.nt.gov.au/lands-and-planning/development-assessment-services/development-consent-authority

Workflow:
1. Search NT Development Applications Online for `data centre`, `data center`, `server`, `technology park`, `AI`, `power station`, and known proposals.
2. Check Darwin, Palmerston, Litchfield, Darwin Waterfront Precinct, and Weddell / Cox Peninsula / Middle Arm-adjacent planning and energy material.
3. Cross-check Power and Water Corporation, Territory Generation, and NT Government energy-hub pages.

NT query templates:
```
site:ntlis.nt.gov.au/planning "data centre"
site:planningcommission.nt.gov.au "data centre"
site:nt.gov.au "data centre" "development application"
"Weddell" "data centre" "Northern Territory"
"Darwin" "AI data centre" "planning"
```

### 1.8 Australian Capital Territory and Commonwealth Government Context

The current manifest line does not expose ACT LGAs, but ACT / Canberra is a key Australian datacentre market because of federal-government workloads.

Primary sources:
- ACT Planning: https://www.planning.act.gov.au/
- ACT development application search: https://www.planning.act.gov.au/development-applications-assessments/development-applications
- Digital Transformation Agency Hosting Certification Framework: https://www.dta.gov.au/help-and-advice/technology/hosting

Use ACT / Commonwealth evidence to seed operators with Canberra campuses, then map to the repo model only if the parent later adds ACT divisions or if a record must be retained as national context.

---

## 2. Energy, Grid, and Environmental Evidence

### 2.1 AEMO and Market-Wide Sources

Primary sources:
- AEMO homepage / publications: https://aemo.com.au/
- AEMO digital demand surge article on data centres: https://www.aemo.com.au/newsroom/news-updates/digital-demand-surge
- AEMO forecasting and planning publications: https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/nem-forecasting-and-planning
- AEMO Integrated System Plan: https://aemo.com.au/energy-systems/major-publications/integrated-system-plan-isp
- AEMO Generation Information: https://aemo.com.au/energy-systems/electricity/national-electricity-market-nem/nem-generation-information
- AEMC rule-change and market-rule material: https://www.aemc.gov.au/

Use AEMO for:
- national / state demand forecasts where data centres are specifically discussed;
- large-load technical requirements and rule changes;
- NEM region context for NSW, VIC, QLD, SA, and TAS;
- corroborating that grid constraints explain project timing or location.

Do not treat AEMO demand totals as a project list unless AEMO or an attachment names individual projects.

### 2.2 Transmission and Distribution Network Operators

Primary targets:
- NSW / ACT transmission: Transgrid https://www.transgrid.com.au/
- NSW distribution: Ausgrid https://www.ausgrid.com.au/ ; Endeavour Energy https://www.endeavourenergy.com.au/ ; Essential Energy https://www.essentialenergy.com.au/
- Victoria transmission / distribution: AusNet https://www.ausnetservices.com.au/ ; CitiPower / Powercor / United Energy https://www.powercor.com.au/ ; Jemena https://www.jemena.com.au/
- Queensland transmission / distribution: Powerlink https://www.powerlink.com.au/ ; Energex / Ergon https://www.energex.com.au/ and https://www.ergon.com.au/
- South Australia transmission / distribution: ElectraNet https://www.electranet.com.au/ ; SA Power Networks https://www.sapowernetworks.com.au/
- Western Australia: Western Power https://www.westernpower.com.au/ ; Horizon Power https://www.horizonpower.com.au/
- Tasmania: TasNetworks https://www.tasnetworks.com.au/
- Northern Territory: Power and Water Corporation https://www.powerwater.com.au/ ; Territory Generation https://territorygeneration.com.au/

Energy query templates:
```
"{project}" "MW" "grid connection"
"{project}" "MVA" "substation"
"{project}" "transmission connection"
"{operator}" "connection agreement" "Australia"
"{suburb}" "data centre" "substation"
site:aemo.com.au "data centre"
site:aemc.gov.au "data centre" "large load"
site:transgrid.com.au "data centre"
site:ausnetservices.com.au "data centre"
site:powerlink.com.au "data centre"
site:electranet.com.au "data centre"
site:westernpower.com.au "data centre"
```

Data to extract: connection size MW / MVA, supply voltage, substation name, network service provider, augmentation works, energisation date, generator / BESS co-location, renewable PPA or firming claim, and whether the source names the datacentre or only an adjacent project.

### 2.3 Environmental, Water, and Backup Generator Trail

Australia has state-specific environmental approval pathways. Datacentres may surface through air/noise/water studies and backup generator approvals rather than a dedicated datacentre licence.

Search targets:
- NSW Environment Protection Authority: https://www.epa.nsw.gov.au/
- Environment Protection Authority Victoria: https://www.epa.vic.gov.au/
- Queensland Department of Environment, Tourism, Science and Innovation: https://www.detsi.qld.gov.au/
- WA Environmental Protection Authority: https://www.epa.wa.gov.au/
- South Australia EPA: https://www.epa.sa.gov.au/
- Tasmanian EPA: https://epa.tas.gov.au/
- NT Environment Protection Authority: https://ntepa.nt.gov.au/

Environmental query templates:
```
"{project}" "air quality" "data centre"
"{project}" "noise assessment" "data centre"
"{project}" "diesel generator" "data centre"
"{project}" "water demand" "data centre"
"{project}" "cooling" "Sydney Water"
"{project}" "EPA" "data centre"
```

Grade **A** when the document is hosted by a planning authority, EPA, water utility, or council. Grade **B** for planner / consultant summaries unless the original report is checked.

---

## 3. ACMA and Telecommunications Regulator Sources

Primary source:
- ACMA Register of Radiocommunications Licences: https://www.acma.gov.au/register-radiocommunications-licences-rrl

Use cases:
- Search licensee / client names such as `Equinix`, `NEXTDC`, `AirTrunk`, `Macquarie`, `CDC`, `Digital Realty`, `Global Switch`, `DigiCo`, `Vocus`, `Telstra`, `TPG`, and known SPVs.
- Search site addresses near known data-centre campuses for microwave, satellite, fixed link, or land-mobile licences.
- Use RRL coordinates / licence sites as **A-grade telecom evidence**, but only as facility evidence when the licensee, site address, or related planning record clearly ties the transmitter to the datacentre.

ACMA query templates:
```
ACMA RRL licensee "{operator}"
ACMA RRL site "{address}"
ACMA RRL "{suburb}" "{operator}"
site:acma.gov.au "Register of Radiocommunications Licences" "{operator}"
```

Other telecom infrastructure leads:
- PeeringDB: https://www.peeringdb.com/ (B for interconnection location unless matched to operator page)
- Internet Exchange Australia: https://internet.asn.au/
- Megaport enabled locations: https://www.megaport.com/locations/
- Telstra Wholesale / exchange and network pages: https://www.telstrawholesale.com.au/

---

## 4. Official Cloud Region Pages

Cloud pages confirm the provider has one or more Australian regions, but they do not disclose exact datacentre buildings. Treat them as **A for region / metro existence** and **C for exact siting unless joined to planning evidence**.

| Provider | Official URL | Australia region signal | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/local/australia/ ; https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Asia Pacific (Sydney) `ap-southeast-2`; Asia Pacific (Melbourne) `ap-southeast-4`, each with 3 AZs | Seed NSW and Victoria searches for Amazon / AWS / Amazon Corporate Services / Amazon Data Services, especially Western Sydney and Melbourne north / west. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://datacenters.microsoft.com/globe/ | Australia East = New South Wales; Australia Southeast = Victoria; Australia Central / Central 2 = Canberra | Seed Sydney, Melbourne, Canberra, and federal-sovereign hosting searches; do not infer exact buildings from region names. |
| Google Cloud | https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | `australia-southeast1` Sydney; `australia-southeast2` Melbourne | Seed Sydney / Melbourne operator and planning searches. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm ; https://www.oracle.com/cloud/public-cloud-regions/ | Australia East (Sydney) `ap-sydney-1`; Australia Southeast (Melbourne) `ap-melbourne-1` | Seed Sydney and Melbourne; exact facilities remain hidden. |

Cloud-provider query templates:
```
"{provider}" "Australia" "data centre" "planning"
"{provider}" "Sydney" "data centre" "development application"
"{provider}" "Melbourne" "data centre" "planning permit"
"Amazon" "data centre" "Craigieburn"
"AWS" "data centre" "Sydney" "SSD"
"Microsoft" "Australia East" "data centre" "NSW"
"Google Cloud" "australia-southeast1" "data centre"
```

---

## 5. Official Colo / Operator Seed List

Use operator pages to build a canonical seed list, then verify every new build or expansion through planning / energy / ASX evidence where possible.

| Operator | Official URL | Australia footprint / high-yield locations | Reliability note |
|---|---|---|---|
| Equinix | Australia https://www.equinix.com/data-centers/asia-pacific-colocation/australia-colocation ; Sydney https://www.equinix.com/data-centers/asia-pacific-colocation/australia-colocation/sydney-data-centers ; Melbourne https://www.equinix.com/data-centers/asia-pacific-colocation/australia-colocation/melbourne-data-centers | Sydney, Melbourne, Perth, Brisbane, Canberra, Adelaide | A for facility existence / metro; check council for expansions. |
| NEXTDC | Australia https://www.nextdc.com/data-centres ; home https://www.nextdc.com/ | Sydney S1-S7, Melbourne M1-M4, Brisbane, Perth, Adelaide, Canberra, Darwin, Geelong / edge | A for facility status / capacity on official specs; ASX filings also valuable. |
| Macquarie Data Centres | https://www.macquariedatacentres.com/ ; Intellicentres https://www.macquariecloudservices.com/intellicentres/ | Sydney CBD, Macquarie Park / Sydney North Zone, Canberra bunker campus | A for official facility / capacity claims; verify IC3 / campus expansions via Ryde or ACT planning. |
| AirTrunk | Australia https://airtrunk.com/location/australia/ | SYD1 Sydney West, SYD2 Sydney North, SYD3 Sydney West, MEL1, MEL2 | A for campus names / capacities where official pages disclose; planning confirms exact site status. |
| Digital Realty | Sydney https://www.digitalrealty.com/data-centers/asia-pacific/sydney ; Melbourne https://www.digitalrealty.com/data-centers/asia-pacific/melbourne | Sydney / Erskine Park, Melbourne | A for listed facilities; planning / council for expansions. |
| CDC Data Centres | https://cdc.com/ ; Sydney https://cdc.com/locations/sydney/ ; Melbourne https://cdc.com/locations/melbourne/ | Canberra, Eastern Creek, Marsden Park, Brooklyn, Laverton, Perth / WA expansion | A for official campuses; state planning and government pages often provide capacity / status. |
| DigiCo / former Global Switch Australia | https://www.digi-co.com.au/ ; Global Switch https://www.globalswitch.com/ | Sydney Ultimo / Harris Street, Sydney West / expansion | A/B depending on whether the current official page or planning record names the asset. |
| Global Switch legacy | https://www.globalswitch.com/ | Sydney East / West historically; ownership changed in Australia | Use as historical seed, then verify current owner/operator. |
| Vocus | https://www.vocus.com.au/ ; support data-centre access list https://support.vocus.com.au/s/article/Data-Centre-Access | Melbourne, Sydney, Perth, Adelaide and telecom facilities | B/C for exact facility list when support pages are indirect; confirm with operator or council. |
| Telstra | https://www.telstra.com.au/business-enterprise/products/cloud/data-centres | Enterprise / telco facilities nationally | A for official Telstra-hosted locations if disclosed; often vague. |
| Leading Edge Data Centres | https://leadingedgedc.com/network-map/ | Regional NSW, VIC, QLD edge sites | A for official announced network; B/C for unbuilt "coming soon" locations. |

Operator workflow:
1. Record official facility / campus name, metro, LGA, disclosed address if any, capacity MW / racks / sqm, status, and certifications.
2. Search exact facility name plus `planning permit`, `development application`, `SSD`, `MVA`, `substation`, and the LGA.
3. Check public-company / listed-parent records where applicable: NEXTDC ASX, Macquarie Technology Group ASX, Infratil / CDC disclosures, Digital Realty investor filings.
4. Use DataCenterMap, Baxtel, Cloudscene, PeeringDB, and Data Centre Dynamics only as B/C discovery leads unless corroborated.

---

## 6. Query Playbook

### 6.1 Core Discovery Queries

Use both spellings and planning terms:
```
"{division}" "data centre"
"{division}" "data center"
"{division}" datacentre
"{division}" "data hall"
"{division}" "server farm"
"{division}" "hyperscale"
"{division}" "AI data centre"
"{division}" "utility installation" "data centre"
"{division}" "development application" "data centre"
"{division}" "planning permit" "data centre"
"{division}" "substation" "data centre"
```

Council-scoped:
```
site:{council-domain} "data centre"
site:{council-domain} "data center"
site:{council-domain} "datacentre"
site:{council-domain} "development application" "data centre"
site:{council-domain} "planning permit" "data centre"
site:{council-domain} "committee report" "data centre"
site:{council-domain} "substation" "data centre"
```

Document-focused:
```
filetype:pdf "data centre" "planning statement" "{state or LGA}"
filetype:pdf "data centre" "development application" "{state or LGA}"
filetype:pdf "data centre" "environmental impact statement" "{state or LGA}"
filetype:pdf "data centre" "air quality assessment" "{state or LGA}"
filetype:pdf "data centre" "noise assessment" "{state or LGA}"
filetype:pdf "data centre" "MVA" "{state or LGA}"
filetype:pdf "data centre" "substation" "{state or LGA}"
```

### 6.2 Capacity Extraction Queries

```
"{project}" "IT load"
"{project}" "critical IT load"
"{project}" "MW IT"
"{project}" "MVA"
"{project}" "power capacity"
"{project}" "operational capacity"
"{project}" "data halls"
"{project}" "GFA"
"{project}" "gross floor area"
"{project}" "racks"
"{project}" "substation"
"{project}" "diesel generators"
```

Preferred extraction hierarchy:
1. State planning application / EIS / decision notice / assessment report.
2. Council DA documents, committee report, public-notification package.
3. Network / AEMO / utility connection document.
4. Official operator specification or ASX filing.
5. Government investment announcement.
6. Trade press citing named primary documents.
7. Directory / map / marketing lead.

---

## 7. Division Enumeration Strategy

For each repo division:
1. Parse the state / territory prefix and LGA name.
2. Start with the state portal relevant to that prefix. NSW and Victoria should be searched at state level first; other states should combine state significant-development search with the LGA council register.
3. Search the LGA register for `data centre`, `data center`, `datacentre`, `data storage`, `server`, `utility installation`, `substation`, `battery`, and operator names.
4. Search web with state / LGA / suburb query templates.
5. Cross-check cloud-region and operator seed lists for nearby known campuses.
6. Cross-check AEMO / network sources for named large-load, substation, or connection evidence.
7. Assign evidence grade conservatively and record `no_projects` only after planning, operator, and web searches produce no credible facility evidence.

High-yield division clusters:
- **NSW Western Sydney**: Penrith, Blacktown, Cumberland, Parramatta, Liverpool, Fairfield, Camden, Campbelltown, The Hills. Most likely to produce SSD records with MW and substation details.
- **NSW Sydney / North Zone**: Sydney, Ryde, Willoughby, North Sydney, Lane Cove. Macquarie Park, Ultimo, Alexandria, Artarmon, and North Ryde require council + operator checks.
- **Victoria Melbourne west / north**: Hume, Hobsons Bay, Maribyrnong, Brimbank, Wyndham, Melton, Whittlesea. Ministerial permit searches are essential.
- **Victoria regional edge**: Greater Geelong, Wodonga, Ballarat, Bendigo, Shepparton, Horsham. NEXTDC / Leading Edge / cloud edge projects may appear before large planning records.
- **Queensland SEQ**: Brisbane, Moreton Bay, Logan, Ipswich, Redland, Sunshine Coast, Gold Coast, Toowoomba. Use council DA + EDQ + Powerlink.
- **WA Perth corridor**: Perth, Canning, Gosnells, Belmont, Swan, Kwinana, Rockingham, Stirling, Joondalup, Armadale. Use WA Planning Online / DAP + Western Power.
- **South Australia**: Adelaide metro for colo; Coorong / Goyder / transmission-adjacent rural LGAs for AI / hyperscale energy-led campuses.
- **Tasmania / NT**: lower-density but high-value for energy-led projects, sovereign / government workloads, and regional edge; check state DA portals and energy utilities carefully.

---

## 8. Red Flags and Normalization Rules

- Do not count a cloud region as a physical datacentre project unless there is a matching planning, operator, or regulator record.
- Do not count a mere land purchase, MoU, policy announcement, or "AI hub" without facility scope as a datacentre unless the source names datacentre buildings, IT load, racks, halls, or planning use.
- For large campuses, store both `capacity_mw` and the capacity basis in notes: `IT load`, `critical IT load`, `operational capacity`, `power consumption`, `MVA`, or `connection capacity` are not identical.
- For NSW SSD and Victorian ministerial permits, preserve official application IDs such as `SSD-...` or `PA...`; these are stable anchors for later re-checks.
- Australian addresses often use suburb names that do not equal the LGA name. Always verify the LGA via the planning portal, council register, or state mapping before assigning the division.
- If a project spans several buildings / stages, record one campus record when the source treats it as one campus; record separate facilities only when official pages or permits split them by building / campus name.
