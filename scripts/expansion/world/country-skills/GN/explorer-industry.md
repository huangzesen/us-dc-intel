# GN Explorer Industry - Guinea Datacenter Discovery

Date verified: 2026-08-12. Scope: industry media, operator pages, vendor pages, directories, IX/peering records, mining-sector IT, and local press for Guinea datacenter enumeration.

## Boundary And Attribution

Primary project attribution uses the project-required 8-division working model from `world-manifest.jsonl`: Boke; Conakry; Kindia; Faranah; Kankan; Labe; Mamou; Nzerekore. Use those ASCII division names in records; keep French/local spellings as aliases.

Aliases: Boke/Boké (Boké, Kamsar, Sangaredi/Sangarédi, Boffa, Fria); Conakry (Kaloum, Dixinn, Ratoma, Kipe/Kipé, Koloma, Matam, Matoto); Kindia (Kindia, Coyah, Dubreka/Dubréka, Forecariah/Forécariah, Telemele/Télimélé); Faranah (Faranah, Dabola, Dinguiraye, Kissidougou); Kankan (Kankan, Siguiri, Kerouane/Kérouané, Kouroussa, Mandiana); Labe/Labé (Labé, Lelouma/Lélouma, Mali, Koubia, Tougué); Mamou (Mamou, Dalaba, Pita); Nzerekore/Nzérékoré/N'Zérékoré (Nzérékoré, Beyla, Gueckedou/Guéckédou, Lola, Macenta, Yomou).

## Reliability Grades

- A: official operator facility/service pages; government/ministry/ARPT/ANSSI/WARDIP/EDG records; presidency records; official cloud-provider region lists; PeeringDB/PCH for interconnection facts.
- B: credible trade/local press, including Data Center Dynamics, Agence Ecofin/Ecofin Agency, Connecting Africa, TechAfrica News, Le360 Afrique, Guineematin, Mediaguinee, Guineenews, Guineeactuelle, AGP, Radio Guinee, Avenirguinee, GuineeSource, when the article names the source/event.
- C: DataCenterMap, Datacenters.com, Data Center Platform, colocation marketplaces, goafricaonline, snippets, social posts, paid market reports, job posts, unsupported MoUs, and any page without address/operator/power/status evidence.

Field-level grading is mandatory. Directory MW/rack/sqm/Tier/coordinates remain C unless confirmed by an operator, official permit, procurement, utility, or engineering source.

## Market Reality

- Guinea now has two high-confidence Conakry data-center seeds: GUILAB's operator-published data-center/colocation/cloud service at Centre Emetteur de Kipe, and the state Data Center National inaugurated/mis en service with the `.gn` domain in September 2025 at the ARPT building in the Kipe/Koloma/Ratoma area.
- GUILAB is the strongest operator-grade facility source. Its own pages state a 228.91 m2 data center with Pylone, Meet-Me Room and COLOC rooms, two 96-fibre links between MMR and COLOC, public-grid plus 2 x 400 kVA generators, 72-hour batteries, ASHRAE temperature range, precision cooling 1+1, FM200 fire suppression, access control, 24/7/365 support, colocation and private-cloud services.
- The national DC is official as an inaugurated/mise-en-service state asset, but capacity and certification are less firm. Presidency confirms the event and sovereignty framing; press gives Kipe/ARPT location, 600 m2 and Tier III wording; Le360 later describes exploitation/maintenance discussions and energy challenges. Treat Tier III as a claim until Uptime/engineering proof appears.
- Connectivity remains Conakry/Kipe-centered: ACE landing station/GUILAB, IXP-GUINEE, operator cores, and future Medusa/second-cable work under WARDIP or related agreements. A landing station, IXP, or NOC is not automatically a datacenter.
- Outside Conakry, expected evidence is mostly mining/industrial IT, telecom PoPs and public-administration server rooms. No commercial colocation facility outside Conakry was verified in this review.
- No AWS, Azure, Google Cloud or OCI public cloud region/local zone in Guinea was found in official lists on 2026-08-12.

## Industry Source Triage

| Source | Verified route | Use | Grade |
|---|---|---|---|
| GUILAB official site | https://guilab.com.gn/data-center-vas/ ; https://guilab.com.gn/colsalisation/ ; https://guilab.com.gn/cloud/ ; https://guilab.com.gn/a-propos/ | Primary operator evidence for Conakry/Kipe colocation, cloud, MMR/COLOC, power and security. | A for operator-stated facts. |
| Presidency | https://presidence.gov.gn/la-guinee-se-dote-de-son-premier-data-center-national-et-du-domaine-gn-une-avancee-majeure-pour-la-souverainete-numerique/ ; https://presidence.gov.gn/compte-rendu-de-la-communication-presidentielle-au-conseil-des-ministres-du-27-septembre-2025/ | Official national DC and `.gn` launch/mise en service. | A for event/status framing; no detailed capacity. |
| Guineematin | https://guineematin.com/2025/09/04/conakry-la-guinee-lance-le-domaine-gn-inaugure-le-data-center-national-et-annonce-une-baisse-du-cout-de-la-data-avec-orange/ | Minister/event quotes for 600 m2, Tier III claim, Orange tariff cut, NIC.GN. | B; article reachable 200. |
| GuineeSource | https://guineesource.com/guinee-lancement-du-domaine-national-gn-et-inauguration-du-data-center-tier-iii/ | Pre-event Kipe/ARPT location and launch date. | B; curl returned 406 but browser/search could fetch. |
| Le360 Afrique | https://afrique.le360.ma/economie/guinee-mise-en-exploitation-du-data-center-au-coeur-dune-infrastructure-qui-ne-doit-jamais-cesser-de_PY7Q5T6ATZBRJPOCYH4VSSS444/ | March 2026 exploitation/maintenance and power-context article for the national DC. | B. |
| TechAfrica News | https://techafricanews.com/2025/09/05/guinea-launches-national-domain-gn-and-unveils-first-tier-iii-data-center/ | English-language corroboration of launch, partners and Orange tariff cut. | B. |
| Mediaguinee / GuineeActuelle / Alwihda | https://mediaguinee.com/2025/09/la-guinee-lance-son-domaine-gn-et-inaugure-son-data-center-lhebergement-de-nos-donnees-a-letranger-coutait-plus-de-5-millions-de-dollars-par-a/ ; https://guineeactuelle.com/innovation-conakry-inaugure-son-premier-data-center-et-lance-le-gn ; https://www.alwihdainfo.com/Guinee-le-pays-se-dote-de-son-premier-Data-Center-national-et-du-domaine-GN_a143999.html | Secondary corroboration of national DC launch. | B/C depending on detail and direct sourcing. |
| Agence Ecofin / Ecofin Agency | ACE station https://www.agenceecofin.com/equipement/0206-20438-la-guinee-inaugure-sa-station-d-atterrissement-du-cable-sous-marin-de-fibre-optique-aujourd-hui ; GUILAB ISO https://www.agenceecofin.com/operateur/1105-47284-guilab-1er-operateur-certifie-iso-9001-2015-en-guinee ; Sotelgui https://www.agenceecofin.com/telecom/1809-80338-guinee-la-relance-de-l-operateur-historique-sotelgui-toujours-dans-les-projets-du-gouvernement ; Medusa 2026 https://www.ecofinagency.com/news-digital/2804-55061-guinea-eyes-medusa-subsea-cable-for-second-internet-link-mou-due-may-6 | Telecom/cable/operator context. | B; some agenceecofin pages return 403 to curl but are indexed. |
| Connecting Africa / Medusa SCS | https://www.connectingafrica.com/connectivity/guinea-joins-medusa-africa-submarine-cable ; https://medusascs.com/news/guinea-seals-its-alliance-with-medusa-submarine-cable-system-for-a-second-submarine-cable/ | 2026 Medusa/second-submarine-cable context. | B for trade/vendor cable facts; not DC evidence. |
| PeeringDB | https://www.peeringdb.com/ix/2520 ; https://www.peeringdb.com/org/21637 | IXP-GUINEE facts; peers/connections/capacity. | A/B for interconnection; user-maintained. |
| DataCenterMap / Data Center Platform / Colocation marketplaces | https://www.datacentermap.com/guinea/ ; https://www.datacentermap.com/guinea/conakry/guilab-data-center/ ; https://datacenterplatform.com/data-centers/guilab/ | Discovery and cross-checking for GUILAB. | C. DatacenterMap returned 429 in curl; directory values must not override GUILAB official pages. |
| goafricaonline / Guinea Check | MOUNA directory https://www.goafricaonline.com/gn/200248-mouna-group-technology-fournisseur-acces-internet-conakry-guinee ; fact-check https://www.guineecheck.org/2025/03/mouna-group-technology-premier-fournisseur-dinternet-en-guinee-rien-ne-le-prouve/ | ISP discovery and caution against unverified "first ISP" claims. | C for directory; B for fact-check. |
| Leadernet | https://leadernet-gn.com/ | ISP services mention colocation/hosting/cloud; no physical facility proof in reviewed page. | C lead until address/power/facility evidence is found. |
| WARDIP / World Bank | https://www.wardip-guinee.org.gn/ ; https://www.wardip-guinee.org.gn/en_GB/wardip ; https://www.banquemondiale.org/fr/news/press-release/2023/12/01/accelerating-digital-transformation-in-west-africa | Digital-infrastructure context. | A for programme, C for facility inference. |
| FratMat article in draft | https://www.fratmat.info/article/239657/economie/construction-du-data-center-national-les-travaux-vont-durer-pres-de-24-mois | Not a Guinea source; it concerns Cote d'Ivoire. | Do not use for GN. |

## Trade And Operator Query Blocks

```text
site:guilab.com.gn ("Data Center" OR Colocation OR Colocalisation OR Cloud OR MMR OR COLOC OR kVA OR ASHRAE OR FM200)
site:datacenterdynamics.com/en/news/ (Guinea OR Guinée) (datacenter OR "data center" OR cloud OR telecom OR Sotelgui OR "Guinée Telecom")
site:connectingafrica.com (Guinea OR Guinée) (datacenter OR "data center" OR cable OR fibre OR cloud OR Medusa)
site:agenceecofin.com (Guinée OR Guinea) (datacenter OR "data center" OR fibre OR cable OR câble OR cloud OR GUILAB OR Sotelgui)
site:ecofinagency.com Guinea (datacenter OR "data center" OR cable OR fibre OR Medusa OR cloud)
site:techafricanews.com Guinea (datacenter OR "data center" OR "digital sovereignty" OR "Tier III")
site:guineematin.com (datacenter OR "data center" OR "centre de données" OR GUILAB OR WARDIP OR ARPT OR ANSSI)
site:mediaguinee.com (datacenter OR "data center" OR "centre de données" OR GUILAB OR WARDIP)
site:guineenews.org (datacenter OR "data center" OR "centre de données" OR cable OR câble OR WARDIP OR ARPT)
site:guineeactuelle.com (datacenter OR "data center" OR "centre de données" OR ".gn")
site:agpguinee.com (datacenter OR "data center" OR telecom OR télécom OR numérique OR "centre de données")
site:radioguinee.com (datacenter OR "data center" OR cable OR câble OR WARDIP)
site:avenirguinee.org (WARDIP OR data OR numérique OR cable OR câble)
site:tic-guinee.net (datacenter OR "data center" OR EDG OR ARPT OR GUILAB OR "groupe électrogène")
"Guinée" OR "Guinea" (datacenter OR "data center" OR "centre de données") (MW OR racks OR m2 OR "m²" OR kVA OR colocation OR "Tier III" OR Uptime)
```

Operator-specific:

```text
GUILAB OR "La Guinéenne de Large Bande" Guinée (datacenter OR "data center" OR colocation OR colocalisation OR cloud OR MMR OR COLOC OR "Centre Emetteur de Kipé")
"Orange Guinée" Conakry (datacenter OR "data center" OR colocation OR cloud OR NOC OR MSC OR "hébergement")
"MTN Guinée" (datacenter OR "data center" OR colocation OR cloud OR NOC OR MSC OR "hébergement")
Cellcom OR "Guinée Telecom" OR Sotelgui (datacenter OR "data center" OR colocation OR cloud OR NOC OR MSC OR relance)
MOUNA OR "Mouna Group" Guinée (datacenter OR "data center" OR colocation OR cloud OR hébergement OR PeeringDB)
Leadernet OR "Leader Net" Guinée (colocation OR cloud OR hébergement OR datacenter OR "data center")
IXP-GUINEE OR "Point d'échange Internet" Guinée (Conakry OR peers OR GUILAB OR MOUNA OR PCH)
```

## Operator And Project Seeds

| Seed | Location signal | Grade | Handling |
|---|---|---|---|
| GUILAB Data Center | Centre Emetteur de Kipe, Ratoma, Conakry | A for facility/service and specific operator-stated specs. | Primary confirmed commercial/operator record. Record 228.91 m2, MMR/COLOC/Pylone, 2 x 400 kVA generators, battery autonomy, cooling/security as A operator-stated fields. Rack/MW unknown. |
| Data Center National | ARPT building, Kipe/Koloma, Ratoma, Conakry | A for launch/mise en service; B for location/capacity/Tier wording. | State/government DC record. Keep legal operator, exact power design, certification and workload cutover as unknown unless official evidence is found. |
| GUILAB ACE landing station | Centre Emetteur de Kipe, Conakry | A for landing-station operation via GUILAB; B via Ecofin corroboration. | Connectivity asset and possible co-site with GUILAB DC; do not double-count as a separate datacenter unless facility boundary is clear. |
| IXP-GUINEE | Conakry; host site not firmly listed in PeeringDB | A/B for IX facts. | Interconnection object; not a DC. Use peers as operator leads. |
| Orange Guinee | Conakry/national | A for licensed operator when sourced from ARPT; B for 2025 launch-event tariff cut. | Search for enterprise hosting/core/NOC evidence. Do not infer DC from Orange Digital Center training/incubator facility. |
| MTN Guinee, Cellcom, Guinee Telecom/Sotelgui | Conakry/national | A/B for operator status; C for facility inference. | Search ARPT catalogues, interconnection docs, MSC/NOC terms, and power/site references. Legacy Sotelgui assets require current operational proof. |
| MOUNA Group Technology | Conakry ISP/IX peer | A/B for PeeringDB presence; C for directory-only claims. | Hosting/colo lead. Do not repeat "first ISP" without proof. |
| Leadernet | Conakry/national ISP | C lead. | Its site advertises colocation/hosting/cloud services, but reviewed evidence did not prove a physical data-center site. |
| Banks / BCRG / fintech | Conakry likely | C leads. | Look for DR/BCP/server-room tenders and audit/annual-report disclosures. |
| Mining IT: CBG, GAC, SMB-Winning, RUSAL Friguia/CBK, Simandou Simfer/WCS, AngloGold Siguiri, Nordgold Lefa | Boke, Kindia, Kankan, Labe, Nzerekore depending on physical site | C leads. | Industrial control rooms, SCADA and camp IT are not datacenters without named facility/hosting evidence. |

## Region-By-Region Industry Strategy

| Division | Capital and aliases | Industry sweep |
|---|---|---|
| Boke | Boké/Boke; Kamsar; Sangaredi/Sangarédi; Boffa; Fria; Gaoual; Koundara | Search CBG/GAC/SMB-Winning/RUSAL industrial IT, port systems at Kamsar, operator PoPs and power. Expect no commercial DC; write negative coverage unless named facility evidence appears. |
| Conakry | Conakry; Kaloum; Dixinn; Ratoma; Kipe/Kipé; Koloma; Matam; Matoto | Full sweep. Confirmed seeds: GUILAB Data Center and Data Center National. Also sweep GUILAB/ACE, IXP-GUINEE, ARPT, ANSSI, Orange, MTN, Cellcom, Guinee Telecom, MOUNA, Leadernet, banks, EDG/power. |
| Kindia | Kindia; Coyah; Dubreka/Dubréka; Forecariah/Forécariah; Telemele/Télimélé | Search CBK/RUSAL, Konkoure/Kaleta/Souapiti power context and corridor PoPs. No verified DC in reviewed sources. |
| Faranah | Faranah; Dabola; Dinguiraye; Kissidougou | Negative sweep; regional administration, telecom PoPs, bank/university server rooms only as C leads. |
| Kankan | Kankan; Siguiri; Kerouane/Kérouané; Kouroussa; Mandiana | Search AngloGold Siguiri, Nordgold Bouly, Simandou/WCS Kerouane, telecom PoPs and bank/administration IT. |
| Labe | Labé/Labe; Lelouma/Lélouma; Mali; Koubia; Tougué | Search Lefa/Nordgold attribution carefully plus regional administration/university IT. Negative sweep expected. |
| Mamou | Mamou; Dalaba; Pita | Negative sweep; transit-corridor PoPs only. |
| Nzerekore | Nzérékoré/Nzerekore/N'Zérékoré; Beyla; Gueckedou/Guéckédou; Lola; Macenta; Yomou | Search Simandou South/Simfer Beyla, border connectivity to Liberia/Cote d'Ivoire, telecom PoPs and industrial control rooms. |

Exact quick queries:

```text
Conakry Guinée (datacenter OR "data center" OR "centre de données" OR colocation OR ARPT OR GUILAB OR IXP-GUINEE OR "data center national")
(Boké OR Boke OR Kamsar OR Sangarédi OR Sangaredi) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR SCADA OR CBG OR GAC OR "SMB-Winning")
Kindia Guinée (datacenter OR "centre de données" OR colocation OR PoP OR CBK OR Kaléta OR Souapiti)
Faranah Guinée (datacenter OR "centre de données" OR colocation OR PoP OR "salle serveur")
(Kankan OR Siguiri OR Kérouané OR Kerouane) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR AngloGold OR WCS OR Simandou)
(Labé OR Labe OR Lélouma OR Lelouma) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR Lefa OR Nordgold)
Mamou Guinée (datacenter OR "centre de données" OR colocation OR PoP OR "salle serveur")
(Nzérékoré OR Nzerekore OR Beyla) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR Simfer OR Simandou)
```

## Cloud, CDN And Edge Handling

Official negative-check queries:

```text
site:aws.amazon.com/about-aws/global-infrastructure (Guinea OR Guinée)
site:aws.amazon.com/about-aws/global-infrastructure/localzones (Guinea OR Guinée)
site:learn.microsoft.com/en-us/azure/reliability/regions-list (Guinea OR Guinée)
site:cloud.google.com/about/locations (Guinea OR Guinée)
site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm (Guinea OR Guinée)
"Guinée" ("AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region" OR "OCI region")
```

Rules:
- Hyperscaler customer, partner, CDN cache, reseller, marketplace, private cloud, or edge PoP claims do not prove a Guinea hyperscaler region or datacenter campus.
- IXP peers prove interconnection at the IXP, not separate hyperscaler facilities.
- Offshore web hosting marketed to Guinean customers is not a Guinea facility unless a Guinea physical site is named and evidenced.

## Evidence Escalation Rules

- Announcement/MoU: C or B depending on source; never operational without service, inauguration, commissioning or customer evidence.
- Construction/procurement: A/B when official procurement, CNT, WARDIP, ministry, operator, utility or contractor records identify the site and work.
- Operational: A/B when an operator service page, official mise en service, customer terms, facility photos/specs, PeeringDB facility relation, utility energization or audited filing exists. GUILAB is A operator-stated; national DC is A for mise en service but B for exploitation detail.
- Capacity: GUILAB 228.91 m2 and 2 x 400 kVA are A operator-stated; national DC 600 m2 and Tier III are B until official specs/certificates; directory values stay C.
- Dedupe before counting: GUILAB Data Center, ACE landing station and IXP-related equipment may share the Kipe estate; the national DC is at/near ARPT Kipe/Koloma and may host `.gn` or state-cloud workloads; do not split workloads into extra facilities.

## Common Guinea Pitfalls

- Do not use the FratMat `construction-du-data-center-national` article for Guinea; it is about Cote d'Ivoire.
- Do not treat GUILAB's ISO 9001 certification as a datacenter Tier/Uptime certification.
- Do not treat national DC "Tier III" wording as independently certified without Uptime, engineering or official certificate evidence.
- Do not infer a DC from `salle serveur`, bank IT rooms, university labs, cybercafes, tower sites, fibre huts, ordinary NOCs, MSCs, government offices or mining SCADA/control rooms.
- Do not infer a facility from ARPT licensing, IXP presence, partner logos or mobile rollout locations.
- Verify prefecture/division placement for mining leads before attribution: Simandou south/Beyla is Nzerekore; Kerouane is Kankan; Lefa/Lelouma needs confirmation from current mine documents.
- Use physical site for division attribution, not article scope or company headquarters.

## Recommended Discovery Order

1. Build Conakry records first: GUILAB Data Center, Data Center National, GUILAB ACE landing station, IXP-GUINEE, ARPT, ANSSI, Orange, MTN, Cellcom, Guinee Telecom, MOUNA, Leadernet, banks.
2. For each seed, search operator + address + ARPT/CNT/Journal Officiel/WARDIP/EDG/PeeringDB/procurement/power terms.
3. Sweep official GUILAB pages before using directories; use directories only to find candidate names or stale aliases.
4. Run all 8 division queries, then mining-sector pivots.
5. Assign field-level grades and write explicit negative coverage notes for every non-Conakry division before creating records.
