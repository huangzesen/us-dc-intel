# PL Explorer Official - Poland Datacenter Enumeration via Permits, Grid, Regulator, Cloud, and Colo Sources

Date: 2026-08-12. Scope: Poland (PL), 16 wojewodztwa plus powiat/gmina drill-down. Focus angle: official/regulatory/cloud-first enumeration for datacenter facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Structural facts that shape Poland enumeration

- Poland has no single public "datacenter registry". Build the census by joining **GUNB/RWDZ construction records**, gmina/powiat planning files, environmental information portals, **PSE/grid connection records**, official cloud-region pages, and operator facility pages.
- The operational permit unit is usually **gmina** or **powiat / city with powiat rights**, not wojewodztwo. Wojewodztwo portals and voivode offices are still useful for environmental, strategic, and appeal records.
- The most important official construction source is GUNB's **RWDZ - Rejestr Wnioskow, Decyzji i Zgloszen**. Public search is at https://wyszukiwarka.gunb.gov.pl/wyniki/ and map search is at https://wyszukiwarka.gunb.gov.pl/mapa/. API documentation is exposed at https://dev.wyszukiwarka.gunb.gov.pl/docs. **Grade A** for permit/application records; public UI may require CAPTCHA, so use official API/export routes where available and treat automated scraping cautiously.
- Polish building records may not say "data center". Search by local words and project functions: `centrum danych`, `centrum przetwarzania danych`, `serwerownia`, `budynek uslugowy`, `budynek technologiczny`, `budynek przemyslowy`, `stacja transformatorowa`, `agregaty pradotworcze`, `magazyn energii`, `chlodzenie`.
- Grid evidence is unusually important. PSE publishes a quarterly **Wykaz obiektow planowanych do przylaczenia do sieci przesylowej** and related application/completeness/refusal files at https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/wykaz-obiektow-planowanych-do-przylaczenia. PSE states this includes generation, storage, distribution systems, **odbiorcze installations** planned for transmission connection, refusals, pending applications, and complete applications; editable XLS/XLSX files are linked. **Grade A for connection-process facts**, but not proof of construction.
- Since **1 July 2026**, PSE directs applications for transmission-grid connection conditions through **ESOP - Elektroniczny System Obslugi Przylaczen** (https://esop.pse.pl), announced at https://www.pse.pl/-/uruchomilismy-elektroniczny-system-obslugi-przylaczen. Use ESOP/PSE references as a current process clue, not a public facility list.
- Regulator **UKE** is useful for telecom/broadband infrastructure and market context, but it is not a datacenter permit registry. UKE/BIP plans and FERC/POPC materials can help identify fiber buildouts and operators; facility enumeration still needs construction/environment/grid/operator confirmation.
- Major market geography: **Warsaw/Mazowieckie** dominates cloud and interconnection; secondary clusters are **Poznan/Wielkopolskie**, **Krakow/Malopolskie**, **Wroclaw/Dolnoslaskie**, **Katowice/Silesia**, **Gdansk/Pomerania**, **Lodz/Lodzkie**, and selected large-power industrial/renewable-grid sites.

Lifecycle vocabulary:

`studium / MPZP / WZ` < `decyzja o srodowiskowych uwarunkowaniach` < `wniosek o pozwolenie na budowe` < `decyzja o pozwoleniu na budowe` < `rozpoczecie budowy` < `pozwolenie na uzytkowanie` < `uruchomienie / oddanie do uzytku`

Only count `pozwolenie na budowe`, `rozpoczecie budowy`, `pozwolenie na uzytkowanie`, or operator-confirmed launch as strong facility evidence. Treat MPZP/WZ and PSE connection applications as planned/pre-development evidence until cross-checked.

---

## 1. Polish and English query patterns

### 1.1 Core Polish terms

```text
centrum danych
centra danych
centrum przetwarzania danych
CPD
data center OR datacenter
serwerownia
kolokacja OR colocation
chmura obliczeniowa
region chmurowy
hiperskalowe centrum danych
kampus centrum danych
budowa centrum danych
pozwolenie na budowe centrum danych
wniosek o pozwolenie na budowe centrum danych
pozwolenie na uzytkowanie centrum danych
decyzja o srodowiskowych uwarunkowaniach centrum danych
raport oddzialywania na srodowisko centrum danych
MPZP centrum danych
warunki zabudowy centrum danych
stacja transformatorowa centrum danych
warunki przylaczenia centrum danych
agregaty pradotworcze centrum danych
chlodzenie centrum danych
cieplo odpadowe centrum danych
```

### 1.2 Permit and planning queries

Substitute `{wojewodztwo}`, `{powiat}`, `{gmina}`, `{miasto}`, `{operator}`, `{legal_entity}`, `{parcel}`.

```text
site:wyszukiwarka.gunb.gov.pl "centrum danych" "{miasto}"
site:wyszukiwarka.gunb.gov.pl "centrum przetwarzania danych"
"{miasto}" "centrum danych" "pozwolenie na budowe"
"{gmina}" "centrum danych" "pozwolenie na budowe"
"{powiat}" "centrum danych" "pozwolenie na budowe"
"{miasto}" "data center" "pozwolenie na budowe"
"{legal_entity}" "pozwolenie na budowe"
"{operator}" "{miasto}" "pozwolenie na uzytkowanie"
site:{gmina-domain} "centrum danych" "MPZP"
site:{gmina-domain} "centrum danych" "warunki zabudowy"
site:{gmina-domain} "centrum danych" "decyzja srodowiskowa"
filetype:pdf "centrum danych" "pozwolenie na budowe" "{miasto}"
filetype:pdf "centrum przetwarzania danych" "decyzja" "{wojewodztwo}"
```

### 1.3 Energy/grid/environment queries

```text
site:pse.pl "centrum danych" "warunki przyłączenia"
site:pse.pl "centrum danych" "sieci przesyłowej"
site:pse.pl "Wykaz obiektów planowanych do przyłączenia" "centrum danych"
site:pse.pl "instalacji odbiorczych" "centrum danych"
site:pse.pl "odmów przyłączenia" "centrum danych"
site:{osd-domain} "centrum danych" "przyłączenie"
"{miasto}" "centrum danych" "stacja transformatorowa"
"{miasto}" "centrum danych" "GPZ"
"{operator}" "{miasto}" "MW" "centrum danych"
"{operator}" "{gmina}" "warunki przyłączenia"
site:ekoportal.gov.pl "centrum danych"
site:gov.pl "centrum danych" "decyzja o środowiskowych uwarunkowaniach"
site:gov.pl "centrum danych" "Regionalny Dyrektor Ochrony Środowiska"
```

### 1.4 English patterns

```text
"Poland" "data center" "building permit"
"Warsaw" "data center" "building permit"
"Poland" "data center" "grid connection"
"Poland" "data center" "PSE" MW
"Poland" "hyperscale campus" "MW"
"Warsaw" "Azure" "Poland Central" "datacenter region"
"Warsaw" "Google Cloud" "europe-central2"
"AWS" "Local Zone" "Warsaw" "Poland"
"{operator}" "{city}" "data center" "Poland"
```

---

## 2. Official / regulatory source backbone

### 2.1 Construction permits: GUNB / RWDZ

Primary sources:

- GUNB e-Budownictwo front door: https://e-budownictwo.gunb.gov.pl/. **Grade A**. Links users to RWDZ and related construction services.
- Public RWDZ search: https://wyszukiwarka.gunb.gov.pl/wyniki/. **Grade A**. It covers applications, decisions, and selected notifications; public browsing may require CAPTCHA.
- RWDZ map search: https://wyszukiwarka.gunb.gov.pl/mapa/. **Grade A**. Useful once a candidate address or parcel identifier is known.
- RWDZ API documentation: https://dev.wyszukiwarka.gunb.gov.pl/docs. **Grade A**. Use for repeatable official data pulls when the endpoint remains publicly available.

Fields to capture from RWDZ/permit records:

- document type: `wniosek`, `decyzja`, `zgloszenie`;
- authority: starosta, prezydent miasta, wojewoda, or specialist authority;
- investment category/description;
- investor legal name;
- address, cadastral precinct, parcel number;
- filing date, decision date, decision status;
- construction category if visible, especially service/industrial/technical buildings and electrical infrastructure.

Do not require the phrase `centrum danych`; many projects will be filed as technical, service, office-technical, industrial, or electrical buildings. Cross-check large anonymous technical buildings near known campuses with operator pages, council files, and grid records.

### 2.2 Local planning and land-use records

Poland's key local planning records are **MPZP** (miejscowy plan zagospodarowania przestrzennego), **WZ** (decyzja o warunkach zabudowy), council resolutions, and public consultations. These are often on gmina/city BIP pages rather than national portals.

Useful portals and patterns:

- National spatial-data viewer / Geoportal: https://www.geoportal.gov.pl/. **Grade A** for cadastral/geospatial context.
- Ministry spatial planning page and local plan datasets via official planning infrastructure: start from https://www.gov.pl/web/rozwoj-technologia. **Grade A for policy/process**, then pivot to gmina BIP.
- City/gmina BIP portals: search `bip {gmina} centrum danych`, `bip {miasto} MPZP centrum danych`, `uchwala centrum danych`, `wylozenie planu centrum danych`.
- Council systems: search `rada gminy`, `rada miasta`, `sesja`, `uchwala`, `sprzedaz nieruchomosci`, `dzierzawa`, `sluzebnosc przesylu`, `stacja transformatorowa`.

Planning evidence is useful for early pipeline detection, but it should be labelled lower than permit evidence unless the plan explicitly reserves land for `centrum danych` or names the investor/project.

### 2.3 Environment / EIA / public information

Primary sources:

- Ekoportal: https://www.ekoportal.gov.pl/. **Grade A** for environmental-information access routes and public environmental data links.
- General Directorate for Environmental Protection (GDOŚ): https://www.gov.pl/web/gdos. **Grade A**. GDOŚ/RDOŚ pages cover environmental-impact assessment functions and regional environmental authorities.
- Local gmina/powiat/wojewoda BIP pages for `decyzja o srodowiskowych uwarunkowaniach`, `obwieszczenie`, `karta informacyjna przedsięwzięcia`, `raport ooś`.

What to extract:

- emergency generators (`agregaty pradotworcze`), fuel storage, batteries/UPS;
- electricity demand / transformer size / substation;
- cooling technology, water demand, noise;
- site area and phasing;
- waste heat (`cieplo odpadowe`) and district-heating connection;
- environmental decision date and authority.

Datacenters may appear indirectly through backup power, electrical substations, or cooling-water permits rather than a datacenter category. Search both Polish terms and operator legal names.

### 2.4 PSE and grid connection evidence

Primary sources:

- PSE planned-connection page: https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/wykaz-obiektow-planowanych-do-przylaczenia. **Grade A**. Download both PDF and editable XLS/XLSX files.
- PSE connection-capacity information: https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/informacja-o-dostepnosci-mocy-przylaczeniowej. **Grade A** for grid availability context.
- PSE ESOP announcement: https://www.pse.pl/-/uruchomilismy-elektroniczny-system-obslugi-przylaczen and ESOP portal https://esop.pse.pl. **Grade A process source**.
- PSE highest-voltage network map: https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/plan-sieci-elektroenergetycznej-najwyzszych-napiec. **Grade A** for transmission geography.

Use PSE files to identify:

- applications for connection conditions waiting for verification;
- complete applications;
- issued/refused connection conditions;
- object type (`instalacja odbiorcza`, storage, generation, distribution system);
- connection point/substation, requested MW, applicant name, commune/voivodeship if present.

Important caution: connection applications in Poland are currently noisy and can include speculative or duplicate large-load requests. A PSE application/condition is **not** a building permit, construction start, or operating facility. Store separate fields for `requested_connection_MW`, `connection_point`, `application_status`, `permit_status`, and `operational_status`.

Distribution grid operators to query by region:

- PGE Dystrybucja: https://pgedystrybucja.pl/
- Tauron Dystrybucja: https://www.tauron-dystrybucja.pl/
- Enea Operator: https://www.operator.enea.pl/
- Energa-Operator: https://energa-operator.pl/
- Stoen Operator (Warsaw): https://stoen.pl/

DSO pages often publish source-connection lists under Energy Law obligations, but large datacenters may appear as loads or substations outside those source lists. Search each DSO for `centrum danych`, `GPZ`, `stacja`, `przyłączenie`, and candidate gmina names.

### 2.5 UKE and telecom/regulatory context

Primary sources:

- UKE main site: https://www.uke.gov.pl/ and BIP: https://bip.uke.gov.pl/. **Grade A regulator context**.
- UKE plans and FERC/POPC materials identify broadband-infrastructure programs, intervention areas, and telecom operators, but generally not datacenter permits.
- UKE can support operator identity and network/fiber context. Treat UKE evidence as **supporting context** unless a document names a datacenter facility, telecom node, or data-processing center.

Useful UKE queries:

```text
site:uke.gov.pl "centrum danych"
site:bip.uke.gov.pl "centrum danych"
site:uke.gov.pl "węzeł telekomunikacyjny" "{miasto}"
site:uke.gov.pl "FERC" "{operator}"
site:uke.gov.pl "POPC" "{operator}" "{powiat}"
```

---

## 3. Official cloud and operator seed list

Cloud-region pages prove a metro/region presence, not exact physical addresses. Use them to seed Warsaw-area permit/grid searches and legal-entity pivots.

| Provider | Official source | Poland signal | Enumeration use |
|---|---|---|---|
| Microsoft Azure | https://news.microsoft.com/europe/2023/04/26/microsoft-launches-its-first-datacenter-region-in-poland-bringing-new-opportunities-to-develop-the-digital-economy/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list | `Poland Central`, physical location Warsaw, region name `polandcentral`; Microsoft says the Polish cloud region has three independent physical locations around Warsaw. | Search `Microsoft`, `Poland Central`, `Microsoft 365`, `Azure`, `Microsoft sp. z o.o.`, and local SPVs around Warsaw/Mazowieckie. |
| Google Cloud | https://cloud.google.com/blog/products/infrastructure/google-cloud-region-in-warsaw-poland-is-now-open and https://docs.cloud.google.com/compute/docs/regions-zones | Warsaw region `europe-central2` with zones `europe-central2-a/b/c`. | Search `Google Cloud`, `europe-central2`, `Google Poland`, `Chmura Krajowa`, `OChK`, Warsaw-area permits/grid. |
| AWS | https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html and https://aws.amazon.com/about-aws/global-infrastructure/ | AWS has Warsaw listed as a Local Zone geography in official docs/search; no Poland AWS Region confirmed from the official global regions list. | Count AWS Warsaw as edge/local-zone/network seed, not a full regional datacenter campus unless official AWS region or local permit evidence is found. |
| OVHcloud | https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ and official location pages | Warsaw/Central Europe service presence appears in official/market maps; exact facility details require operator confirmation. | Search `OVHcloud Warszawa`, `OVH sp. z o.o.`, permits, and telecom/colo partners. |
| Oracle / IBM / Alibaba / others | Official global-region pages | No Poland full region should be assumed without current official confirmation. | Use as network/PoP seeds only unless official Poland datacenter/region page exists. |

Major colocation/operator official seeds:

| Operator | Official source | Poland seed |
|---|---|---|
| Beyond.pl | https://www.beyond.pl/en/data-centers-campus/location-poland/ and https://www.beyond.pl/en/data-centers-campus/beyond-pl-data-center-2/ | Poznan campus; official page states a multi-tier 150 MW campus and DC2 at A. Kreglewskiego 11 with published space/PUE/certifications. Search Poznan permits for Beyond.pl, DC1/DC2, `Kreglewskiego`, `Polwiejska`, and any campus expansions. |
| Atman | https://atman.pl/en/atman-data-center/warsaw-1/, https://atman.pl/en/atman-data-center/warsaw-2/, and https://datacenterpoland.com/ | Warsaw-1 at Grochowska 21a; Warsaw-2 in central Warsaw; WAW-3 campus near Ozarow/Duchnice with 14.4 MW per building and 43.2 MW target on official campaign site. Search Warsaw, Ozarow Mazowiecki, Duchnice, Grochowska, Atman sp. z o.o. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/poland-colocation/warsaw-data-centers | Warsaw WA1, WA2, WA3, and WA4x/xScale references. WA1 page lists Aleje Jerozolimskie 65/79; WA2 at Poleczki 23; WA3 in Salomea District. Search Equinix, WA1/WA2/WA3/WA4x, Salomea, Poleczki, Aleje Jerozolimskie. |
| Netia | https://www.netia.pl/en/instytucje-publiczne/produkty/data-center-cloud/data-center | MIND in Jawczyce, SOUL in Krakow, BRAIN in Grodzisk Mazowiecki, HEART in Warsaw. Search Netia, Jawczyce, Grodzisk Mazowiecki, Krakow, Warsaw. |
| T-Mobile Polska | https://biznes.t-mobile.pl/en/products-and-services/data-center/server-colocation | Official page says 5 commercial data centers in Krakow, Warsaw and Wroclaw; Szlachecka expansion completed December 2021; Piaseczno is described as the largest/key T-Mobile Poland DC. Search T-Mobile, Szlachecka, Piaseczno, Krakow, Wroclaw. |
| Orange Polska / Polcom / Comarch / 3S / Exea / Data4 / Vantage / EdgeConneX-type entrants | Official operator pages and local permits | Treat as secondary seed set. Confirm with RWDZ, environmental decisions, and operator pages before counting. |

Operator pivot queries:

```text
"Beyond.pl" Poznan "pozwolenie na budowe"
"Beyond.pl" "Kreglewskiego" "centrum danych"
"Atman" Duchnice "pozwolenie na budowe"
"Atman" "Ozarow" "centrum danych"
"Equinix" WA4x Warsaw "building permit"
"Equinix" "Poleczki" "pozwolenie"
"Netia" Jawczyce "centrum danych"
"T-Mobile" Szlachecka "centrum przetwarzania danych"
"T-Mobile" Piaseczno "data center"
"Polcom" Skawina "centrum danych"
"Comarch" Krakow "data center"
```

---

## 4. Per-division enumeration workflow

Use wojewodztwo as the routing layer, then drill into powiat/gmina/city records.

1. **National official pull**: query RWDZ/GUNB for datacenter terms and known operator legal names; pull PSE XLS/XLSX connection files; check PSE refusals and pending/complete applications; search Ekoportal/GDOŚ/RDOŚ and UKE for supporting records.
2. **Cloud/colo seed**: start from official Azure, Google Cloud, AWS Local Zone, Beyond.pl, Atman, Equinix, Netia, T-Mobile pages. Generate city/gmina/legal-entity pivots.
3. **Wojewodztwo sweep**: search voivode office, RDOŚ regional office, marshal office, and official regional development pages for `centrum danych`, `centrum przetwarzania danych`, `decyzja srodowiskowa`, `inwestycja`, `strefa ekonomiczna`.
4. **Powiat/gmina sweep**: search BIP, council resolutions, planning documents, land-sale notices, and local construction authority pages. Use RWDZ map search for candidate parcels.
5. **Grid validation**: for every candidate, check PSE/DSO terms: `warunki przylaczenia`, `GPZ`, `stacja transformatorowa`, `linia 110 kV`, `400 kV`, `220 kV`, `moc przylaczeniowa`, `odmowa przylaczenia`.
6. **Evidence grading**: A = permit/environment/grid/operator official; B = reputable trade press, legal advisories, commercial real-estate reports; C = marketplace lists, maps, social posts, unsourced capacity claims.

### 4.1 Wojewodztwo priority routing

| Wojewodztwo | Priority cities/gminy | First routes | Notes |
|---|---|---|---|
| Mazowieckie | Warszawa, Piaseczno, Jawczyce/Ozarow/Michalowice, Grodzisk Mazowiecki, Duchnice, Raszyn/Salomea, Pruszkow | RWDZ, Warsaw BIP, Mazowieckie RDOŚ, Stoen Operator, PGE Dystrybucja, PSE | Highest priority: Azure Poland Central, Google Warsaw, Equinix, Atman, Netia, T-Mobile. Search Warsaw districts and suburban gminy, not only "Warszawa". |
| Wielkopolskie | Poznan | RWDZ, Poznan BIP, Wielkopolskie RDOŚ, Enea Operator, PSE | Beyond.pl campus/DC1/DC2; search Poznan street names and expansion terms. |
| Malopolskie | Krakow, Skawina, Zabierzow | RWDZ, Krakow BIP, Malopolskie RDOŚ, Tauron Dystrybucja | Netia SOUL, T-Mobile Krakow, Comarch/Polcom-type facilities. |
| Dolnoslaskie | Wroclaw, Bielany Wroclawskie, Kobierzyce | RWDZ, Wroclaw BIP, Dolnoslaskie RDOŚ, Tauron Dystrybucja/PSE | Wroclaw is a strong secondary metro and enterprise/edge location. Search special economic zones and industrial parks. |
| Slaskie | Katowice, Gliwice, Sosnowiec, Chorzow | RWDZ, Slaskie RDOŚ, Tauron Dystrybucja | Industrial grid/fiber assets; Atman/3S/telco and enterprise facilities likely. |
| Pomorskie | Gdansk, Gdynia, Slupsk area | RWDZ, Pomorskie RDOŚ, Energa-Operator, PSE | Watch port/subsea/fiber and speculative hyperscale/AI campuses; require permit/grid confirmation. |
| Lodzkie | Lodz, Strykow, Zgierz | RWDZ, Lodzkie RDOŚ, PGE Dystrybucja | Central logistics/fiber/power geography; search `centrum danych` plus industrial parks. |
| Kujawsko-Pomorskie | Bydgoszcz, Torun | RWDZ, RDOŚ, Enea/Energa | Lower density; query telco, public-sector, and edge facilities. |
| Lubelskie | Lublin | RWDZ, RDOŚ, PGE Dystrybucja | Sweep public-sector/cloud-edge and university/HPC terms. |
| Lubuskie | Zielona Gora, Gorzow, border industrial sites | RWDZ, RDOŚ, Enea | Watch Germany-border fiber/power siting; validate with permits. |
| Opolskie | Opole | RWDZ, RDOŚ, Tauron | Lower density; include industrial energy sites. |
| Podkarpackie | Rzeszow | RWDZ, RDOŚ, PGE | Search defense/aerospace/IT parks but avoid counting generic server rooms. |
| Podlaskie | Bialystok | RWDZ, RDOŚ, PGE | Lower density; telco/public-sector edge. |
| Swietokrzyskie | Kielce | RWDZ, RDOŚ, PGE | Lower density; search `centrum przetwarzania danych` and public IT facilities. |
| Warminsko-Mazurskie | Olsztyn, Elblag | RWDZ, RDOŚ, Energa/PGE | Lower density; verify any renewable-power campus claims. |
| Zachodniopomorskie | Szczecin, Koszalin | RWDZ, RDOŚ, Enea/ENEA Operator, PSE | Port/fiber/renewables angle; distinguish industrial power projects from datacenters. |

### 4.2 Standard per-division checklist

For each wojewodztwo/powiat/gmina:

```text
1. RWDZ search: "centrum danych", "centrum przetwarzania danych", "serwerownia", operator names.
2. BIP search: MPZP/WZ, environmental decisions, council resolutions, land sale/easement.
3. RDOŚ/Ekoportal search: environmental decision, EIA report, generators, cooling, substation.
4. PSE/DSO search: connection point, requested MW, refusal/complete application, substation works.
5. Operator page validation: official facility name, address/city, IT space, MW, launch/phase.
6. Trade press only after official sweep; use it to find project names, then return to official files.
```

---

## 5. Reliability and counting rules

- **Count as operational** only with operator official page, occupancy/launch announcement, `pozwolenie na uzytkowanie`, or equivalent strong evidence.
- **Count as under construction** with building permit plus construction-start/operator statement, tender/contractor launch, or official site works record.
- **Count as planned/permitted** with RWDZ building-permit decision, environmental decision, named MPZP/WZ, or land transaction with project description.
- **Count as grid pipeline only** with PSE/DSO application/condition/refusal and no planning/building permit. Do not merge speculative duplicate grid applications into facility counts unless same legal entity/site is verified.
- **Never equate cloud zones with exact facilities.** Azure/Google/AWS locality confirms regional infrastructure only; exact buildings require permit/grid/operator evidence.
- **Keep capacities typed:** `IT load`, `gross power`, `requested grid connection`, `generator capacity`, `contracted energy`, and `marketed campus capacity` are separate fields.

---

## 6. Secondary sources to use carefully

Use these for leads, not final counts without primary confirmation:

- WysokieNapiecie / energy trade press reports on PSE datacenter connection queues. **Grade B** for sector-scale claims; verify project details in PSE files.
- DCD, DataCenterDynamics, Baxtel, Data Center Map, Datacenters.com, commercial market reports. **Grade B/C depending on source and sourcing**; good for operator names, facility codes, launch dates, and addresses to back-check.
- Polish law-firm briefings (CMS, Dudkowiak, Miller Canfield, PAIH-style guides). **Grade B for permitting-process explanation**, not facility evidence.

High-value secondary lead queries:

```text
"Poland data center market" Atman Beyond Equinix Netia T-Mobile
"centra danych" PSE "GW"
"centrum danych" "warunki przyłączenia" "GW"
"Warsaw data center campus" "MW"
"Poznan data center campus" "Beyond.pl" "MW"
```
