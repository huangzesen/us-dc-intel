# LV Explorer Official - Latvia Datacenter Enumeration via BIS, Municipal, Energy, Regulator, Cloud, and Operator Sources

Date: 2026-08-12. Scope: Latvia (LV), 43 municipality/state-city divisions from `world-manifest.jsonl`. Focus angle: official/regulatory/primary-source enumeration for datacenter facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Structural facts that shape Latvia enumeration

- Latvia has no single public "data center registry". Build the census by joining **BIS construction cases**, municipal construction-board/council/environment pages, **AST/Sadales tikls electricity evidence**, SPRK regulatory context, official cloud-region pages, and operator facility pages.
- Latvia's practical permit source is the national **Building Information System (Buvniecibas informacijas sistema, BIS)** at https://bis.gov.lv/en. BIS exposes public sections for current/planned construction and maps, including https://bis.gov.lv/bisp/en/planned_constructions and https://bis.gov.lv/bisp/en/planned_constructions/bismap. Grade **A** for construction-intention and building-process records; the map UI is JavaScript-heavy and some detail may require Latvija.lv authentication.
- BIS public-information guidance says public construction-intention content is available on the public BIS portal and that operation-case basic data/documents are also publicly accessible for authorized users: https://bis.gov.lv/en/public-information. Grade **A** for process/source scope.
- The State Construction Control Bureau (BVKB) administers BIS; BVKB describes BIS as the electronic environment for circulation of construction information: https://www.bvkb.gov.lv/en/administration-building-information-system-0. Grade **A** for system ownership.
- Municipal construction boards (`buvvalde`), municipal BIP/publication pages, council minutes, and procurement pages are essential. Search the municipality site even when BIS returns little, because Latvian municipal pages often publish road servitudes, electricity-cable projects, heating interconnection, land-lease, and construction-board decisions.
- Latvian datacenter filings may not use English "data center". Search both Latvian and English: `datu centrs`, `datu centra`, `datucentrs`, `datu apstrades centrs`, `serveru telpa`, `serveru ferma`, `kolokacija`, `kritiska IT infrastruktura`, `telekomunikaciju mezgls`, `rezerves barosana`, `dizelgeneratori`, `UPS`, `transformatoru apakstacija`, `elektroapgade`, `20 kV`, `110 kV`, `siltuma atguve`, `atlikumsiltums`.
- Most confirmed commercial capacity is in **Riga** and the Riga metro, especially **Salaspils** and **Kekavas novads**. Strong non-Riga development leads are **Liepaja**, **Jekabpils novads**, **Ventspils/Kurzeme**, and LVRTC regional nodes.
- Count facility evidence conservatively. Operator pages and official municipal releases can prove existence and status. BIS/building decisions prove construction process. Power-connection evidence is a lead unless tied to a named building/project.

Lifecycle vocabulary:

`teritorijas planojums / lokaplanojums / detaplanojums` < `buvniecibas iecere` < `buvprojekts minimala sastava` < `buvatlauja` < `buvdarbi / buvdarbu uzsaksana` < `nodosana ekspluatacija` < `sviniga atklasana / pirmie klienti`

Only treat `buvatlauja`, `buvdarbu uzsaksana`, `nodosana ekspluatacija`, or operator-confirmed launch as strong facility evidence. Treat zoning, grid-capacity, and real-estate announcements as planned/pre-development until cross-checked.

---

## 1. Latvian and English query patterns

### 1.1 Core Latvian terms

```text
datu centrs
datu centra
datu centri
datucentrs
datu apstrades centrs
serveru telpa
serveru ferma
kolokacija
makonpakalpojumi
kritiska IT infrastruktura
telekomunikaciju mezgls
interneta apmainas punkts
dizelgeneratori
rezerves barosana
UPS
transformatoru apakstacija
apakstacija
elektroapgade
20kV OR "20 kV"
110kV OR "110 kV"
siltuma atguve
atlikumsiltums
centralizeta siltumapgade
nodosana ekspluatacija
buvatlauja
buvniecibas iecere
buvprojekts
buvvalde
ietekmes uz vidi novertejums
sakotnejais ietekmes uz vidi izvertejums
```

### 1.2 Permit / municipal queries

Substitute `{municipality}`, `{city}`, `{operator}`, `{legal_entity}`, `{address}`, `{parcel}`.

```text
site:bis.gov.lv "datu centrs" "{municipality}"
site:bis.gov.lv "datu centra" "{city}"
site:bis.gov.lv "serveru" "buvatlauja"
site:bis.gov.lv "{operator}" "buvniecibas"
"{municipality}" "datu centrs" "buvatlauja"
"{municipality}" "datu centra" "nodosana ekspluatacija"
"{municipality}" "datu centrs" "buvvalde"
"{city}" "datu centrs" "buvniecibas iecere"
"{address}" "datu centrs"
"{operator}" "{municipality}" "Krasta iela" OR "Cuibes iela" OR "Jana Asara iela"
site:{municipality-domain} "datu centrs"
site:{municipality-domain} "datu centra" "elektroapgade"
site:{municipality-domain} "datu centram" "20kV"
site:{municipality-domain} "datu centrs" "siltumapgade"
filetype:pdf "datu centrs" "buvatlauja"
filetype:pdf "datu centram" "elektroapgade"
```

### 1.3 Energy / environment queries

```text
site:ast.lv "datu centrs"
site:ast.lv "data centre" Latvia "110 kV"
site:ast.lv "connections to the transmission grid" "datu centrs"
site:sadalestikls.lv "datu centrs"
site:sprk.gov.lv "datu centrs"
site:sprk.gov.lv "elektroenergija" "Augstsprieguma tikls" "Sadales tikls"
site:vpvb.gov.lv "datu centrs"
site:videscentrs.lvgmc.lv "datu centrs"
"{operator}" "{municipality}" "110 kV"
"{operator}" "{municipality}" "20 kV"
"{operator}" "{municipality}" "atlikumsiltums"
"{operator}" "{municipality}" "Salaspils Siltums"
"datu centrs" "dizelgeneratori" "ietekmes uz vidi"
```

### 1.4 English patterns

```text
"Latvia" "data center" "building permit"
"Latvia" "data centre" "commissioned"
"Riga" "data center" "BIS" OR "building permit"
"Salaspils" "DC7" "data center" "building permit"
"Latvia" "data center" "110 kV"
"Latvia" "data center" "grid connection"
"Latvia" "data center" "waste heat"
"Liepaja" "data centre" "120 MW"
"Jekabpils Old Airport" "data centre" "114 MW"
"Riga" "Delska" "10 MW" "data center"
"Tet" "DC7" "Salaspils" "data center"
"LVRTC" "Positron" "data center"
```

---

## 2. Official / regulatory source backbone

### 2.1 Construction and operation: BIS / BVKB

Primary sources:

- BIS portal: https://bis.gov.lv/en. Grade **A**.
- BIS planned/current construction list: https://bis.gov.lv/bisp/en/planned_constructions. Grade **A**.
- BIS planned/current construction map: https://bis.gov.lv/bisp/en/planned_constructions/bismap. Grade **A**; JS UI, use manually or with browser automation.
- BIS public-information page: https://bis.gov.lv/en/public-information. Grade **A** for public availability and public/authorized access boundaries.
- BVKB BIS administration page: https://www.bvkb.gov.lv/en/administration-building-information-system-0. Grade **A** for system authority.
- Ministry of Economics page on the Construction Information System: https://www.em.gov.lv/en/construction-information-system-0. Grade **A** process context.

Fields to extract from BIS/municipal construction records:

- construction case number and construction authority (`buvvalde`);
- project name/function, building group/category, construction stage;
- applicant/investor legal entity and representative;
- address, cadastral designation, parcel, land use;
- decision type/date: construction intention, design conditions, building permit, construction start, commissioning/operation;
- associated external works: 20 kV/110 kV cable, transformer/substation, optical duct, cooling/heating, generators/fuel storage.

Do not require a record to say `datu centrs`. Large Latvian projects can appear as telecom/IT, industrial, engineering-network, energy-supply, or office/technical buildings. Use operator legal names and address pivots.

### 2.2 Municipal planning, BIP, and council records

Municipal pages are Grade **A** where they publish council decisions, public-consultation material, construction-board notices, or utility-route approvals.

Use these source types:

- municipal official site and BIP/public documents;
- `buvvalde` decisions and agendas;
- council agendas/minutes (`domes sede`, `lemumi`);
- territorial planning (`teritorijas planojums`, `lokaplanojums`, `detaplanojums`);
- public procurements and land/servitude decisions;
- road, fiber, 20 kV cable, water/cooling, and district-heating connection decisions.

High-yield example: Salaspils council PDF search found DC7 utility evidence for Krasta iela 2/1, including optical connection from the Salaspils substation and external 20 kV electricity supply: https://www.salaspils.lv/sites/default/files/Domes%20s%C4%93des/L%C4%93mumi/2025/public-JS-7-11-09-2025.pdf. Grade **A** for municipal utility-routing facts.

### 2.3 Electricity: SPRK, AST, Sadales tikls

Primary sources:

- SPRK electricity sector page: https://www.sprk.gov.lv/en/electricity-0. Grade **A**. It identifies Latvia's single transmission system operator as JSC `Augstsprieguma tikls` and distribution as 8 DSOs, with JSC `Sadales tikls` supplying 99% of power users.
- SPRK homepage/regulator: https://www.sprk.gov.lv/lv and English section https://www.sprk.gov.lv/en. Grade **A** regulatory context for electricity/electronic communications; not a datacenter registry.
- SPRK registration/electronic communications pages, e.g. https://www.sprk.gov.lv/lv/registresana-1 and https://www.sprk.gov.lv/lv/elektronisko-sakaru-nozare-0. Grade **A** for regulated-company context.
- AST front page: https://ast.lv/en. Grade **A** for TSO identity and high-voltage network context.
- AST transmission-grid connection page: https://ast.lv/en/content/connections-transmission-grid. Grade **A** for transmission-connection process.
- AST development plan: https://ast.lv/en/content/power-transmission-system-development-plan. Grade **A** grid geography/planning context.
- Sadales tikls: https://sadalestikls.lv/. Grade **A** for distribution-grid context and connection process, especially for sub-110 kV loads.

Use energy evidence to identify:

- direct 110 kV transmission connection needs;
- 20 kV distribution connection or external electricity-supply construction;
- substation names: Salaspils, Riga CHP/HPP area, Liepaja industrial/SEZ nodes, Jekabpils 110 kV nodes, Kurzeme Ring/Broceni/Ventspils context;
- requested/permitted load where public;
- waste-heat or cooling interconnection with district heating (`Salaspils Siltums`, municipal utilities).

Important caution: Latvia power sources are better for infrastructure context than public large-load lists. Grid connection evidence is **not** proof of an operating datacenter unless tied to BIS/municipal/operator records.

### 2.4 Environment / EIA / operational impacts

Primary source surfaces:

- State Environmental Bureau / VPVB: https://www.vpvb.gov.lv/ and historic EIA materials on `vpvb.gov.lv` / `old1.vpvb.gov.lv`. Grade **A**.
- State Environmental Service: https://www.vvd.gov.lv/. Grade **A** for permits/controls where relevant.
- Latvian Environment, Geology and Meteorology Centre: https://videscentrs.lvgmc.lv/. Grade **A** for environmental data context.
- Municipal public-consultation and environmental-decision pages. Grade **A**.

Search for datacenter clues in environmental material:

- backup generators and fuel storage;
- battery/UPS rooms;
- cooling towers/chillers and water demand;
- noise from chillers/generators;
- heat reuse/district-heating interconnection;
- construction traffic and utility corridors.

Most Latvian data centers are unlikely to trigger a full EIA under a direct "data center" category. Environment records are more useful for large generator/fuel/cooling infrastructure or industrial-site conversion.

### 2.5 Official cloud-region checks

Use cloud pages to avoid inventing hyperscale regions in Latvia.

| Provider | Official source | Latvia signal | Enumeration use |
|---|---|---|---|
| AWS | Global Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No public AWS Region or Local Zone in Riga/Latvia found in official lists as of 2026-08-12. | Grade **A** for absence from official region/local-zone list; do not infer AWS facilities from enterprise usage. |
| Microsoft Azure | Azure global infrastructure / datacenter regions: https://azure.microsoft.com/en-us/explore/global-infrastructure/ | No public Azure Latvia region found as of 2026-08-12. | Grade **A** for official region list; Latvia may be served from nearby EU/Nordic regions. |
| Google Cloud | Locations: https://cloud.google.com/about/locations ; Compute regions/zones docs: https://cloud.google.com/compute/docs/regions-zones | No public Google Cloud Latvia region found as of 2026-08-12. | Grade **A** for official region list; do not count Google offices/partners as DCs. |
| Oracle Cloud | Public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ | No public OCI Latvia commercial region found as of 2026-08-12. | Grade **A** for region list; check Stockholm/Frankfurt/Warsaw/Nordics for service context only. |

Official cloud regions prove logical service geography, not exact building locations. In Latvia the major hyperscale clues are currently operator/developer/energy leads, not public cloud-region pages.

---

## 3. Primary-source facility seeds to verify

Use these as pivots for official/municipal/BIS searches. Operator-owned pages are **A** for advertised facility existence/status and **B** for capacity unless backed by formal certificates/spec sheets.

| Operator / project | Primary source | Current signal | Official enumeration use |
|---|---|---|---|
| Delska / DEAC EU North Riga LV DC1 | https://delska.com/data-centers/eu-north-riga-lv-dc1/ and portfolio https://delska.com/ | 10 MW, 1,000 racks, Riga, AI/HPC-ready; Delska says launched/ready. | Search BIS/Riga for `Delska`, `DEAC`, `Cuibes iela 17`, `datu centrs`, substation/cable works. |
| Delska / DEAC Riga LV DC2 and LV DC3 | https://delska.com/ and https://delska.com/data-centers/ | Portfolio lists LV DC2, LV DC3; LV DC3 is underground/secure. | Pivot on `Cuibes iela 17`, `Jana Asara iela 24`, `DEAC`, `Delska`. |
| Tet data centers in Riga | https://tetcloud.com/data-centers | Dattum, Brivibas, Kleistu, Perses, Atlasa, Tet DC 6; page lists racks, MW for many sites. | Pivot on Tet facility names and addresses; confirm older sites with BIS only if status/capacity is uncertain. |
| Tet DC7, Salaspils | Tet official news: https://www.tet.lv/par-mums/jaunumi/tet-datu-centra-dc7-pirma-karta-nodota-ekspluatacija-novembri-planota-sviniga-atklasana ; Salaspils official: https://salaspils.lv/lv/node/3751 and https://salaspils.lv/lv/node/3972 | First phase completed/put into operation; EUR30m+ project; waste-heat reuse with Salaspils Siltums; full buildout by 2028 in public reports. | Search Salaspils site/BIS for `DC7`, `Krasta iela 2/1`, `Tet`, `20kV`, `optiskais pieslegums`, `Salaspils Siltums`. |
| LVRTC data centers / Baltic Data Hub | https://www.lvrtc.lv/en/baltic-data-hub/data-centers/ | LVRTC says two Riga sites plus one regional hub, integrated with nationwide colocation facilities. | Operator page is primary but broad; use PeeringDB/municipal docs for exact regional sites, mark regional nodes carefully. |
| LVRTC Positron | https://www.lvrtc.lv/en/news/datu-centri/lvrtc-most-physically-secure-data-center-baltics/ and https://www.lvrtc.lv/projekti/datu-centrs-pozitrons/ | Official construction announcement for secure regional/Kurzeme data center planned to commission by early 2027. | Search `Pozitrons`, `LVRTC`, `Kurzeme`, construction-board approval, exact municipality only if public. |
| Northern Energy Liepaja Data Centre | https://northernenergy.eu/projects | Developer states 120 MW operational capacity by 2029 in Liepaja SEZ, with 110 kV/33 kV connectivity. | Grade **A** for developer claim; verify with Liepaja SEZ/municipality/BIS/AST before counting as permitted/construction. |
| Northern Energy Jekabpils Old Airport | https://northernenergy.eu/projects | Developer states 114 MW available today, scalable to 400 MW by 2030, 110 kV grid connections. | Grade **A** for developer claim; verify with Jekabpils municipality, airport-site land records, BIS, AST/Sadales tikls. |
| C.T.Co / SIA Fraternitas, Valdlauci | Citrus Solutions project page: https://www.citrus.lv/en/projects/data-centers/constrution-works-of-the-data-centre-of-c-t-co/ | Completed 2015 construction works, 20 racks, Meistaru Street 33, Valdlauci. | Grade **B** contractor lead; verify with Kekavas novads/BIS/address if included. |

---

## 4. Division-by-division official workflow

Use the manifest divisions as municipalities/state cities. For each division:

1. Run a local-language web sweep:

```text
"{division}" "datu centrs"
"{division}" "datu centra" "buvatlauja"
"{division}" "serveru telpa"
"{division}" "datu centram" "elektroapgade"
"{division}" "datu centrs" "nodosana ekspluatacija"
site:{municipality-domain} "datu centrs" OR "datucentrs"
```

2. Search BIS manually by municipality/city, operator, and address. Use both planned-construction list and map:

```text
https://bis.gov.lv/bisp/en/planned_constructions
https://bis.gov.lv/bisp/en/planned_constructions/bismap
```

3. Search municipal documents for council and utility decisions:

```text
site:{municipality-domain} "datu centrs" "lemums"
site:{municipality-domain} "datu centrs" "domes sede"
site:{municipality-domain} "datu centram" "20kV"
site:{municipality-domain} "datu centram" "110kV"
site:{municipality-domain} "atlikumsiltums" "datu centrs"
site:{municipality-domain} "buvvalde" "datu centrs"
```

4. Search official energy/regulatory pages for the candidate operator/address:

```text
site:ast.lv "{operator}" OR "{project}"
site:sadalestikls.lv "{operator}" OR "{project}"
site:sprk.gov.lv "{operator}"
"{operator}" "elektronisko sakaru komersants"
```

5. Grade and store separately:

- `operator_status`: marketed/planned/launched from operator page;
- `construction_status`: BIS/municipal permit/commissioning status;
- `energy_status`: distribution/transmission/heating/fiber evidence;
- `confidence`: A/B/C, with exact URLs.

### Priority clusters

- **Riga**: Delska/DEAC, Tet Dattum/Brivibas/Kleistu/Perses/Atlasa/DC6, LVRTC Riga sites. Query Riga municipality/BIS with addresses (`Cuibes iela 17`, `Jana Asara iela 24`, `Kleistu iela 5`, `Talejas iela 1`) and operator legal names.
- **Salaspils novads**: Tet DC7 at/near `Krasta iela 2/1`, Salaspils Siltums heat reuse, optical and 20 kV external supply. This is the highest-value municipal-document workflow.
- **Liepaja**: Northern Energy Liepaja Data Centre in Liepaja Special Economic Zone; search Liepaja city, Liepaja SEZ, BIS, AST/Sadales tikls, `120 MW`, `110 kV`.
- **Jekabpils novads**: Northern Energy Jekabpils Old Airport; search airport land records, municipal agenda, BIS, AST/Sadales tikls, `114 MW`, `400 MW`, `110 kV`.
- **Kekavas novads**: C.T.Co / SIA Fraternitas at Valdlauci; likely small/enterprise facility but useful completeness check.
- **Kurzeme / Ventspils / Liepaja / Talsi / Kuldiga / Dienvidkurzemes novads**: LVRTC Positron's exact municipality may be obscured; do not assign exact location beyond public evidence.
- **Daugavpils, Valmiera, Ventspils, Liepaja regional LVRTC nodes**: treat LVRTC nationwide colocation nodes as facilities only when a primary or strong interconnection source names the site/address. Capacity is often unavailable.

### Low-yield municipalities

For municipalities with no obvious operator/industrial power lead, one pass of local-language queries plus BIS map/list search is usually enough. Record `no_projects` only after searching:

```text
"{division}" "datu centrs"
"{division}" "datucentrs"
"{division}" "serveru ferma"
"{division}" "kolokacija"
"{division}" "datu centram" "elektroapgade"
site:{municipality-domain} "datu centrs"
```

Avoid false positives from public-sector "data centers" meaning statistical/geospatial information centers, school IT rooms, or agriculture/weather data services.

---

## 5. Reliability rules

- **A**: BIS record, municipal council/construction-board/public-utility document, SPRK/AST/Sadales tikls official page, operator facility page, official cloud-region list, official LVRTC/Tet/Delska/Northern Energy page.
- **B**: established trade press such as Data Center Dynamics, Latvian Public Media/LSM, Labs of Latvia, Baltic Times, contractor pages (Citrus Solutions), PeeringDB for interconnection signal.
- **C**: DataCenterMap, Baxtel, Datacenters.com, Cloudscene, ColoMap, Lursoft snippets, marketplaces, social media, unsourced market reports.

Recommended record fields:

```text
name
division
municipality
address
cadastral_or_parcel_id
developer_operator
legal_entity
status
capacity_mw
racks_or_white_space
construction_evidence_url
operator_evidence_url
energy_evidence_url
evidence_date
evidence_grade
notes
```

Final caution: Latvia has small telecom/enterprise server rooms and nationwide telecom colocation nodes. Distinguish commercial/regional colocation from hyperscale/AI campuses, and avoid upgrading aggregate directory entries unless an operator, municipal, BIS, or regulator source confirms them.
