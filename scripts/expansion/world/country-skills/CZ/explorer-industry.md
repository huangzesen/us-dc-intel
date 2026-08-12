# CZ Explorer Industry — Czechia Datacenter Enumeration from Operators, Cloud, Associations, HPC, and Press

Date: 2026-08-12. Scope: Czechia (CZ), all 14 manifest divisions: Prague; Central Bohemia; South Bohemia; Plzen; Karlovy Vary; Usti nad Labem; Liberec; Hradec Kralove; Pardubice; Vysocina; South Moravia; Olomouc; Zlin; Moravia-Silesia. This file is the industry-source methodology. Use `explorer-official.md` to confirm permits, EIA, grid, cadastre, telecom-regulator, and procurement evidence.

Reliability grades used here:

- **A**: official operator/cloud/association/HPC/public-institution page or document tied to a named facility, service, or location.
- **B**: established trade press, operator blog/project announcement, investment-agency statement, or reputable vendor case study that still lacks permit or current official-facility confirmation.
- **C**: directory/map/marketplace/database entry, social post, SEO page, or unsourced capacity/location claim.

Industry sources are excellent for discovery but weak for final counts unless they identify an operator, facility, location, and current status. Pair every lead with official evidence from `explorer-official.md` before producing a final inventory.

---

## 1. Market Reality and Counting Posture

Czechia is primarily a Prague-centered colocation and interconnection market, with secondary activity in Brno and Ostrava and scattered enterprise/public facilities elsewhere. As of this review, official AWS, Azure, Google Cloud, and Oracle OCI region/location pages did **not** confirm a Czech public-cloud Region. Do not count cloud sales presence, CDN nodes, exchange ports, or network PoPs as datacenter facilities.

Directory sources such as DataCenterMap, Baxtel, datacenters.com, PeeringDB, Inflect, and market-research summaries are useful C-grade seed lists. They are not authoritative enough for final counts because they often duplicate entries, preserve old brands, infer addresses from PeeringDB, or mix data centers with PoPs.

Recommended facility classes:

```text
commercial_colocation
telecom_colocation
cloud_provider_datacentre_or_local_zone
enterprise_corporate
public_HPC_research
government_or_public_sector
network_pop_or_exchange_only
lead_unconfirmed
```

Only the first six can be counted as facilities, and only with sufficient evidence. `network_pop_or_exchange_only` and `lead_unconfirmed` should remain out of facility totals.

---

## 2. Verified Cloud-Region Status

| Provider | Official URL | Grade | Czechia status from reviewed official pages | Counting instruction |
|---|---|---:|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; `https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/` | A | No Czech AWS Region or Local Zone found on official reviewed pages. | Do not count Czech AWS region/local zone. Treat CloudFront/edge/PoP mentions as network seeds only. |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; `https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies` | A | No Czech public-cloud region found on official reviewed pages. | Do not count an Azure Czech region. |
| Google Cloud | `https://cloud.google.com/about/locations`; `https://datacenters.google/locations` | A | No Czech Google Cloud region or Google-owned datacenter location found on official reviewed pages. | Treat Google/Chomutov speculation as B/C until Google and local official sources confirm it. |
| Oracle OCI | `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`; `https://www.oracle.com/cloud/public-cloud-regions/` | A | No official Prague/Czech OCI public region found in reviewed sources. | Re-check any `eu-prague-1` claim against Oracle docs before counting. |
| OVHcloud | `https://www.ovhcloud.com/en/datacenter/europe/czech-republic/prague/`; `https://www.ovhcloud.com/en/datacenter/` | A | Official Prague datacentre page exists. | Count as an operator/cloud datacentre seed; confirm product type/address with permits or operator documents before capacity claims. |

---

## 3. Operator and Facility Seed List

| Operator / asset | Official or best source | Grade | Location signal | How to use |
|---|---|---:|---|---|
| T-Mobile Czech Republic / DC7 | `https://www.t-mobile.cz`; known DC7 address should be verified against official T-Mobile PDF/page or local records | A when official page/PDF is captured; otherwise B/C for directory details | Prague, K Pérovně / Malešice-Hostivař area | Search `DC7`, `K Pérovně`, `T-Mobile Czech Republic a.s.`, ARES IČO, Prague district notice boards, PREdistribuce. |
| O2 Czech Republic | `https://www.o2.cz/firmy-a-organizace/it-reseni/datove-centrum` | A | Official datacenter service page; directories list Prague/Brno sites but addresses need confirmation | Resolve current O2 facility names/addresses from O2 material, then search Prague and Brno permits. |
| CETIN | `https://www.cetin.cz/products-and-services/collocation` | A | Collocation service in CETIN buildings throughout Czechia | Network collocation seed. Count only site-specific records with address/facility evidence. |
| OVHcloud Prague | `https://www.ovhcloud.com/en/datacenter/europe/czech-republic/prague/` | A | Prague | Official facility seed; search OVH legal entity, Prague address, PREdistribuce, permits. |
| TTC TELEPORT | `https://ttc-teleport.cz/en/` | A | Prague 10-Malešice; official contact page lists Tiskařská 257/10 and helpdesks for DC1/DC2 | Strong Prague operator seed; search `TTC DC1`, `TTC DC2`, `Tiskařská`, `Sazečská`, permits. |
| CE Colo | `https://www.cecolo.com/` | A for operator existence; C/B for address/capacity if from directories | Prague; directory/PeeringDB sources point to Nad Elektrárnou 1428/47 | Verify facility address on CE Colo materials or local records before A-grade facility count. |
| SafeDX | `https://www.safedx.eu/en/` | A | Prague-Vysočany official service page | Search SafeDX legal entity, Prague-Vysočany permits, backup power/IPPC. |
| VSHosting | `https://vshosting.cz/tech` | A | Prague; official technical/datacenter capability page | Use as operator seed; confirm exact site/address via official/company filings or permits. |
| Coolhousing | `https://www.coolhousing.net/en/coolhousing-about-us` | A | Official page says one public data center in Prague/Vinohradská and a private data center in Brno/Cejl | Count Prague if current-service/address confirmed; Brno private site needs status and address confirmation. |
| MasterDC / Master Internet | `https://www.master.cz/blog/u-brna-vznikne-prvni-ai-datove-centrum-masterdc-jej-postavi-do-roka/` | B for Kanice project announcement; A for current operator service pages if captured | Brno; Kanice u Brna AI DC target autumn 2026 | Treat Kanice as planned/lead until permit, EIA, or launch evidence exists. Search Kanice/JMK/EG.D. |
| IT4Innovations / VLQ / EuroHPC | `https://www.it4i.cz/en/infrastructure/vlq-quantum-computer`; `https://www.it4i.cz` | A | Ostrava; VLQ installed/commissioned in 2025, integrated into EuroHPC supercomputer Karolina | Count as `public_HPC_research`, not commercial colo. |
| CESNET / e-INFRA CZ | `https://www.cesnet.cz/en/e-infrastructure`; `https://cloud.e-infra.cz/` | A | National research/e-infrastructure with Prague/Brno/Ostrava ecosystem | Network/research compute context; only count site-specific compute/storage facilities. |
| ASCDC, Czech Data Centre Association | `https://ascdc.cz/` | A for association facts | Czech DC association | Use members/events as operator seeds; membership does not prove a facility. |
| CSDIA | `https://www.csdia.online/` | A/B for association context | Czech-Slovak digital infrastructure association | Use members/news as leads; confirm independently. |
| NIX.CZ | `https://nix.cz/en/about/` | A for interconnection context | Prague IXP | Use member/connected-site list for operator discovery. Peering presence is not a DC count. |
| Datové centrum Monaco / SYNOT | Best reviewed sources were secondary/directory pages; find SYNOT official confirmation before A-grade | B/C until official SYNOT page or permit captured | Zlín / Uherské Hradiště area | Search `SYNOT ICT Services`, `Monaco`, `Zlín`, `Uherské Hradiště`, ARES, municipal permits. |
| Equinix Prague | No official Equinix Prague location page found in reviewed searches; directories mention PR1/PR2 | C until official or local evidence | Prague lead only | Do not count as Equinix facility without official Equinix page, permit, lease/acquisition record, or strong address evidence. |
| Chomutov datacenter / data hub | Czech press/investment lead; official permit/EIA not captured in this review | B lead | Chomutov, Ústecký kraj | Search Chomutov notice board, Ústecký kraj, CENIA, ČEZ Distribuce, CzechInvest. Do not count yet. |

---

## 4. Industry Query Templates

### 4.1 Operator Discovery

```text
"datové centrum" "{city}" "kolokace"
"datacentrum" "{city}" "provozovatel"
"serverhousing" "{city}" "datové centrum"
"colocation" "{city}" "Czech Republic"
"{operator}" "datové centrum" "{city}"
"{operator}" "housing" "Praha" OR "Brno"
"{operator}" "adresa" "datové centrum"
"{operator}" "IČO" "datové centrum"
"{operator}" "TIER III" "Czech"
```

### 4.2 Project / Expansion Discovery

```text
"datacentrum" "postaví" "Česko"
"datové centrum" "otevřel" OR "otevře" "Praha"
"datové centrum" "rozšíření" "Praha" OR "Brno"
"AI datacentrum" "Česko"
"hyperskalní datové centrum" "Česko"
"Chomutov" "datacentrum" OR "datový hub"
"Kanice" "MasterDC" "datové centrum"
"Czechia" "data center" "announcement" 2025 OR 2026
"Czech Republic" "data center campus" "MW"
```

### 4.3 Association / Interconnection

```text
site:ascdc.cz "člen" OR "partner" "datové centrum"
site:csdia.online "členové" OR "datacentra"
site:nix.cz "members" "Prague"
site:nix.cz "connected" "data center"
site:peeringdb.com "Prague" "data center" "Czech"
"NIX.CZ" "datové centrum" "Praha"
```

### 4.4 Press Sources

```text
site:lupa.cz "datacentrum" "Česko"
site:lupa.cz "datové centrum" "Chomutov"
site:idnes.cz "datové centrum" "Česko"
site:forbes.cz "datové centrum" "Česko"
site:e15.cz "datacentrum" "Česko"
site:hn.cz "datové centrum" "T-Mobile" OR "MasterDC"
site:datacenterdynamics.com "Czech" "data center"
site:oenergetice.cz "datacentra" "příkon" OR "ČEPS"
```

Press output should create a lead record with `source_grade=B`, then route to official checks: CENIA, municipal notice board, CUZK, DSO/ČEPS, ARES/justice.cz.

---

## 5. Per-Division Industry Strategy

| Manifest division | Czech region | Industry density | Primary industry leads | First queries | Confirmation route |
|---|---|---:|---|---|---|
| Prague | Hlavní město Praha | High | T-Mobile DC7, TTC TELEPORT, CE Colo, OVHcloud Prague, SafeDX, VSHosting, O2/CETIN, Coolhousing, possible Equinix directory leads | `Praha datové centrum kolokace`, `Prague colocation operator`, `NIX.CZ members Prague`, operator names + districts | Operator official page -> Prague district notices -> PREdistribuce -> CUZK. |
| Central Bohemia | Středočeský kraj | Medium-low | Škoda Auto corporate DC, Prague-periphery enterprise/logistics sites | `Mladá Boleslav datové centrum Škoda`, `Kladno datacentrum`, `Středočeský kraj datové centrum` | Company/press lead -> ARES/justice.cz -> municipal board -> ČEZ Distribuce/CUZK. |
| South Bohemia | Jihočeský kraj | Low | Public-sector, university, municipal/server-room facilities | `České Budějovice datové centrum`, `Tábor serverovna`, `Jihočeský kraj cloud` | NEN/institution pages -> city notice board -> EG.D/CENIA. |
| Plzen | Plzeňský kraj | Low-mid | Regional enterprise colo and industrial IT | `Plzeň datové centrum`, `Plzeň colocation`, `D5 průmyslová zóna datacentrum` | Operator/press -> Plzeň notice board -> ČEZ Distribuce -> CUZK. |
| Karlovy Vary | Karlovarský kraj | Low | Small enterprise/public-sector server rooms | `Karlovy Vary datacentrum`, `Sokolov serverovna`, `Karlovarský kraj datové centrum` | Keep most as leads until municipal/official proof. |
| Usti nad Labem | Ústecký kraj | Medium lead potential | Chomutov datacenter/data-hub lead, industrial brownfields, large power-load speculation | `Chomutov datacentrum`, `datový hub Chomutov`, `Ústecký kraj datové centrum`, `Most datacentrum` | Press/investment lead -> CENIA -> Chomutov/Ústecký notice boards -> ČEZ Distribuce/ČEPS -> CUZK. |
| Liberec | Liberecký kraj | Low-mid | Enterprise/fiber-tech companies, local hosting | `Liberec datové centrum`, `Jablonec serverovna`, `Liberecký kraj datacentrum` | Operator lead -> municipal notices -> ČEZ Distribuce. |
| Hradec Kralove | Královéhradecký kraj | Low | Hospital/university/public IT, enterprise server rooms | `Hradec Králové datové centrum`, `Královéhradecký kraj serverovna` | Public procurement/institution -> municipal/kraj board -> ČEZ Distribuce. |
| Pardubice | Pardubický kraj | Low-mid | Electronics/industrial park enterprise facilities | `Pardubice datacentrum`, `Chrudim serverovna`, `Pardubický kraj cloud` | Press/company -> municipal board -> ČEZ Distribuce/CENIA. |
| Vysocina | Kraj Vysočina | Low | Public-sector, energy-adjacent speculation, Jihlava enterprise IT | `Jihlava datové centrum`, `Vysočina datacentrum`, `Dukovany datové centrum` | Treat energy context carefully; require operator/permit/DSO proof. |
| South Moravia | Jihomoravský kraj | High outside Prague | MasterDC Brno and Kanice AI DC lead, Coolhousing Brno private DC, O2 Brno, CESNET/CERIT/e-INFRA | `Brno datové centrum kolokace`, `MasterDC Kanice AI datacentrum`, `Brno Cejl datové centrum`, `CERIT scientific cloud` | Operator/institution page -> Brno/Kanice notices -> JMK/CENIA -> EG.D/CUZK. |
| Olomouc | Olomoucký kraj | Low-mid | Local hosting/public-sector facilities | `Olomouc datové centrum`, `Prostějov datacentrum`, `Olomoucký kraj serverovna` | Operator/NEN -> municipal board -> ČEZ Distribuce. |
| Zlin | Zlínský kraj | Medium lead potential | Datové centrum Monaco / SYNOT, Uherské Hradiště ICT | `Zlín datové centrum Monaco`, `SYNOT ICT Services datové centrum`, `Uherské Hradiště datacentrum` | Find SYNOT official/current page -> ARES -> Zlín/UH notices -> DSO/CUZK. |
| Moravia-Silesia | Moravskoslezský kraj | Medium-high public/HPC | IT4Innovations, VLQ quantum computer, Karolina/Barbora, Czech AI Factory, Ostrava industrial brownfields | `Ostrava IT4Innovations LUMI-Q`, `Czech AI Factory Ostrava`, `Ostrava datové centrum kolokace` | Official IT4I/EuroHPC pages -> VŠB/Ostrava/MSK records -> ČEZ Distribuce/CENIA. |

---

## 6. HPC, Research, and Government Cloud

- **IT4Innovations (Ostrava)**: official source `https://www.it4i.cz`. The VLQ page at `https://www.it4i.cz/en/infrastructure/vlq-quantum-computer` states the system is integrated into EuroHPC supercomputer Karolina and installation/commissioning occurred in 2025. Count as `public_HPC_research`.
- **CESNET / e-INFRA CZ**: `https://www.cesnet.cz/en/e-infrastructure` and `https://cloud.e-infra.cz/` confirm national research/e-infrastructure context. Use for network/storage/compute discovery, but require site-level evidence for facility counts.
- **CERIT Scientific Cloud**: use as a Brno/South Moravia research-compute seed through e-INFRA CZ. Count only with site-level official evidence.
- **Government/sovereign cloud**: search NEN and ministry pages for `vládní cloud`, `eGovernment cloud`, `datové centrum`, `serverovna`, and `kolokace`. Government cloud procurements are A-grade for procurement facts, but not necessarily for physical facility location unless the tender identifies it.

---

## 7. Trade Press and Directory Use

B-grade lead sources to search: Lupa.cz, iDNES.cz/ČTK, Hospodářské noviny (`hn.cz`), Forbes.cz, Euro.cz, E15, CzechCrunch, oEnergetice.cz, Computerworld/Computertrends, and DataCenterDynamics.

C-grade seed sources: DataCenterMap, Baxtel, datacenters.com, Data Center Platform, PeeringDB, Inflect, marketplace/SEO pages, generic market reports, and social posts.

Rules:

- Use B/C sources to discover names, addresses, operators, and dates.
- Never use C-grade capacity claims as final capacity without operator/permit/grid confirmation.
- Directory entries for old brands such as GTS/Telefonica must be reconciled to current legal/operator entities through ARES/justice.cz and operator pages.
- If a press story says `will build`, `plans`, `is considering`, or `could be`, status is `lead` or `planned`, not operational.
- A dated target such as `autumn 2026` remains a target until a launch/current-service source confirms operation.

---

## 8. Open Items to Track Honestly

- Equinix Prague: keep as C-grade lead unless official Equinix or local records confirm facility identity.
- OVHcloud Prague: official page confirms Prague datacentre presence; still collect exact operational detail, product class, and address if possible.
- T-Mobile DC7: verify and archive the official brochure/page, then use Prague permit/PREdistribuce pivots for expansion history.
- O2 Czech Republic: official services page exists; resolve current facility names/addresses from O2 material rather than directory-only lists.
- MasterDC Kanice: official blog announces a planned AI datacenter for autumn 2026; confirm permit/EIA/EG.D before marking under construction or operational.
- Chomutov data hub: B-grade lead; needs CENIA, Chomutov/Ústecký notices, CzechInvest/municipal, and grid confirmation.
- Datové centrum Monaco/SYNOT: promising Zlín lead; needs official SYNOT/current service or permit confirmation.
- Public/HPC inventory: keep IT4Innovations, CESNET, CERIT, and government DCs separate from commercial colocation.
