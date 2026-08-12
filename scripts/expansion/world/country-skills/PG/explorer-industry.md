# PG Explorer Industry - colo providers, cloud, trade press, and province queries

Date: 2026-08-12. Scope: Papua New Guinea datacenter enumeration methodology focused on industry/vendor discovery: PNG colocation and telecom operators, sovereign/government cloud, hyperscaler-region checks, trade press, associations, connectivity-led leads, and repeatable province-level query patterns. Reliability grades: **A** = official/primary source (operator page, government/SOE page, regulator, procurement/standards document, cloud-provider official region list, contractor project page), **B** = strong secondary/trade press/local business press/vendor case study with named details, **C** = directory, map, social post, market report snippet, or unverified mention.

---

## 0. Papua New Guinea-specific frame

- PNG has no public national datacenter registry. Enumeration works best by triangulating **operator pages**, **state-owned enterprise/SOE announcements**, **Department of ICT digital-government material**, **NICTA licensing context**, **National Procurement Commission tenders/awards**, **subsea cable/IXP sources**, **trade press**, and **data-center directories**.
- Expect a small market. The Internet Society Pulse country report listed **2 active data centers and 2 active IXPs in Papua New Guinea in 2026**: https://pulse.internetsociety.org/en/reports/pg/. Treat this as market context, not a complete facility register.
- Hard facility evidence is concentrated in **National Capital District / Port Moresby** and **Madang**. Secondary watch locations are **Morobe / Lae**, **Western Highlands / Mount Hagen**, **West Sepik / Vanimo**, **Bougainville / Arawa-Buka**, **East New Britain / Kokopo-Rabaul**, **Milne Bay / Alotau**, **New Ireland / Kavieng**, and **Northern / Popondetta** because these are cable, telco, government, or provincial ICT nodes.
- PNG sources usually use English. Search both **data centre** and **data center**; also use `datacentre`, `cloud`, `sovereign cloud`, `AI data centre`, `GovCloud`, `government cloud`, `Tier III`, `colocation`, `co-location`, `hosting`, `disaster recovery`, `DR site`, `cable landing station`, `CLS`, `MCLS`, `IXP`, `PPC-1`, `Coral Sea Cable`, `Kumul Submarine Cable`, `Pukpuk`, `Bulikula`, `Hawaiki Nui`, `earth station`, and `regional data centre`.
- Tok Pisin/local-language searching has low yield for commercial datacenters. Use it only as a secondary check for local press/social posts: `senta bilong data`, `data senta`, `intanet`, `klaut`, `seva`, `kabel`, `laen`, `launisim`, `gavman`. Verify all such hits against English official or operator sources.
- Do not overcount telecom network facilities. In PNG, `data centre` may mean a mobile core/network operations room, cable landing station, provincial government server room, micro-edge rack, or cloud product launch. Count a record as a datacenter only when it has a physical facility/operator, hosting/compute/colo/DR function, and a province/city/site signal.

---

## 1. Source map and grades

### 1.1 Primary / official sources

| Source | URL | Use | Grade |
|---|---|---|---|
| PNG DataCo - Data Center Services | https://www.pngdataco.com/services/ict-and-cloud-solutions/data-center-services/ | Best official source for PNG DataCo's Tier 3/ISO-certified sovereign hosting and rack-space offer. Pivot to Port Moresby, Madang, NTN, KSCN, PPC-1, Coral Sea Cable, Oracle, and government cloud. | A |
| PNG DataCo corporate/news pages | https://www.pngdataco.com/ | Operator news for cable landings, network outages, Coral Sea Cable, KSCN provincial landings, Google/Bulikula/Pacific Connect, and DataCo cloud partnerships. | A |
| Datec PNG - Datacenter service page | https://datec.com.pg/detail/internet-datacenter/datacenter | Official Datec service page for cloud, equipment colocation, disaster recovery, and BCP suite. It confirms Datec as a PNG colo/cloud operator, but may not expose full facility address/capacity. | A for services; B for facility inference if no address |
| Datec / Telikom / CloudSigma sovereign AI data-centre announcement | Datec: https://www.datec.com.pg/detail/papua-new-guinea-advances-with-launch-of-first-sovereign-ai-data-centre ; Kumul Consolidated Holdings: https://www.kch.com.pg/papua-new-guinea-advances-with-launch-of-first-sovereign-ai-data-centre/ | Primary/SOE confirmation of the March 2026 pre-launch of PNG's first Sovereign AI Data Centre with Telikom, Datec, and CloudSigma. Verify whether it is a new physical site, an existing Datec/Telikom facility, or a cloud stack hosted in-country. | A for launch/partners; B until physical site/capacity is confirmed |
| Department of ICT (DICT) | https://www.ict.gov.pg/ | Digital Government Plan, Government Cloud Policy, cloud/data-centre standards, GovCloud events, RFIs, and national data-centre procurement references. Search PDFs and news. | A |
| DICT Government Cloud Standards PDF | https://www.ict.gov.pg/Digital%20Standards/Government%20Cloud%20Standards%2C%20guideline%20and%20specifications.pdf | Official standards context for public-sector cloud migration, IaaS, redundancy/connectivity requirements. Helps interpret government cloud references as policy/service requirements rather than facility evidence. | A |
| DICT Digital Transformation Summit / DTS pages | https://www.ict.gov.pg/90168-2/ | Good source for current domestic provider universe; DTS25 named Digitec, Datec, APCS, AWS, Oracle, Alibaba in cloud/data-centre hosting discussions and introduced GovCloud. | A/B |
| NICTA | https://www.nicta.gov.pg/ | Regulator for ICT licensing. Use for licensee/permit context for Telikom, Digicel, Vodafone/Digitec, ISPs, Starlink, and market-entry barriers. It is not a facility registry. | A |
| National Procurement Commission | https://npc.gov.pg/ | Search tenders/awards for `data centre`, `Government Cloud`, `e-GP`, `NOC`, `server`, `hosting`, `ICT platform`. Public records may reveal government hosting/procurement before operator pages. | A when a tender/award record is found |
| PNG ICT Cluster | https://ictcluster.org.pg/ | Local industry association/events. Useful for provider names and digital-economy context; not a facility register. | B/C |
| Coral Sea Cable Company | https://coralseacablecompany.com/the-system | Primary-ish system page for the 4,700 km Sydney-Port Moresby-Honiara cable and Port Moresby landing context. | A/B |
| Kumul Consolidated Holdings telecommunications page | https://www.kch.com.pg/investor-centre/key-impact-projects/telecommunications/ | SOE parent context for Coral Sea Cable and DataCo infrastructure; useful for national backbone/subsea framing. | A |
| PNG Power | https://www.pngpower.com.pg/ | Grid/power context for large-load claims. Search Port Moresby substations, Kanudi/Bomana, Lae, Madang, and provincial electrification. | A/B |

### 1.2 Trade press, local press, and directories

Use press to discover project names, operators, locations, and status verbs, then verify with an operator/SOE/government page.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics - PNG tag | https://www.datacenterdynamics.com/en/tags/papua-new-guinea/ | Best global trade feed for PNG datacenter/subsea/edge items: NFA Zella edge deployment, Huawei-built government data centre, cable breaks, Puk-Puk 1, Google cable plans. | B |
| Business Advantage PNG | https://www.businessadvantagepng.com/ | Strong local business source for DataCo, Oracle, Huawei government data centre issues, Digicel/Vodafone, and ICT investment context. | B |
| Developing Telecoms | https://developingtelecoms.com/ | Telecom trade press for DataCo/Oracle, Digicel upgrades, Vodafone/Digitec, Starlink, Pukpuk, and regional network projects. | B |
| PNG Business News / The PNG Bulletin / EMTV / NBC PNG / FM100 | https://www.pngbusinessnews.com/ ; https://thepngbulletin.com/ ; https://www.emtv.com.pg/ ; https://www.nbc.com.pg/ ; https://fm100.com.pg/ | Local announcements for sovereign AI data centre, Datec roadshows, Morobe digital government, policy events, provincial ICT launches. Verify because wording may call a cloud platform a data centre. | B/C |
| APAC Outlook | https://www.apacoutlookmag.com/ | Useful executive-interview source for Vodafone PNG main Port Moresby data centre and planned regional data centres in Lae/Mount Hagen; also DataCo context. | B |
| DataCenterMap | https://www.datacentermap.com/papua-new-guinea/ | Directory lead source; currently useful for PNG DataCo Port Moresby and Madang CLS. Verify operator pages because directory pages may be incomplete/stale. | C/B- |
| Inflect | https://inflect.com/datacenters/apac/papua-new-guinea | Directory lead source; useful for Datec PNG Port Moresby and market notes. Use only as seed unless operator confirms. | C |
| Cloudscene / PeeringDB / Packet Clearing House / IXP Tracker | https://www.cloudscene.com/ ; https://www.peeringdb.com/ ; https://www.pch.net/ixp ; https://pulse.internetsociety.org/ | Interconnection layer: PNG-IX/PNGIX, ASNs, facility/metro names, caches, carrier presence. Proves network exchange presence, not datacenter capacity. | B/C |
| SubmarineNetworks / TeleGeography Submarine Cable Map / SubTel Forum | https://www.submarinenetworks.com/ ; https://www.submarinecablemap.com/ ; https://subtelforum.com/ | Cable landing and CLS leads: KSCN, PPC-1, Coral Sea Cable, Puk-Puk 1, Hawaiki Nui, Bulikula/Pacific Connect. | B/C unless operator/government-owned page |
| LinkedIn/Facebook/Instagram posts by operators/ministers | operator-owned social pages | Often the only source for facility photos, launch events, or provincial roadshows. Use as discovery only unless posted by an official operator/government account and backed by another source. | C/B- |

High-value trade queries:

```text
site:datacenterdynamics.com/en/news/ "Papua New Guinea" "data center"
site:datacenterdynamics.com/en/news/ "Papua New Guinea" "data centre"
site:datacenterdynamics.com/en/news/ "PNG DataCo" OR "Telikom" OR "Datec"
site:businessadvantagepng.com "data centre" "Papua New Guinea"
site:businessadvantagepng.com "PNG DataCo" Oracle "data centre"
site:developingtelecoms.com "Papua New Guinea" "data centre" OR "cloud"
site:nbc.com.pg Datec "data centre" Lae
site:fm100.com.pg Telikom Datec CloudSigma "data center"
site:apacoutlookmag.com Vodafone PNG "data centre" Lae "Mount Hagen"
```

---

## 2. Operator, colo, and telecom seed list

| Operator / developer | Primary / useful URL | PNG geography signals | Notes |
|---|---|---|---|
| PNG DataCo | https://www.pngdataco.com/services/ict-and-cloud-solutions/data-center-services/ | Port Moresby/NCD primary data centre; Madang CLS/DR lead; national cable backbone | State-owned wholesale/transmission operator. Strongest official route for sovereign hosting and DataCo-managed data centres. Search `Gerehu`, `Earth Station Road`, `Madang CLS`, `Modilon Road`, `NTN`, `KSCN`, `PPC-1`. |
| Telikom Limited / Telikom PNG | https://www.telikompng.com.pg/ | Port Moresby and national telco sites | Telikom is a partner in the 2026 sovereign AI data-centre/cloud launch with Datec and CloudSigma. Search Telikom site and SOE pages for cloud/hosting specifics. |
| Datec PNG | https://datec.com.pg/detail/internet-datacenter/datacenter | Port Moresby/NCD; Lae roadshow/branches; national enterprise services | Officially offers cloud, equipment colocation, DR, and BCP services. Cross-check Inflect, Datec news, and Telikom/CloudSigma launch materials. |
| CloudSigma | https://www.cloudsigma.com/ | In-country sovereign AI/cloud partnership with Datec/Telikom | Official CloudSigma pages may lag local announcements. Treat as cloud/service partner until physical hosting site is confirmed. |
| Digitec / Vodafone PNG | https://vodafone.com.pg/about/about-us/vodafone-png | Port Moresby main data centre; planned/possible regional data centres in Lae and Mount Hagen | APAC Outlook reported Vodafone PNG's office/main data centre in Port Moresby and regional data centres commencing in Lae then Mount Hagen. Verify current state through Vodafone/Digitec pages, NICTA/ICCC filings, local maps, and site photos. |
| Digicel PNG / Digicel Pacific | https://www.digicelpacific.com/ | Port Moresby, Lae, Kokopo, Mount Hagen, Wewak, Bougainville coverage nodes | Usually telecom network/mobile-core infrastructure, not public colo. Search for `data centre`, `core`, `network upgrade`, `Lae`, `Port Moresby`; count only when hosting/colo/DR function is explicit. |
| Online South Pacific / online.net.pg | https://www.online.net.pg/data_centre.html | Port Moresby | Claims two Port Moresby data centres for co-location. Verify ownership, current status, and addresses before grade above B/C. |
| Daltron PNG | https://www.daltronpng.com/technical-services/ | Port Moresby and national enterprise IT | IT services, servers/storage/power; likely integrator rather than facility operator unless a data-centre/hosting page or contract appears. |
| APCS / AP+CS | search DICT DTS, local ICT events | Port Moresby likely | Mentioned in DICT cloud/data-centre hosting event context. Needs official operator confirmation. |
| Bank South Pacific / BSP | RPS project page: https://www.rpsgroup.com/projects/bank-of-south-pacific-data-and-operations-centres-papua-new-guinea/ | Port Moresby/NCD | Enterprise data and operations centres; not colo, but important private-sector facility evidence. RPS page is primary vendor/project evidence. |
| Government of PNG / Huawei-built Government National Data Centre | DICT docs and DCD/Business Advantage coverage | Port Moresby/NCD | Opened around 2018; DCD reported major security/maintenance failures in 2020. Treat as government facility with uncertain current operational quality/status; verify in current DICT/GovCloud documents before marking active. |
| National Fisheries Authority / Zella DC | DCD 2024 article and NFA/Zella posts | Site unspecified unless source gives location | Micro-edge deployment, not a colo facility. Capture as edge datacenter only with exact site/province evidence. |

Operator sweep templates:

```text
site:pngdataco.com "data center" OR "data centre" OR "Data Center Services"
site:pngdataco.com Madang "data centre" OR CLS OR "cable landing"
site:pngdataco.com "Gerehu" OR "Earth Station" "data"
site:datec.com.pg "datacenter" OR "data centre" OR colocation OR "co-location"
site:datec.com.pg Telikom CloudSigma "AI Data Centre"
site:telikompng.com.pg "data centre" OR cloud OR CloudSigma OR Datec
site:vodafone.com.pg "data centre" OR datacenter OR "regional data"
site:online.net.pg "Data Centre" "co-location"
site:digicelpacific.com "Papua New Guinea" "data centre" OR "network core"
site:daltronpng.com "data centre" OR hosting OR "server"
"PNG DataCo" "Tier 3" "data centre" "Port Moresby"
"PNG DataCo" "Madang" "CLS" "data center"
"Datec PNG" "Port Moresby" colocation "data center"
"Vodafone PNG" "main data centre" "Port Moresby"
"Vodafone PNG" "regional data centres" Lae "Mount Hagen"
"Bank of South Pacific" "data centre" "Papua New Guinea"
```

---

## 3. Cloud-region and sovereign-cloud sweep

No major global hyperscaler public cloud region was found in PNG as of this methodology date. Do not infer a hyperscale region from local sales offices, partners, training, or reseller announcements. Use official region lists for A-grade region status and local operator/SOE pages for in-country sovereign-cloud deployments.

| Provider | Official page / route | PNG signal | Grade |
|---|---|---|---|
| AWS | AWS regions docs: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/ | No PNG Region/Local Zone/Wavelength Zone found. DICT DTS listed AWS in a cloud/data-centre hosting panel, so search for partnerships/training, but do not record a PNG physical region without AWS official confirmation. | A for absence/presence on official list |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | No PNG Azure public region found; nearest practical regions are in Australia/Asia depending workload. Search for government cloud partnerships separately. | A |
| Google Cloud | Google Cloud locations: https://cloud.google.com/about/locations ; data-center locations: https://datacenters.google/locations/ | No Google Cloud region or Google-owned datacenter location in PNG. Google is relevant through Pacific Connect/Bulikula/Pukpuk subsea cable initiatives, which are connectivity leads, not cloud-region evidence. | A for region/location list; B for cable press |
| Oracle Cloud / OCI | OCI public regions: https://www.oracle.com/cloud/public-cloud-regions/ | No public OCI region in PNG on Oracle's global list. However, PNG DataCo/Oracle and DICT materials indicate local Oracle infrastructure/partnership discussions; treat as sovereign/dedicated/partner cloud until Oracle/DataCo identify facility and product scope. | A for official public regions; B for local partnership |
| Alibaba Cloud | Alibaba region list: https://www.alibabacloud.com/global-locations | DICT DTS listed Alibaba in cloud/data-centre hosting discussion. No PNG public region found; treat as sales/partner context unless official region or local deployment appears. | A for region list |
| CloudSigma | https://www.cloudsigma.com/ | Partner in the 2026 Telikom/Datec sovereign AI data-centre launch. Search CloudSigma official posts plus Datec/Telikom/KCH pages to verify physical footprint and production status. | A/B |

Hyperscaler/cloud queries:

```text
"Papua New Guinea" "AWS" "Local Zone" OR "Wavelength"
"Papua New Guinea" "Azure region" OR "Microsoft cloud"
"Papua New Guinea" "Google Cloud" "region" OR "data center"
"Papua New Guinea" "Oracle Cloud Infrastructure" "DataCo"
"PNG DataCo" Oracle "cloud infrastructure" "data centre"
"Papua New Guinea" Alibaba Cloud "data centre"
"CloudSigma" "Datec PNG" "Telikom" "AI Data Centre"
"Government Cloud" "Papua New Guinea" "data centre"
site:ict.gov.pg "GovCloud" "data centre"
site:ict.gov.pg "Cloud/Data Centre Hosting Innovations"
```

---

## 4. Connectivity and interconnection pivots

PNG facility discovery is often easier through network infrastructure than through real-estate/planning sources.

| Pivot | Source / URL | How to use | Grade |
|---|---|---|---|
| Coral Sea Cable System | https://coralseacablecompany.com/the-system ; KCH page https://www.kch.com.pg/investor-centre/key-impact-projects/telecommunications/ | Port Moresby international landing/backbone evidence. Search for modular cable landing station, MCLS, DataCo, Vocus, Alcatel Submarine Networks. | A/B |
| Kumul Submarine Cable Network | PNG DataCo news and SubmarineNetworks: https://www.submarinenetworks.com/en/systems/asia-australia/png-national/png-national | Links fourteen provinces and the two national data centres in Port Moresby and Madang according to cable-system summaries. Use provincial landings as search seeds, not automatic datacenter records. | B unless DataCo page |
| PPC-1 | DataCenterMap Madang CLS and cable maps | Important Madang CLS/international cable lead. Search `PPC-1 Madang data centre`, `Modilon Road`, `Madang CLS`. | B/C |
| Puk-Puk 1 | DCD 2026: https://www.datacenterdynamics.com/en/news/puk-puk-1-cable-linking-papua-and-papua-new-guinea-goes-live/ | Vanimo/West Sepik watch lead. Cable lands in Vanimo and connects to Jayapura; do not infer a datacenter without CLS/facility evidence. | B |
| Google/Pukpuk Connectivity Initiative | DCD 2025: https://www.datacenterdynamics.com/en/news/google-to-build-three-subsea-cables-in-papua-new-guinea-as-part-of-australian-defense-treaty/ ; DICT press release search | Search for northern/southern PNG and Bougainville cable routes, landing stations, and any Google edge/cache/on-ramp follow-up. | A/B |
| PNG-IX / IXP | APNIC blog: https://blog.apnic.net/2017/04/20/launching-papua-new-guineas-first-neutral-ixp/ ; PeeringDB/PCH/ISOC Pulse | IXP location/member clues for hosting buildings and carrier-neutral nodes. It proves interconnection presence, not a commercial datacenter by itself. | B |

Connectivity queries:

```text
"Kumul Submarine Cable Network" "data centres" "Port Moresby" Madang
"Kumul Submarine Cable" "{province OR town}" "landing"
"PPC-1" Madang "data centre" OR CLS
"Coral Sea Cable" "Port Moresby" "landing station" OR MCLS
"Puk-Puk 1" Vanimo "cable landing" "PNG DataCo"
"Bulikula" "PNG DataCo" "landing station"
"Hawaiki Nui" "Papua New Guinea" "landing"
"PNG-IX" "data centre" OR facility OR "Port Moresby"
site:peeringdb.com "Papua New Guinea" "Port Moresby"
```

---

## 5. Government/procurement and standards sweep

Planning-permit discovery is weak in PNG compared with Australia/NZ/UK. For public-sector facilities, use DICT, NPC, SOE, and regulator records first.

```text
site:ict.gov.pg "data centre" "Papua New Guinea"
site:ict.gov.pg "Government Cloud" "data centre"
site:ict.gov.pg "Data Centre Standards"
site:ict.gov.pg "Tier III" "national data centre"
site:ict.gov.pg "GovCloud"
site:npc.gov.pg "data centre"
site:npc.gov.pg "Government Cloud"
site:npc.gov.pg "server" "hosting"
site:npc.gov.pg "National Operations Centre" "data"
site:nicta.gov.pg "data centre" OR "cloud"
site:nicta.gov.pg "registered licensees" Digitec OR Datec OR Telikom OR Digicel
site:iccc.gov.pg Digitec "data-centre hosting"
```

When a government or procurement hit appears, capture:

- Procuring agency, NPC reference, tender/award date, supplier, value, scope, and whether it is works, managed service, hosting, software, or cloud.
- Whether the source identifies a **physical site** or only a service/platform.
- Whether it connects to DICT standards, Government Cloud Policy, Digital Government Plan, National Cyber Security Centre/CERT, Integrated Government Information System (IGIS), or PNG DataCo.
- Stage words: `RFI`, `EOI`, `RFP`, `tender`, `contract awarded`, `pre-launch`, `launch`, `migration`, `operational`, `procure a Tier III national data centre`.

---

## 6. National query templates

### 6.1 Facility discovery

```text
"Papua New Guinea" ("data centre" OR "data center" OR datacentre) (Port Moresby OR Madang OR Lae OR "Mount Hagen")
"PNG" ("data centre" OR "data center") (colocation OR "co-location" OR hosting OR "disaster recovery")
"Papua New Guinea" "Tier III" "data centre"
"Papua New Guinea" "ISO-certified" "data center"
"Papua New Guinea" "sovereign data centre" OR "Sovereign AI Data Centre"
"Papua New Guinea" "Government National Data Centre" OR GNDC
"Papua New Guinea" "GovCloud" "data centre"
"Papua New Guinea" "AI data centre" CloudSigma Datec Telikom
"Papua New Guinea" "micro data center" OR "edge data center" OR Zellabox OR Zella
```

### 6.2 Capacity/status extraction

```text
"{project/operator}" ("MW" OR MVA OR kVA OR racks OR cabinets OR sqm OR "square metres")
"{project/operator}" ("Tier 3" OR "Tier III" OR "Uptime Institute" OR ISO)
"{project/operator}" ("opened" OR launched OR "pre-launched" OR operational OR commissioned)
"{project/operator}" ("construction" OR "procure" OR tender OR RFP OR "contract awarded")
"{project/operator}" ("backup power" OR UPS OR generator OR cooling OR redundancy)
```

### 6.3 Weak lead filters

Use these to avoid false positives:

```text
"data centre" "Papua New Guinea" -"call centre" -"training centre"
"data center" "Papua New Guinea" -"health centre" -"resource centre"
"data centre" PNG "server room"
"data centre" PNG "mobile core" OR "network operations"
```

If the source only says `server room`, `ICT resource centre`, `training centre`, `NOC`, or `digital service platform`, do not count it as a datacenter unless hosting/colo/compute infrastructure and a physical facility are explicit.

---

## 7. Province-by-province enumeration recipes

For every province/district/autonomous region, run five passes:

1. **Operator pass (A/B)**: province + main town + PNG DataCo, Telikom, Datec, Digicel, Vodafone/Digitec, Online South Pacific, Daltron, CloudSigma, Oracle.
2. **Connectivity pass (B/C)**: province + KSCN, Coral Sea Cable, PPC-1, Puk-Puk, Bulikula, Hawaiki Nui, cable landing, CLS, MCLS, IXP, earth station.
3. **Government/procurement pass (A/B)**: province + DICT, NPC, GovCloud, Digital Government, National Data Centre, server/hosting/tender.
4. **Local press pass (B/C)**: NBC PNG, EMTV, Post-Courier, The National PNG, PNG Business News, Business Advantage PNG, provincial government/Facebook pages.
5. **Directory/OSM pass (C)**: DataCenterMap, Inflect, Cloudscene, PeeringDB, Google Maps/OSM/Mapcarta for named buildings such as `Vodafone Data Centre` or `PNG DataCo CLS`; verify with operator before grade above C.

Universal province template:

```text
"{province}" "Papua New Guinea" "data centre"
"{province}" PNG "data center"
"{main town}" PNG datacentre OR "data centre"
"{main town}" "PNG DataCo" OR Telikom OR Datec OR Digicel OR Vodafone
"{main town}" PNG colocation OR "co-location" OR hosting
"{main town}" PNG "cable landing" OR CLS OR "earth station"
"{province}" PNG "Kumul Submarine Cable" OR KSCN
"{province}" PNG "Government Cloud" OR GovCloud
site:ict.gov.pg "{province OR town}" "data centre" OR cloud
site:npc.gov.pg "{province OR town}" "data centre" OR server OR hosting
site:datacenterdynamics.com/en/news/ "Papua New Guinea" "{province OR town}"
site:businessadvantagepng.com "{province OR town}" "data centre"
```

### 7.1 Priority geographies

| Division | Main towns / localities | Seeds and query notes |
|---|---|---|
| National Capital District | Port Moresby, Waigani, Hohola, Gerehu, Boroko, Poreporena Freeway | Highest priority. Search PNG DataCo Primary Data Centre, Datec Port Moresby, Telikom/Datec/CloudSigma sovereign AI data centre, Online South Pacific, Vodafone main data centre, BSP data/operations centres, Huawei-built government data centre, PNG-IX, Coral Sea Cable landing, Gerehu Earth Station. |
| Madang | Madang town, Modilon Road | Highest non-NCD priority. Search PNG DataCo Madang CLS, PPC-1, KSCN, disaster recovery, Madang cable landing, DataCo outages. Directory evidence is common; seek PNG DataCo confirmation. |
| Morobe | Lae, Nadzab, Huon Gulf | Watch for Vodafone regional data centre, Datec Lae AI/cloud roadshow, Morobe provincial government DataCo/Oracle digital government project, Digicel upgrades, KSCN/cable nodes. Treat cloud/digital-government projects as non-facility until a building is identified. |
| Western Highlands | Mount Hagen | Watch for Vodafone regional data centre plan, Highlands network aggregation, Digicel/Vodafone/Telikom nodes, airport/electricity reliability. Search `Mt Hagen` and `Mount Hagen`. |
| West Sepik | Vanimo | Watch for Puk-Puk 1 landing with Telkom Indonesia/Telin and PNG DataCo. Search for Vanimo CLS/cable landing station follow-up; do not count cable landing alone as datacenter. |
| Bougainville | Arawa, Buka, Kokopau | Watch Google/Pukpuk/Pacific Connect and KSCN/Bougainville cable landings. Search Autonomous Region of Bougainville pages and local press for digital government/server projects. |
| East New Britain | Kokopo, Rabaul, Gazelle | KSCN landing/connectivity and Digicel/telecom upgrades; no confirmed public colo lead from industry sources. Search provincial government and cable terms. |
| Milne Bay | Alotau | KSCN/earthquake outage/cable link watch area. Search `Alotau data centre`, `Madang Alotau cable`, and DataCo outage notices. |
| New Ireland | Kavieng, Namatanai | KSCN landing in Kavieng is a connectivity seed. Search for CLS, provincial ICT, tourism/government hosting. |
| Northern | Popondetta, Oro Bay | KSCN/Alotau-Popondetta outage references; likely connectivity-only. Search DataCo, cable break, CLS, provincial ICT. |
| Central | Port Moresby outskirts, Bautama, Laloki, Sogeri | Avoid misattributing NCD Port Moresby facilities to Central Province. Search if sources mention land just outside NCD, data-centre campus, solar/power, or government infrastructure. |
| Western | Kiunga, Tabubil, Daru | Mining/enterprise ICT and Ok Tedi/Tabubil communications may produce server-room or DR leads. Search enterprise/vendor case studies; require facility proof. |
| East Sepik | Wewak, Maprik | Digicel/Vodafone network expansion and KSCN provincial capital connectivity; no confirmed DC. Search `Wewak data centre`, `East Sepik server`, `KSCN Wewak`. |
| West New Britain | Kimbe, Bialla | Search cable/telecom/provincial government ICT; likely no commercial DC. |
| New Ireland, Manus, Gulf | Kavieng, Lorengau, Kerema | Mostly connectivity/provincial government/server-room searches. Use KSCN/cable and DICT/NPC terms. |
| Highlands provinces: Chimbu, Eastern Highlands, Enga, Hela, Jiwaka, Southern Highlands | Kundiawa, Goroka, Wabag, Tari, Minj, Mendi | Search telecom aggregation, provincial government server rooms, mining/oil/gas enterprise DR, and Starlink/community gateway style infrastructure. Count only with physical datacenter evidence. |

### 7.2 Compact division query table

Use these city pivots with the universal template:

| Division | City/town pivots |
|---|---|
| Chimbu | Kundiawa, Kerowagi |
| Central | Bautama, Laloki, Sogeri, Port Moresby outskirts |
| East New Britain | Kokopo, Rabaul, Gazelle, Kerevat |
| Eastern Highlands | Goroka, Kainantu |
| Enga | Wabag, Porgera |
| East Sepik | Wewak, Maprik |
| Gulf | Kerema, Kikori |
| Hela | Tari, Komo |
| Jiwaka | Minj, Banz |
| Milne Bay | Alotau, Esa'ala |
| Morobe | Lae, Nadzab, Bulolo, Wau |
| Madang | Madang, Modilon, Bogia |
| Manus | Lorengau, Lombrum |
| National Capital District | Port Moresby, Waigani, Hohola, Gerehu, Boroko |
| New Ireland | Kavieng, Namatanai |
| Northern | Popondetta, Oro Bay |
| Bougainville | Arawa, Buka, Kokopau |
| West Sepik | Vanimo, Aitape |
| Southern Highlands | Mendi, Ialibu |
| West New Britain | Kimbe, Bialla |
| Western Highlands | Mount Hagen, Kagamuga |
| Western | Kiunga, Tabubil, Daru |

---

## 8. Evidence grading and pitfalls

- **A-grade facility existence**: operator-owned page with service/facility description; government/SOE announcement naming a data centre; procurement/contract for data-centre works; contractor project page for delivered facility; official cloud-region list for public cloud geography.
- **B-grade lead**: DCD, Business Advantage PNG, Developing Telecoms, APAC Outlook, NBC/EMTV/FM100/PNG Business News with named operator/project/location; vendor case study with physical delivery details.
- **C-grade lead**: directories, Mapcarta/OSM/Google Maps, social posts, LinkedIn claims, market reports, broad cloud/ICT event text, or a cable map.
- **Common false positives**: call centres, health/resource/training centres, generic `data centre solutions` by IT integrators, telecom exchanges, mobile tower/core upgrades, cable landing stations with no hosting role, government data exchange platforms, and `cloud` services hosted offshore.
- **Status discipline**: `pre-launched`, `MoU`, `partnership`, `roadshow`, or `plans to procure` is not operational facility proof. Mark as announced/planned unless an operator or official source says the facility is commissioned/operational and gives a physical location.
- **Capacity discipline**: PNG sources rarely disclose MW/racks. Do not invent capacity from Tier rating, cable capacity, or telecom network scale. Record capacity as null unless MW/kVA/racks/cabinets are explicit.
- **Province attribution**: Port Moresby is **National Capital District**, not Central Province. Lae is Morobe, Madang town is Madang, Mount Hagen is Western Highlands, Vanimo is West Sepik, Alotau is Milne Bay, Popondetta is Northern, Kavieng is New Ireland, Kokopo/Rabaul are East New Britain, Arawa/Buka are Bougainville.

---

## 9. Recommended PNG discovery pipeline

1. **Seed known operators**: PNG DataCo, Datec, Telikom, CloudSigma, Vodafone/Digitec, Digicel, Online South Pacific, Daltron, APCS, BSP/Huawei government facility.
2. **Confirm public cloud**: check AWS/Azure/GCP/OCI/Alibaba official region pages; record no PNG public region unless official lists change.
3. **Run NCD and Madang deep pass**: operator pages, directories, IXP/PeeringDB/PCH, cable landing sources, government cloud/procurement, local press.
4. **Run regional watch pass**: Lae/Morobe, Mount Hagen/Western Highlands, Vanimo/West Sepik, Bougainville, Kokopo/Rabaul, Alotau, Kavieng, Popondetta using cable/operator/local-press terms.
5. **Verify each lead** against a primary source and classify as commercial colo, sovereign/government cloud, enterprise/private facility, telecom/network facility, micro-edge, cable landing station, or false positive.
6. **Capture uncertainty explicitly**: if a source confirms a service but not a building, record it as cloud/hosting service lead rather than physical datacenter until facility evidence appears.

