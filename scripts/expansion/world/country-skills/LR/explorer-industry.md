# LR Explorer Industry - Liberia Datacenter Discovery

Date reviewed: 2026-08-12. Scope: Liberia (LR) datacenter discovery from operator pages, industry media, local press, cable/IXP records, cloud/edge sources, aggregators, and county-level query patterns.

Division coverage: **15 counties**: Bomi, Bong, Gbarpolu, Grand Bassa, Grand Cape Mount, Grand Gedeh, Grand Kru, Lofa, Margibi, Maryland, Montserrado, Nimba, River Cess / Rivercess, River Gee, Sinoe.

## Reliability Grades

- **A** - Official/operator primary proof for the specific claim: CCL, LTA, MoPT/NDS, EPA, LEC, PPCC, Uptime, official cloud provider, official telco/bank/agency page.
- **B** - Strong industry or institutional lead: DCD, Capacity, CommsUpdate/TeleGeography, SubTel Forum, Developing Telecoms, TechAfrica News, WeAreTech Africa, World Bank/ECOWAS/USAID, PCH/PeeringDB for IXP location, or reputable Liberian press with named site/stage.
- **C** - Discovery lead only: datacenter directory, market-report teaser, social post, tender aggregator, blog repost, or local article that lacks primary-source support.
- **U** - Reject or hold: no physical site, no Liberia context, generic provider availability, or Monrovia Indiana/California result.

## Liberia Industry Frame

- Liberia is a **small, Monrovia-led** market. Most likely records are CCL/ACE cable-landing colocation, LIXP/LIXPA, government NDC at LTC Mobile, NIR/CBL institutional data facilities, telco switch/data rooms, banks, and institutional server rooms.
- No verified hyperscale cloud region, public cloud local zone, or Uptime-certified Tier III/IV commercial campus in Liberia was visible in reviewed official sources.
- CCL is the best commercial/interconnection seed: its official site markets submarine capacity, co-location services, and 24/7 hosting with power redundancy, security, NOC operations, and LIXPA access with Google cache servers.
- LIXP is important but must not be counted as a datacenter by itself. LTA says it is Liberia's first and only IXP, established in 2015 and operated by LIXPA. PCH confirms active status in Monrovia; PeeringDB places LIXPA at the CCL Building / Libtelco Compound, Lynch Street, Monrovia, Montserrado.
- The National Digital Strategy confirms the government NDC has been established at LTC Mobile, is underutilized/outdated, and is targeted for revamp in 2025-2027. It also confirms NIR on-premise data storage and a CBL DR center used mainly by financial institutions.
- Treat `plans`, `MoU`, `revamp`, `needs assessment`, `study`, and `cloud strategy` as pipeline language, not operational status.
- Search both `data centre` and `data center`; include `datacentre`, `colo`, `colocation`, `co-location`, `hosting`, `carrier-neutral`, `landing station`, `IXP`, `LIXP`, `LIXPA`, `Google cache`, `CDN`, `server room`, `NOC`, `switch`, `disaster recovery`, `Tier III`, `Uptime`, `generator`, `captive power`, `substation`, `MW`, and `MVA`.
- Filter out US Monrovia results unless the source explicitly says Liberia/LR or uses Liberian entities.

## High-Signal Industry Sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Cable Consortium of Liberia | https://ccliberia.com/ and https://ccliberia.com/about-us/ | Primary operator proof for ACE landing, submarine capacity, co-location, hosting, LIXPA access, Google cache claim. | A |
| LTA LIXP | https://lta.gov.lr/lixp/ | Official proof that LIXP is Liberia's first/only IXP, established in 2015, operated by LIXPA. | A |
| PCH LIXP | https://www.pch.net/ixp/details/1897 | Confirms LIXP active, Monrovia, Liberia, managed by LIXPA, established 2015-08-04. | B |
| PeeringDB LIXPA | https://www.peeringdb.com/org/15077 | Address/organization lead: CCL Building, Libtelco Compound, Lynch Street, Monrovia, Montserrado. | B/C; user-maintained |
| ACE official cable site | https://ace-submarinecable.com/en/submarine-cable/ | ACE system context and country landings. | A/B |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com/submarine-cable/africa-coast-to-europe-ace | Cable and landing-point discovery. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Trade leads for cable landing station relocation/outage and Monrovia connectivity stories. | B |
| Capacity Media | https://www.capacitymedia.com/ | Telecom/subsea/IXP capacity leads. | B |
| CommsUpdate / TeleGeography | https://www.commsupdate.com/ | Liberia telecom licensing, operator, cable, and connectivity news. | B |
| SubTel Forum | https://subtelforum.com/ | Subsea cable stories; verify against ACE/CCL/LTA. | B |
| Developing Telecoms | https://developingtelecoms.com/ | Telecom and landing-station news; verify against primary sources. | B |
| WeAreTech Africa | https://www.wearetech.africa/ | West Africa digital infrastructure, including LIXP upgrade leads. | B |
| TechAfrica News | https://techafricanews.com/ | Operator/government digital announcements. | B |
| FrontPageAfrica | https://frontpageafricaonline.com/ and https://fpa.news/ | Liberian government/business/ICT reporting. | B/C |
| Daily Observer | https://liberianobserver.com/ | Local ICT and government project leads. | B/C |
| The New Dawn Liberia | https://thenewdawnliberia.com/ | Local digital/government leads. | B/C |
| The Analyst Liberia | https://analystliberiaonline.com/ | Local government/business leads. | B/C |
| LINA / MICAT | https://lina.micat.gov.lr/ | Government news announcements; useful for MoUs and launches. | B |
| allAfrica Liberia | https://allafrica.com/liberia/ | Republishes local press; trace back to original. | C/B |
| Tender aggregators | https://www.liberiatenders.com/ plus web search for TendersOnTime Liberia results | Procurement discovery only; follow to PPCC/procuring MAC. Do not treat blocked or reposted pages as source evidence. | C |
| US trade guide | https://www.trade.gov/country-commercial-guides/liberia-telecommunication | Telecom market context, operators, CCL, LTA. | B |

## Industry Query Sets

### General Press and Trade

```text
site:datacenterdynamics.com/en/news/ Liberia "data centre" OR "data center" OR "landing station"
site:datacenterdynamics.com/en/news/ Monrovia Liberia ACE OR CCL OR cable
site:capacitymedia.com Liberia ACE OR CCL OR LIXP OR "landing station"
site:commsupdate.com Liberia "data" OR ACE OR "submarine cable" OR "LIXP"
site:subtelforum.com Liberia ACE OR "landing station" OR CCL
site:developingtelecoms.com Liberia ACE OR "data centre" OR "landing station"
site:wearetech.africa Liberia IXP OR LIXP OR "data center" OR "data centre"
site:techafricanews.com Liberia "data center" OR "data centre" OR cloud OR IXP
site:frontpageafricaonline.com Liberia "data center" OR "data centre" OR "digital"
site:fpa.news Liberia "data center" OR "data centre" OR "digital"
site:liberianobserver.com "data center" OR "data centre" OR ICT Liberia
site:thenewdawnliberia.com Liberia "data" "ICT" OR "digital"
site:analystliberiaonline.com Liberia "data centre" OR "data center" OR cloud
site:lina.micat.gov.lr Liberia "data" OR ICT OR telecom OR cloud
```

Capture exact stage terms:

- Lead only: `plans`, `seeks`, `MoU`, `study`, `needs assessment`, `strategy`, `framework`.
- Pipeline: `tender`, `RFP`, `PPCC`, `EIA`, `ESIA`, `groundbreaking`, `construction`, `revamp`, `upgrade`.
- Operational: `commissioned`, `launched`, `opened`, `operational`, `hosting`, `colocation`, `NOC`, `Uptime award`, `customer live`.

### Operators and Facility Seeds

| Operator / project | Priority locations | Industry use | Grade rule |
|---|---|---|---|
| CCL | Monrovia, Lynch/Broad Street, Libtelco Compound, PHP Beach / central Monrovia, Freeport/Bushrod Island leads | Primary colocation/interconnection seed; ACE landing ecosystem. | A from CCL; B from cable press; C from directories. |
| LIXP / LIXPA | Monrovia, CCL Building / Libtelco Compound | IXP/peering/edge discovery; Google cache claim via CCL. | A from LTA, B from PCH, B/C from PeeringDB. |
| LTC / LTC Mobile | Monrovia | NDC manager and CCL/Liberian incumbent context. | A from NDS/LTA/operator. |
| Government NDC | Monrovia / LTC Mobile | Government datacenter; revamp target 2025-2027. | A from NDS; tender/award needed for construction status. |
| NIR | Monrovia | On-premise centralized data storage; planned NDC co-location. | A from NDS. |
| CBL | Monrovia | Disaster recovery center used mainly by financial institutions. | A from NDS for existence; use CBL source for address/capacity. |
| Lonestar Cell MTN | Monrovia plus network sites | Telco data/switch rooms; CCL shareholder; aggregator lists `MTN Monrovia`. | A only with operator/LTA/EPA/PPCC; aggregator alone C. |
| Orange Liberia / Cellcom | Monrovia plus network sites | Telco data/switch rooms; CCL shareholder. | A only with operator/LTA/EPA/PPCC. |
| Banks: Ecobank, GTBank, UBA, AccessBank, LBDI, CBL-regulated institutions | Monrovia | In-house DC/DR and payment systems. | A from bank/CBL annual report; B/C from press. |
| Universities and agencies | Monrovia, Harper, Gbarnga/Suakoko, Sinje | Campus server rooms, NREN/ICT upgrades, labs. | Usually C unless a named datacenter/server facility is official. |

```text
"CCL" Liberia "co-location" OR colocation OR hosting OR "landing station"
"Cable Consortium of Liberia" "Google cache" OR LIXPA OR "co-location"
"Liberia Internet Exchange Point" Monrovia facility OR members
"LIXP" OR "LIXPA" Liberia peering OR "Google cache" OR CCL
"LTC Mobile" "National Data Center" Liberia
"National Data Center" Liberia "LTC Mobile" OR MoPT
"NIR" Liberia "co-location" OR "National Data Centre"
"Central Bank of Liberia" "disaster recovery center" OR "data center"
"Lonestar" OR "MTN" Monrovia "data center" OR "data centre" OR "server"
"Orange Liberia" OR Cellcom Monrovia "data center" OR "data centre" OR "server"
"Liberia" "Uptime Institute" "data center" OR "Tier III"
```

### Cloud, Edge, and CDN

Official absence checks:

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

No Liberia region/local zone was visible on these official pages as of this review. Count CCL's Google cache/LIXPA claim as **edge/cache/interconnection**, not as Google Cloud, Google datacenter, or Google region.

```text
site:aws.amazon.com Liberia "region" OR "Local Zone"
site:docs.aws.amazon.com/local-zones Liberia
site:learn.microsoft.com/en-us/azure/reliability/regions-list Liberia
site:cloud.google.com/about/locations Liberia
site:oracle.com/cloud "Liberia" "public cloud region"
"Google cache" Liberia LIXP OR LIXPA OR CCL
"Liberia" "cloud region" OR "cloud data center" OR "sovereign cloud"
```

### Directories and Aggregators

Use only as leads unless corroborated:

```text
site:datacenters.com Liberia Monrovia CCL OR "Cable Consortium"
site:datacenters.com/providers/cable-consortium Liberia
site:datacenterplatform.com Liberia Monrovia MTN OR "data center"
site:colo.exchange Liberia OR Monrovia
site:datacenterplanet.com Liberia OR Monrovia
site:cloudscene.com Liberia OR Monrovia
site:peeringdb.com Liberia Monrovia facility OR "LIXP"
```

Known lead patterns:

- `CCLiberia Cable Landing Facility Monrovia` appears in directories. Confirm with CCL/LTA/PCH/PeeringDB before counting and do not copy directory capacity fields without primary support.
- `MTN Monrovia` appears in aggregator listings. Treat as C until MTN/Lonestar, LTA, EPA, or procurement evidence names the facility.
- `DatacenterMap` and similar pages may be incomplete or behind bot protection; use as alternate-name discovery only.

## County-Level Industry Matrix

For each county:

```text
"{county}" Liberia ("data centre" OR "data center" OR datacentre) ("MW" OR racks OR "IT load" OR server)
"{county capital}" Liberia ("data centre" OR "data center") (opened OR launched OR commissioned OR construction OR revamp)
"{county}" Liberia colocation OR "co-location" OR "carrier neutral" OR "Tier III" OR "Tier IV"
"{county}" Liberia "cloud" OR "e-government" OR "County Service Center" OR "ICT hub"
"{county}" Liberia "captive power" OR generator OR substation
"{operator}" "{county OR town}" Liberia
site:frontpageafricaonline.com "{county}" "data" OR ICT
site:fpa.news "{county}" "data" OR ICT
site:liberianobserver.com "{county}" ICT OR digital
site:lina.micat.gov.lr "{county}" ICT OR telecom OR digital
```

| County | Capital / main localities | Industry seeds and handling |
|---|---|---|
| Bomi | Tubmanburg | Legacy mining/county ICT. Expected negative. Count only named institutional server rooms with primary support. |
| Bong | Gbarnga, Phebe, Suakoko | County Service Center, health/eHealth, Cuttington/Suakoko ICT. Expected negative for public colo. |
| Gbarpolu | Bopolu | CSC and connectivity-only leads. Expected negative. |
| Grand Bassa | Buchanan, Edina | Port, Freeport/industrial, mining corridor, LEC/EPA leads. Captive comms possible; public colo unlikely. |
| Grand Cape Mount | Robertsport, Kinjor, Sinje | Mining/Bea Mountain, Sinje campus, coastal connectivity. Expected negative for commercial DC. |
| Grand Gedeh | Zwedru | CSC and border connectivity. Expected negative. |
| Grand Kru | Barclayville | CSC only. Expected negative. |
| Lofa | Voinjama, Foya, Zorzor | Agriculture/NGO/health ICT, border links, power. Expected negative. |
| Margibi | Kakata, Harbel, Marshall, Robertsfield | Firestone/Harbel industrial ICT, airport/Robertsfield, Marshall, CSC. Captive enterprise rooms possible; public colo unlikely. |
| Maryland | Harper, Pleebo | Harper port, Tubman University, LTA outreach/cybersecurity leads, CSC. Usually server-room only. |
| Montserrado | Monrovia, Paynesville, Congo Town, Sinkor, Mamba Point, Bushrod Island, Freeport, Lynch Street/Broad Street | Highest-recall pass. CCL colo, LIXP/LIXPA, NDC/LTC Mobile, NIR, CBL DR, Lonestar/MTN, Orange, banks, agencies. Deduplicate carefully and filter US Monrovia hits. |
| Nimba | Sanniquellie, Ganta, Saclepea, Yekepa | Mining communications at Yekepa, Ganta commercial activity, CSC. Captive only unless operator/official evidence says hosting/colo. |
| River Cess / Rivercess | River Cess, Cestos City | Search both spellings. CSC only; expected negative. |
| River Gee | Fish Town | CSC/border connectivity. Expected negative. |
| Sinoe | Greenville | Port/timber/industrial ICT, CSC. Captive server rooms possible; public colo unlikely. |

## Donor and Programme Signals

Follow donor language to tenders and implementation records:

- World Bank Liberia projects: https://projects.worldbank.org/en/country/liberia
- Digital Liberia Week: https://www.worldbank.org/en/events/2025/10/22/digital-liberia-week
- LTA Liberia Digital Transformation Project: https://lta.gov.lr/liberia-digital-transformation/
- LTA USAID/World Bank page: https://lta.gov.lr/usaid-and-world-bank/
- USAID home/search entry point: https://www.usaid.gov/

```text
"GREAT project" Liberia "National Data Center" OR ICT OR "County Service Center"
"WARDIP" Liberia "data center" OR cloud OR "digital integration"
site:worldbank.org Liberia "data center" OR "data centre" OR "National Data Center"
site:worldbank.org Liberia "County Service Center" ICT OR digital
site:usaid.gov Liberia digital ICT data cloud
```

Do not turn donor programme names into datacenter records unless a physical facility, procurement package, or implementation site is named.

## Final Validation Rules

- Require county + city/locality for every facility candidate. Minimum for Liberia should be `Montserrado / Monrovia` unless the source gives another county.
- Confirm that the source is Liberia, not Monrovia IN/CA.
- Separate facility types: cable landing station, colocation/hosting room, IXP, telco switch/data room, government NDC, institutional server room, bank DR, cloud region.
- Keep stage honest: NDC is established/underutilized plus planned revamp; national DR center is planned; CCL colo is operator-marketed; LIXP is active IXP; NIR co-location is planned/discussed in the NDS.
- Never assign hyperscale, cloud-region, Tier III/IV, MW, racks, or uptime claims from aggregators without primary proof.
- Deduplicate Monrovia records: CCL facility, LIXP/LIXPA, NDC/LTC Mobile, NIR storage, CBL DR, telco facilities, and bank facilities are separate only when the evidence supports separate physical/operator identities.
- Use `River Cess` and `Rivercess` in searches; both appear in sources.
