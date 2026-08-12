# GB Explorer — Industry / Trade Press / Vendor-Led Discovery for UK Datacentres

Date: 2026-08-12. Scope: how to enumerate United Kingdom datacentre projects from industry/trade press, vendor pages, and local planning authority evidence. Country code: **GB**. Reliability grades: **A** = official/primary (local planning portals, appeal/DCO decisions, operator official pages for owned sites, cloud region docs for operational region presence), **B** = strong secondary (DCD, The Register, techUK/DCA, council news, specialist property/planning press), **C** = weak/aggregate (directories, LinkedIn, marketing-only proposals, local campaign pages).

---

## 0. UK structural facts for enumeration

- The UK is not a single planning database market. Most datacentre projects are found in **local planning authority (LPA)** portals, with different software per council (Idox, PublicAccess, Civica, Agile, in-house). The national Planning Portal is mainly an application-submission service, not a complete search index.
- England has a partial planning-data layer at https://www.planning.data.gov.uk, but it warns that coverage is incomplete. Use it as a discovery aid, not a registry.
- Large projects may now route through national decision channels. The UK designated datacentres as **Critical National Infrastructure** in 2024 (https://www.gov.uk/government/news/datacentres-to-be-given-massive-boost-and-protections-from-cyber-criminals-and-it-blackouts). Government AI Growth Zone guidance says most AI datacentres still use the local Town and Country Planning Act route, but a small number of very large projects may use the NSIP route (https://www.gov.uk/government/publications/delivering-ai-growth-zones/delivering-ai-growth-zones). Track Planning Inspectorate / recovered appeals for the biggest schemes.
- The live estate is concentrated around **Greater London + Thames Valley / M4 corridor**: Slough, Hayes, Uxbridge, Park Royal, Docklands, Reading/Wokingham, Bracknell/Windsor. Fast-growing new-build clusters are **Hertfordshire/Essex**, **South Wales (Cardiff/Newport/Bridgend)**, **North East/Northumberland**, **Yorkshire/Lincolnshire/Humber**, **Manchester/Stockport**, **Wiltshire/Corsham**, and **Scotland central belt**.
- UK planning descriptions often classify datacentres under **Use Class B8** (storage/distribution) with sui generis traits. Search "data centre" and "datacentre", plus "Use Class B8", "hyperscale", "server halls", "backup generators", "energy centre", "BESS", "substation", and "district heating".

---

## 1. Trade press and industry sources (Grade B discovery backbone)

Use trade press to discover names, developer entities, MW claims, and planning references; then verify in the LPA portal or operator page.

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD), UK & Ireland / Construction | https://www.datacenterdynamics.com/en/news/ | Best open discovery feed for UK project proposals, approvals, expansions, acquisitions, and MW claims. Examples: DC01UK/Hertsmere, Manor Farm Slough, Elsham Tech Park, Kao Harlow, Vantage Wales. | B; promote to A only when it links to/quotes primary docs |
| The Register | https://www.theregister.com/tag/datacenter/ | Strong on policy, grid constraints, AI Growth Zones, planning controversy, and UK energy bottlenecks. Use for context and search leads, not final facility capacity unless independently confirmed. | B |
| Data Centre Review | https://datacentrereview.com/ | UK sector news; useful for FOI/statistical planning-application stories and energy/planning items. | B |
| techUK Data Centres Programme | https://www.techuk.org/developing-markets/data-centres.html | Industry-policy channel; useful for CNI/NSIP/AI Growth Zone positions and market context. techUK reported support for datacentres being allowed to opt into NSIP. | B |
| Data Centre Alliance (DCA) | https://www.dcauk.org/ | UK trade association and member directory. Use for operator/vendor universe, not facility enumeration. | B/C depending on item |
| Data Centre World London | https://www.techshowlondon.co.uk/data-centre-world | Conference/exhibitor list for vendor discovery; not evidence of a facility. | C |
| Planning Resource / council committee reports / law-firm planning notes | https://www.planningresource.co.uk/ plus council sites | Good for called-in/recovered appeals, Green Belt reasoning, and references; verify against decision letters. | B |
| Local business press | Insider Media, Place North West, BusinessCloud, Construction Enquirer, Yorkshire Post, BBC local | Good early leads for brownfield conversions and local approvals. Always pivot to LPA reference. | B/C |
| Directories | Cloudscene, DataCenterMap, Baxtel, OCOLO, Inflect, Colo-X, datacentresintheuk.com | Useful for operational legacy colocation sites and address/operator hints. Capacity is often stale or paywalled; grade B only when consistent with operator page, otherwise C. | C/B |

High-value DCD query examples:
```
site:datacenterdynamics.com/en/news/ "UK" "data center" "planning"
site:datacenterdynamics.com/en/news/ "approved" "data center" "UK"
site:datacenterdynamics.com/en/news/ "Slough" OR "Hertsmere" OR "Harlow" "data center"
site:datacenterdynamics.com/en/news/ "AI Growth Zone" "data center" "UK"
site:datacenterdynamics.com/en/news/ "Northumberland" OR "Lincolnshire" OR "Newport" "data center"
```

The Register / policy queries:
```
site:theregister.com "UK" "datacenter" "grid"
site:theregister.com "AI Growth Zone" "datacenters" "UK"
site:theregister.com "Slough" "datacenter"
site:theregister.com "planning" "datacenters" "UK"
```

---

## 2. Vendor/operator sweep (official pages = A for owned-site existence)

### 2.1 Major UK colo / wholesale operators to seed

| Operator/developer | UK geographies to check first | Official / useful page | Notes |
|---|---|---|---|
| Equinix | London Docklands, Slough, Manchester, South Mimms/Hertsmere | https://www.equinix.com/data-centers/europe-colocation/united-kingdom-colocation/london-data-centers | Official pages confirm metro/facility portfolio. Equinix bought DC01UK South Mimms in 2025 per DCD; verify planning via Hertsmere application 24/1152/OUTEI and council docs. |
| Digital Realty | Docklands, Slough, Crawley, Wokingham/Reading pipeline | https://www.digitalrealty.com/data-centers/emea/london | Includes legacy Interxion/Telecity estate; also check operator/customer PR. |
| VIRTUS Data Centres | Slough, Hayes, Stockley Park, Enfield, Park Royal | https://virtusdatacentres.com/locations/ | Major London/Thames Valley pure-play; official locations are strong for existing sites. |
| Ark Data Centres | Corsham/Wiltshire, Farnborough/Hampshire, potential Hertsmere/Watford | https://www.ark-d-c.com/locations/ | Spring Park/Corsham is a key secure campus; Wiltshire planning application PL/2024/05527 covers recent extension. |
| Kao Data | Harlow/Essex, Slough, Northolt, Manchester/Stockport | https://kaodata.com/locations/ | Harlow official page gives facility/phasing MW; DCD tracks KLON-03/04 expansion and Nebius lease. |
| Vantage Data Centers | Newport/Cardiff, Bridgend, potential South Wales AI Growth Zone | https://vantage-dc.com/ | Newport campus inherited from Next Generation Data; DCD reported 148MW full buildout and 80MW expansion approval. |
| NTT Global Data Centers | Hemel Hempstead/London region | https://services.global.ntt/en/services/data-centers | Official portfolio page; supplement with DCD/local planning. |
| Global Switch | London Docklands | https://www.globalswitch.com/locations/london/ | Large legacy interconnection site; official page for operational confirmation. |
| Telehouse / KDDI | London Docklands | https://www.telehouse.net/data-centres/london-data-centres/ | Carrier-dense Docklands facilities; good for operational estate. |
| Iron Mountain Data Centers | Slough / London corridor | https://www.ironmountain.com/data-centers/locations/london-data-center | Official page states LON-1/2/3 in Slough corridor and public MW totals. |
| CyrusOne | Slough/London | https://cyrusone.com/locations/europe/london/ | Check official page + local planning for phases. |
| Colt DCS | London metro | https://www.coltdatacentres.net/en-GB/our-locations | Official facility pages expose MW in some countries; verify UK pages. |
| iomart | Glasgow, Manchester, Nottingham, London, Leicester, Maidenhead | https://www.iomart.com/ | Mid-market operational estate; official pages plus DataCenterMap for addresses. |
| Pulsant | Edinburgh, Glasgow, Newcastle, Manchester, Reading, South London | https://www.pulsant.com/ | Edge/colo estate across regional UK; official page good for operational sites. |
| nLighten / Proximity / edge operators | Birmingham, Bristol, Cambridge, Leeds, Liverpool, Nottingham, Sheffield, Wolverhampton etc. | https://www.nlighten.eu/ | Useful for smaller regional divisions that lack hyperscale projects. |
| QTS / Blackstone | Cambois/Blyth, Northumberland | https://q.com/data-centers/cambois/ | QTS Cambois is a major new Northumberland campus; cross-check Northumberland Council and project docs. |
| Microsoft / Google / AWS / Oracle | UK South/London, Wales/Newport/Cardiff, Essex/North Yorkshire, cloud-region sites | official cloud infra pages below | Hyperscalers rarely publish street addresses; local consultation/planning sites are needed for physical projects. |

Operator query templates:
```
"{operator}" "{division}" "data centre"
"{operator}" "{town}" "MW" "data centre"
site:{operator-domain} "United Kingdom" "data centre" "{town}"
"{operator}" "planning application" "data centre" "{council}"
"{operator}" "public consultation" "data centre" "{town}"
```

### 2.2 Official hyperscale cloud region pages

These prove operational cloud-region presence at metro/region level, not exact facility addresses.

| Provider | Official page | UK signal |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | `eu-west-2` Europe (London), 3 AZs. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | UK South = London; UK West = Cardiff. |
| Google Cloud | https://cloud.google.com/about/locations | `europe-west2` London. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and https://www.oracle.com/cloud/uk-sovereign-cloud/ | UK South/London and UK West/Newport; sovereign cloud also London and Newport. |

Search hyperscaler projects separately:
```
"Google" "data centre" "Thurrock" OR "North Weald" OR "Essex"
"Microsoft" "data centre" "Newport" OR "Eggborough" OR "North Yorkshire"
"AWS" OR "Amazon" "data centre" "Slough" OR "London" "planning"
"Oracle" "Newport" "data centre" "UK West"
```

---

## 3. Local planning authority workflow (A-grade verification)

### 3.1 Core LPA query pattern

For each manifest division, identify the relevant council/LPA portal, then search:
```
"{division}" "planning" "data centre"
site:{council-domain} "data centre" "planning"
site:{council-domain} "datacentre" "planning"
site:{council-domain} "hyperscale" "data centre"
site:{council-domain} "server halls" "backup generators"
site:{council-domain} "Use Class B8" "data centre"
site:{council-domain} "energy centre" "data centre"
site:{council-domain} "substation" "data centre"
```

Inside the LPA portal search both British and US spelling:
```
data centre
datacentre
data center
hyperscale
server hall
backup generator
standby generator
BESS
energy centre
Use Class B8
```

Capture these fields from the planning file:
- application reference, applicant, land/site address, ward/parish, description of development;
- status: screening/scoping, submitted, committee recommended, approved, refused, appeal, called-in, recovered appeal, reserved matters, discharge of conditions, construction;
- documents: planning statement, design and access statement, energy statement, environmental statement, transport, noise, air quality, flood risk, committee report, decision notice, s106;
- capacity evidence: IT load MW, electrical import capacity/MVA, number of data halls, gross external area, backup generator count, substation rating, phasing.

### 3.2 National/appeal channels to search

- Planning Inspectorate National Infrastructure: https://national-infrastructure-consenting.planninginspectorate.gov.uk/ (use for any future datacentre DCO/NSIP case).
- GOV.UK recovered appeals / called-in decisions: search `site:gov.uk "data centre" "recovered appeal"` and `site:gov.uk "Poyle Road" "data centre"`.
- Example: Manor Farm Slough recovered appeal decision, ref 3366043, 10 June 2026: https://www.gov.uk/government/publications/recovered-appeal-land-at-manor-farm-and-land-north-of-wraysbury-reservoir-poyle-road-slough-ref-3366043-10-june-2026. Slough council points users to planning reference **P/10076/013** for the portal documents: https://www.slough.gov.uk/planning/public-inquiry-manor-farm.
- London applications: also check the Planning London Datahub (GLA): https://www.london.gov.uk/programmes-strategies/planning/digital-planning/planning-london-datahub.
- England open planning data: https://www.planning.data.gov.uk/entity/ and map/API. Use only as a partial index.

### 3.3 Examples of planning references / council routes

| Project | Division | Primary route |
|---|---|---|
| Manor Farm / Tritax 147MW Slough | England - Slough | Slough application search ref **P/10076/013** and GOV.UK recovered appeal ref **3366043**. |
| DC01UK / Equinix South Mimms | England - Hertfordshire | Hertsmere council item **24/1152/OUTEI**; council news confirms outline permission on 23 Jan 2025. |
| Elsham Tech Park | England - North Lincolnshire | North Lincolnshire planning ref **PA/2025/643**; council and DCD report outline permission in March 2026. |
| Google North Weald | England - Essex | Epping Forest District Council planning portal; DCD reports outline approval by Epping Forest DC on 10 Dec 2025. |
| Kao Harlow campus | England - Essex | Harlow District Council LDO/compliance applications + Kao official location page. |
| Ark Spring Park DC7 | England - Wiltshire | Wiltshire planning ref **PL/2024/05527**; council strategic planning committee approval. |

---

## 4. Per-division enumeration method (185 GB divisions)

The manifest uses county/unitary authority/council area/local government district divisions. Enumerate by **division -> LPA(s) -> industry/vendor sweep -> planning verification**.

### 4.1 England

1. For unitary/metropolitan borough divisions (Slough, Reading, Wokingham, Blackpool, Manchester, Birmingham, Leeds, North Lincolnshire), use the named council planning portal directly.
2. For county divisions with district LPAs (Hertfordshire, Essex, Hampshire, Lancashire, Lincolnshire, Surrey, Kent, West Sussex, etc.), search both county name and every district/borough inside it. Example: **Hertfordshire** needs Hertsmere, Three Rivers, Watford, Dacorum, Welwyn Hatfield, St Albans, Stevenage, East Herts, North Herts, Broxbourne.
3. Prioritize known English hotspots:
   - **Slough / Windsor and Maidenhead / Hillingdon / Hounslow / Ealing / Brent / Reading / Wokingham / Bracknell Forest / West Berkshire**: M4/Thames Valley and Heathrow corridor.
   - **Greater London**: Docklands (Tower Hamlets/Newham), Park Royal (Ealing/Brent), Hayes/Uxbridge (Hillingdon), Northolt, Enfield, Havering.
   - **Hertfordshire/Essex**: South Mimms/Hertsmere, Watford, Harlow, North Weald/Epping Forest, Basildon/Wickford, Thurrock.
   - **Wiltshire/Hampshire**: Corsham/Spring Park, Farnborough.
   - **Manchester/Stockport/Warrington/Liverpool/Leeds/Sheffield/Birmingham/Coventry/Nottingham/Leicester**: regional colo and brownfield conversion searches.
   - **Northumberland/North Tyneside/County Durham/North Yorkshire/East Riding/North Lincolnshire/Lincolnshire**: AI Growth Zone, power-station, former-industrial and freeport-led giga-campus searches.

### 4.2 Wales

1. Use Welsh unitary authority portals: Newport, Cardiff, Bridgend, Vale of Glamorgan, Wrexham, Swansea, etc.
2. Prioritize **Newport/Cardiff/Bridgend**. Vantage/NGD Newport, Microsoft Newport, Oracle UK West/Newport, and South Wales AI Growth Zone items create high project density.
3. Query in English; Welsh-language terms are uncommon in technical planning titles, but add `canolfan ddata` / `canolfan data` when searching Welsh council pages.
```
"Newport" "data centre" "planning"
site:newport.gov.uk "data centre"
"Bridgend" "Vantage" "data centre"
"South Wales" "AI Growth Zone" "data centre"
"canolfan ddata" "Newport" OR "Caerdydd"
```

### 4.3 Scotland

1. Planning is council-based; use ePlanning Scotland / council portals where available: https://eplanning.scot/.
2. Prioritize Glasgow City, City of Edinburgh, North Lanarkshire, South Lanarkshire, Fife, West Lothian, Aberdeen City/Aberdeenshire, Highland (renewables/edge/HPC), and central-belt industrial parks.
3. Query:
```
site:{council-domain} "data centre" "planning"
"Scotland" "data centre" "AI Growth Zone"
"Glasgow" OR "Edinburgh" "colocation" "data centre"
"data centre" "renewable" "Scotland" "MW"
```

### 4.4 Northern Ireland

1. Planning is through local councils, but many applications surface in the NI Planning Portal: https://planningregister.planningsystemni.gov.uk/.
2. Prioritize Belfast, Lisburn and Castlereagh, Armagh City Banbridge and Craigavon, and Derry City and Strabane.
3. Query:
```
site:planningregister.planningsystemni.gov.uk "data centre"
"Belfast" "data centre" "planning"
"Northern Ireland" "data centre" "colocation"
```

---

## 5. County / division search recipes

### 5.1 Universal county sweep

For each division `D`:
```
"{D}" "data centre"
"{D}" "datacentre"
"{D}" "data center"
"{D}" "hyperscale"
"{D}" "AI data centre"
"{D}" "colocation"
"{D}" "server hall"
"{D}" "backup generators" "data centre"
"{D}" "substation" "data centre"
"{D}" "BESS" "data centre"
site:datacenterdynamics.com/en/news/ "{D}"
site:theregister.com "{D}" "datacenter"
site:planning.org.uk "{D}" "data centre"
site:docs.planning.org.uk "{D}" "data centre"
```

Then pivot on each found project:
```
"{project name}" "planning statement"
"{project name}" "environmental statement"
"{project name}" "design and access statement"
"{project name}" "committee report"
"{project name}" "decision notice"
"{applicant SPV}" "data centre"
"{site address}" "data centre"
"{planning reference}"
```

### 5.2 Planning-document capacity extraction

Capacity is frequently hidden in PDFs. Search within downloaded PDFs for:
```
MW
MVA
IT load
electrical demand
power capacity
import capacity
data halls
server halls
generators
standby generation
PUE
gross external area
GEA
phasing
substation
```

Use MW hierarchy:
1. IT load MW from operator/planning statement = best capacity.
2. Grid import / MVA = upper electrical service, not IT load; record separately or caveat.
3. Generator count x rating = resilience plant, not IT load; use only for sanity checking.
4. Area-only statements (sqm/sq ft) cannot be converted without density assumptions; leave `capacity_mw: null` unless another source gives MW.

---

## 6. Known regional developer map (starting points)

| Region/divisions | Operators/developers to search |
|---|---|
| Slough / Royal Borough of Windsor and Maidenhead / Hillingdon / Reading / Wokingham / Bracknell | Equinix, VIRTUS, Digital Realty, Iron Mountain, CyrusOne, Global Switch, Ark, Kao, Tritax/Manor Farm, Microsoft/TVP, Oracle/AWS leads |
| Greater London | Telehouse, Global Switch, Digital Realty, Equinix, VIRTUS, Colt DCS, nLighten, Google/Havering/Digital Reef, Park Royal/Hayes/Northolt developers |
| Hertfordshire | Equinix/DC01UK South Mimms, Ark Watford/Hertsmere, NTT/Hemel Hempstead, local film/tech corridor projects |
| Essex | Kao Harlow, Google North Weald, Google Thurrock, Caineal Basildon/Wickford, Digital Reef/Havering (Greater London/Essex boundary), Epping Forest/Harlow/Thurrock/Basildon councils |
| Wales: Newport/Cardiff/Bridgend | Vantage/NGD, Microsoft, Oracle, South Wales AI Growth Zone, former industrial sites |
| Wiltshire/Hampshire | Ark Corsham/Spring Park, Ark Farnborough, defence/secure cloud sites |
| Northumberland/North East | QTS Cambois, Wansbeck Regeneration, North Tyneside/Stargate-style AI announcements; verify because some projects may pause or change sponsor |
| Yorkshire/Lincolnshire/Humber | Elsham Tech Park, Drax/Selby, Yorkshire Energy Park, Microsoft Eggborough, freeport/energy park proposals |
| North West | Kao Manchester/Stockport, Manchester regional colo, Warrington brownfield conversions, Liverpool/Greater Manchester edge operators |
| Midlands | Birmingham/Coventry/Nottingham/Leicester/Wolverhampton regional colo, industrial-estate conversions, hyperscale power-site proposals |
| Scotland | DataVita, Pulsant, iomart, Brightsolid, renewable/HPC proposals; use ePlanning Scotland and council portals |
| Northern Ireland | Belfast regional colo / government-cloud leads; use NI Planning Portal first |

---

## 7. Evidence grading rules for UK

| Evidence | Grade | Notes |
|---|---|---|
| LPA planning portal application, planning statement, environmental statement, committee report, decision notice | A | Primary for project existence, status, applicant, site, capacity if stated. |
| GOV.UK recovered appeal / Secretary of State decision / Planning Inspectorate DCO docs | A | Primary for called-in or nationally significant schemes. |
| Operator official facility page | A for existence/location; B for marketing capacity | Official but may show design-max capacity and omit phases. |
| Cloud provider region docs | A for operational cloud-region presence; not facility-level | Do not infer exact address. |
| Council news / committee minutes | A-/B+ | Strong status confirmation; planning file remains primary. |
| DCD / The Register / Data Centre Review / planning-law notes | B | Best discovery feed; verify with planning/operator evidence. |
| Cloudscene / DataCenterMap / Baxtel / OCOLO / Inflect / Colo-X | C/B | Useful for operational colo census and addresses; capacity must be verified or caveated. |
| LinkedIn, campaign sites, project marketing microsites | C unless backed by planning docs | Good for leads and consultation dates only. |

Status semantics:
- `announced`: press release, AI Growth Zone bid, consultation, or project microsite with no submitted planning application.
- `planned`: application submitted or pre-application/scoping evidence exists.
- `approved`: permission/outline permission/recovered appeal granted, but no construction evidence.
- `construction`: discharge of conditions, reserved matters, contractor mobilization, enabling works, or operator construction PR.
- `operational`: operator says live, tenant announced live capacity, or facility directory + operator service page corroborate.

---

## 8. Practical pitfalls

- **"London" often means not London**: Slough, Harlow, Hemel Hempstead, Crawley, Newport/Cardiff, and Reading/Wokingham facilities may be marketed as London-region sites. Bucket by physical LPA/division, not metro marketing name.
- **County vs LPA mismatch**: GeoNames admin2 divisions include counties and unitary authorities. A county division may require 5-15 district portal searches.
- **Green Belt / grey belt appeals**: major projects can be refused locally but approved by Secretary of State; always search GOV.UK and Planning Resource for the project name.
- **Power claims can be speculative**: UK grid-queue stories include inflated or speculative GW demand. Count a project only when tied to site/applicant/planning evidence.
- **AI Growth Zone does not equal a datacentre**: it is a policy/site-enabling designation. Record named facilities separately; keep region-level AGZ claims as C unless a site and developer are named.
- **Directory duplicates**: one campus can appear as operator brand, tenant brand, building name, and acquired former operator (e.g. NGD/Vantage, Telecity/Digital Realty, 4D/Redcentric/Stellanor). Dedupe on address + operator lineage.

---

## 9. Recommended GB discovery pipeline

1. **Seed high-signal projects** from DCD UK searches, The Register policy/grid stories, Data Centre Review, techUK/DCA, and local business press.
2. **Vendor sweep** major operators in §2; record official location pages and public MW where available.
3. **Per-division LPA sweep** using §4-§5. For county divisions, enumerate district LPAs first.
4. **National decision sweep** for large projects: Planning Inspectorate, GOV.UK recovered appeals, AI Growth Zone guidance/news.
5. **Directory backfill** for smaller operational colocation facilities in divisions with no hyperscale projects.
6. **Verify and grade**: planning/operator evidence for A/B; trade press as B lead; directories as C unless corroborated.
7. **Dedupe** by physical address, planning reference, applicant SPV, operator ultimate parent, and phase.

Quick URL index:
- DCD UK news: https://www.datacenterdynamics.com/en/news/
- The Register datacenter tag: https://www.theregister.com/tag/datacenter/
- techUK datacentres: https://www.techuk.org/developing-markets/data-centres.html
- DCA: https://www.dcauk.org/
- Planning.data.gov.uk: https://www.planning.data.gov.uk/
- Planning Inspectorate NSIP: https://national-infrastructure-consenting.planninginspectorate.gov.uk/
- Planning Portal: https://www.planningportal.co.uk/
- ePlanning Scotland: https://eplanning.scot/
- NI Planning Register: https://planningregister.planningsystemni.gov.uk/
- Slough Manor Farm recovered appeal: https://www.gov.uk/government/publications/recovered-appeal-land-at-manor-farm-and-land-north-of-wraysbury-reservoir-poyle-road-slough-ref-3366043-10-june-2026
- AI Growth Zones: https://www.gov.uk/government/publications/delivering-ai-growth-zones/delivering-ai-growth-zones
