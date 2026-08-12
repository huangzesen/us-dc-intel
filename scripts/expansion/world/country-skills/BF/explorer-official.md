# BF Explorer Official - Burkina Faso Datacenter Enumeration

Date verified: 2026-08-12. Country: BF - Burkina Faso. Primary angle: official, regulatory, public-procurement, environmental, energy, interconnection, and cloud-provider evidence.

Important boundary note: this explorer preserves the requested legacy **13-region** model for compatibility with the country-skills framework. Burkina Faso's Presidency announced on 2025-07-02 that the country was reorganized from **13 regions / 45 provinces** to **17 regions / 47 provinces**, with endogenous names and a six-month transition. Use both old and new names in current searches. Official source: https://www.presidencedufaso.bf/conseil-des-ministres-du-2-juillet-2025/. The legacy 13 regions are still the required coverage set for this file: Boucle du Mouhoun; Cascades; Centre; Centre-Est; Centre-Nord; Centre-Ouest; Centre-Sud; Est; Hauts-Bassins; Nord; Plateau-Central; Sahel; Sud-Ouest.

Reliability grades:
- **A**: primary source: ministry, Presidency/SIG, ANPTIC, ARCEP, ANEVE/SINADEVE, commune permit, ARMP/DGMP procurement notice, ARSE/SONABEL, official operator facility page, official cloud-provider region page, PeeringDB/PCH interconnection record, BRVM/issuer filing.
- **B**: strong secondary: Data Center Dynamics, Developing Telecoms, Ecofin Agency, AIB, Sidwaya, leFaso.net, Burkina24, Wakat Sera, credible vendor case study, trade association, local media relaying a named official event.
- **C**: weak lead: aggregator directory, market-report snippet, social media, old MoU, launch claim without site/power/permit evidence, "server room" mention without hosting/colo/cloud function.

## 1. Official Source Map

| Source | Verified URL | Use | Grade and cautions |
|---|---|---|---|
| Ministry of Digital Transition, Posts and Electronic Communications (MTDPCE/MDENP legacy domain) | https://www.mdenp.gov.bf/ | Government cloud, national datacenters, NOC, "zero white zones", digital-transformation programs. Search its news detail pages and PDFs. | A for ministry pages; B if only ministry Facebook is available. |
| ANPTIC - Agence Nationale de Promotion des TIC | https://anptic.gov.bf/ | Implements and operates state ICT infrastructure. Its indexed pages include administration datacenter and 2026 modular-datacenter material, but article slugs returned intermittent 404 during liveness checks; use the site search templates below. | A for live ANPTIC pages; B/C for cached snippets until opened. |
| Presidency / SIG | https://www.presidencedufaso.bf/ ; https://www.sig.gov.bf/ ; https://gouvernement.gov.bf/ | Council-of-ministers decisions, administrative divisions, funding decisions, official project announcements. | A for official communiques. |
| ARCEP - telecom regulator | https://www.arcep.bf/ ; licences https://www.arcep.bf/demande-de-licences-2/ ; operator register https://www.arcep.bf/repertoire/ ; licence-list download https://www.arcep.bf/download/liste-des-operateurs-titulaires-de-licence/ | Operator census, neutral licences for ONATEL, Orange Burkina Faso, Telecel, network/frequency authorizations, value-added services. | A for licence/register facts. ARCEP does not by itself prove a datacenter. |
| ANEVE / environmental e-permitting | https://sinadeve.envieau.gov.bf/ | Feasibility and environmental-compliance requests for large facilities, fibre, power, gensets, cooling, waste-to-energy projects. | A when an official notice/EIA is found; portal search may be poor, so also search indexed documents. |
| ARSE - energy regulator | https://www.arse.bf/ | Electricity regulation, tariffs, annual reports, sector decisions. | A for published regulator documents. |
| SONABEL - national utility | Official ministry directory page: https://www.energie-mines.gov.bf/le-ministere/les-structures/details?cHash=eb8e43010d647dc017782d3336c852c2&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=31 | Grid connection, substations, generation, large-consumer and power-quality clues. | A for ministry/utility documents. The standalone SONABEL domain is reported by directories but timed out during curl checks, so do not depend on it without manual verification. |
| ARCOP / procurement (ex-ARMP terminology in older sources) | https://www.arcop.bf/ | Tender and award notices for government datacenters, NOC, fibre and supervision-center works. | A for official tender/award records. |
| BFIX | https://www.bfix.bf/ ; PeeringDB IX https://www.peeringdb.com/ix/2729 ; PeeringDB org https://www.peeringdb.com/org/14212 | IXP presence and local facilities: PeeringDB lists BFIX Ouagadougou at Virtix and legacy facilities "Datacenter Immeuble du Faso" and "Datacenter Ministere de l'agriculture"; peers include Orange, Cloudflare, Meta, VTS, PCH. | A/B for interconnection presence, not enough alone for commercial DC classification. |
| Official cloud region lists | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Negative verification for hyperscaler regions. | A. As verified, no AWS/Azure/GCP/OCI Burkina Faso public cloud region. |

## 2. Official Search Templates

Run French first; English second. Keep quoted French terms because they match government and press usage.

```text
site:mdenp.gov.bf ("datacenter" OR "data center" OR "centre de données" OR "cloud gouvernemental" OR "souveraineté numérique" OR "zéro donnée")
site:anptic.gov.bf ("datacenter" OR "data center" OR "centre de données" OR "cloud gouvernemental" OR hébergement)
site:presidencedufaso.bf OR site:sig.gov.bf OR site:gouvernement.gov.bf ("datacenter" OR "centre de données" OR "cloud gouvernemental" OR "infrastructures numériques" OR NOC)
site:arcep.bf ("liste des opérateurs" OR licence OR "licence technologiquement neutre" OR "infrastructures passives")
site:sinadeve.envieau.gov.bf ("datacenter" OR "centre de données" OR "data center" OR "centre de supervision" OR "groupe électrogène")
site:arse.bf (tarif OR électricité OR SONABEL OR "grand client")
site:sonabel.bf ("datacenter" OR "centre de données" OR "poste de transformation" OR kVA OR MVA)
site:armp.bf ("datacenter" OR "centre de données" OR "cloud gouvernemental" OR NOC OR "centre de supervision")
"Burkina Faso" ("datacenter" OR "centre de données") ("permis de construire" OR "étude d'impact" OR "avis environnemental" OR SONABEL OR ARMP)
```

For each operator/project:

```text
"{operator}" Burkina ("datacenter" OR "data center" OR "centre de données" OR colocation OR hébergement)
"{operator}" Burkina (ARCEP OR licence OR ANEVE OR SINADEVE OR SONABEL OR "permis de construire")
"{operator}" (BFIX OR PeeringDB OR "Ouaga 2000" OR "Avenue de la Dignité" OR "Avenue Kwame Nkrumah")
```

## 3. Officially Verified Seeds and How to Treat Them

| Project/operator | Location signal | Official/primary sources | Grade | Treatment |
|---|---|---|---|---|
| Government Cloud - two modular datacenters | Ouagadougou; exact sites not public in the pages reviewed | MTDPCE construction-progress page: https://www.mdenp.gov.bf/details?cHash=6c732178fee5fa9a762ad626e10a7e3f&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=1015 ; DCD corroboration: https://www.datacenterdynamics.com/en/news/govt-of-burkina-faso-launches-two-mini-data-centers-to-support-data-sovereignty/ ; Connecting Africa: https://www.connectingafrica.com/data-centers/burkina-faso-launches-two-mini-data-centers | A for MTDPCE construction/project existence; B for inauguration/capacity details from trade press unless the ANPTIC article opens live | Count as two government/institutional datacenters only if physical sites are represented separately; otherwise one project with two site records pending addresses. Capacity reported by press: 3 PB storage, 105.6 TB memory, 28,800 CPU cores, 7,000+ VMs; cost around 15.2-16 bn FCFA. |
| ANPTIC / administration datacenter estate | Ouagadougou plus legacy government nodes | ANPTIC site search: https://anptic.gov.bf/ ; older G-Cloud page: https://www.mdenp.gov.bf/details?cHash=4c4f77e8032d813f9cc1a5387eb98c2d&tx_news_pi1%5Baction%5D=detail&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Bnews%5D=124 | A for live agency pages; C/B for legacy node count unless updated | Use to deduplicate legacy MDENP/G-Cloud rooms against the 2026 modular DCs. Do not count each "mini datacenter" mention unless it has a distinct site. |
| Education datacenter / UVBF | Likely Ouagadougou or university-hosted; site must be confirmed | ANPTIC indexed title "LANCEMENT OFFICIEL DU DATACENTER DE L'EDUCATION"; start from https://anptic.gov.bf/ and query `site:anptic.gov.bf "DATACENTER DE L'EDUCATION"` | B until the article opens live; A only for a live ANPTIC page | Specialized education/government DC. Count only if facility-level details are confirmed, not as commercial colo. |
| Digital Infrastructure Supervision Center / NOC | Ouagadougou | Ecofin: https://www.ecofinagency.com/news-digital/2001-52093-burkina-faso-launches-5-4-million-digital-infrastructure-supervision-center ; DCD NOC mention in 2026 gov-DC article | B until official award/permit found | It supervises backbone, cybersecurity and state DCs. Treat as NOC/operations building, not a datacenter unless later evidence shows hosting/compute halls. |
| Virtix Data Center / Virtual Technologies and Solutions SA | Palais des Sports, Ouaga 2000, Ouagadougou | Official site: https://virtix.bf/ ; PeeringDB BFIX facility listing: https://www.peeringdb.com/ix/2729 ; directory lead: https://datacenterplatform.com/data-centers/virtual-technologies-and-solutions-sa/ | A for official location/marketed services; B for PeeringDB interconnect; C for aggregator capacities | Confirmed commercial/carrier-neutral colo lead. Marketing "Tier 3/hyperscale" is self-claimed unless Uptime record is found. |
| IKA Cloud / IKA Solution LTD | Avenue de la Dignite, Cissin/Secteur 26, Ouagadougou | IKA Cloud pricing/services: https://www.ikacloud.bf/princing-package.php?currency=1 ; IKA Solution site: https://ikasolution.bf/ | A for operator address and advertised hosting/colo services; B/C for launch press | Count as a local hosting/colo operator if the physical facility is verified. Flag "premier datacenter" claims as marketing because Virtix predates it. |
| Alink Telecom | Ouagadougou; exact BF site not public in verified official pages | Reported official domain, HTTP only during liveness check: http://www.alinktelecom.net ; directory lead: https://datacenterplatform.com/data-centers/alink-telecom/ | B/C for company domain/directory; C for DataCenterPlatform's two-DC count/location | Use as a lead. Require ARCEP/licence, operator page, BFIX, permit, or customer evidence before final facility status above C. |
| IPSyS TELECOM | Avenue Kwame Nkrumah, Ouagadougou | Official site: https://ipsys-bf.com/ ; Inflect lead: https://inflect.com/datacenters/emea/burkina-faso | A for company site if facility services are shown; C for aggregator | Use as telecom/datacenter lead. Verify whether the listed address is office, PoP or actual DC. |
| Orange Burkina Faso datacenter | Ouagadougou city-level | ARCEP register for Orange licence: https://www.arcep.bf/repertoire/ ; DCD solar article: https://www.datacenterdynamics.com/en/news/orange-deploying-solar-panels-at-data-centers-in-cote-divoire-and-burkina-faso/ | A for licence; B for DC existence/location from DCD | Count as telco-core DC only with a site-level record; no public address found. Solar evidence supports facility existence but not commercial colo. |
| ONATEL / Moov Africa Burkina Faso | Ouagadougou plus exchange/core sites | ARCEP register and licence downloads: https://www.arcep.bf/repertoire/ ; official site https://www.moov-africa.bf/ | A for operator licence; B/C for DC/hosting claims unless filing says facility | Treat as incumbent telco core infrastructure. Do not multiply switch sites into DCs. |
| Telecel Faso | Ouagadougou plus mobile core sites | ARCEP Telecel licence download: https://www.arcep.bf/download/licence-neutre-telecel-s-a/ ; official site https://telecelfaso.bf/ | A for licence; C for inferred DC | Search for named core-network, MSC, switching or hosting facilities before counting. |
| BFIX legacy facilities | Ouagadougou: Immeuble du Faso; Ministere de l'agriculture; Virtix | PeeringDB IX local facilities: https://www.peeringdb.com/ix/2729 | B for network-node presence; C for commercial DC interpretation | Use as legacy facility leads. Verify owner, status and whether the "Ministere de l'agriculture" site is still active. |
| Essor Services + Kaia Energy waste-to-energy datacenter | Burkina Faso; site not public | DCD: https://www.datacenterdynamics.com/en/news/burkina-faso-to-launch-data-center-powered-by-waste-to-energy-plant/ ; WeAreTech: https://www.wearetech.africa/en/fils-uk/news/tech/burkina-faso-to-launch-data-center-powered-by-waste-to-energy-plant | C until permit/EIA/construction evidence | Announced 12 MW waste-to-energy plus DC, target Nov 2025. No official EIA/permit/built evidence found in this review; keep as speculative lead. |

## 4. Regulatory and Permitting Logic

- ARCEP's licence page cites Decret 2010-245/PRES/PM/MPTIC/MEF for licence, authorization and declaration procedures. Licence status is necessary for public electronic communications services but not sufficient to prove a datacenter.
- Use ARCEP to build the operator universe: ONATEL, Orange Burkina Faso, Telecel Faso, PAV-Burkina and other licensed capacity/service providers. Pivot each licensed operator into facility, hosting, colocation and BFIX searches.
- Use ANEVE/SINADEVE for any new build, generator-heavy site, fibre corridor, energy plant or waste-to-energy project. Strong datacenter records should capture EIA facts: proponent, locality, backup generation, fuel storage, cooling/water, land parcel, construction phase.
- Building permits are commune-level and usually not searchable online. For Ouagadougou, search "mairie de Ouagadougou" and district/sector names, then contact the commune for permit confirmation where the record is high value.
- Power sanity checks are mandatory. Extract kVA/MVA/MW, voltage, substation, generator autonomy, UPS topology, fuel storage and solar/PPA evidence. Grade the power field independently from the facility field.

## 5. Region Coverage Strategy - Required 13-Region Model

Use the legacy region name, capital, and the post-2025 endogenous/new names where relevant.

| Legacy region | Capital / current-search aliases | Expected DC yield | Required strategy |
|---|---|---|---|
| Centre | Ouagadougou; new name Kadiogo | High | Exhaustive enumeration. Search Ouaga 2000, Palais des Sports, Cissin, Avenue de la Dignite, Avenue Kwame Nkrumah, Immeuble du Faso, Ministere de l'agriculture, Kossodo, Gounghin, Patte d'Oie. Seeds: gov modular DCs, ANPTIC, Virtix, IKA, Alink, IPSyS, Orange, ONATEL/Moov, Telecel, BFIX. |
| Hauts-Bassins | Bobo-Dioulasso; new name Guiriko | Low-medium | Search telco PoPs/core rooms, BFIX Bobo-Dioulasso, banks, university/server-room leads, SONABEL substations, fibre route to Cote d'Ivoire. Count only named hosting/colo/cloud or carrier facility. |
| Boucle du Mouhoun | Dedougou; post-2025 Bankui and Sourou/Tougan split | Low | Run negative sweep. Add Sourou/Tougan aliases for current records. Watch solar/power and fibre corridors; do not count administrative ICT rooms. |
| Cascades | Banfora; new name Tannounyan | Low | Search Banfora and border/fibre routes to Cote d'Ivoire/Mali. Expect telco edge only. |
| Centre-Est | Tenkodogo; new name Nakambe | Low | Search Tenkodogo, border routes to Togo/Ghana, operator PoPs. |
| Centre-Nord | Kaya; new name Kuilse | Low | Search Kaya, security-related connectivity and government infrastructure. Avoid counting training/ICT offices. |
| Centre-Ouest | Koudougou; new name Nando | Low | Search Universite Norbert Zongo, commune ICT, telco PoPs, SONABEL. |
| Centre-Sud | Manga; new name Nazinon | Low | Negative sweep; search Manga plus government digital projects and operator PoPs. |
| Est | Fada N'Gourma; post-2025 Goulmou plus Sirba/Bogande and Tapoa/Diapaga split | Low | Use old Est and new Goulmou/Sirba/Tapoa aliases. Watch Benin/Niger fibre interconnection and energy projects. |
| Nord | Ouahigouya; new name Yaadga | Low | Search telco coverage/tower projects and operator PoPs; security conditions lower confidence of unsourced claims. |
| Plateau-Central | Ziniare; new name Oubri | Low | Negative sweep; distinguish ICT training/event facilities from datacenters. |
| Sahel | Dori; post-2025 Liptako and Soum/Djibo split | Lowest | Use Dori, Djibo, Liptako, Soum aliases. Treat physical-site claims as low-confidence unless official. |
| Sud-Ouest | Gaoua; new name Djoro | Low | Negative sweep; search Gaoua and border/fibre/power leads. |

Universal per-region query block:

```text
"{legacy region}" Burkina ("datacenter" OR "data center" OR "centre de données" OR colocation OR hébergement)
"{new region/name}" Burkina ("datacenter" OR "centre de données" OR "salle serveur" OR cloud)
"{capital}" Burkina ("datacenter" OR "centre de données" OR "salle serveur" OR hébergement)
"{capital}" Burkina (Orange OR ONATEL OR "Moov Africa" OR Telecel OR BFIX OR ANPTIC) ("datacenter" OR "centre de données" OR PoP OR "point de présence")
"{legacy region}" Burkina ("permis de construire" OR "étude d'impact" OR "avis environnemental") ("datacenter" OR "centre de données" OR "infrastructures numériques")
site:mdenp.gov.bf "{capital}" (datacenter OR "centre de données" OR numérique)
site:anptic.gov.bf "{capital}" (datacenter OR "centre de données" OR RESINA OR cloud)
site:arcep.bf "{capital}" (Orange OR ONATEL OR Telecel OR licence)
```

Exact 13-region quick sweep:

```text
"Boucle du Mouhoun" Burkina ("datacenter" OR "data center" OR "centre de données")
Cascades Burkina (Banfora) ("datacenter" OR "centre de données")
Centre Burkina Ouagadougou ("datacenter" OR "centre de données" OR colocation)
"Centre-Est" Burkina Tenkodogo ("datacenter" OR "centre de données")
"Centre-Nord" Burkina Kaya ("datacenter" OR "centre de données")
"Centre-Ouest" Burkina Koudougou ("datacenter" OR "centre de données")
"Centre-Sud" Burkina Manga ("datacenter" OR "centre de données")
Est Burkina "Fada N'Gourma" ("datacenter" OR "centre de données")
"Hauts-Bassins" Burkina Bobo-Dioulasso ("datacenter" OR "centre de données")
Nord Burkina Ouahigouya ("datacenter" OR "centre de données")
"Plateau-Central" Burkina Ziniare ("datacenter" OR "centre de données")
Sahel Burkina Dori ("datacenter" OR "centre de données")
"Sud-Ouest" Burkina Gaoua ("datacenter" OR "centre de données")
```

Post-2025 alias sweep for current records:

```text
Bankui Dedougou Burkina datacenter
Sourou Tougan Burkina "centre de données"
Goulmou "Fada N'Gourma" Burkina datacenter
Sirba Bogande Burkina "centre de données"
Tapoa Diapaga Burkina datacenter
Liptako Dori Burkina datacenter
Soum Djibo Burkina "centre de données"
Kadiogo Ouagadougou Burkina datacenter
Guiriko Bobo-Dioulasso Burkina datacenter
```

## 6. Cloud-Provider Negative Checks

No official public cloud region in Burkina Faso was found on the major provider region lists checked on 2026-08-12.

| Provider | Official URL | Burkina handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No BF region/local zone listed. Tenant, partner or edge claims do not imply an AWS datacenter in BF. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No BF public cloud region. Edge POP/CDN claims require separate verification and are not facility records. |
| Google Cloud | https://cloud.google.com/about/locations | No BF cloud region/location. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No BF OCI region. |

## 7. Minimum Record Standard

Every candidate facility should carry:
- canonical name and aliases;
- owner/operator and legal entity;
- legacy 13-region attribution plus post-2025 alias when applicable;
- locality, district, street/landmark and coordinates if available;
- status: announced, procurement, permitted, under construction, inaugurated, operational, inactive;
- function: commercial colo, government cloud, education/government, telco core, IXP, NOC, server room, speculative;
- capacity with exact units and field-level grades: racks, sqm, MW/kVA/MVA, storage, CPU cores, RAM, VMs;
- evidence URLs with grades per field;
- dedup notes against ANPTIC/G-Cloud, MDENP legacy, BFIX legacy, operator offices and telco exchanges.

Do not create datacenter records from cybercafes, ordinary web-hosting resellers, offshore hosting, university labs, commune IT offices, "digital hubs", tower sites, fibre routes, or NOC/control rooms unless the source proves hosting/colo/cloud/compute facility function.
