# NR Explorer Official - Nauru Datacenter Enumeration via Government ICT, Regulation, Cable Landing, and Power

Date: 2026-08-12. Scope: Nauru (NR), 14 repo divisions: Aiwo, Anabar, Anetan, Anibare, Baitsi, Boe, Buada, Denigomodu, Ewa, Ijuw, Meneng, Nibok, Uaboe, Yaren. Angle: **official / regulatory / government pipeline**.

Reliability grades used here:

- **A**: official/primary sources: `nauru.gov.nr`, `stats.gov.nr`, RONLAW / official act text, `naurufibrecable.com`, `eastmicronesiacable.com`, AIFFP/DFAT/ADB/World Bank project documents, NUC official pages and annual reports, ITU and official cloud-region lists.
- **B**: strong secondary or project-side sources: nem Australasia as EMC Project Coordination Unit, NEC, SubTel Forum, submarine cable references, DCD, RNZ/ABC/PACNEWS/Loop/Pacific Islands Times when citing named officials or project documents.
- **C**: weak/aggregate sources: datacenter directories, generic vendor service pages, SEO market reports, social media, uncited Chinese/English articles, BGP/outage monitors unless used only as a routing clue.

## 0. Ground Truth for Nauru

- Nauru is a single-island microstate of about 21 km2. The 14 repo divisions are complete and match the government/parliamentary district set: **Aiwo; Anabar; Anetan; Anibare; Baitsi/Baiti; Boe; Buada; Denigomodu; Ewa; Ijuw; Meneng; Nibok; Uaboe; Yaren**. Official parliament pages group those districts into eight constituencies: Aiwo; Anabar = Anabar, Anibare, Ijuw; Anetan = Anetan, Ewa; Boe; Buada; Meneng; Ubenide = Baiti, Denigomodu, Nibok, Uaboe; Yaren. Use this as the division-completeness check: https://www.nauru.gov.nr/parliament-of-nauru/about-parliament/who-comprises-parliament.aspx and https://www.nauru.gov.nr/parliament-of-nauru/constitution-of-nauru.aspx. `stats.gov.nr` hosts the 2021 census release and microdata tables by district: https://stats.gov.nr/2023/09/06/nauru-2021-population-and-housing-census-report-available/.
- District-level datacenter enumeration is normally not meaningful on Nauru. Treat the country as one market and tag facilities to a district only when a primary source gives a district/address or when the location can be defensibly inferred from an official address. Do not invent a district for the cable landing station: current public project pages confirm a Nauru landing site and CLS, but not a precise district/parcel.
- There is no verified public evidence of a commercial colocation market, hyperscale datacenter, cloud region, AI/HPC campus, or independent carrier hotel in Nauru. The realistic official inventory is: (1) the East Micronesia Cable (EMC) Nauru cable landing station, (2) government ICT Center/server rooms in Yaren, (3) Cenpac Net / Digicel operator rooms, and (4) any future donor-funded national data hosting, digital government cloud, or cybersecurity infrastructure project.
- The government ICT baseline is the Department of ICT page: https://www.nauru.gov.nr/government/departments/department-of-telecommunications.aspx. It says the Department of ICT is located at the **ICT Center, Yaren District**, is responsible for all government communications and information systems, operates government network/internet/email/web services, and has 26 staff across administration, line technicians, technicians/trainees, and administrators. This is an A-grade source for a government server-room lead, but it is not a public datacenter count by itself.
- The Nauru National Digital Transformation Strategy PDF is live at https://www.nauru.gov.nr/media/204028/nndts_final_version_2025.pdf, linked from https://www.nauru.gov.nr/government/departments/department-of-telecommunications/digital-transformation-strategy.aspx. It supports broad digital infrastructure, cybersecurity, privacy, digital government, and a **digital government cloud strategy and plan** target, but it does not by itself announce a named national datacenter facility. Treat it as **planned-policy evidence**, not a facility.
- The current communications law baseline is **not** the Telecommunications and Regulatory Affairs Act 2017. The **Communications and Broadcasting Act 2018** repealed the 2017 Act and established the Nauru Communications Authority; see RONLAW (https://ronlaw.gov.nr/ and https://ronlaw.gov.nr/nauru_lpms/) and WIPO mirror text https://www.wipo.int/wipolex/en/text/580197. Older 2017 project documents remain useful historically but should not be cited as the current regulator framework without this correction.

## 1. Official Source Register

### 1.1 Government ICT and Digital Government (Grade A)

- Government portal: https://www.nauru.gov.nr/
- Department of ICT: https://www.nauru.gov.nr/government/departments/department-of-telecommunications.aspx
  - Use for ICT Center/Yaren location, government communications/information systems scope, management contacts, government email/web/network responsibilities, and links to ICT policies.
  - Facility interpretation: **government server room / ICT operations lead**, not a commercial datacenter unless a later source names a datacenter, racks, power, or hosting service.
- Nauru EMC Fibre Project page under ICT: https://www.nauru.gov.nr/government/departments/department-of-telecommunications/nauru-emc-fibre-project.aspx
  - Use for historical RFI package and early scope documents.
- Digital Transformation Strategy page and PDF:
  - https://www.nauru.gov.nr/government/departments/department-of-telecommunications/digital-transformation-strategy.aspx
  - https://www.nauru.gov.nr/media/204028/nndts_final_version_2025.pdf
  - Use for planned digital government cloud, cybersecurity framework, data privacy, digital infrastructure, and e-government priorities. Do not convert strategy goals into facility records without a project/procurement source.
- Government Directory 2025: linked from the Department of ICT page and currently discoverable as https://www.nauru.gov.nr/media/202632/govt_directory_2025.pdf. Use for minister/secretary/department contacts.
- Government Information Office media releases, gazette, and bulletin:
  - https://www.nauru.gov.nr/government-information-office/media-release.aspx
  - https://www.nauru.gov.nr/government-information-office/government-gazette.aspx
  - https://www.nauru.gov.nr/government-information-office/nauru-bulletin.aspx
  - Use for ICT procurements, civil works notices, appointments, government project ceremonies, and donor announcements.

### 1.2 Law and Regulation (Grade A)

- RONLAW entry point: https://ronlaw.gov.nr/ and https://ronlaw.gov.nr/nauru_lpms/
- Communications and Broadcasting Act 2018 mirror: https://www.wipo.int/wipolex/en/text/580197
  - The Act states that it repealed the Telecommunications and Regulatory Affairs Act 2017 and established the Nauru Communications Authority. Use current-law terms in extraction: licence/authority under the 2018 Act; older Telecom Act licences may survive under transitional provisions, but verify status.
- Nauru Fibre Cable Corporation / Cable Corporation legal context:
  - NFCC governance page: https://www.naurufibrecable.com/governance
  - ADB development coordination document records that the Nauru Cable Corporation Act 2017 established the cable corporation to manage the submarine cable and wholesale bandwidth: https://ewsdata.rightsindevelopment.org/files/documents/01/ADB-50348-001_cMYl8po.pdf

### 1.3 East Micronesia Cable and Nauru CLS (Grade A)

- EMC official site: https://www.eastmicronesiacable.com/
- EMC project page: https://www.eastmicronesiacable.com/the-project
  - Confirms a four-year project begun in 2022 with expected delivery in late 2025; landing stations at each landing point; 2,250 km Tarawa-Pohnpei route with branches to Nauru and Kosrae; connection to HANTRU-1; single fibre pair spectrum sharing; 100 Gbps initial provisioned capacity per country; 10 Tbps system capability; land infrastructure includes CLS, beach manholes, ducts, and near-station backhaul.
- NFCC official site: https://www.naurufibrecable.com/
- NFCC Nauru landing article: https://www.naurufibrecable.com/news/east-micronesia-cable-landing-in-second-pacific-location-of-nauru-celebrated-with-ceremonial-buoy-event
  - Confirms Nauru cable landing on 9 August 2025, Nauru/development partner ceremony, cable landing station tour, AUD135m funding, and expected ready-for-service in November 2025.
- AIFFP investment page: https://www.aiffp.gov.au/investments/investment-list/improving-digital-connectivity-in-the-federated-states-of-micronesia-kiribati-and-naoero-via-submarine-cable
  - Confirms AUD135m project, up to AUD65m AIFFP grant, 100% grant-funded project, partners, Naoero Fibre Cable, route to HANTRU-1 in Pohnpei, and impact rationale.
- AIFFP civil works article: https://www.aiffp.gov.au/news/nauru-breaks-ground-first-international-submarine-cable-connection-0
  - Confirms 1 November 2024 start of Nauru civil works including beach manhole, duct work, foundational structures for the cable landing station, and target delivery by December 2025.
- AIFFP landing article: https://www.aiffp.gov.au/news/east-micronesia-cable-lands-second-pacific-location-nauru
  - Confirms the 9 August 2025 landing, Nauru Primary School students touring the CLS, and expected RFS in November 2025.
- DFAT project milestone pages:
  - https://www.dfat.gov.au/news/media-release/memorandum-understanding-east-micronesia-cable-project
  - https://www.dfat.gov.au/news/media-release/advancing-delivery-east-micronesia-cable-project
  - https://www.dfat.gov.au/news/media-release/work-start-east-micronesia-cable-following-contract-signing
- ADB and World Bank project documents:
  - ADB development coordination: https://ewsdata.rightsindevelopment.org/files/documents/01/ADB-50348-001_cMYl8po.pdf
  - ADB economic and financial analysis: https://ewsdata.rightsindevelopment.org/files/documents/01/ADB-50348-001_AoyiB7L.pdf
  - ADB linked document URL verified live: https://www.adb.org/sites/default/files/linked-documents/50348-001-dc.pdf
  - World Bank project paper: https://ewsdata.rightsindevelopment.org/files/documents/63/WB-P161363.pdf
  - Use these for historical design, institutional, cost, and onshore-infrastructure facts. They do not supply a public Nauru parcel/district in the accessible text; do not use them to assert Anibare/Yaren/Aiwo without another source.

### 1.4 Power and Utilities (Grade A/B)

- Nauru / Naoero Utilities Corporation: https://www.nuc.com.nr/
  - Confirms NUC as the relevant power/water utility, main office at **Aiwo District Power House**, a 6MW solar farm project, and current maximum island power demand around 5-6 MW/month in the last 12 months.
- NUC annual report PDF verified live via NUC-hosted Wix file: https://00486d66-ece8-4274-bbb5-161dafd6fe8e.filesusr.com/ugd/b1284f_11173298df70404cbcdb9ddae662e427.pdf?index=true
  - Reports 11.6 MW firm electricity production capacity and maximum demand of 5.3 MW for the report period. Use as a power sanity check: any MW-scale datacenter would be nationally material.
- NUC tender portal: https://www.tenderlink.com/nuc/ (Grade A for NUC procurement channel; public tender detail may require registration).
- Pacific/energy mirrors may be useful for older documents but should be dated clearly: policy.asiapacificenergy.org, PRDR/SPC, PPA, PCREEE.

### 1.5 International / Cloud Negative Sources (Grade A)

Use official lists only for cloud-region negatives:

- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

As of 2026-08-12, these lists do not show a Nauru public cloud region. Do not treat reseller/cloud-service marketing or Starlink/O3b availability as a local cloud region or datacenter.

## 2. Official Query Templates

Government and law:

```text
site:nauru.gov.nr ("data centre" OR "data center" OR datacenter OR "server room" OR "server farm")
site:nauru.gov.nr (ICT OR telecommunications OR "digital transformation") (cloud OR hosting OR cybersecurity OR infrastructure)
site:nauru.gov.nr "ICT Center" OR "ICT Centre" OR "Yaren District"
site:nauru.gov.nr (tender OR procurement OR contract OR gazette) (ICT OR server OR cloud OR cybersecurity OR telecom)
site:ronlaw.gov.nr ("Communications and Broadcasting Act" OR "Nauru Communications Authority" OR "Nauru Fibre Cable Corporation")
site:ronlaw.gov.nr ("data protection" OR privacy OR cybersecurity OR "electronic transactions") Nauru
```

Cable and CLS:

```text
"Nauru" "cable landing station"
"Nauru" "beach manhole"
"Nauru" "near station backhaul"
"East Micronesia Cable" Nauru landing station
site:eastmicronesiacable.com Nauru
site:naurufibrecable.com (Nauru OR Naoero) (landing OR "ready for service" OR commissioning OR wholesale OR backhaul)
site:aiffp.gov.au Nauru "East Micronesia Cable"
site:dfat.gov.au "East Micronesia Cable" Nauru
filetype:pdf "East Micronesia Cable" Nauru (BMH OR "beach manhole" OR "landing station" OR ducting)
```

Power and permits:

```text
site:nuc.com.nr ("Power Demand" OR MW OR diesel OR solar OR battery OR BESS OR "large customer")
site:tenderlink.com/nuc Nauru (substation OR generator OR transformer OR solar OR battery)
"Nauru Utilities Corporation" ("data centre" OR "data center" OR server OR telecom OR "cable landing")
"Aiwo District Power House" Nauru (MW OR generator OR load)
```

Development-finance / change detection:

```text
site:adb.org Nauru (ICT OR cable OR broadband OR "digital government" OR cybersecurity)
site:worldbank.org Nauru (digital OR ICT OR connectivity OR cloud OR cybersecurity)
site:aiffp.gov.au Naoero OR Nauru (digital OR cable OR broadband)
site:dfat.gov.au Nauru (ICT OR digital OR cable OR cybersecurity)
"Nauru" ("data centre" OR "data center" OR datacenter) (China OR 中国 OR 数据中心)
```

Whole-country negative sweep:

```text
"Nauru" ("data centre" OR "data center" OR datacenter) -tourism
"Nauru" ("server room" OR "server farm" OR hosting OR colocation OR "rack space")
"Nauru" ("digital government cloud" OR "government cloud" OR "sovereign cloud")
"Nauru" (AI OR GPU OR supercomputer OR "high performance computing")
```

## 3. Per-Division Official Enumeration Strategy

Use the table for location tagging and coverage completeness. Every run should touch all 14 names at least via the whole-country and low-priority district sweeps; only high/medium districts need deeper source review unless a hit appears.

| Repo division | Priority | Official search strategy | Count rule |
|---|---:|---|---|
| Yaren | High | Government offices, Parliament, airport, and **ICT Center**. Search Department of ICT, GIO/Gazette, Government Directory, ICT policy PDFs, and procurement notices for servers, hosting, cloud, cybersecurity, and e-government infrastructure. | Count only if source names a server room/datacenter/project, or tag ICT Center as government ICT/server-room lead. |
| Aiwo | High | NUC main office/power house, harbour/industrial precinct, Cenpac Net Civic Centre address. Search NUC, GIO/Gazette, harbour works, telecom operator addresses, and large-load notices. | Count operator/power/industrial facilities only with named facility evidence. Do not infer datacenter from power station alone. |
| Anibare | Medium | Possible east-coast landing geography in earlier assumptions, but public A-grade sources reviewed here only say Nauru landing site/CLS. Search EMC/AIFFP/NFCC/ESIA terms plus satellite review before assigning. | Do not tag CLS to Anibare unless a source or imagery workflow supports it. |
| Denigomodu | Low | Former phosphate/Location area; possible industrial reuse and Nauru Rehabilitation Corporation facilities. Search GIO, energy reports, and land/rehabilitation notices. | Only explicit ICT, server, telecom, or large power-load evidence. |
| Meneng | Low | Regional Processing Centre, Menen Hotel area, government/contractor ICT. Search only for explicit server/telecom/data-hosting projects. | Do not count refugee-processing-centre or hotel ICT as datacenter without facility evidence. |
| Boe | Very low | Government/school/residential district. District keyword sweep plus GIO/Gazette. | Promote only on named facility/project hit. |
| Buada | Very low | Inland residential/lagoon area. District keyword sweep; check solar/water/utility only if project names district. | Promote only on named facility/project hit. |
| Ewa | Very low | Residential/northwest. District keyword sweep. | Promote only on named facility/project hit. |
| Nibok | Very low | Ubenide constituent district; district keyword sweep. | Promote only on named facility/project hit. |
| Uaboe | Very low | Ubenide constituent district; district keyword sweep. | Promote only on named facility/project hit. |
| Baitsi | Very low | Ubenide constituent district, spelled **Baiti** in some official pages. Search both Baitsi and Baiti. | Promote only on named facility/project hit. |
| Anabar | Very low | Northern/eastern constituency district. District keyword sweep. | Promote only on named facility/project hit. |
| Anetan | Very low | Northern constituency district. District keyword sweep. | Promote only on named facility/project hit. |
| Ijuw | Very low | Eastern constituency district. District keyword sweep. | Promote only on named facility/project hit. |

District sweep template:

```text
"{district}" Nauru ("data centre" OR "data center" OR datacenter OR "server room" OR hosting OR colocation OR telecom OR "cable landing")
site:nauru.gov.nr "{district}" (ICT OR telecom OR server OR cloud OR cable OR power)
```

## 4. Candidate Handling and Extraction Schema

Minimum validation before counting a facility:

- One Grade A source naming the facility/project and its function; or
- An operator/government official page plus one independent Grade A/B source; and
- A district/address/coordinate source if district-level tagging is claimed.

Expected candidate records:

```text
country_code: NR
division: Aiwo | Anabar | Anetan | Anibare | Baitsi | Boe | Buada | Denigomodu | Ewa | Ijuw | Meneng | Nibok | Uaboe | Yaren | Unknown NR
facility_or_project_name:
operator_or_owner: NFCC | Department of ICT | Cenpac Net Inc | Digicel Nauru | NUC | donor-project | other
consent_or_authorisation: Communications and Broadcasting Act 2018 licence/authority | NFCC/cable corporation mandate | department approval | donor agreement | none found
site_address:
coordinates:
status: operational | under construction | ready-for-service | planned | lead | verified-negative
facility_type: cable landing station | government server room | operator exchange | colocation | cloud-region | AI/HPC | other
it_load_mw:
power_connection: NUC grid | diesel | solar/BESS | unknown
connectivity: EMC | satellite/O3b/Starlink backup | local fibre | unknown
evidence_grade: A | B | C
primary_urls:
source_documents:
notes:
last_checked: 2026-08-12
```

Initial candidate expectations as of this review:

- **East Micronesia Cable Nauru CLS**: NFCC / EMC; status landed August 2025, RFS expected November 2025 in public 2025 sources; facility type cable landing station; division **Unknown NR until district/parcel verified**; A-grade URLs: EMC, NFCC, AIFFP.
- **Department of ICT / ICT Center**: government ICT/server-room lead in **Yaren**; status operational ICT function; not a commercial datacenter; A-grade URL: Department of ICT page.
- **Cenpac Net Inc / Nauru Internet Centre**: operator/server-room lead in **Aiwo** from official Cenpac address; verify hosting/server claims before counting as facility; A-grade URL: https://www.cenpac.net.nr/.
- **Digicel Nauru**: telecom operator lead; no public colocation/DC offer found; A/B sources only for operator presence.
- **Cloud regions / hyperscale / colocation**: verified negative unless future official list or operator source changes.

## 5. Common False Positives

- Treating the CLS as a commercial datacenter. Record it as telecom infrastructure unless NFCC later offers colocation/hosting at the site.
- Using outdated **Telecommunications and Regulatory Affairs Act 2017** as current law. It was repealed by the 2018 Act; cite the current act for current authorization.
- Assigning the Nauru CLS to Anibare, Yaren, or Aiwo without a source. Public AIFFP/NFCC/EMC pages confirm a Nauru landing site and CLS but do not expose a parcel/district in the reviewed text.
- Counting government Moodle, school labs, the Regional Processing Centre, hotels, or cyber-awareness programs as datacenters.
- Counting Starlink/O3b/Kacific/Intelsat access as datacenter infrastructure.
- Accepting generic data-center construction, market-size, or "Unknown Nauru Data Center" directory pages as evidence. These are Grade C unless corroborated by A-grade sources.

## 6. Recommended First-Pass Workflow

1. Read Department of ICT and Digital Transformation Strategy PDF for government hosting, cloud, cybersecurity, and procurement terms.
2. Run the EMC/CLS chain: EMC project page -> NFCC news -> AIFFP investment/civil works/landing pages -> DFAT milestones -> ADB/WB design documents.
3. Pin location only after a source or imagery workflow establishes the parcel/district; otherwise keep division as `Unknown NR`.
4. Check NUC for power demand/capacity and any large-customer or substation work.
5. Search RONLAW for current communications, data, cyber, public utilities, land, and procurement law.
6. Sweep all 14 district names using the table above, including both `Baitsi` and official spelling variant `Baiti`.
7. Record verified negatives for cloud regions, colocation, AI/HPC, and datacenter directories so future diffs identify new signals quickly.
