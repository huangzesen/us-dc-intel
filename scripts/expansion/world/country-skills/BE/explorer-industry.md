# BE Explorer Industry - Belgium Datacenter Enumeration via Trade Press, Associations, Operators, IXPs, Cables, Directories

Date: 2026-08-12. Scope: Belgium (BE). Subnational model: **region**. Required division coverage: **Brussels-Capital Region**, **Flanders**, **Wallonia**. Focus: industry and operator discovery methodology for datacenter facilities and projects. Use this file to find leads; use `explorer-official.md` to validate permits, grid, legal entities, and regional assignment.

Reliability grades:

| Grade | Meaning |
|---|---|
| A | Operator-owned, cloud-provider, IXP-operator, certification body, or other primary source for the exact fact. |
| B | Reliable trade press, association report, contractor page, or strong professional source. |
| C | Directory, broker, market report, or weak secondary source; seed only. |
| U | Unverified; do not count without stronger evidence. |

---

## 0. Belgium Industry Frame

- Belgium is a small but dense near-core European datacenter market. The commercial colocation market is concentrated around the Brussels metro and airport axis, but the official regional split matters: many "Brussels" facilities are actually in Flemish Brabant and therefore **Flanders**.
- There is no single authoritative industry list. Start with BDIA, operator location pages, IXP host pages, and DCD/Belgian press, then reconcile against official permits and grid evidence.
- Search in Dutch, French, and English. Use municipality names aggressively: Zaventem, Diegem, Machelen, Evere, Neder-Over-Heembeek, Asse, Zellik, Aalst, Huizingen, Antwerp/Antwerpen, Ghent/Gent, Hasselt, Mechelen, Oostkamp, Bruges/Brugge, Mouscron/Moeskroen, Saint-Ghislain, Farciennes, Gembloux, Charleroi, Mons, Liege/Luik, Namur/Namen.
- Main hyperscale anchors: Google St. Ghislain and Farciennes in Wallonia; Microsoft Azure Belgium Central at region level with undisclosed physical sites. Do not infer Microsoft building locations from the region name.
- Major ownership change: Proximus sold four datacenters to Datacenter United, announced in October 2024 and closed in Q1 2025 per DCD. Legacy Proximus listings may now be DCU-operated.

---

## 1. Industry Source Backbone

### 1.1 Association and Market Anchors

| Source | URL | Use | Grade |
|---|---|---|---|
| Belgian Digital Infrastructure Association (BDIA) | `https://bdia.be/` | National association, reports, database, map, policy statements, industry guides. | B+ |
| BDIA State of Belgian Data Centres 2025 | `https://bdia.be/insights/the-state-of-belgian-data-centres-2025/` | Market framing; BDIA says the sector is growing and grid connections remain a critical challenge. | B+ |
| BDIA guide/database/map | `https://bdia.be/insights/`, `https://bdia.be/database/`, `https://bdia.be/map/` | Facility and member lead generation; validate facilities elsewhere. | B/C |
| Agoria | `https://www.agoria.be/` | Technology-sector policy and member context. | B |
| Digital Wallonia / Agence du Numerique | `https://www.digitalwallonia.be/`, `https://www.adn.be/` | Wallonia digital policy and investment context. | B/A depending page |

### 1.2 Belgian and International Trade Press

| Source | URL/query | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `https://www.datacenterdynamics.com/` | Hyperscaler and operator announcements, acquisitions, status changes. | B |
| Brussels Times | `https://www.brusselstimes.com/` | English Belgian news; useful for Google/Farciennes and policy coverage. | B |
| L'Echo / De Tijd | `https://www.lecho.be/`, `https://www.tijd.be/` | Business and financing coverage; project finance and land/energy issues. | B |
| DataNews / Le Vif | `https://datanews.levif.be/`, `https://www.levif.be/` | Belgian IT/business coverage. | B |
| ITdaily | `https://itdaily.com/` | Belgian datacenter and grid coverage. | B |
| Computable Belgium | `https://www.computable.be/` | Dutch-language cloud/datacenter coverage. | B |
| TechPulse | `https://techpulse.be/` | Belgian IT business coverage. | B |
| RTBF / VRT / Belga | `https://www.rtbf.be/`, `https://www.vrt.be/`, `https://www.belganewsagency.eu/` | Local and wire reporting for public inquiries, investment, regional politics. | B |
| Capacity, Telecompaper, Mobile Europe, Techzine | respective sites | Secondary trade leads; validate from operator/official records. | B/C |

Trade press can establish announcement/construction status when corroborated, but permit status should come from official regional records whenever possible.

---

## 2. Operator and Developer Pivots

Operator pages are A for marketed existence/address/specs they publish. They are not A for permit status unless they link the permit decision.

| Operator/developer | URL | Division pivots | Current evidence notes | Grade |
|---|---|---|---|---|
| Microsoft | `https://datacenters.microsoft.com/gl_regions/belgiumcentral/`; launch PR `https://pulse.microsoft.com/en/transform-2/na/fa2-microsoft-opens-its-first-cloud-region-in-belgium-accelerating-innovation-and-economic-growth/` | Region-level Belgium/Brussels launch; physical sites undisclosed | Azure Belgium Central opened 2025-11-18. Treat as cloud region, not three countable buildings unless other evidence identifies addresses. | A/U |
| Google | `https://datacenters.google/locations/belgium/`; Google blog `https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-infrastructure-investment-belgium/` | Wallonia: Saint-Ghislain, Farciennes | Official St. Ghislain location; additional EUR 5B Belgium AI/cloud infrastructure investment announced in 2025; Farciennes construction covered by DCD/Brussels Times. | A/B |
| Datacenter United | `https://datacenterunited.com/en/our-datacenters/` | Brussels and Flanders; possible Wallonia lead at Mouscron/Moeskroen | Operator states 14 datacenters across 12 Belgian locations. Pages exist for DC Evere, Antwerp/Flanders, Machelen, Ghent, Mechelen, Hasselt, Oostkamp-Bruges, Moeskroen/Mouscron and others. | A |
| LCL Data Centers | `https://www.lcl.be/`; FAQ `https://www.lcl.be/en/q-a-frequently-asked-questions/are-all-lcl-data-centers-located-in-belgium/` | Flanders: Diegem, Aalst, Huizingen, Antwerp. Wallonia: Gembloux. | LCL states all five datacenters are in Belgium: Brussels-North in Diegem, Brussels-West in Aalst, Brussels-South in Huizingen, Antwerp, Wallonia One in Gembloux. | A |
| Digital Realty | `https://www.digitalrealty.com/data-centers/emea/brussels` | Flanders: Zaventem | Current operator page lists three Brussels metro sites: BRU1 at Wezembeekstraat 2, Zaventem; BRU3 and BRU4 at Mercuriusstraat 27, Zaventem. | A |
| KevlinX | `https://www.kevlinx.com/`; `https://www.kevlinx.com/location/brussels` | Brussels-Capital: northern Brussels/Neder-Over-Heembeek area | Operator page confirms 32 MW+ BRU01; BESIX reports handover in Dec 2025; DCD reports ready-for-service. | A/B |
| Penta Infra | `https://penta-infra.com/data-centers/`; `https://penta-infra.com/data-centers/brussels/` | Flanders lead: Asse/Zellik/Brussels periphery | Operator page confirms Brussels-market BRU01 and certifications; pin the exact address from operator or official sources before assigning. | A for existence; U for exact municipality unless address confirmed |
| Combell | `https://www.combell.com/en/colocation` | Flanders/Ghent lead | Markets colocation; facility address and permit status require independent corroboration. | A/U |
| Cegeka | `https://www.cegeka.com/` | Flanders/Hasselt lead | Enterprise/cloud provider; datacenter facility details need operator or permit page confirmation. | A/U |
| Orange Belgium | `https://www.orange.be/` | Flanders/Antwerp-Hoboken lead | Hoboken datacenter appears in trade/directory sources; require current operator-page or permit evidence before final count. | B/C |
| Proximus | `https://www.proximus.be/` | Legacy sites in Brussels/Flanders | Four datacenters sold to DCU; use as historical lead, not current owner unless confirmed. | B |
| Equinix | `https://www.equinix.com/data-centers/europe-colocation` | Brussels metro lead | Belgium/Brussels BR-series could not be confirmed as current operator pages in this review; use only as a lead unless PeeringDB/operator proof is found. | U |
| Etix Everywhere | `https://www.etixeverywhere.com/data-centers-in-liege/`; `https://www.etixeverywhere.com/our-data-centers/` | Wallonia: Liege/Villers-le-Bouillet lead | Etix official pages confirm a Belgium/Liege datacenter presence; directories place Belgium DC 1 at Rue de la Science 3, 4530 Villers-le-Bouillet. Use official page for existence and directory/official records for exact address. | A/C |
| DC Alliance | no Belgium-specific official URL confirmed | Legacy/ambiguous Liege-Brussels lead | Searches point to unrelated APAC/Australian DC Alliance entities; do not use this as a Belgium facility lead without new evidence. | U |

---

## 3. IXPs, Peering, and Network-Density Sources

| Source | URL | Use | Grade |
|---|---|---|---|
| BNIX | `https://www.bnix.net/`; PoPs `https://www.bnix.net/en/partners/pops` | Primary Belgian IXP. BNIX says it is deployed across five sites in and around Brussels. | A |
| BELNET BNIX anniversary | `https://www.belnet.be/en/about/press-releases/milestone-belgian-internet-national-internet-exchange-point-bnix-celebrates` | Confirms BNIX was founded in 1995 by Belnet and remains a key Belgian internet exchange. | A/B |
| BelgiumIX | `https://belgiumix.net/` | Active Belgian internet exchange lead; map member/facility data separately. | A/B |
| AMS-IX | `https://www.ams-ix.net/ams/where-to-connect` | Official where-to-connect page includes Brussels/Belgium remote/direct options; use for PoP leads only. | A/B |
| DE-CIX | `https://www.de-cix.net/en/services/where-to-connect` | Global where-to-connect surface; search Belgium/Brussels in current UI. | A/B |
| NL-ix | `https://www.nl-ix.net/` and PeeringDB | Often present in Digital Realty/Brussels ecosystem; confirm host facility. | B/U |
| PeeringDB | `https://www.peeringdb.com/` | Facility and exchange membership. Example: Digital Realty BRU1 fac/68 lists BNIX, BelgiumIX, Global Peer Exchange, NL-ix. User-maintained, so use as B/U corroboration. | B/U |

IXP query templates:

```text
site:bnix.net Brussels PoP datacenter
site:belgiumix.net Brussels datacenter
site:ams-ix.net Brussels Belgium "where to connect"
site:de-cix.net Brussels Belgium "where to connect"
site:peeringdb.com/fac Belgium Brussels Zaventem BNIX
"Digital Realty BRU1" BNIX PeeringDB
```

---

## 4. Directories and Aggregators

Directories are useful for seed lists and aliases, but they frequently mis-assign Brussels-market facilities to Brussels-Capital when the address is in Flanders.

| Source | URL | Use | Grade |
|---|---|---|---|
| DatacenterMap Belgium | `https://www.datacentermap.com/belgium/`; Brussels page `https://www.datacentermap.com/belgium/brussels/` | Facility/address/operator seeds, but validate every address. | C |
| Baxtel | `https://baxtel.com/data-center/belgium` | Facility/spec/news seeds. | C |
| Datacenters.com | `https://www.datacenters.com/locations/belgium` | Provider/facility broker listings. | C |
| DataCenterPlatform | `https://datacenterplatform.com/` | Facility profiles and BDIA membership hints. | C |
| DataCenterCatalog | `https://datacentercatalog.com/belgium` | Spec/certification leads. | C |
| Cloudscene, Ocolo, Upstack | respective sites | Broker/marketplace leads. | C |
| Arizton, ResearchAndMarkets, Mordor-style market reports | respective report pages | Market size and forecast context only. | C |

Never use a directory count as a facility census without deduplication and operator/official validation.

---

## 5. Per-Division Industry Enumeration

### 5.1 Brussels-Capital Region

Expected industry profile: dense interconnection market, KevlinX BRU01, Datacenter United DC Evere, possible legacy carrier/government sites, BNIX/BelgiumIX/other IXP PoPs in host facilities. The biggest trap is overcounting Flemish Brabant as Brussels.

Priority pivots:

```text
KevlinX BRU01
Datacenter United DC Evere
BNIX Brussels PoP
BelgiumIX Brussels
Colt Brussels / Lumen / Level3 legacy
BELNET datacenter Brussels
Smals datacenter Brussels
CIRB OR paradigm.brussels datacenter
"Neder-Over-Heembeek" datacenter
"Evere" datacenter
```

Known industry-side seeds:

| Facility/project | Municipality | Evidence | Grade |
|---|---|---|---|
| KevlinX BRU01 | Brussels City / Neder-Over-Heembeek | KevlinX operator page; BESIX construction handover; DCD ready-for-service. | A/B |
| Datacenter United DC Evere | Evere | DCU operator page lead; validate address/specs and permits. | A/U |
| BNIX/BelgiumIX/other IXP PoPs | Brussels and periphery | IXP pages and PeeringDB; count host facilities, not the exchange switch itself. | A/B/U |
| Government/parastatal rooms | Brussels | BELNET/BOSA/Smals/CIRB-type leads; facility details often non-public. | U at facility level |

Realistic result: Brussels-Capital should have fewer facilities than the generic "Brussels metro" directory count once Zaventem/Diegem/Aalst/Huizingen/Asse are moved to Flanders.

### 5.2 Flanders

Expected industry profile: strongest commercial colo count, including Brussels Airport/periphery, Antwerp, Ghent, Aalst, Hasselt, Mechelen, Oostkamp/Bruges, and possibly Moeskroen/Mouscron. Grid constraints and flexible connections should be tracked as status metadata.

Priority pivots:

```text
Digital Realty BRU1 BRU3 BRU4 Zaventem
Datacenter United Antwerp Machelen Ghent Mechelen Hasselt Oostkamp Moeskroen
LCL Diegem Aalst Huizingen Antwerp
Penta Infra BRU01 Asse Zellik
Combell colocation Gent
Cegeka datacenter Hasselt
Orange Belgium Hoboken datacenter
Telenet datacenter Mechelen
Citymesh datacenter Bruges
Edpnet datacenter Zaventem
```

Known industry-side seeds:

| Facility/project | Municipality | Evidence | Grade |
|---|---|---|---|
| Digital Realty BRU1 | Zaventem | Operator page lists address and space. | A |
| Digital Realty BRU3 | Zaventem | Operator page lists address and space. | A |
| Digital Realty BRU4 | Zaventem | Operator page lists address and space. | A |
| LCL Brussels-North | Diegem/Machelen | LCL FAQ/contact pages. | A |
| LCL Brussels-West | Aalst | LCL FAQ/news; LCL Tier III CoCF news for Aalst. | A |
| LCL Brussels-South | Huizingen | LCL FAQ/news. | A |
| LCL Antwerp | Antwerp | LCL FAQ/news; PeeringDB/directory can refine address. | A/B |
| Datacenter United Antwerp/Flanders | Antwerp | Operator page; Uptime Institute client story confirms DCU Tier IV story. | A |
| Datacenter United Machelen/Ghent/Mechelen/Hasselt/Oostkamp-Bruges | Respective Flemish municipalities | Operator pages surfaced; confirm each address and permit. | A/U |
| Datacenter United Moeskroen/Mouscron | Mouscron, Walloon border city in Hainaut if address is 7700 Mouscron | Operator page surfaced as coming soon; classify as Wallonia if address is 7700 Mouscron, not Flanders. | A/U |
| Penta Infra BRU01 | Asse/Zellik lead | Operator page confirms Brussels-market facility; exact municipality/address must be pinned. | A/U |
| Combell | Ghent lead | Operator markets colocation. | A/U |
| Cegeka | Hasselt lead | Operator/company lead; facility-level proof required. | A/U |
| Orange Belgium Hoboken | Antwerp/Hoboken | Trade/directory lead for 2019 opening; confirm current status. | B/C |

Correction to watch: Mouscron/Moeskroen is in Wallonia (Hainaut), even if it appears in a Flanders-heavy DCU list.

### 5.3 Wallonia

Expected industry profile: lower facility count but high hyperscale weight. Google dominates; LCL Wallonia One is the clean commercial-colo anchor; other leads need caution.

Priority pivots:

```text
Google Saint-Ghislain data center
Google Farciennes data center permis unique
Google Belgium EUR 5 billion AI infrastructure
LCL Wallonia One Gembloux
Datacenter United Moeskroen Mouscron
Etix Liege Belgium DC 1 Villers-le-Bouillet
SPW datacenter Wallonie
"centre de données" "Wallonie" "permis unique"
```

Known industry-side seeds:

| Facility/project | Municipality | Evidence | Grade |
|---|---|---|---|
| Google St. Ghislain | Saint-Ghislain | Google official location page; Google Cloud locations. | A |
| Google Farciennes | Farciennes area | DCD and Brussels Times report construction and EUR 1B investment; official Walloon permit documents needed for final permit status. | B |
| Google Belgium expansion | Saint-Ghislain and broader Belgium | Google official blog announces EUR 5B over two years to expand cloud/AI infrastructure, including Saint-Ghislain campus expansion. | A |
| LCL Wallonia One | Gembloux | LCL acquisition/news page confirms Gembloux facility. | A |
| Datacenter United Moeskroen/Mouscron | Mouscron | DCU page surfaced; treat as Wallonia if address is 7700 Mouscron and confirm status. | A/U |
| Etix Belgium/Liege datacenter | Liege market; Villers-le-Bouillet address lead | Etix official pages confirm Belgium/Liege presence; directory sources place Belgium DC 1 at Rue de la Science 3, 4530 Villers-le-Bouillet. | A/C |
| DC Alliance / Liege-Brussels legacy leads | Unresolved | Searches point to unrelated APAC/Australian entities; ignore unless new Belgium-specific evidence appears. | U |

---

## 6. Search Templates

### Broad Discovery

```text
("datacenter" OR "datacentrum" OR "datacentra") (België OR Vlaanderen OR Brussel OR Antwerpen OR Gent OR Aalst OR Hasselt OR Zaventem OR Diegem OR Machelen) (MW OR m² OR uitbreiding OR nieuw)
("datacenter" OR "centre de données") (Belgique OR Wallonie OR Bruxelles OR Charleroi OR Mons OR Namur OR Liège OR Farciennes OR "Saint-Ghislain") (MW OR m² OR extension OR nouveau OR permis)
"Belgium" "data center" (operator OR city) (MW OR expansion OR acquisition OR permit OR construction)
site:datacenterdynamics.com Belgium data center
site:brusselstimes.com "data center" Belgium Google Microsoft
site:bdia.be datacenter Belgium operator
```

### Operator/Status Confirmation

```text
"{operator}" "{facility}" "Belgium" datacenter
"{operator}" "{address}" datacenter
"{operator}" "{municipality}" colocation OR datacenter
"{facility}" "ready for service" OR operational OR "in gebruik" OR "en service"
"{facility}" "construction" OR "start bouw" OR "début des travaux"
"{operator}" "Tier III" OR "Tier IV" "Belgium"
```

### Permit/Grid Bridge Queries

```text
"{operator}" "{municipality}" omgevingsvergunning OR "permis unique"
"{operator}" "{municipality}" "openbaar onderzoek" OR "enquête publique"
"{operator}" "{municipality}" Elia OR Fluvius OR Sibelga OR ORES OR RESA
"datacenter" "netcongestie" België OR Vlaanderen
"centre de données" "raccordement" Wallonie
```

### Ownership/Dedup Queries

```text
"Proximus" "Datacenter United" datacenters sale leaseback
"Interxion" "Digital Realty" Brussels BRU1 BRU3 BRU4
"LCL Brussels-West" Aalst
"LCL Brussels-South" Huizingen
"BRU01" Zaventem OR Asse OR Brussels datacenter
```

---

## 7. Subsea Cable and Edge Infrastructure

Belgium has North Sea coastal telecom relevance, with Ostend/Oostende and Zeebrugge often appearing in cable-landing searches. Treat cable landings as adjacency signals, not datacenter evidence.

Authoritative or useful sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| TeleGeography Submarine Cable Map | `https://www.submarinecablemap.com/` | Current cable systems and landing stations. | B |
| Operator/cable-system pages | per cable | Primary for specific landing station facts. | A/B |
| Fiber Atlantic and similar summaries | `https://www.fiberatlantic.com/` | Lead material only. | C |

Queries:

```text
Oostende OR Ostend "submarine cable" "landing station"
Zeebrugge "submarine cable" "landing station"
Belgium "subsea cable" datacenter
site:submarinecablemap.com Belgium Ostend Zeebrugge
```

Do not count cable landing stations as datacenters unless a separate facility source identifies a datacenter/colo building at that location.

---

## 8. Final Evidence Rules

- Facility existence: prefer operator page, official permit, cloud-provider location page, or IXP host proof.
- Status: operational needs operator/official/service evidence; construction needs operator/contractor/reliable press plus no contrary permit evidence.
- Division: assign by municipality and Belgian Region, not by metro label.
- Capacity: use MW/MVA/m2 only when the source explicitly states the metric. Distinguish IT load, connection capacity, campus capacity, building shell area, and white space.
- Hyperscale: count St. Ghislain and Farciennes where evidence identifies campus municipalities. Do not count Azure Belgium Central's undisclosed buildings.
- DCU/Proximus: avoid double-counting legacy Proximus sites after the DCU acquisition.
- Directories: use for discovery and aliases only; never final status or division without stronger corroboration.
- Uptime: certification proves a certification claim for the named site, not operational status or current ownership unless the entry says so.

---

## 9. Re-Check Cadence

- **Every run**: cloud region pages for Azure, Google, AWS, Oracle, IBM; operator pages for DCU, LCL, Digital Realty, KevlinX, Penta.
- **Monthly**: DCD, Brussels Times, Belgian trade press, public procurement, and grid/congestion news.
- **Quarterly**: PeeringDB, BNIX/BelgiumIX/AMS-IX/DE-CIX/NL-ix host locations, DatacenterMap/Baxtel/datacenters.com, BDIA map/database.
- **Annual**: BDIA reports/guides, Uptime Institute certified-facility list, market reports for context only.
- **Event-triggered**: Microsoft/Google/AWS/Oracle announcements, new Elia/Fluvius/Sibelga/ORES/RESA connection policy, regional public inquiries, acquisitions, or ownership changes.
