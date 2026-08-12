# ML Explorer Industry - Mali Datacenter Discovery

Date verified: 2026-08-12. Scope: industry media, operator pages, vendor pages, directories, IX/peering records, and local press for Mali datacenter enumeration.

## Boundary And Attribution

Primary project attribution uses the complete **11-division working model**: Bamako District; Kayes; Koulikoro; Sikasso; Segou; Mopti; Tombouctou; Gao; Kidal; Taoudenit; Menaka.

Mali's 2023 legal map is broader: 19 regions plus Bamako. Do not describe the 19-region reform as only proposed. Use the nine added regions as mandatory search aliases and, where the data model only supports 11 divisions, roll them up carefully: Bougouni and Koutiala under Sikasso; Dioila and Nara under Koulikoro; Nioro and Kita under Kayes; Bandiagara and Douentza under Mopti; San under Segou. Note the 2023-region name in aliases/notes.

Boundary references: SGG Journal Officiel portal https://sgg-mali.ml/fr/journal-officiel/le-journal-officiel.html ; KAS March 2023 press review summary https://www.kas.de/documents/265798/17649333/KAS_Bamako_%2BNewsletter%2B4%2BMars1%2B2023.pdf .

## Reliability Grades

- **A**: official operator facility/service page, government/ministry/SMTD/AMRTP/APDP/AEDD/ARMDS/DGMP/EDM/CREE record, commune permit, official cloud-provider region list, PeeringDB/PCH record for interconnection facts.
- **B**: strong trade or local press: Data Center Dynamics, Connecting Africa, Ecofin/Agence Ecofin, TechAfrica News, ITWeb Africa, Africa24 TV, L'Essor, maliweb.net, Malijet, Bamada, Telecom Review Africa, WeAreTech Africa, credible vendor case study.
- **C**: directories and market aggregators, social posts not from official channels, paid market-report snippets, job posts, old MoUs, provider marketplaces, and claims lacking address/status/operator/power evidence.

Field-level grading is required. Directory MW, rack, coordinate or certification values stay C until verified by an operator, permit, procurement, power or engineering source.

## Market Reality

- Mali's datacenter evidence is overwhelmingly Bamako-centric. Outside Bamako/Kati, expect telco PoPs, towers, microwave/fibre regeneration, public-administration server rooms and ordinary IT rooms rather than customer-ready datacenters.
- Confirmed high-value seeds are the national Tier III government datacenter announcement in Bamako, SMTD-SA's mutualized hosting datacenter, Afribone's commercial datacenter/colocation pages, and MLIX as an interconnection point.
- The 2026 national datacenter is reported as inaugurated in Bamako on 2026-01-31 during Mali's third Semaine du Numerique. Treat location/status as B unless using the government Facebook/CIGMA post; treat Tier III as a claim until certification/design evidence is found.
- Mali is landlocked, so international capacity depends on terrestrial routes through Senegal, Guinea, Cote d'Ivoire, Mauritania and regional operators. Do not infer hyperscale viability from sovereignty messaging alone.
- Power is a gating constraint. Any operational facility record needs generator/UPS/grid/solar/PPA evidence or an explicit unknown field.
- No AWS, Azure, Google Cloud or Oracle OCI public cloud region in Mali was found on official region lists checked on 2026-08-12.

## Industry Source Triage

| Source | Verified route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/government-of-mali-launches-data-center-in-bamako/ | Corroborates the 2026 Bamako government datacenter; states Tier III-standard/design language. | B. |
| Connecting Africa | https://www.connectingafrica.com/data-centers/mali-inaugurates-a-tier-iii-data-center | Trade coverage of the Tier III opening. | B. |
| Ecofin / Agence Ecofin | https://www.agenceecofin.com/actualites-numerique/0202-135390-le-mali-inaugure-un-data-center-tier-iii-et-renforce-sa-souverainete-numerique ; https://www.ecofinagency.com/news-digital/0202-52488-mali-opens-tier-iii-data-center-in-bamako-amid-regional-push-to-keep-data-at-home | Digital and telecom project coverage; useful for Mali DC/state-sovereignty leads. | B. |
| TechAfrica News | https://techafricanews.com/2026/02/02/mali-inaugurates-tier-iii-data-center-to-strengthen-digital-sovereignty-in-the-sahel/ | Named minister/event details for 2026 Tier III inauguration. | B. |
| Africa24 TV | https://africa24tv.com/mali-un-data-center-de-derniere-generation-inaugure-a-bamako/ | Video/press coverage for Bamako inauguration; note it contains a date typo in snippet contexts, so verify against other sources. | B/C. |
| maliweb.net | https://www.maliweb.net/technologie/mali-inauguration-dun-data-center-tier-iii-un-tournant-majeur-pour-la-souverainete-numerique-de-laes-3113579.html | Local coverage of state DC and sovereignty messaging. | B. |
| Bamada | https://bamada.net/le-mali-dispose-desormais-dun-data-center-un-centre-de-stockage-de-donnee-numerique-cree-par-afribone-mali | Local report on Afribone's 2019 datacenter launch. | B/C; verify against Afribone page. |
| Afribone | https://afribone.com/data-center/ ; https://afribone.com/data-center/colocation-housing/ | Operator-owned commercial datacenter and colocation evidence. | A for service existence/contact; capacity/power needs verification. |
| SMTD-SA | https://www.smtd.ml/nos-services/centre-de-donnees/ ; https://www.smtd.ml/ | State operator hosting datacenter service. | A for service existence. |
| PeeringDB | https://www.peeringdb.com/ix/2665 ; https://www.peeringdb.com/fac/7240 ; https://www.peeringdb.com/org/23638 | MLIX and Afribone interconnection/facility leads. | A/B for interconnection/facility directory facts; not power/capacity proof. |
| DataCenterMap | https://www.datacentermap.com/mali/ ; https://www.datacentermap.com/mali/bamako/ ; example Huawei/Mali page https://www.datacentermap.com/mali/bamako/huawei-mali/ | Discovery only; current Mali/Bamako count pages show 1 listed facility, and a Huawei/Mali government-Tier lead appears. | C. |
| DC Hub / Connectbase / datacenters.com | https://dchub.cloud/facilities/afribone-mali-sa-afribone-dc-bamako-mali-d1f706d8 ; https://www.connectbase.com/data-center/afribone-dc-bamako-mali/ ; https://www.datacenters.com/locations/mali/bamako | Discovery and cross-check of Afribone/Bamako listings. | C unless corroborated. Keep directory MW/coordinates C. |
| Official cloud lists | AWS, Azure, Google, Oracle links in official explorer | Negative hyperscaler check. | A. |

Trade-press query block:

```text
site:datacenterdynamics.com/en/news/ Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données")
site:connectingafrica.com Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données")
site:agenceecofin.com Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR fibre OR cloud)
site:ecofinagency.com Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR fibre OR cloud)
site:techafricanews.com Mali (datacenter OR "data center" OR "digital sovereignty" OR "centre de donnees")
site:africa24tv.com Mali (datacenter OR "data center" OR "centre de donnees" OR numerique OR numérique)
site:maliweb.net Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR "souverainete numerique" OR "souveraineté numérique")
site:bamada.net Mali (datacenter OR "centre de donnees" OR Afribone OR Telecel OR AMRTP)
site:malijet.com Mali (SMTD OR datacenter OR "centre de donnees" OR EDM OR fibre)
"Mali" (datacenter OR "data center" OR "centre de donnees" OR "centre de données") (MW OR racks OR FCFA OR colocation OR "Tier III" OR Uptime)
```

## Operator And Project Seeds

| Seed | URLs | Location signal | Grade | Handling |
|---|---|---|---|---|
| National Tier III government datacenter | Government FB/CIGMA https://www.facebook.com/GouvMali/posts/cigma-info-inauguration-du-data-center-tier-iii-un-pas-d%C3%A9cisif-vers-la-souverain/1426931632127756/ ; DCD https://www.datacenterdynamics.com/en/news/government-of-mali-launches-data-center-in-bamako/ ; Ecofin https://www.agenceecofin.com/actualites-numerique/0202-135390-le-mali-inaugure-un-data-center-tier-iii-et-renforce-sa-souverainete-numerique ; TechAfrica News https://techafricanews.com/2026/02/02/mali-inaugurates-tier-iii-data-center-to-strengthen-digital-sovereignty-in-the-sahel/ ; Maliweb https://www.maliweb.net/technologie/mali-inauguration-dun-data-center-tier-iii-un-tournant-majeur-pour-la-souverainete-numerique-de-laes-3113579.html | Bamako District; exact address/operator not public in verified sources | B for inauguration/location; A only with official web/procurement/operator page; Tier III is claim-grade until certification/design docs. | Record as a state-government facility lead. Required follow-up: operator, address, Huawei/contractor role if any, capacity, power, certification and dedupe against SMTD. |
| SMTD-SA mutualized hosting datacenter | https://www.smtd.ml/nos-services/centre-de-donnees/ ; https://www.smtd.ml/nos-services/ ; https://www.smtd.ml/projets/mali-numerique/ | Bamako/Kati urban area; exact facility not public in verified sources | A for service existence. | State hosting/colo lead. Do not conflate with the 2026 Tier III DC unless site/operator evidence proves it. |
| Afribone DC / colocation | https://afribone.com/data-center/ ; https://afribone.com/data-center/colocation-housing/ ; Bamada 2019 launch https://bamada.net/le-mali-dispose-desormais-dun-data-center-un-centre-de-stockage-de-donnee-numerique-cree-par-afribone-mali ; PeeringDB org https://www.peeringdb.com/org/23638 | Bamako, Baco Djicoroni/Baco Djikoroni | A for official service/contact; B for launch press; C for aggregator capacity fields. | Strong commercial DC candidate. Verify address, coordinates, power, certification and current operational status. |
| MLIX - Point d'echange du Mali | https://www.peeringdb.com/ix/2665 ; https://www.peeringdb.com/fac/7240 ; http://www.mlix.ml | Bamako | A/B for IX facts; C if used as DC proof. | PeeringDB shows 5 peers and 5G capacity. Count as interconnection, not as a standalone datacenter. |
| Orange Mali | https://www.orangemali.com/ ; AMRTP routes https://amrtp.ml/ | Bamako core plus national network | A for operator status; C for datacenter inference. | Search for hosting/cloud/enterprise colocation or core facility evidence. Do not count shops, towers or offices. |
| Moov Africa Malitel / SOTELMA | PeeringDB peer appears on MLIX https://www.peeringdb.com/ix/2665 | Bamako core plus national network | A/B for operator and peering; C for datacenter inference. | Incumbent/telco core seed. Need hosting/colo/cloud, NOC/core or facility source before record creation. |
| Telecel Mali / ATEL SA | MLIX peer via PeeringDB https://www.peeringdb.com/ix/2665 ; Bamada rollout searches | Bamako/ACI 2000 plus rollout cities such as Kati, Sikasso, Segou, Kayes, Koutiala, Koulikoro | A/B for operator/peering; C for inferred DC. | Search MSC/core-network and hosting evidence. Rollout city does not imply datacenter. |
| Directories: Huawei Mali, Afribone listings | DataCenterMap Huawei lead https://www.datacentermap.com/mali/bamako/huawei-mali/ ; DC Hub Afribone https://dchub.cloud/facilities/afribone-mali-sa-afribone-dc-bamako-mali-d1f706d8 ; Connectbase Afribone https://www.connectbase.com/data-center/afribone-dc-bamako-mali/ | Bamako | C. | Use only to trigger official searches. Directory coordinates/MW/certifications require corroboration. |
| Banks, universities, government agencies | Search-specific only | Bamako and regional capitals | C unless site-level evidence. | Watch for DR sites and server rooms, but count only if source proves hosting/colo/cloud/compute facility function. |

Operator query block:

```text
SMTD OR "Societe Malienne de Transmission" Mali (datacenter OR "centre de donnees" OR "centre de données" OR hebergement OR hébergement OR fibre OR cloud)
Afribone Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR housing OR MLIX)
"Orange Mali" Bamako (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR cloud OR NOC)
"Moov Africa Malitel" OR SOTELMA Mali (datacenter OR "centre de donnees" OR "centre de données" OR hebergement OR hébergement OR cloud OR NOC)
"Telecel Mali" OR "ATEL" Mali (datacenter OR "centre de donnees" OR "centre de données" OR MSC OR "coeur de reseau" OR "cœur de réseau")
MLIX OR "Point d'echange du Mali" OR "Point d’échange du Mali" (Bamako OR peers OR Afribone OR SOTELMA OR ATEL)
"Mali" (datacenter OR "centre de donnees" OR "centre de données") ("Tier III" OR inauguration OR souverainete OR souveraineté OR AES OR Huawei)
```

## Region-By-Region Industry Strategy

| Division | Capital and aliases | Industry sweep |
|---|---|---|
| Bamako District | Bamako; ACI 2000, Hamdallaye, Rue 390/Rue 360, Baco Djicoroni/Baco Djikoroni, Badalabougou, Faladie, Korofina, Senou | Full sweep. Seeds: government Tier III DC, SMTD DC, Afribone DC, MLIX, Orange, Moov/SOTELMA, Telecel/ATEL, AMRTP. Validate interconnection via PeeringDB/MLIX and power via EDM/CREE/AEDD/procurement. |
| Kayes | Kayes; Kita, Nioro du Sahel, Diema | Search fibre corridors to Senegal/Mauritania, Telecel/operator PoPs, energy projects and bank/agency DR rooms. Expect negative DC result. |
| Koulikoro | Koulikoro; Kati, Dioila, Nara | Search Kati heavily because SMTD's new HQ is in the Kati agglomeration and Bamako-adjacent infrastructure may appear there. Also sweep Koulikoro/Dioila/Nara PoPs. |
| Sikasso | Sikasso; Koutiala, Bougouni | Search border connectivity to Cote d'Ivoire, operator rollout, banks and government regional systems. Require hosting/colo/cloud proof. |
| Segou | Segou/Ségou; San | Search operator PoPs, regional administration IT, hydropower/EDM context, and San as 2023-region alias. |
| Mopti | Mopti; Sevare, Bandiagara, Douentza | Search security/connectivity projects and regional PoPs. Treat unsourced facility claims as C because of conflict/security context. |
| Tombouctou | Tombouctou/Timbuktu; Goundam, Dire, Niafunke | Mandatory negative sweep. Search satellite, tower, administrative connectivity and Taoudenit split references. |
| Gao | Gao; Bourem, Ansongo | Negative sweep; search telco PoPs and state-connectivity projects only. |
| Kidal | Kidal; Tessalit, Aguelhok | Negative sweep. Require official/operator confirmation for any site claim. |
| Taoudenit | Taoudenit/Taoudeni/Taoudénit/Taoudennit | Negative sweep. Expect mining, satellite, tower or administrative leads rather than datacenters. |
| Menaka | Menaka/Ménaka; Anderamboukane | Negative sweep. Require official evidence plus power/connectivity proof. |

Exact quick queries:

```text
Bamako Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR MLIX OR SMTD OR Afribone OR Huawei)
Kayes Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Koulikoro OR Kati Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Sikasso Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Segou OR Ségou Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Mopti OR Sevare Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Tombouctou OR Timbuktu Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Gao Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Kidal Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Taoudenit OR Taoudeni OR Taoudénit OR Taoudennit Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
Menaka OR Ménaka Mali (datacenter OR "centre de donnees" OR "centre de données" OR colocation OR PoP)
```

2023 alias quick queries:

```text
Bougouni Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Dioila Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Nioro du Sahel Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Koutiala Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Kita Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Nara Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Bandiagara Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
San Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
Douentza Mali (datacenter OR "centre de donnees" OR "centre de données" OR PoP)
```

## Cloud, CDN And Edge Handling

Official negative-check queries:

```text
site:aws.amazon.com/about-aws/global-infrastructure Mali
site:aws.amazon.com/about-aws/global-infrastructure/localzones Mali
site:learn.microsoft.com/en-us/azure/reliability/regions-list Mali
site:cloud.google.com/about/locations Mali
site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Mali
"Mali" ("AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region" OR "OCI region")
```

Rules:
- Hyperscaler customer, partner, CDN cache, local reseller or edge PoP claims do not prove a datacenter campus.
- MLIX peers prove interconnection at MLIX, not separate hyperscaler facilities.
- Web hosting marketed to Mali from France, Senegal, Cote d'Ivoire or elsewhere is not an ML facility unless a Mali site is named.
- AES-regional sovereignty claims are policy signals; count only site-level records.

## Evidence Escalation Rules

- Announcement/MoU: C or B depending on source; never operational without inauguration/service evidence.
- Construction/procurement: B/A if DGMP, marchespublics, ARMDS, AEDD, commune permit or official contractor page exists.
- Operational: A/B if operator service page, official inauguration, PeeringDB facility connection, customer terms, utility energization or audited filing exists.
- Capacity: grade separately. A directory's 3 MW claim for Afribone remains C until Afribone, a utility, permit or engineering record confirms it.
- Dedupe before counting: national Tier III, SMTD and future cloud-gouvernemental references may be one physical estate; MLIX is an IXP; operator offices and NOCs are not DCs by default.

## Common Mali Pitfalls

- Do not use directory pages as final authority. DataCenterMap currently shows one Mali/Bamako market listing and a Huawei/Mali lead, but those are C-grade discovery leads until official evidence confirms them.
- Do not omit Tombouctou from the 11-division sweep.
- Do not call Mali's 2023 19-region reform merely proposed; instead state how the project schema handles attribution.
- Do not convert `salle serveur`, bank IT rooms, university labs, cybercafes, tower sites, fibre huts, government offices or NOCs into datacenter records without hosting/colo/cloud/compute evidence.
- Do not treat Tier III as certified unless Uptime Institute, official design/certification, procurement specification or engineering evidence supports it.
- Do not infer a facility from an AMRTP licence or a mobile-network rollout city.
- Use physical site for region attribution, not the scope of a national article.

## Recommended Discovery Order

1. Build Bamako seed records: national Tier III DC, SMTD DC, Afribone DC, MLIX, Orange, Moov/SOTELMA, Telecel/ATEL.
2. For each seed, run operator + address + `AMRTP`, `DGMP`, `marchespublics`, `AEDD`, `EDM`, `CREE`, `MLIX`, `PeeringDB`, `permis de construire`, `rapport annuel`.
3. Sweep DCD, Connecting Africa, Ecofin, TechAfrica News, Africa24 TV, maliweb, Bamada and Malijet using French and English datacenter terms.
4. Run all 11-division queries, then all 2023 alias queries.
5. Assign field-level grades and write explicit negative coverage notes for every non-Bamako division before creating facility records.
