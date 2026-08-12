# FR Explorer — Official / Regulatory / Cloud Pipeline for France Datacenter Enumeration

Date: 2026-08-11. Scope: enumerate France datacenter facilities and projects from official/regulatory/cloud/colo sources, with French and English query patterns. Country: **FR France**. Administrative sweep: **18 regions + 101 departements**; use communes/EPCI as the planning-permit unit because building permits are filed locally. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association, **C** = weak/aggregate/advocacy/self-media.

---

## 0. Structural facts for France

- France has no single public facility registry for all datacenters. Build the census by joining **urbanisme permits**, **environmental/prefecture consultations**, **grid signals**, **cloud-region pages**, and **operator official pages**.
- The planning clue is usually **permis de construire / autorisation d'urbanisme** at commune or intercommunal level, later surfaced in national **SITADEL** open data. Search both French and English terms: `data center`, `datacenter`, `centre de donnees`, `centre de données`, `centre informatique`, `hebergement informatique`, `salle informatique`.
- The environmental clue is often not "datacenter" as a legal category. Datacenters appear in dossiers for **installations classees / ICPE**, backup generators, fuel tanks, batteries, cooling systems, "autorisation environnementale", "enquete publique", or "consultation du public". Prefecture pages and MRAe/Autorite environnementale opinions frequently expose exact communes, MW, generator counts, site area, and phasing.
- The grid clue is strong for hyperscale. RTE says it had connected **8 datacenters since 2016 for 800 MW contracted capacity**, with only **120 MW maximum consumption at end-2024**, showing that contracted grid capacity can overstate built/used capacity. Enedis states there are roughly **400 distribution-connected data centers** in France, mostly small/medium sites; a 2026 Enedis presentation says the current count is about **460**, with **1.2 GW** distribution-connected power. Use RTE for transmission-scale projects and Enedis for distribution-scale projects.
- France policy/regulator sources are relevant but mostly aggregate: **DGE/entreprises.gouv.fr** publishes data-center implantation guidance and a government contact path; **ARCEP** has new cloud regulation missions under SREN/Data Act and collects aggregate data-center environmental data. These are not facility lists, but they frame obligations and point to public reporting.
- Main geography: Paris/Ile-de-France dominates carrier-neutral and hyperscale colocation; Marseille is the subsea/network gateway; northern France is OVHcloud's base; secondary signals appear in Lyon, Bordeaux, Toulouse, Lille/Roubaix, Strasbourg, Nantes/Rennes, Grenoble, Nice/Sophia Antipolis, and AI/hyperscale industrial sites announced by state/regional development agencies.

---

## 1. High-value official sources (Grade A backbone)

### 1.1 Planning / building-permit data

- **SITADEL / SDES open data**: official national data for building permits and other planning authorizations since 2013. Source page: https://www.statistiques.developpement-durable.gouv.fr/donnees-des-permis-de-construire-et-autres-autorisations-durbanisme and data.gouv dataset: https://www.data.gouv.fr/datasets/liste-des-permis-de-construire-et-autres-autorisations-durbanisme. Use monthly non-residential files and filter on applicant names, commune, surface, and text-like fields where available. **Grade A** for permit existence, date, commune, authorization type, and surface; it may not reveal "datacenter" explicitly.
- **Géoportail de l'Urbanisme (GPU)**: official portal for PLU/PLUi, SCOT, servitudes and zoning documents: https://www.geoportail-urbanisme.gouv.fr/. It is not a permit list, but it verifies whether a candidate parcel/commune is in an industrial/logistics/equipment zone compatible with a datacenter. **Grade A** for zoning context.
- **Commune / EPCI urbanisme portals**: permits are filed with the commune and may be instructed by the EPCI/metropole or state DDT(M). Search mairie and metropole pages for `permis de construire`, `arrete`, `registre des autorisations d'urbanisme`, `ADS`, `urbanisme`, and the operator/SPV name. **Grade A** when the posted permit order or deliberation is official.

Planning query templates:

```text
site:statistiques.developpement-durable.gouv.fr SITADEL permis construire locaux non residentiels
site:data.gouv.fr SITADEL "permis de construire" "locaux non résidentiels"
"{commune}" "permis de construire" ("data center" OR datacenter OR "centre de données" OR "centre informatique")
site:{commune}.fr "permis de construire" "centre de données"
site:{metropole}.fr "autorisation d'urbanisme" datacenter
"{operator}" "{commune}" "permis de construire"
"{SPV name}" "PC" "{department number}"
```

Practical SITADEL filters:

- Applicant/operator names: `Equinix`, `Digital Realty`, `Interxion`, `DATA4`, `Telehouse`, `OVH`, `OVHcloud`, `Scaleway`, `Iliad`, `Online`, `Amazon Data Services`, `Microsoft`, `Google`, `Orange`, `SFR`, `Bouygues Telecom`, `Free`, `CyrusOne`, `Colt`, `Global Switch`, `DataBank`, `Segro`, `Data Hills`.
- Destinations/surfaces: non-residential buildings, industrial/warehouse/technical/equipment surfaces, very large floor area with low employment, electrical substation wording. SITADEL may use broad non-residential categories rather than a datacenter-specific type.
- Join with BAN/Base Adresse Nationale and commune INSEE code for geocoding; use departmental code as the stable sweep key.

### 1.2 Environmental / ICPE / public consultation records

- **Prefecture department sites**: every department has a state-services site under patterns such as `https://www.{department-slug}.gouv.fr/` and publishes `Enquetes publiques`, `Consultations du public`, `Installations classees`, `ICPE`, `Autorisation environnementale`, and signed prefectural orders. Example: Val-de-Marne posted a SEGRO datacenter consultation at Bonneuil-sur-Marne; Seine-Saint-Denis posted a Data Hills datacenter enquiry at Aulnay-sous-Bois. **Grade A**.
- **Projet environnement portal**: https://www.projets-environnement.gouv.fr/ exposes environmental authorization records; example query result exists for `Construction du datacenter Interxion MRS4 et d'une sous-station` in Marseille. Search by `datacenter`, `centre de données`, `Interxion`, `Digital Realty`, and commune. **Grade A**.
- **MRAe / Autorite environnementale**: regional environmental authority opinions and case-by-case decisions are often the best technical files for new facilities. Search `mrae.developpement-durable.gouv.fr datacenter`, `centre de données`, and region. **Grade A** for project descriptions and environmental concerns.
- **Géorisques / Inspection des installations classées**: inspection reports can identify operating entities and ICPE rubriques. Search `georisques.gouv.fr datacenter`, operator name, or SIRET. **Grade A** for inspections.

Environmental query templates:

```text
site:{departement}.gouv.fr (datacenter OR "data center" OR "centre de données" OR "centre informatique") (ICPE OR "autorisation environnementale" OR "enquête publique" OR "consultation du public")
site:projets-environnement.gouv.fr (datacenter OR "centre de données" OR Interxion OR Equinix OR "Digital Realty")
site:mrae.developpement-durable.gouv.fr ("data center" OR datacenter OR "centre de données") "{region}"
site:georisques.gouv.fr (datacenter OR "centre de données" OR "Amazon Data Services France")
"{operator}" "{commune}" ("groupes électrogènes" OR "rubrique 2910" OR ICPE)
"{project name}" "avis de l'autorité environnementale"
```

Status terms to parse: `depose`, `accorde`, `arrete`, `recours`, `suspension`, `annulation`, `enquete publique`, `consultation parallélisée`, `autorisation environnementale`, `mise en service`, `exploitation`, `extension`, `poste de transformation`, `sous-station`.

### 1.3 Grid and energy evidence

- **RTE**: transmission-scale raccordement and SDDR materials. Source: https://assets.rte-france.com/prod/public/2025-02/SDDR2025-principales-orientations-fiche5-raccordement-industrie_0.pdf. Use for large projects, contracted MW, and warnings about speculative capacity reservation. **Grade A** for aggregate transmission facts; project-level names may be absent.
- **Enedis Observatoire / press / open data**: Enedis states about 400 distribution-connected datacenters and 2024 distribution consumption of 2.9 TWh; open-data portal: https://data.enedis.fr/; datacenter article: https://observatoire.enedis.fr/article/la-france-attractive-pour-les-data-centers-2; press page: https://www.enedis.fr/presse/observatoire-de-la-transition-ecologique-la-data-enedis-data-centers-quelle-consommation. **Grade A** for aggregate distribution facts.
- **Connection process pages**: Enedis professional building connection page https://www.enedis.fr/raccordement-batiment-professionnel-entreprise helps identify expected workflow terms (`demande de raccordement`, `proposition de raccordement`, `poste source`), but not facility names. **Grade A process / not a facility list**.
- **Local deliberations**: commune/EPCI council minutes often reveal land sale, power easement, heat-reuse, or substation work before the permit is visible. Search `poste source`, `raccordement electrique`, `convention`, `chaleur fatale`, `reseau de chaleur`, `datacenter`.

Grid query templates:

```text
site:rte-france.com datacenter raccordement France MW
site:rte-france.com "centre de données" raccordement
site:enedis.fr datacenter "raccordés" "réseau public de distribution"
site:data.enedis.fr datacenter
"{commune}" datacenter "poste source" OR "poste électrique" OR "sous-station"
"{operator}" "{commune}" raccordement électrique MW
"{department}" "réseau de chaleur" datacenter "chaleur fatale"
```

Energy caution: never treat contracted MW as operational IT load. Keep separate fields for `contracted/grid capacity`, `authorized generator capacity`, `facility shell power`, `IT load`, and `actual consumption`.

### 1.4 Regulator / policy / official cloud framework

- **DGE / entreprises.gouv.fr** data-center guidance: https://www.entreprises.gouv.fr/secteurs-dactivite/le-secteur-du-numerique-en-france/data-centers-atouts-enjeux-et-accompagnement and the 2025 implantation guide PDF: https://www.entreprises.gouv.fr/files/files/Publications/2025/Guide/25112025__Guide%20Datacenters.pdf. Notes official government contact paths (`datacenters.dge@finances.gouv.fr`, Business France for foreign investors), and says ARCEP collects aggregate operator data. **Grade A** for policy/process.
- **ARCEP cloud regulation**: ARCEP gained cloud-service regulation missions under the 2024 SREN law/Data Act context. Useful sources: ARCEP opinion 2024-2773 PDF, 2025 cloud interoperability consultation press release, and 2025 EU cloud/AI policy contribution. ARCEP is not a permit registry; use it for provider obligations and aggregated environmental reports. Main site: https://www.arcep.fr/. **Grade A policy / not facility-level**.
- **CNIL / ANSSI** may identify sovereign cloud operators and SecNumCloud-certified offerings, but generally not facility lists. Use for provider identity only. **Grade A policy/certification**.

---

## 2. Official cloud and operator seed lists

### 2.1 Hyperscale cloud regions (Grade A existence, not exact addresses)

| Provider | Official source | France signal | Notes |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and AZ IDs page | `eu-west-3`, Europe (Paris), 3 AZs | AWS does not publish exact sites. Pivot to `Amazon Data Services France SAS`, prefecture ICPE, SITADEL, and local grid records. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | France Central = Paris; France South paired region | Search `Microsoft France Central`, `France South`, `Microsoft datacenter France`, and SPVs. |
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/about/locations | `europe-west9`, Paris | Google announced Paris region opening in 2022; exact sites hidden. Search operator/SPV and local public files. |
| OVHcloud | https://www.ovhcloud.com/en/datacenter/ and https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ | Gravelines, Paris, Roubaix, Strasbourg; northern France SecNumCloud region across Gravelines/Roubaix/Strasbourg | Official pages expose city-level campus geography; local permits and ICPE give building detail. |
| Scaleway | https://www.scaleway.com/en/blog/introducing-dc5-hyper-scale-mechanical-cooling-datacenter/ and impact reports | DC2/DC3/DC4/DC5 in/near Paris; DC5 >20 MW IT power | Scaleway pages and impact reports name DC IDs and environmental metrics. Pivot to Vitry-sur-Seine/Saint-Ouen-l'Aumone/Paris-area permits. |

Cloud query templates:

```text
"AWS" "eu-west-3" France datacenter
"Amazon Data Services France" ("permis de construire" OR ICPE OR "autorisation environnementale")
"Microsoft" "France Central" datacenter "permis de construire"
"Google Cloud" "europe-west9" Paris "centre de données"
"OVHcloud" (Gravelines OR Roubaix OR Strasbourg OR Paris) (datacenter OR "centre de données" OR permis)
"Scaleway" (DC2 OR DC3 OR DC4 OR DC5) (permis OR ICPE OR "centre de données")
```

### 2.2 Major carrier-neutral / colocation operators (official pages first)

| Operator | Official source | France facility seed |
|---|---|---|
| Equinix | https://www.equinix.com/data-centers/europe-colocation/france-colocation/paris-data-centers | Paris metro: PA2, PA3, PA4, PA5, PA6, PA7, PA8x, PA9x, PA10, PA13x; also Bordeaux nearby listing. Search Saint-Denis, Pantin, and xScale project names. |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/paris | Paris page says 13 data centers around the ring road, 86.6k m2 colocation space; also Marseille Interxion/Digital Realty campuses for subsea gateway. Search PAR and MRS codes. |
| DATA4 | https://www.data4group.com/en/data-center-in-paris-france/ | Paris-Saclay campus addresses at Nozay and Marcoussis (PAR01/PAR02/PAR03). Search DATA4, Data4 Group, Nozay, Marcoussis, Villejust. |
| Telehouse | Official Telehouse France pages | Paris Voltaire, Magny-les-Hameaux and related facilities; search public inquiry PDFs and CNCE records. |
| Global Switch | Official Global Switch Paris page | Clichy/Paris carrier-neutral seed; verify via local permits and ICPE. |
| Orange / SFR / Bouygues Telecom / Free-Iliad | Operator official pages, annual reports, ARCEP context | Telco DCs may be network/in-house sites; facility count is less transparent. Use SITADEL, ICPE, and energy/heat-reuse announcements. |

Colo query templates:

```text
"Equinix" (PA2 OR PA3 OR PA4 OR PA8x OR PA10 OR PA13x) "France"
"Equinix" Pantin "permis de construire" datacenter
"Digital Realty" Paris (PAR1 OR PAR5 OR PAR8 OR PAR11 OR "Digital Park")
"Interxion" Marseille (MRS3 OR MRS4 OR MRS5) "autorisation environnementale"
"DATA4" (Nozay OR Marcoussis OR Villejust) ("permis de construire" OR ICPE OR MW)
"Telehouse" "Magny-les-Hameaux" datacenter "enquête publique"
"Global Switch" Clichy "centre de données"
```

---

## 3. Per-division enumeration workflow (18 regions + 101 departements)

Use France's administrative hierarchy as a funnel:

1. **National seed**: SITADEL monthly files + official cloud/colo pages + DGE/ARCEP/RTE/Enedis aggregate sources.
2. **Region sweep**: search region prefecture, MRAe region page, regional development agency, regional energy/heat-reuse terms, and major metropole portals.
3. **Department sweep**: search each department prefecture site for `datacenter`, `centre de données`, ICPE and public consultation records.
4. **Commune/EPCI sweep**: for hits from steps 1-3, search the commune mairie and metropole/communauté d'agglomération urbanisme portal for permit orders, land sales, council minutes, PLU modifications, and heat-network agreements.
5. **Operator pivot**: for every operator/SPV found, run SITADEL, Pappers/Sirene, prefecture, MRAe, and local queries using the legal entity name and project code.
6. **Grid validation**: search RTE/Enedis/local energy terms and council minutes for substation/raccordement evidence. Record grid capacity separately from operational IT load.

### 3.1 Priority regions and what to search

- **Ile-de-France** (75, 77, 78, 91, 92, 93, 94, 95): highest priority. Search Saint-Denis, Pantin, La Courneuve, Aubervilliers, Aulnay-sous-Bois, Bonneuil-sur-Marne, Wissous, Lisses, Nozay, Marcoussis, Magny-les-Hameaux, Clichy, Vitry-sur-Seine, Saint-Ouen-l'Aumone. Portals: DRIEAT/MRAe IDF, prefectures 75/77/78/91/92/93/94/95, Institut Paris Region. Operators: Equinix, Digital Realty/Interxion, DATA4, Telehouse, Scaleway, Global Switch, Amazon/Microsoft/Google.
- **Provence-Alpes-Cote d'Azur** (04, 05, 06, 13, 83, 84): Marseille is the key subsea/interconnection hub. Search Interxion/Digital Realty MRS, Marseille-Fos, Bouc-Bel-Air, Aix-Marseille-Provence, Nice/Sophia. Use projects-environnement and Bouches-du-Rhone prefecture.
- **Hauts-de-France** (02, 59, 60, 62, 80): OVHcloud Roubaix and northern AI/hyperscale site announcements. Search Roubaix, Gravelines, Lille metropole, Dunkerque, Cambrai/Valenciennes industrial land, `FranceforAI`.
- **Grand Est** (08, 10, 51, 52, 54, 55, 57, 67, 68, 88): OVHcloud Strasbourg and cross-border cloud/colo. Search Strasbourg, Bas-Rhin/Haut-Rhin prefectures, Eurometropole, heat-reuse.
- **Auvergne-Rhone-Alpes** (01, 03, 07, 15, 26, 38, 42, 43, 63, 69, 73, 74): Lyon/Grenoble industrial and cloud edge sites; watch recent AI data-center projects in Drome/Isere/Rhone. Search Lyon metropole, Grenoble-Alpes, Rovaltain/Valence, `permis suspendu datacenter`.
- **Nouvelle-Aquitaine** (16, 17, 19, 23, 24, 33, 40, 47, 64, 79, 86, 87): Bordeaux listed by Equinix as nearby/metro; search Bordeaux Metropole, Gironde prefecture, Poitiers/Limoges industrial parks.
- **Occitanie** (09, 11, 12, 30, 31, 32, 34, 46, 48, 65, 66, 81, 82): Toulouse/Montpellier edge/HPC; search `datacenter souverain`, CNES/Airbus ecosystem, metropole permits.
- **Pays de la Loire / Bretagne / Normandie / Centre-Val de Loire / Bourgogne-Franche-Comte / Corse / overseas DROM-COM departments**: lower base density but still sweep prefecture + SITADEL + local press for sovereign cloud, telco, university/HPC, and industrial AI sites.

### 3.2 Department site pattern

For each department, derive three queries:

```text
site:{department-slug}.gouv.fr (datacenter OR "data center" OR "centre de données")
site:{department-slug}.gouv.fr ("centre de données" OR datacenter) ("enquête publique" OR ICPE OR "autorisation environnementale")
site:{department-slug}.gouv.fr "{operator}" ("permis" OR "consultation du public" OR "arrêté préfectoral")
```

Examples of department slugs: `seine-saint-denis.gouv.fr`, `val-de-marne.gouv.fr`, `essonne.gouv.fr`, `yvelines.gouv.fr`, `bouches-du-rhone.gouv.fr`, `nord.gouv.fr`, `bas-rhin.gouv.fr`, `gironde.gouv.fr`, `rhone.gouv.fr`.

For overseas departments (971, 972, 973, 974, 976), search `site:{slug}.gouv.fr datacenter`, `site:*.fr "centre de données" "{territory}"`, and telco/cloud edge operators; count only facility-grade evidence, not generic "data sovereignty" policy.

---

## 4. Search pattern library

### 4.1 French discovery

```text
"centre de données" "{commune}" ("permis de construire" OR ICPE OR "enquête publique")
datacenter "{commune}" ("autorisation environnementale" OR "consultation du public")
"data center" "{departement}" "arrêté préfectoral"
"centre informatique" "{operator}" "{commune}"
"salle informatique" "permis de construire" "{departement}"
"hébergement informatique" "centre de données" "{region}"
"datacenter" "chaleur fatale" "{commune}"
"datacenter" "réseau de chaleur" "{metropole}"
"datacenter" "poste source" "{commune}"
"datacenter" "sous-station" "{commune}"
"datacenter" "groupes électrogènes" "{commune}"
```

### 4.2 English discovery

```text
"France" "data center" "building permit" "{operator}"
"Paris" "data center" "environmental authorization"
"Marseille" "data center" "Interxion" "MRS4"
"France" "hyperscale data center" "RTE" MW
"France" "data center" "grid connection" "RTE"
"France" "data center" "public inquiry" "{operator}"
"France" "data center campus" "{commune}"
```

### 4.3 Entity and legal-name pivots

```text
"{legal entity}" site:societe.com OR site:pappers.fr OR site:annuaire-entreprises.data.gouv.fr
"{legal entity}" "SIREN" datacenter
"{legal entity}" "permis de construire"
"{legal entity}" "autorisation environnementale"
"{legal entity}" "rubrique 2910"
"{legal entity}" "raccordement"
```

Use legal-entity pivots for SPVs such as `Amazon Data Services France SAS`, local real-estate SPVs, `Digital Realty`, `Interxion France`, `Equinix France`, `DATA4 Services`, `Scaleway Datacenter`, `Online SAS`, `OVH SAS/OVHcloud`, `Telehouse International`, and project-specific SNC/SAS names found in permits.

---

## 5. Reliability and extraction rules

### 5.1 Evidence hierarchy

| Source | Grade | Use |
|---|---:|---|
| SITADEL / SDES permit data | A | Building-permit existence, commune, date, surface, authorization type. |
| Commune/EPCI permit orders and council minutes | A | Land sale, permit decision, PLU change, heat network, local opposition/appeal. |
| Prefecture ICPE/enquete publique/autorisation environnementale | A | Facility scope, generators, batteries/fuel, environmental constraints, status. |
| Projets-environnement / MRAe / Autorite environnementale | A | Project descriptions, exact communes, MW/generator clues, cumulative impacts. |
| RTE / Enedis | A | Grid aggregate data and sometimes raccordement context; not always facility names. |
| ARCEP / DGE / Business France | A | Policy/regulatory framework and aggregate reporting, not facility lists. |
| Official cloud region pages | A for region existence, C for exact location | Confirms cloud region/city but hides buildings. |
| Official colo/operator facility pages | A- for existence/location, B for capacity | Marketing pages may round capacity or omit phases. |
| Trade press (DCD, LeMoniteur, Banque des Territoires, local economic press) | B | Discovery and status; verify with filings. |
| Activist maps, social media, forums, generic DC maps | C | Lead generation only; verify before counting. |

### 5.2 Status model

Use these lifecycle labels:

- `rumor/lead`: only trade/advocacy/local news, no official filing.
- `site selection`: land sale, development-agency announcement, council deliberation.
- `permitted`: permis de construire or environmental authorization granted.
- `under review`: enquiry/consultation/MRAe opinion pending.
- `appealed/suspended`: court or prefecture record blocks permit; do not count as active construction.
- `under construction`: permit plus works announcement, construction tender, or satellite evidence.
- `operational`: operator page, ARCEP/environmental report, commissioning, customer availability, or inspection record.
- `expansion`: existing campus with new building/phase permit or environmental modification.

### 5.3 Capacity fields to keep separate

- `surface_m2`: from SITADEL, permits, operator pages.
- `it_mw`: only when explicitly "puissance IT", "IT load", or operator technical page.
- `grid_mw`: raccordement/contracted power from RTE/Enedis/local grid records.
- `generator_mw`: ICPE/environmental backup-generation total; not IT load.
- `campus_plan_mw`: long-term marketing or industrial-plan number; mark as planned.
- `actual_consumption`: kWh/TWh data when present, rare at facility level.

Pitfalls:

- A "data center" can be a small enterprise/server room; require facility-scale evidence before adding as a datacenter facility.
- ICPE rubriques may identify generators/fuel/batteries without saying "datacenter" in the title.
- Paris facilities are often branded "Paris" but physically in Seine-Saint-Denis, Val-de-Marne, Hauts-de-Seine, Essonne, or Yvelines.
- Cloud regions/AZs are logical abstractions and should not be treated as separate physical buildings unless a permit/official facility page proves it.
- Grid contracted MW and generator MW are not operating IT capacity.

---

## 6. Recommended France pipeline

1. **Seed official operator universe**: AWS/Azure/GCP/OVHcloud/Scaleway official region pages; Equinix, Digital Realty/Interxion, DATA4, Telehouse, Global Switch official facility pages.
2. **Run SITADEL national sweep**: filter non-residential authorizations since 2013 by operator/legal names and large technical/industrial surfaces; geocode by commune/departement.
3. **Run prefecture/MRAe sweep per department**: use the 101 department site pattern for `datacenter`, `centre de données`, ICPE, `autorisation environnementale`, `enquête publique`, and operator names.
4. **Run region/metropole deep dives**: prioritize Ile-de-France, Marseille/PACA, Hauts-de-France, Grand Est, Auvergne-Rhone-Alpes, Nouvelle-Aquitaine. Search mairie/EPCI portals for permit orders, council minutes, land transactions, heat-network and grid deliberations.
5. **Cross-check grid**: search RTE/Enedis/local substation terms for each large candidate; record grid capacity separately from IT load.
6. **Verify legal entities**: use annuaire-entreprises.data.gouv.fr, Pappers, Societe.com, and SIRENE fields for legal names/SIREN/SIRET; then re-run official-site queries with legal names.
7. **Assign confidence per field**: a facility can be A for existence/location, B for IT capacity, and C for future phase capacity.

Minimum acceptance for a facility record:

- existence evidence from one **A** source, or two independent **B** sources plus a local official lead;
- commune/departement resolved;
- operator/legal entity or project owner resolved;
- status label assigned;
- capacity fields separated and evidence-graded.

---

## 7. Source index

- SDES SITADEL permits: https://www.statistiques.developpement-durable.gouv.fr/donnees-des-permis-de-construire-et-autres-autorisations-durbanisme
- data.gouv SITADEL listing: https://www.data.gouv.fr/datasets/liste-des-permis-de-construire-et-autres-autorisations-durbanisme
- Géoportail de l'Urbanisme: https://www.geoportail-urbanisme.gouv.fr/
- Projets-environnement portal: https://www.projets-environnement.gouv.fr/
- MRAe / Autorite environnementale: https://www.mrae.developpement-durable.gouv.fr/
- RTE SDDR industry raccordement note: https://assets.rte-france.com/prod/public/2025-02/SDDR2025-principales-orientations-fiche5-raccordement-industrie_0.pdf
- Enedis datacenter observatory: https://observatoire.enedis.fr/article/la-france-attractive-pour-les-data-centers-2
- Enedis open data: https://data.enedis.fr/
- DGE data-center guidance: https://www.entreprises.gouv.fr/secteurs-dactivite/le-secteur-du-numerique-en-france/data-centers-atouts-enjeux-et-accompagnement
- DGE implantation guide PDF: https://www.entreprises.gouv.fr/files/files/Publications/2025/Guide/25112025__Guide%20Datacenters.pdf
- ARCEP: https://www.arcep.fr/
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OVHcloud datacenters: https://www.ovhcloud.com/en/datacenter/
- OVHcloud regions: https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/
- Equinix Paris: https://www.equinix.com/data-centers/europe-colocation/france-colocation/paris-data-centers
- Digital Realty Paris: https://www.digitalrealty.com/data-centers/emea/paris
- DATA4 Paris: https://www.data4group.com/en/data-center-in-paris-france/
- Scaleway DC5: https://www.scaleway.com/en/blog/introducing-dc5-hyper-scale-mechanical-cooling-datacenter/
