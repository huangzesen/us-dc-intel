# IE Explorer Official - Ireland Datacenter Enumeration via Planning, Energy, EPA, Cloud Regions, and Official Registries

Date: 2026-08-12. Scope: Ireland (IE). Division model: **province**; cover exactly these repo divisions: **Leinster; Munster; Connacht (repo may spell Connaught); Ulster**. For Ulster, include only the Republic of Ireland counties **Cavan, Donegal, Monaghan**; Antrim, Armagh, Down, Fermanagh, Londonderry/Derry, and Tyrone are Northern Ireland / UK and are out of scope.

Reliability grades are per fact, not per source page:

- **A** - official or primary: local-authority planning register/decision, ePlan record, An Coimisiun Pleanala case file/decision, EPA IE/IPC licence or LEAP record, CRU/EirGrid/ESB Networks official document, CSO/Oireachtas/gov.ie publication, IDA press release for the announcement itself, cloud-provider official region list, operator-owned facility page for existence/location.
- **B** - reliable secondary: DCD, RTE, Irish Times, Business Post, Silicon Republic, The Journal, named local press, law-firm briefs that summarise official decisions.
- **C** - aggregators/trackers: Baxtel, DatacenterMap, OCOLO, datacenters.com, BuildingInfo, market reports. Use only as leads.
- **U** - unverified. Do not count a facility or status from U evidence.

A grade supports only the fact it actually proves. A council grant is A for the decision and conditions, not for construction start. A cloud-region page proves region availability, not physical campus addresses.

---

## 0. Ireland-Specific Operating Facts

Ireland has **no single national public datacenter facility register**. Official enumeration is a reconciliation task across local planning registers, An Coimisiun Pleanala, EPA licensing, grid-connection policy, government statistics, IDA announcements, cloud-region pages, and operator pages.

Planning is local-authority based. Ireland has 31 local authorities: 26 county councils, 3 city councils (Dublin, Cork, Galway), and 2 city-and-county councils (Limerick, Waterford). The four Dublin planning authorities are Dublin City, Dun Laoghaire-Rathdown, Fingal, and South Dublin.

Planning law remains grounded in the Planning and Development Act 2000 as amended. The Planning and Development Act 2024 is being commenced in stages and restructured An Bord Pleanala into **An Coimisiun Pleanala**. Search both names; the live domain is https://www.pleanala.ie/en-ie/home .

Large datacenters can appear as Strategic Infrastructure Development (SID) or as ordinary local-authority applications with appeal to An Coimisiun Pleanala. Do not assume every hyperscale project has a council-only record.

Energy is the gating layer. The CRU 2021 datacenter connection framework restricted new grid connections, especially around Dublin. The CRU published a new electricity connection policy for data centres on 2025-12-12, **CRU/2025236**, at https://www.cru.ie/about-us/news/the-cru-publishes-its-decision-on-new-electricity-connection-policy-for-data-centres/ . EirGrid implements it through **Data Centre Connection Offer Process and Policy Version 3 (DCCOPP v3)** on https://www.eirgrid.ie/industry/becoming-customer/demand-connections . Treat CRU/EirGrid as A for policy, but normally not as facility evidence unless a named connection is published.

Datacenters with large backup/emergency generation may require EPA Industrial Emissions / IPC licensing, commonly under energy combustion classes. Use EPA licence search https://www.epa.ie/our-services/licensing/licencesearch/ and LEAP https://leap.epa.ie/ . EPA is A for licensed emissions infrastructure, but it is not a complete datacenter census.

Official demand context is available from CSO. CSO reported datacenters consumed **22% of metered electricity in 2024** (https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2024/keyfindings/) and RTE reported CSO's 2025 share as **23%** in July 2026 (https://www.rte.ie/news/business/2026/0707/1582175-cso-data-centre-energy-figures/). Use the newest CSO release for current background numbers.

Cloud-region facts:

| Provider | Official source | Ireland signal | Use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | `eu-west-1`, Europe (Ireland), 3 AZs | A for region existence. Use planning/EPA/operator records for campuses. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | North Europe = Ireland | A for region existence. Seed Grange Castle/South Dublin searches. |
| Google Cloud | https://cloud.google.com/about/locations | No Google Cloud public region in Ireland on the official locations list | Google has an Irish data center presence, but GCP region docs do not prove an Ireland public cloud region. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No OCI commercial public region in Ireland on the official commercial-region table | Do not infer Irish OCI facilities from Oracle services hosted in AWS Dublin or dedicated/cloud-at-customer offerings. |
| Meta | https://datacenters.atmeta.com/all-locations/ | Clonee, County Meath | A for owned-campus existence; not a public cloud region. |

---

## 1. Search Vocabulary

Use English first; Ireland's planning and regulator records are primarily in English. Run Irish/Gaeilge only as a supplementary sweep.

```text
data centre
data center
datacentre
datacenter
server farm
colocation
colo
hosting
cloud region
digital infrastructure
strategic infrastructure
grid connection
MIC
MVA
Industrial Emissions licence
IPC licence
```

Irish-language supplementary terms:

```text
ionad sonrai
ionad sonrai data centre
freastalai
freastalaithe
feirm freastalaithe
nealriomhaireacht
bonneagar digiteach
cead pleanala
cabla fomhuiri
```

Core query bundle:

```text
site:eplanning.ie "data centre" "{county}"
site:{council-domain} "data centre"
"{council}" "data centre" "planning permission"
"{operator}" "{town}" "data centre" planning
site:pleanala.ie "data centre"
"An Coimisiun Pleanala" "data centre" "{county}"
"An Bord Pleanala" "data centre" "{county}"
site:epa.ie "data centre" "{operator}"
site:leap.epa.ie "data centre"
"{operator}" "Industrial Emissions" licence Ireland
site:cru.ie "data centre"
site:eirgrid.ie "DCCOPP" "data centre"
site:esbnetworks.ie "data centre" connection
site:gov.ie "data centres" Ireland enterprise strategy
site:cso.ie data centres metered electricity consumption
```

Extract these fields from each official record: planning ref, appeal/SID ref, applicant/SPV, operator/tenant if named, address, townland, county, province, site area, gross floor area, number of data halls/buildings, backup-generation capacity, MIC/MVA/MW if stated, water/cooling assumptions, decision, decision date, conditions, appeal/JR status, EPA licence ref, source URL, and evidence grade.

---

## 2. Official Source Backbone

### Planning Registers

- National ePlan: https://www.eplanning.ie/ . A for records served through the platform. Council participation varies, so always check the council's own planning page too.
- An Coimisiun Pleanala: https://www.pleanala.ie/en-ie/home . A for SID, appeal, and decision records. The data.gov.ie ACP dataset page points users back to pleanala.ie for current cases: https://data.gov.ie/dataset/cases-2016-onwards-received-or-decided-by-an-bord-pleanala-on-or-after-1st-january-2016 .
- Dublin City planning search: https://www.dublincity.ie/planning-and-land-use/find-planning-application/view-or-search-planning-applications .
- Donegal planning search: https://www.donegalcoco.ie/en/services/planning/search-a-planning-application .
- Mayo planning search: https://www.mayo.ie/en-ie/your-council/services/planning/planning-applications/search-for-planning .
- eTenders: https://www.etenders.gov.ie/ . A for procurement notices; mostly hosting/services rather than private datacenter construction.

High-priority planning authorities by province:

| Province | Planning authorities to search every cycle |
|---|---|
| Leinster | Dublin City, Fingal, South Dublin, Dun Laoghaire-Rathdown, Meath, Louth, Kildare, Wicklow, Westmeath, Offaly, Carlow, Laois, Longford, Kilkenny, Wexford |
| Munster | Clare, Cork City, Cork County, Limerick, Tipperary, Waterford, Kerry |
| Connacht | Galway City, Galway County, Mayo, Sligo, Roscommon, Leitrim |
| Ulster (IE) | Cavan, Donegal, Monaghan |

### Energy and Grid

- CRU: https://www.cru.ie/ . Key verified page: CRU decision on new electricity connection policy for data centres, 2025-12-12, https://www.cru.ie/about-us/news/the-cru-publishes-its-decision-on-new-electricity-connection-policy-for-data-centres/ .
- CRU proposed LEU decision consultation CRU/202504: https://consult.cru.ie/en/consultation/review-large-energy-users-connection-policy .
- EirGrid demand connections / DCCOPP v3: https://www.eirgrid.ie/industry/becoming-customer/demand-connections .
- ESB Networks: https://www.esbnetworks.ie/ . Search for distribution-level connection process material, but prefer CRU/EirGrid for datacenter-specific policy.
- Government data-centre enterprise statement: https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/government-statement-on-the-role-of-data-centres-in-irelands-enterprise-strategy/ .
- Oireachtas Library research on data centres and energy: https://data.oireachtas.ie/ie/oireachtas/libraryResearch/2024/2024-07-23_spotlight-data-centres-and-energy_en.pdf .

### EPA and Environmental Records

- EPA licence search: https://www.epa.ie/our-services/licensing/licencesearch/ .
- LEAP online register: https://leap.epa.ie/ .
- IE/IPC open dataset: https://data.gov.ie/dataset/industrial-emissions-ie-and-integrated-pollution-control-ipc-facilities .
- Use EPA as a confirmation layer for backup-generation/emissions infrastructure. Absence from EPA does not prove absence of a datacenter.

### Government, Statistics, and Regulators

- CSO datacenter electricity releases: https://www.cso.ie/en/releasesandpublications/ep/p-dcmec/datacentresmeteredelectricityconsumption2024/ .
- IDA Ireland newsroom: https://www.idaireland.com/latest-news . A for FDI announcements and jobs/capital claims made by IDA; still cross-check physical facilities with planning/EPA/operator pages.
- ComReg: https://www.comreg.ie/ . A for telecom regulatory context only; no facility census.
- DPC: https://www.dataprotection.ie/ . A for data-protection legal context only; no facility census.
- OGCIO: https://www.ogcio.gov.ie/ . Useful for public-sector hosting context, not private facility enumeration.

---

## 3. Province Coverage and Expectations

| Province | Counties in scope | Current expectation and official-first focus |
|---|---|---|
| **Leinster** | Carlow, Dublin, Kildare, Kilkenny, Laois, Longford, Louth, Meath, Offaly, Westmeath, Wexford, Wicklow | Ireland's main hub. Search Dublin x4, Meath/Clonee, Louth/Drogheda, Kildare/Naas, Wicklow/Arklow, Westmeath/Rochfortbridge, Offaly/Lumcloon first. |
| **Munster** | Clare, Cork, Kerry, Limerick, Tipperary, Waterford | Moderate. Ennis/Art Data Centres is a major active project; Cork has confirmed regional colo/IXP infrastructure. Other counties are lower-yield but must be swept. |
| **Connacht** | Galway, Leitrim, Mayo, Roscommon, Sligo | Low to moderate. Apple Athenry is historical/cancelled; Killala/Mayo is a live permitted/appealed project; Galway cable activity is connectivity context. |
| **Ulster (IE only)** | Cavan, Donegal, Monaghan | Very low. Donegal has datacenter supply-chain activity such as Vertiv Letterkenny, but no confirmed major datacenter facility found in this review. Sweep all three councils to preserve coverage. |

---

## 4. Known Facilities and Projects - Official Evidence Status

Status legend: OPER = operational; UC = under construction; PLN = planning/approved/appealed; PRO = proposed/lead; HIST = historical/cancelled. Grades apply to the cited fact.

| Facility / project | Province (county) | Status | Evidence + grade | Notes |
|---|---|---|---|---|
| AWS `eu-west-1` Europe (Ireland) region | Leinster (Dublin region) | OPER | AWS region docs (A): https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Region existence only; do not use for campus addresses. |
| AWS Dublin-area facilities | Leinster (Dublin/Fingal/South Dublin) | OPER/UC | Planning/EPA records under Amazon Data Services Ireland Ltd should be primary (A); DCD/RTE/Irish press are B leads | Search Clonshaugh, Tallaght, Mulhuddart, Ballycoolin, and legal-entity aliases. |
| AWS Drogheda / Premier Periclase site | Leinster (Louth) | PLN/UC | RTE on 2020 conditional permission (B): https://www.rte.ie/news/business/2020/0207/1113886-amazon-gets-green-light-for-drogheda-data-centre/ ; Business Post / Irish Times for later phase and objections (B) | Verify current Louth County Council refs and appeal status before classifying as under construction. |
| Microsoft Azure North Europe / Grange Castle | Leinster (South Dublin) | OPER/expanding | Azure region list (A): https://learn.microsoft.com/en-us/azure/reliability/regions-list ; planning records and Microsoft local pages for campus detail | A for region; use South Dublin planning for buildings. |
| Google Dublin data center, Grange Castle | Leinster (South Dublin) | OPER; new permission refused in 2024 | Google data-center locations (A for corporate location list): https://datacenters.google/locations ; Silicon Republic on SDCC refusal (B): https://www.siliconrepublic.com/business/google-dublin-data-centre-planning-permission-ireland-refused-grange-castle | Google Cloud has no Ireland public region on the official GCP locations page. Verify any 2025-2026 appeal or fresh application. |
| Meta Clonee data center | Leinster (Meath) | OPER | Meta official locations and Clonee sheet (A): https://datacenters.atmeta.com/all-locations/ ; https://datacenters.atmeta.com/asset/clonee-data-center-info-sheet/ | Search Meath records for phases and conditions. |
| Digital Realty / Interxion Dublin portfolio | Leinster (Dublin) | OPER/UC | Digital Realty official Dublin pages (A): https://www.digitalrealty.com/data-centers/emea/dublin | A for marketed facilities; planning/EPA needed for construction chronology and generation. |
| Equinix Dublin portfolio | Leinster (Dublin) | OPER/UC | Equinix official Dublin page (A): https://www.equinix.com/data-centers/europe-colocation/ireland-colocation/dublin-data-centers | DB7x/DB8 status needs planning and DCD/law-report cross-checks. |
| CyrusOne Dublin I, Grange Castle Business Park South | Leinster (South Dublin) | UC/status verify | DCD ground-breaking report (B): https://www.datacenterdynamics.com/en/news/cyrusone-breaks-ground-wildlife-friendly-dublin-campus/ | Use SDCC records for exact refs and conditions; operator page may not expose full status. |
| Pure DC Dublin, Ballycoolin/Orion Business Park | Leinster (Fingal) | OPER | Pure DC official page (A): https://puredc.com/dublin | A for campus marketing claims; verify power/microgrid details against planning/EPA where material. |
| Echelon DUB20 Arklow and wider Irish pipeline | Leinster (Wicklow/Dublin) | UC/PRO | Echelon official DUB20 Green Energy Park page (A for company claim): https://echelon-dc.com/echelon-launches-irelands-first-green-energy-park/ ; DCD on 2025 ground-breaking (B) | DUB20 in Arklow is the clearest Wicklow project; verify DUB30/DUB40 and Dublin-site refs separately. |
| Vantage Dublin campus | Leinster (Dublin) | PRO | CRE Herald (B): https://www.creherald.com/vantage-data-centers-enters-irish-market-with-e1bn-dublin-investment/ | Announcement only until planning/operator page identifies location and refs. |
| Herbata Ltd Naas data-centre campus | Leinster (Kildare) | PLN/appealed | Kildare County Council EIAR decision list (A): https://kildarecoco.ie/AllServices/Planning/PlanningApplicationsandPermission/DecisionsonPlanningApplicationswithEIAR/Decisions%20on%20planning%20applications%20accompanied%20by%20an%20Environmental%20Impact%20Assessment%20Report%20%28EIAR%29.pdf ; ClientEarth/FIE appeal summaries (B) | Planning ref 24/60787, grant dated 2025-08-20 for six two-storey data-centre buildings. Track ACP appeal/JR status. |
| Red Admiral DC / Lumcloon Rochfortbridge | Leinster (Westmeath) | PLN/appealed | RTE on Westmeath grant (B): https://www.rte.ie/news/business/2026/0608/1577376-westmeath-data-centre-approved/ ; Lumcloon project page (A for sponsor/project claim): https://lumcloonenergy.com/red-admiral/ | Six-unit datacenter plus decentralised energy resource/solar. Verify Westmeath ref, ACP appeal validity, and conditions. |
| Lumcloon / SK Ecoplant fuel-cell concept | Leinster (Offaly/Westmeath sponsor base) | PRO/related | Lumcloon official Red Admiral page (A for sponsor claim); DCD/SK coverage (B) | The concrete planning target found in this review is Westmeath/Rochfortbridge, not a confirmed standalone Offaly facility. |
| Art Data Centres / Ennis campus | Munster (Clare) | PLN; court challenge dismissed | William Fry summary of High Court decision (B): https://www.williamfry.com/knowledge/data-centres-climate-obligations-and-mathematical-argument-limitations/ ; The Journal on March 2026 High Court clearance (B): https://www.thejournal.ie/high-court-clears-way-for-e1-6bn-data-centre-project-in-co-clare-6985143-Mar2026/ | Clare permission granted 2022, ABP/ACP approved 2024, High Court challenge dismissed 2026. Verify current enabling works and any EPA licence. |
| CIX Cork Internet Exchange, Hollyhill | Munster (Cork) | OPER | CIX official site (A): https://cix.ie/ ; INEX/Cork press as B corroboration | Regional colo/IXP anchor, not hyperscale. |
| Mayo Data Hub / Killala Business Park | Connacht (Mayo) | PLN/appealed | Western People on appeal (B): https://www.westernpeople.ie/news/appeal-lodged-over-mayo-data-centre_arid-59116.html ; Irish Times on appeal and 50MW claim (B): https://www.irishtimes.com/business/2025/05/23/approval-for-mayo-data-centre-plan-is-appealed/ | Applicant reported as Mayo Data Hub Ltd / AVAIO Digital. Verify Mayo ref and current ACP decision before moving to UC. |
| Apple Athenry | Connacht (Galway) | HIST | RTE cancellation (B): https://www.rte.ie/news/ireland/2018/0510/961460-apple-athenry/ ; RTE 2022 extension quash (B): https://www.rte.ie/news/business/2022/0607/1303435-planning-extension-for-apple-galway-data-centre-quashed/ | Historical planning marker only; do not count as active. |
| Vertiv Letterkenny expansion | Ulster (Donegal) | OPER supply-chain, not DC | IDA release (A): https://www.idaireland.com/latest-news/press-release/vertiv-plans-expansion-of-ireland-and-north-west-facility-footprint | Ecosystem lead only. No confirmed Donegal datacenter facility from this review. |
| Cavan / Monaghan / Donegal facility sweep | Ulster (IE) | No confirmed major DC found | Council planning registers (A surfaces) | Record negative searches and date them; do not import Northern Ireland facilities. |

---

## 5. Province Query Templates

### Leinster

```text
"Amazon Data Services Ireland" "Drogheda" planning
"Premier Periclase" data centre Drogheda
site:louthcoco.ie "data centre" "Drogheda"
site:fingal.ie "data centre" Amazon OR Pure DC OR Ballycoolin OR Mulhuddart
site:sdcc.ie "data centre" "Grange Castle" OR Google OR Microsoft OR CyrusOne OR Echelon
site:meath.ie "data centre" Clonee OR Meta OR Facebook
site:kildarecoco.ie "24/60787" OR Herbata OR "data centre"
site:westmeathcoco.ie "Red Admiral" OR Rochfortbridge OR "data centre"
site:wicklow.ie Echelon OR Arklow "data centre"
site:offalycoco.ie Lumcloon OR "data centre"
```

### Munster

```text
site:clarecoco.ie "Art Data Centres" OR Ennis "data centre"
"Doyle" "An Coimisiun Pleanala" Ennis data centre
site:corkcity.ie "data centre" OR colocation
site:corkcoco.ie "data centre" OR CIX OR Hollyhill
site:limerick.ie "data centre"
site:tipperarycoco.ie "data centre"
site:waterfordcouncil.ie "data centre"
site:kerrycoco.ie "data centre"
```

### Connacht

```text
site:mayo.ie Killala "data centre" OR "Mayo Data Hub" OR AVAIO
"Killala Business Park" "data centre" appeal
site:galwaycoco.ie "data centre" Athenry OR Farice
site:galwaycity.ie "data centre" OR colocation
site:sligococo.ie "data centre"
site:roscommoncoco.ie "data centre"
site:leitrimcoco.ie "data centre"
```

### Ulster (IE)

```text
site:donegalcoco.ie "data centre" OR datacentre OR "server farm"
site:cavancoco.ie "data centre" OR datacentre OR "server farm"
site:monaghan.ie "data centre" OR datacentre OR "server farm"
"Vertiv" Letterkenny IDA datacenter supply chain
```

---

## 6. Validation Rules

1. Count a facility only when supported by at least one A source, or one B source that names a specific planning decision/ref and is queued for A-source follow-up.
2. Treat construction, operational status, and capacity as separate facts with separate grades.
3. Do not equate MIC/MVA, contracted grid capacity, backup-generation capacity, IT load, or marketed campus power.
4. Do not double-count campuses by operator code changes: Interxion/Digital Realty DUB codes, Equinix DB codes, Meta/Facebook Clonee, and Amazon/AWS/SPV names need alias normalization.
5. Do not count cloud-region availability as a facility address.
6. Do not count supply-chain factories, cable landings, IXPs, or energy projects as datacenters unless there is a separate datacenter planning/operator record.
7. For negative provinces/counties, preserve a dated search note rather than silently omitting them.

---

## 7. Re-Check Cadence

- **Weekly**: DCD, RTE Business, Irish Times, Business Post, Silicon Republic, The Journal for Ireland datacenter stories; use articles only as leads until official records are captured.
- **Monthly**: planning registers for Dublin x4, Meath, Louth, Kildare, Wicklow, Westmeath, Clare, Mayo, Cork, and Offaly.
- **Quarterly**: all 31 local authorities, An Coimisiun Pleanala, EPA/LEAP, CRU/EirGrid/ESB Networks, IDA newsroom, eTenders.
- **Annually**: refresh cloud-region official pages, CSO electricity statistics, Oireachtas research, province coverage, and all stale B/C claims.

High-priority watch items after this review: ACP outcome for Mayo/Killala; ACP/JR status for Herbata Naas; appeal status for Red Admiral Rochfortbridge; EPA licensing for Ennis/Art, Naas/Herbata, Red Admiral, and major self-generation projects; any fresh Google Grange Castle application; current AWS Drogheda construction status; confirmed Vantage Dublin location and planning refs.
