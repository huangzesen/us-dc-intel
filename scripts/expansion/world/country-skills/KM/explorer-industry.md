# KM Explorer Industry — Comoros Datacenter Enumeration via Operators, Connectivity Infrastructure, Trade Press, and Division Query Patterns

Date: 2026-08-12. Country: **KM Comoros (Union des Comores)**. Scope: industry/operator-led datacentre discovery across the 3 `world-manifest.jsonl` divisions (**Anjouan**, **Grande Comore**, **Moheli**). Mayotte (France) is out of scope. Reliability grades: **A** = operator/certification/cable/cloud/government primary source that proves the exact claim; **B** = reputable local or trade press with named parties, dates, and places; **C** = directory, marketplace, social, SEO hosting, or unverified aggregate evidence. Press reports of official statements remain B unless the cited official document/page is also captured.

---

## 0. Market shape and verified facts

- The Comoros datacentre market is very small, state-led, and young. **One confirmed facility**: the **Data Center de l'Administration Publique** (national/public-administration DC), co-managed by **ANADEN** and **Comores Câbles**, inaugurated **2025-05-19** per ANADEN. Press/trade reports add claimed Tier 3 and “44.4 Tb” hosting capacity (unit ambiguous; treat as stated). **No independent certification (TIA-942/EPI/Uptime), no carrier-neutral colocation, and no hyperscaler region were confirmed** in this pass.
- **PADEC** (AfDB project P-KM-G00-001, approved 2024): the AfDB document page and appraisal/procurement chain make it the clearest facility pipeline: a datacenter/incubator digital-infrastructure project, plus procurement wording for a primary datacentre and an upgrade of a secondary datacentre. Use AfDB as A-grade for project scope/financing, not for the national DC's claimed Tier unless the document states the tier.
- **Operators (duopoly):** **Comores Telecom** (historic state operator; Huri brand; HQ Place Volo-volo, BP 7000, Moroni; 5G frequency attribution 2025-05-27) and **Yas Comores** (ex-**Telma Comores**, AXIAN Telecom group; second licensee since 2016; first 5G launch reported in May 2025; AXIAN announced a €25M IFC loan in June 2025 for mobile/fixed broadband, 5G, FTTH and FTTO). Neither operator publishes a dedicated datacentre/colo offer; their HQ/NOC/core sites are leads only.
- **Comores Câbles S.A.** (state cable company, est. ~2016 under the RCIP4/World Bank connectivity programme; new HQ inaugurated Nov 2023, Moroni) operates cable landings and the national backbone and co-manages the national DC; its own 2026 roadmap mentions Cloud and AI-ready infrastructure ambitions (lead only).
- **Cables**: EASSy (Moroni), Avassa (Chindini/Moroni/Mutsamudu + Mayotte), FLY-LION3 (Moroni–Kaweni via Itsandra station), 2Africa Comoros branch (Itsandra beach, landed 2023-01-12), Comoros Domestic Cable/backbone (naming to verify). Landing points per GeoCables: Moroni (4), Chindini (2), Mutsamudu (2), Fomboni Moheli (1). All are **connectivity sites unless hosting evidence appears**.
- **Government digital layer**: ANADEN (anaden.org), Comores Câbles (comorescables.km), ANRTIC (anrtic.km), Journal Officiel (journalofficiel-km.com), egouv.km, Comoros Open Data (opendata-comores.org), Cour Suprême audit reports (coursupremecomores.km), AfDB PADEC, and the 2026 IsDB public-administration modernization GPN. The IsDB project is adjacent digital-platform/AI-lab evidence, not a DC by itself.
- **No public MW/rack/sqm figures were found for any facility.** Set `capacity_mw: null` unless a primary source explicitly states a value. Starlink consumer/enterprise service is available in Comoros (per Starlink support posts, Apr 2025) — satellite service, not a DC; gateway location to verify.

### Source URL validation notes

Verified/detectable source behavior in August 2026:

| Source | URL | Result | Handling |
|---|---|---|---|
| ANADEN réalisations | https://anaden.org/realisations | HTTP 200; contains the national DC launch item | A for launch/existence/co-management. |
| ANRTIC | https://www.anrtic.km/ | Browser/search works; direct article HEAD can return 403 | Do not discard; use browser, search cache, or GET. |
| AfDB PADEC | https://mapafrica.afdb.org/fr/projects/46002-P-KM-G00-001 and https://www.afdb.org/en/documents/comoros-comorian-economic-digitalization-support-project-padec-project-appraisal-report | Indexed/openable; curl may hit Cloudflare | A for PADEC project facts when captured. |
| Comores Câbles | https://comorescables.km/ | HTTP 200 | A for company/cable statements. |
| Comores Telecom | https://www.comorestelecom.km/ | HTTP 200 only with relaxed TLS in curl during this pass | Site is live; log TLS-chain caveat if crawler fails. |
| Yas Comores | https://www.yas.km/ | HTTP 200 | A for operator/service facts. |
| AXIAN Telecom | https://www.axian-telecom.com/ | HTTP 200 | A for Yas group financing/rollout statements. |
| egouv.km | https://egouv.km/ | 302 to `/en/`, then 200 | Government portal, not a facility register. |
| Cour Suprême | https://www.coursupremecomores.km/ | HTTP 200 | A for audit-report evidence. |

---

## 1. Priority operator and infrastructure sweep

| Lead | Source route | Locality/division handling | Evidence grade and action |
|---|---|---|---|
| National DC (Data Center de l'Administration Publique) | ANADEN réalisation page; Comores Câbles; AfDB PADEC (mapafrica.afdb.org 46002-P-KM-G00-001; AfDB document page; PPM xlsx 2025-07-02); Agence Ecofin 2025-05-14; Data Centres Africa 2025-05-15; Focus-OI | Grande Comore, Moroni-area; verify commune/quartier; do not fix sub-island location without an address source | **A** for existence/date/co-management from ANADEN and PADEC financing from AfDB; **B** for the “Tier 3” and “44.4 Tb” claims unless an official page is in the active source chain; record capacity as stated only (44.4 Tb, unit ambiguous) |
| Secondary DC upgrade (PADEC) | AfDB PPM wording (“mise à niveau du secondaire”); Comores Telecom / ministry facility checks | Grande Comore candidate (Comores Telecom server facility or government IT facility) | **B/C** lead until a primary source names the facility |
| Comores Telecom | comorestelecom.km; ANRTIC licence/5G decision (2025-05-27); Al-Watwan/Gazette; Cour Suprême/state-enterprise context | HQ Place Volo-volo, BP 7000, Moroni (Grande Comore); exchanges/PoPs on all three islands | **A** for operator identity/address; DC/NOC facility **lead** until primary proof |
| Yas Comores (ex-Telma Comores) | yas.km; axian-telecom.com (€25M IFC loan, 2025-06-20, for 5G/FTTH/FTTO and service expansion); ANRTIC 5G decision; press on 5G launch | Moroni HQ/core candidate (Grande Comore); network sites island-wide | **A** for operator/financing facts; core/DC facility **lead** |
| Comores Câbles landing stations (Itsandra, Moroni, Chindini, Mutsamudu, Fomboni) | comorescables.km; consortium pages (flylion3.lion-submarinesystem.com); 2Africa official; Al-Watwan; GeoCables/TeleGeography; Cour Suprême audit ROD 2023-01-05 | Itsandra & Moroni & Chindini = Grande Comore; Mutsamudu = Anjouan; Fomboni = Moheli | **A** for cable facts; **not a DC** without server/colo evidence |
| PADEC incubator | AfDB PADEC docs; ANADEN | Grande Comore (verify) | **A** for project financing; facility status to verify |
| Government/ministry hosting | egouv.km; ANADEN; Journal Officiel; PADEC procurement; Cour Suprême audits; IsDB public-administration modernization GPN | Moroni (Grande Comore) primarily | Internal facility/demand lead; count only with tender, facility, hosting, or planning proof |
| Financial-sector server rooms (BCC, BIC, Exim, Banque Postale des Comores, Mvola fintech) | Bank official pages; BCC; press; PADEC | Moroni (Grande Comore) and Anjouan (Mutsamudu) branches | Demand signal only; **C** until primary facility evidence |
| Satellite/edge (Starlink etc.) | Starlink availability map/support; ANRTIC decisions | Service-level, not facility-level | **B/C**; not a DC; gateway evidence to verify separately |

Operator query templates:
```text
"Comores Telecom" ("data center" OR "centre de données" OR "salle de serveurs" OR NOC)
"Comores Telecom" ("Place Volo-volo" OR "BP 7000") (serveurs OR hébergement)
("Yas Comores" OR "Telma Comores") ("data center" OR "centre de données" OR "core network" OR backbone)
AXIAN Comores ("data center" OR 5G OR investissement OR IFC)
ANADEN ("centre de données" OR "data center" OR PADEC)
"Comores Câbles" ("station d'atterrissement" OR "data center" OR cloud)
PADEC Comores (datacenter OR "centre de données" OR incubateur OR "protection des données")
```

---

## 2. Industry and press sources

| Source | URL | Use | Grade rule |
|---|---|---|---|
| ANADEN | https://anaden.org/ (Réalisations) | National DC launch, PADEC, Comoros Numérique 2028 | A for official statements; B for claimed tier/capacity details without separate primary proof |
| Comores Câbles | https://comorescables.km/ | Cables, backbone, station d'atterrissement, Cloud/AI ambitions | A for company facts; facility/DC claims need facility-level proof |
| Comores Telecom | https://www.comorestelecom.km/ | Operator identity, HQ address (Place Volo-volo, BP 7000 Moroni), services | A for address/operator facts when page is captured; B/C for inferred DC unless facility proof appears; note TLS-chain crawler caveat. |
| Yas Comores | https://www.yas.km/ | Operator identity and offers (ex-Telma Comores) | A for company facts |
| AXIAN Telecom | https://www.axian-telecom.com/ | Yas Comores group context and €25M IFC loan announcement for 5G/FTTH/FTTO expansion | A for group/operator financing and rollout statements |
| ANRTIC | https://anrtic.km/ | Licences, 5G frequency decisions (2025-05-27), QoS observatories | A for regulatory decisions |
| AfDB PADEC | https://mapafrica.afdb.org/fr/projects/46002-P-KM-G00-001 ; https://www.afdb.org/en/documents/comoros-comorian-economic-digitalization-support-project-padec-project-appraisal-report ; appraisal report and PPM xlsx on afdb.org | Primary/secondary DC + incubator components | A for project facts |
| IsDB public-administration modernization | https://www.isdb.org/project-procurement/fr/appels-doffres/2026/gpn/projet-de-modernisation-de-ladministration-publique-comorienne-par-le-bais | E-government/interoperability/payment/e-services and AI-lab procurement context | A for adjacent digital-platform demand; not a DC unless later notices name hosting/facility works |
| World Bank | https://www.banquemondiale.org/ | RCIP4/backbone history, Comoros digital portfolio, Yas loan reporting | A for project facts; B for press-reported loans |
| Journal Officiel de l'Union des Comores | https://journalofficiel-km.com/ | Laws/decrees (ANADEN, Comores Câbles, ANRTIC, SONELEC; data-protection law) | A |
| Cour Suprême — Section des Comptes | https://www.coursupremecomores.km/ | ROD audits of Comores Câbles (2023), SONELEC | A for audited assets/operations |
| egouv.km / Comoros Open Data | https://egouv.km/ ; https://opendata-comores.org/ | Government portal, open data on organisations | A/B |
| Al-Watwan | https://alwatwan.net/ | 2Africa Itsandra landing (2023-01-12), FLY-LION3, company news | B; cite any linked primary document separately for A-grade evidence |
| La Gazette des Comores | https://lagazettedescomores.com/ | ANRTIC audits, Comores Câbles HQ, SONELEC DG changes | B |
| Habari za Comores | https://www.habarizacomores.com/ | Telecom pricing/regulatory news | B |
| Comores Infos | https://www.comoresinfos.net/ | Backbone/RCIP4 history (2016) | B |
| Masiwa Komor / km-news.net / Al-Fajr | Local press | State-enterprise reform, operator news, ACTIC statements | B |
| Focus-OI | https://www.focus-oi.com/ | DC inauguration reporting and Comoros telecom/digital-economy context | B |
| Agence Ecofin | https://www.agenceecofin.com/ | DC inauguration (2025-05-14), PADEC, digital economy | B; cite the official source separately for any A-grade claim |
| Data Centres Africa | https://datacentresafrica.com/ | National DC launch story (2025-05-15) | B |
| Techpoint Africa | https://techpoint.africa/ | AfDB funding (Oct 2024) | B |
| Submarine Networks | https://www.submarinenetworks.com/ | EASSy/FLY-LION3/2Africa system pages | B for reporting; A only if citing an operator/system primary page it hosts or quotes |
| GeoCables / TeleGeography / submarinecablemap | https://geocables.com/locations/km ; https://www.submarinecablemap.com/ | Landing points, cables, RFS years | B+ for mapping facts; verify with primary cable pages |
| DCD / Developing Telecoms / WeAreTech Africa / Telecom Review Africa | Industry sites | Regional telecom/DC context | B |
| DataCenterMap / Baxtel / Cloudscene / PeeringDB / datacenters.com | Directories | Seed discovery only; Comoros listings currently absent | C until matched to primary |
| Social media | Facebook/LinkedIn (Comores Telecom, Comores Câbles, ANADEN, ANRTIC, ACTIC) | Change feed for announcements | C unless the official account links to a primary document |

Press/trade query templates:
```text
site:alwatwan.net Comores ("centre de données" OR "data center" OR câble)
site:lagazettedescomores.com Comores ("centre de données" OR "data center" OR numérique)
site:habarizacomores.com Comores (télécommunications OR "centre de données")
site:comoresinfos.net Comores (backbone OR câble OR "data center")
site:agenceecofin.com Comores ("centre de données" OR numérique)
site:datacentresafrica.com Comoros ("data centre" OR "data center")
site:techpoint.africa Comoros ("data centre" OR AfDB)
site:submarinenetworks.com (Comoros OR Comores) cable
site:focus-oi.com Comores ("centre de données" OR Yas OR numérique)
```

---

## 3. Directory-to-primary workflow

1. Seed only from directories/marketplaces: DataCenterMap, Baxtel, Cloudscene, datacenters.com, PeeringDB, CDN PoP lists, hosting-provider pages, and Starlink/OneWeb availability pages. Expected result for Comoros: no or near-zero DC entries — record that as the finding.
2. Search exact facility/operator/address against primary domains: `anaden.org`, `comorescables.km`, `comorestelecom.km`, `yas.km`, `axian-telecom.com`, `anrtic.km`, `journalofficiel-km.com`, `afdb.org`, `banquemondiale.org`.
3. Verify division through the island/commune/address: Grande Comore (Moroni, Itsandra, Chindini), Anjouan (Mutsamudu), Moheli (Fomboni). If only a broad locality is available, use the manifest division with an uncertainty note.
4. Verify status with inauguration/certification/operational-service evidence. Use `announced`, `under development`, or `lead` if only a planned project or press statement exists.
5. Keep directory-only entries as Grade C; do not merge them into confirmed facilities unless name/address/operator line up.

Negative-control queries:
```text
"Comores" OR "Comoros" colocation OR "co-location" OR hosting OR VPS
"Comoros" "cloud hosting" OR "dedicated server"
"Comoros" "TIA-942" OR "Uptime Institute" OR "Tier IV" OR "Tier 3"
"Comoros" "AWS" OR Azure OR "Google Cloud" OR OCI region OR "data centre"
site:baxtel.com Comoros
site:datacentermap.com Comoros
"Comoros" Starlink gateway OR "ground station"
"KM" "data center" -Comoros -Comores
```

---

## 4. Division recipes for all 3 divisions

Use the exact manifest spellings in records (Anjouan, Grande Comore, Moheli). Add local variants only in queries: Anjouan = Ndzuwani/Nzwani; Grande Comore = Ngazidja; Moheli = Mwali.

Universal division query:
```text
("{division}" OR "{local variant}") Comores ("centre de données" OR "data center" OR datacenter OR "salle de serveurs" OR colocation)
("{division}" OR "{local variant}") Comores ("station d'atterrissement" OR "câble sous-marin" OR backbone OR "network operations")
("{division}" OR "{local variant}") Comores ("groupe électrogène" OR UPS OR climatisation OR serveur OR hébergement)
site:alwatwan.net "{division}" ("centre de données" OR télécom OR câble)
site:lagazettedescomores.com "{division}" (numérique OR télécom)
site:anrtic.km "{division}" (licence OR fréquence)
site:comorestelecom.km ("{division}" OR Moroni OR Mutsamudu OR Fomboni)
```

High-yield division variants:
```text
("Grande Comore" OR Ngazidja OR Moroni OR Itsandra OR Chindini) ("centre de données" OR "data center" OR "station d'atterrissement" OR "Comores Telecom" OR "Comores Câbles" OR ANADEN)
(Anjouan OR Ndzuwani OR Nzwani OR Mutsamudu) (câble OR station OR télécom OR serveur OR "centre de données")
(Moheli OR Mohéli OR Mwali OR Fomboni) (câble OR station OR télécom OR serveur OR "centre de données")
```

Division checklist and expected handling:

| Division | Expected yield | Notes |
|---|---|---|
| Grande Comore | High (1 confirmed DC + leads) | National DC (ANADEN/Comores Câbles); Comores Telecom HQ Place Volo-volo Moroni; Yas Comores HQ/core; Itsandra station (FLY-LION3 + 2Africa); Moroni EASSy landing; Chindini landing; ministry/bank server rooms; PADEC incubator. Verify commune boundaries (Moroni-Bambao vs Itsandra) before fixing sub-island location. |
| Anjouan | Low/medium | Mutsamudu landing (Avassa/domestic cable) and telecom PoPs/exchanges (Comores Telecom, Yas) only; EDA/SONELEC power context; banks. No public DC found in this pass — do not invent one. |
| Moheli | Low | Fomboni landing (domestic cable) and telecom PoPs only. No public DC found in this pass — mark explicitly. |

---

## 5. Seed records to validate during enumeration

| Seed | Status | Capacity | Developer/operator | Grade | Sources to use |
|---|---|---|---|---|---|
| Data Center de l'Administration Publique (national DC) | Operational / inaugurated 2025-05-19 per ANADEN | null (only “44.4 Tb” hosting statement, unit ambiguous) | ANADEN + Comores Câbles (state); AfDB PADEC financing context | A for existence/date/co-management from ANADEN; B for Tier-3/44.4 Tb unless official source captured | ANADEN, Comores Câbles, PADEC docs, Agence Ecofin, Data Centres Africa, Focus-OI; certification registries (negative) |
| Secondary DC upgraded under PADEC | Lead / under development | null | Unidentified (candidate: Comores Telecom or government IT facility) | B/C | AfDB PPM 2025-07-02; Comores Telecom; ministry; Journal Officiel |
| Comores Telecom HQ server rooms/NOC | Lead | null | Comores Telecom (Huri) | B/C | comorestelecom.km, ANRTIC, Al-Watwan/Gazette, SONELEC context |
| Yas Comores (ex-Telma Comores) core/network sites | Lead | null | Yas Comores / AXIAN Telecom | B/C | yas.km, axian-telecom.com, ANRTIC, Focus-OI, World Bank reporting |
| Itsandra landing station | Connectivity site | null | Comores Câbles (FLY-LION3 + 2Africa) | A for cable | comorescables.km, consortium pages, Al-Watwan |
| Moroni EASSy landing | Connectivity site | null | EASSy consortium / Comores Câbles | A for cable | Submarine Networks, GeoCables/TeleGeography |
| Chindini landing | Connectivity site | null | Comores Câbles / Avassa & FLY-LION3 context | A for cable | GeoCables/TeleGeography, cable records |
| Mutsamudu landing | Connectivity site | null | Comores Câbles / Avassa & domestic cable | A for cable | GeoCables/TeleGeography, cable records |
| Fomboni landing | Connectivity site | null | Comores Câbles / domestic cable | A for cable | GeoCables/TeleGeography, cable records |
| PADEC incubator | Under development | null | ANADEN / AfDB | A for financing | PADEC docs, ANADEN |
| Government/ministry server rooms | Internal lead | null | State | C | egouv.km, Journal Officiel, PADEC procurement, Cour Suprême audits |
| Bank/fintech server rooms (BCC, BIC, Exim, Banque Postale des Comores, Mvola) | Demand lead | null | Private/state banks | C | Bank official pages, BCC, press |

---

## 6. Capacity and reliability extraction

Record these fields when available: certification body, tier/rating level (flag claimed vs certified), certificate ID, awarded/expiry dates, capex, launch/inauguration date, address, division, operator, customer type, public services offered, and connectivity/cable adjacency.

Do not derive capacity from:
- The national DC “Tier 3” claim or its “44.4 Tb” statement (unit ambiguous).
- PADEC/Comoros Numérique 2028 budget figures (€9.51M, 21 billion KMF, US$47.8M).
- FLY-LION3/EASSy/2Africa/Avassa cable bandwidth or cable capex.
- Yas Comores €25M network investment.
- Claims such as “world-class”, “souveraineté numérique”, or “AI-ready” without facility-level evidence.

Capacity query templates:
```text
"centre de données" Comores (rack OR racks OR m² OR MW OR MVA OR kVA)
("Data Center de l'Administration Publique" OR "centre de données de l'administration publique") (Tier OR capacité)
PADEC Comores (datacenter OR "centre de données") (capacité OR racks OR MW)
"Comores Telecom" "centre de données" (rack OR MW OR kVA)
"Comores Câbles" ("data center" OR "centre de données") (capacité OR MW)
```

Reliability grading rules:
- **A**: operator/government/certification/cable-consortium/AfDB-World Bank source proves facility, address, status, or certification.
- **B**: press/trade source supports dates, capex, launch, public remarks, or cable events but does not independently prove a certified facility/address.
- **C**: directory/social/hosting page only, or a service page that does not show physical facility ownership/location.

Pitfalls: keep all 3 divisions in the sweep even where prior batches found no projects; do not let “Tier 3” or “national first” marketing override the absence of certification registries; do not count cable landings as datacentres; keep Mayotte facilities out of scope; always include “Comores”/“Comoros” in searches to avoid ccTLD/SEO false positives; record the national DC address as unverified until ANADEN/Comores Câbles or the Journal Officiel publish one.
