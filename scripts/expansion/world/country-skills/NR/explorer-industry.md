# NR Explorer Industry - Nauru Datacenter Enumeration via Cable Landing, Operators, Colocation, Cloud, and Trade Press

Date: 2026-08-12. Scope: Nauru (NR), 14 repo divisions: Aiwo, Anabar, Anetan, Anibare, Baitsi, Boe, Buada, Denigomodu, Ewa, Ijuw, Meneng, Nibok, Uaboe, Yaren. Angle: **industry / operator / infrastructure pipeline**.

Reliability grades used here:

- **A**: operator/project/government primary sources: `naurufibrecable.com`, `eastmicronesiacable.com`, `cenpac.net.nr`, Digicel official pages, AIFFP/DFAT/ADB/World Bank documents, Department of ICT, RONLAW/official act text, NUC, ITU and official cloud-region lists.
- **B**: authoritative industry/press: nem Australasia as EMC Project Coordination Unit, NEC, SubTel Forum, submarine cable references, DCD, APNIC/PeeringDB/BGP tools for network metadata, RNZ/ABC/PACNEWS/Loop/Pacific Islands Times when tied to named sources.
- **C**: datacenter directories, generic vendor lead-generation pages, SEO market reports, social media, uncited Chinese/English claims, outage/geocable aggregators except as weak routing clues.

## 0. Market Reality

- Nauru has **no verified commercial colocation/datacenter market** in public sources as of 2026-08-12. Data Center Map's public country list is a negative-check source, and search results that claim an "Unknown Nauru Data Center" or generic Nauru construction/site-selection services are Grade C until corroborated by an operator, government, or project document.
- The practical industry census is tiny: (1) **East Micronesia Cable (EMC) Nauru cable landing station**, (2) **Cenpac Net Inc / Nauru Internet Centre** operator infrastructure in Aiwo, (3) **Digicel Nauru** mobile switching/access infrastructure, and (4) **government ICT Center** in Yaren (covered more heavily in `explorer-official.md`).
- The cable landing station is a telecom facility, not automatically a datacenter. Count it as a `cable landing station`; add colocation/interconnection only if NFCC or another operator advertises rack/hosting/interconnection service at the site.
- Power is a hard market filter. NUC reports island peak demand around 5-6 MW on its official site, and an NUC annual report gives 11.6 MW firm capacity and 5.3 MW maximum demand for that period. Any multi-MW datacenter claim is nationally material and needs primary power/procurement evidence.
- District coverage is complete with 14 divisions: Aiwo, Anabar, Anetan, Anibare, Baitsi, Boe, Buada, Denigomodu, Ewa, Ijuw, Meneng, Nibok, Uaboe, Yaren. Search **Baitsi** and **Baiti** because official parliament pages use Baiti in the Ubenide constituency listing.

## 1. Cable Industry Sources

### 1.1 East Micronesia Cable / NFCC (Grade A)

- EMC official site: https://www.eastmicronesiacable.com/
- EMC project page: https://www.eastmicronesiacable.com/the-project
  - Confirms 2022-2025 project timeline, 2,250 km route, Tarawa-Pohnpei trunk, branches to Nauru and Kosrae, connection to HANTRU-1, landing stations at landing points, single-fibre-pair spectrum sharing, 100 Gbps initial provisioned capacity per country, 10 Tbps system capability, optical transmission and power-feed equipment in CLS, beach manholes/ducting, and near-station backhaul for local operators.
- NFCC official site: https://www.naurufibrecable.com/
- NFCC landing article: https://www.naurufibrecable.com/news/east-micronesia-cable-landing-in-second-pacific-location-of-nauru-celebrated-with-ceremonial-buoy-event
  - Confirms Nauru landing on 9 August 2025, attendance by Nauru/development partner representatives, cable landing station interior tour, AUD135m project, and expected November 2025 ready-for-service.
- NFCC governance: https://www.naurufibrecable.com/governance
  - Points to the founding NFCC legislation; use alongside RONLAW/ADB legal documents for mandate.
- AIFFP investment page: https://www.aiffp.gov.au/investments/investment-list/improving-digital-connectivity-in-the-federated-states-of-micronesia-kiribati-and-naoero-via-submarine-cable
- AIFFP civil works article: https://www.aiffp.gov.au/news/nauru-breaks-ground-first-international-submarine-cable-connection-0
- AIFFP Nauru landing article: https://www.aiffp.gov.au/news/east-micronesia-cable-lands-second-pacific-location-nauru
- DFAT milestones:
  - https://www.dfat.gov.au/news/media-release/memorandum-understanding-east-micronesia-cable-project
  - https://www.dfat.gov.au/news/media-release/advancing-delivery-east-micronesia-cable-project
  - https://www.dfat.gov.au/news/media-release/work-start-east-micronesia-cable-following-contract-signing
- NEC supplier press release: https://www.nec.com/en/press/202306/global_20230606_02.html (Grade B+ for supplier/contract confirmation; primary to NEC, secondary to national facility enumeration).

CLS extraction notes:

```text
facility_or_project_name: East Micronesia Cable - Nauru Cable Landing Station
operator: Nauru Fibre Cable Corporation / Naoero Fibre Cable
facility_type: cable landing station
status: landed 2025-08-09; expected RFS 2025-11 in public 2025 sources; verify current operational status on each run
capacity_or_scale: 100 Gbps initial provisioned capacity per country; 10 Tbps system capability
connectivity: EMC to Pohnpei / HANTRU-1 / Guam; near-station backhaul for local operators
power: NUC grid likely, but record only when sourced
location: Nauru landing site; district/parcel not public in reviewed sources
primary_urls: EMC, NFCC, AIFFP
```

### 1.2 Project-Side and Trade Sources (Grade B)

- nem Australasia news: https://www.nem.net.au/news
  - Nauru landing article: https://www.nem.net.au/news/2025/8/20/east-micronesia-cable-landing-in-second-pacific-location-of-nauru-celebrated-with-ceremonial-buoy-event
  - Kosrae final-landing follow-up: https://www.nem.net.au/news/2025/9/1/east-micronesia-cable-lands-in-kosrae-fsm-final-step-towards-enhanced-pacific-connectivity
  - Use as B+ because nem is the AIFFP-contracted Project Coordination Unit, but prefer NFCC/AIFFP/EMC pages for A-grade facts.
- Submarine cable references: https://www.submarinecablemap.com/, https://www.submarinenetworks.com/.
- DCD / SubTel Forum / Pacific Islands Times are useful for historical EMC financing, security, and vendor-context stories. Keep source grade B unless they reproduce primary project documents.

## 2. Operator Sources

### 2.1 Cenpac Net Inc (Grade A for operator identity/address; B/C for inferred facility scale)

- Official site: https://www.cenpac.net.nr/
  - Confirms Cenpac Net Inc / Nauru Internet Centre, ISP since 1998, official contacts, `.nr` registry role, technical contacts, and **Civic Centre, Aiwo District** address.
- ITU country profile PDF: https://www.itu.int/en/ITU-D/LDCs/Documents/2017/Country%20Profiles/Country%20Profile_Nauru.pdf
  - Confirms historical market structure: Digicel plus Cenpac; Cenpac operates an internet cafe, manages `.nr`, had a west-side government fibre backbone, and competed in business internet. Date it as 2017.
- ADB development coordination: https://ewsdata.rightsindevelopment.org/files/documents/01/ADB-50348-001_cMYl8po.pdf
  - Confirms Nauru services by government-owned Cenpac Net Incorporated and Digicel Nauru in the project-preparation period.
- APNIC/BGP clues (Grade B for network metadata, not facility): APNIC WHOIS via tools, https://bgp.tools/as/55722, https://ipgeolocation.io/browse/asn/AS55722.

Cenpac extraction posture: record as **operator exchange/server-room lead in Aiwo** only if the inventory accepts telco server rooms. Do not tag as commercial colocation unless Cenpac publishes hosting/rack/facility service evidence.

### 2.2 Digicel Nauru (Grade A/B for operator presence; no colo evidence)

- Digicel Pacific Nauru page: https://www.digicelpacific.com/mobile/nr
- Digicel cable-related news: https://www.digicelpacific.com/news/a-bigger-better-connection-for-nauru
- Nauru Government media release on Telstra/Digicel Pacific: https://www.nauru.gov.nr/government-information-office/media-release/telstra-buys-digicel-pacific-for-us%2416-billion.aspx
- ITU country profile: https://www.itu.int/en/ITU-D/LDCs/Documents/2017/Country%20Profiles/Country%20Profile_Nauru.pdf

Digicel extraction posture: assume mobile core/switching infrastructure exists for operations, but no public source reviewed here identifies a datacenter/colo site. Keep as `operator exchange lead`, division `Unknown NR` unless a local address/source is found.

### 2.3 Government ICT Center (Grade A, official-side overlap)

- Department of ICT: https://www.nauru.gov.nr/government/departments/department-of-telecommunications.aspx
- Treat as an operational government ICT/server-room lead in **Yaren**. It can explain local government hosting but should not be counted as commercial industry capacity.

## 3. Industry Query Templates

Cable / interconnection:

```text
"East Micronesia Cable" Nauru (RFS OR "ready for service" OR commissioning OR activated OR operational)
"Nauru Fibre Cable" (wholesale OR backhaul OR interconnection OR colocation OR hosting OR rack)
"Naoero Fibre Cable" (wholesale OR backhaul OR interconnection OR colocation OR hosting OR rack)
"Nauru" "cable landing station" (operator OR backhaul OR interconnection OR rack)
site:naurufibrecable.com ("ready for service" OR wholesale OR backhaul OR interconnection OR colocation)
site:eastmicronesiacable.com (Nauru OR Naoero) (operator OR backhaul OR "landing station")
```

Operators:

```text
site:cenpac.net.nr (hosting OR server OR DNS OR domain OR "data centre" OR "data center" OR colocation)
"Cenpac Net" Nauru (server OR hosting OR colocation OR exchange OR "internet centre" OR "Civic Centre" OR Aiwo)
"CenpacNet" OR "Cenpac Net Inc" "AS55722" OR APNIC OR PeeringDB
site:digicelpacific.com Nauru ("data centre" OR "data center" OR switch OR core OR LTE OR 5G OR cable)
"Digicel Nauru" (switch OR exchange OR "data centre" OR "data center" OR hosting OR core network)
```

Colocation / cloud / AI negative checks:

```text
"Nauru" (colocation OR "colo" OR "rack space" OR "carrier hotel" OR "internet exchange")
"Nauru" ("data centre" OR "data center" OR datacenter) -tourism -"processing centre"
"Nauru" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "edge location")
"Nauru" (GPU OR AI OR "artificial intelligence" OR "high performance computing" OR supercomputer) (investment OR facility OR data)
site:datacentermap.com Nauru
site:cloudinfrastructuremap.com Nauru
```

Pacific trade press:

```text
site:datacenterdynamics.com Nauru "East Micronesia Cable"
site:subtelforum.com "East Micronesia Cable" Nauru
site:submarinenetworks.com "East Micronesia Cable" Nauru
site:rnz.co.nz Nauru (cable OR internet OR Digicel OR Cenpac)
site:abc.net.au Nauru (cable OR internet OR Digicel OR Cenpac)
site:pacificislandtimes.com Nauru (cable OR internet OR datacenter OR data center)
site:loopnauru.com Nauru (ICT OR cable OR internet OR Digicel OR Cenpac)
```

Chinese-language / rumor watch:

```text
"瑙鲁" ("数据中心" OR "云" OR "算力" OR "海底光缆" OR "通信")
"Nauru" ("data centre" OR "data center" OR cloud OR ICT) (China OR Chinese OR Huawei OR HMN OR "China Harbour")
```

Grade Chinese/SEO hits C unless corroborated by NFCC, Nauru government, AIFFP/DFAT/ADB/WB, or a named operator.

## 4. Per-Division Industry Strategy

| Repo division | Priority | Industry angle | Promote when |
|---|---:|---|---|
| Aiwo | High | Cenpac Net / Nauru Internet Centre at Civic Centre; NUC Power House; harbour/industrial users. Search Cenpac, APNIC/BGP, NUC, and GIO. | Operator facility, hosting product, exchange, power upgrade, or industrial ICT project is named. |
| Yaren | High | Government ICT Center and government demand cluster; airport/government offices. Search official ICT plus vendor/contractor mentions. | Government server room/cloud project or operator serving government is named. |
| Unknown NR / CLS location | High | EMC Nauru landing site and CLS. Until district is sourced, keep as Unknown NR rather than forcing Anibare/Aiwo/Yaren. | NFCC/AIFFP/EMC/ESIA/source or imagery confirms exact district/parcel. |
| Anibare | Medium | Possible landing geography from coastline assumptions; verify only with source/imagery. | CLS/landing/BMH evidence identifies Anibare. |
| Denigomodu | Low | Former phosphate/Location industrial area; possible large loads or reused industrial buildings. | Named telecom/hosting/power customer evidence. |
| Meneng | Low | Regional Processing Centre and contractor ICT; not market infrastructure by default. | Explicit datacenter/server-room/telecom facility evidence outside ordinary site IT. |
| Boe | Very low | Residential/government adjacency; quick operator/district keyword sweep. | Named facility/project evidence. |
| Buada | Very low | Inland/residential; possible wireless/backhaul coverage only. | Named facility/project evidence. |
| Ewa | Very low | Residential/northwest; search with Anetan constituency. | Named facility/project evidence. |
| Nibok | Very low | Ubenide constituent district; quick sweep. | Named facility/project evidence. |
| Uaboe | Very low | Ubenide constituent district; quick sweep. | Named facility/project evidence. |
| Baitsi | Very low | Search Baitsi and Baiti spelling. | Named facility/project evidence. |
| Anabar | Very low | Search with Anabar/Anibare/Ijuw constituency terms. | Named facility/project evidence. |
| Anetan | Very low | Search with Ewa/Anetan constituency terms. | Named facility/project evidence. |
| Ijuw | Very low | Eastern district; quick sweep. | Named facility/project evidence. |

District sweep:

```text
"{district}" Nauru (Cenpac OR Digicel OR NFCC OR "Nauru Fibre" OR telecom OR "cable landing" OR server OR hosting OR colocation)
"{district}" Nauru ("data centre" OR "data center" OR datacenter)
```

## 5. Required Fields per Candidate

```text
country_code: NR
division: Aiwo | Anabar | Anetan | Anibare | Baitsi | Boe | Buada | Denigomodu | Ewa | Ijuw | Meneng | Nibok | Uaboe | Yaren | Unknown NR
facility_or_project_name:
operator: NFCC/Naoero Fibre Cable | Cenpac Net Inc | Digicel Nauru | Department of ICT | NUC | other
facility_type: cable landing station | operator exchange | government server room | colocation | cloud region | AI/HPC | other
status: operational | landed | ready-for-service | under construction | planned | lead | verified-negative
capacity_or_scale: 100 Gbps initial / 10 Tbps system capability / racks / MW / unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
connectivity: EMC via Pohnpei/HANTRU-1/Guam | satellite/O3b/Starlink backup | local fibre | unknown
power: NUC grid | diesel | solar/BESS | unknown
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

Minimum count standard: one Grade A facility/project source, or operator official source plus one independent Grade A/B corroborator. For district tagging, require source address/district or a documented imagery/geocoding step.

## 6. Verified Negatives and False Positives

- **Commercial colocation**: no verified Nauru colocation provider found. Generic Nauru landing pages from construction/site-selection vendors are Grade C lead generation, not facility evidence.
- **Hyperscaler cloud regions**: no Nauru region in official AWS, Azure, Google Cloud, or Oracle OCI region lists:
  - https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
  - https://learn.microsoft.com/en-us/azure/reliability/regions-list
  - https://cloud.google.com/about/locations
  - https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
- **Directory artifacts**: `Unknown Nauru Data Center`-style entries with no operator name, address, or corroborating source are Grade C and should not be counted.
- **Satellite/access providers**: Starlink, O3b, Kacific, Intelsat, outage maps, and BGP routes can explain connectivity but are not datacenter facilities.
- **Regional Processing Centre**: Do not confuse the detention/refugee-processing facility in Meneng with data processing. Count only if a source names an ICT/server facility.
- **Historical telecom claims**: Nauru Telecom, old satellite earth stations, and 2017 market documents are context only unless current operator evidence confirms the facility still exists.
- **Chinese SEO/market claims**: ignore market-size or invented facility claims unless corroborated by Nauru government, NFCC, AIFFP/DFAT/ADB/WB, NEC, Cenpac, or Digicel.

## 7. Recommended Sweep Order

1. EMC/CLS status: NFCC -> AIFFP -> EMC -> nem -> NEC -> DFAT. Confirm whether November/December 2025 RFS was achieved or delayed.
2. CLS location pin: search ADB/WB/ESIA PDFs and NFCC/GIO media for BMH/CLS site details; if still absent, keep `Unknown NR`.
3. Cenpac: official site -> APNIC/BGP -> hosting/DNS/domain pages -> local address confirmation in Aiwo.
4. Digicel: official Nauru page -> cable news -> government/Telstra/Digicel Pacific sources -> any switching/core location evidence.
5. Official overlap: Department of ICT and Digital Transformation Strategy for government cloud/server-room signals.
6. Power filter: NUC pages, annual reports, and tenders for load growth or large-customer interconnects.
7. Full district sweep across all 14 divisions and both Baitsi/Baiti spelling variants.
8. Record negatives for cloud, colo, AI/HPC, and directories each run so future changes are visible.
