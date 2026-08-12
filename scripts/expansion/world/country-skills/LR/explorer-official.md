# LR Explorer Official - Liberia Datacenter Enumeration

Date reviewed: 2026-08-12. Country: **Liberia (LR)**. Division model: **15 counties**: Bomi, Bong, Gbarpolu, Grand Bassa, Grand Cape Mount, Grand Gedeh, Grand Kru, Lofa, Margibi, Maryland, Montserrado, Nimba, River Cess / Rivercess, River Gee, Sinoe.

Scope: official, regulator, utility, procurement, government-policy, and operator-primary methodology for finding commercial colocation, telco, government, financial-sector, cable-landing, IXP-adjacent, and institutional datacenter/server-room facilities in Liberia.

## Reliability Grades

- **A** - Primary source for the specific claim: Liberia Telecommunications Authority (LTA) licence/order/page; Ministry of Posts and Telecommunications (MoPT) or official digital-strategy/policy document; Environmental Protection Agency (EPA) EIA/ESIA/permit record; Liberia Electricity Corporation (LEC) utility evidence; Public Procurement and Concessions Commission (PPCC) tender; Cable Consortium of Liberia (CCL) operator page; official cloud-provider location page; Uptime Institute award record; official operator, bank, agency, or university facility page.
- **B** - Strong secondary source: World Bank/ECOWAS/USAID project document, trade press, TeleGeography/CommsUpdate/Capacity/DCD, reputable Liberian press, PeeringDB/PCH for IXP location, or a government news item with named site/stage.
- **C** - Weak lead only: datacenter directory/aggregator, social post, market-report teaser, procurement repost without PPCC link, MoU without site/status, or county ICT/server-room mention that does not prove a datacenter.
- **U** - Unusable for enumeration until corroborated: no location, no Liberia context, generic cloud marketing, or Monrovia USA false positive.

## Liberia-Specific Baseline

- Liberia has **no public national datacenter registry**. Enumeration requires joining telecom licensing, government digital-strategy documents, environmental permits, procurement, power, cable/IXP, operator pages, and local press.
- Known datacenter-like activity is concentrated in **Montserrado County / Monrovia**. As of this review, no verified Liberia hyperscale cloud region, Uptime Tier III/IV commercial campus, or large public colocation market is visible in official sources.
- The practical official seed set is: CCL's ACE cable landing and colocation/hosting node in Monrovia; LIXP/LIXPA interconnection at/near CCL; the National Data Center (NDC) established at LTC Mobile and slated for upgrade; planned national disaster-recovery work; NIR on-premise storage and planned co-location at the NDC; Central Bank of Liberia DR facility used mainly by financial institutions; telco network facilities; and bank/institutional server rooms.
- Search both `data centre` and `data center`, plus `datacentre`, `server room`, `server farm`, `colocation`, `co-location`, `hosting`, `carrier neutral`, `landing station`, `meet-me`, `IXP`, `LIXP`, `LIXPA`, `cloud`, `sovereign cloud`, `government cloud`, `disaster recovery`, `NDC`, `NIR`, `LTC Mobile`, `generator`, `captive power`, `substation`, `MVA`, `MW`, `Tier III`, and `Uptime`.
- **Monrovia false-positive rule**: Monrovia, Indiana and Monrovia, California generate US datacenter hits. Count only records tied to Liberia, `.lr`, LTA, LEC, CCL, LIXP/LIXPA, LTC, Liberian counties, or Liberia country code `LR`.

## Official Sources and Use

### Liberia Telecommunications Authority (LTA)

Verified URLs:

- Home: https://lta.gov.lr/
- Licensing registry: https://lta.gov.lr/licensing-registry/
- Licensing framework: https://lta.gov.lr/licensing-framework/
- Licensing procedures: https://lta.gov.lr/licensing/
- Licensing requirements: https://lta.gov.lr/licensing-requirement/
- Regulations and guidelines: https://lta.gov.lr/regulations/
- Orders and notices: https://lta.gov.lr/order-and-notices/
- Telecom Act 2007 PDF: https://lta.gov.lr/wp-content/uploads/2023/10/LTA-Act-2007.pdf
- ICT Policy of Liberia 2019-2024 PDF: https://lta.gov.lr/wp-content/uploads/2023/12/ICT-Policy-of-Liberia-2019-2024.pdf
- LIXP page: https://lta.gov.lr/lixp/
- ccTLD page: https://lta.gov.lr/cctld/
- Cybersecurity page: https://lta.gov.lr/cyber-security/
- Liberia Digital Transformation Project page: https://lta.gov.lr/liberia-digital-transformation/
- USAID and World Bank page: https://lta.gov.lr/usaid-and-world-bank/
- Annual reports: https://lta.gov.lr/lta-annual-reports/
- Industry statistics: https://lta.gov.lr/industry-statistics-2/

Use LTA as **A evidence for licence, regulator status, LIXP existence, sector structure, or LTA statements**. A licence does not by itself prove a physical datacenter. Scan licensees and orders for mobile, fixed, ISP, international gateway, submarine cable, VAS, hosting, and data-service operators.

```text
site:lta.gov.lr "data centre"
site:lta.gov.lr "data center"
site:lta.gov.lr datacentre OR "server room" OR hosting
site:lta.gov.lr colocation OR "co-location"
site:lta.gov.lr LIXP OR LIXPA OR peering
site:lta.gov.lr "landing station" OR "submarine cable" OR ACE OR CCL
site:lta.gov.lr "National Data Center" OR "National Data Centre" OR NDC
site:lta.gov.lr "{operator}" licence OR license OR registry
site:lta.gov.lr "{county}" ICT OR broadband OR "County Service Center"
```

Extract: legal licensee name, licence category, licence dates, addresses, service scope, county/city, operator aliases, and whether the source proves only telecom service authority or a named facility.

### MoPT, OTDI, and Government Digital Strategy

Verified URLs:

- MoPT home: https://mopt.gov.lr/
- Whole-of-Government National Digital Strategy 2025-2029 PDF: https://mopt.gov.lr/wp-content/uploads/2025/09/Liberia-National-Digital-Strategy.pdf
- Draft National Data Governance Policy 2026 PDF: https://mopt.gov.lr/wp-content/uploads/2022/06/2026-Liberia-Data-Governance-Policy-REVISED-CIPESA-1.pdf
- OTDI home/search entry point: https://otdi.gov.lr/

The National Digital Strategy is the highest-value official source for government datacenter enumeration. Verified content from the PDF:

- The **National Data Center has been established at LTC Mobile** but is underutilized by Ministries, Agencies, and Commissions (MACs).
- The **NDC is managed by LTC Mobile**, underutilized, and relies on outdated systems.
- The roadmap assigns **Revamp the National Data Center** to **MoPT / LTC Mobile** for **2025-2027**.
- The roadmap assigns **Co-location hosting of NIR data at the National Data Centre** to **NIR / LTC Mobile** for **2025-2027**.
- NIR currently has **on-premise centralized data storage**, with no dedicated disaster recovery site, and discussions are underway for NDC co-location.
- There is **no National Disaster Recovery Center**. The **Central Bank of Liberia has established a disaster recovery center**, used primarily by financial institutions.
- NDS calls for needs assessment, NDC upgrade, national disaster-recovery plan, disaster-recovery center setup, cloud strategy, cloud-provider certification standards, energy assessment, carbon baseline, and renewable energy for National Data Centers.
- County Service Centers have been established in all 15 counties, but NDS says effectiveness is limited and not all have reliable internet. Treat CSCs as public-service ICT/server-room leads, not datacenters, unless an upgrade tender names a facility.

```text
site:mopt.gov.lr "National Data Center" OR "National Data Centre"
site:mopt.gov.lr "disaster recovery" "data"
site:mopt.gov.lr "LTC Mobile" "National Data"
site:mopt.gov.lr "NIR" "co-location" OR "co-location hosting"
site:mopt.gov.lr "Government Data Centers and Cloud Adoption"
site:mopt.gov.lr "County Service Center" ICT
site:otdi.gov.lr "data centre" OR "data center" OR "cloud"
"National Data Center" Liberia "LTC Mobile"
"National Data Centre" Liberia "NIR" "LTC"
"Central Bank of Liberia" "disaster recovery center"
```

Extract: facility/project name, lead MAC, operator/manager, county/city, current status, planned timeline, funding source, and whether the text describes existing infrastructure, planned upgrade, policy, or only a study.

### EPA Liberia

Verified URLs:

- EPA home: https://epa.gov.lr/
- ESIA Procedural Guidelines 2017 PDF: https://epa.gov.lr/wp-content/uploads/2024/06/Environmental-Social-Impact-Assessment-Procedural-Guidelines-2017.pdf

EPA evidence is **A for environmental process and project components**. Datacenter projects may be hidden under buildings, telecom infrastructure, backup generators, fuel storage, substations, fibre/cable, industrial parks, ports, or government campus upgrades.

```text
site:epa.gov.lr "data centre" OR "data center" OR datacentre
site:epa.gov.lr "server room" OR "ICT" OR telecommunications "Environmental"
site:epa.gov.lr/wp-content/uploads "{operator}" ESIA OR EIA
site:epa.gov.lr "{project}" "environmental permit"
"{operator}" Liberia ESIA OR EIA "generator" OR "fuel storage" OR substation
"{county}" Liberia ESIA "telecommunications" OR "ICT"
```

Extract: proponent, project title, EIA/ESIA status, county/locality, power/generator/fuel details, construction scope, and dates.

### LEC and Power Evidence

Verified URL:

- Liberia Electricity Corporation: https://lecliberia.com/

LEC evidence is **A for utility connection, substation, or power-sector claim**. Power-only evidence is **not** enough to create a datacenter record unless the load is named. Because grid reliability is a known constraint in Liberia, serious facilities should be checked for generator/captive power, fuel storage, and redundancy.

```text
site:lecliberia.com "data center" OR "data centre" OR "data"
site:lecliberia.com substation "Monrovia" OR "Lynch" OR "Broad"
"LEC" Liberia "data center" OR "data centre" OR "large customer"
"Liberia" "data centre" generator OR "captive power" OR diesel
"{facility}" Liberia substation OR generator OR "fuel storage"
```

### PPCC Procurement

Verified URL:

- Public Procurement and Concessions Commission: https://www.ppcc.gov.lr/

Use PPCC/e-GP as **A for tenders and contract-stage evidence**. Aggregator tender sites are only C leads unless they link back to PPCC or the procuring MAC.

```text
site:ppcc.gov.lr "data center" OR "data centre" OR datacentre
site:ppcc.gov.lr "National Data Center" OR "National Data Centre"
site:ppcc.gov.lr "disaster recovery" OR "cloud"
site:ppcc.gov.lr server OR "ICT infrastructure" "County Service Center"
"PPCC" Liberia tender "data center" OR "data centre" OR "cloud"
"MoPT" Liberia "National Data Center" tender OR procurement
```

### CCL, LIXP, Cable Landing, and Interconnection

Verified URLs:

- CCL home: https://ccliberia.com/
- CCL about: https://ccliberia.com/about-us/
- LTA LIXP page: https://lta.gov.lr/lixp/
- PCH LIXP page: https://www.pch.net/ixp/details/1897
- PeeringDB LIXPA organization: https://www.peeringdb.com/org/15077
- ACE cable official site: https://ace-submarinecable.com/en/submarine-cable/
- TeleGeography submarine cable map route: https://www.submarinecablemap.com/submarine-cable/africa-coast-to-europe-ace

CCL is the strongest official/operator seed for commercial colocation in Liberia. Its site markets submarine capacity, co-location services, 24/7 hosting with power redundancy/security/NOC, and access to LIXPA with Google cache servers. LTA confirms LIXP was established in 2015 as Liberia's first and only IXP and is owned/operated by LIXPA. PCH confirms LIXP is active in Monrovia and established on 2015-08-04. PeeringDB places LIXPA at the CCL Building / Libtelco Compound, Lynch Street, Monrovia, Montserrado.

Do not double-count:

- **CCL ACE landing/hosting/colo** - facility/operator record.
- **LIXP/LIXPA** - interconnection exchange, likely in the same ecosystem, not a datacenter by itself.
- **Google cache at LIXPA** - edge/cache presence, not a Google Cloud region.

```text
site:ccliberia.com colocation OR "co-location" OR hosting OR "NOC"
site:ccliberia.com "Google cache" OR LIXPA OR LIXP
site:lta.gov.lr LIXP OR LIXPA OR peering
site:pch.net "Liberia Internet Exchange Point"
site:peeringdb.com "CCL Building" "Lynch Street" Liberia
"ACE cable" Monrovia "landing station" Liberia
"CCL" Liberia "landing station" "co-location"
```

### Cloud and Uptime Absence Checks

Official pages are **A for cloud-region or Uptime-award existence/absence at review time**:

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Uptime awards list: https://uptimeinstitute.com/uptime-institute-awards/list

As of this review, these official cloud lists do not show a Liberia region/local zone. Search the Uptime awards list and map for Liberia/LR before accepting any Tier claim.

```text
site:aws.amazon.com Liberia "region" OR "Local Zone"
site:docs.aws.amazon.com/local-zones Liberia
site:learn.microsoft.com/en-us/azure/reliability Liberia
site:cloud.google.com/about/locations Liberia
site:oracle.com/cloud "Liberia" "region"
site:uptimeinstitute.com/uptime-institute-awards Liberia OR "LR"
```

## Official Facility / Project Seed List

| Seed | County / city | Grade | What is verified | Enumeration rule |
|---|---:|---:|---|---|
| CCL ACE landing/hosting/colo node | Montserrado / Monrovia | A | CCL markets co-location, 24/7 hosting, redundancy/security/NOC, LIXPA access; ACE is Liberia's landing cable ecosystem. | Count as commercial/telecom interconnection colo if facility inventory allows. Capacity unknown unless primary source gives it. |
| LIXP / LIXPA | Montserrado / Monrovia | A/B | LTA confirms first/only IXP; PCH confirms active Monrovia IXP; PeeringDB gives CCL/Libtelco Compound address. | Record as IXP/edge interconnection, not standalone datacenter. Link to CCL if physically co-located. |
| National Data Center at LTC Mobile | Montserrado / Monrovia | A | NDS says NDC established at/managed by LTC Mobile, underutilized/outdated, revamp planned 2025-2027. | Count as government datacenter; status existing plus planned upgrade, not new build unless tender/award found. |
| NIR on-premise data storage | Montserrado / Monrovia | A | NDS says NIR has on-premise centralized storage, no dedicated DR, NDC co-location discussions/plans. | Count only as institutional server/data-storage facility; planned co-location should be separate status note. |
| Central Bank of Liberia DR center | Montserrado / Monrovia | A | NDS says CBL has a DR center used primarily by financial institutions. | Count as financial-sector/private DR if inventory includes captive facilities; public location/capacity unknown. |
| Future national DR center | likely Montserrado unless tender says otherwise | A for plan | NDS targets national DR plan and DR center setup by Q4 2027. | Planned only until PPCC/MoPT award, EIA, or commissioning evidence appears. |
| County Service Centers | all 15 counties | A for CSC existence, C for datacenter | NDS says CSCs exist in all counties, under-resourced, not all reliable internet. | Do not count as datacenters unless a site-specific ICT room/datacenter upgrade is documented. |
| Telco facilities: LTC, Lonestar Cell MTN, Orange Liberia, Libermobile/others | mainly Montserrado, network sites nationwide | A for licence/operator claims | LTA/NDS identify sector operators; CCL shareholder context supports interconnection role. | Count only if an official/operator/EPA/PPCC source names a data center, switch center, hosting room, or colocation offer. |

## County-by-County Official Strategy

Run the same official pass for every county:

```text
"{county}" Liberia "data centre"
"{county}" Liberia "data center"
"{county}" Liberia datacentre OR "server room" OR "server farm"
"{county capital}" Liberia "data centre" OR "data center"
"{county}" Liberia "County Service Center" ICT OR server
"{county}" Liberia "cloud" OR "e-government" OR "ICT hub"
site:lta.gov.lr "{county}" data OR ICT OR broadband
site:mopt.gov.lr "{county}" data OR ICT OR "County Service Center"
site:epa.gov.lr "{county}" telecommunications OR ICT OR generator
site:ppcc.gov.lr "{county}" ICT OR server OR "data"
site:lecliberia.com "{county}" substation OR "large customer"
"{operator}" "{county}" Liberia
```

| County | Capital / main localities | Official-first strategy and expected result |
|---|---|---|
| Bomi | Tubmanburg | Search CSC, LTA broadband, LEC power, and Tubmanburg ICT tenders. Expected negative for commercial DC; CSC/server-room leads only. |
| Bong | Gbarnga, Phebe, Suakoko | Search county CSC, Phebe/health ICT, Cuttington/Suakoko, LTA broadband. Expected negative for commercial DC; institutional server rooms possible. |
| Gbarpolu | Bopolu | Search CSC, LTA connectivity, PPCC county ICT. Expected negative; CSC only unless a government upgrade tender names equipment rooms. |
| Grand Bassa | Buchanan, Edina | Search port, Buchanan, mining corridor, LEC/substation, EPA industrial permits, CSC. Expected negative for public colo; port/mining comms rooms are captive only. |
| Grand Cape Mount | Robertsport, Kinjor, Sinje | Search mining/Bea Mountain, Robertsport, Sinje university/ICT, EPA/LEC, CSC. Expected negative for public colo. |
| Grand Gedeh | Zwedru | Search CSC, border connectivity, LTA, EPA/PPCC ICT. Expected negative; institutional/county server rooms only. |
| Grand Kru | Barclayville | Search CSC and county ICT. Expected negative. |
| Lofa | Voinjama, Foya, Zorzor | Search CSC, agriculture/health ICT, border connectivity, micro-hydro/power. Expected negative for commercial DC. |
| Margibi | Kakata, Harbel, Marshall, Robertsfield | Search airport/Robertsfield, Firestone/Harbel industrial power, Marshall, CSC, LTA/LEC/EPA. Expected negative for commercial DC; captive industrial ICT possible. |
| Maryland | Harper, Pleebo | Search Harper/Tubman University, port, LTA outreach, CSC. Expected negative for commercial DC; university/server-room leads possible. |
| Montserrado | Monrovia, Greater Monrovia, Paynesville, Congo Town, Sinkor, Mamba Point, Bushrod Island, Freeport, Lynch Street/Broad Street | Full official pass: CCL, LIXP/LIXPA, LTC Mobile/NDC, CBL DR, NIR, LTA registry/orders, PPCC tenders, EPA, LEC, banks, telcos. This is the only county with verified datacenter/colo/interconnection seeds. |
| Nimba | Sanniquellie, Ganta, Saclepea, Yekepa | Search mining, ArcelorMittal/Yekepa comms, Ganta ICT, CSC, LEC/EPA. Expected negative for public colo; captive mining/server rooms possible. |
| River Cess / Rivercess | River Cess, Cestos City | Search both spellings. Expected negative; CSC only. |
| River Gee | Fish Town | Search CSC, border/county ICT. Expected negative. |
| Sinoe | Greenville | Search port/timber, Greenville, CSC, EPA/LEC. Expected negative for public colo; captive port/industrial ICT possible. |

## Development-Partner Follow-Up

Use these as B sources unless they link to a government tender, official project document, or operator page:

- World Bank Liberia projects: https://projects.worldbank.org/en/country/liberia
- Digital Liberia Week event: https://www.worldbank.org/en/events/2025/10/22/digital-liberia-week
- USAID home/search entry point: https://www.usaid.gov/
- LTA USAID/World Bank page: https://lta.gov.lr/usaid-and-world-bank/

```text
site:worldbank.org Liberia "National Data Center" OR "data centre" OR "data center"
site:worldbank.org Liberia GREAT digital OR "County Service Center"
site:worldbank.org Liberia WARDIP OR "regional digital integration"
site:usaid.gov Liberia digital ICT data
"GREAT project" Liberia "National Data Center" OR ICT
"WARDIP" Liberia "data center" OR cloud OR connectivity
```

## Evidence Extraction Checklist

For every candidate, record:

- `country_code=LR`, county, city/town, locality/street, coordinates if available.
- Facility/project name and aliases: CCL ACE CLS, CCL colo, LIXP/LIXPA, NDC, LTC Mobile NDC, NIR storage, CBL DR.
- Developer/operator/legal owner and parent/shareholder context.
- Evidence grade and exact URL.
- Status basis: operational, established, underutilized, planned, tender, EIA, construction, commissioned, revamp.
- Date basis: publication date, tender deadline, licence date, strategy roadmap date, commissioning date.
- Capacity fields separately: IT load MW, site load MW/MVA, utility import, captive generation, racks, floor area, storage; use unknown when unpublished.
- Caveats: cable landing vs colocation, IXP vs datacenter, telco switch vs public colo, CSC vs datacenter, bank DR vs public colo, MoU vs construction, Monrovia USA false positive.
