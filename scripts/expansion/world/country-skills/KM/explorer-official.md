# KM Explorer Official — Comoros Datacenter Enumeration via Official, Regulatory, Project-Financing, Cable, and Public-Sector Sources

Date: 2026-08-12. Country: **KM Comoros (Union des Comores)**. Division model: **3 divisions** from `world-manifest.jsonl` (subnational type: geographical unit): **Anjouan**, **Grande Comore**, **Moheli**. Angle: **official / regulatory / primary-source methodology** for finding operational, under-construction, planned, and institutional datacentre facilities. Mayotte is a French overseas department and is **out of scope** even though Comoros–Mayotte cable links (Avassa, FLY-LION3) cross into it.

Reliability grades: **A** = official/primary source that proves the exact claim being recorded (Journal Officiel text or decision, ANRTIC decision/communiqué, ANADEN or Comores Câbles official page/statement, AfDB/World Bank/IsDB project document, Cour Suprême audit report, operator official page, cable-system/consortium official page, hyperscaler official region page). **B** = reputable press/trade source with named parties, dates, and places (Al-Watwan, La Gazette des Comores, Habari za Comores, Comores Infos, Masiwa Komor, Focus-OI, Agence Ecofin, Data Centres Africa, Techpoint Africa, DCD, Developing Telecoms, Submarine Networks when not the cable owner/operator). **C** = directories, marketplaces, SEO hosting pages, social posts, republished press, or claims without address/facility evidence. Do not promote a press item to A simply because it reports an official statement; cite the underlying official source separately.

---

## 0. Verified national baseline

- Comoros is a very small, telecom- and government-led island market (three islands, ~0.9M people). Datacentre-relevant infrastructure is concentrated on **Grande Comore**, especially the **Moroni / Itsandra** area. Anjouan (Mutsamudu) and Moheli (Fomboni) have cable landings and telecom PoPs but no public dedicated DC evidence was found in this pass.
- **One confirmed national/public facility from official and trade sources:**
  - **Data Center de l'Administration Publique (national / public-administration data centre)**, co-managed by **ANADEN** (Agence Nationale de Développement du Numérique) and **Comores Câbles (Comoros Cables S.A.)**. The verified ANADEN page states that ANADEN and Comores Câble announced inauguration of the national data center on **2025-05-19** and describes secure hosting, centralisation, backup of public data, IT-resource mutualisation, and service resilience. Press/trade reports on 2025-05-14/15 add the claimed **Tier 3** category and **44.4 Tb hosting capacity** (unit ambiguous as published; treat as stated, do not convert or interpret as MW). The **AfDB PADEC project** (P-KM-G00-001, “Projet d'Appui à la Digitalisation de l'Économie Comorienne”, approved 2024) is an A-grade financing source for a datacenter/incubator digital-infrastructure programme; use its project page and appraisal/procurement documents for scope, executing agency, grant amount, procurement status, and secondary-DC upgrade wording.
  - Grade honesty: existence, co-management, and inauguration date are **A** from ANADEN. PADEC scope and financing are **A** from AfDB. Claimed Tier 3 and the 44.4 Tb figure are **B unless found on an official ANADEN/Comores Câbles/AfDB document in the active citation chain**. The **“Tier 3” label is self-declared until proven otherwise: no TIA-942/EPI/Uptime certification entry for Comoros was found in this pass**. Record Tier as `claimed Tier 3 (certification not found)` and recheck certification registries every refresh.
  - **Address/parcel not public in this pass.** Assign to **Grande Comore** (Moroni-area; some reports associate the digital programme with Moroni; verify exact commune/quartier — e.g., Moroni-Bambao vs Itsandra — via ANADEN, Comores Câbles, Al-Watwan, or the Journal Officiel before fixing a sub-island location).
- **One secondary datacentre upgrade is financed** under PADEC (“mise à niveau du secondaire” in the AfDB procurement plan). Identity of the existing facility is **unverified**: candidates are a Comores Telecom server facility (HQ Place Volo-volo, BP 7000, Moroni) and/or a government IT facility. Treat as a **lead** until a primary source names the facility.
- **Operators (duopoly):** **Comores Telecom** (historic state operator; Huri mobile brand; 20 years of operations celebrated 2025; 5G frequency attribution by ANRTIC 2025-05-27) and **Yas Comores** (ex-**Telma Comores**, part of **AXIAN Telecom**; second licensee since 2016; first to launch 5G 2025-05-16; ~€25M network investment announced mid-2025). Both are licensed by **ANRTIC** (Agence Nationale de Régulation des TIC). No public DC evidence for either operator was found in this pass; their HQ/NOC/server rooms are leads.
- **Comores Câbles S.A.** (est. ~2016 in the RCIP4/World Bank connectivity programme; new HQ inaugurated 2023-11 in Moroni) operates the submarine-cable landings and the national backbone and co-manages the national DC. Its Jan-2023 Cour Suprême audit report (coursupremecomores.km) is official primary evidence on assets — useful for facility verification.
- **Cable/landing inventory (connectivity infrastructure, NOT datacentres by default):** landing points per GeoCables: **Moroni (4 cables)**, **Chindini (2)**, **Mutsamudu/Anjouan (2)**, **Fomboni/Moheli (1)**. Cables: **EASSy** (Moroni, ~2012), **Avassa** (2016, Comoros–Mayotte; Chindini/Moroni/Mutsamudu/Mamoudzou), **FLY-LION3** (Moroni–Kaweni, 400 km; consortium Comores Câbles/Orange/SRR; connected to the **Itsandra** landing station), **2Africa Comoros branch** (landed Itsandra beach 2023-01-12; Comores Câbles role; service status per operator announcements — verify), and the **Comoros Domestic Cable/backbone** (inter-island; naming varies by source — verify on TeleGeography/Submarine Networks and comorescables.km). Promote a landing station to a facility record only if a source says it hosts servers/colo/cloud or there is a planning/operator record for a data hall.
- **No carrier-neutral colocation provider, no hyperscaler region, and no TIA-942/EPI/Uptime-certified facility were confirmed.** Recheck official cloud-region pages and certification registries during each refresh.
- **No public capacity figures (MW/racks/sqm) exist for any Comoros facility.** Do not infer capacity from “Tier 3”, “44.4 Tb”, capex, or cable bandwidth. Use `capacity_mw: null` unless an explicit primary source states capacity.

### Source URL validation notes from this pass

These routes were checked for existence or discoverability in August 2026:

| Source | URL | Validation result | Enumerator handling |
|---|---|---|---|
| Journal Officiel | https://journalofficiel-km.com/ | HTTP 200 by direct check | Use for laws/decrees; search may require exact French terms and dates. |
| ANADEN réalisations | https://anaden.org/realisations | HTTP 200; page text includes the May 2025 national data-center launch | Primary source for existence/date/co-management and public-data hosting purpose. |
| ANRTIC | https://www.anrtic.km/ | Search/browser retrieval works; direct HEAD to article pages may return 403 | Do not mark dead on curl HEAD alone; use browser/search or normal GET. |
| AfDB PADEC | https://mapafrica.afdb.org/fr/projects/46002-P-KM-G00-001 and https://www.afdb.org/en/documents/comoros-comorian-economic-digitalization-support-project-padec-project-appraisal-report | Indexed/openable through search; direct curl may hit Cloudflare | Treat as live; capture PDF/document URL and project ID in records. |
| Comores Câbles | https://comorescables.km/ | HTTP 200 | Primary source for company/cable claims; DC claims still need facility-level evidence. |
| Comores Telecom | https://www.comorestelecom.km/ | HTTP 200 with `curl -k`; TLS chain may fail strict curl | Treat site as live but note TLS-validation caveat in crawl logs. |
| Yas Comores | https://www.yas.km/ | HTTP 200 | Primary source for operator identity/services. |
| AXIAN Telecom | https://www.axian-telecom.com/ | HTTP 200 | Primary source for Yas group financing and rollout statements. |
| egouv.km | https://egouv.km/ | HTTP 302 to `/en/`, then 200 | Government portal; useful for ministries/platforms, not a DC register. |
| Cour Suprême | https://www.coursupremecomores.km/ | HTTP 200 | Primary audit-report source for state-company assets. |

---

## 1. Official and primary sources

### 1.1 Legal gazette, legislation, and administrative decisions

Primary routes:
- **Journal Officiel de l'Union des Comores**: https://journalofficiel-km.com/ (official publication of laws, decrees, orders, administrative acts; unique official source since 1975 per the institution's own description).
- Ministry of Justice legal repository: https://justice.gouv.km/legislation-et-textes-officiels/
- e-Gov government portal: https://egouv.km/

Use the Journal Officiel for: law numbers and dates (including the data-protection law), decrees creating/chartering ANADEN, Comores Câbles, ANRTIC, SONELEC, and the PADEC/PPP instruments, 5G and licence decisions, and any official notice tied to datacentre, incubator, or digital-infrastructure projects.

Queries (quote the French phrases; run single concepts separately if the engine mishandles `OR`):
```text
site:journalofficiel-km.com ("données à caractère personnel" OR "protection des données")
site:journalofficiel-km.com (ANADEN OR numérique OR "data center" OR "centre de données")
site:journalofficiel-km.com ("Comores Câbles" OR "câbles sous-marins" OR backbone)
site:journalofficiel-km.com (5G OR fréquences OR ANRTIC)
site:egouv.km (numérique OR "économie numérique" OR "data center" OR "centre de données")
```

Extract from each record: instrument number/date, issuing authority, legal entity concerned, object, and source URL/file.

### 1.2 Communications regulator and telecom law

Primary route:
- **ANRTIC** — Agence Nationale de Régulation des Technologies de l'Information et de la Communication: https://anrtic.km/ (also www.anrtic.km). Sections: Régulation (Avis & Décisions, Lois, Décrets, Arrêtés, Contentieux), Observatoires (quality of service), Appels d'offres, Rapports, Études & enquêtes.

ANRTIC defines the licensed-operator universe, frequency assignments, numbering, and quality-of-service obligations; it also oversees personal-data handling by licensed operators per its regulatory framework. Use it to pivot from licensees to facilities; it is **not** a complete facility register. Key recent decisions found in this pass: 5G frequency attributions to **YAS COMORES** and to **Comores Telecom** (both 2025-05-27). Historical context: the second licence was awarded to Telma Comores in Oct 2015 (US$16M fee), operations from 2016. The current framework-law instrument numbers were not confirmed in this pass — verify via ANRTIC “Textes de référence” / Journal Officiel rather than citing from memory.

Queries:
```text
site:anrtic.km (5G OR "attribution de fréquence" OR licence)
site:anrtic.km ("Comores Telecom" OR "Comores Télécom" OR Yas OR Telma)
site:anrtic.km ("données à caractère personnel" OR "protection des données")
site:anrtic.km ("data center" OR "centre de données" OR hébergement)
site:journalofficiel-km.com ("communications électroniques" OR télécommunications)
```

### 1.3 Datacentre certification registries (negative controls)

These are Grade A when an entry exists; in Comoros the expected result is “no entry”, which is itself a finding to record.

- TIA-942 information / certification route: https://tiaonline.org/942-datacenter/ and the EPI certified-sites list https://www.epi-certification.com/sites/list — search Comoros/KM and filter by country where available.
- EPI certified clients: https://www.epi-certification.com/
- Uptime Institute awards: https://uptimeinstitute.com/uptime-institute-awards/datacenter

Result in this pass: **no Comoros facility found in any registry.** Therefore the national DC “Tier 3” claim is unverified. Recheck on every refresh and record certificate IDs/dates if any appear.

### 1.4 Government digital agency, cable company, ministry, and procurement

Primary routes:
- **ANADEN** — Agence Nationale de Développement du Numérique: https://anaden.org/ (created by decree, Jan 2019). Executing agency of PADEC; drives “Comoros Numérique 2028”; co-manages the national DC. Its “Réalisations” page documents the national DC launch (19 May 2025) under the President and the Minister of Posts, Telecommunications, Digital Economy and Transparency.
- **Comores Câbles S.A.** — https://comorescables.km/ (cable company; official pages on FLY-LION3, 2Africa, backbone; company statements on Cloud/AI-ready infrastructure plans for 2026 — treat as industry lead, not facility proof).
- **Ministère des Postes, Télécommunications, Économie Numérique et Transparence** (name in reporting; a functional ministry website was not confirmed in this pass — use egouv.km, ANRTIC, ANADEN, Journal Officiel, and official social channels).
- **AfDB PADEC**: project pages https://mapafrica.afdb.org/fr/projects/46002-P-KM-G00-001 and https://mapafrica.afdb.org/en/projects/46002-P-KM-G00-001 (JS-rendered; use browser/search snippets if needed), AfDB document page https://www.afdb.org/en/documents/comoros-comorian-economic-digitalization-support-project-padec-project-appraisal-report, appraisal report `comoros_-_ar_-_comorian_economic_digitalisation_support_project_padec.pdf` on afdb.org, and the simplified procurement plan (PPM) of 2025-07-02 (xlsx on afdb.org) which states: supply/install equipment for the construction and operationalisation of a **primary datacentre** and an **incubator**, and **upgrade of the secondary**.
- **IsDB public-administration modernization project**: https://www.isdb.org/project-procurement/fr/appels-doffres/2026/gpn/projet-de-modernisation-de-ladministration-publique-comorienne-par-le-bais — verified as a 2026 GPN for digital administration platforms/interoperability/payment/e-services and an AI lab at IUT. Treat as adjacent demand/integration evidence only; it is **not** a datacentre project unless a later procurement notice names hosting or facility works.
- **World Bank**: Comoros digital/connectivity programme (RCIP4 era, backbone, Comores Câbles establishment) and the reported Yas Comores network loan: https://www.banquemondiale.org/ (country pages; search “Comoros digital” / “transforming telecommunications”).
- **Cour Suprême des Comores — Section des Comptes**: https://www.coursupremecomores.km/ — audit reports (Rapports d'Observations Définitives) on state companies are official primary evidence of assets and operations, e.g. Comores Câbles audit (ROD 2023-01-05) and SONELEC audit.
- **Comoros Open Data**: https://opendata-comores.org/ (ANRTIC and other organisations listed).

Queries:
```text
site:anaden.org ("data center" OR "centre de données" OR "19 mai" OR "Comores Numérique 2028")
site:comorescables.km ("data center" OR "centre de données" OR cloud OR "station d'atterrissement")
PADEC Comores ("centre de données" OR datacenter OR incubateur OR "protection des données")
site:afdb.org PADEC Comores
site:banquemondiale.org Comores (numérique OR télécommunications OR backbone OR "Comores Câbles")
site:coursupremecomores.km ("Comores Câbles" OR SONELEC OR "data center")
site:isdb.org Comores ("administration publique" OR interopérabilité OR "laboratoire IA")
```

### 1.5 Data protection and the future personal-data authority

Primary routes:
- Data-protection law text: “loi portant protection des données à caractère personnel” of the Union des Comoros (text archived at blog.africadataprotection.org, Sep 2025 upload). **Verify the official law number/date and publication via the Journal Officiel — not confirmed in this pass.**
- PADEC includes creation of a **National Authority for the Protection of Personal Data and Access to Information** (per AfDB/techpoint reporting, Oct 2024). Track its establishment: it may publish processing registers, notifications, and licensing that surface hosting/data-storage operators.

Queries:
```text
"Comores" "protection des données à caractère personnel" loi
site:journalofficiel-km.com "protection des données"
"autorité nationale" "protection des données" Comores PADEC
```

### 1.6 Energy, utilities, and environment

Primary routes:
- **SONELEC** — Société Nationale de l'Électricité des Comores (created by 2018 decree merging MAMWE for Grande Comore/Moheli and EDA for Anjouan): official web presence is thin (Facebook page; Devex profile); use the Cour Suprême SONELEC audit (Rapport_SONELEC-VF.pdf on coursupremecomores.km) as primary evidence.
- Water utility context: MAMWE/SONEDE naming varies by period (verify).
- Ministry/agencies in charge of energy and environment for EIA/permitting context.

Use energy records as corroboration for large electrical loads, substations, standby generation, or fuel storage. Do not promote a site solely because it has a generator or a SONELEC power connection. **Grid reliability is a known constraint (frequent outages per local press); DCs in Comoros are expected to run heavy backup generation — do not infer a DC from generator presence.**

Queries:
```text
SONELEC Comores "data center" OR "grande charge" OR central OR MVA OR kVA
site:coursupremecomores.km SONELEC audit électricité
"Comores" "centre de données" "groupe électrogène" OR UPS OR climatisation
```

### 1.7 Submarine cable primary/connectivity chain

| Cable / system | Best primary sources | Comoros signal | Enumeration handling |
|---|---|---|---|
| **EASSy** | EASSy consortium / Submarine Networks system page; TeleGeography | 9 landing stations incl. Comoros; landing at **Moroni** (per Submarine Networks and cable-map sources); in service ~2012 | Record Moroni CLS as connectivity; not a DC without hosting evidence. |
| **Avassa** | Cable-status/GeoCables records; operator consortium material | 260 km Comoros–Mayotte system, in service 2016; landings **Chindini, Moroni, Mutsamudu** (and Mamoudzou, Mayotte) | Comoros-side landings are connectivity; Mayotte facilities are out of scope. |
| **FLY-LION3** | Comores Câbles official page (comorescables.km); consortium site flylion3.lion-submarinesystem.com; Al-Watwan | 400 km Moroni–Kaweni; consortium Comores Câbles/Orange/SRR; connected to the **Itsandra** landing station (reported ~2021); 4,000 Gbit/s system with 2,000 Gbit/s protected (per Comores Câbles statements) | Itsandra station is a key co-location point for cables and possibly future hosting; keep as connectivity unless server/colo evidence appears. |
| **2Africa Comoros branch** | 2Africa official (2africacable.net); Comores Câbles; Al-Watwan | Landed at **Itsandra beach**, Grande Comore, 2023-01-12; Comores Câbles involved; commercial status per operator announcements — verify | Landing station = connectivity; not a DC. |
| **Comoros Domestic Cable / national backbone** | GeoCables/TeleGeography naming; comorescables.km; RCIP4/World Bank docs; Comores Infos (backbone pose, 2016) | Inter-island domestic connectivity (Moroni, Mutsamudu, Fomboni area landings) | Verify system name/ownership (Comores Câbles) and treat as backbone/connectivity, not DC. |

Cable queries:
```text
"Comores" "landing station" Moroni OR Itsandra OR Chindini OR Mutsamudu OR Fomboni
"FLY-LION3" Comores Itsandra OR Moroni station
"2Africa" Comores Itsandra atterrissage OR landing
"EASSy" Comoros Moroni landing
"Avassa" cable Chindini OR Moroni OR Mutsamudu
"Comoros Domestic" cable OR backbone "Comores Câbles"
```

### 1.8 Official cloud-region absence checks

Check official pages on every refresh:
- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of this methodology pass, none lists a Comoros region/local zone. Record local VPS/reseller/cloud pages as service evidence only unless a hyperscaler official page names Comoros.

---

## 2. Division coverage workflow

Run the universal workflow for **each of the 3 manifest divisions**. The table below is the coverage checklist; every division must be either assigned a verified project/lead or explicitly marked no public project found.

| Division | Search priority | Official-first route | Expected yield (honest) |
|---|---:|---|---|
| **Grande Comore** | High | National DC (ANADEN/Comores Câbles) address verification; Comores Telecom HQ (Place Volo-volo, Moroni) server rooms/NOC; Itsandra landing station (FLY-LION3 + 2Africa); Moroni EASSy landing; Chindini landing; egouv.km ministries; PADEC procurement; SONELEC power | 1 confirmed facility (national DC, Tier-3 claim unverified) + 2–4 leads (operator HQ/NOC, CLS sites, ministry server rooms) |
| **Anjouan** | Medium | Mutsamudu landing (Avassa/domestic cable); EDA/SONELEC Anjouan power context; Comores Telecom / Yas PoPs and exchanges; banks (BIC/Exim/BCC branches) | 0 confirmed DC; cable landing(s) + telecom PoPs as leads; mark no public DC found unless new evidence |
| **Moheli** | Low | Fomboni landing (domestic cable); telecom PoPs; SONELEC/MAMWE context | 0 confirmed DC; likely only the Fomboni landing/telecom lead; mark no public DC found |

Division universal query template (replace `{division}` with the manifest spelling):
```text
("{division}" OR "{local variant}") Comores ("centre de données" OR "data center" OR datacenter OR "salle de serveurs")
("{division}" OR "{local variant}") Comores ("station d'atterrissement" OR "câble sous-marin" OR backbone OR NOC)
("{division}" OR "{local variant}") Comores ("groupe électrogène" OR UPS OR climatisation OR serveur OR hébergement)
site:journalofficiel-km.com "{division}" (numérique OR télécom OR câble)
site:anrtic.km "{division}" (licence OR fréquence OR qualité)
site:anaden.org "{division}" (numérisation OR "centre de données")
site:comorescables.km "{division}" (câble OR station OR atterrissement)
```

Local variants: Anjouan = Ndzuwani/Nzwani; Grande Comore = Ngazidja; Moheli = Mwali. Add commune-level terms (Moroni, Itsandra, Chindini, Mutsamudu, Fomboni) for the island they belong to.

---

## 3. Facility seed list for enumerators

This is a seed list, not the final census. Reverify each record during division enumeration and preserve null capacity where no explicit capacity source exists.

| Seed | Preferred division assignment | Status | Grade | Best evidence path |
|---|---|---|---|---|
| Data Center de l'Administration Publique (national DC) | Grande Comore (Moroni-area; verify commune) | Operational / inaugurated 2025-05-19 per ANADEN | A for existence/date/co-management (ANADEN); A for PADEC programme scope (AfDB); B for “Tier 3” and “44.4 Tb” unless an official page is in the active source chain | ANADEN réalisation page; AfDB PADEC project/document/procurement; Agence Ecofin 2025-05-14; Data Centres Africa 2025-05-15; Focus-OI; Journal Officiel/creation decree; address verification pending |
| Secondary datacentre upgraded under PADEC | Grande Comore (candidate: Comores Telecom facility or government IT facility) | Lead (identity unverified) | B/C until primary proof | AfDB PPM 2025-07-02 wording; Comores Telecom / ministry facility verification; Journal Officiel |
| Comores Telecom HQ server rooms/NOC | Grande Comore — Place Volo-volo, BP 7000, Moroni | Lead | B/C until facility proof | comorestelecom.km; ANRTIC licence/decisions; Al-Watwan/Gazette company reporting; SONELEC power context |
| Yas Comores (ex-Telma Comores) core/network sites | Grande Comore (Moroni); network sites on all three islands | Lead | B/C until facility proof | yas.km; axian-telecom.com (€25M IFC loan, 2025-06-20, for 5G/FTTH/FTTO expansion); ANRTIC 5G decision; press on 5G launch |
| Itsandra landing station (FLY-LION3 + 2Africa) | Grande Comore — Itsandra (near Moroni) | Connectivity site | A for cable, not DC | comorescables.km; Al-Watwan 2Africa landing (2023-01-12) and FLY-LION3 items; consortium pages |
| Moroni EASSy landing | Grande Comore — Moroni | Connectivity site | A for cable, not DC | Submarine Networks EASSy; GeoCables/TeleGeography; Comores Câbles |
| Chindini landing | Grande Comore — Chindini | Connectivity site | A for cable, not DC | GeoCables/TeleGeography; Avassa/FLY-LION3 records |
| Mutsamudu landing | Anjouan — Mutsamudu | Connectivity site | A for cable, not DC | GeoCables/TeleGeography; Avassa records |
| Fomboni landing | Moheli — Fomboni | Connectivity site | A for cable, not DC | GeoCables/TeleGeography; domestic cable records |
| PADEC incubator (digital) | Grande Comore (verify) | Under development | A for project financing | AfDB PADEC docs; ANADEN |
| Government/ministry server rooms (egouv, ministries, banks: BCC, BIC, Exim, Banque Postale des Comores) | Grande Comore (Moroni) primarily | Internal/demand leads | C until tender/facility proof | egouv.km; Journal Officiel; PADEC procurement; bank official pages |

---

## 4. Pitfalls and decision rules

- **“Tier 3” is a claim, not a certification.** No TIA/EPI/Uptime entry exists for Comoros in this pass. Record claimed tier with an explicit unverified flag; never convert tier to capacity.
- **“44.4 Tb” is ambiguous as published** (Tbps vs TB; hosting vs transit). Record the figure as stated with the unit caveat; do not convert into MW/racks.
- **Island-level divisions only.** The manifest uses 3 geographical divisions; communes (e.g., Moroni-Bambao vs Itsandra within Grande Comore) are sub-locations to note, not divisions. Do not invent division-level precision.
- **Mayotte is out of scope.** Avassa and FLY-LION3 cross into Mayotte (Kaweni, Mamoudzou); count only Comoros-side landings and facilities.
- **Cable landing stations are not datacentres.** Keep cable records in notes/connectivity unless server/hosting/colo evidence is explicit.
- **Online planning-permit search has very low yield in Comoros.** No e-planning portal was confirmed in this pass; use Journal Officiel, egouv.km, and commune-level records for corroboration, and say so rather than pretending a permit sweep was run.
- **French-first sourcing.** Comorian official and press material is overwhelmingly French: search “centre de données”, “salle de serveurs”, “hébergement”, “station d'atterrissement”, “câble sous-marin”, “économie numérique” alongside English terms.
- **State-company audit reports are underused primary evidence.** Cour Suprême RODs (Comores Câbles 2023, SONELEC) list assets/operations and can confirm or kill facility leads.
- **Press can name real facilities but is not always Grade A.** Al-Watwan, La Gazette des Comores, Habari za Comores, Comores Infos, Masiwa, Agence Ecofin, Data Centres Africa, Techpoint are usually Grade B unless they reproduce a primary document that is separately cited.
- **Avoid `.km`/KM ambiguity.** Always include “Comores”/“Comoros” or an operator/place name; plain “KM data center” can return unrelated ccTLD/SEO noise.
- **No deletion in enumeration.** If an old lead cannot be verified, retain it as a lead with a downgraded grade and a note naming the missing evidence rather than silently dropping it.
- **Grid context.** Frequent SONELEC outages mean generator/UPS presence is near-universal for any ICT room; never count a generator as a datacentre.
