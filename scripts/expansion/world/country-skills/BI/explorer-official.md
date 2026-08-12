# BI Explorer Official - Burundi Datacenter Enumeration

Date verified: 2026-08-12. Country: **BI - Burundi**. Angle: official/regulatory/government-digital sources for identifying datacenter-like facilities, telco core rooms, government hosting infrastructure, university/server-room deployments, and planned national data infrastructure.

Important administrative correction: do **not** label Burundi as a 17-province country. Burundi had 18 provinces from the 2015 creation of Rumonge until the 2025 reform, and the current operational model is **5 provinces**: Buhumuza, Bujumbura, Burunga, Butanyerera, and Gitega. Legacy search coverage must still include all 18 former province names because older tenders, press, operator pages, and donor documents use them. If a downstream schema is fixed to the pre-2015 17-province model, record Rumonge leads against both source legacy parents, Bururi and Bujumbura Rural, and keep the original Rumonge source text in notes.

Reliability grades:
- **A** = official or primary source: ARCT licensing/decrees/statistics/tenders, SETIC/PAFEN/PDDSP/eNama/Primature/finance-ministry documents, operator service pages or tenders, REGIDESO/AREEN/OBPE records, World Bank project documents, official cloud-provider region lists.
- **B** = strong secondary: established local or regional press quoting official material, donor/project coverage, Internet Society/African Union IXP release, PeeringDB for interconnection metadata, recognized trade press.
- **C** = lead only: colocation/hosting aggregators, social posts, LinkedIn job posts, vendor marketing without a named Burundi site, old MoUs, scraped directory entries, unsourced local blogs.

---

## 0. Burundi Source Reality

- Burundi has **no public national datacenter registry** and no reliable online construction-permit search. Enumeration depends on joining telecom licensing, government digital-project documents, operator pages/tenders, energy/environment evidence, procurement notices, IXP/interconnection records, and local press.
- The market is small and mostly **telco/government/server-room driven**, not hyperscale colocation. Count candidates conservatively: SETIC/government hosting, BBS hosting/server hosting, Lumitel/ONATEL/Econet core or cloud services, CNI/NIC.BI registry infrastructure, PAFEN-funded university computing centres, BDIXP/IXP infrastructure, and small Bujumbura hosters.
- **Cloud region availability is negative evidence**. AWS, Azure, Google Cloud, and Oracle OCI official region lists show African regions outside Burundi, mostly South Africa. Do not convert cloud service availability into a Burundi facility record.
- **Bujumbura** is the commercial/telecom centre. **Gitega** is the political capital and a government-project focus. Current provincial searches should use the 5 provinces, then expand to former provinces and communes for source recall.
- French is the main discovery language. Use `centre de donnees`, `data center`, `datacenter`, `centre informatique`, `serveurs`, `hebergement`, `colocation`, `cloud`, `salle de serveurs`, `e-gouvernement`, `digitalisation`, `fibre optique`, and `point de presence`.

---

## 1. Administrative Coverage

### 1.1 Current 5-province model, effective in public reporting after the 2025 reform

| Current province | Capital | Legacy search names to include |
|---|---|---|
| Buhumuza | Cankuzo | Cankuzo, Muyinga, Ruyigi |
| Bujumbura | Bujumbura | Bujumbura Mairie, Bujumbura Rural, Bubanza, Cibitoke, parts of Muramvya, parts of Rumonge |
| Burunga | Makamba | Bururi, Makamba, Rutana, parts of Rumonge, Mahwa/Gitega edge cases |
| Butanyerera | Ngozi | Ngozi, Kayanza, Kirundo, parts of Muramvya |
| Gitega | Gitega | Gitega, Karuzi, Mwaro, parts of Muramvya |

### 1.2 Legacy 18-province search checklist

Run the legacy pass for: Bubanza, Bujumbura Mairie, Bujumbura Rural, Bururi, Cankuzo, Cibitoke, Gitega, Karuzi, Kayanza, Kirundo, Makamba, Muramvya, Muyinga, Mwaro, Ngozi, Rumonge, Rutana, Ruyigi.

Older drafts and some datasets may say "17 provinces"; that is obsolete or internally inconsistent. Rumonge was created in 2015 and appears in 2015-2025 sources, while 2025+ sources increasingly use the 5-province reform.

Administrative verification sources:
- Presidency: current government and 2025 decrees, https://presidence.gov.bi/
- Presidency example of current 5-province language: https://presidence.gov.bi/2025/08/29/le-president-ndayishimiye-a-presente-le-nouveau-gouverneur-de-burunga-et-ladministrateur-de-makamba/
- Presidency governors decree page: https://presidence.gov.bi/2025/07/03/decret-no-100-087-du-03-juillet-2025-portant-nomination-des-gouverneurs-de-province/
- Background/reform cross-check: https://www.burunditimes.com/burundis-new-governors-sworn-in-following-major-provincial-reforms/

---

## 2. Official And Regulatory Sources

### 2.1 ARCT - telecom regulator

ARCT is the operator/licence census and telecom market source, not a facility registry.

- Site: https://arct.gov.bi/
- Licensing/forms: https://arct.gov.bi/license/
- Decrees/laws: https://arct.gov.bi/decret-et-lois/
- Statistics and market observatories: https://arct.gov.bi/statistiques/ and https://arct.gov.bi/observatoires-des-marches/
- Tenders: https://arct.gov.bi/appel-doffres/
- Digital authorization portal: https://portail.arct.gov.bi/ ; ARCT announced its platform for import/export/release authorizations for electronic-communications equipment, operational from 10 November 2025: https://arct.gov.bi/2025/10/24/lancement-de-la-plateforme-numerique-de-gestion-des-autorisations-des-materiels-de-communications-electroniques/
- Q2 2025 observatory confirms mobile operators ECONET LEO, LUMITEL, and ONATEL: https://arct.gov.bi/2025/12/29/observatoire-du-marche-des-services-de-communications-voix-sms-internet-et-services-financiers-mobiles-au-burundi-deuxieme-trimestre-2025/

Use ARCT to identify licensed network/service operators and procurement around telecom infrastructure. A telecom licence alone is **not** a datacenter facility.

Queries:
```text
site:arct.gov.bi licence internet Burundi
site:arct.gov.bi observatoire ECONET LEO LUMITEL ONATEL
site:arct.gov.bi "appel d'offres" fibre OR internet OR equipement
site:arct.gov.bi "centre de donnees" OR "data center" OR hebergement
"ARCT" Burundi "Starlink" OR "services internet"
```

### 2.2 Government digital ministries, SETIC, PAFEN, PDDSP

Primary route:
- Ministry of Communication and Media: https://mincom.gov.bi/ ; Presidency government page confirms the current ministerial portfolio: https://presidence.gov.bi/gouvernement-2/membres-du-gouvernement/
- Former/legacy ICT ministry domain to search for older pages: https://mincotim.gov.bi/
- Ministry of Finance, Budget and Digital Economy: https://finances.gov.bi/
- SETIC: https://setic.gov.bi/
- PAFEN: https://pafen.gov.bi/
- eNama: https://enama.gov.bi/
- Primature PDDSP download page: https://primature.gov.bi/plan-directeur-de-digitalisation-des-services-publics-du-burundi-pddsp-2023-2033/

Verified signals:
- Iwacu reported in May 2021 that SETIC was the government body for ICT promotion, management of a data center, and hosting state institutions' sites/data. This is **B** for the facility claim unless paired with a SETIC source naming the same facility: https://www.iwacu-burundi.org/tic-les-institutions-etatiques-pas-tres-rassurees-par-le-setic/
- SETIC mid-term PAFEN page names national hosting through a Data Center and modernization of the government communications network: https://setic.gov.bi/evaluation-a-mi-parcours-du-projet-pafen-2023-2028/
- SETIC/PAFEN tendered a study for data hosting strategy/infrastructure: https://setic.gov.bi/wp-content/uploads/2024/03/AMI_hebergement-des-donnees_0001.pdf
- PAFEN is a World Bank/IDA-funded digital-foundations project; PAFEN pages cite the USD 92 million IDA grant and its role in broadband access and public digital-service capacity: https://pafen.gov.bi/ and https://pafen.gov.bi/a-propos/
- PAFEN tender page includes acquisition of equipment for **five university computing centres (CIU)**: University of Burundi, ENS, Institut National de Sante Publique, Universite Polytechnique de Gitega, and Universite Espoir d'Afrique: https://pafen.gov.bi/appels-doffres/
- PAFEN BERNET security and administration tenders identify education/research network infrastructure work: https://pafen.gov.bi/termes-de-reference-pour-le-recrutement-dun-consultant-charge-de-la-securite-du-reseau-informatique-de-burundi-education-and-research-network-bernet/ and https://pafen.gov.bi/recrutement-consultant-charge-dappuyer-dans-ladministration-du-reseau-de-burundi-education-andresearch-network-bernet/
- Finance ministry reported a 61% budget engagement for PAFEN at mid-term review on 23 March 2026: https://finances.gov.bi/index.php/2026/03/23/pafen-une-evaluation-a-mi-parcours-pour-accelerer-la-transformation-numerique/
- PDDSP 2023-2033 is official public-service digitalization strategy material. It is a project-plan source for national data/hosting infrastructure, not proof of an operating site until tender/award/construction evidence names a location.

Queries:
```text
site:setic.gov.bi "data center" OR "centre de donnees" OR hebergement
site:setic.gov.bi PAFEN OR PDDSP OR BERNET OR "reseau de communication gouvernementale"
site:pafen.gov.bi "centre informatique universitaire" OR CIU OR BERNET
site:pafen.gov.bi hebergement OR "data center" OR "centre de donnees" OR serveurs
site:finances.gov.bi PAFEN OR numerique OR digitalisation
site:primature.gov.bi PDDSP OR "Plan Directeur de Digitalisation"
site:enama.gov.bi PDDSP OR "centre de donnees" OR CDIN
"Centre de Donnees Integre National" Burundi
"CDIN" Burundi "centre de donnees"
```

### 2.3 BBS - Burundi Backbone System

BBS is now a primary-confirmed hosting/server-hosting lead, not just an aggregator lead.

- Site: https://www.bbs.bi/
- BBS service navigation includes `Hebergement Web` and `Hebergement Serveur`; the homepage also shows server-hosting pricing: https://www.bbs.bi/fr/
- Server/web hosting pricing page: https://www.bbs.bi/fr/sb25/
- Tenders page for fibre/network procurement: https://www.bbs.bi/fr/sb14/Appel_d%E2%80%99Offres
- BBS LinkedIn describes a national fibre backbone connecting provinces and borders: https://bi.linkedin.com/company/burundi-backbone-systems
- Historical finance/context: Agence Ecofin reported an USD 11.5M PTA Bank loan for national fibre: https://www.agenceecofin.com/equipement/2705-11223-burundi-backbone-system-recoit-un-pret-de-11-5-millions-pour-un-reseau-national-de-fibre-optique

Record BBS as:
- **A** for marketed hosting/server-hosting service existence.
- **B/C** for a specific colocation facility unless BBS pages or tenders name the site, room, racks, address, power, or SLA.
- **B** for national backbone/PoP context when supported by BBS, ITU, World Bank/IEG, or strong press.

Queries:
```text
site:bbs.bi hebergement OR serveur OR data OR colocation
site:bbs.bi "appel d'offres" fibre OR equipement OR routeur OR transmission
"Burundi Backbone System" "hebergement serveur" OR "data center"
"BBS" Bujumbura colocation OR "centre de donnees"
```

### 2.4 Operators: ONATEL, Lumitel, Econet Leo, CNI/NIC.BI

Operator official pages are primary for services and offices; they are not enough for facility-level location unless they identify hosting/server/cloud infrastructure.

| Entity | Primary route | Verified official signal | Facility handling |
|---|---|---|---|
| ONATEL | https://onatel.bi/ | ONATEL describes national telecom operations; HQ/service context in Bujumbura. ARCT confirms ONATEL as a mobile operator in 2025. | Core rooms are telco infrastructure leads. Count as facility only with hosting/cloud/DC evidence. |
| Lumitel / Viettel Burundi | https://lumitel.bi/ ; cloud server tab: https://lumitel.bi/package-vas?tab=Cloud+server | Official site gives Bujumbura address and cloud-server service surface. PAFEN/press identify Lumitel in broadband rollout. | **A lead** for marketed cloud service; require site evidence before naming a physical DC. |
| Econet Leo | Econet group release and ARCT; LinkedIn domain lead `econet.bi` | ARCT confirms ECONET LEO as a mobile operator. LinkedIn/job posts mention Data Centre Engineer, but that is a C lead unless official career page is captured. | Treat as telco core/data-centre engineering lead; verify via official domain, tender, or ARCT/press. |
| CNI / NIC.BI | https://www.cni.bi/ and https://nic.bi/ | Legacy computing and .bi registry lead. | Registry/hosting infrastructure is likely Bujumbura but needs a primary page naming server/hosting infrastructure. |

Queries:
```text
site:onatel.bi hebergement OR cloud OR data OR "appel d'offres"
site:lumitel.bi "Cloud server" OR cloud OR entreprise OR data
site:econet.bi "data centre" OR "data center" OR cloud OR "appel d'offres"
site:cni.bi hebergement OR serveur OR data
site:nic.bi serveur OR infrastructure OR hebergement
"Econet Leo" Burundi "Data Centre Engineer"
```

### 2.5 Environment, planning, energy, and power feasibility

Use these as facility corroboration and feasibility checks.

- OBPE: https://www.obpe.bi/ . Search for EIES/NIE records for telecom, fibre, large buildings, diesel generators, substations, solar plants, and government digital projects. No public DC-specific EIES was verified in the reviewed pass.
- REGIDESO: https://regideso.bi/ . Use large-connection, transformer, substation, and urban grid-improvement tenders as power-feasibility evidence.
- AREEN: https://www.areen.bi/ . AREEN is the water/energy regulator; use for tariff/regulatory context, not facility enumeration.
- World Bank Burundi energy context: the country is still electricity-constrained; World Bank notes current programs adding grid generation/access, including Jiji/Mulembwe and Rusumo contributions: https://www.worldbank.org/ext/en/country/burundi and https://www.worldbank.org/en/news/press-release/2024/06/26/accelerating-access-to-clean-afe-and-reliable-electricity-in-burundi

Queries:
```text
site:obpe.bi "etude d'impact" fibre OR "centre de donnees" OR data OR telecom
site:regideso.bi "appel d'offres" transformateur OR poste OR raccordement OR Bujumbura
site:areen.bi electricite OR tarif OR licence OR production
"REGIDESO" Burundi "data center" OR serveurs OR "grand client"
"EIES" Burundi fibre OR telecom OR "centre de donnees"
```

---

## 3. Cloud, Edge, And Interconnection Signals

| Signal | Source | Burundi interpretation |
|---|---|---|
| AWS regions | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Burundi region. Africa region is outside Burundi; negative evidence only. |
| Azure regions | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Burundi region. South Africa North/West are outside Burundi. |
| Google Cloud locations | https://cloud.google.com/about/locations | No Burundi region. Johannesburg is the relevant Africa region. |
| Oracle OCI regions | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Burundi region. Johannesburg and other Africa/Middle East regions are outside Burundi. |
| BDIXP / BurundiX IXP | Internet Society launch: https://www.internetsociety.org/news/press-releases/2014/internet-exchange-point-launched-on-21-march-2014-in-bujumbura-burundi/ ; PeeringDB: https://www.peeringdb.com/ix/2552 ; current site: https://bdixp.org.bi/en/home/ | Bujumbura interconnection infrastructure; **not** DC capacity by itself. |
| Starlink | ARCT/CIO Mag/press and ARCT statistics | Connectivity option and enterprise backhaul lead; not a datacenter. Ground/backhaul evidence would be an edge/telecom record only. |

---

## 4. Facility And Project Seed List

| Candidate | Status | Grade | Location handling | Why it matters |
|---|---|---|---|---|
| SETIC government data centre | Operating lead | B now; A if SETIC source names the facility/site | Likely Bujumbura unless official source says otherwise | Iwacu states SETIC manages a data center and hosts government data; SETIC/PAFEN pages discuss national hosting and government network modernization. |
| National hosting / Data Center under PAFEN | Pipeline | A for tender/study; not operating | Location unknown until award/site | SETIC/PAFEN study and mid-term references show policy/procurement path for national data hosting. |
| CDIN - Centre de Donnees Integre National | Planned | A for plan, not facility | Unknown; search Bujumbura/Gitega | PDDSP/PDDSP-derived government material should be tracked for implementation evidence. |
| Five PAFEN university computing centres (CIU) | Procured/deployed lead | A for tender existence | UB, ENS, INSP, Universite Polytechnique de Gitega, Universite Espoir d'Afrique | Server-room/computing-centre deployments; count as institutional compute rooms, not commercial colocation. |
| BBS hebergement serveur/web | Marketed service | A for service; B/C for physical facility details | Bujumbura/BBS network unless site named | BBS official site lists hosting/server-hosting and prices. |
| Lumitel cloud server | Marketed service lead | A for service page; C/B for facility | Bujumbura operator HQ/core unless site named | Official page has cloud-server surface; physical infrastructure may be local or off-net until verified. |
| ONATEL core rooms / possible hosting | Telco lead | A for operator; B/C for facility | Bujumbura, Gitega, Ngozi likely; require source | Incumbent operator, ARCT-confirmed. Count only if source names hosting/cloud/DC. |
| Econet Leo data centre engineering/core | Telco lead | B/C until official page/tender | Bujumbura likely | ARCT-confirmed operator; LinkedIn job posts are leads only. |
| CNI / NIC.BI registry infrastructure | Registry/hosting lead | B/C until primary infrastructure evidence | Bujumbura likely | .bi registry and legacy computing institution. |
| BDIXP / BurundiX IXP | Interconnection | A/B for IXP existence | Bujumbura | Interconnection point; not a DC unless co-location facility is separately proven. |

---

## 5. Province Search Workflow

Use both current and legacy names in every enumeration cycle.

1. Run current-province searches: Buhumuza, Bujumbura, Burunga, Butanyerera, Gitega.
2. Expand to legacy 18 province names and capital/commune names.
3. For each area, run `site:` searches across ARCT, SETIC, PAFEN, Primature, finance ministry, BBS, OBPE, REGIDESO, AREEN, and operator sites.
4. Search operators plus place: ONATEL, Lumitel, Viettel Burundi, Econet Leo, BBS, SETIC, CNI, NIC.BI, BERNET, Huawei, ZTE.
5. Search project terms: PAFEN, PDDSP, CDIN, CIU, BERNET, COMGOV, eNama, e-gouvernement, fibre optique, point de presence, hebergement.
6. Record negative searches where results are only cybercafes, training rooms, generic ICT offices, school labs, NGO server rooms, or press releases without infrastructure.

High-yield mapping:
- **Bujumbura / legacy Bujumbura Mairie**: SETIC government hosting, BBS hosting/server hosting, ONATEL, Lumitel, Econet Leo, CNI/NIC.BI, BDIXP, banks and payment systems. This is the only credible commercial cluster.
- **Gitega / legacy Gitega, Karuzi, Mwaro**: political capital and university/government project searches; CIU at Universite Polytechnique de Gitega; possible CDIN future-site leads.
- **Butanyerera / legacy Ngozi, Kayanza, Kirundo**: BBS/ONATEL/Lumitel/Econet regional network leads; expect PoPs and telco rooms, not public DCs.
- **Buhumuza / legacy Cankuzo, Muyinga, Ruyigi**: backbone/mobile rollout and donor-project leads; mostly negative commercial searches.
- **Burunga / legacy Bururi, Makamba, Rutana, Rumonge parts**: border/backbone and energy/donor leads; mostly negative commercial searches.
- **Bujumbura province legacy outer areas / Bubanza, Cibitoke, Bujumbura Rural, Rumonge parts**: search fibre/backbone/edge rooms and power projects; do not merge rural edge sites with Bujumbura Mairie facilities unless the source does.

Copy/paste query block:
```text
"Bujumbura" Burundi ("centre de donnees" OR "data center" OR datacenter OR hebergement OR colocation OR cloud)
"Gitega" Burundi ("centre de donnees" OR "data center" OR PAFEN OR CIU OR BERNET OR CDIN)
"Ngozi" Burundi (BBS OR ONATEL OR Lumitel OR Econet) (fibre OR "point de presence" OR serveur)
"Buhumuza" OR Cankuzo OR Muyinga OR Ruyigi Burundi (fibre OR "data center" OR "centre de donnees")
"Burunga" OR Bururi OR Makamba OR Rutana OR Rumonge Burundi (fibre OR "data center" OR "centre de donnees")
"Butanyerera" OR Ngozi OR Kayanza OR Kirundo Burundi (fibre OR "data center" OR "centre de donnees")
```

Legacy exhaustive query block:
```text
Bubanza Burundi "data center" OR "centre de donnees" OR datacenter OR colocation OR fibre
"Bujumbura Mairie" Burundi (BBS OR ONATEL OR Lumitel OR SETIC OR CNI OR BDIXP) "data center" OR hebergement OR colocation OR cloud
"Bujumbura Rural" Burundi "data center" OR "centre de donnees" OR fibre OR "point de presence"
Bururi Burundi "data center" OR "centre de donnees" OR fibre
Cankuzo Burundi "data center" OR "centre de donnees" OR fibre
Cibitoke Burundi "data center" OR "centre de donnees" OR fibre
Gitega Burundi ("data center" OR "centre de donnees" OR BERNET OR PAFEN OR CIU OR CDIN)
Karuzi Burundi "data center" OR "centre de donnees" OR fibre
Kayanza Burundi "data center" OR "centre de donnees" OR fibre
Kirundo Burundi "data center" OR "centre de donnees" OR fibre
Makamba Burundi "data center" OR "centre de donnees" OR fibre
Muramvya Burundi "data center" OR "centre de donnees" OR fibre
Muyinga Burundi "data center" OR "centre de donnees" OR fibre
Mwaro Burundi "data center" OR "centre de donnees" OR fibre
Ngozi Burundi (Econet OR ONATEL OR Lumitel OR BBS) "data center" OR fibre OR "point de presence"
Rumonge Burundi "data center" OR "centre de donnees" OR fibre
Rutana Burundi "data center" OR "centre de donnees" OR fibre
Ruyigi Burundi "data center" OR "centre de donnees" OR fibre
```

---

## 6. Counting, Grading, And De-Dup Rules

- A facility exists only when a source names infrastructure and location with enough specificity to distinguish a physical site. A marketed hosting/cloud service without a named site is a provider-level service lead.
- Keep `facility_type` precise: `commercial_hosting`, `telco_core`, `ixp`, `government_dc`, `planned_national_dc`, `university_compute_centre`, `registry_infrastructure`, `edge_pop`, or `lead_only`.
- Keep status precise: `operational`, `marketed_service`, `procurement`, `planned`, `under_construction`, `unknown`, `negative`.
- CDIN/PDDSP items remain `planned` until an official tender, award, EIES, construction notice, or inauguration names a site.
- PAFEN CIUs are institutional computing centres, not commercial datacenters. Count them separately from national DC/CDIN records.
- BBS hosting/server hosting is A for service existence. Do not assert rack count, MW, Tier, or street address unless BBS or a tender states it.
- Telco mobile/fixed licences and ARCT market shares do not imply countable DCs. Count ONATEL/Lumitel/Econet core rooms only if another source describes hosting/cloud/data-centre/server infrastructure.
- BDIXP/IXP is interconnection infrastructure. It can be a co-location lead, but never a datacenter record on its own.
- Starlink is connectivity, not a facility. Treat ground-station or gateway claims as C until ARCT or SpaceX confirms a Burundi site.
- Capacity fields are normally null in Burundi. Do not infer MW/racks from subscriber count, cloud-service marketing, or fibre kilometres.
- De-dup government infrastructure: SETIC data centre, eNama hosting, national hosting under PAFEN, and CDIN may refer to overlapping or future estates. Keep one canonical physical record when the source proves common location; otherwise keep separate `planned/project` records with cross-references.

---

## 7. Source Priority Checklist

1. ARCT licences, observatories, statistics, tenders, and decrees.
2. SETIC, PAFEN, Primature/eNama/PDDSP, and finance-ministry official documents.
3. BBS, ONATEL, Lumitel, Econet, CNI/NIC.BI official pages and tenders.
4. OBPE EIES/NIE records and commune/construction-permit evidence where available.
5. REGIDESO and AREEN power/regulatory evidence.
6. World Bank project documents and procurement records.
7. Internet Society/African Union/PeeringDB for IXP/interconnection.
8. Local and regional press for corroboration: Iwacu, Burundi Eco, ABP, Le Renouveau, Agence Ecofin, WeAreTech, CIO Mag, TechAfricaNews.
9. Aggregators and social/job posts as C-grade discovery only.

Final note: the most important review correction is the province model. Use 5 current provinces for final 2026 location normalization, legacy 18 province names for search recall, and never repeat "17 provinces" without an explicit explanation that it is an obsolete pre-Rumonge schema.
