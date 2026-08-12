# IE Explorer Industry - Ireland Datacenter Enumeration via Operators, Trade Press, IXPs, Cables, and Aggregators

Date: 2026-08-12. Scope: Ireland (IE). Division model: **province**: **Leinster; Munster; Connacht (repo may spell Connaught); Ulster**. In Ulster, include only Republic of Ireland counties **Cavan, Donegal, Monaghan**; the other six Ulster counties are Northern Ireland / UK and out of scope.

Angle: industry/vendor discovery. Use this file to find leads, operator aliases, campus names, connectivity signals, and market status. Use the official file to confirm planning, EPA, and grid facts.

Reliability grades:

- **A** - operator-owned pages, cloud-provider official region pages, IXP official pages, IDA announcements for the announcement itself, regulator/official records.
- **B** - reliable trade/business/local press and regulator-adjacent analysis: DCD, RTE, Irish Times, Business Post, Silicon Republic, The Journal, Total Telecom, law-firm briefs, named local press.
- **C** - aggregators/directories and trackers: Baxtel, DatacenterMap, OCOLO, datacenters.com, PeeringDB for self-entered facility metadata, Uptime listings, market reports.
- **U** - unverified; do not count without follow-up.

Grade each fact separately. Operator pages are A for facilities the operator markets, but capacity/build status still needs planning/EPA/press corroboration. Aggregator counts are never a census.

---

## 0. Market Structure

Ireland's commercial datacenter market is dominated by the greater Dublin region: Grange Castle, Clonshaugh/Profile Park, Blanchardstown/Ballycoolin, Citywest/Kilcarbery, and related sites in Meath, Louth, Kildare, Wicklow, and Westmeath. Grid constraints and CRU/EirGrid policy have pushed new proposals outward from Dublin.

Important non-facility signals:

- Electricity demand: CSO reported datacenters at 22% of metered electricity in 2024 and 23% in 2025. Use CSO/RTE as background, not facility evidence.
- Connectivity: INEX, Dublin colocation campuses, and subsea cables make Dublin the main Irish interconnection hub. Cork has a smaller but real IXP/colo role through CIX/INEX.
- Associations: Digital Infrastructure Ireland and IDCSA surface member/operator/vendor leads, not a facility registry.
- Cloud regions: AWS and Azure have Ireland regions; Google Cloud and Oracle OCI do not have standard public Ireland regions on their official public-region lists as of this review. Google and Oracle-related infrastructure claims still require separate facility evidence.

---

## 1. Discovery Queries

General:

```text
Ireland OR Dublin "data centre" 2025 OR 2026
"{operator}" Ireland "data centre" campus
"{county}" "data centre" planning 2025 OR 2026
"data centre" "{town}" MW OR MVA OR MIC
"data centre" "An Coimisiun Pleanala" OR "An Bord Pleanala"
"data centre" "High Court" Ireland
"ionad sonrai" "{county}"
```

Trade and status:

```text
site:datacenterdynamics.com Ireland data center OR data centre
site:siliconrepublic.com "data centre" Ireland
site:rte.ie "data centre" Ireland
site:irishtimes.com "data centre" "{county}"
site:thejournal.ie "data centre" Ireland
"{project}" "breaking ground" OR construction OR commissioning OR operational
"{project}" judicial review OR appeal OR refused OR granted
"{operator}" Ireland PUE OR power OR renewables OR microgrid
```

Associations and events:

```text
site:digitalinfrastructure.ie data centre member
site:idcsa.ie data centre
site:datacentres-ireland.com exhibitor data centre
"Host in Ireland" "data centre" member
```

Aggregators and connectivity:

```text
site:peeringdb.com Dublin data center facility
site:datacentermap.com ireland data center
site:baxtel.com Ireland data center
site:ocolo.io Ireland data center
site:uptimeinstitute.com Ireland data centre
site:inex.ie Dublin Cork data centre
Ireland submarine cable landing station Dublin Galway
"Farice" Galway cable
"Aqua Comms" Ireland cable landing
"Narwhal" Ireland transatlantic cable
```

---

## 2. Industry Source Map

### Associations and Events

- Digital Infrastructure Ireland: https://www.digitalinfrastructure.ie/ . B+ for ecosystem/member leads; not a facility census.
- IDCSA: https://idcsa.ie/ . B for supplier ecosystem; not facility evidence.
- DataCentres Ireland: https://www.datacentres-ireland.com/ . B/C for exhibitors, sponsors, vendor leads.
- IDA Ireland: https://www.idaireland.com/latest-news . A for IDA announcements, but a project still needs planning/operator confirmation.
- ICHEC: https://www.ichec.ie/ . Research/HPC context, not commercial datacenter enumeration.

### Trade and Business Press

- DCD Ireland tag: https://www.datacenterdynamics.com/en/tags/ireland/ . B; strongest routine trade source.
- Silicon Republic: https://www.siliconrepublic.com/ . B; useful for Ireland planning, Google, AWS, INEX/Cork.
- RTE Business: https://www.rte.ie/news/business/ . B; useful for major planning decisions and CSO statistics.
- Irish Times / Business Post / The Journal / Irish Independent. B; strongest when they name applicant, ref, decision date, or court outcome.
- Regional press: Connaught Telegraph, Western People, Clare Echo, Westmeath Independent/Examiner, Offaly Independent. B when they name applicants and local-authority actions.
- Law firms: William Fry, Mason Hayes & Curran, Algoodbody, ByrneWallace, Philip Lee, Beauchamps. B for readable summaries of CRU/planning/JR decisions; cite the official decision when available.

### Operators and Official Pages

| Operator / signal | Official source | Ireland use |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | `eu-west-1` region. Search Amazon Data Services Ireland Ltd, AWS Dublin, Drogheda, Mulhuddart, Clonshaugh, Tallaght, Premier Periclase. |
| Microsoft | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Azure North Europe = Ireland. Search Grange Castle/South Dublin and Microsoft Ireland planning. |
| Google | https://cloud.google.com/about/locations and https://datacenters.google/locations | No GCP Ireland public region; Google corporate data-center presence in Ireland requires separate planning/operator evidence. |
| Meta | https://datacenters.atmeta.com/all-locations/ | Clonee, Co. Meath. Owned campus, not cloud region. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No standard OCI commercial public Ireland region on official table. Do not count Oracle Database@AWS Dublin as an Oracle datacenter. |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/dublin | Major Dublin colo portfolio: DUB facilities across Blanchardstown, Clonshaugh/Profile Park, Grange Castle. Normalize legacy Interxion names. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/ireland-colocation/dublin-data-centers | DB1/DB2/DB3/DB4/DB6x/DB7x/DB8 signals. Official page for marketed sites; planning for expansions. |
| CyrusOne | https://www.cyrusone.com/ | Dublin I / Grange Castle Business Park South lead. DCD is stronger for 74MW ground-breaking details. |
| Pure DC | https://puredc.com/dublin | Ballycoolin/Orion Business Park campus. Verify power/microgrid claims with official records where material. |
| Echelon Data Centres | https://echelon-dc.com/ | DUB20 Arklow is active; DUB30/DUB40/Dublin sites are pipeline/verify items. Official DUB20 page: https://echelon-dc.com/echelon-launches-irelands-first-green-energy-park/ . |
| Vantage Data Centers | https://vantage-dc.com/ | Dublin market-entry announcement is a lead until location/planning refs are confirmed. |
| CIX | https://cix.ie/ | Cork/Hollyhill colo and INEX Cork signal; confirmed Munster anchor. |
| Blacknight | https://www.blacknight.com/colocation/ | Small colo/hosting; Carlow and Dublin leads need facility-level verification. |
| Servecentric | https://www.servecentric.com/ | Dublin/Blanchardstown hosting/colo lead; verify current facility claims. |
| Lumcloon / Red Admiral DC | https://lumcloonenergy.com/red-admiral/ | Westmeath/Rochfortbridge datacenter and energy project lead; reconcile with Westmeath planning and ACP appeals. |

### IXPs, Cables, and Directories

- INEX: https://www.inex.ie/ . A for IXP existence and INEX-published locations; use facility names to seed operator records.
- PeeringDB: https://www.peeringdb.com/ . B/C for facility metadata and network presence; self-maintained, not a permit source.
- DatacenterMap: https://www.datacentermap.com/ireland/ . C seed only.
- Baxtel: https://baxtel.com/ . C/B- seed only; useful for facility aliases and construction news links.
- OCOLO: https://www.ocolo.io/ . C seed only.
- Uptime Institute: https://uptimeinstitute.com/ . B for certification facts when a certificate can be found; not a census.
- Aqua Comms: https://www.aquacomms.com/ and EXA acquisition release https://exainfra.net/media-centre/press-releases/exa-infrastructure-enters-into-agreement-to-acquire-aqua-comms/ . A for corporate/cable-owner claims.
- Submarine Cable Map: https://www.submarinecablemap.com/ . B/C for landing-station discovery; verify material landing details with cable owners or planning records.
- Farice Galway lead: https://oceannews.com/news/subsea-cable/galway-to-become-a-gateway-to-connectivity-to-northern-europe/ . B connectivity signal, not a datacenter.
- MDM Narwhal lead: https://subtelforum.com/mdm-announces-narwhal-1-and-2-transatlantic-cables/ . B connectivity signal, not a datacenter.

---

## 3. Province-by-Province Industry Approach

| Province | Counties | Expected activity | Priority industry signals |
|---|---|---|---|
| **Leinster** | Carlow, Dublin, Kildare, Kilkenny, Laois, Longford, Louth, Meath, Offaly, Westmeath, Wexford, Wicklow | Highest activity. Dublin colo/hyperscale core plus overflow to Meath, Louth, Kildare, Wicklow, Westmeath. | AWS, Azure/Microsoft, Google, Meta, Digital Realty, Equinix, CyrusOne, Pure DC, Echelon, Vantage, Herbata, Red Admiral/Lumcloon, Blacknight Carlow. |
| **Munster** | Clare, Cork, Kerry, Limerick, Tipperary, Waterford | Moderate. Ennis is the major active project; Cork has regional colo/IXP. | Art Data Centres Ennis, CIX Hollyhill, INEX Cork, any Limerick/Waterford/Tipperary planning leads. |
| **Connacht** | Galway, Leitrim, Mayo, Roscommon, Sligo | Low to moderate. Killala/Mayo is live; Apple Athenry historical; Galway cable leads. | Mayo Data Hub/AVAIO Killala, Farice Galway, Athenry historical cleanup, small colo/hosting sweeps. |
| **Ulster (IE)** | Cavan, Donegal, Monaghan | Very low. No confirmed major datacenter found; Donegal has supply-chain signals. | Vertiv Letterkenny, Cavan/Donegal/Monaghan planning sweeps, avoid Northern Ireland imports. |

---

## 4. Known Industry Signals and Evidence Status

| Facility / signal | Province (county) | Status | Evidence + grade | Industry use |
|---|---|---|---|---|
| AWS Ireland region and Irish facilities | Leinster | OPER/UC | AWS official region docs (A); DCD/RTE/Irish press for facility projects (B) | Seed Amazon Data Services Ireland Ltd, Dublin, Drogheda, Mulhuddart, Clonshaugh, Tallaght. |
| Microsoft Azure North Europe / Grange Castle | Leinster (Dublin) | OPER | Microsoft region list (A) | Region and South Dublin campus seed; planning confirms buildings. |
| Google Dublin / Grange Castle | Leinster (Dublin) | OPER; expansion/refusal watch | Google data-center locations (A); Silicon Republic SDCC refusal (B) | Do not infer GCP Ireland public region. Track new planning attempts. |
| Meta Clonee | Leinster (Meath) | OPER | Meta official location page/info sheet (A) | Anchor Meath facility; search Facebook/Meta aliases. |
| Digital Realty Dublin portfolio | Leinster (Dublin) | OPER/UC | Operator page (A) | Normalize DUB codes and Interxion legacy names; verify each site before counting. |
| Equinix Dublin portfolio | Leinster (Dublin) | OPER/UC | Operator page (A), DCD/law/council updates (B/A) | DB7x/DB8 status requires official planning follow-up. |
| CyrusOne Dublin I | Leinster (Dublin) | UC/status verify | DCD ground-breaking (B) | Strong lead; planning/EPA needed for status and power. |
| Pure DC Dublin | Leinster (Dublin/Fingal) | OPER | Pure DC official page (A) | Campus lead; verify capacity/microgrid claims. |
| Echelon DUB20 Arklow | Leinster (Wicklow) | UC | Echelon official DUB20 page (A for company status), DCD ground-breaking (B) | Major Wicklow record; DUB30/DUB40 are watch items. |
| Vantage Dublin | Leinster (Dublin) | PRO | CRE Herald (B) | Do not count until an operator page or planning ref identifies the campus. |
| Herbata Naas | Leinster (Kildare) | PLN/appealed | Kildare decision list (A), DCD/ClientEarth/FIE (B) | Add to active Leinster watchlist; high climate/JR risk. |
| Red Admiral / Lumcloon Rochfortbridge | Leinster (Westmeath) | PLN/appealed | Lumcloon project page (A for sponsor claim), RTE/The Journal/local press (B) | Major new midlands lead; reconcile planning conditions and appeal status. |
| Art Data Centres Ennis | Munster (Clare) | PLN/enabling works watch | William Fry/The Journal/DCD (B) | Major non-Dublin project; verify official Clare/ACP/EPA records. |
| CIX / Cork Internet Exchange | Munster (Cork) | OPER | CIX official (A) | Cork colo/INEX anchor; not hyperscale. |
| INEX Dublin and Cork peering points | Leinster + Munster | OPER | INEX official (A) | Use INEX sites to seed facility aliases and carrier-neutral facilities. |
| Mayo Data Hub / AVAIO Killala | Connacht (Mayo) | PLN/appealed | Western People / Irish Times / DCD (B) | Verify Mayo and ACP records before upgrading status. |
| Apple Athenry | Connacht (Galway) | HIST | RTE/BBC/DCD (B) | Historical/cancelled; suppress from active counts. |
| Farice Galway cable | Connacht (Galway) | PRO cable | Ocean News (B) | Connectivity lead only. |
| Aqua Comms / EXA Irish cable systems | Leinster/coastal | OPER/PRO cable | Aqua Comms/EXA official (A) | Connectivity lead only; exact landing stations require verification. |
| Vertiv Letterkenny | Ulster (Donegal) | OPER supply chain | IDA release (A) | Not a datacenter; supply-chain context. |

---

## 5. Industry Enumeration Workflow

1. Seed from operator pages and cloud-region pages: AWS, Microsoft, Google, Meta, Digital Realty, Equinix, CyrusOne, Pure DC, Echelon, Vantage, CIX, Blacknight, Servecentric, Lumcloon/Red Admiral.
2. Sweep DCD, Silicon Republic, RTE, Irish Times, Business Post, The Journal, and regional press for the newest status.
3. For each lead, capture aliases: parent company, Irish SPV/applicant, campus code, legacy operator name, townland, business park, county, province.
4. Promote to the official pipeline: planning register, ACP, EPA/LEAP, CRU/EirGrid if named, IDA/gov.ie if announcement-level.
5. Split each record into separately graded facts: existence, address, planning decision, appeal/JR status, construction, operational status, power/MIC, IT load, floor area, tenant.
6. De-duplicate by campus and building code. Common aliases include Interxion/Digital Realty, Facebook/Meta, AWS/Amazon Data Services Ireland, Microsoft/Azure, Red Admiral/Lumcloon.
7. Keep C-grade aggregator facts in a lead queue until confirmed elsewhere.

---

## 6. Pitfalls

- Aggregator facility counts for Dublin vary widely and are not comparable. Never cite them as Ireland's facility count.
- Cloud regions are logical service regions. They are not exact facility locations.
- Google has an Irish data-center presence but no Google Cloud Ireland public region on the official locations list.
- Oracle Database@AWS in Dublin does not establish an OCI Ireland public region.
- Cable landings, IXPs, and equipment factories are digital infrastructure signals, not datacenters.
- Self-generation claims such as gas turbines, fuel cells, microgrids, batteries, and solar farms need planning/EPA/CRU context; they are often the litigated part of the project.
- Dublin campus codes can refer to multiple buildings or phases. Count buildings only when the source distinguishes them.
- Ulster must not pull in Belfast or other Northern Ireland facilities.

---

## 7. Re-Check Cadence

- **Weekly**: DCD Ireland tag, RTE Business, Silicon Republic, Irish Times/Business Post/The Journal, regional press for Ennis, Naas, Rochfortbridge, Killala, Drogheda, Arklow.
- **Monthly**: operator pages for Digital Realty, Equinix, Pure DC, Echelon, CyrusOne, AWS, Microsoft, Google, Meta, Vantage, Lumcloon/Red Admiral; PeeringDB new Dublin/Cork facilities.
- **Quarterly**: Digital Infrastructure Ireland, IDCSA, DataCentres Ireland exhibitors, Uptime lookups, Baxtel/DatacenterMap/OCOLO seed sweeps, INEX site/member pages, cable news.
- **Annually**: complete province coverage audit and refresh cloud-region pages for AWS, Azure, Google Cloud, Oracle OCI, and Meta locations.
