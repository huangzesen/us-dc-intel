# GN Explorer Official - Guinea Datacenter Enumeration

Date verified: 2026-08-12. Country: GN - Guinea. Scope: official, regulatory, procurement, budget, environmental, energy, interconnection, and cloud-provider evidence for datacenter discovery.

## Boundary Model

Use the project-required 8-division working model exactly as `world-manifest.jsonl` names it: Boke; Conakry; Kindia; Faranah; Kankan; Labe; Mamou; Nzerekore. These correspond to Guinea's seven administrative regions plus the special zone/governorate of Conakry. Use the ASCII manifest names for record attribution and keep French/local spellings as aliases.

Division aliases and capitals: Boke/Boké (Boké; Kamsar, Sangaredi/Sangarédi, Boffa, Fria, Gaoual, Koundara); Conakry (Kaloum, Dixinn, Ratoma, Matam, Matoto; Kipe/Kipé and Koloma are Ratoma/Koloma-area signals); Kindia (Kindia; Coyah, Dubreka/Dubréka, Forecariah/Forécariah, Telemele/Télimélé); Faranah (Faranah; Dabola, Dinguiraye, Kissidougou); Kankan (Kankan; Siguiri, Kerouane/Kérouané, Kouroussa, Mandiana); Labe/Labé (Labé; Lelouma/Lélouma, Mali, Koubia, Tougué); Mamou (Mamou; Dalaba, Pita); Nzerekore/Nzérékoré/N'Zérékoré (Nzérékoré; Beyla, Gueckedou/Guéckédou, Lola, Macenta, Yomou).

Guinea remains in a transition-state context. Ministry names and digital portfolios have changed since 2021, so verify the current portfolio on the government portal before grading any ministry identity A. Attribute facilities by physical site, not by the ministry name appearing in an older article.

Boundary and legal sources:
- Project manifest: `/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/world-manifest.jsonl`
- Journal Officiel / SGG: https://journal-officiel.sgg.gov.gn/
- Government portal: https://gouvernement.gov.gn/
- INSTAT: use official statistics publications when reachable; direct homepage access returned 403 in the 2026-08-12 curl check, so do not cite it without a current successful fetch.

## Reliability Grades

- A: primary source: presidency, ministry/agency, ARPT, ANSSI, GUILAB, WARDIP, World Bank, Journal Officiel/SGG, CNT, EDG/ministry power records, official cloud-region lists, PeeringDB/PCH for interconnection facts.
- B: strong secondary: Data Center Dynamics, Agence Ecofin/Ecofin Agency, Connecting Africa, TechAfrica News, Le360 Afrique, and reputable Guinean outlets relaying a named official event or official text: Guineematin, Mediaguinee, Guineenews, Guineeactuelle, AGP, Radio Guinee, Avenirguinee, GuineeSource.
- C: directories/marketplaces, snippets, social media, job posts, paid market reports, MoUs, unverifiable scraped pages, reseller web-hosting offers, or wording such as NOC/server room/landing station without a hosting, colocation, cloud, or compute-facility function.

Grade by field. A facility can have A-grade existence and location but B/C-grade capacity, certification, or operating status. Never promote MW, rack count, Tier certification, coordinates, or owner/operator fields above the source that proves that exact field.

## Official Source Map

| Source | Verified URL | Use | Grade and cautions |
|---|---|---|---|
| Presidency of Guinea | https://presidence.gov.gn/ ; national DC announcement https://presidence.gov.gn/la-guinee-se-dote-de-son-premier-data-center-national-et-du-domaine-gn-une-avancee-majeure-pour-la-souverainete-numerique/ ; council note https://presidence.gov.gn/compte-rendu-de-la-communication-presidentielle-au-conseil-des-ministres-du-27-septembre-2025/ | Official inauguration/mise en service of the Data Center national and `.gn`; Simandou 2040 sovereignty framing. | A for the event and policy framing. The presidency page does not prove sqm, racks, MW, Uptime certification, legal operator, or detailed power design. |
| Government portal / MPTEN | https://gouvernement.gov.gn/ ; MPTEN service-public page https://service-public.gov.gn/mpten/ ; portfolio example https://gouvernement.gov.gn/mpten-la-guinee-prend-une-part-active-a-la-vivatech-2025-a-paris/ | Current ministry identity, digital portfolio, `.gn`, national datacenter, WARDIP oversight. | A for government-portal records. Use government/service-public mirrors when a ministry vanity domain is unreachable. |
| ARPT | https://www.arpt.gov.gn/ ; contact https://www.arpt.gov.gn/contact/ ; presentation https://www.arpt.gov.gn/presentation-de-larpt/ ; law page https://www.arpt.gov.gn/loi-l2016-037-an-relative-a-la-cybersecurite-et-la-protection-des-donnees/ | Regulator, operator universe, interconnection/market documents, ARPT headquarters address at Centre Directionnel de Koloma. | A for ARPT address and regulatory facts. A telecom licence or interconnection catalogue is not datacenter proof. |
| ANSSI | https://anssi.gov.gn/ ; cybersecurity/data law https://anssi.gov.gn/nproject/loi-l037-2016-relative-a-la-cybersecurite-et-la-protection-des-donnees-a-caractere-personnel/ ; WARDIP activity https://anssi.gov.gn/?nproject=transformation-numerique-pour-lafrique-de-louest-dtfa-wardip | Cybersecurity, personal-data law, CERT/cyber capacity, WARDIP safeguards/training. | A for agency/law/activity facts. Cybersecurity activity is context, not facility evidence. |
| GUILAB - La Guineenne de Large Bande SA | https://guilab.com.gn/a-propos/ ; Data Center & VAS https://guilab.com.gn/data-center-vas/ ; colocation https://guilab.com.gn/colsalisation/ ; cloud https://guilab.com.gn/cloud/ | State/PPP infrastructure operator; ACE capacity/landing-station operation; confirmed data-center, colocation, cloud, MMR/COLOC details at Centre Emetteur de Kipe, Ratoma. | A for facility existence, address, 228.91 m2, room functions, 2 x 400 kVA generators, batteries, cooling/security details as stated by GUILAB. ISO 9001 is A for GUILAB operations, not a Tier/Uptime certification. |
| WARDIP Guinea / World Bank | https://www.wardip-guinee.org.gn/ ; https://www.wardip-guinee.org.gn/en_GB/wardip ; World Bank release https://www.banquemondiale.org/fr/news/press-release/2023/12/01/accelerating-digital-transformation-in-west-africa | Regional digital integration, broadband, backbone, cable, CERT/e-government context. | A for project facts. Do not infer datacenter funding or site location unless a WARDIP procurement/document names it. |
| CNT | https://cnt.gov.gn/ ; MPTEN LFI 2025 https://cnt.gov.gn/lfi-2025-postes-telecommunication/ ; APDP bill https://cnt.gov.gn/personnel-apdp/ | Laws, ratifications, budgets, APDP/personal-data authority. | A for CNT records. Search budget/procurement vocabulary before adding state-cloud records. |
| Journal Officiel / SGG | https://journal-officiel.sgg.gov.gn/ | Legal texts, decrees, telecom/cyber/electricity/procurement framework. | A for published legal text. Laws do not prove facilities. |
| IXP-GUINEE / PeeringDB | PeeringDB IX https://www.peeringdb.com/ix/2520 ; org https://www.peeringdb.com/org/21637 | IXP-GUINEE in Conakry; PeeringDB showed 4 peers / 4 connections / 3G total capacity in the 2026-08-12 check. | A/B for interconnection facts. An IXP is not a datacenter by itself. |
| Official cloud-region lists | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Negative check for hyperscaler regions/local zones. | A. No AWS, Azure, Google Cloud, or OCI public cloud region/local zone in Guinea found on 2026-08-12. |
| NIC.GN / IANA | IANA `.gn` record to verify during record creation; NIC.GN association appears in official/press launch coverage. | ccTLD registry and `.gn` repatriation. | B until a stable official NIC.GN/IANA citation is attached to the record. DNS registry hosting may be a workload, not a separate facility. |
| EDG / Energy ministry | Search official EDG/ministry releases and procurement. TIC/EDG aggregator: https://tic-guinee.net/electricite-de-guinee/ | Grid, substations, load shedding, gensets, utility connection. | A only for official utility/ministry documents; press/aggregator relays are B/C. Power must be graded separately from facility existence. |

## Official Search Templates

Use separate queries per domain; `site:a OR site:b` is unreliable.

```text
site:presidence.gov.gn ("data center" OR datacenter OR "centre de donnees" OR "centre de données" OR ".gn" OR "mise en service" OR Simandou)
site:gouvernement.gov.gn (MPTEN OR "Postes" OR "Télécommunications" OR numerique OR numérique OR WARDIP OR "data center" OR ".gn")
site:service-public.gov.gn/mpten (datacenter OR "data center" OR "centre de données" OR WARDIP OR ".gn")
site:www.arpt.gov.gn (operateur OR opérateur OR licence OR interconnexion OR "catalogue" OR "produits et services des FAI" OR "data center")
site:anssi.gov.gn (WARDIP OR CERT OR "protection des données" OR "data center" OR cloud OR hébergement)
site:guilab.com.gn ("Data Center" OR Colocation OR Colocalisation OR Cloud OR MMR OR COLOC OR Kipe OR Kipé)
site:cnt.gov.gn (datacenter OR "data center" OR "centre de données" OR MPTEN OR WARDIP OR APDP OR budget OR hébergement)
site:wardip-guinee.org.gn (datacenter OR "data center" OR cable OR câble OR backbone OR fibre OR CERT OR cloud OR hébergement)
site:journal-officiel.sgg.gov.gn (telecommunications OR télécommunications OR numerique OR numérique OR cybersecurite OR cybersécurité OR "protection des données" OR electricite OR électricité)
```

Operator pivots:

```text
"{operator}" Guinée (datacenter OR "data center" OR "centre de données" OR colocation OR colocalisation OR cloud OR hébergement OR MMR OR COLOC)
"{operator}" Guinée (ARPT OR licence OR interconnexion OR EDG OR "poste électrique" OR kVA OR MVA OR UPS OR "groupe électrogène")
"{operator}" (IXP-GUINEE OR PeeringDB OR "196.60.61" OR Conakry OR Kipé OR Koloma OR Ratoma)
```

## Officially Verified Seeds

| Candidate | Physical attribution | Best verified URLs | Grade | Handling |
|---|---|---|---|---|
| GUILAB Data Center / colocation / private cloud | Conakry division; Ratoma commune; Centre Emetteur de Kipe/Kipé | https://guilab.com.gn/data-center-vas/ ; https://guilab.com.gn/colsalisation/ ; https://guilab.com.gn/cloud/ ; https://guilab.com.gn/a-propos/ | A for operator, facility/service existence, address, 228.91 m2, MMR/COLOC/Pylone rooms, 2 x 400 kVA generators, battery autonomy, cooling and security details as operator-stated. | Record as a confirmed commercial/operator data-center facility. Unknowns: rack count, IT load/MW, exact coordinates, commissioning date, tenant list, certifications beyond GUILAB's ISO 9001 claim. Dedupe against ACE landing station and IXP-GUINEE because they may be in/near the same Kipe site. |
| Data Center National / national datacenter / `.gn` launch | Conakry division; ARPT building at Kipe/Koloma, Ratoma/Conakry | Presidency announcement above; presidency council note above; GuineeSource https://guineesource.com/guinee-lancement-du-domaine-national-gn-et-inauguration-du-data-center-tier-iii/ ; Guineematin https://guineematin.com/2025/09/04/conakry-la-guinee-lance-le-domaine-gn-inaugure-le-data-center-national-et-annonce-une-baisse-du-cout-de-la-data-avec-orange/ ; Le360 exploitation article https://afrique.le360.ma/economie/guinee-mise-en-exploitation-du-data-center-au-coeur-dune-infrastructure-qui-ne-doit-jamais-cesser-de_PY7Q5T6ATZBRJPOCYH4VSSS444/ | A for inauguration/mise en service from presidency. B for exact Kipe location, 600 m2, Tier III wording, and later exploitation commentary unless official engineering documents are found. | Record as state/government datacenter, status inaugurated/mise en service. Treat operation at scale as partial/transitioning if using Le360 only. Unknowns: legal operator, owner, funding source, racks/MW, Uptime certificate, production cutover, customer/workload list. |
| `.gn` / NIC.GN registry workload | Conakry likely; physical hosting not independently proved | Presidency and Guineematin launch coverage; verify IANA `.gn` before record creation. | B for launch/repatriation; A only after official NIC/IANA confirmation. | Do not create a separate datacenter record. Attach as workload/context to the national DC only if a source proves physical hosting there. |
| IXP-GUINEE | Conakry | https://www.peeringdb.com/ix/2520 ; https://www.peeringdb.com/org/21637 | A/B for IX facts; C for any host-site inference. | Interconnection object and discovery pivot; do not count as a datacenter unless a facility host is named. |
| ACE landing station / GUILAB infrastructure | Conakry division; Kipe/Ratoma | https://guilab.com.gn/a-propos/ ; Ecofin ACE/ISO articles as secondary corroboration | A for GUILAB/ACE role and address. | Landing-station function is separate from the GUILAB data-center service; dedupe carefully at the Kipe site. |
| WARDIP digital infrastructure | National scope; sites TBD | WARDIP and World Bank URLs above | A for programme facts; C for facility inference. | Track for second cable, national backbone, CERT/e-government and procurement notices. Do not assert WARDIP funded the national DC without a source. |
| Telecom operators: Orange Guinee, MTN Guinee, Cellcom, Guinee Telecom/Sotelgui, MOUNA, Leader Net, VDC Telecom | Mostly Conakry network cores; sites unverified | ARPT records; GUILAB customer/partner logos; PeeringDB for MOUNA; operator sites | A/B for licence/operator facts; C for datacenter inference. | Build operator universe from ARPT and GUILAB/PeeringDB, then search for colocated equipment, MSC/NOC/core, enterprise cloud, and power/site evidence. |
| Banks and state platforms | Conakry cores likely; DR sites unverified | BCRG/commercial-bank annual reports and procurement only | C leads. | Count only with named DR/hosting/server-facility evidence. |
| Mining/industrial IT | Boke, Kindia, Kankan, Labe, Nzerekore depending on physical mine/rail/port site | Company pages and permits | C leads. | Control rooms/SCADA/camp IT are plausible but not datacenters unless a source proves hosting/compute facility function. |

## Regulatory And Permitting Logic

- Telecom: ARPT identifies operators, ISPs, interconnection obligations and market catalogues. Use it to build the universe; do not equate licences, towers, NOCs, MSCs or fibre PoPs with datacenters.
- Cyber/data: Loi L/2016/037/AN and ANSSI explain sovereignty/localization pressure. A dedicated personal-data authority (APDP) was under CNT review; treat this as regulatory context, not facility proof.
- Procurement/budget: search CNT, WARDIP, Journal Officiel and official procurement portals for `appel d'offres`, `attribution`, `marché`, `fourniture`, `installation`, `hébergement`, `cloud gouvernemental`, `centre de données`, `groupe électrogène`, `UPS`, `climatisation de précision`.
- Energy: record power separately. For GUILAB, operator page states public grid, 2 x 400 kVA generators, 72-hour batteries, precision cooling 1+1. For the national DC, press describes energy redundancy and Le360 reports two incoming city power lines plus generators; keep those B until official engineering evidence appears.
- Environment/building permits: Conakry commune permits and EIES are poorly indexed. Search by commune/quartier plus contractor/vendor and power/cooling terms.
- Important correction: the FratMat article titled `construction-du-data-center-national-les-travaux-vont-durer-pres-de-24-mois` is about Cote d'Ivoire, not Guinea. Do not use it for GN.

## 8-Division Coverage Strategy

| Division | Capital / aliases | Expected yield | Official strategy |
|---|---|---|---|
| Boke | Boké; Boke; Kamsar; Sangaredi/Sangarédi; Boffa; Fria; Gaoual; Koundara | Low to medium | Search bauxite/alumina/port IT at CBG, GAC, SMB-Winning, RUSAL Friguia. Require named facility evidence; otherwise record as mining IT lead or negative coverage. |
| Conakry | Conakry; Kaloum; Dixinn; Ratoma; Kipe/Kipé; Koloma; Matam; Matoto | High | Exhaustive pass. Confirmed seeds: GUILAB Data Center at Centre Emetteur de Kipe and Data Center National at ARPT building. Also sweep IXP-GUINEE, ARPT, ANSSI, MPTEN, Orange, MTN, Cellcom, Guinee Telecom, MOUNA, Leader Net, banks, EDG/power. |
| Kindia | Kindia; Coyah; Dubreka/Dubréka; Forecariah/Forécariah; Telemele/Télimélé | Low | Search CBK/RUSAL bauxite, Conakry-Kindia fibre/PoPs, Kaleta/Souapiti power context. No confirmed DC evidence in reviewed sources. |
| Faranah | Faranah; Dabola; Dinguiraye; Kissidougou | Very low | Negative sweep mandatory; search regional administration, telecom PoPs, university/bank server rooms only as C leads. |
| Kankan | Kankan; Siguiri; Kerouane/Kérouané; Kouroussa; Mandiana | Low to medium | Search AngloGold Siguiri, Nordgold Bouly, Simandou/WCS Kerouane control rooms and telecom PoPs. Do not infer DCs from mine automation. |
| Labe | Labé; Labe; Lelouma/Lélouma; Mali; Koubia; Tougué | Low | Search Lefa/Nordgold attribution carefully, administration/university/bank IT and Fouta connectivity. No confirmed DC evidence in reviewed sources. |
| Mamou | Mamou; Dalaba; Pita | Very low | Negative sweep; transit-corridor telecom PoPs only. |
| Nzerekore | Nzérékoré; Nzerekore; N'Zérékoré; Beyla; Gueckedou/Guéckédou; Lola; Macenta; Yomou | Low | Search Simandou South/Simfer Beyla, border connectivity toward Liberia/Cote d'Ivoire and industrial control rooms. No commercial DC evidence in reviewed sources. |

Per-division query block:

```text
"{division}" Guinée (datacenter OR "data center" OR "centre de donnees" OR "centre de données" OR colocation OR colocalisation OR hébergement OR cloud)
"{capital}" Guinée ("salle serveur" OR "point de presence" OR PoP OR NOC OR "centre de données" OR datacenter)
"{capital}" Guinée (Orange OR MTN OR Cellcom OR "Guinée Telecom" OR GUILAB OR MOUNA OR LeaderNet) (datacenter OR colocation OR cloud OR PoP OR NOC)
"{division}" Guinée (EIES OR EDG OR "poste électrique" OR "groupe électrogène" OR UPS OR kVA OR MVA) (datacenter OR "centre de données" OR numerique OR numérique)
site:www.arpt.gov.gn "{capital}" (operateur OR opérateur OR licence OR agrement OR agrément OR interconnexion)
```

Exact 8-division sweep:

```text
(Boké OR Boke OR Kamsar OR Sangarédi OR Sangaredi) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR SCADA OR "salle serveur")
Conakry Guinée (datacenter OR "data center" OR "centre de données" OR colocation OR ARPT OR GUILAB OR IXP-GUINEE OR "data center national")
Kindia Guinée (datacenter OR "centre de données" OR colocation OR PoP OR CBK OR bauxite OR Kaleta OR Souapiti)
Faranah Guinée (datacenter OR "centre de données" OR colocation OR PoP OR "salle serveur")
(Kankan OR Siguiri OR Kérouané OR Kerouane) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR AngloGold OR Simandou OR WCS)
(Labé OR Labe OR Lélouma OR Lelouma) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR Lefa OR Nordgold)
Mamou Guinée (datacenter OR "centre de données" OR colocation OR PoP OR "salle serveur")
(Nzérékoré OR Nzerekore OR N'Zérékoré OR Beyla) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR Simfer OR Simandou)
```

## Cloud-Provider Negative Checks

No Guinea public cloud region or local zone was found in the official AWS, Azure, Google Cloud, or Oracle OCI region/location lists checked on 2026-08-12. Africa-listed regions in these sources are South Africa for AWS/Azure/OCI, Morocco and South Africa for OCI, and the current Google Cloud global locations page lists 43 regions without a Guinea region.

Rules:
- CDN cache, customer, reseller, marketplace, or Outposts/private-cloud deployments do not imply a hyperscaler datacenter in Guinea.
- GUILAB partner logos or IXP peers are interconnection/service evidence only; verify physical facility before counting a separate record.
- Web hosting sold to Guinea from France, Senegal, Cote d'Ivoire, or elsewhere is offshore unless a Guinea site is named and evidenced.

## Minimum Record Standard

Every candidate facility record must carry: canonical name and aliases; owner/operator/legal entity; 8-division attribution using manifest names; Conakry commune/quartier where relevant; locality/address/coordinates when sourceable; status; function; facility/equipment capacity with per-field grades; power evidence; source URLs; dedupe notes.

Do not create datacenter records from cybercafes, web-hosting resellers, university labs, ordinary bank IT rooms, tower sites, landing stations, fibre routes, government offices, NOCs, MSCs, or mining control rooms unless source evidence proves hosting/colocation/cloud/compute facility function.
