# CG Explorer Official - Republic of the Congo Datacenter Enumeration

Date: 2026-08-12. Country: **CG - Republic of the Congo / Congo-Brazzaville** (`Republique du Congo`). Target division model for this explorer: **12 legacy/manifest departments**: Bouenza; Brazzaville; Cuvette; Cuvette-Ouest / West Cuvette; Kouilou; Lekoumou; Likouala; Niari; Plateaux; Pointe-Noire / Black Point; Pool; Sangha.

Important administrative note: official Congo government material now refers to **15 departments** after the 2024 territorial reform. The March 2025 government prefect appointments list 15 departments and includes the new Congo-Oubangui, Djoue-Lefini, and Nkeni-Alima departments: https://gouvernement.cg/decentralisation-nomination-des-prefets-des-quinze-departements/. This explorer remains keyed to the requested 12-department manifest. When searching, map new labels back to the legacy coverage: Nkeni-Alima mostly overlaps former Plateaux search space; Djoue-Lefini overlaps Pool/Plateaux/Brazzaville hinterland; Congo-Oubangui overlaps Cuvette/Likouala river search space.

Reliability grades used in this file:
- **A** = primary or official for the fact asserted: government/ministry/ARPCE/ANSSI/E2C page, donor project page/document, official operator facility page, official cloud-region page, Uptime Institute record, Journal Officiel/government legal act.
- **B** = strong secondary: Agence Ecofin, ADIAC, ACI, Digital Business Africa, DCD, Telecompaper, We Are Tech Africa, French Treasury sector note, local press quoting named officials.
- **C** = lead only: directories, market reports, social posts, unquoted vendor claims, ambiguous hosting/cloud claims, policy-only statements.

## 0. Ground Rules

- There is **no public national datacenter registry** for Congo-Brazzaville. Build the inventory by joining official telecom/regulator evidence, donor project records, official operator pages, IXP evidence, energy/permit clues, and trade press.
- Search in French first. High-yield terms: `centre de donnees`, `datacenter`, `data center`, `centre de stockage de donnees`, `hebergement`, `hebergement serveur`, `colocation`, `salle serveurs`, `cloud souverain`, `souverainete numerique`, `Tier III`, `Tier 3+`, `point d'echange Internet`, `IXP`, `CGIX`, `CGIX-PN`, `fibre optique`, `dorsale`, `CAB`, `WACS`, `2Africa`, `station d'atterrage`, `poste electrique`, `MVA`, `MW`, `permis de construire`, `EIES`, `appel d'offres`.
- Disambiguate from DRC every time. Republic of Congo evidence normally says Brazzaville, Pointe-Noire, Oyo, ARPCE, Congo Telecom, Congo-Brazzaville, or Republic of Congo. DRC evidence often says Kinshasa, Lubumbashi, RDC, ARPTC, SNEL, GUPEC, Raxio, OADC.
- Count physical facilities, not policy objectives, corporate offices, generic cloud services, tower sites, cable landing points, or telco POPs. A facility record needs physical siting or facility language such as data center, racks, technical rooms, white space, colocation, IXP host, Tier design/certification, launch, construction, or commissioning.

## 1. Official and Regulatory Sources

### 1.1 Ministry of Posts, Telecommunications and Digital Economy

Use first for the national datacenter programme and official operator/agency context.

Verified URLs:
- Ministry homepage: https://postetelecom.gouv.cg/
- ARPCE organ page: https://postetelecom.gouv.cg/organes/arpce/
- Congo Telecom organ page: https://postetelecom.gouv.cg/organes/congo-telecom/
- Ministry article on the national datacenter: https://postetelecom.gouv.cg/congo-vers-une-revolution-numerique-avec-le-lancement-imminent-du-data-center-national/
- Ministry/operator examples: https://postetelecom.gouv.cg/airtel-congo-b/ and likely sibling pages for MTN/Congo Telecom.

Use as **A** for ministry statements, operator existence, government programme status, and official project descriptions. Do not use it alone to infer commercial colocation unless it names a facility or service.

Queries:

```text
site:postetelecom.gouv.cg "data center"
site:postetelecom.gouv.cg "centre de donnees"
site:postetelecom.gouv.cg datacenter
site:postetelecom.gouv.cg "Bacongo" datacenter
site:postetelecom.gouv.cg "Oyo" "data center"
site:postetelecom.gouv.cg "CGIX"
site:postetelecom.gouv.cg "Congo Telecom" hebergement
"Ministere des Postes" Congo "datacenter national"
"Leon Juste Ibombo" "data center" Congo
```

Extract: project name, city/department, arrondissement/quartier, build status, opening target, contractor, managing delegate, intended tenants, funding, and whether the page proves a facility or only policy.

### 1.2 ARPCE - telecom regulator and IXP sponsor

Verified URLs:
- ARPCE homepage: https://www.arpce.cg/
- ARPCE communications: https://arpce.cg/communications
- ARPCE IXP page: https://www.arpce.cg/point-echange-internet
- CGIX-PN official/near-official local coverage: ADIAC reports that CGIX-PN was launched on 20 September 2024 and hosted in the new ARPCE Tier 3+ datacenter in Pointe-Noire: https://www.adiac-congo.com/content/technologie-lancement-du-deuxieme-point-cgix-de-larpce-pointe-noire-159992

Use ARPCE pages as **A** for regulator, licence, IXP, and official-operator facts. Use ADIAC/ACI/Agence Ecofin/DCD coverage as **B** for ARPCE datacenter facts when ARPCE pages are unavailable or JS-heavy.

Queries:

```text
site:arpce.cg "centre de donnees"
site:arpce.cg "data center"
site:arpce.cg datacenter
site:arpce.cg "point d'echange Internet"
site:arpce.cg CGIX
site:arpce.cg "Pointe-Noire" "Tier"
site:arpce.cg "licence" "operateur"
"ARPCE" "datacenter" "Pointe-Noire"
"ARPCE" "Tier 3+" "Pointe-Noire"
"CGIX-PN" "datacenter"
```

Extract: facility host, IXP members, launch dates, licence category, operator legal name, department/city coverage, service scope, and whether the record proves network service only or a physical facility.

### 1.3 ANSSI and data-protection sources

Verified URLs:
- ANSSI homepage: https://anssi.cg/
- ANSSI about: https://anssi.cg/agence/a-propos
- Cybersecurity/RGSSI lead: https://lejournalducongo.com/22/04/2026/cybersecurite-le-congo-franchit-une-etape-cle-avec-le-futur-referentiel-general-de-securite-des-systemes-dinformation-rgssi/
- ARPCE/ANSSI partnership lead: https://www.adiac-congo.com/content/cybersecurite-nationale-larpce-et-lanssi-unissent-leurs-forces-pour-proteger-lespace

ANSSI is a compliance and sovereign-hosting lead generator, not a datacenter register. Use ANSSI as **A** only when its own pages name a hosting/facility decision or standard. Third-party cybersecurity articles are **B/C** depending on sourcing.

Queries:

```text
site:anssi.cg "centre de donnees"
site:anssi.cg datacenter
site:anssi.cg hebergement donnees
site:anssi.cg "cloud"
"ANSSI" Congo "data center"
"RGSSI" Congo hebergement
"protection des donnees" Congo commission hebergement
```

### 1.4 Energy, grid, and environmental/permit sources

Verified URLs:
- E2C utility: https://e2c.cg/
- Government energy category: https://gouvernement.cg/category/infrastructures/energie-hydraulique/
- French Treasury sector note confirms E2C aerial fibre capacity and Congo Telecom/Silicone Connect use: https://www.tresor.economie.gouv.fr/Pays/CG/le-secteur-du-numerique

No searchable national building-permit registry was found. Building permits are expected at commune/urbanism level; environmental studies may surface through donor documents, ministries, or consultants. Treat named permits/EIES as **A/B** depending on issuer; generic construction mentions remain leads.

Queries:

```text
site:e2c.cg "data center"
site:e2c.cg "centre de donnees"
site:e2c.cg "Brazzaville" "poste"
site:e2c.cg "Pointe-Noire" "poste"
site:gouvernement.cg energie "Brazzaville" datacenter
"datacenter national" Bacongo electricite OR E2C OR MVA OR MW
"ARPCE" "Pointe-Noire" datacenter electricite OR MVA OR MW
"Moukoukoulou" barrage Bouenza
"Imboulou" centrale Plateaux Cuvette
"Liouesso" centrale Sangha
"permis de construire" datacenter Congo Brazzaville
"EIES" "centre de donnees" Congo
```

Extract exact power meaning: grid connection, substation, site load, IT load, MVA/MW, generator/fuel, cooling/water, permit dates, and commissioning.

### 1.5 Procurement and donor projects

Verified URLs:
- AfDB national datacenter article (French): https://www.afdb.org/fr/news-and-events/congo-le-nouveau-datacenter-finance-par-la-banque-africaine-de-developpement-va-consacrer-la-souverainete-numerique-du-pays-et-de-la-sous-region-70845
- AfDB national datacenter article (English): https://www.afdb.org/en/news-and-events/congo-new-data-centre-funded-african-development-bank-will-cement-national-and-subregional-digital-sovereignty-70847
- AfDB project procurement documents search: https://www.afdb.org/fr/documents/project-related-procurement
- World Bank PATN press release: https://www.banquemondiale.org/fr/news/press-release/2022/06/14/afw-la-banque-mondiale-accompagne-lacceleration-de-la-transformation-numerique-en-republique-du-congo
- World Bank P175592 documents: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099630005112275398
- Two national datacenter tender coverage: https://www.agenceecofin.com/breves-telecom/2502-95380-congo-12-societes-se-disputent-le-marche-de-construction-des-deux-centres-de-donnees-nationaux
- Tender-launch mirror: https://leonjusteibombo.cg/2021/11/23/congo-lancement-dun-appel-doffre-pour-la-construction-dun-data-center-national/

Use donor pages as **A** for financing/project scope. Use procurement notices as **B** for planned facilities until award/site/construction evidence is found.

Queries:

```text
site:afdb.org Congo datacenter
site:afdb.org Congo "data centre" Brazzaville
site:documents.worldbank.org P175592 Congo digital acceleration
site:projects.worldbank.org P175592 Congo
"Congo" "appel d'offres" datacenter Oyo Brazzaville
"datacenter national" Congo Sumec Bacongo
"datacenter national" Congo "mai 2026"
"Oyo" "centre de donnees" Congo
```

### 1.6 Official cloud-region negative controls

Use these as **A** only for cloud-region existence/non-existence. No official AWS, Azure, Google Cloud, or OCI public cloud region is in CG in the checked public lists.

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Microsoft Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

Queries:

```text
"Brazzaville" "AWS Direct Connect" OR "ExpressRoute" OR "Cloud Interconnect" OR "FastConnect"
"Pointe-Noire" AWS Azure Google Oracle "data center"
"Congo-Brazzaville" "cloud region"
"ST Digital" Brazzaville cloud colocation
```

### 1.7 Uptime Institute

- Awards list: https://uptimeinstitute.com/uptime-institute-awards/list

No public Uptime Institute listing for a CG facility surfaced in this review. Treat `Tier III`/`Tier 3+` as design, compliance, or operator claim unless the Uptime list confirms the exact facility and certification type.

Queries:

```text
site:uptimeinstitute.com Congo Brazzaville
site:uptimeinstitute.com "Pointe-Noire"
site:uptimeinstitute.com "ST Digital" "Brazzaville"
site:uptimeinstitute.com ARPCE Congo
```

## 2. Verified Facility and Lead Seeds

| Facility / project | Department | Evidence and grade | Status and handling |
|---|---|---|---|
| **Datacenter national du Congo - Bacongo, Brazzaville** | Brazzaville | AfDB official article **A**: https://www.afdb.org/fr/news-and-events/congo-le-nouveau-datacenter-finance-par-la-banque-africaine-de-developpement-va-consacrer-la-souverainete-numerique-du-pays-et-de-la-sous-region-70845. Ministry page **A**: https://postetelecom.gouv.cg/congo-vers-une-revolution-numerique-avec-le-lancement-imminent-du-data-center-national/. Status press **B**: https://www.digitalbusiness.africa/congo-le-datacenter-national-operationnel-dici-mai-2026-selon-le-president-de-la-bad/ and https://lejournalducongo.com/26/02/2026/brazzaville-le-futur-data-center-national-et-le-projet-de-satellite-souverain-entrent-dans-leur-phase-finale-pour-transformer-le-paysage-numerique-congolais/ | Confirmed under-construction / near-completion project. Bacongo, three levels plus basement/technical rooms, Tier III target, Sumec contractor, CAB/AfDB financing. Latest reliable public status found in this review was 95%/operational target around May 2026; no robust public inauguration/operational proof was found, so do **not** mark operational without a newer official launch. |
| **ARPCE Data Center - Pointe-Noire** | Pointe-Noire | DCD **B**: https://www.datacenterdynamics.com/en/news/republic-of-congo-launches-data-center-in-pointe-noire-for-2africa-cable/. Agence Ecofin **B**: https://www.agenceecofin.com/equipement/2902-116638-le-congo-renforce-son-infrastructure-numerique-avec-la-mise-en-service-d-un-nouveau-centre-de-donnees-de-6-3-millions-nbsp. ADIAC CGIX-PN host **B**: https://www.adiac-congo.com/content/technologie-lancement-du-deuxieme-point-cgix-de-larpce-pointe-noire-159992. Directory lead **C**: https://www.datacenters.com/arpce-arpce-pointe-noire-tier-3 | Operational/commissioned on 28 Feb 2024 by ARPCE; reported 3.8bn FCFA / about USD 6.3m; Tier 3+ claim; hosts CGIX-PN from 20 Sep 2024. DCD reports 54 racks / 156 sqm; keep capacity as **B/C** until an ARPCE datasheet is found. |
| **ARPCE Data Center - Brazzaville 2021** | Brazzaville | DCD/Telecompaper cite ARPCE DG saying ARPCE built a Brazzaville datacenter in 2021 **B**: https://www.datacenterdynamics.com/en/news/republic-of-congo-launches-data-center-in-pointe-noire-for-2africa-cable/ and https://www.telecompaper.com/news/congo-launches-facility-to-store-sovereign-data-in-pointe-noire--1494296 | Real lead but identity/address must be resolved. Do not merge automatically with ST Digital or the AfDB-funded Bacongo national DC; the 2021 date suggests a separate ARPCE/government facility or first ARPCE DC. |
| **ST Digital Brazzaville datacenter** | Brazzaville | Official operator page **A**: https://st.digital/en/datacenters and https://st.digital/datacenters. Colocation page **A**: https://st.digital/en/colocation. Cloud store: https://cloudstore.africa/ | Operator confirms a Brazzaville datacenter offering colocation/cloud/DRP/BCP and Tier 3/Tier III language. Grade official service/location as **A**; grade Uptime certification as unverified unless found on Uptime list. Need exact address and local licence/compliance joins. |
| **Data center national secondaire - Oyo** | Cuvette | Tender coverage **B**: https://www.agenceecofin.com/breves-telecom/2502-95380-congo-12-societes-se-disputent-le-marche-de-construction-des-deux-centres-de-donnees-nationaux | Planned/tender lead only. February 2022 tender had separate bidding for Brazzaville and Oyo. No public award/construction/operation evidence was found in this review. |
| **CGIX / CGIX-PN** | Brazzaville; Pointe-Noire | ARPCE IXP page **A**: https://www.arpce.cg/point-echange-internet. ISOC Pulse tracker **B+**: https://pulse.internetsociety.org/fr/ixp-tracker/country/CG/. ADIAC CGIX-PN launch **B**: above. | IXPs are not standalone datacenters. CGIX-PN is hosted in ARPCE Pointe-Noire DC. CGIX-BZV launch/host site must be joined to ARPCE or PeeringDB before using as facility evidence. ADIAC reports a third CGIX planned at Oyo; treat as planned interconnection lead. |
| **Congo Telecom carrier / landing-station facilities** | Kouilou; Pointe-Noire; Brazzaville | Ministry Congo Telecom **A**: https://postetelecom.gouv.cg/organes/congo-telecom/. Operator site **A** for company: https://congotelecom.cg/. French Treasury **B+** for WACS/2Africa/backbone facts: https://www.tresor.economie.gouv.fr/Pays/CG/le-secteur-du-numerique. Directories for PNR1 **C**: https://colo.exchange/data-centers/congo-telecom-congo-telecom-carrier-facility-pnr1 and https://www.datacenterslist.com/data-centers/congo-telecom-carrier-facility-pnr1-pointe-noire | Treat WACS Matombi and 2Africa shore facilities as cable/telecom infrastructure, not datacenters. PNR1 is a C-grade facility lead until Congo Telecom, ARPCE, PeeringDB, or customer evidence confirms colocation/rack service. |

## 3. Department Coverage and Strategy

Run both exact department and city/anchor terms. For the current 15-department official overlay, add the new names shown below but store results under the requested 12 manifest unless the downstream schema changes.

Generic query block:

```text
("{department}" OR "{capital}" OR "{alias}") (datacenter OR "data center" OR "centre de donnees" OR "salle serveurs" OR colocation OR hebergement) Congo -RDC -Kinshasa
("{city}") ("fibre optique" OR backbone OR dorsale OR IXP OR "point d'echange Internet" OR "poste electrique") (datacenter OR "centre de donnees" OR "{operator}")
site:arpce.cg "{city}"
site:postetelecom.gouv.cg "{city}"
site:e2c.cg "{city}"
"{operator}" "{city}" (datacenter OR colocation OR hebergement OR POP OR "point de presence")
```

| Manifest department | Search aliases and anchors | Priority | Concrete strategy |
|---|---|---:|---|
| Bouenza | Madingou, Nkayi, Moukoukoulou | Medium | Energy/fibre corridor. Search Moukoukoulou dam/SEMC/AKSA and E2C fibre; expect power/backbone rooms rather than colocation. |
| Brazzaville | Bacongo, Makélékélé/Makelekele, Poto-Poto, Moungali, Ouenzé/Ouenze, Talangaï/Talangai, Mfilou, Madibou, Djiri, Mpila, Plateau des 15 ans | Very high | Seed national DC Bacongo, ST Digital, ARPCE 2021 lead, CGIX-BZV, Congo Telecom/MTN/Airtel rooms. Dedupe government DC vs ARPCE 2021 vs ST Digital by operator/address/date. |
| Cuvette | Owando, Oyo, Boundji; current overlay: Congo-Oubangui/Mossaka partly split from former Cuvette | High planned | Search Oyo national secondary DC and third CGIX plan; require award/construction before counting. Include Owando/Mossaka river-fibre terms for current-boundary searches. |
| Cuvette-Ouest / West Cuvette | Ewo, Kelle, Mbomo, Okoyo, Etoumbi, Mbama | Low | Low colo probability. Search only for government service rooms, FASUCE, fibre, VSAT, and disaster-recovery rhetoric. |
| Kouilou | Loango, Hinda, Matombi, Tchimpounga, Djeno | High infrastructure | WACS Matombi and 2Africa shore route are connectivity leads. Do not count landing stations as DCs unless rack/colo facility evidence appears. |
| Lekoumou | Sibiti, Zanaga, Komono | Low/medium | Mining and government edge-room searches. Treat any Zanaga/mining IT room as enterprise private unless colocation offered. |
| Likouala | Impfondo, Betou/Bétou, Liranga; current overlay: Congo-Oubangui split can affect Liranga/Mossaka searches | Low | Riverine/northern connectivity. Search VSAT, fibre extension, government intranet, and border connectivity; expect no public colo. |
| Niari | Dolisie, Mossendjo, Loubomo, Moutamba | Medium | Pointe-Noire-Brazzaville rail/fibre corridor and operator POPs. Count only if facility/rack language appears. |
| Plateaux | Djambala, Gamboma, Imboulou, Abala, Ollombo, Makotipoko; current overlay: Nkeni-Alima/Gamboma | Low/medium | Imboulou power and RN2/fibre context; use Nkeni-Alima/Gamboma after 2024 reform. Avoid treating energy projects as datacenters. |
| Pointe-Noire / Black Point | Pointe-Noire, Black Point, Loandjili, Tie-Tie/Tié-Tié, Mvoumvou, Lumumba, Mongo-MPoukou, Ngoyo, Port autonome, Agostinho Neto | Very high | Seed ARPCE Tier 3+ DC, CGIX-PN host, Congo Telecom PNR1 lead, SOFIA business ISP, WACS/2Africa adjacency. Separate city DC from Kouilou/Matombi landing site. |
| Pool | Kinkala, Mindouli, Mayama, Djoue/Djoué, Goma Tse-Tse, Kintélé; current overlay: Djoue-Lefini/Odziba partly split | Medium | Brazzaville hinterland, Djoue hydro, RN1/RN2 corridors. Search Djoue-Lefini/Odziba after 2024 reform, but expect connectivity not colo. |
| Sangha | Ouesso/Ouésso, Pokola, Kabo, Ngombe/Ngombé, Sembé | Medium | CAB phase-2 fibre to Cameroon/CAR, logging towns, Ouesso edge rooms. Treat facilities as POP/backbone unless explicit datacenter evidence. |

## 4. Evidence Capture Rules

For every candidate record capture:

```text
facility_name:
operator_or_owner:
department_manifest_12:
current_department_if_different:
city_quartier_address:
status: operational | commissioned | under construction | planned | tender | lead-only | rejected
source_grade_by_fact:
source_urls:
physical_evidence: racks | rooms | MW/MVA | Tier | IXP host | landing station | POP | office
capacity:
power_cooling:
connectivity:
tenant_or_service_scope:
dedupe_notes:
country_disambiguation:
```

Status hierarchy: official/operator operational page or inauguration > commissioning coverage > under-construction official/donor page > contract award > tender > policy/strategy. Capacity hierarchy: official datasheet > operator statement > trade press quoting operator > directory. Do not promote a C-grade directory lead without a non-directory join.

## 5. Rejection Patterns

- DRC/Kinshasa/Lubumbashi sources unless they explicitly describe a cross-border CG facility.
- Hyperscale region claims for AWS/Azure/GCP/OCI in Congo-Brazzaville unless the provider region page names CG.
- WACS/2Africa landing stations counted as datacenters without adjacent facility evidence.
- `cloud`, `hebergement`, or `hosting` services with no Congo physical site.
- Ministry or bank server rooms unless named as a significant data center, disaster-recovery site, or colocation facility.
