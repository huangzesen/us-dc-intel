# SI Explorer Official - Slovenia Datacenter Enumeration via Permits, Energy, Regulator, Cloud, and Public Procurement

Date: 2026-08-12. Scope: Slovenia (SI), 212 municipalities, grouped for field work by 12 SURS statistical regions. Focus angle: official/regulatory/cloud-first enumeration for data-center facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak aggregate/unverified lead.

---

## 0. Slovenia-specific frame

- Slovenia has no public national "data center registry". Build the census by joining **PIS/eGraditev construction acts**, municipal spatial-planning files, environmental-assessment records, **ELES/SODO energy-grid evidence**, public procurement, AKOS telecom infrastructure context, official cloud-region pages, and operator confirmations.
- The effective permit geography is usually the **municipality (obcina)** and **administrative unit (upravna enota / UE)**, not the statistical region. Use statistical regions to organize the search, but resolve each candidate to a municipality, cadastral municipality (`katastrska obcina`), parcel, address, and administrative act.
- Slovenia's strongest construction source is the public **PIS Zbirka podatkov o graditvi objektov**: https://pis.eprostor.gov.si/pis-ua-jv/seznam.html?mobile=false . The eConstruction/eGraditev introduction page states that construction administrative acts, including building permits, use permits, inspection decisions and start-of-construction notifications, are registered and that basic data are publicly available: https://pis.eprostor.gov.si/en/pis/predstavitev-sistema/uvedba-egraditev.html . **Grade A** for act metadata.
- The PIS construction database uses Slovenian procedure labels. Important filters/fields: `GD` = gradbeno dovoljenje/building permit, `UD` = uporabno dovoljenje/use permit, `PG` = prijava zacetka gradnje/start of construction or demolition/start notification, `ID akta`, `Upravni organ`, `Naziv`, `Postopek`, issue/finality dates, cadastral municipality, parcels, utility connections, CC-SI object classification.
- Slovenian filings may not say "data center". Search both English and Slovenian words plus support-infrastructure terms: `podatkovni center`, `podatkovnega centra`, `racunalniski center`, `strezniski center`, `strezniska soba`, `kolokacija`, `oblak`, `superracunalnik`, `tovarna umetne inteligence`, `UPS`, `agregat`, `dizelski agregat`, `hlajenje`, `odvecna toplota`, `transformatorska postaja`, `RTP`, `prikljucitev`, `elektroenergetski prikljucek`.
- Official examples proving the source mix: GOV.SI confirms ARNES data-center construction in Maribor and a waste-heat cooperation letter around the site; e-JN has an official tender record titled `Podatkovni center Arnes - lokaciji Maribor in Ljubljana`; GOV.SI confirms Posta Slovenije handed a new Ljubljana postal-logistics-centre data center to the Ministry of Digital Transformation on 2025-09-30.
- Major geography: **Osrednjeslovenska/Ljubljana** for state, telecom, IXP and commercial colocation; **Podravska/Maribor** for ARNES, Posta/Posita and government/research capacity; **Goriska/Nova Gorica**, **Obalno-kraska/Koper**, **Gorenjska/Kranj**, and selected telecom/industrial sites are secondary checks. Most small municipalities will return no project evidence.

Lifecycle vocabulary:

`OPN/OPPN/prostorski akt` < `predodlocba/projektni pogoji/mnenja` < `GD gradbeno dovoljenje` < `PG prijava zacetka gradnje` < `UD uporabno dovoljenje` < `predaja v uporabo/operativno/otvoritev`

Only count a facility as strong evidence with one of: `GD`, `PG`, `UD`, official government/operator launch, official procurement award/build record, or operator-owned facility page. Treat spatial plans, grid-capacity maps, AKOS telecom-map signals, and trade articles as leads until cross-checked.

---

## 1. Core Slovenian and English query vocabulary

### 1.1 Slovenian datacenter terms

```text
podatkovni center
podatkovnega centra
podatkovni centri
racunalniski center OR racunalniskega centra
strezniski center OR strezniska soba OR streznikov
kolokacija OR gostovanje kolokacije
oblak OR oblacne storitve
virtualni podatkovni center
superracunalnik OR superracunalniski center
tovarna umetne inteligence OR SLAIF
rezervni podatkovni center OR nadomestni podatkovni center
drzavni podatkovni center OR informacijska infrastruktura
visokozmogljivo racunalnistvo OR HPC
modularni podatkovni center OR kontejnerski podatkovni center
odvecna toplota
UPS OR neprekinjeno napajanje
dizelski agregat OR agregati
transformatorska postaja OR RTP OR elektroenergetski prikljucek
hlajenje podatkovnega centra
gradbeno dovoljenje podatkovni center
uporabno dovoljenje podatkovni center
prijava zacetka gradnje podatkovni center
okoljevarstveno soglasje podatkovni center
presoja vplivov na okolje podatkovni center
OPPN podatkovni center
OPN podatkovni center
obcinski podrobni prostorski nacrt podatkovni center
prostorski izvedbeni akt podatkovni center
javna narocila podatkovni center
evidencno narocilo podatkovni center
vzdrzevanje podatkovnega centra
nadgradnja podatkovnega centra
siritev podatkovnega centra
```

### 1.2 Official source query templates

Substitute `{region}`, `{municipality}`, `{city}`, `{operator}`, `{legal_entity}`, `{UE}`, `{parcel}`, `{address}`.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center"
site:pis.eprostor.gov.si/pis-ua-jv "racunalniski center"
site:pis.eprostor.gov.si/pis-ua-jv "{operator}" "{municipality}"
site:pis.eprostor.gov.si/pis-ua-jv "{address}"
site:pis.eprostor.gov.si/pis-ua-jv "transformatorska postaja" "{municipality}"
site:gov.si "podatkovni center" "{municipality}"
site:gov.si "podatkovnega centra" "gradnja" "{city}"
site:gov.si "gradbeno dovoljenje" "podatkovni center"
site:{municipality-domain} "podatkovni center" "gradbeno dovoljenje"
site:{municipality-domain} "podatkovni center" "OPPN" OR "OPN"
site:{municipality-domain} "podatkovni center" "obcinski podrobni prostorski nacrt"
site:{municipality-domain} "strezniska" "agregat"
site:{municipality-domain} "{operator}" "gradbeno dovoljenje"
site:ejn.gov.si "podatkovni center" "{city}"
site:enarocanje.si "podatkovni center" "{city}"
site:akos-rs.si "{operator}" "podatkovni center"
site:akos-rs.si "Geoportal AKOS" "{municipality}"
site:eles.si "podatkovni center" OR "data centre"
site:sodo.si "podatkovni center" OR "data center"
site:agen-rs.si "podatkovni center"
```

### 1.3 English patterns

```text
"Slovenia" "data center" "building permit"
"Slovenia" "data centre" "construction"
"Ljubljana" "data center" "building permit"
"Maribor" "data center" ARNES "building"
"Slovenia" "data center" "grid connection"
"Slovenia" "data centre" "waste heat"
"Slovenia" "data center" "public procurement"
"Slovenia" "AI Factory" "data center" "Maribor"
"Slovenia" "cloud region" AWS Azure Google Oracle
"Slovenia" "colocation" Ljubljana Maribor Koper Nova Gorica
```

---

## 2. Official / regulatory source backbone

### 2.1 Construction permits: PIS / eGraditev / construction acts

Primary sources:

- PIS Construction Database (`Zbirka podatkov o graditvi objektov`): https://pis.eprostor.gov.si/pis-ua-jv/seznam.html?mobile=false . **Grade A** for public construction-act metadata.
- PIS/eGraditev introduction and rollout: https://pis.eprostor.gov.si/en/pis/predstavitev-sistema/uvedba-egraditev.html . **Grade A** for process. It describes eConstruction as part of the Spatial Information System, public basic construction data, registration of building permits/use permits/start notifications, and nationwide electronic operation by 2026.
- PIS front door: https://pis.eprostor.gov.si/en/pis/predstavitev-sistema . **Grade A** for spatial/planning system routing.

Fields to capture from PIS records:

- `ID akta`, procedure (`GD`, `UD`, `PG`, integrated procedure if shown);
- administrative authority (`Upravni organ`, usually UE or ministry);
- title/name (`Naziv`) and applicant/investor if displayed;
- date of application, issue, finality/finality/pravnomočnost, start-of-construction notification date;
- cadastral municipality, parcel, construction land, utility connections;
- individual objects and CC-SI classification;
- related acts (`Povezani akti`), which can link GD -> PG -> UD.

Workflow:

1. Search PIS directly by `podatkovni center`, `racunalniski center`, `strezniski`, `kolokacija`, operator legal name, and known address.
2. If direct term search fails, search by support infrastructure near candidate sites: `transformatorska postaja`, `agregat`, `hlajenje`, `energetski objekt`, `telekomunikacijski objekt`.
3. Use the graphical view to attach cadastral parcels and compare against municipality spatial plans and operator pages.
4. Store PIS act status separately from operating status. A `GD` is construction authorization; `PG` indicates start; `UD` or official handover/launch indicates use/operation.

Important caveat: Slovenia's market includes many small enterprise/server-room and government data centers located inside existing buildings. These may have no standalone building permit. For conversions, search PIS for `sprememba namembnosti`, renovation works, HVAC/UPS/generator works, and procurement records.

### 2.2 Spatial planning and municipal records

Primary sources:

- PIS/ePlan routing via Spatial Information System: https://pis.eprostor.gov.si/en/pis/predstavitev-sistema . **Grade A** for official planning-system access.
- Municipal websites and BIP-like public-document pages. Slovenia does not use one uniform municipal portal pattern; use both `obcina.si` domains and city domains.
- SURS region/municipality application for geography and region membership: https://www.stat.si/obcine/en . **Grade A** for the 12 statistical-region framework and municipality grouping.

Planning record types:

- `OPN` = municipal spatial plan;
- `OPPN` = municipal detailed spatial plan;
- `prostorski izvedbeni akt`, `prostorski akt`, `lokacijska preveritev`;
- council materials: `obcinski svet`, `gradivo`, `sklep`, `odlok`, `javna razgrnitev`, `dopolnjen osnutek`;
- land/property actions: `prodaja zemljisca`, `stavbna pravica`, `sluznost`, `komunalni prispevek`.

Municipal query templates:

```text
site:{municipality-domain} "podatkovni center" "OPPN"
site:{municipality-domain} "podatkovni center" "OPN"
site:{municipality-domain} "racunalniski center" "prostorski akt"
site:{municipality-domain} "strezniski" "prostorski"
site:{municipality-domain} "transformatorska postaja" "{operator}"
site:{municipality-domain} "odvecna toplota" "podatkovni center"
site:{municipality-domain} "{operator}" "obcinski svet"
site:{municipality-domain} "{legal_entity}" "komunalni prispevek"
```

Planning evidence is **A for land-use process** but weak for facility enumeration unless it names a data center, operator, or unmistakable support infrastructure. Use it to find parcels and early projects, then confirm with PIS/GD/PG/UD, procurement, or operator records.

### 2.3 Environment / EIA / public environmental documents

Primary sources:

- GOV.SI Environmental Assessment policy page: https://www.gov.si/en/policies/environment-and-spatial-planning/environment/environmental-assessment/ . **Grade A process source**.
- GOV.SI organization/news/document search for environment, ARSO/MOPE/MNVP notices: https://www.gov.si/ . **Grade A when the document is an agency decision or official notice**.
- Municipal public notices for `okoljevarstveno soglasje`, `okoljevarstveno dovoljenje`, `predhodni postopek`, `presoja vplivov na okolje`, `sklep`, `obvestilo javnosti`.

Search terms:

```text
"podatkovni center" "presoja vplivov na okolje"
"podatkovni center" "okoljevarstveno soglasje"
"podatkovni center" "okoljevarstveno dovoljenje"
"podatkovni center" "predhodni postopek"
"podatkovni center" "odlocba" "ARSO"
"podatkovni center" "dizelski agregat"
"podatkovni center" "hrup" "hlajenje"
"podatkovni center" "odvecna toplota"
site:gov.si "podatkovni center" "okolje"
site:gov.si "dizelski agregat" "podatkovni center"
site:{municipality-domain} "podatkovni center" "okolje"
```

Extract:

- backup generators, fuel tanks, batteries/UPS, fire suppression;
- electrical demand, transformer size, grid connection point;
- cooling technology, noise, water use, refrigerants;
- waste-heat reuse agreements and district-heating integration;
- EIA screening/decision date, authority, applicant and parcel.

Datacenters may fall below full EIA thresholds if they are modular, installed in existing buildings, or filed as IT/HVAC/electrical works. Environment records are high signal when diesel generators, large cooling systems, or waste-heat reuse are disclosed.

### 2.4 Energy and grid evidence

Primary sources:

- ELES development network page: https://www.eles.si/razvoj-prenosnega-omrezja . **Grade A** for transmission/distribution development planning.
- ELES grid connection capacity page and interactive map: https://www.eles.si/en/res-hosting-capacity-of-slovenian-transmission-network . **Grade A** for estimated available connection capacity at transmission substations; use as siting/grid-feasibility context, not facility evidence.
- ELES 2025-2034 development-plan announcement: https://www.eles.si/medijsko-sredisce/sporocila-za-javnost-in-obvestila/sporocila-za-javnost/ArticleID/21895/Elektroenergetsko-omre%C5%BEje-2025%E2%80%932034-Zgodovinski-razvojni-cikel . **Grade A** for current planning cycle.
- SODO development page: https://www.sodo.si/o-omrezju/razvoj and English SODO overview: https://www.sodo.si/en/about-sodo . **Grade A** for distribution-system planning context.
- Energy portal development plans: https://www.energetika-portal.si/dokumenti/strateski-razvojni-dokumenti/razvojni-nacrti-operaterjev-sistema/ . **Grade A** for official development-plan routing.
- Energy Agency (`Agencija za energijo`): https://www.agen-rs.si/web/en . **Grade A** regulator context.

Use cases:

- Map large projects against ELES substation capacity, especially Ljubljana, Maribor, Koper, Nova Gorica, Kranj, Celje, Novo mesto, and industrial zones.
- Search ELES/SODO/DSO and municipal material for `RTP`, `transformatorska postaja`, `prikljucitev`, `soglasje za prikljucitev`, `elektroenergetsko omrezje`.
- For public/government DCs, procurement often names power/cooling requirements more clearly than grid registers.

DSO/operator pivots:

```text
site:elektro-ljubljana.si "podatkovni center" OR "RTP" "{municipality}"
site:elektro-maribor.si "podatkovni center" OR "RTP" "{municipality}"
site:elektro-celje.si "podatkovni center" OR "RTP" "{municipality}"
site:elektro-gorenjska.si "podatkovni center" OR "RTP" "{municipality}"
site:elektro-primorska.si "podatkovni center" OR "RTP" "{municipality}"
site:eles.si "{operator}" "{municipality}"
site:sodo.si "{operator}" "{municipality}"
```

Caution: ELES capacity maps and development plans do not prove a datacenter exists. Use them to prioritize likely substations and feasibility, then require permit/operator/procurement confirmation.

### 2.5 AKOS telecommunications regulator and infrastructure context

Primary sources:

- AKOS main site: https://www.akos-rs.si/ . **Grade A regulator context**.
- AKOS operator register page: https://www.akos-rs.si/registri/seznam-registrov/operaterji . **Grade A** for registered electronic-communications operators.
- AKOS operator registration information: https://www.akos-rs.si/en/telecommunications/explore/operator-registration . **Grade A process source**.
- AKOS Geoportal overview: https://www.akos-rs.si/en/telecommunications/exposing/comparison-of-operators-electronic-communications-market-data-and-other-information-on-akos-portals . **Grade A/B** for telecom infrastructure and planned public utility infrastructure context.
- AKOS reference-offer/operator list page, useful as a telco seed list: https://www.akos-rs.si/telekomunikacije/raziscite/vzorcne-ponudbe . **Grade B** for active telecom operator pivots.

AKOS is not a datacenter permit registry. It is useful for:

- confirming telecom/network operators and registered electronic-communications providers;
- mapping electronic communications infrastructure, network connection points and build intentions through Geoportal AKOS;
- identifying interconnection/fiber context near candidate sites;
- discovering operator legal names for PIS/procurement searches.

Queries:

```text
site:akos-rs.si "podatkovni center"
site:akos-rs.si "{operator}" "register"
site:akos-rs.si "{operator}" "vzorcne ponudbe"
site:akos-rs.si "Geoportal AKOS" "{municipality}"
site:akos-rs.si "gradnja javne komunikacijske infrastrukture" "{municipality}"
```

### 2.6 Public procurement

Primary sources:

- e-JN public procurement portal: https://ejn.gov.si/ . **Grade A for tender notices and contracting metadata**.
- National public-procurement portal: https://www.enarocanje.si/ . **Grade A for notices and documents when available**.
- TED EU procurement: https://ted.europa.eu/ . **Grade A/B for EU-level notices; may lag local documents**.

High-signal examples and terms:

- e-JN result `Podatkovni center Arnes - lokaciji Maribor in Ljubljana`, procedure `JN003755/2024-EUe16/01`, contracting authority `Akademska in raziskovalna mreza Slovenije`, subject `Gradnje`. This is a strong official construction lead even if the dynamic detail page later expires.
- Search government, university, hospital and municipal tenders for `podatkovni center`, `strezniska soba`, `modularni podatkovni center`, `UPS`, `hlajenje`, `agregat`, `pozarno varovanje`, `kolokacija`, `najem podatkovnega centra`.

Templates:

```text
site:ejn.gov.si "podatkovni center" "Gradnje"
site:ejn.gov.si "podatkovni center" "Maribor" OR "Ljubljana"
site:enarocanje.si "podatkovni center" "JN"
site:ted.europa.eu "Slovenia" "data centre" "construction"
site:ted.europa.eu "Slovenia" "data center" ARNES
"podatkovni center" "JN" "naročnik" "{city}"
"modularni podatkovni center" "Univerza v Ljubljani"
```

Procurement can be better than permits for in-building or modular projects; count it as **A for purchase/build contract**, but resolve status with handover, completion certificate, use permit, or operator page.

---

## 3. Official cloud and public-sector seed list

Cloud pages prove logical region availability or absence, not physical facility addresses. As of this research pass, there is no official AWS/Azure/GCP/OCI public cloud region or AWS Local Zone named for Slovenia. Use nearby European regions as negative context, then enumerate Slovenian facilities through colo/government/operator records.

| Provider / public operator | Official source | Slovenia signal | Enumeration use |
|---|---|---|---|
| AWS | Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No Slovenia region/local zone found in official lists reviewed. Nearby regions/zones may serve Slovenian customers. | Do not infer physical DCs from AWS usage in Slovenia. Search Direct Connect/partner pages only as network leads. |
| Microsoft Azure | Geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Slovenia geography/region in official public list reviewed. | Treat Azure reseller/cloud-service pages as enterprise services, not hyperscale DC evidence. |
| Google Cloud | Locations: https://cloud.google.com/about/locations ; Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones | No Slovenia region in official public list reviewed. | Use only for cloud-market context unless a Slovenian colocation/interconnect facility is listed officially. |
| Oracle Cloud Infrastructure | Regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Slovenia commercial OCI region in official list reviewed. | No facility inference. Search Oracle partner/local government cloud contracts only as service leads. |
| ARNES | Project page: https://www.arnes.si/en/the-first-arnes-data-centre-of-the-future-will-be-located-in-maribor/ ; GOV.SI groundbreaking: https://www.gov.si/novice/2025-05-06-odkrit-temeljni-kamen-za-arnesov-podatkovni-center-maribor/ ; event: https://www.gov.si/dogodki/2025-05-06-odkritje-temeljnega-kamna-za-podatkovni-center-arnes-maribor/ | New Maribor research/HPC/AI data center, construction started May 2025, planned completion/operation around 2026, waste-heat reuse cooperation. | A seed for Podravska/Maribor; verify PIS acts, e-JN records, municipality and ARNES updates. |
| Ministry of Digital Transformation / Posta Slovenije | GOV.SI handover: https://www.gov.si/novice/2025-09-30-posta-slovenije-ministrstvu-za-digitalno-preobrazbo-predala-v-uporabo-nov-podatkovni-center/ | New data center at postal logistics center in Ljubljana handed to ministry on 2025-09-30; connected to existing primary DCs leased from Posta Slovenije. | A for official operating/handover signal; locate via Posta/Posita and PIS records. |
| SURS | Regions/municipalities: https://www.stat.si/obcine/en | Official regional/municipal grouping. | Use for region sweep organization and municipality normalization. |

---

## 4. Per-statistical-region official enumeration approach

Use SURS region names as buckets, but query by municipality/city, UE and local domains. Standard regional loop:

1. Pull all municipality names in the region from SURS or the project manifest.
2. Run the PIS searches: datacenter terms, operator names, `RTP/transformatorska postaja`, `agregat`, known addresses.
3. Run municipal-domain searches for OPN/OPPN/council/procurement/environment terms.
4. Run ELES/SODO/DSO capacity and substation context for candidates above small server-room scale.
5. Run AKOS operator/Geoportal checks for telecom/fiber context.
6. Confirm status with operator/government handover/opening, PIS `PG/UD`, or procurement completion.

### 4.1 Osrednjeslovenska (Central Slovenia) - Ljubljana, Trzin, Domzale, Logatec, Vrhnika, Grosuplje

Highest priority official sweep. Known public signals include Ljubljana colocation, SIX/ARNES, Posita/Posta, ministry-leased data centers, telecom operators, and modular/university projects.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Ljubljana"
site:pis.eprostor.gov.si/pis-ua-jv "Tehnoloski park" "Ljubljana"
site:pis.eprostor.gov.si/pis-ua-jv "Cesta v Mestni log" OR "postni logistični center"
site:gov.si "podatkovni center" "Ljubljana"
site:ljubljana.si "podatkovni center" OR "strezniska"
site:ljubljana.si "OPPN" "podatkovni center"
site:uni-lj.si "podatkovni center" OR "modularni podatkovni center"
site:ejn.gov.si "podatkovni center" "Ljubljana"
site:akos-rs.si "Ljubljana" "Geoportal AKOS"
site:elektro-ljubljana.si "podatkovni center" OR "RTP" "Ljubljana"
```

### 4.2 Podravska - Maribor, Ptuj, Slovenska Bistrica, Ruše, Tezno

Highest priority outside Ljubljana because ARNES Maribor and Posta/Posita Maribor are official/public-sector leads.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Maribor"
site:gov.si "Arnesov podatkovni center Maribor"
site:arnes.si "podatkovni center" "Maribor"
site:ejn.gov.si "Podatkovni center Arnes" "Maribor"
site:maribor.si "podatkovni center" OR "odvecna toplota"
site:maribor.si "Energetika Maribor" "podatkovni center"
site:eles.si "Maribor" "podatkovni center" OR "RTP"
site:elektro-maribor.si "podatkovni center" OR "RTP" "Maribor"
```

### 4.3 Goriska - Nova Gorica, Ajdovscina, Sempeter-Vrtojba

Focus on Arctur/Nova Gorica leads, cross-border Trieste fiber/colo adjacency, and municipal/PIS confirmation.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Nova Gorica"
site:novagorica.si "podatkovni center" OR "racunalniski center"
site:ajdovscina.si "podatkovni center"
site:sempeter-vrtojba.si "podatkovni center" OR "strezniska"
site:gov.si "podatkovni center" "Nova Gorica"
site:elektro-primorska.si "RTP" "Nova Gorica" "podatkovni"
```

### 4.4 Obalno-kraska - Koper, Izola, Piran, Ankaran, Sezana

Focus on Koper commercial/telecom leads, port/logistics IT, cross-border Trieste interconnection, and coastal municipal records.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Koper"
site:koper.si "podatkovni center" OR "strezniska"
site:ekopercapodistria.si "podatkovni center" OR "OPPN"
site:izola.si "podatkovni center"
site:piran.si "podatkovni center"
site:sezana.si "podatkovni center" OR "racunalniski"
site:elektro-primorska.si "RTP" "Koper" "podatkovni"
```

### 4.5 Gorenjska - Kranj, Skofja Loka, Jesenice, Radovljica

Focus on Kranj/technology-company data rooms and telecom/industrial campuses.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Kranj"
site:kranj.si "podatkovni center" OR "strezniska"
site:kranj.si "transformatorska postaja" "{operator}"
site:gov.si "podatkovni center" "Kranj"
site:elektro-gorenjska.si "RTP" "Kranj" OR "podatkovni center"
```

### 4.6 Savinjska - Celje, Velenje, Zalec, Sostanj

Focus on telecom/industrial server rooms, power-industry sites, and local public-sector infrastructure.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Celje"
site:celje.si "podatkovni center" OR "strezniska"
site:velenje.si "podatkovni center" OR "racunalniski center"
site:sostanj.si "podatkovni center" OR "strezniska"
site:elektro-celje.si "RTP" "Celje" OR "podatkovni center"
```

### 4.7 Jugovzhodna Slovenija - Novo mesto, Kocevje, Crnomelj, Trebnje

Focus on municipal/industrial IT, automotive/pharma supply-chain sites, and public-sector server rooms. Expect few commercial DC leads.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Novo mesto"
site:novomesto.si "podatkovni center" OR "strezniska"
site:kocevje.si "podatkovni center"
site:crnomelj.si "podatkovni center"
site:elektro-ljubljana.si "RTP" "Novo mesto" OR "Kocevje"
```

### 4.8 Pomurska - Murska Sobota, Lendava, Gornja Radgona

Lower-probability region; search public-sector, telco, and industrial-zone records.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Murska Sobota"
site:murska-sobota.si "podatkovni center" OR "strezniska"
site:lendava.si "podatkovni center"
site:elektro-maribor.si "RTP" "Murska Sobota" OR "podatkovni center"
```

### 4.9 Koroska - Slovenj Gradec, Ravne na Koroskem, Dravograd

Lower probability; search industrial/public-sector IT and energy support terms.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Slovenj Gradec"
site:slovenjgradec.si "podatkovni center" OR "strezniska"
site:ravne.si "podatkovni center"
site:dravograd.si "podatkovni center"
site:elektro-celje.si "RTP" "Koroska" "podatkovni"
```

### 4.10 Posavska - Krsko, Brezice, Sevnica

Search energy/industrial/public-sector sites; do not confuse nuclear/power infrastructure with a DC without direct IT-facility evidence.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Krsko"
site:krsko.si "podatkovni center" OR "strezniska"
site:brezice.si "podatkovni center"
site:sevnica.si "podatkovni center"
site:eles.si "RTP" "Krsko" "podatkovni"
```

### 4.11 Primorsko-notranjska - Postojna, Ilirska Bistrica, Cerknica

Search logistics/industrial zones and PIS because this region was early in eGraditev rollout.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Postojna"
site:postojna.si "podatkovni center" OR "strezniska"
site:ilirska-bistrica.si "podatkovni center"
site:cerknica.si "podatkovni center"
```

### 4.12 Zasavska - Trbovlje, Hrastnik, Zagorje ob Savi

Lower probability; search public-sector, industrial redevelopment and energy-grid terms.

```text
site:pis.eprostor.gov.si/pis-ua-jv "podatkovni center" "Trbovlje"
site:trbovlje.si "podatkovni center" OR "strezniska"
site:hrastnik.si "podatkovni center"
site:zagorje.si "podatkovni center"
site:elektro-ljubljana.si "RTP" "Zasavje" "podatkovni"
```

---

## 5. Evidence grading and dedupe rules

- **A**: PIS `GD/PG/UD` act, official GOV.SI/municipal/agency decision, official procurement award/notice, ELES/SODO/AKOS official infrastructure context, operator-owned facility page or government handover/opening.
- **B**: DCD/Slovenia Times/Finance/Monitor/ICT press, association/conference material, customer case studies by engineering contractors, official vendor pages that describe services but not exact facilities.
- **C**: DataCenterMap, Cloudscene, Datacenters.com, Inflect, Baxtel, market-research pages, directory snippets and SEO pages.

Dedupe:

- Normalize legal entities: `Posta Slovenije d.o.o.` / `Posita`; `Akademska in raziskovalna mreza Slovenije` / `ARNES`; telecom brand vs registered entity (`T-2 d.o.o.`, `Telemach d.o.o.`, `A1 Slovenija`, `Telekom Slovenije`, `Softnet`, `MEGA M`).
- Normalize Slovene diacritics in search and storage: `Š`/`S`, `Č`/`C`, `Ž`/`Z`, `Koroška`/`Koroska`, `Obalno-kraška`/`Obalno-kraska`, `Šempeter-Vrtojba`/`Sempeter-Vrtojba`.
- One campus may have multiple acts: new building, utility connection, transformer station, cooling plant, generator, and use permit. Keep the same facility id when address/parcel/operator align.
- Do not count cloud service/reseller offices, corporate headquarters, software companies or government "data portals" as facilities unless there is physical data-center/server-room evidence.
