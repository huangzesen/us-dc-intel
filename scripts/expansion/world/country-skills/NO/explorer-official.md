# NO Explorer Official - Norway Datacenter Enumeration

Date: 2026-08-12. Scope: Norway (NO). Repo divisions use the 2020-2023 county labels plus Arctic territories: Oslo; Rogaland; More and Romsdal; Northland; Svalbard; Jan Mayen; Viken; Inland; Vestfold and Telemark; Agder; Westland; Trondelag; Troms and Finnmark.

Purpose: enumerate Norwegian data centers from official registers, municipal planning/building records, environmental permits, grid records, and regulator/government sources. Use industry sources only to discover names, then confirm through the official sources below.

Reliability grades:

- Grade A: official/primary source proving the specific fact: Nkom data-centre register, municipal planning/building/postjournal record, Statsforvalteren/Miljodirektoratet permit, NVE/Statnett grid document, Lovdata law/regulation, operator-owned page for its own facility.
- Grade B: credible secondary source with named operator, place, date, and status, but not the underlying permit/register.
- Grade C: directories, market reports, social posts, rumors, or press without a source trail. Use as leads only.

## 0. Norway-specific structure

### 0.1 Master register: Nkom

Norway's national data-centre regulation started on 2025-01-01 with the new Electronic Communications Act (`ekomloven`) and the data-centre regulation (`datasenterforskriften`). Data-centre operators above the regulation threshold must register with the National Communications Authority (Nkom).

Primary URLs:

- Nkom data-centre landing page: https://nkom.no/datasenter
- Nkom public commercial-operator overview: https://nkom.no/datasenter/oversikt
- Nkom CSV export: https://stenonicprdnoea01.blob.core.windows.net/enonicpubliccontainer/prd/tildeling/datasenter/datasenter-operatorer.csv
- Lovdata regulation: https://lovdata.no/dokument/SF/forskrift/2024-12-18-3313
- Government regulation notice: https://www.regjeringen.no/no/aktuelt/ny-datasenterforskrift/id3080690/

Current verified state on 2026-08-12: the Nkom overview is marked "Sist oppdatert: 11.08.2026", reports 115 registered data centres including internal sites, and lists 61 commercial data-centre operators. The public table names commercial operators only; it does not publish names/details for business-internal data centres for security and preparedness reasons. Therefore:

- Use Nkom as the Grade A census of commercial operators and national counts.
- Do not assume the Nkom table gives all site addresses or all enterprise/internal facilities.
- For facility-level rows, pivot from Nkom operator names to municipal permits, environmental permits, NVE/Statnett documents, and operator pages.
- Keep crypto-mining flags exactly as Nkom reports them; do not reclassify without a primary update.

### 0.2 County mapping and repo coverage

The repo still uses the 2020-2023 county labels. Since 2024-01-01, Viken, Vestfold og Telemark, and Troms og Finnmark were split again. Official mapping is documented by the government and Kartverket:

- https://www.regjeringen.no/no/tema/kommuner-og-regioner/kommunestruktur/fylkesinndelingen-fra-2024/id2922222/
- https://www.kartverket.no/til-lands/kommunereform/regionsendringer-2024

Search both old and current names.

| Repo division | Current/admin names to search | Required coverage strategy |
|---|---|---|
| Oslo | Oslo | Oslo PBE, Nkom, Bulk OS-IX, STACK/DigiPlex legacy, GlobalConnect/Telia/Telenor colo. |
| Rogaland | Rogaland | Stavanger/Rennesoy, Sandnes, Time, Tysvaer, Karmoy, Suldal, Haugaland Naeringspark/Gismarvik. |
| More and Romsdal | More og Romsdal | Kristiansund, Averoy, Alesund, Orsta/Hovdebygda; NEAS, Tafjord, Tussa, Magnora Scale Averoya. |
| Northland | Nordland | Glomfjord/Meloy, Ballangen/Narvik, Stokmarknes/Hadsel; Nscale, Trollfjord IKT, dormant Kolos, Statnett northern constraints. |
| Svalbard | Svalbard | Treat as separate Arctic territory; search Longyearbyen/Svalbard ground-station and local energy limits; do not infer commercial DCs. |
| Jan Mayen | Jan Mayen | Treat as separate Arctic territory; expect no commercial DCs; document negative search. |
| Viken | Viken; Akershus; Buskerud; Ostfold | Enebakk, Lillestrom/Fetsund, Lorenskog, Nittedal, Ullensaker, Ringerike/Honefoss, Halden, Fredrikstad, Moss. |
| Inland | Innlandet | Hamar, Loten, Elverum; Green Mountain OSL-Hamar, Eidsiva, possible Arcem/market leads. |
| Vestfold and Telemark | Vestfold og Telemark; Vestfold; Telemark | Tinn/Rjukan, Skien/Gromstul, Porsgrunn/Heroya, Tordal/Drangedal; Green Mountain, WS Computing/Google, PolarDC. |
| Agder | Agder | Kristiansand/Vennesla; Bulk N01 campus, Tonstad/Sirdal market leads, former battery/fuel sites repurposed as DC leads. |
| Westland | Vestland | Stad/Eid/Nordfjordeid/Lefdal, Bergen, Husnes/Kvinnherad; Lefdal Mine, Datafjellet, Eviny, Arcem leads. |
| Trondelag | Trondelag | Trondheim, Tydal, Namsskogan, Roros, Steinkjer; Tydal Data Center/Bitdeer, Exanorth, NTE, Ren Roros, GlobalConnect. |
| Troms and Finnmark | Troms og Finnmark; Troms; Finnmark | Tromso, Harstad, Bardu, Alta, Hammerfest, Kirkenes; expect few public commercial DCs; use Nkom names and Statnett northern-grid context. |

### 0.3 Legal/process vocabulary

Planning/building lifecycle:

```text
planinitiativ
oppstartsmote
planprogram
planforslag
horing
offentlig ettersyn
reguleringsplan
detaljregulering
rammetillatelse
igangsettingstillatelse
midlertidig brukstillatelse
ferdigattest
postjournal
saksinnsyn
```

Environmental lifecycle:

```text
soknad om tillatelse etter forurensningsloven
utslippstillatelse
forurensende virksomhet
nodstromsaggregat
dieselaggregat
testkjoring
stoy
overvann
prosessavlopsvann
kjolevann
```

Grid/power lifecycle:

```text
nettilknytning
tilknytningsavtale
reservert effekt
tilknyttet effekt
anleggskonsesjon
omradekonsesjon
transformatorstasjon
132 kV
420 kV
MVA
MW
TWh
```

Count a facility as high-confidence only after at least one Grade A facility source exists: Nkom commercial registration tied to the operator, municipal permit, environmental permit, NVE/Statnett grid record, or the operator's own facility page. Land purchase, political support, grid-capacity reservation, cloud-region naming, and directory entries are leads until cross-checked.

## 1. Official source backbone

### 1.1 Nkom and national regulation

Use Nkom first for the commercial-operator universe:

```text
site:nkom.no/datasenter "Registrerte datasenteroperatorer og datasentre"
site:nkom.no/datasenter "datasenterforskriften"
"{operator}" site:nkom.no/datasenter
```

Extract: operator legal name, organization number, crypto-mining flag, page update date, CSV date if available, and whether the target appears to be commercial or business-internal.

### 1.2 Municipal planning and building records

Municipalities are the primary planning/building authorities under the Planning and Building Act. Use municipal `saksinnsyn`, `planinnsyn`, `postjournal`, `byggesak`, and PDF archives.

Core official portals:

- Oslo PBE Saksinnsyn: https://innsyn.pbe.oslo.kommune.no/saksinnsyn/main.asp
- Oslo innsyn landing: https://www.oslo.kommune.no/innsyn/
- National building authority DiBK: https://www.dibk.no/
- Altinn building-application process: https://info.altinn.no/skjemaoversikt/kommunene/byggesak-soknad-etter-plan-og-bygningsloven/
- Kartverket geodata/address/parcels: https://www.kartverket.no/
- eInnsyn for public journals where municipalities/agencies publish there: https://einnsyn.no/

Municipal query templates:

```text
site:{kommune}.kommune.no datasenter
site:{kommune}.kommune.no serverhall
site:{kommune}.kommune.no "datalagringssenter"
site:{kommune}.kommune.no "reguleringsplan" datasenter
site:{kommune}.kommune.no "rammetillatelse" datasenter
site:{kommune}.kommune.no "igangsettingstillatelse" datasenter
site:{kommune}.kommune.no "ferdigattest" datasenter
site:{kommune}.kommune.no "postjournal" "{operator}"
site:{kommune}.kommune.no "{gbnr}" datasenter
```

Extract: municipality, old repo division, current county, plan/case ID, applicant, property (`gbnr`), address, plan title, land area, building count, gross floor area, power/cooling text, emergency generators, decision dates, permit type, appeal status, and PDF URLs.

### 1.3 Environment: Statsforvalteren and Miljodirektoratet

Environmental permits are often the best official proof for operating or near-operating data centers, especially because backup generators, noise, stormwater, and cooling can trigger pollution-law permits.

Primary URLs:

- Statsforvalteren home/search: https://www.statsforvalteren.no/
- Miljodirektoratet home: https://www.miljodirektoratet.no/
- Miljodirektoratet consultations: https://www.miljodirektoratet.no/hoeringer/
- Norske utslipp permit database: https://www.norskeutslipp.no/
- Forurensningsloven: https://lovdata.no/lov/1981-03-13-6

Verified examples to model extraction:

- WS Computing/Google Gromstul, Skien: Statsforvalteren says Datasenter 1 received a pollution permit on 2025-08-25, and Datasenter 2 had a 2026 hearing: https://www.statsforvalteren.no/vestfold-og-telemark/miljo-og-klima/forurensning/tillatelse-til-ws-computing-as-for-datalagringssenter-pa-gromstul-i-skien/ and https://www.statsforvalteren.no/vestfold-og-telemark/horinger/2026/06/soknad-om-tillatelse-etter-forurensningsloven---ws-computing-as---datasenter-2-gromstul/
- Green Mountain Rennesoy permit PDF via Norske utslipp: https://www.norskeutslipp.no/WebHandlers/PDFDocumentHandler.ashx?aar=0&companyID=156934&documentID=938081&documentType=T&epslanguage=en

Search templates:

```text
site:statsforvalteren.no datasenter "{operator}"
site:statsforvalteren.no datasenter "{kommune}"
site:statsforvalteren.no "datalagringssenter" "{kommune}"
site:miljodirektoratet.no/hoeringer datasenter
site:norskeutslipp.no "{operator}" datasenter
"{operator}" "{kommune}" "tillatelse etter forurensningsloven"
"{operator}" "{kommune}" "nødstrømsaggregat"
```

### 1.4 Energy/grid: NVE, RME, Statnett, grid companies

Primary URLs:

- NVE concession portal/landing: https://www.nve.no/konsesjon
- NVE English licensing context: https://www.nve.no/licensing/
- RME within NVE: https://www.nve.no/reguleringsmyndigheten/
- Statnett: https://www.statnett.no/
- Statnett news/industry pages: https://www.statnett.no/en/about-statnett/news-and-press-releases/ and https://www.statnett.no/en/for-stakeholders-in-the-power-industry/news-for-the-power-industry/

Use grid sources to prove enabling infrastructure, not data-center operation. Keep these fields separate:

- `reservert effekt`: capacity reservation/queue position
- `tilknyttet effekt`: connection capacity
- `IT load`: operator/customer IT capacity
- `gross power` or `site power`: marketed or engineering site capacity

Northern Norway note: credible 2026 reporting says Statnett temporarily stopped new reservations for projects above 5 MW north of Svartisen in Nordland. Treat this as a gating lead unless an official Statnett page/document is captured for the specific date.

Search templates:

```text
site:nve.no datasenter
site:nve.no "anleggskonsesjon" datasenter
site:nve.no "{operator}" "{kommune}"
site:nve.no "{project}" "transformatorstasjon"
site:statnett.no datasenter
site:statnett.no "nettutviklingsplan" datasenter
site:statnett.no "Svartisen" "5 MW"
"{kommune}" datasenter "132 kV"
"{kommune}" datasenter "420 kV"
"{operator}" "{kommune}" "nettilknytning"
```

### 1.5 Government strategy and security

Primary URLs:

- 2025 data-centre strategy, English landing: https://www.regjeringen.no/en/documents/the-data-centre-industry-a-sustainable-industry-of-the-future-for-the-digital-norway/id3112356/
- 2025 data-centre strategy, Norwegian landing: https://www.regjeringen.no/no/dokumenter/datasenternaringa/id3112356/
- Older 2021 strategy: https://www.regjeringen.no/no/dokumenter/norske-datasenter/id2867155/
- NSM: https://nsm.no/
- Nkom Data Act page: https://nkom.no/internett/internettbaserte-plattformer/data-act-da

Use these for policy context, not facility enumeration. They are Grade A for rules and objectives, not for site counts unless they cite a specific register.

## 2. Query patterns

### 2.1 Norwegian and English discovery

```text
datasenter
datasentre
datalagringssenter
serverhall
datahall
kolokasjon
samlokalisering
skytjenester
hyperscale
AI-datasenter
KI-datasenter
kraftkrevende næring
elintensivt
overskuddsvarme
fjernvarme
reservekraft
nødstrøm
dieselaggregat
kjøling
frikjøling
væskekjøling
```

```text
"Norway" "data center" "building permit"
"Norway" "data center" "environmental permit"
"Norway" "data center" "grid connection"
"Norge" datasenter "rammetillatelse"
"Norge" datasenter "utslippstillatelse"
"{operator}" "{site}" "{kommune}"
"{operator}" "{site}" "gbnr"
```

### 2.2 Known official pivots

```text
"WS Computing" Gromstul Skien datasenter
"Google" Gromstul Skien datasenter
"Green Mountain" Enebakk "rammetillatelse"
"Green Mountain" Heggvin Hamar Løten
"Green Mountain" Rennesøy "utslippstillatelse"
"Green Mountain" Rjukan Tinn datasenter
"Bulk Data Centers" OS-IX Oslo
"Bulk Data Centers" N01 Kristiansand Vennesla
"Nscale" Glomfjord Meløy datasenter
"Tydal Data Center" Tydal datasenter
"Bitdeer" Tydal "anleggskonsesjon"
"Lefdal Mine" Stad datasenter
"Datafjellet" Bergen datasenter
"Magnora Scale Averøya" datasenter
"atNorth" Haugaland Gismarvik Tysvær datasenter
"Storespeed" Halden datasenter
```

## 3. Per-division official enumeration strategy

### Oslo

Primary portals: Oslo PBE Saksinnsyn and Oslo innsyn. Search exact addresses and legacy operator names.

Targets:

- Bulk OS-IX, Hans Moller Gasmanns vei 9. Operator page confirms Oslo Internet Exchange; verify any expansions in PBE and environmental records. URL: https://bulkinfrastructure.com/data-centers/locations/os-ix
- STACK/DigiPlex Ulven and other Oslo SPVs in Nkom (`SI OSL 01 AS`, `SI OSL 02 AS`, `SI OSL 03.1 AS`, `SI OSL 03.2 AS`, `SI OSL 04 AS`). Search `SI OSL`, `DigiPlex`, `STACK`, `Ulven`, and addresses in PBE.
- GlobalConnect, Telia, Telenor, Blix, Orange Business, and Atea appear in the Nkom universe or industry pages; treat facility addresses as unconfirmed until municipal/operator pages agree.

### Rogaland

Primary municipalities: Stavanger, Sandnes, Time, Tysvaer, Karmoy, Suldal.

Targets:

- Green Mountain SVG-Rennesoy in Stavanger/former Rennesoy. Operator page gives 25 MW and 22,600 m2; Norske utslipp/Statsforvalteren provides permit evidence for emissions/noise/cooling. URLs: https://greenmountain.no/data-center/svg-rennesoy/ and https://www.norskeutslipp.no/WebHandlers/PDFDocumentHandler.ashx?aar=0&companyID=156934&documentID=938081&documentType=T&epslanguage=en
- atNorth NOR01 Haugaland at Haugaland Business Park, Gismarvik/Tysvaer. Operator page confirms planned 36 ha, 120 MW initial phases, 350 MW site power. Confirm land, zoning, generator/cooling permits, and grid in Tysvaer/NVE/Statnett. URL: https://www.atnorth.com/nordic-data-centers/norway-data-centers/haugaland-nor01/
- Green Mountain Sandnes/Vagle, Time/Undheim, and Haugaland options are development leads unless municipal permits are found.
- Asp Data Center AS appears in Nkom; search Suldal/Rogaland records before treating it as a facility.
- Microsoft Azure Norway West is a region anchor, not a building proof. Search Sandnes/Stavanger municipal records for Microsoft/contractor/SPV names.

### More and Romsdal

Primary municipalities: Kristiansund, Averoy, Alesund, Orsta, Volda, Molde.

Targets:

- NEAS IT AS appears in Nkom; NEAS markets local data centers in Kristiansund and Oppdal. Verify facility addresses and any permits in Kristiansund/Oppdal records. URL lead: https://neas.no/bedrift/it/neas-datasenter/
- Tussa IKT AS appears in Nkom; Tussa markets data-center services on Sunnmore/Orsta. Verify in Orsta/Hovdebygda building records. URL: https://www.tussa.no/bedrift/it/tussa-datasenter
- Tafjord Connect AS appears in Nkom and markets colocation; verify Alesund records. URL: https://www.tafjord.no/bedrift/fiber/produkt-tjenester/colocation/
- Magnora Scale Averoya is a 100 MW development lead from Magnora; not operational until permits/construction evidence exist. URL: https://magnoraasa.com/company-portfolio/magnora-data-center-norway/

### Northland

Search both `Nordland` and repo spelling `Northland`. Primary municipalities: Meloy/Glomfjord, Narvik/Ballangen, Hadsel/Stokmarknes, Bodo.

Targets:

- Nscale Glomfjord in Meloy is a confirmed operator lead: Nscale states 30 MW operational capacity expandable to 60 MW. Nkom lists `NSCALE DRIFT AS`. Verify in Meloy, NVE, and Statsforvalteren. URL: https://www.nscale.com/product/glomfjord
- Trollfjord IKT Senter AS appears in Nkom and Bronnoysund/Proff sources describe data-center/hosting purpose in Stokmarknes; verify local records.
- Kolos Ballangen/Narvik is dormant unless new official evidence appears.
- Apply Statnett northern capacity constraints when assessing new >5 MW projects north of Svartisen.

### Svalbard

No verified commercial colocation/hyperscale data-center facility found in current primary sources. Search Longyearbyen Lokalstyre, Sysselmesteren, Svalbard Energi, Statsbygg, and satellite/ground-station terms separately. Do not confuse satellite ground stations, research IT, or telecom rooms with commercial data centers.

Queries:

```text
site:lokalstyre.no datasenter
site:sysselmesteren.no datasenter
Svalbard datasenter serverhall Longyearbyen
Svalbard ground station data center
```

### Jan Mayen

No verified commercial data centers. Treat Jan Mayen as a negative-control division; search meteorological, defense, and telecom infrastructure only to avoid false positives.

Queries:

```text
"Jan Mayen" datasenter
"Jan Mayen" serverhall
"Jan Mayen" data center
```

### Viken: Akershus, Buskerud, Ostfold

Search the old Viken label and current counties.

Akershus targets:

- Green Mountain OSL-Enebakk. Operator page confirms 75,000 m2, 93 MW line-of-sight capacity, three completed buildings by 2024. Verify municipal permits in Enebakk. URL: https://greenmountain.no/data-center/osl-enebakk/
- STACK/DigiPlex Fetsund/Lillestrom (`SI OSL 03.*` in Nkom). Search `Heiaveien 9`, `Fetsund`, `DigiPlex`, `STACK`, `SI OSL`.
- Search Lorenskog, Nittedal, Ullensaker, Lillestrom for operator/SPV names in Nkom.

Buskerud targets:

- Ringerike/Honefoss/Treklyngen are development/land leads unless Ringerike municipal permits are found.
- Search `Treklyngen`, `DigiPlex`, `STACK`, `Green Mountain`, `datasenter`, and `nettilknytning`.

Ostfold targets:

- Storespeed Halden/Fredrikstad. Nkom lists Storespeed AS; confirm Halden operating details via operator page/municipal permits and Magnora acquisition filings where needed.
- Search Moss for new Arcem/Polar/Magnora leads, but keep C/B until official permits exist.

### Inland

Primary municipalities: Hamar, Loten, Elverum, Ringsaker.

Targets:

- Green Mountain OSL-Hamar at Heggvin Naeringspark/Hamar-Loten. Operator page confirms Norway's largest data-center campus, TikTok tenant, 18,000 m2 existing IT space, 12,000 m2 planned IT space, 150 MW site capacity, first three buildings complete/in operation. Verify municipal and NVE details for transformer/grid cases. URL: https://greenmountain.no/data-center/osl-hamar/
- Nkom lists Green Mountain Innlandet AS and Eidsiva Digital AS; search both in Hamar/Loten records.
- Elverum appears in 2026 market/developer leads; keep as watch-list until municipal records exist.

### Vestfold and Telemark: Vestfold, Telemark

Primary municipalities: Tinn, Skien, Porsgrunn, Drangedal/Tordal, Larvik, Sandefjord, Tonsberg.

Targets:

- Green Mountain TEL-Rjukan in Tinn. Operator page confirms 29,000 m2 and 50 MW site capacity; verify any building/environment changes locally. URL: https://greenmountain.no/data-center/tel-rjukan/
- WS Computing/Google Gromstul in Skien. Skien municipality says Google announced a 600 million euro data-center investment in February 2024; Statsforvalteren granted Datasenter 1 pollution permit in 2025 and held a Datasenter 2 hearing in 2026. URLs: https://www.skien.kommune.no/by-og-naeringsutvikling/google-etablering-i-skien-kommune/tidslinje-hva-har-skjedd-fram-til-naa/ and Statsforvalteren URLs in section 1.3.
- PolarDC DRA/HER01 and Tordal/Drangedal leads require official municipal/NVE confirmation; directory/vendor claims alone are not enough.

### Agder

Primary municipalities: Kristiansand, Vennesla, Sirdal/Tonstad.

Targets:

- Bulk N01 is the main official operator lead. Bulk describes a 3 km2 zoned Norwegian campus in Southern Norway/Agder and up to 1 GW power next to a major renewable substation. Confirm exact municipal coverage and permits through Kristiansand/Vennesla/Sirdal records and NVE/Statnett. URL: https://bulkinfrastructure.com/data-centers/locations/n01
- Bulk OS-IX is Oslo, not Agder; do not double-count.
- Tonstad/Sirdal and former battery/e-fuel sites are watch-list leads until official permit transfer/rezoning records exist.

### Westland

Search `Vestland`, `Sogn og Fjordane`, `Hordaland`, `Stad`, `Eid`, `Nordfjordeid`, `Maloy`, `Bergen`, `Kvinnherad`, `Husnes`.

Targets:

- Lefdal Mine Datacenter. Operator page confirms underground mountain-hall facility; Business Norway and Sigma2/HPE material confirm national HPC/AI use. URL: https://www.lefdalmine.com/
- Sigma2 national data-centre/supercomputer anchors: https://www.sigma2.no/our-data-centre and https://www.sigma2.no/procurement-project-hpc-a2
- Datafjellet in Bergen is a Nkom-listed commercial operator lead; verify through Bergen records. URL: https://www.datafjellet.no/
- Eviny Fiber AS appears in Nkom; treat as operator lead and verify facility specifics.
- Arcem/Bergen/Husnes leads from 2026 press are watch-list until municipal records appear.

### Trondelag

Primary municipalities: Trondheim, Tydal, Namsskogan, Roros, Steinkjer, Levanger.

Targets:

- Tydal Data Center AS appears in Nkom. Industry sources tie Tydal/Bitdeer/DCI to a large AI/compute development; verify in Tydal municipal, NVE, and Statsforvalteren records before accepting 180 MW claims.
- Exanorth AS appears in Nkom as crypto-mining; press ties it to Namsskogan/Tunnsjodalen. Verify with municipal and grid records.
- GlobalConnect Trondheim appears in data-center directories and GlobalConnect's Nordic colocation offering; verify address/permit through Trondheim records and Nkom operator row.
- NTE Telekom AS and Ren Roros Digital AS appear in Nkom. Search `Moholt Datasenter`, `Steinkjer`, `Roros`, and operator names for local public-sector data-center facilities.

### Troms and Finnmark

Primary municipalities: Tromso, Harstad, Bardu, Senja, Alta, Hammerfest, Sor-Varanger/Kirkenes.

Current status: no large, named commercial data-center campus verified from the reviewed primary sources. Nkom may include operators with northern presence, but the public table does not publish facility locations for every operator. Search municipal records and NVE/Statnett, and record negative results explicitly.

Context: grid constraints north of Svartisen can block or delay new >5 MW leads; do not mark planned northern projects as feasible without current Statnett/NVE evidence.

## 4. Extraction and grading rules

Minimum fields per candidate:

```text
facility_name
operator_legal_name
org_number
repo_division
current_county
municipality
address_or_gbnr
source_grade
source_url
source_date
status: proposed | permitted | under_construction | operational | dormant | withdrawn | unknown
power_mw_type: IT_load | site_power | grid_reserved | grid_connected | generator_thermal
power_mw_value
building_area_m2
environmental_permit
municipal_case_id
grid_case_id
notes
```

Grading:

- A: current Nkom/operator/municipal/environment/grid source directly supports the field.
- B: named and dated trade/financial/construction source supports the field, but official permit/source not yet found.
- C: directory, social, unsourced market report, or inference.

Do not upgrade a capacity number just because the facility is real. Example: an operator page may be A for existence/location and B for future full-build capacity if no permit/grid record supports the final MW.
