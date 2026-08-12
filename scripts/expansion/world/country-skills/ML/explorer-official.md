# ML Explorer Official - Mali Datacenter Enumeration

Date verified: 2026-08-12. Country: ML - Mali. Scope: official, regulatory, procurement, environmental, energy, interconnection, and cloud-provider evidence for datacenter discovery.

## Boundary Model

Use the project-required **11-division working model** for primary attribution: Bamako District plus Kayes, Koulikoro, Sikasso, Segou, Mopti, Tombouctou, Gao, Kidal, Taoudenit, and Menaka. This is the complete 10-region + Bamako model used by many datasets after Taoudenit and Menaka were operationalized.

Do **not** say the 19-region reform is merely proposed. Mali's 2023 legal/administrative map expanded to 19 regions plus Bamako. The SGG Journal Officiel is the primary route for the laws; secondary summaries cite Loi 2023-006 and Loi 2023-007. Until the upstream schema changes, keep the nine newer regions as mandatory search aliases and resolve physical sites back to the requested 11-division model where possible.

Core 11 divisions: Bamako District; Kayes; Koulikoro; Sikasso; Segou; Mopti; Tombouctou; Gao; Kidal; Taoudenit; Menaka.

2023 added-region aliases to sweep: Bougouni, Dioila, Nioro, Koutiala, Kita, Nara, Bandiagara, San, Douentza. Also search spellings with accents: Segou/Ségou, Tombouctou/Timbuktu, Taoudenit/Taoudeni/Taoudénit/Taoudennit, Menaka/Ménaka.

Boundary sources:
- SGG Journal Officiel portal: https://sgg-mali.ml/fr/journal-officiel/le-journal-officiel.html
- SGG JO archive example for official legal texts: https://sgg-mali.ml/JO/2026/mali-jo-2026-10-3.pdf
- KAS Mali press review summarizing the March 2023 decentralization package: https://www.kas.de/documents/265798/17649333/KAS_Bamako_%2BNewsletter%2B4%2BMars1%2B2023.pdf

## Reliability Grades

- **A**: primary source: ministry/agency/official-gazette page, SMTD or operator-owned facility/service page, AMRTP licence/register/decision, DGMP/marchespublics/ARMDS procurement record, AEDD environmental record, EDM/CREE power record, commune permit, official cloud-provider region list, PeeringDB/PCH/IXP record for interconnection facts.
- **B**: strong secondary: Data Center Dynamics, Connecting Africa, Ecofin/Agence Ecofin, TechAfrica News, Africa24 TV, ITWeb Africa, L'Essor, maliweb.net, Malijet, Bamada, local media relaying a named official event, credible vendor case study.
- **C**: weak lead: aggregator directories, social media unless it is a verified government/operator account, paid market reports, job posts, MoUs, launch claims with no address/operator/power/permit trail, ordinary server-room/NOC wording without hosting/colo/cloud function.

Grade by field. A facility can have A-grade existence, B-grade status, and C-grade capacity. Do not promote a Tier III, MW, rack, or coordinate field above the source that actually proves that field.

## Official Source Map

| Source | Verified URL | Use | Grade and cautions |
|---|---|---|---|
| Ministry of Communication, Digital Economy and Administration Modernization (MCENMA) | https://communication.gouv.ml/ ; official event site https://semainedunumerique.gouv.ml/ ; official FB https://www.facebook.com/MCENMAMali/ | Digital policy, Mali Numerique, Semaine du Numerique, government datacenter/cloud announcements. | A for communication.gouv.ml and semainedunumerique.gouv.ml pages; B for Facebook-only posts unless corroborated. |
| SMTD-SA - Societe Malienne de Transmission et de Diffusion | https://www.smtd.ml/ ; https://www.smtd.ml/nos-services/centre-de-donnees/ ; https://www.smtd.ml/nos-services/ ; https://www.smtd.ml/projets/mali-numerique/ | State infrastructure operator. Its centre-de-donnees page says SMTD provides a mutualized hosting datacenter under Malian jurisdiction. | A for the SMTD datacenter service existence and service claims. Still verify physical address, racks, power and whether this is the same site as the 2026 national Tier III DC. |
| AMRTP - telecom/TIC/post regulator | https://amrtp.ml/ ; https://www.amrtp.ml/OM/ | Operator licences, authorisations, declarations, sector observatory, interconnection and numbering context. | A for licence/register/operator facts; licence does not prove a datacenter. |
| CREE - electricity/water regulator | Primature page https://primature.ml/cree-commission-de-regulation-de-lelectricite-et-de-leau/ ; AFUR member page listing www.creemali.ml and Bamako contact https://afurnet.org/member.php?id=12 | Tariffs, regulated electricity/water service context, large-consumer power sanity checks. | A for official Primature legal/institutional text; B for AFUR directory details. Verify creemali.ml if reachable before using as A. |
| EDM-SA / energy ministry | https://energie.gouv.ml/ | Grid supply, substations, large-consumer power, load-shedding context, sector agencies such as AMADER. | A for official ministry/utility documents. Every DC record needs separate power evidence because Mali has recurring grid-supply constraints. |
| AMADER | https://energie.gouv.ml/amader/ | Rural electrification and off-grid/mini-grid context for regional leads. | A for agency facts; not DC evidence by itself. |
| AEDD - environmental agency | https://aedd.gouv.ml/ | Environmental and social impact (EIES) trail for generator-heavy or large construction projects. | A when a project-specific AEDD/EIES notice is found. |
| ARMDS - public procurement regulator | https://www.armds.ml/ | Procurement disputes, awards, transparency records for state datacenter/cloud/fibre/NOC contracts. | A for official procurement/regulatory records. |
| DGMP-DSP and public-procurement portal | https://www.dgmp.gouv.ml/ ; https://marchespublics.ml/ | Tender and award searches for datacenter, cloud, fibre, NOC, supervision-center and e-government infrastructure. | A for notices/awards. Search syntax must query each domain separately. |
| API-Mali | https://apimali.gov.ml/ | Investment-code approvals and investor records for large ICT infrastructure. | A for official approvals; investor-marketing pages are discovery only. |
| APDP - personal-data authority | https://apdp.ml/ ; Primature institutional page https://primature.ml/apdp-autorite-de-protection-des-donnees-a-caractere-personnel/ | Data-protection obligations and sovereignty/localization arguments. | A for APDP/Primature facts. Data-protection law does not prove a facility. |
| MLIX - Point d'echange du Mali | PeeringDB IX https://www.peeringdb.com/ix/2665 ; facility https://www.peeringdb.com/fac/7240 ; org route https://www.peeringdb.com/org/20064 ; http://www.mlix.ml | Interconnection evidence in Bamako. PeeringDB shows MLIX, Bamako, 5G total capacity, prefix 196.60.46.0/24, peers Afribone, ATEL, PCH AS3856, PCH AS42 and SOTELMA. | A/B for interconnection facts; PeeringDB is user-maintained and the IX record is old. MLIX is not a commercial datacenter record by itself. |
| Official cloud-region lists | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Negative check for hyperscaler regions. | A. No AWS, Azure, Google Cloud or OCI public cloud region in Mali found in official lists checked on 2026-08-12. |

## Official Search Templates

Use separate queries per domain; `site:a OR site:b` is unreliable in most search tools.

```text
site:communication.gouv.ml Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR cloud OR "souverainete numerique" OR "souveraineté numérique")
site:semainedunumerique.gouv.ml Mali (datacenter OR "centre de donnees" OR "centre de données" OR Tier OR cloud OR AES)
site:smtd.ml (datacenter OR "centre de donnees" OR "centre de données" OR hebergement OR hébergement OR cloud OR "Mali numerique" OR "Mali numérique")
site:amrtp.ml (datacenter OR "centre de donnees" OR "centre de données" OR operateur OR opérateur OR autorisation OR agrement OR agrément OR interconnexion)
site:amrtp.ml/OM/ (operateurs OR opérateurs OR trafic OR abonnes OR abonnés OR indicateurs)
site:dgmp.gouv.ml (datacenter OR "centre de donnees" OR "centre de données" OR "cloud gouvernemental" OR "fibre optique" OR NOC OR "centre de supervision")
site:marchespublics.ml (datacenter OR "centre de donnees" OR "centre de données" OR cloud OR "fibre optique" OR NOC OR "centre de supervision")
site:armds.ml (datacenter OR "centre de donnees" OR "centre de données" OR cloud OR "marches publics" OR "marchés publics")
site:aedd.gouv.ml (datacenter OR "centre de donnees" OR "centre de données" OR EIES OR "etude d'impact" OR "étude d'impact" OR groupe électrogène OR refroidissement)
site:energie.gouv.ml (EDM OR electricite OR électricité OR CREE OR tarif OR coupure OR délestage OR substation OR poste)
site:apimali.gov.ml (datacenter OR "centre de donnees" OR "centre de données" OR numerique OR numérique OR investissement OR agrement OR agrément)
site:apdp.ml (hebergement OR hébergement OR cloud OR donnees OR données OR transfert OR responsable OR sous-traitant)
```

Operator and project pivots:

```text
"{operator}" Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR hebergement OR hébergement OR cloud)
"{operator}" Mali (AMRTP OR licence OR agrement OR agrément OR EDM OR CREE OR AEDD OR "permis de construire")
"{operator}" (MLIX OR PeeringDB OR "196.60.46" OR Bamako OR "ACI 2000" OR Hamdallaye OR Kati)
```

## Officially Verified Seeds

| Candidate | Physical attribution | Best verified URLs | Grade | Handling |
|---|---|---|---|---|
| National Tier III government datacenter | Bamako District; exact site/operator not public in sources reviewed | Government FB/CIGMA announcement: https://www.facebook.com/GouvMali/posts/cigma-info-inauguration-du-data-center-tier-iii-un-pas-d%C3%A9cisif-vers-la-souverain/1426931632127756/ ; DCD https://www.datacenterdynamics.com/en/news/government-of-mali-launches-data-center-in-bamako/ ; Ecofin https://www.agenceecofin.com/actualites-numerique/0202-135390-le-mali-inaugure-un-data-center-tier-iii-et-renforce-sa-souverainete-numerique ; TechAfrica News https://techafricanews.com/2026/02/02/mali-inaugurates-tier-iii-data-center-to-strengthen-digital-sovereignty-in-the-sahel/ ; Maliweb https://www.maliweb.net/technologie/mali-inauguration-dun-data-center-tier-iii-un-tournant-majeur-pour-la-souverainete-numerique-de-laes-3113579.html | B for inauguration and Bamako; A only if an official web page/procurement/operator spec is found. Tier III is a claim unless certification/design documents are found. | Record as state/government DC lead for e-government, state data and AES data-sovereignty use. Required unknowns: operator, address, certification basis, racks, MW/kVA, gensets, UPS, cooling, procurement trail, dedupe against SMTD. |
| SMTD-SA mutualized hosting datacenter | Bamako/Kati urban area; exact facility address not public in verified sources | https://www.smtd.ml/nos-services/centre-de-donnees/ ; https://www.smtd.ml/nos-services/ ; https://www.smtd.ml/ ; SMTD new HQ in Kati article https://www.smtd.ml/smtd-sa-les-ministres-de-laes-inuagurent-le-nouveau-siege/ | A for SMTD-operated hosting-service existence; field grades remain unknown for capacity/power/site. | Confirmed state-owned datacenter service. Do not merge with the national Tier III DC until an official address/operator relation proves it. |
| Afribone datacenter / colocation | Bamako, Baco Djicoroni/Baco Djikoroni area | Official page https://afribone.com/data-center/ ; colocation page https://afribone.com/data-center/colocation-housing/ ; PeeringDB org https://www.peeringdb.com/org/23638 ; secondary launch story https://bamada.net/le-mali-dispose-desormais-dun-data-center-un-centre-de-stockage-de-donnee-numerique-cree-par-afribone-mali | A for operator service page and address/contact; B for PeeringDB/network context; C for directory-only MW/coordinate claims. | Strong commercial/ISP facility seed. Verify whether the facility is neutral, exact street/coordinates, power and current customer-ready colocation terms. |
| MLIX | Bamako | PeeringDB IX https://www.peeringdb.com/ix/2665 ; PeeringDB facility https://www.peeringdb.com/fac/7240 ; http://www.mlix.ml | A/B for IX/interconnection facts; not DC proof. | Treat as interconnection object hosted at/near a facility. Do not count as a datacenter without host-facility evidence. |
| Orange Mali, Moov Africa Malitel/SOTELMA, Telecel/ATEL and other AMRTP operators | National operations, core likely Bamako; regional PoPs possible | AMRTP https://amrtp.ml/; operator websites | A for telecom status; C for inferred facilities. | Build operator universe from AMRTP, then pivot to facility/service evidence. A telco licence, tower, MSC, NOC or office does not equal a datacenter record. |
| Government cloud / e-government hosting | Bamako-centric until site proven otherwise | MCENMA https://communication.gouv.ml/ ; SMTD https://www.smtd.ml/projets/mali-numerique/ ; DGMP and marchespublics portals | B/A depending on source. | Use to find procurement and platform dependencies. Dedupe against SMTD and Tier III datacenter. |

## Regulatory And Permitting Logic

- Telecom: AMRTP licences and reports identify the operator universe. Use them to find Orange Mali, Moov Africa Malitel/SOTELMA, Telecel/ATEL, Afribone and smaller ISPs, then pivot to datacenter/hosting/colocation evidence.
- Procurement: government datacenter/cloud/NOC/fibre contracts should surface in DGMP-DSP, marchespublics.ml, ARMDS or official ministry releases. Search French terms and tender vocabulary: `avis d'appel d'offres`, `attribution`, `marché`, `fourniture`, `installation`, `centre de données`.
- Building permits: likely commune-level and poorly indexed. For Bamako, search mairie/commune names and quartier names; for regional capitals, expect offline confirmation.
- Environmental: search AEDD and indexed EIES files for generator fuel storage, cooling systems, building works, energy plants and large ICT estates.
- Energy: grade the power layer separately. Look for EDM grid connection, substation/poste source, kVA/MVA/MW, genset autonomy, UPS topology, fuel storage, solar/PPA and load-shedding mitigation.
- Data protection: APDP evidence supports compliance and sovereignty rationale but never proves a physical facility.
- Investment: API-Mali approvals can identify foreign or large local ICT infrastructure projects but require site-level follow-up.

## 11-Division Coverage Strategy

| Division | Capital / aliases | Expected yield | Official strategy |
|---|---|---|---|
| Bamako District | Bamako; ACI 2000, Hamdallaye, Rue 390/Rue 360, Baco Djicoroni/Baco Djikoroni, Badalabougou, Faladie, Korofina, Senou | High | Exhaustive pass. Seeds: Tier III government DC, SMTD DC, Afribone DC, MLIX, AMRTP, Orange, Moov/SOTELMA, Telecel/ATEL. Search permits, AEDD, EDM/CREE and procurement. |
| Kayes | Kayes; Kita, Nioro du Sahel, Diema | Low | Search telco PoPs, fibre corridors to Senegal/Mauritania, energy projects and any DR/hosting wording. Attribute Kita/Nioro hits carefully under the 11-division model unless schema supports 2023 regions. |
| Koulikoro | Koulikoro; Kati, Dioila, Nara | Low to medium because Kati is close to Bamako | Search Kati and Koulikoro for SMTD/telecom facilities, military/state infrastructure, fibre routes and power. Kati may produce Bamako-adjacent facility evidence. |
| Sikasso | Sikasso; Koutiala, Bougouni | Low | Search border/fibre route to Cote d'Ivoire, operator PoPs, banks, university/server-room leads. Do not count ordinary IT rooms. |
| Segou | Segou/Ségou; San | Low | Search Segou/San operator PoPs, hydropower/EDM context, government regional IT projects. |
| Mopti | Mopti; Bandiagara, Douentza, Sevare | Low | Search security/connectivity projects, regional PoPs and administration IT. Require official confirmation for any physical-site claim. |
| Tombouctou | Tombouctou/Timbuktu; Goundam, Dire, Niafunke | Very low | Negative sweep is mandatory. Search Taoudenit/Tombouctou split issues, satellite/tower/mining-camp leads, and official state-connectivity projects. |
| Gao | Gao; Bourem, Ansongo | Very low | Negative sweep; search PoPs, state connectivity and security projects. Treat private facility claims as C unless official. |
| Kidal | Kidal; Tessalit, Aguelhok | Very low | Negative sweep; security context makes facility claims high-risk. Require official/operator site proof. |
| Taoudenit | Taoudenit/Taoudeni/Taoudénit/Taoudennit; desert basin | Very low | Negative sweep using all spelling variants. Expect only mining, satellite, tower or administrative-connectivity leads. |
| Menaka | Menaka/Ménaka; Anderamboukane | Very low | Negative sweep; require official confirmation and power/connectivity evidence. |

Per-division query block:

```text
"{division}" Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR hebergement OR hébergement OR cloud)
"{capital}" Mali (datacenter OR "centre de donnees" OR "centre de données" OR "salle serveur" OR "point de presence" OR PoP)
"{capital}" Mali (Orange OR "Moov Africa" OR Malitel OR SOTELMA OR Telecel OR ATEL OR Afribone OR SMTD) (datacenter OR "centre de donnees" OR "centre de données" OR PoP OR NOC)
"{division}" Mali ("permis de construire" OR EIES OR AEDD OR EDM OR CREE OR "poste électrique" OR "groupe électrogène") (datacenter OR "centre de donnees" OR numerique OR numérique)
site:amrtp.ml "{capital}" (operateur OR opérateur OR licence OR agrement OR agrément)
```

Exact 11-division sweep:

```text
Bamako Mali (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR MLIX OR SMTD OR Afribone)
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

2023 alias sweep:

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

## Cloud-Provider Negative Checks

No Mali public cloud region was found in the official AWS, Microsoft Azure, Google Cloud or Oracle OCI region lists checked on 2026-08-12.

| Provider | Official URL | Mali handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No Mali region/local-zone evidence. CloudFront/CDN/customer claims do not imply an AWS datacenter in Mali. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Mali Azure public cloud region. |
| Google Cloud | https://cloud.google.com/about/locations | No Mali Google Cloud region/location. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Mali OCI region. |

## Minimum Record Standard

Every candidate facility record must carry:
- canonical name and aliases;
- owner/operator/legal entity;
- 11-division attribution plus 2023-region alias if relevant;
- locality, quartier/street/landmark and coordinates when sourceable;
- status: announced, procurement, permitted, construction, inaugurated, operational, inactive;
- function: commercial colocation, government cloud, state hosting, telco core, IXP, NOC, server room, speculative;
- capacity fields with separate grades: racks, sqm, MW/kVA/MVA, storage, compute, VMs;
- power fields: EDM grid, substation/poste, gensets, fuel autonomy, UPS, cooling, solar/PPA;
- evidence URLs and grade per material field;
- dedupe notes against SMTD, national Tier III DC, Afribone, MLIX and operator offices.

Do not create datacenter records from cybercafes, web-hosting resellers hosted offshore, university labs, bank IT rooms, ordinary NOCs, fibre routes, tower sites or administrative IT offices unless source evidence proves hosting/colo/cloud/compute facility function.
