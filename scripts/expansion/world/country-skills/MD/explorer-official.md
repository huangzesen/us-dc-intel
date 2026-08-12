# MD Explorer Official - Moldova Datacenter Enumeration via Official, Regulatory, Permit, Energy, Cloud, and Public-Sector Sources

Date: 2026-08-12. Scope: Republic of Moldova (MD), including districts, municipalities, Gagauzia, and the left-bank territorial unit. Focus angle: official/regulatory-first methodology for datacenter facility and project enumeration. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/operator source, **C** = weak aggregate or unverified lead.

---

## 0. Moldova-specific frame

- Moldova has no public national datacenter registry. Build the census from **local construction/urbanism permits**, Chisinau municipal records, **ARCOM/ANRCETI provider registers**, **STISC/MCloud government cloud records**, energy/grid connection evidence, public procurement, and operator-owned facility pages.
- The market is highly concentrated in **Chisinau municipality**. Existing public listings and operator pages mostly point to Chisinau facilities; other districts should be treated as low-yield except for government site-search leads in **Balti, Ungheni, and Falesti**, border/interconnection corridors, industrial parks, and the Transnistria/left-bank hosting market.
- Moldova's construction permitting authority is normally the local public administration. National statistics give counts, but not a searchable facility register. For exact projects, use local pages and document repositories for `certificat de urbanism`, `autorizatie de construire`, council decisions, and public consultations.
- Romanian is the best search language. Also search Russian for Transnistria and older telecom/hosting material, plus English for operator and directory pages.
- Cloud-region pages are negative evidence: as of this research pass, AWS, Azure, Google Cloud, and OCI official public-region lists do not show a Moldova/Chisinau cloud region. Use them to avoid misclassifying local VPS/colo as hyperscale cloud regions.

Lifecycle vocabulary:

`concept / strategie / studiu de fezabilitate` < `identificarea terenului` < `certificat de urbanism pentru proiectare` < `acord de mediu / decizie evaluare prealabila` < `autorizatie de construire` < `lucrari de constructie` < `dare in exploatare / punere in functiune` < `servicii de colocare / hosting operational`

For a counted facility, prefer operator-owned facility pages, PeeringDB/facility records, construction permits, environmental decisions, grid-connection records, or STISC/government records. Treat pure "cloud server in Moldova" offers, VPS IP-geolocation pages, and SEO directories as leads only.

---

## 1. Official Romanian, Russian, and English query vocabulary

### 1.1 Romanian core terms

```text
centru de date
centre de date
centru de prelucrare a datelor
centru de procesare a datelor
centrul de date guvernamental
MCloud
cloud guvernamental
servicii de colocare
colocare servere
gazduire servere
hosting dedicat
server farm
infrastructura IT
infrastructura critica
camera servere
nod telecomunicatii
statie de transformare
post de transformare
generator diesel
surse neintreruptibile UPS
racordare la reteaua electrica
aviz de racordare
certificat de urbanism
certificat de urbanism pentru proiectare
autorizatie de construire
autorizatii de construire
acord de mediu
evaluarea impactului asupra mediului
evaluare prealabila
dezbatere publica
achizitii publice
studiu de fezabilitate
teren centru de date
Tier III
AI-Ready
```

### 1.2 Russian and English terms

```text
центр обработки данных Молдова
дата центр Кишинев
ЦОД Кишинев
колокация серверов Молдова
хостинг серверов Тирасполь
серверная Кишинев
разрешение на строительство дата центр

Moldova data center
Chisinau data center
Moldova colocation
Chisinau colocation
Moldova government cloud
MCloud Moldova data center
STISC national data center Moldova
Moldova grid connection data center
Moldova building permit data center
```

### 1.3 Official query templates

Substitute `{division}`, `{city}`, `{municipality}`, `{operator}`, `{legal_entity}`, `{street}`, `{site_domain}`.

```text
site:chisinau.md "centru de date"
site:chisinau.md "autorizatie de construire" "centru de date"
site:chisinau.md "certificat de urbanism" "centru de date"
site:dgaurf.md "centru de date" OR "autorizatie de construire"
site:{site_domain} "centru de date" "autorizatie de construire"
site:{site_domain} "certificat de urbanism pentru proiectare" "centru de date"
site:{site_domain} "{operator}" "autorizatie de construire"
site:{site_domain} "{street}" "certificat de urbanism"
site:am.gov.md "centru de date"
site:am.gov.md "generator" "centru de date"
site:am.gov.md "evaluare prealabila" "centru de date"
site:moldelectrica.md "centru de date" OR "aviz de racordare"
site:anre.md "centru de date" OR "sistem de distributie inchis"
site:stisc.gov.md "Centrul de Date" "Tier III"
site:stisc.gov.md "studiu de fezabilitate" "centru de date"
site:mtender.gov.md "centru de date" OR "MCloud" OR "colocare"
site:tender.gov.md "centru de date" OR "servere" "STISC"
```

---

## 2. Official / regulatory source backbone

### 2.1 Communications regulator: ANRCETI / ARCOM

Primary sources:

- ARCOM/ANRCETI main site: https://en.anrceti.md/ and Romanian site navigation. **Grade A** for regulator context.
- Public Register of Electronic Communications Network and Service Providers: https://en.anrceti.md/lista_furnizori_servicii_retele_ce . **Grade A** for authorized telecom/network provider identity.
- General authorization guidance: https://en.anrceti.md/gfcap1 and https://en.anrceti.md/node/15 . **Grade A** for understanding the notification/general authorization regime.
- ARCOM history page: https://en.anrceti.md/history . **Grade A** for the 2026 institutional rename from ANRCETI to ARCOM.

Use ARCOM to validate legal entities behind network-heavy datacenter operators: Moldtelecom, Orange Moldova, StarNet, Trabia Network, Inovare-Prim/IP HOST, Infotech-Grup/AvenaCloud, MivoCloud, Cogent Moldova, and government/STISC network entities. ARCOM registration is **not** proof of a datacenter, but it is strong identity evidence for telecom/provider pivots.

Useful ARCOM pivots:

```text
site:anrceti.md "{operator}"
site:arcom.md "{operator}"
site:en.anrceti.md "{operator}" "Public Register"
"{legal_entity}" "ANRCETI" "registrul public"
"{legal_entity}" "ARCOM" "retele si servicii de comunicatii electronice"
```

### 2.2 Construction and urbanism permits

Primary sources:

- National construction-permit e-filing portal: https://construct-permits.gov.md/ . **Grade A process source**; public search may require authentication and may not expose a complete public project list.
- e-Government announcement on online construction permits: https://egov.md/en/node/40791 . **Grade A process source**. It says four documents became requestable online in March 2025: informational urban planning certificate, urban planning certificate for design, building permit, and demolition permit, initially through Chisinau City Hall.
- EVO service page for `Certificat de urbanism pentru proiectare`: https://evo.gov.md/acasa/servicii/alte/Certificat%20de%20urbanism%20pentru%20proiectare . **Grade A process source**.
- Chisinau municipality: https://www.chisinau.md/ . **Grade A** for municipal records, consultations, urbanism documents, and council decisions.
- Chisinau Architecture, Urbanism and Land Relations directorate (DGAURF): https://www.dgaurf.md/ . **Grade A** for Chisinau urbanism/land-use context.
- Moldova.digital processed Chisinau construction-permit dataset: https://moldova.digital/en/articles/construction-permits-issued-in-chisinau-municipality-updated-2022-01-10/ . **Grade B** as a processed copy of official Chisinau records; use only as a search/discovery aid and re-check source documents.
- National Bureau of Statistics construction-permit metadata: https://old.statistica.md/public/files/Metadate/en/Autorizatii_cladiri_en.pdf . **Grade A** for definitions and national aggregate series, not facility enumeration.

Fields to extract from permit/urbanism records:

- issuer/local authority;
- document type: `certificat de urbanism`, `autorizatie de construire`, `autorizatie de desfiintare`;
- beneficiary/investor legal name;
- address, cadastral number, land category, zoning designation;
- object description: datacenter, telecom node, server room, technical building, transformer station, backup generators, cooling/chiller plant;
- date, validity, decision number, and any attached technical conditions.

Datacenters may appear as `cladire tehnica`, `obiectiv de telecomunicatii`, `spatii pentru echipamente IT`, `statie de transformare`, or `constructii industriale/de depozitare` rather than "centru de date". Cross-check ambiguous technical buildings against operator addresses, PeeringDB, and ARCOM entities.

### 2.3 Environment / EIA

Primary sources:

- Environmental Agency main site: https://www.am.gov.md/ . **Grade A**.
- EIA process page: https://am.gov.md/ro/evaluarea-impactului-asupra-mediului . **Grade A**. The agency describes EIA as an early planning/design procedure before requesting the urbanism certificate for design.
- Environmental Agency announcements: https://am.gov.md/ro/anunturi-0 . **Grade A** for public EIA notices and attached applications/decisions.
- Law No. 86/2014 on environmental impact assessment: https://www.legis.md/cautare/getResults?doc_id=21797&lang=ro . **Grade A legal source**.

Datacenter triggers to search in EIA/public notices:

```text
"centru de date" "acord de mediu"
"centru de date" "evaluare prealabila"
"generator diesel" "acord de mediu" Chisinau
"statie de transformare" "centru de date"
"UPS" "deseuri" "centru de date"
"sistem de racire" "centru de date"
"rezervoare combustibil" "centru de date"
```

What to extract:

- backup-generator count/capacity and fuel storage;
- transformer/substation capacity and grid connection point;
- cooling system, noise, water use, wastewater;
- battery/UPS and hazardous-waste handling;
- planned area, phasing, and exact land parcel;
- whether the notice is screening/preliminary assessment, EIA program, full EIA report, or environmental agreement.

### 2.4 Energy, grid, and utilities

Primary sources:

- Ministry of Energy: https://energie.gov.md/ . **Grade A** for policy and grid-connection reform context.
- Moldelectrica connection to transmission network: https://moldelectrica.md/en/network/access and Romanian https://moldelectrica.md/ro/network/access . **Grade A** for high-voltage connection process. Moldelectrica states technical permits/connection notices are required for consumers requesting connection to the transmission grid.
- Moldelectrica services/document list: https://moldelectrica.md/ro/activity/services_docs_list . **Grade A** for connection-document templates.
- Moldelectrica renewable-energy connection page: https://moldelectrica.md/ro/network/renewable_energy_sources . **Grade A** for available connection-capacity context and transmission-connection pressure. It is mostly generation-focused, but high-load datacenters compete for the same grid geography.
- ANRE electricity sector page: https://anre.md/index.php/energia-electrica-3-167 . **Grade A** for energy-sector regulatory context.
- ANRE annual/activity reports, example 2024 report: https://anre.md/storage/upload/administration/reports/1473/Raportul%20privind%20Activitatea%20ANRE%20%C3%AEn%20anul%202024...pdf . **Grade A** for licensed operators and investment plans.
- Distribution operators: Premier Energy Distribution (central/south and Chisinau) and RED Nord (north). Premier Energy Group operations page states the Moldova distribution network covers 16 districts and Chisinau: https://premierenergygroup.eu/our-activity/our-operations/ . **Grade B/A depending on entity page**; confirm with ANRE for official licensing.

Use energy evidence to separate small hosting rooms from material datacenter projects. A serious new facility should leave some combination of `aviz de racordare`, transformer/substation works, generator/fuel environmental material, or utility investment references.

Energy queries:

```text
site:moldelectrica.md "{operator}" "aviz de racordare"
site:moldelectrica.md "instalatie de utilizare" "centru de date"
site:anre.md "{operator}" "energie electrica"
site:anre.md "sistem de distributie inchis" "centru de date"
"{operator}" "aviz de racordare" "Chisinau"
"{operator}" "statie de transformare" "Chisinau"
"{city}" "centru de date" "post de transformare"
"{city}" "centru de date" "generator diesel"
```

### 2.5 Public procurement and government cloud

Primary sources:

- MTender public portal: https://mtender.gov.md/en . **Grade A** for Moldova public procurement discovery.
- Public Procurement Agency: https://tender.gov.md/en . **Grade A** for procurement-policy/source routing.
- STISC main site: https://stisc.gov.md/ro . **Grade A** for government IT/cybersecurity operator records.
- STISC procurement page: https://stisc.gov.md/ro/achizitii . **Grade A** for STISC procurement and monitoring reports.
- MCloud platform page: https://www.egov.md/en/content/mcloud-platform . **Grade A** for national government cloud context. It describes MCloud as consolidating government datacenters under a common technology platform.
- STISC 2025 activity report: https://stisc.gov.md/sites/default/files/documents/Raport%20de%20activitate%20STISC%202025.pdf . **Grade A** for planned national datacenter/site-search evidence; it mentions a `Centrul de Date TIER III, AI-Ready`, feasibility-study procurement, and land-identification trips to Ungheni district, Falesti district, and Balti municipality.
- Government release on Latvia support: https://gov.md/en/press-releases/pm-meets-ambassador-latvia-moldova . **Grade A** for future national datacenter methodological-support signal.

Procurement queries:

```text
site:mtender.gov.md "centru de date"
site:mtender.gov.md "MCloud"
site:mtender.gov.md "colocare"
site:mtender.gov.md "servere" "STISC"
site:stisc.gov.md "Centrul de Date TIER III"
site:stisc.gov.md "studiu de fezabilitate" "Centrul de Date"
site:stisc.gov.md "Ungheni" "Fălești" "Bălți" "Centrul de Date"
```

For public-sector projects, record whether the evidence is an operational government platform, a procurement for hardware/services, a feasibility study, or actual construction. Do not turn `MCloud` service modernization into a new physical datacenter unless a site, build, or facility record is named.

### 2.6 Cadastre, addresses, and geospatial checks

Primary sources:

- Public Services Agency / cadastre services: https://www.asp.gov.md/ro/servicii/bunuri-imobile/54 and cadastral-plan service https://www.asp.gov.md/ro/servicii/bunuri-imobile/54/545 . **Grade A** for cadastral-service process.
- ASP FAQ on immovable-property register information: https://www.asp.gov.md/ro/intrebari-frecvente/bunuri-imobile/0021 . **Grade A** for access process.

Use ASP/cadastre after a candidate address is known. Capture cadastral number, owner/tenant if legally accessible, and relation to industrial parks or high-voltage routes. Do not rely on geocoded IP or map pins alone.

---

## 3. Official cloud-region checks

Use official cloud-location pages as a negative/normalization check:

| Provider | Official source | Moldova signal | Enumeration use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html and AWS Wavelength https://aws.amazon.com/wavelength/locations/ | No Moldova Region/Local Zone/Wavelength found in official lists during this pass. | Do not classify Moldovan hosting/VPS as AWS region infrastructure without an official announcement. |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Moldova public Azure region found during this pass. Nearest official public regions are outside Moldova. | Use only as absence check; local Microsoft partner/cloud services are not Azure region facilities. |
| Google Cloud | https://cloud.google.com/about/locations and Google datacenter locations https://datacenters.google/locations | No Moldova Google Cloud region/datacenter location found during this pass. | Avoid counting Google office/partner/cloud adoption as physical DC. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | No Moldova OCI public cloud region found during this pass. | Treat OCI partner/reseller claims as service presence, not datacenter presence. |

CDN/edge nodes can exist without hyperscale datacenters. If Cloudflare, Bunny, Akamai, Google cache, or similar appears in PeeringDB/IXP/member data, record it as edge/PoP evidence unless it is tied to a physical colocation facility.

---

## 4. Division-level official enumeration strategy

### 4.1 Chisinau municipality: highest priority

Chisinau should receive the deepest pass because known facilities and most operator addresses are concentrated there.

Official workflow:

1. Seed known operator addresses from Moldtelecom Data City, MoldData Cloud/Host.md, Trabia, AlexHost, IP HOST/Inovare-Prim, AvenaCloud/Infotech-Grup, Cogent, StarNet, Orange Moldova, and Mezon.
2. Query Chisinau/DGAURF for permits and certificates by operator, street, `centru de date`, `cladire tehnica`, `statie de transformare`, and `generator`.
3. Query Environmental Agency for backup power/cooling/environmental notices by operator and address.
4. Query ARCOM for telecom-provider legal entity identity.
5. Query PeeringDB/IXP records to confirm active interconnection at named sites.
6. Query Moldelectrica/Premier Energy/ANRE for any large-load or substation works.

Templates:

```text
site:chisinau.md "centru de date"
site:chisinau.md "Alba Iulia 77" OR "Moldtelecom"
site:chisinau.md "Armeneasca 37/1" OR "MoldData"
site:chisinau.md "Vlaicu Pircalab" "Trabia"
site:chisinau.md "Uzinelor" "IP HOST" OR "Inovare-Prim"
site:chisinau.md "Muncesti 364" OR "AvenaCloud"
site:chisinau.md "Constantin Brancusi" "AlexHost"
site:dgaurf.md "centru de date" OR "servere"
site:am.gov.md "Chisinau" "centru de date"
site:am.gov.md "Chisinau" "generator diesel" "server"
```

### 4.2 Government/national datacenter search areas: Balti, Ungheni, Falesti, Stauceni/Chisinau

STISC's 2025 report makes these the main official planned-project watchlist. Treat them as **planned/site-search** until a final land selection, permit, or construction record appears.

Templates:

```text
site:stisc.gov.md "Centrul de Date TIER III" "Bălți"
site:stisc.gov.md "Centrul de Date TIER III" "Ungheni"
site:stisc.gov.md "Centrul de Date TIER III" "Fălești"
"Centrul de Date TIER III" "Balti" "STISC"
"Centrul de Date TIER III" "Ungheni" "STISC"
"Centrul de Date TIER III" "Falesti" "STISC"
"centru de date" "Moldova HiTech Park" "Stauceni"
site:gov.md "national data center" Moldova STISC
site:mtender.gov.md "studiu de fezabilitate" "centru de date"
```

### 4.3 North, center, and south districts

For districts without operator leads, use a fast negative-screening sequence:

1. Query local authority site and `site:{district}.md` variants for `centru de date`, `servere`, `camera servere`, `statie de transformare`, and `autorizatie de construire`.
2. Query MTender for district + `servere`, `centru de date`, `camera servere`, `cloud`, `colocare`.
3. Query ANRE/Moldelectrica/Premier/RED Nord for major substation or connection works if a datacenter-like lead exists.
4. Search local press in Romanian/Russian for `data center`, `centru de date`, and operator names.

District templates:

```text
"{division}" "centru de date"
"{division}" "data center" Moldova
"{division}" "servere" "achizitii"
"{division}" "autorizatie de construire" "centru de date"
"{division}" "statie de transformare" "centru de date"
site:{division-domain} "centru de date"
site:{division-domain} "autorizatie de construire" "servere"
site:mtender.gov.md "{division}" "servere"
site:mtender.gov.md "{division}" "centru de date"
```

Higher-yield non-Chisinau divisions: **Balti**, **Ungheni**, **Falesti**, **Ialoveni/Straseni** (Chisinau spillover and industrial/logistics belt), **Cahul** (regional development/free economic zone), **Gagauzia** (industrial park/free economic zone), and **Stinga Nistrului / Transnistria** for Russian-language hosting/mining/colo evidence.

### 4.4 Transnistria / left-bank territorial unit and Bender

Official Moldova registers may not fully cover or enforce left-bank records. Use a separate confidence label and avoid over-grading.

Templates:

```text
"Тирасполь" "дата центр"
"Тирасполь" "ЦОД"
"Приднестровье" "дата центр"
"Bender" "data center" Moldova
"Tiraspol" "colocation" Moldova
"Imperial Hosting" "Tiraspol" "data center"
```

Treat operator-owned Russian/English hosting pages as **B/C** unless a physical facility address, power, permits, or independent interconnection record is found.

---

## 5. Evidence grading and counting cautions

- **A**: operator-owned facility page with address/services; official local permit/urbanism record; Environmental Agency EIA/decision; ARCOM provider register for legal identity; STISC/government record naming government datacenter work; Moldelectrica/ANRE connection/regulatory record.
- **B**: PeeringDB facility/IX data, established trade press, processed official datasets, credible operator marketplace page, DataCenterMap page with operator/address details.
- **C**: VPS directories, generic "cloud in Moldova" SEO pages, IP-geolocation claims, forums, weak facility marketplaces, social posts without source documents.
- Do not count `MCloud`, "cloud server in Chisinau", or CDN/cache node listings as physical datacenters unless tied to a named facility.
- Do not count national datacenter concepts as projects in Balti/Ungheni/Falesti unless the final site is public. Store them as candidate/site-search evidence.
- For Chisinau facilities, capture exact address and legal entity because multiple brands may refer to the same building or provider ecosystem.
