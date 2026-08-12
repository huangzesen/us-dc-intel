# AU Explorer — Industry / Trade Press / Vendor-Led Discovery for Australian Datacentres

Date: 2026-08-12. Scope: how to enumerate Australia (AU) datacentre projects through industry/trade press, vendor/operator pages, cloud-region pages, and state/LGA planning search patterns. The manifest divisions are **local government areas (LGAs / admin2)** grouped by state or territory. Reliability grades: **A** = official/primary (state planning portals, LGA DA registers, operator official pages for owned sites, cloud-region official pages, ASX/investor filings), **B** = established trade press / industry association / legal planning notes / strong property press, **C** = weak secondary / directories / social posts / speculative investment commentary.

---

## 0. Australia-specific frame

- Australia has no single public datacentre registry. Enumeration works by triangulating **operator location pages**, **hyperscaler region pages**, **DCD/CRN/ARN/iTnews/AFR/property press**, **state significant development portals**, **LGA DA registers**, **Development Assessment Panels**, **power/transmission evidence**, and **ASX/investor disclosures**.
- Use Australian spelling first: **data centre**. Also search **data center** for international operators/trade press, plus **datacentre**, **data storage**, **high technology industry**, **utility installation**, **warehouse and ancillary office** (WA/industrial planning descriptions may disguise DCs), **AI infrastructure**, **hyperscale**, **sovereign cloud**, **substation**, **MVA**, **IT load**, **backup generators**, **diesel**, **cooling**, **liquid cooling**, and **renewable energy**.
- Current high-density clusters:
  - **NSW / Sydney**: Blacktown, Cumberland, Penrith, Parramatta, Ryde, Lane Cove, Willoughby, Liverpool, Fairfield, Sydney, Bayside, Northern Beaches; suburbs to query include Eastern Creek, Huntingwood, Horsley Park, Marsden Park, Erskine Park, Macquarie Park, Lane Cove West, Artarmon, Guildford West, Minchinbury.
  - **Victoria / Melbourne**: Maribyrnong, Brimbank, Hobsons Bay, Hume, Wyndham, Melton, Melbourne, Port Phillip, Monash, Kingston, Greater Dandenong, Greater Geelong; suburbs include West Footscray/Tottenham, Tullamarine, Port Melbourne, Brooklyn, Derrimut, Truganina, Laverton North, Campbellfield, Plumpton, Clayton, Thomastown, Geelong.
  - **ACT / Canberra**: Fyshwick, Hume, Beard, Symonston, Bruce; sovereign/government workloads drive CDC, Macquarie Government, Microsoft/Oracle government-cloud trails.
  - **Queensland**: Brisbane, Ipswich, Logan, Moreton Bay, Gold Coast, Sunshine Coast, Toowoomba, Townsville, Gladstone; Brisbane industrial suburbs, Springfield/Ipswich, Maroochydore/Sunshine Coast cable landing, Gold Coast proposals.
  - **Western Australia**: Perth metro LGAs (Gosnells/Maddington, Malaga/Swan, Perth, Canning, Belmont, Victoria Park), Port Hedland/Newman for edge/mining, Greater Geraldton/Oakajee for power/renewables-led proposals.
  - **South Australia**: Adelaide CBD and metro LGAs, Port Adelaide Enfield, Playford, Salisbury, Whyalla/Upper Spencer Gulf for renewable/AI-infrastructure policy leads.
  - **Northern Territory**: Darwin CBD, Darwin Waterfront Precinct, Palmerston, Litchfield, Weddell/Darwin region; subsea cable and defence/AI campus proposals.
  - **Tasmania**: Hobart/Glenorchy/Clarence/Launceston/Brighton/Northern Midlands plus hydro/renewables-led proposals; lower probability, but state policy and renewable-energy stories matter.
- Australia is planning-law fragmented. Large NSW projects often appear as **State Significant Development (SSD)** on the NSW Planning Portal. Large Victorian projects often appear in the **Planning Victoria Ministerial Permits Register** under clause **53.22** as `Utility Installation (Data Centre)`. WA high-value projects may be determined by **Development Assessment Panels (DAP)**. SA is creating a faster data-centre pathway through PlanSA and proposed dedicated legislation. Always search both state portals and the LGA named by the manifest.

---

## 1. Trade press and industry sources

Use trade press to discover operator, campus name, suburb, MW/MVA, customer, contractor, land transaction, and lifecycle verb; then verify in an operator page, planning portal, ASX filing, or LGA record.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Best open feed for Australia DC launches, land buys, MW claims, hyperscale contracts, and state-level proposals. Recent AU examples include NEXTDC S4/S7/D2/Geelong, AirTrunk MEL2, CDC Melbourne/Perth/555MW contract, Macquarie IC3 Super West. | B; promote only when it points to primary docs |
| CRN Australia | https://www.crn.com.au/ | Strong channel/trade coverage of Data Centres Australia, AirTrunk, Insite DC, Microsoft/AWS/partner ecosystem. Good for operator/customer context. | B |
| ARN / iTnews / Australian Financial Review / The Australian / InDaily / local metro press | site-scoped search | Useful for local controversy, land transactions, investor plans, and official-opening stories. AFR and The Australian can be paywalled; use them as leads unless details are independently visible. | B/C |
| Data Centres Australia | https://datacentres.org.au/ | New sector body launched after a pilot involving AirTrunk, AWS, CDC, Microsoft, and NEXTDC; members reported by CRN include Equinix, Goodman Group, Schneider Electric, STACK, TikTok. Use for policy/body/member discovery, not facility proof. | B |
| Legal/planning commentary | Dentons, Ashurst, Pinsent Masons, Johnson Winter Slattery | Good for approval pathway changes, energy/renewables policy, and state reform context. Not a facility registry. | B |
| Directories and aggregators | Baxtel, DataCenterMap, OCOLO, Datacenters.com, Cloudscene | Useful for legacy colocation addresses and smaller sites. Treat capacity/location as C unless it matches operator page or planning evidence. | C/B |
| RenewMap / project trackers | state datacentre project pages | Good for energy/pipeline leads and state comparison; verify project status elsewhere. | C/B depending on linked evidence |

High-value DCD queries:

```text
site:datacenterdynamics.com/en/news/ Australia "data center" "Sydney" "MW"
site:datacenterdynamics.com/en/news/ Australia "data center" "Melbourne" "MW"
site:datacenterdynamics.com/en/news/ Australia "NEXTDC" "data center" "S7" OR "Horsley Park"
site:datacenterdynamics.com/en/news/ Australia "AirTrunk" "MEL2" OR "SYD3"
site:datacenterdynamics.com/en/news/ Australia "CDC" "Perth" OR "Maddington" OR "Melbourne"
site:datacenterdynamics.com/en/news/ Australia "Macquarie Data Centres" "IC3" OR "Macquarie Park"
site:datacenterdynamics.com/en/news/ Australia "Stockland" OR "Goodman" OR "Insite DC" "data center"
```

CRN/ARN/iTnews query templates:

```text
site:crn.com.au "data centre" Australia "AirTrunk" OR "NEXTDC" OR "CDC"
site:crn.com.au "Data Centres Australia"
site:arnnet.com.au "data centre" "{operator}" Australia
site:itnews.com.au "data centre" "{suburb}" OR "{LGA}"
site:afr.com "data centre" "{operator}" "{suburb}"
site:theaustralian.com.au "data centre" Australia "AI" "{state}"
```

Lifecycle verb interpretation:

- `announced`, `eyes`, `shortlisted`, `MoU`, `strategy`, `landbank` = lead only, usually **C/B**.
- `acquires site`, `files/submits plans`, `SSD lodged`, `ministerial permit`, `DAP approval` = concrete pipeline, **B/A** depending on source.
- `approved`, `permit`, `determination`, `construction starts`, `breaks ground`, `tops out`, `opens`, `ready for service` = countable status if primary/operator evidence exists.
- `contracted capacity` and `future pipeline` are not the same as built capacity; capture the exact timeframe and phase.

---

## 2. Vendor/operator sweep

Official operator pages are **A for owned marketed presence** and usually **B for capacity** unless the page or filing gives phase-specific IT load. For public companies, prefer ASX/investor presentations for capacity, capex, and status.

| Operator/developer | Priority geographies | Official / useful URL | Notes |
|---|---|---|---|
| NEXTDC | Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, Darwin, Sunshine Coast, Port Hedland/Newman, Geelong, Gold Coast | https://www.nextdc.com/data-centres and https://www.nextdc.com/about-us/our-history | Official pages state national footprint across major capitals. DCD reports 20 AU sites in operation/development and major S4/S7/Sydney, D2 Darwin, Geelong, Adelaide signals. ASX filings are high-value. |
| AirTrunk | Sydney West/North, Melbourne | https://airtrunk.com/location/australia/ and https://airtrunk.com/locations/ | Official page lists SYD1, SYD2, SYD3, MEL1, MEL2 and 755+MW in Australia. DCD/CRN report MEL2 at 354MW+ and total Melbourne 630MW+. |
| CDC Data Centres | Canberra, Sydney, Melbourne, Perth | https://cdc.com/locations/ | Official locations page says 20 locations across 8 campuses/4 cities and 5 regions incl. Auckland. DCD reports 302MW operational, 388MW in development, Perth/Maddington and Melbourne campus. Infratil disclosures are high-value. |
| Macquarie Data Centres / Macquarie Government | Sydney CBD, Macquarie Park, Canberra | https://www.macquarietechnologygroup.com/our-data-centres/ and https://www.macquariegovernment.com/canberra-data-centre/ | Official pages cover IC3 East/Super West and Canberra bunker/government campuses. DCD tracks IC3 Super West and a 200MW Macquarie Park expansion. |
| Equinix | Sydney, Melbourne, Perth, Brisbane, Canberra, Adelaide | https://www.equinix.com/data-centers/asia-pacific-colocation/australia-colocation | Official AU page says Sydney, Melbourne, Perth, Brisbane, Canberra, Adelaide; Equinix paper says 18 AU data centres. Use metro pages for facility names. |
| Digital Realty | Sydney, Melbourne | https://www.digitalrealty.com/data-centers/asia-pacific/sydney and /melbourne | Official Sydney page lists two Sydney data centers and colocation sqm. Good for operational estate, not new hyperscale pipeline unless press/permits. |
| Global Switch / HMC Capital | Sydney Ultimo | https://www.globalswitch.com/ and HMC/Global Switch sale announcements | Major legacy Sydney East/West campus; DCD reported sale of AU assets to HMC Capital. Verify current ownership before final operator attribution. |
| Telstra InfraCo / Doma / Starwood | Sydney, Melbourne, Canberra | Telstra InfraCo pages plus DCD press | Legacy carrier colocation and new Minchinbury/Western Sydney project. Treat directories as leads; verify via Telstra/Doma/project filings. |
| Goodman Group, Stockland, Centuria, Insite DC, STACK, DigiCo, Firmus | Sydney/Melbourne first, then state-specific industrial land | company sites + ASX/press + planning portals | Many are developers/landowners rather than operating colo brands. Strong leads for new AI/hyperscale campuses, but require planning or tenant evidence. |
| Leading Edge Data Centres, Field Solutions Group, regional edge providers | regional NSW/QLD/VIC/WA | official pages + local council grants/news | Small edge facilities surface in local press/council minutes, not DCD. Capture separately from hyperscale. |
| Telcos/MSPs: Telstra, Optus, TPG/Vocus, Fujitsu, Interactive, Datacom | capital-city legacy sites | official pages/directories | Useful for operational smaller colocation, not new build unless DA/press exists. |

Vendor query templates:

```text
"{operator}" "{LGA}" "data centre"
"{operator}" "{suburb}" ("MW" OR "MVA" OR "IT load" OR "technical space")
"{operator}" "{state}" ("development application" OR "planning approval" OR "ministerial permit" OR "SSD")
site:{operator-domain} "Australia" "data centre" "{city}"
site:asx.com.au "{operator}" "data centre" "MW"
site:investi.com.au OR site:infratil.com "CDC" "data centre" "MW"
"{operator legal name}" "EPBC" "data centre"
```

---

## 3. Hyperscaler official region pages

These are **A for cloud-region existence** but do not identify exact physical facilities. Use them to map likely metros, then pivot to colocation/operator and planning evidence.

| Provider | Official page | Australia signal |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/local/australia/ | `ap-southeast-2` Asia Pacific (Sydney), 3 AZs; `ap-southeast-4` Asia Pacific (Melbourne), 3 AZs. AWS local page says Melbourne is the second AU region, joining Sydney. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Australia East = New South Wales, Australia Southeast = Victoria, Australia Central and Australia Central 2 = Canberra. Search CDC/Canberra and protected-government-cloud context separately. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | `australia-southeast1` Sydney and `australia-southeast2` Melbourne. Google blog confirms Melbourne as second AU cloud region after Sydney. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | Australia East (Sydney), Australia Southeast (Melbourne), plus Australian Government cloud region in Canberra for IRAP PROTECTED workloads. |

Hyperscaler physical-site pivot:

```text
"AWS" "Australia" "data centre" "Sydney" OR "Melbourne" "AirTrunk" OR "NEXTDC" OR "CDC"
"Microsoft" "Australia" "data centre" "Canberra" OR "Sydney" OR "Melbourne"
"Google" "Australia Connect" "Darwin" "NEXTDC" OR "Bosun"
"Oracle" "Australian Government" "Canberra" "data centre" OR "CDC"
"TikTok" "Data Centres Australia" "Sydney" OR "Melbourne" "data centre"
```

---

## 4. Planning and permitting workflow by state / territory

### 4.1 Universal LGA/state query pattern

For every manifest division, parse `{state} - {LGA}`. Run the state portal first for large projects, then the LGA DA register/council site, then vendor/trade queries.

```text
"{LGA}" "data centre" "development application"
"{LGA}" "data center" "development application"
"{LGA}" "data storage" "development application"
"{suburb}" "data centre" "{state}"
site:{council-domain} "data centre"
site:{council-domain} "data storage"
site:{council-domain} "hyperscale"
site:{council-domain} "backup generators" "data centre"
site:{council-domain} "substation" "data centre"
```

Inside planning registers, search:

```text
data centre
data center
datacentre
data storage
high technology industry
utility installation
warehouse and ancillary structures
backup generator
substation
MVA
```

Capture fields:

- application/reference number, project name, applicant/proponent, land address/lot-plan, suburb, LGA, state;
- pathway: SSD, ministerial permit, DA, DAP, priority development area, environmental significance opinion, EPBC referral;
- status: lodged, exhibition, response to submissions, approved, refused, under appeal, construction, operational;
- evidence documents: EIS/EES, planning statement, architectural drawings, noise/air quality/water, traffic, energy, substation/grid connection, generator/fuel storage, decision notice, conditions;
- capacity evidence: IT load MW, grid import MVA/MW, number of data halls, technical space, phase count, generator count, BESS/substation rating, cooling/water design.

### 4.2 New South Wales

Primary state routes:

- NSW Planning Portal major projects: https://www.planningportal.nsw.gov.au/major-projects/projects
- NSW data-centres planning reform page: https://www.planning.nsw.gov.au/the-planning-system/planning-reforms/ssd-warehouses-and-data-centres
- Investment Delivery Authority project pipeline where relevant: https://www.nsw.gov.au/departments-and-agencies/investment-nsw/ida/projects-by-ida

NSW introduced a specific **data centres** land-use term and identifies data centres as a type of **high-technology industry**. Many large projects are SSDs with `SSD-########` references. Search the portal by `Development Type = Data Storage` and terms `data centre`, `data storage`, `SSD`.

High-priority NSW LGAs and examples:

- **Blacktown**: Marsden Park Data Centre `SSD-70889211`; Honeman Close `SSD-58601963`; Eastern Creek/Project Atlas `SSD-101067971`; AirTrunk/NEXTDC/CDC/STACK-style Western Sydney searches.
- **Penrith**: Erskine Park, Mamre Road, Kemps Creek/Aerotropolis edge, STACK SYD01 `SSD-82211208`, industrial precincts.
- **Ryde / Lane Cove / Willoughby**: Macquarie Park, Lane Cove West, Artarmon, Julius Avenue `SSD-80018208`, Project Apollo `SSD-74069708`, Project Mars `SSD-82052708`, Macquarie/NEXTDC/Equinix legacy clusters.
- **Cumberland / Parramatta / Fairfield / Liverpool**: Guildford West Project Pluto `SSD-69223466`, Wetherill Park/Smithfield/Moorebank industrial zones.
- **Sydney / Bayside / Inner West**: legacy/edge/cable and CBD colo; verify no false positives from office "data centre" rooms.

NSW query templates:

```text
site:planningportal.nsw.gov.au/major-projects/projects "data centre" "{LGA}"
site:planningportal.nsw.gov.au/major-projects/projects "data storage" "{suburb}"
site:planningportal.nsw.gov.au/major-projects/projects "SSD-" "data centre" "Blacktown"
"{suburb}" "SSD" "data centre" "NSW"
"{LGA}" "high technology industry" "data centre"
```

### 4.3 Victoria

Primary state route:

- Planning Victoria Ministerial Permits Register: https://www.planning.vic.gov.au/planning-approvals/ministerial-permits-register

Victorian large projects often use **Clause 53.22** and descriptions like `Use and development ... for a Utility Installation (Data Centre)`. The register is very high-yield for 2024-2026 projects, including permits for Port Melbourne, West Footscray/Tottenham, Cobblebank, Campbellfield/Plumpton-style campuses, and high-MVA proposals.

High-priority Victorian LGAs:

- **Maribyrnong / Brimbank / Hobsons Bay**: West Footscray, Tottenham, Brooklyn, Derrimut, Laverton North; NEXTDC M3/M4 and CDC/Stockland/Goodman style industrial conversions.
- **Hume / Melton / Wyndham**: Tullamarine, Campbellfield, Plumpton, Truganina; AirTrunk MEL2 and new greenfield campuses.
- **Port Phillip / Melbourne**: Port Melbourne/NEXTDC, CBD/edge.
- **Monash / Kingston / Greater Dandenong**: Clayton, Springvale, Dandenong South; Telstra/Centuria/industrial power-ready sites.
- **Greater Geelong**: NEXTDC GE1 and large land acquisitions near Lovely Banks/Geelong.

Victoria query templates:

```text
site:planning.vic.gov.au/planning-approvals/ministerial-permits-register "data centre" "{LGA}"
site:planning.vic.gov.au/planning-approvals/ministerial-permits-register "Utility Installation (Data Centre)"
site:planning.vic.gov.au "53.22" "data centre" "{suburb}"
"{suburb}" "PA24" OR "PA25" OR "PA26" "data centre" "Victoria"
"{LGA}" "data centre" "ministerial permit"
```

### 4.4 Queensland

Primary routes:

- Brisbane City Council Development.i: https://developmenti.brisbane.qld.gov.au/
- Economic Development Queensland for Priority Development Areas: https://www.statedevelopment.qld.gov.au/economic-development-qld
- Each LGA has its own DA register; Gold Coast, Ipswich, Logan, Moreton Bay, Sunshine Coast, Townsville and Toowoomba are priorities.

High-priority Queensland LGAs:

- **Brisbane**: industrial suburbs including Seventeen Mile Rocks, Willawong, Keperra, Eagle Farm/Pinkenba, Murarrie; use Development.i nightly-updated application/property search.
- **Ipswich / Logan / Moreton Bay / Gold Coast**: greenfield industrial campuses and Gold Coast first-DC proposals; check state/PDA pathways as well as councils.
- **Sunshine Coast**: Maroochydore international broadband submarine cable, NEXTDC SC1/SC2, edge/cloud ecosystem.
- **Townsville / Gladstone / Western Downs / Toowoomba**: energy/renewables/industrial proposals, usually C until planning or operator proof.

Queensland query templates:

```text
site:developmenti.brisbane.qld.gov.au "data centre"
"{LGA}" "data centre" "material change of use" Queensland
"{suburb}" "data centre" "development application" "QLD"
site:{council-domain} "data centre" "Material Change of Use"
site:statedevelopment.qld.gov.au "data centre" "Priority Development Area"
```

### 4.5 Western Australia

Primary routes:

- WA Planning / Development Assessment Panels documents: https://www.planning.wa.gov.au/
- WA DAP search/documents and local council planning pages (e.g. City of Gosnells DAP page).
- DevelopmentWA industrial land pages for site leads: https://developmentwa.com.au/

WA DAP documents can describe datacentre campuses as `Proposed Warehouses and Ancillary Structures`. Example: City of Gosnells / Maddington DAP `DAP/25/02926` for CDC, with WA Planning PDFs and minutes. Use address/lot searches after discovering a project.

High-priority WA LGAs:

- **Gosnells**: Maddington / Kenwick Road / Bickley Road CDC campus.
- **Swan / Perth / Canning / Belmont / Victoria Park / Stirling / Joondalup / Cockburn / Kwinana**: Perth metro colo/industrial power sites; NEXTDC P1/P2 around Malaga/Perth.
- **Port Hedland / East Pilbara / Ashburton / Karratha**: mining/edge facilities such as NEXTDC PH1/NE1 and resource-sector remote operations.
- **Greater Geraldton / Oakajee**: power/renewables-led speculative proposals; verify with DevelopmentWA/state documents.

WA query templates:

```text
site:planning.wa.gov.au "data centre" "DAP"
site:planning.wa.gov.au "Data Centres" "{LGA}"
site:planning.wa.gov.au "DAP/" "data centre" "Maddington"
site:{council-domain} "Development Assessment Panel" "data centre"
"{LGA}" "Proposed Warehouses and Ancillary Structures" "data centre"
"{suburb}" "data centre" "JDAP" OR "DAP"
```

### 4.6 South Australia

Primary route:

- PlanSA / Development Application Register: https://plan.sa.gov.au/
- PlanSA regulation updates: https://plan.sa.gov.au/news/article/2025/recent-regulation-changes

PlanSA has public-register CSV endpoints and a statewide planning system. Recent regulation changes added datacentre-specific essential-infrastructure style requirements, including SA Water advice and Technical Regulator certification for power-system reliability/security/stability. SA government/legal press in 2026 also points to a proposed Data Centre and AI Infrastructure Act.

High-priority SA LGAs:

- **Adelaide**: NEXTDC A1 at 211 Pirie Street; PlanSA register record described a six-level data centre and ancillary office.
- **Port Adelaide Enfield / Playford / Salisbury / West Torrens / Charles Sturt / Marion**: metro industrial land and grid access.
- **Whyalla / Port Augusta / Port Pirie / Upper Spencer Gulf LGAs**: renewables/hydrogen/industrial power proposals; mostly lead-stage until official DA/strategy docs.

SA query templates:

```text
site:plan.sa.gov.au "data centre" "Development Application Register"
site:plan.sa.gov.au "data centre" "Adelaide"
site:plan.sa.gov.au "data centre" "essential infrastructure"
"{LGA}" "data centre" "PlanSA"
"{suburb}" "data centre" "DAP" "South Australia"
```

### 4.7 Australian Capital Territory

Primary routes:

- ACT Planning DA and environmental pages: https://www.planning.act.gov.au/
- Environmental Significance Opinions: https://www.planning.act.gov.au/applications-and-assessments/environmental-impact-assessment/environmental-significance-opinion

ACT evidence often appears through **Environmental Significance Opinions (ESO)** and DA pages. Example: Beard 2 ESO in 2026 described a three-storey data centre with 12 data halls and 84MW capacity; Fyshwick ESO records include 11kV feeder works to support a data centre. Search federal/government cloud vendor pages too.

ACT query templates:

```text
site:planning.act.gov.au "data centre" "Environmental Significance Opinion"
site:planning.act.gov.au "data centre" "Beard" OR "Fyshwick" OR "Hume"
site:planning.act.gov.au "Canberra Data Centre"
"CDC" "Canberra" "data centre" "campus"
"Macquarie Government" "Canberra Data Centre"
```

### 4.8 Northern Territory

Primary routes:

- NT Planning Notices / Development Applications: https://planning.nt.gov.au/
- Invest NT project/case-study pages: https://australiasnorthernterritory.com.au/invest

High-priority NT LGAs:

- **Darwin / Darwin Waterfront Precinct**: NEXTDC D1/D2, subsea cable connectivity, Google Australia Connect/Bosun references.
- **Palmerston / Litchfield / Weddell region**: very large AI campus proposals and power-policy debate; treat news as C/B until planning application or investor/operator proof.
- **Alice Springs / Katherine / remote LGAs**: mostly edge/telecom/mining/defence leads; verify official sources.

NT query templates:

```text
site:planning.nt.gov.au "data centre" "development application"
site:australiasnorthernterritory.com.au/invest "data centre" "NEXTDC"
"Darwin" "data centre" "D2" "NEXTDC"
"Weddell" "AI data centre" "Northern Territory"
"Northern Territory" "data centre" "renewable" "gas" "planning"
```

### 4.9 Tasmania

Primary routes:

- Tasmanian Planning Portal: https://www.planning.tas.gov.au/
- Local council DA registers for Hobart, Glenorchy, Clarence, Launceston, Brighton, Northern Midlands, Devonport/Burnie.

Tasmania has fewer known hyperscale builds but attractive renewable-power narratives. Separate genuine DC proposals from unrelated "Australian Antarctic Data Centre" and scientific data repositories.

Tasmania query templates:

```text
site:planning.tas.gov.au "data centre"
"Tasmania" "data centre" "renewable" "MW"
"Hobart" OR "Launceston" "data centre" "development application"
site:{council-domain} "data centre" "planning"
"data centre" "hydro" "Tasmania" "AI infrastructure"
```

---

## 5. State/LGA enumeration recipe for the AU manifest

1. **Normalize the division**: split `New South Wales - Blacktown` into state=`NSW`, LGA=`Blacktown`; build a suburb watchlist from trade/operator hits.
2. **Run state portal search**:
   - NSW: Planning Portal major projects / SSD.
   - VIC: Planning Victoria ministerial permits.
   - QLD: Development.i for Brisbane plus council/PDA portals elsewhere.
   - WA: WA Planning DAP documents plus LGA pages.
   - SA: PlanSA register and CSV/public-register queries.
   - ACT: planning DAs + ESO list.
   - NT: NT Planning + Invest NT.
   - TAS: Tas planning portal + council registers.
3. **Run LGA DA/council search** for exact LGA and known suburbs using `data centre`, `data center`, `data storage`, `utility installation`, `high technology industry`, `substation`, `backup generator`.
4. **Run vendor/operator sweep** against the LGA/suburb: NEXTDC, AirTrunk, CDC, Macquarie, Equinix, Digital Realty, Telstra, Global Switch/HMC, Goodman, Stockland, Centuria, Insite DC, STACK, DigiCo, Leading Edge.
5. **Run trade press sweep** for the LGA/suburb and operator names; record source URLs and lifecycle verbs.
6. **Verify capacity/status** against primary evidence. If only trade press says `350MW campus`, store as planned/ultimate capacity, not operational MW.
7. **Avoid double counting**: same campus can appear as operator code (`S7`), project name (`Project Atlas`), suburb (`Eastern Creek`), LGA (`Blacktown`), landowner (`Goodman/Stockland`), and customer (`Microsoft/OpenAI/TikTok`). Key records by `(operator/developer, campus/site address, phase)`.

---

## 6. Evidence grading and pitfalls

| Evidence | Grade |
|---|---|
| State planning portal application/determination, LGA DA register, WA DAP minutes, ACT ESO, PlanSA register | A |
| Operator official location page or ASX/investor disclosure | A for presence/status; A/B for capacity depending on phase detail |
| Cloud official region list | A for cloud region; not facility-level |
| DCD, CRN, ARN, iTnews, AFR/property press | B for discovery and event reporting |
| Data Centres Australia / legal planning notes | B for policy and member context |
| Baxtel/DataCenterMap/OCOLO/Datacenters.com/Cloudscene | C unless corroborated |
| LinkedIn/social/local campaign pages | C lead only |

Common pitfalls:

- Australian records mix British and US spellings; use both.
- Planning descriptions may omit `data centre` and use `data storage`, `utility installation`, `high technology industry`, or `warehouse and ancillary structures`.
- MW headlines are often **ultimate campus capacity**, not phase-one or operational IT load.
- Power can be stated as **MVA grid import**, not IT MW; do not convert without assumptions.
- Operator, landowner, developer, customer, and contractor may all be different entities.
- Community opposition pages and news often cite unverified energy/water figures; pivot to EIS/noise/water/power reports.
- EPBC referrals are not a full planning registry, but search them for very large greenfield campuses, transmission lines, diesel fuel storage, or sensitive ecological locations.

Recommended final query pack per LGA:

```text
"{state}" "{LGA}" "data centre"
"{LGA}" "{suburb}" "data centre" "development application"
"{LGA}" "data storage" "planning"
"{suburb}" ("MVA" OR "MW" OR "substation") "data centre"
"{operator}" "{suburb}" "data centre"
site:datacenterdynamics.com/en/news/ "{suburb}" "Australia" "data center"
site:crn.com.au "{operator}" "data centre"
site:{state-planning-domain} "data centre" "{LGA}"
site:{council-domain} "data centre" OR "data storage"
```
