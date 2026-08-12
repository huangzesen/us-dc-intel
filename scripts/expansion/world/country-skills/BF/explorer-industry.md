# BF Explorer Industry - Burkina Faso Datacenter Discovery

Date verified: 2026-08-12. Scope: industry media, operator pages, vendor pages, directories, IX/peering records, and local press for Burkina Faso datacenter enumeration.

Boundary model: use the requested legacy **13 administrative regions** for coverage, but include post-2025 names in searches. The Presidency announced on 2025-07-02 a move to **17 regions / 47 provinces** and endogenous region names: https://www.presidencedufaso.bf/conseil-des-ministres-du-2-juillet-2025/. Current records may say Kadiogo for Centre, Guiriko for Hauts-Bassins, Bankui/Sourou for former Boucle du Mouhoun, Goulmou/Sirba/Tapoa for former Est, and Liptako/Soum for former Sahel.

Reliability grades:
- **A**: official operator facility page, government/ministry/ANPTIC/ARCEP/ANEVE/ARSE/SONABEL/ARMP record, PeeringDB/PCH network record, official cloud-provider region page, BRVM/issuer filing.
- **B**: strong trade or local press: Data Center Dynamics, Developing Telecoms, Ecofin Agency, AIB, Sidwaya, leFaso.net, Burkina24, Wakat Sera, Telecom Review Africa, TechAfrica News, WeAreTech, credible vendor case study.
- **C**: aggregator directories, marketplace pages, social posts, paid market reports, old MoUs, claims that lack address/status/power/operator evidence.

## 1. Market Reality

- Burkina Faso's datacenter market is small and Ouagadougou-centric. Confirmed or high-confidence facility evidence clusters in **Centre / Ouagadougou / Kadiogo**.
- The core 2026 demand signal is the state data-sovereignty program: two government modular datacenters inaugurated on 2026-01-23, a national digital-infrastructure supervision/NOC building targeted for October 2026, and continuing government-cloud expansion.
- Burkina Faso is landlocked. There are no subsea cable landings in-country; international routes depend on terrestrial fibre to coastal systems through Cote d'Ivoire, Ghana, Togo and Benin. Treat "low-latency hyperscale" claims skeptically unless backed by BFIX/PeeringDB, operator backbone or measured latency evidence.
- Electricity is a major constraint. Any industry claim should be reconciled with SONABEL/ARSE, generator, UPS, solar/PPA or EIA evidence.
- No AWS, Azure, Google Cloud or Oracle public cloud region in Burkina Faso was found on official region lists checked on 2026-08-12.

## 2. Industry Source Triage

| Source | URL / route | What it is good for | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ ; search `site:datacenterdynamics.com Burkina Faso data center` | Government mini-DCs, NOC, Essor/Kaia waste-to-energy proposal, Orange solar-at-DC item, tower-program context. | B; upgrade only when it links to/quotes official docs. |
| Ecofin Agency | https://www.ecofinagency.com/ ; search Burkina digital infrastructure | NOC/supervision center, telecom towers, public digital projects. | B. |
| Developing Telecoms | https://developingtelecoms.com/ | Telecom and energy-for-DC corroboration; useful for Essor/Kaia and tower projects. | B. |
| leFaso.net | https://lefaso.net/ | Local government-adjacent reporting; useful for French terms and launch events. | B; sometimes A-adjacent when reproducing official communications. |
| AIB | https://www.aib.media/ | Official news-agency style notices and regional reports. | B. |
| Sidwaya | https://www.sidwaya.info/ | State-affiliated daily; useful for institutional reforms and official events. | B. |
| Burkina24 | https://burkina24.com/ | Local government and ICT reporting; also covered the 2025 administrative reorganization. | B/C depending on detail. |
| Wakat Sera | https://www.wakatsera.com/ | Local reporting on official speeches and inaugurations. | B. |
| TechAfrica News | https://techafricanews.com/ | Short English summaries of ministry projects, tower and NOC items. | B/C; verify against official pages. |
| WeAreTech Africa | https://www.wearetech.africa/ | Regional tech coverage; useful for project and budget signals. | B/C. |
| Telecom Review Africa | https://www.telecomreviewafrica.com/ | Secondary details on 2026 government mini-DC capacities. | B/C. |
| DataCenterPlatform | https://datacenterplatform.com/countries/burkina-faso/ | Discovery only: lists MDENP, Virtix, Alink, IPSyS and claimed counts. | C. Never final authority. |
| DataCenterMap | https://www.datacentermap.com/burkina-faso/ | Discovery only; current listing found one Ouagadougou market/facility. | C. |
| Inflect | https://inflect.com/datacenters/emea/burkina-faso | Discovery only; IPSyS Ouagadougou lead. | C. |
| PeeringDB | https://www.peeringdb.com/ix/2729 ; https://www.peeringdb.com/org/14212 | BFIX Ouagadougou, local facilities, peers and ASNs. | B/A for interconnection facts; not commercial-facility proof by itself. |
| PCH / Internet Society Pulse | PCH IX details; ISOC Pulse IXP tracker | BFIX corroboration, capacity/membership context. | B for IXP context. |

Trade-press query block:

```text
site:datacenterdynamics.com/en/news/ "Burkina Faso" ("data center" OR "data centre" OR datacenter)
site:ecofinagency.com "Burkina Faso" ("data center" OR "digital infrastructure" OR "centre de supervision" OR towers)
site:developingtelecoms.com "Burkina Faso" ("data centre" OR "data center" OR towers OR "waste-to-energy")
site:lefaso.net Burkina (datacenter OR "centre de données" OR "cloud gouvernemental" OR "souveraineté numérique")
site:aib.media Burkina (datacenter OR "centre de données" OR "infrastructures numériques")
site:burkina24.com Burkina (datacenter OR "centre de données" OR "découpage administratif")
site:wakatsera.com Burkina (datacenter OR "centre de données" OR "cloud gouvernemental")
site:wearetech.africa Burkina Faso ("data center" OR "centre de données" OR "white zones")
"Burkina Faso" ("data center" OR "centre de données" OR datacenter) (MW OR racks OR FCFA OR colocation)
```

## 3. Operator and Project Seeds

| Seed | URLs | Location signal | Grade | Industry handling |
|---|---|---|---|---|
| Government Cloud modular datacenters | MTDPCE progress page https://www.mdenp.gov.bf/details?cHash=6c732178fee5fa9a762ad626e10a7e3f&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=1015 ; DCD https://www.datacenterdynamics.com/en/news/govt-of-burkina-faso-launches-two-mini-data-centers-to-support-data-sovereignty/ ; Connecting Africa https://www.connectingafrica.com/data-centers/burkina-faso-launches-two-mini-data-centers | Ouagadougou; two sites, exact addresses not public in reviewed sources | A for MTDPCE project existence; B for press capacities/inauguration unless live ANPTIC article opens | Operational/inaugurated government infrastructure. Capacity commonly reported as 3 PB storage, 105.6 TB RAM, 28,800 CPU cores, 7,000+ VMs; verify official page text before writing capacity as A. |
| ANPTIC / legacy G-Cloud / education datacenter | ANPTIC site https://anptic.gov.bf/ ; old G-Cloud https://www.mdenp.gov.bf/details?cHash=4c4f77e8032d813f9cc1a5387eb98c2d&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=124 ; education DC query `site:anptic.gov.bf "DATACENTER DE L'EDUCATION"` | Mostly Ouagadougou and government/university estate | A for live agency pages; B/C for indexed article snippets until opened | Important dedup area. Separate only when site/function/status are distinct. |
| Virtix Data Center / VTS | Official https://virtix.bf/ ; PeeringDB BFIX https://www.peeringdb.com/ix/2729 ; DataCenterPlatform https://datacenterplatform.com/data-centers/virtual-technologies-and-solutions-sa/ ; DataCenterMap https://www.datacentermap.com/burkina-faso/ouagadougou/virtix-data-center/ | Palais des Sports, Ouaga 2000, Ouagadougou | A for official location/services; B for PeeringDB; C for directory capacity | Best commercial colo seed. Treat "Tier 3/hyperscale" as self-claim unless Uptime certification is found. Directory figures such as 1,200 sqm/3 MW need independent confirmation. |
| IKA Cloud / IKA Solution | IKA Cloud https://www.ikacloud.bf/princing-package.php?currency=1 ; IKA Solution https://ikasolution.bf/ | Avenue de la Dignite, Cissin/Secteur 26, Ouagadougou | A for advertised services and address; B/C for launch media | New local hosting/colo platform. Claims "premier" should be recorded as marketing because Virtix is older. Verify physical DC vs reseller/platform before final commercial record. |
| Alink Telecom | Reported official domain, HTTP only in liveness check: http://www.alinktelecom.net ; DataCenterPlatform https://datacenterplatform.com/data-centers/alink-telecom/ | Ouagadougou in directory; exact facility not verified | B/C for company domain/directory; C for directory DC count | Lead only until operator page, ARCEP, BFIX, permit, customer or power evidence ties it to a live BF facility. |
| IPSyS TELECOM | Official https://ipsys-bf.com/ ; Inflect https://inflect.com/datacenters/emea/burkina-faso | Avenue Kwame Nkrumah, Ouagadougou in directory | A for company page if facility/services shown; C for directory | Verify whether the address is the actual facility or office. Search `IPSyS TELECOM DATACENTER`, `Patrick Pons`, `Avenue Kwame Nkrumah`. |
| Orange Burkina Faso | Official https://www.orange.bf/ ; ARCEP register https://www.arcep.bf/repertoire/ ; DCD solar item https://www.datacenterdynamics.com/en/news/orange-deploying-solar-panels-at-data-centers-in-cote-divoire-and-burkina-faso/ | Ouagadougou city-level | A for licence/operator; B for DC and solar from DCD | Telco-core DC lead. Do not classify as public colo without an Orange product/site page. |
| ONATEL / Moov Africa BF | Official https://www.moov-africa.bf/ ; ARCEP register https://www.arcep.bf/repertoire/ | Ouagadougou plus telco exchanges/PoPs | A for licence/operator; C/B for DC claims | Incumbent network core. Look for annual reports, hosting offers, backbone/NOC/core references. |
| Telecel Faso | Official https://telecelfaso.bf/ ; ARCEP licence https://www.arcep.bf/download/licence-neutre-telecel-s-a/ | Ouagadougou plus mobile-core infrastructure | A for licence/operator; C for inferred DC | Treat as mobile-core site universe, not standalone DC unless named. |
| BFIX legacy facilities | BFIX https://www.bfix.bf/ ; PeeringDB https://www.peeringdb.com/ix/2729 | Ouagadougou: Virtix, Immeuble du Faso, Ministere de l'agriculture | B/A for IXP/facility connection | Good interconnection leads. Need owner/status validation before counting legacy sites as DC inventory. |
| Essor Services + Kaia Energy | DCD https://www.datacenterdynamics.com/en/news/burkina-faso-to-launch-data-center-powered-by-waste-to-energy-plant/ ; WeAreTech https://www.wearetech.africa/en/fils-uk/news/tech/burkina-faso-to-launch-data-center-powered-by-waste-to-energy-plant | Burkina Faso; site undisclosed | C | Announced 12 MW waste-to-energy plant plus DC, completion target Nov 2025. Keep speculative unless EIA/permit/construction/commissioning evidence appears. |
| National digital infrastructure supervision center / NOC | Ecofin https://www.ecofinagency.com/news-digital/2001-52093-burkina-faso-launches-5-4-million-digital-infrastructure-supervision-center ; TechAfrica News https://techafricanews.com/2026/01/20/burkina-faso-kicks-off-construction-of-digital-infrastructure-monitoring-center/ | Ouagadougou | B | NOC/control center, not a DC by default. Use as join target for state DC operations and possible building permit/procurement records. |

Operator query block:

```text
"Virtix" OR "Virtual Technologies and Solutions" Burkina ("datacenter" OR colocation OR BFIX OR "Ouaga 2000")
"IKA Cloud" OR "IKA Solution" Burkina (datacenter OR hébergement OR colocation OR "Avenue de la Dignité")
"Alink Telecom" Burkina (datacenter OR colocation OR "centre de données" OR BFIX)
"IPSyS" OR "IPSYS TELECOM" Burkina (datacenter OR "Avenue Kwame Nkrumah" OR colocation)
"Orange Burkina" Ouagadougou ("data center" OR "centre de données" OR solaire OR SolarX)
"ONATEL" OR "Moov Africa Burkina" ("data center" OR "centre de données" OR hébergement OR cloud)
"Telecel Faso" Burkina ("data center" OR "centre de données" OR MSC OR "coeur de réseau")
"BFIX" Burkina ("Immeuble du Faso" OR "Ministere de l'agriculture" OR Virtix)
```

## 4. Region-by-Region Industry Strategy

The industry pass should record negative coverage explicitly. Most non-Centre hits will be telco PoPs, fibre, tower projects or ordinary IT rooms.

| Legacy region | Capital and current aliases | Industry sweep |
|---|---|---|
| Centre | Ouagadougou; Kadiogo | Full sweep. Search operator names plus Ouaga 2000, Palais des Sports, Cissin, Avenue de la Dignite, Avenue Kwame Nkrumah, Immeuble du Faso, Ministere de l'agriculture, Kossodo. Use BFIX/PeeringDB to validate interconnection. |
| Hauts-Bassins | Bobo-Dioulasso; Guiriko | Search BFIX Bobo-Dioulasso, Orange/ONATEL/Telecel, banks, university IT, fibre to Abidjan and SONABEL. Count only named colo/cloud/IX/PoP facilities. |
| Boucle du Mouhoun | Dedougou; Bankui; Sourou/Tougan | Search legacy and new names. Watch solar/energy and fibre route leads; expect negative DC result. |
| Cascades | Banfora; Tannounyan | Search Banfora, border fibre, telco PoPs, banks. |
| Centre-Est | Tenkodogo; Nakambe | Search Tenkodogo, Ghana/Togo corridor, operators and government digital services. |
| Centre-Nord | Kaya; Kuilse | Search Kaya, tower coverage, public services and security-related connectivity. |
| Centre-Ouest | Koudougou; Nando | Search Koudougou, Universite Norbert Zongo, operator PoPs, local hosting firms. |
| Centre-Sud | Manga; Nazinon | Negative sweep with Manga, government cloud/RESINA, operators. |
| Est | Fada N'Gourma; Goulmou; Sirba/Bogande; Tapoa/Diapaga | Search all aliases. Watch Benin/Niger interconnection, PRICAO and operator fibre, but require facility proof. |
| Nord | Ouahigouya; Yaadga | Search operator/tower projects and administrative ICT; security context means unsourced DC claims stay C. |
| Plateau-Central | Ziniare; Oubri | Search training, government and telco leads; do not count seminar/training centers. |
| Sahel | Dori; Liptako; Soum/Djibo | Lowest expected yield. Search Dori/Djibo with tower/fibre/operator terms; require official confirmation. |
| Sud-Ouest | Gaoua; Djoro | Search Gaoua, border links, government/ANPTIC and operator PoPs. |

Exact quick queries:

```text
"Boucle du Mouhoun" Burkina ("data center" OR datacenter OR "centre de données" OR colocation)
Cascades Banfora Burkina ("data center" OR datacenter OR "centre de données")
Centre Ouagadougou Burkina ("data center" OR datacenter OR "centre de données" OR colocation)
"Centre-Est" Tenkodogo Burkina ("data center" OR datacenter OR "centre de données")
"Centre-Nord" Kaya Burkina ("data center" OR datacenter OR "centre de données")
"Centre-Ouest" Koudougou Burkina ("data center" OR datacenter OR "centre de données")
"Centre-Sud" Manga Burkina ("data center" OR datacenter OR "centre de données")
Est "Fada N'Gourma" Burkina ("data center" OR datacenter OR "centre de données")
"Hauts-Bassins" Bobo-Dioulasso Burkina ("data center" OR datacenter OR "centre de données" OR BFIX)
Nord Ouahigouya Burkina ("data center" OR datacenter OR "centre de données")
"Plateau-Central" Ziniare Burkina ("data center" OR datacenter OR "centre de données")
Sahel Dori Burkina ("data center" OR datacenter OR "centre de données")
"Sud-Ouest" Gaoua Burkina ("data center" OR datacenter OR "centre de données")
```

Post-2025 alias queries:

```text
Kadiogo Ouagadougou Burkina datacenter
Guiriko Bobo-Dioulasso Burkina datacenter
Bankui Dedougou Burkina datacenter
Sourou Tougan Burkina "centre de données"
Goulmou "Fada N'Gourma" Burkina datacenter
Sirba Bogande Burkina datacenter
Tapoa Diapaga Burkina datacenter
Liptako Dori Burkina datacenter
Soum Djibo Burkina datacenter
```

## 5. Cloud, CDN and Edge Handling

Official region checks:

```text
site:aws.amazon.com/about-aws/global-infrastructure Burkina Faso
site:learn.microsoft.com/en-us/azure/reliability/regions-list Burkina Faso
site:cloud.google.com/about/locations Burkina Faso
site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Burkina Faso
"Burkina Faso" ("AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region")
```

Rules:
- A hyperscaler customer, partner, CDN cache or edge PoP is not a datacenter campus.
- Cloudflare and Meta appearing as BFIX peers proves interconnection at BFIX, not a separate Cloudflare/Meta datacenter.
- Local web hosting marketed to Burkina Faso from France, Dakar, Abidjan or elsewhere is not a BF facility unless the provider names a Burkina Faso facility.

## 6. Evidence Escalation Rules

- **Announcement to C/B**: press release, MoU, partner announcement, launch claim with no address or permit.
- **Construction to B/A**: groundbreaking, procurement award, ANEVE notice, commune permit, contractor notice, dated construction photos from official channel.
- **Operational to A/B**: official inauguration, operator services page with address, customer-ready colocation terms, BFIX/PeeringDB facility connection, utility energization, audited filing.
- **Capacity fields graded separately**: an official operator page can make location A while MW/rack/sqm figures from directories remain C.
- **Dedup before counting**: Cloud Gouvernemental, ANPTIC, MDENP, "mini datacenters", education DC and NOC are adjacent government infrastructure but not automatically the same facility. BFIX, Virtix and legacy Immeuble du Faso/Ministere de l'agriculture can overlap.

## 7. Common Burkina Faso Pitfalls

- Do not promote DataCenterPlatform/DataCenterMap/Inflect/Baxtel/DCJournal entries above C without corroboration.
- Do not count ordinary "salle serveur", cybercafe, university lab, bank DR room, NOC, telecom tower, fibre regeneration hut or e-government office unless the source proves hosting/colo/cloud/compute use.
- Do not rely on "Tier III" unless Uptime Institute or an equivalent certification page is found; otherwise record it as an operator claim.
- Do not assume a commercial facility from ARCEP licence alone. ARCEP identifies licensed telecom/service operators; facility proof needs site, interconnection, permit, EIA, power or service evidence.
- Do not assign a record to a region from a national article. Use the physical site. Most true records will resolve to Ouagadougou/Centre/Kadiogo.
- Keep security context in mind for Sahel, Nord and parts of Est: high-value infrastructure claims there need official confirmation.

## 8. Recommended Discovery Order

1. Build the Ouagadougou seed table from ANPTIC, Virtix, IKA, BFIX/PeeringDB, Orange, ONATEL/Moov, Telecel, Alink and IPSyS.
2. For each seed, run operator + address + `ARCEP`, `ANEVE`, `SONABEL`, `BFIX`, `PeeringDB`, `permis de construire`, and `rapport annuel`.
3. Sweep DCD, Ecofin, Developing Telecoms, leFaso.net, AIB, Sidwaya, Burkina24, Wakat Sera and WeAreTech for the seed names and French datacenter vocabulary.
4. Run the 13-region quick queries, then the post-2025 alias queries for current boundary names.
5. Reconcile every candidate against the official explorer source map and assign field-level grades before creating or updating facility records.
