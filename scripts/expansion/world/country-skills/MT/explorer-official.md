# MT Explorer Official - Malta Datacenter Enumeration via Planning, Environmental, Energy, Telecom, and Public-Sector Sources

Date: 2026-08-12. Scope: Malta (MT), 68 local-council divisions. Angle: **official/regulatory methodology** for finding operational and proposed datacentres. Reliability grades: **A** = official/primary source (Planning Authority, Government Gazette, ERA permit, MITA/operator official page, MCA/REWS/Enemalta official record, cloud provider official region page), **B** = strong secondary or trade press with named parties, **C** = directory/aggregate/marketing-only evidence.

---

## 0. Malta-specific structural facts

- Malta is a compact, single-country planning market: **Planning Authority (PA)** records and the Government Gazette weekly PA notices are the main development-permit backbone, not local-council planning portals.
- The repo divisions are **local councils**, but permits are centralized. Use the locality field in PA/Gazette/ERA records to assign facilities to divisions. Watch common spelling and boundary variants: `Mriehel`/`Mriehel-CBD` may appear under Birkirkara or Qormi; `Madliena` can be assigned to Swieqi or Naxxar in secondary listings; `Victoria` is Rabat, Gozo.
- Most confirmed Malta facilities are **telecom/government/colo rooms**, not hyperscale campuses. Public MW disclosure is rare. Generator permits, rack counts, floor area, substation references, and official facility pages are more common than IT-load figures.
- Malta has no public AWS/Azure/GCP/OCI cloud region as of this research pass. Official cloud-region pages are still useful to confirm the absence of a Malta hyperscale region and to prevent falsely promoting local colo/cloud-reseller sites into hyperscale evidence.
- Maltese searches usually work in English, but add Maltese terms for completeness: `centru tad-data`, `centru data`, `ċentru tad-data`, `server farm`, `faċilita'`, `permess`, `applikazzjoni`, `żvilupp`.

---

## 1. Grade A official/regulatory sources

### 1.1 Planning Authority and development permits

- **Planning Authority website**: https://www.pa.org.mt/
- **PA eApplications portal**: https://eapps.pa.org.mt/
- **PA map server / Planning MT app lead**: https://pamapserver.pa.org.mt/ and PlanningMT app listings. Use map layers for development applications, development notifications, and enforcement points when text search is poor.
- **Government Gazette PA listings**: https://www.gov.mt/en/Government/DOI/Government%20Gazette/pa/Pages/Planning-Authority.aspx. The Gazette page links weekly lists of applications received, decisions, and enforcement notices.
- **BusinessFirst development permits**: https://www.businessfirst.com.mt/licenses/development-permits/. Confirms that structural works or change-of-use generally require Planning Authority permitting and links directly to PA/eApplications.
- **Malta Spatial Data Infrastructure (MSDI)**: https://msdi.data.gov.mt/. Planning Authority-provided geospatial portal; useful for site polygons/layers but not a complete datacentre index.

PA/Gazette keyword set:
```
"data centre"
"data center"
"datacentre"
"server farm"
"server room"
"ICT facility"
"telecommunications equipment"
"hosting facility"
"co-location" OR "colocation"
"backup generators"
"standby generators"
"substation"
"change of use" "data centre"
"Bulebel" "data centre"
"SmartCity" "data centre"
"Handaq" "data centre"
"Madliena" "data centre"
"Marsa" "underground" "data centre"
```

Maltese/local terms:
```
"centru tad-data"
"ċentru tad-data"
"centru data"
"faċilita" "data"
"permess" "data centre"
"applikazzjoni" "data centre"
"ġeneraturi" "data centre"
```

Planning extraction fields:
- application number, development type, applicant/SPV, owner, architect/perit, locality, site address, parcel/industrial estate;
- description of development, change-of-use wording, number of floors/rooms/data halls, gross floor area, rack count if disclosed;
- electrical connection/substation, generator count, fuel storage, cooling plant, acoustic/air-quality documents;
- status: application received, validated, approved, refused, reconsideration, appeal, development notification, enforcement;
- decision date and conditions, especially operating hours/noise/emissions/fire-safety conditions.

### 1.2 Environment and Resources Authority (ERA)

- **ERA home / environmental permitting**: https://era.org.mt/
- **ERA Medium Combustion Plants category**: https://era.org.mt/era-topic-categories/medium-combustion-plants/. ERA states that new MCPs require a permit to operate immediately; this is high-yield for datacentre backup generators.
- **ERA Melita Data Centre MCP record**: https://era.org.mt/era_mcp/melita-data-centre/. Grade A example: locality Swieqi, permit EP1255/22, two diesel engines at Melita Data Centre, Triq il-Madliena, with coordinates and thermal-input bands.
- **Servizz.gov environmental permit for industry**: https://www.servizz.gov.mt/en/Pages/Environment_-Energy_-Agriculture-and-Fisheries/Environment/Industrial-Permits/WEB1873/default.aspx. Use for procedure/timelines and the responsible authority.

ERA query templates:
```
site:era.org.mt/era_mcp "data centre"
site:era.org.mt/era_mcp "data center"
site:era.org.mt/era_mcp "BMIT" OR "Melita" OR "GO" OR "Epic" OR "MITA"
site:era.org.mt "medium combustion" "data centre"
site:era.org.mt "generator" "data centre" "Malta"
"EP" "data centre" "Malta" "ERA"
```

How to use ERA records:
1. Treat facility name, locality, coordinates, permit number, fuel type, operating date, and rated thermal-input bands as Grade A.
2. Do not convert thermal-input bands directly into IT load. Use them only as generator/emissions evidence.
3. Cross-check the ERA locality against PA and operator pages where boundary names differ.

### 1.3 Energy and grid sources

- **Enemalta**: https://enemalta.com.mt/. Malta's electricity network operator and a primary source for grid context, customer connection procedures, and major distribution upgrades.
- **Enemalta/Streamcast official project update**: https://enemalta.com.mt/2018/04/12/collaboration-streamcast-enemalta-moves-ahead-rapidly/. Grade A for the original Enemalta statement that a global data-center pilot at Marsa had been developed with Streamcast; later status must be checked against court/trade press.
- **Regulator for Energy and Water Services (REWS)**: https://www.rews.org.mt/. Use for electricity licensing/regulatory context.
- **REWS single contact point for renewable/CHP/storage permitting**: https://www.rews.org.mt/single-contact-point-renewable-energy-permitting-in-malta/. Relevant when a datacentre proposal includes energy storage, CHP, or dedicated renewable supply.
- **Energy and Water Agency security-of-supply page**: https://energywateragency.gov.mt/security-of-supply/. Confirms Malta-Sicily interconnector and national supply context.

Energy query templates:
```
"{operator}" "{locality}" "substation"
"{operator}" "{locality}" "MVA"
"{operator}" "{locality}" "MW" "data centre"
"data centre" "Enemalta" "Marsa"
"data centre" "Bulebel" "substation"
"data centre" "SmartCity" "power"
site:enemalta.com.mt "data center" OR "data centre"
site:rews.org.mt "data centre" OR "data center"
```

### 1.4 Communications regulator and network evidence

- **Malta Communications Authority (MCA)**: https://www.mca.org.mt/
- **MCA register of authorised undertakings**: https://www.mca.org.mt/articles/register-authorised-undertakings-providing-electronic-communications-networks-andor. Use to verify licensed telecom operators that may own facilities or provide fibre/cloud/colo services.
- **MCA spectrum licensing**: https://www.mca.org.mt/regulatory/authorizations_licensing/spectrum-licensing. Confirms licensed GO, Melita, Epic spectrum rights; not a datacentre list.
- **MCA data/report sheets and market reports**: use for fixed/mobile broadband market context and for identifying major infrastructure owners. The key telecom operators for Malta datacentre enumeration are GO, Melita, Epic, Vanilla Telecoms, and smaller authorised ECS/ISP providers.
- **Malta Internet Exchange (MIX)**: https://www.mix.net.mt/; background from NIC Malta https://www.nic.org.mt/about/. MIX is useful interconnection evidence and a lead for University of Malta/Msida infrastructure, but it is not itself a public datacentre inventory.

MCA/MIX query templates:
```
site:mca.org.mt "Register of Authorised Undertakings" "Malta"
site:mca.org.mt "GO plc" "Melita" "Epic" "fixed broadband"
site:mca.org.mt "data centre" OR "cloud"
site:mix.net.mt "Malta Internet Exchange"
site:nic.org.mt "Malta Internet Exchange"
"MIX" "University of Malta" "data centre"
```

### 1.5 MITA and government datacentres

- **MITA home/contact**: https://mita.gov.mt/ lists the MITA Data Centre at Old Railway Track, Santa Venera SVR9019 and the Gozo Innovation Hub in Xewkija.
- **MITA facilities at Data Centre**: https://mita.gov.mt/portfolio/facilities-at-data-centre/. Grade A for MITA's government hosting service and datacentre function.
- Search MITA procurement documents for site lists and WAN/fibre links. Example: MITA procurement WAN-link appendices have referenced `Gozo Data Centre, St. Francis Square, Victoria, Gozo` (assign to Rabat Gozo/Victoria when verified).

MITA queries:
```
site:mita.gov.mt "Data Centre" "Santa Venera"
site:mita.gov.mt "Gozo Data Centre"
site:procurement.mita.gov.mt "Gozo Data Centre"
site:procurement.mita.gov.mt "data centre" "WAN"
site:mita.gov.mt "Old Railway Track" "Santa Venera"
```

### 1.6 Official cloud region pages

Use these only to confirm public cloud-region presence/absence:

| Provider | Official page | Malta signal |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Malta region found; nearest relevant official Europe regions are outside Malta. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Malta Azure public region found. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Malta Google Cloud region found. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Malta OCI public region found. |

Do not count a local reseller's `cloud`, `VPS`, or `IaaS` service as a hyperscale region unless the hyperscaler has an official Malta region/local-zone page.

---

## 2. Locality enumeration workflow

For each local-council division:

1. Search PA/eApplications and Gazette notices for English and Maltese datacentre terms plus the locality.
2. Search ERA MCP records for the locality and operator names; map coordinates to the council boundary where needed.
3. Search MCA authorised undertakings for telecom operators tied to the locality, then pivot to operator facility pages.
4. Search Enemalta/REWS for power, substation, energy storage, or dedicated connection leads.
5. Search exact facility/operator names in the Malta Business Registry (MBR) BAROS/company search via https://www.mbr.mt/ to validate legal entities and SPVs.
6. Promote a project to Grade A only when a PA/Gazette/ERA/MITA/operator official page confirms the physical facility or permit. Use trade press as Grade B until the primary record is checked.

High-priority locality clusters:

| Locality/division | Why it is high yield | Official-first route |
|---|---|---|
| Santa Venera | MITA Data Centre, Epic/Vodafone directory leads, Continent 8 directory leads | MITA pages, ERA MCP search, PA/Gazette for Canon Road/Old Railway Track |
| Birkirkara | GO Birkirkara and CSL Birkirkara/CBD activity | GO/CSL official pages, MCA operator context, PA/Gazette by address |
| Qormi / Handaq / Mriehel | BMIT Handaq, Melita Mriehel secondary facility leads | BMIT official/investor docs, PA/Gazette, ERA generators |
| Kalkara / SmartCity / Bighi | BMIT SmartCity, Heritage Malta data centre, SmartCity planning history | PA/Gazette SmartCity/Ricasoli/Bighi, operator official pages |
| Swieqi / Madliena | Melita Primary Data Centre with ERA MCP permit | ERA EP1255/22, Melita official page, PA/Gazette by Triq il-Madliena |
| Marsa | GO Marsa directory lead; Enemalta/Streamcast underground data-centre project later disputed | Enemalta official archive, PA/Gazette, MaltaToday/DCD for status |
| Żejtun / Bulebel | BMIT Żejtun purpose-built facility | BMIT official announcement, PA/Gazette Bulebel/Triq Hal Tarxien, MBR |
| Gzira | MIDI/SIS DC1 directory lead | PA/Gazette North Shore/Gzira, MBR for SIS/MIDI, directories only until primary confirmed |
| Msida / University of Malta | MIX and University/Msida data-centre directory leads | MIX official, University pages, PA/Gazette campus records |
| Rabat Gozo / Victoria | Gozo Data Centre procurement lead | MITA procurement, government annual reports, PA/Gazette Victoria |
| Xewkija | MITA Gozo Innovation Hub but not necessarily a datacentre | MITA official page; do not count as DC without facility evidence |

Low-yield divisions should still get the generic sweep plus nearest industrial estate terms, but require stronger evidence before recording a facility.

---

## 3. Confidence and pitfalls

- **Grade A**: PA application/decision, Government Gazette PA notice, ERA MCP permit, MITA official datacentre page, operator official page with physical locality, MCA/REWS/Enemalta official record for telecom/energy context.
- **Grade B**: Data Center Dynamics, MaltaToday, Times of Malta, TVM, The Malta Independent, official company announcements reposted by newspapers, stock-exchange announcements.
- **Grade C**: DataCenterMap, Datacenters.com, Cloudscene, Data Center Platform, Colomap, Upstack, generic hosting/VPS pages without facility ownership/address.

Common pitfalls:
- `Mriehel`, `Central Business District`, and `Handaq` can be assigned inconsistently between Birkirkara and Qormi.
- `Madliena` listings can be placed under Madliena/Naxxar, while ERA gives Melita Data Centre locality as Swieqi.
- `Rabat Gozo` equals Victoria in many official/procurement sources; avoid mixing it with Rabat, Malta.
- Telecom head-office address is not necessarily a datacentre address. Epic/Luqa and BMIT/Pembroke are examples where office/headquarter evidence must not be treated as a facility.
- The Enemalta/Streamcast Marsa project has official launch evidence but later trade/court reporting says it did not materialise as planned; record status conservatively.
