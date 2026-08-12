# MC Explorer Industry - Monaco Datacentre Enumeration via Operators, Sovereign Cloud, Trade Press, and Directories

Date: 2026-08-12. Scope: Monaco (MC), covering all 17 repo divisions: La Colle, La Condamine, Fontvieille, La Gare, Jardin Exotique, Larvotto, Malbousquet, Monte-Carlo, Moneghetti, Monaco-Ville, Moulins, Port-Hercule, Sainte-Devote, La Source, Spelugues, Saint-Roman, Vallon de la Rousse.

Reliability grades: **A** = operator official page/certificate, government/regulator page, Journal de Monaco notice, or official company announcement; **B** = trade press/local business press with named parties and dates; **C** = directory, marketplace, reseller, SEO page, or unverified aggregate. Keep field-level grades: a source can be Grade A for operator existence but only Grade C for a specific address if the address came from a directory.

---

## 0. Market shape

- Monaco's datacentre market is tiny and sovereignty-driven. The main discoverable players are **Monaco Telecom**, **Telis / MonacoDATACENTER**, and **Monaco Cloud**. There is no known hyperscale campus and no public AWS, Azure, Google Cloud, or OCI Monaco region.
- The most important correction to older drafts: Monaco Telecom should not be described as "all Fontvieille" without qualification. Its official 2025 certificate lists `25 boulevard de Suisse` for Centre de données n°1 and `Zone F, 4-6 avenue Albert II` for Centre de données n°6, while Journal de Monaco identifies DC3 at the Zone F building, `6 avenue Albert II`.
- Monaco Cloud is a sovereign cloud service/operator, not automatically a separate physical datacentre. Its official site says services are multi-site, data is stored in Monaco under Monegasque law, and Monaco Cloud is AMSN-qualified; enumerate the physical sites through Monaco Telecom/Telis evidence.
- Demand drivers: public administration, OIV/critical services, finance/private banking, iGaming, insurance, luxury/event operations, and health-data hosting. Many customers operate in-house server rooms; do not count those without facility-level evidence.
- Common French terms: `centre de données`, `datacenter`, `data center`, `hébergement`, `colocation`, `cloud souverain`, `salle informatique`, `salle de serveurs`, `baies`, `groupe électrogène`, `thalassothermie`, `SeaWergie`.

---

## 1. Operator and vendor sweep

### 1.1 Priority operators and facilities

| Operator / facility lead | Official / useful URL | Division to resolve | Evidence use |
|---|---|---|---|
| Monaco Telecom hosting platform | https://monaco-telecom.mc/en/data-center/ and https://monaco-telecom.mc/data-center/ | Multiple | Grade A for platform: 3 data centers in the Principality, colocation/private space, ISO 27001:2022, up to 12 kW/rack, 1.3 kW/m2, 2N power, generators, N+1 cooling |
| Monaco Telecom 2025 certificate | https://monaco-telecom.mc/wp-content/uploads/2025/12/Certificats-MT_V2.pdf | Fontvieille and likely Monte-Carlo/Sainte-Devote edge | Grade A for current certified sites: `4-6 avenue Albert II - Zone F` primary/head office and DC3; `25 boulevard de Suisse` Centre de données n°1; `Zone F, 4-6 avenue Albert II` Centre de données n°6 |
| Monaco Telecom DC3 | Journal protected-zone notice: https://journaldemonaco.gouv.mc/fr/Journaux/2019/Journal-8435/Arrete-Ministeriel-n-2019-452-du-16-mai-2019-creant-une-zone-protegee-au-Data-Center-n-3-de-Monaco-Telecom ; 2015 launch coverage: https://www.globalsecuritymag.fr/Monaco-Telecom-Inaugurates-a-New%2C20150605%2C53223 | Fontvieille unless repo geometry says otherwise | Grade A address/status from Journal; Grade B historical specs from press: about 1,000 m2 / 200 racks, Tier III design/construction, Schneider Electric/SDMO/Emerson/Schroff/Chubb ecosystem |
| Monaco Telecom Zone J / legacy site | Monaco Life outage report: https://monacolife.net/what-caused-monaco-telecoms-worst-outage-in-25-years/ | Fontvieille | Grade B: Zone J under Fontvieille shopping centre, SMEG grid maintenance, generator failure, outage on 29 November 2022; use as resilience/location clue, not final capacity |
| Monaco Telecom Larvotto Supérieur project | Journal tender: https://journaldemonaco.gouv.mc/switchlanguage/to/jdm_eng/Journaux/2023/Journal-8649/Avis-d-Appel-Public-a-Candidatures-Larvotto-Superieur-pour-la-Direction-des-Travaux-Publics-de-la-Principaute-de-Monaco ; DCD: https://www.datacenterdynamics.com/en/news/monaco-telecom-to-build-basement-data-center-in-new-residential-tower/ | Larvotto/Saint-Roman boundary check | Grade A for proposed project: about 1,600 m2 data center for Monaco Telecom in R-3/R-4; Grade B for 19 boulevard du Larvotto, 1,550 m2, 2027 completion reporting |
| Telis / MonacoDATACENTER | https://www.telis.mc/digital-solutions/it-systems/ , https://www.telis.mc/development-and-innovation/ , https://www.telis.mc/labels-and-certifications/ , https://www.telis.mc/it-and-digital-transformation-partner-in-monaco/ | Fontvieille | Grade A: `14 avenue de Grande-Bretagne`, first Monaco green datacenter, created/opened 2013, ISO 27001/HDS, Tier III-designed, 99.997% claimed availability, seawater/free-cooling, 24/7/365 supervision |
| Monaco Cloud | https://www.monacocloud.mc/ and https://www.monacocloud.mc/presentation | HQ Fontvieille; infrastructure via MT/Telis | Grade A platform evidence: operator of Monaco's state sovereign cloud, state-majority, public cloud, multi-site, data under Monegasque law, AMSN PINH Avancé/PSSI-E, `9 avenue Albert II - Le Copori` office |
| DRSI / government IT room | https://journaldemonaco.gouv.mc/Journaux/2019/Journal-8435/Arrete-Ministeriel-n-2019-453-du-16-mai-2019-creant-une-zone-protegee-au-sein-de-la-Direction-des-Reseaux-et-Systemes-d-Information | Fontvieille unless repo geometry says otherwise | Grade A public-sector server-room evidence at `23 avenue Albert II`; not commercial colocation |
| Bank/casino/hotel in-house rooms | Search by operator name plus `salle informatique`, `data center`, `hébergement`, `PRA` | Monte-Carlo, Spelugues, Moulins, La Condamine | Default Grade C/no-count unless a facility-level source proves a dedicated datacenter |

Operator search templates:

```text
"Monaco Telecom" "data center"
"Monaco Telecom" "centre de données"
"Monaco Telecom" "DC3"
"Monaco Telecom" "Centre de données n°1"
"Monaco Telecom" "Centre de données n°6"
"Monaco Telecom" "25 boulevard de Suisse"
"Monaco Telecom" "4-6 avenue Albert II"
"Monaco Telecom" "Zone F"
"Monaco Telecom" "Zone J" Fontvieille
"Monaco Telecom" "Larvotto Supérieur"
"Monaco Telecom" "19 boulevard du Larvotto"
"MonacoDATACENTER" "14 avenue de Grande-Bretagne"
"Telis" "MonacoDATACENTER" "HDS"
"Telis" "MonacoDATACENTER" "Tier III"
"Monaco Cloud" "multi-site"
"Monaco Cloud" "PINH Avancé"
"Monaco Cloud" "Monaco Telecom"
"Monaco Cloud" "Telis"
```

### 1.2 Connectivity context

- Monaco Telecom's public business products provide dedicated fibre up to 10 Gbps and hosting/cloud services; use this as connectivity context, not facility count. Sources: https://monaco-telecom.mc/en/connectivity/ and https://monaco-telecom.mc/en/hebergement-cloud-a-monaco-telecom/
- Trade coverage around DC3 states Monaco benefits from the Europe India Gateway submarine cable and carrier connectivity. Treat carrier/cable claims as Grade B unless confirmed by Monaco Telecom or cable-owner records.
- No public Monaco IXP was verified. Do not invent an exchange, campus, or carrier-neutral meet-me ecosystem from generic connectivity claims.

---

## 2. Trade press and secondary sources

| Source | URL / query | Monaco use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/monaco-telecom-to-build-basement-data-center-in-new-residential-tower/ | Larvotto Supérieur project details: 19 boulevard du Larvotto, basement data center, 1,550 m2, 2027 completion, SeaWergie/solar context; verify against Journal tender | B |
| Monaco Life | https://monacolife.net/what-caused-monaco-telecoms-worst-outage-in-25-years/ | 29 Nov 2022 Monaco Telecom outage: Zone J under Fontvieille shopping centre, SMEG grid, generator failure, public-service impact | B |
| Monaco Hebdo | https://monaco-hebdo.com/economie/stockage-de-donnees%E2%80%89-le-pari-de-monaco-telecom/ | Historical 2014 MT expansion: Fontvieille data center planned at about 1,000 m2 / 200 racks; avenue de la Costa legacy reference; EUR 6m investment | B |
| Global Security Mag | https://www.globalsecuritymag.fr/Monaco-Telecom-Inaugurates-a-New%2C20150605%2C53223 | 2015 DC3 inauguration coverage: about 1,000 m2, heart of Monaco, design/construction Tier III, supplier ecosystem | B |
| Univers Freebox | search `Monaco Telecom Xavier Niel inaugure Data Center 1000m2` | Secondary launch article for DC3; useful if original operator press release is unavailable | B |
| Monaco Now | https://monaconow.com/monaco-cloud-the-first-operational-sovereign-cloud-in-europe/ | Monaco Cloud operational since Oct 2021, state sovereign cloud messaging | B |
| Cloud Computing News | https://www.cloudcomputing-news.net/news/monaco-launches-europes-first-state-sovereign-cloud/ | Monaco Cloud launch; data stored only in Monaco and governed by Monegasque law; cross-check with Monaco Cloud official | B |
| Le Monde Informatique | https://www.lemondeinformatique.fr/actualites/lire-monaco-devoile-ses-ambitions-sur-son-cloud-souverain-77967.html | Early Monaco sovereign-cloud / AWS Outposts option; historical only, not proof of an AWS region | B |
| Monaco Tribune / Monaco-Matin / Nice-Matin / Gazette de Monaco | query by facility/project | Local construction/council/status updates; use named-party details but verify with Journal/official pages | B |
| DatacenterMap / Baxtel / Data Center Platform / Cloudscene / DC Byte | query by operator and country | Seed addresses and market leads only. Baxtel has Larvotto Supérieur under construction; Data Center Platform lists Telis at 14 Av. de Grande Bretagne | C unless corroborated |

Trade-query examples:

```text
site:datacenterdynamics.com Monaco "Monaco Telecom"
site:monacolife.net "Monaco Telecom" "data centre"
site:monaco-hebdo.com "Monaco Telecom" "data center"
site:globalsecuritymag.fr "Monaco Telecom" "Data Center"
site:monaconow.com "Monaco Cloud"
site:cloudcomputing-news.net "Monaco Cloud"
site:lemondeinformatique.fr "Monaco" "cloud souverain"
site:monaco-tribune.com "data center" Monaco
site:lagazettedemonaco.com "Larvotto Supérieur" "data center"
site:nicematin.com "Monaco Telecom" "Zone J"
```

---

## 3. Directory-to-primary verification workflow

1. Seed potential sites from directories:
   - DatacenterMap `Monaco Telecom DC3`, `MonacoDATACENTER`.
   - Baxtel `Monaco Telecom: Monaco` / Larvotto Supérieur.
   - Data Center Platform `Telis Datacenter`, 14 Av. de Grande Bretagne.
   - DC Byte / Cloudscene / DatacenterCatalog Monaco entries.
2. Resolve each seed to a primary source:
   - Monaco Telecom page + ISO/HDS certificate + Journal protected-zone notice.
   - Telis pages + MonacoDATACENTER official content.
   - Journal de Monaco tender/protected-zone notices.
3. Map the physical address to the repo quarter using address geometry, not marketing district names.
4. Store directory-only claims as `candidate_seed` / Grade C and do not include them in final facility counts unless primary or named-party evidence confirms the site.
5. For Larvotto Supérieur, keep status as `proposed` or `under_construction` until an official commissioning, certificate, or operator page proves it is live.

Directory queries:

```text
site:datacentermap.com/monaco/ "Monaco Telecom"
site:datacentermap.com/monaco/ "MonacoDATACENTER"
site:baxtel.com "Monaco Telecom" Monaco "Larvotto"
site:datacenterplatform.com "Telis" "Monaco"
site:cloudscene.com "Monaco" "data center"
site:dcbyte.com "Monaco Telecom"
site:datacentercatalog.com "Monaco Telecom"
```

---

## 4. Quarter search recipes

Run each recipe for all 17 divisions:

```text
"{quarter}" Monaco "data center"
"{quarter}" Monaco "data centre"
"{quarter}" Monaco "centre de données"
"{quarter}" Monaco datacenter
"{quarter}" Monaco "salle informatique"
"{quarter}" Monaco "salle de serveurs"
"{quarter}" Monaco colocation
"{quarter}" Monaco hébergement
"{quarter}" "Monaco Telecom"
"{quarter}" "MonacoDATACENTER"
"{quarter}" "Monaco Cloud"
"{quarter}" "SMEG"
```

High-yield variants:

```text
"Fontvieille" "Monaco Telecom" "Zone F"
"Fontvieille" "Zone J" "data center"
"Centre Commercial de Fontvieille" "data center"
"avenue Albert II" "Data Center n°3"
"4-6 avenue Albert II" "Centre de données"
"23 avenue Albert II" "salle informatique"
"14 avenue de Grande-Bretagne" "MonacoDATACENTER"
"boulevard de Suisse" "Monaco Telecom" "Centre de données"
"Larvotto Supérieur" "data center"
"19 boulevard du Larvotto" "Monaco Telecom"
"Monte-Carlo" "boulevard de Suisse" "Monaco Telecom"
"Spelugues" OR "Spélugues" "salle informatique"
"Port Hercule" "data center" Monaco
"La Rousse" OR "Vallon de la Rousse" "data center"
"Sainte-Devote" OR "Sainte-Dévote" "Monaco Telecom"
```

Quarter handling:

- **Fontvieille**: highest yield. Avenue Albert II / Zone F, Le Copori, Les Terrasses de Fontvieille, and Avenue de Grande-Bretagne are the core cluster. Confirm if the repo's quarter geometry places `4-6/6 avenue Albert II`, `9 avenue Albert II`, `14 avenue de Grande-Bretagne`, and `23 avenue Albert II` in Fontvieille.
- **Monte-Carlo / Sainte-Devote edge**: `25 boulevard de Suisse` is a certified Monaco Telecom data-center address; resolve carefully.
- **Larvotto / Saint-Roman edge**: Larvotto Supérieur / `19 boulevard du Larvotto` is a future Monaco Telecom DC project; resolve against repo geometry because Monaco marketing may use Larvotto broadly.
- **La Condamine / Port-Hercule**: expect connectivity and business IT, not public colo. Exclude harbour/event telecom rooms unless data-center evidence appears.
- **Moulins / Spelugues**: likely in-house hotel/casino/bank IT; no count without facility-level evidence.
- **La Colle, La Gare, Jardin Exotique, Malbousquet, Moneghetti, La Source, Vallon de la Rousse**: low-yield sweep; record negative coverage rather than assuming Fontvieille-only coverage.

---

## 5. Known seed list for validation

This is a methodology seed list, not a final census.

| Seed | Division assignment | Status tendency | Best evidence path | Grade |
|---|---|---|---|---|
| Monaco Telecom DC3 | Fontvieille likely; `6 avenue Albert II`, Zone F | Operational | Journal protected-zone notice + Monaco Telecom certificate + operator page | A |
| Monaco Telecom Centre de données n°1 | Resolve `25 boulevard de Suisse`; likely Monte-Carlo/Sainte-Devote edge | Operational | Monaco Telecom certificate | A |
| Monaco Telecom Centre de données n°6 | Fontvieille likely; `Zone F, 4-6 avenue Albert II` | Operational | Monaco Telecom certificate | A |
| Monaco Telecom Zone J legacy/main site | Fontvieille, under Centre Commercial de Fontvieille | Operational/legacy; relationship to certified current sites must be checked | Monaco Life/Monaco-Matin outage + seek MT/SMEG/JDM confirmation | B |
| Monaco Telecom Larvotto Supérieur | Larvotto/Saint-Roman boundary | Proposed/under construction; not yet operational unless later source proves commissioning | Journal n°8649 tender + DCD/local council coverage | A for project, B for some status details |
| Telis MonacoDATACENTER | Fontvieille; `14 avenue de Grande-Bretagne` | Operational since 2013 | Telis official pages + certification page | A |
| Monaco Cloud | HQ Fontvieille; physical platform hosted across local sites | Operational sovereign cloud since 2021 | Monaco Cloud official + AMSN qualification + Monaco Now/Cloud Computing News | A for platform, not facility |
| DRSI computer room | Fontvieille likely; `23 avenue Albert II` | Operational public-sector server room | Journal n°8435 protected-zone notice | A |
| SBM / bank / hotel server rooms | Monte-Carlo, Spelugues, Moulins, La Condamine possible | In-house only unless proven | Official or named-party facility-level source required | C by default |

---

## 6. Capacity extraction guidance

Monaco rarely publishes MW. Record disclosed proxies and do not infer electrical capacity.

- **Monaco Telecom platform**: official page states up to 12 kW/rack, 1.3 kW/m2, 2N electrical chain from generators to rack PDUs, direct expansion/chilled-water cooling with N+1 redundancy, inert gas fire suppression, 24/7 secure access.
- **Monaco Telecom 2020/2025 certification**: 2,000 m2 of IT rooms across 3 data centers was stated in the 2020 ISO announcement; current certificate is stronger for site list and certification scope.
- **Monaco Telecom DC3 historical specs**: about 1,000 m2 and 200 racks from 2014/2015 press. Treat as historical B unless operator materials are recovered.
- **Larvotto Supérieur**: Journal says about 1,600 m2; DCD/local press say about 1,550 m2. Use the official 1,600 m2 wording for methodology unless a later permit/as-built source supersedes it.
- **Telis MonacoDATACENTER**: operator pages state Tier III design target, ISO 27001/HDS, 99.997% claimed availability, 100% availability claim since opening, seawater/free-cooling; do not translate energy savings into MW.
- **Monaco Cloud**: official pages state multi-site services, encryption/security, Monegasque legal governance, and AMSN qualification. Do not count cloud instances as physical capacity.

Capacity queries:

```text
"Monaco Telecom" "baies"
"Monaco Telecom" "racks"
"Monaco Telecom" "m2" "data center"
"Monaco Telecom" "kW/baie"
"Monaco Telecom" "groupe électrogène"
"Monaco Telecom" "HDS" "ISO 27001"
"Larvotto Supérieur" "1600 m2" "data center"
"MonacoDATACENTER" "baies"
"MonacoDATACENTER" "HDS"
"MonacoDATACENTER" "Tier III"
"MonacoDATACENTER" "thalassothermie"
"Monaco Cloud" "multi-site"
```

When no explicit MW source exists, set `capacity_mw: null` and preserve the exact proxy values in notes with their source/grade.
