# HU Explorer Official - Hungary Datacenter Enumeration via Permits, Energy, Telecom Regulator, Public Procurement, and Cloud Sources

Date: 2026-08-12. Country: **HU Hungary**. Division model: **counties / cities with county rights / capital city** from `world-manifest.jsonl`. Angle: official and regulatory enumeration for operational, under-construction, and planned datacenter projects.

Reliability grades:
- **A** = official / primary source: national or local authority record, NMHH telecom-construction notice, official environmental record, MAVIR / DSO / MEKH record, EKR / Public Procurement Authority notice, official cloud-provider infrastructure page, official operator page.
- **B** = strong secondary source: established trade press, operator-linked contractor case study, HIPA / association material, Uptime / certification record, CERN / EuroHPC / university primary page where facility scope is compute/HPC rather than commercial colo.
- **C** = weak lead: directories, marketplace pages, generic hosting pages without facility detail, old press, market-report snippets, unverified capacity claims.

---

## 0. Hungary-specific structural facts

- Hungary has no public national "datacenter registry". Enumeration is a join across **OENY / E-epites / ETDR building-authority workflows**, local government and county-government notices, **NMHH telecom-construction permits**, environmental records, **MAVIR / DSO power evidence**, public procurement, and operator pages.
- The high-yield commercial market is **Budapest and the Budapest agglomeration in Pest county**: Budapest XIII / VIII / XI / XIV / X, Budaors, Torokbalint, and other western/southern suburbs. Secondary confirmed or plausible nodes include **Gyor**, **Szeged**, **Debrecen**, **Pecs**, **Nyiregyhaza**, **Szolnok**, **Szombathely**, **Eger**, **Zalaegerszeg**, and planned energy/HPC leads around **Paks / Tolna**.
- Building-permit records may describe datacenters as `adatkozpont`, `szerverkozpont`, `szerverterem`, `gephaz`, `iroda es technologiai epulet`, `telekommunikacios letesitmeny`, `informatikai kozpont`, `szamitastechnikai kozpont`, `gepterem`, `aggregator`, `UPS`, `hutestechnika`, `transzformatorallomas`, or `optikai csatlakozas`, rather than using an explicit real-estate asset class.
- Hungary's official online portals often require KAÜ / DAP login for deep case access. Public enumeration should therefore use **public notice pages, indexed official PDFs, authority announcements, EKR attachments, and operator-confirmed facility pages**, then record when the source is only a process route.
- Do not treat cloud sales offices as datacenter regions. AWS has a Budapest office announcement, but no official AWS Hungary Region or Local Zone found in AWS infrastructure pages as of this file date. Microsoft Azure's official region lists do not show a Hungary public cloud region. Google Cloud's official locations do not show a Hungary cloud region. Oracle/OCI has region-code signals that should be rechecked in official OCI region documentation; treat any `eu-budapest-1` / IdomSoft Budapest signal as a sovereign/dedicated-region lead until confirmed by Oracle primary documentation and local-government records.

Hungarian lifecycle vocabulary:

```text
telepulesrendezesi terv / HESZ / SZT
telepuleskepi velemeny
kornyezeti vizsgalat / elozetes vizsgalat
kornyezetvedelmi engedely / levegotisztasag-vedelmi engedely
epitesi engedely
epitesi naplo megnyitasa
hasznalatbaveteli engedely / hasznalatbavetel tudomasulvetele
uzembe helyezes / atadas
```

Strong facility evidence: `epitesi engedely`, `hasznalatbaveteli engedely`, official operator launch/current facility page, official procurement/contract naming a physical datacenter, NMHH permit naming datacenter connectivity, or official HPC/cloud-region launch. Treat zoning, grid discussions, and letters of intent as planned/pre-development.

---

## 1. Hungarian and English query patterns

Search both ASCII and accented forms. Hungarian sites vary in indexing, and many government PDFs use accents.

### 1.1 Core Hungarian terms

```text
adatkozpont / adatközpont
adatkozponti szolgaltatas / adatközponti szolgáltatás
szerverkozpont / szerverközpont
szerverterem
gepterem / gépterem
szamitastechnikai kozpont / számítástechnikai központ
informatikai kozpont / informatikai központ
kolokacio / kolokáció
szerver hosting / szerver hoszting
felho / felhő
felhoszolgaltatas / felhőszolgáltatás
hiperskala / hyperscale
MI adatkozpont / AI adatkozpont
nagy kapacitasu szamitogepes adatkozpont
optikai csatlakozas / optikai megcsatlakozas
transzformatorallomas / trafoallomas
aggregator / aramfejleszto
szunetmentes tapegyseg / UPS
hutestechnika / hutes
levegotisztasag-vedelmi engedely
kornyezeti hatasvizsgalat
epitesi engedely
hasznalatbaveteli engedely
kozbeszerzes
```

### 1.2 Official permit and planning templates

Substitute `{division}`, `{county}`, `{city}`, `{district}`, `{operator}`, `{legal_entity}`, `{address}`, `{parcel}`.

```text
site:e-epites.hu "adatkozpont" "{city}"
site:e-epites.hu "szerverkozpont"
site:e-epites.hu "szerverterem" "epitesi engedely"
site:etdr.gov.hu "adatkozpont"
site:kormanyhivatalok.hu "{county}" "adatkozpont"
site:kormanyhivatalok.hu "{city}" "epitesi engedely" "adatkozpont"
site:{city-domain} "adatkozpont" "epitesi engedely"
site:{city-domain} "szerverterem" "hasznalatbaveteli"
site:{city-domain} "HESZ" "adatkozpont"
site:{city-domain} "telepulesrendezesi" "adatkozpont"
site:{city-domain} "transzformatorallomas" "adatkozpont"
"{operator}" "{city}" "epitesi engedely"
"{legal_entity}" "hasznalatbaveteli engedely"
"{address}" "adatkozpont"
filetype:pdf "adatkozpont" "epitesi engedely" "{city}"
filetype:pdf "szerverterem" "kivitelezes" "{city}"
```

### 1.3 Environment, power, and telecom templates

```text
site:webgis.okir.hu "adatkozpont"
site:kapu.okir.hu "adatkozpont"
site:kormanyhivatalok.hu "adatkozpont" "kornyezeti"
site:kormanyhivatalok.hu "szerverterem" "levegőtisztaság" OR "levegotisztasag"
site:mavir.hu "adatkozpont"
site:mavir.hu "{city}" "transzformatorallomas"
site:mavir.hu "{project}" OR "{legal_entity}"
site:mekh.hu "adatkozpont" OR "{operator}"
site:eon.hu "adatkozpont" "{city}"
site:mvmhalozat.hu "adatkozpont" "{city}"
site:opustitasz.hu "adatkozpont" "{city}"
site:nmhh.hu "adatkozpont" "epitesi engedely"
site:nmhh.hu "optikai csatlakozas" "adatkozpont"
site:nmhh.hu "{operator}" "adatkozpont"
site:nmhh.hu "{city}" "DC1" "adatkozpont"
```

### 1.4 English templates

```text
"Hungary" "data center" "building permit"
"Budapest" "data center" "building permit"
"Hungary" "data centre" "grid connection"
"Budapest" "data center" "MAVIR"
"Hungary" "AI data center" "Paks"
"Azure" "Hungary" "region" site:learn.microsoft.com
"AWS" "Hungary" "Local Zone" site:aws.amazon.com
"Oracle Cloud" "Budapest" "eu-budapest-1"
"Google Cloud" "Hungary" "region" site:cloud.google.com
"{operator}" "{city}" "data center" Hungary
```

---

## 2. Grade A official / regulatory source backbone

### 2.1 Building permits and construction administration: E-epites / OENY / ETDR

Primary sources:

- E-epites portal: https://www.e-epites.hu/. **Grade A for process and linked systems**.
- ETDR page: https://www.e-epites.hu/etdr. **Grade A for building-authority case workflow**. It supports applications and notices for construction permits, demolition, retention permits, occupancy/use permits, simple notifications, and heritage procedures. Public data are available through the public ETDR interface, but deep use may require central authentication.
- Lechner E-construction description: https://lechnerkozpont.hu/en/oldal/e-construction. **Grade A process source**. It confirms ETDR as the national electronic documentation system for building-authority licensing and authenticated decisions.
- E-epites building-permit guidance: https://www.e-epites.hu/lakossagi-tajekoztatok/tajekoztato-az-epitesi-engedelyezesi-eljaras-szabalyairol. **Grade A process source**. It notes that building permits are requested for a parcel / whole construction activity and through the territorially competent building authority or ETDR.
- E-naplo / electronic construction log: linked from E-epites. **Grade A process source**, but public enumeration is limited.
- E-kozmu: linked from E-epites. **Grade A utility-map/process source**, useful for parcel-level infrastructure context after a lead is known.

What to extract:

- authority and case number;
- applicant / investor legal name;
- project description and function;
- `helyrajzi szam` / cadastral parcel, address, district, municipality;
- permit type: `epitesi engedely`, `bontasi engedely`, `fennmaradasi engedely`, `hasznalatbaveteli engedely`, `egyszeru bejelentes`;
- dates: application, decision, finality, start, occupancy/use;
- specialist-authority involvement: environment, fire, disaster management, water, telecom, heritage, road;
- technical clues: IT rooms, backup generators, transformer rooms, cooling plant, fuel storage, UPS/battery rooms, fiber connection.

Caution: an ETDR process route is not itself a public project list. For repeatable enumeration, use ETDR public data where available, indexed official notices, and municipality/county PDFs. Do not scrape authenticated case material.

### 2.2 Local government and county government records

The public permit unit is often a **district / municipality / government-office** workflow rather than a county-level dataset. Search both municipality sites and `kormanyhivatalok.hu`.

Primary routes:

- County/capital government offices: https://kormanyhivatalok.hu/. **Grade A** for official notices, environmental files, administrative decisions, and county-office contacts.
- Municipality and city portals: `budapest.hu`, district sites such as `bp13.hu`, `jozsefvaros.hu`, `ujbuda.hu`, `kobanya.hu`, and county-right city sites such as `debrecen.hu`, `gyor.hu`, `szegedvaros.hu`, `pecs.hu`, `nyiregyhaza.hu`, `szolnok.hu`, `zalaegerszeg.hu`. **Grade A** when the notice is official.
- Local planning documents: `HESZ`, `szabalyozasi terv`, `telepulesrendezesi eszkozok`, `telepuleskepi velemeny`, council minutes, zoning amendments, land sales, and utility-servitude records.

Use local pages to catch early pipeline:

```text
site:{city-domain} "HESZ" "adatkozpont"
site:{city-domain} "szabalyozasi terv" "adatkozpont"
site:{city-domain} "kozgyules" "adatkozpont"
site:{city-domain} "telepuleskepi velemeny" "szerverterem"
site:{city-domain} "ingatlan ertekesites" "adatkozpont"
site:{city-domain} "ipari park" "adatkozpont"
```

Planning evidence alone is **B/C for project existence** unless it names the investor and facility function. Upgrade only after permit, procurement, grid, or operator confirmation.

### 2.3 Environmental, disaster-management, and water evidence

Primary sources:

- OKIR / National Environmental Information System map and data browser: https://webgis.okir.hu/base/. **Grade A for official environmental-object and emissions/waste/water datasets**.
- OKIRkapu: https://kapu.okir.hu/okirkapuugyfel/. **Grade A process source** for environmental customer/object reporting, but login is required for customer-side submissions.
- County government office environmental notices: https://kormanyhivatalok.hu/. **Grade A** when a public notice or PDF names the project.

Datacenters can surface as:

- air-emissions permits for backup diesel generators (`aggregator`, `aramfejleszto`, `levegotisztasag-vedelmi engedely`);
- noise studies for cooling plant;
- fuel storage, battery/UPS, or fire-protection systems;
- water permits if cooling or stormwater works are material;
- environmental preliminary screening (`elozetes vizsgalat`) if the project is part of a larger industrial campus.

Search:

```text
"{operator}" "aggregator" "adatkozpont"
"{city}" "szerverterem" "levegotisztasag"
"{city}" "adatkozpont" "zaj"
"{project}" "kornyezeti hatasvizsgalat"
"{project}" "elozetes vizsgalat"
"{project}" "katasztrofavedelem" "adatkozpont"
```

Grade **A** when a public authority document names the facility/operator. Grade **B** if the environmental source only confirms associated power/cooling infrastructure near a known operator site.

### 2.4 NMHH telecom-regulator and telecom-construction records

Primary sources:

- NMHH main site and registries: https://nmhh.hu/ and https://nmhh.hu/hirkozles/nyilvantartasok. **Grade A regulator source** for electronic-communications registries and telecom-related notices.
- Electronic communications service/provider registry: https://nmhh.hu/hirkozles/szolgaltatasok-nyilvantartasa. **Grade A for provider/service registration**, but not proof of datacenter facility.
- NMHH guide for electronic communications structures: https://nmhh.hu/cikk/742/Utmutato_elektronikus_hirkozlesi_epitmenyek_engedelyezesi_eljarasahoz. **Grade A process source** for telecom construction.
- NMHH permit notice example: https://nmhh.hu/cikk/237142/Ertesites_epitesi_engedely_megadasarol__CD605322023_szamu_hatarozat_Debrecen_BMW_Hungary_Kft_DC1_adatkozpont_optikai_csatlakozas. **Grade A**. It demonstrates that NMHH notices can explicitly name a datacenter-related optical connection: Debrecen, BMW Hungary Kft. DC1 datacenter optical connection.

Use NMHH for:

- fiber routes and optical connections to named datacenters;
- carrier/ISP legal-entity pivots;
- telecom construction permits where the datacenter building itself is not listed in a public construction search;
- public-sector or enterprise campuses with `DC1`, `DC2`, `adatkozpont optikai megcsatlakozas`.

Do not count an NMHH service-provider registry record alone as a datacenter. It is **A for legal/operator identity**, **C for facility existence** until matched to a facility page, permit, procurement, interconnection, or construction record.

### 2.5 Energy and grid evidence: MAVIR, MEKH, and DSOs

Primary sources:

- MAVIR official site: https://www.mavir.hu/. **Grade A** for transmission-system operator context, transmission assets, network plans, and national electricity-system information.
- MVM / transmission and system-operation overview: https://mvm.hu/en/Tevekenysegunk/AtvitelRendszerIranyitas. **Grade A/B** for group-level context.
- Hungarian Energy and Public Utility Regulatory Authority (MEKH): https://www.mekh.hu/. **Grade A regulator source** for electricity and utility regulation.
- IEA Hungary electricity security profile: https://www.iea.org/articles/hungary-electricity-security-policy. **B** for context; it identifies MAVIR as TSO and notes the role of DSOs under the energy regulator.
- DSO/operator pages to search by geography:
  - E.ON Hungaria / E.ON Aramhálózat: https://www.eon.hu/
  - MVM Halózat / MVM EMASZ / MVM DEMASZ: https://mvmhalozat.hu/
  - OPUS TITASZ: https://www.opustitasz.hu/
  - ELMU Halózat / Budapest-Pest distribution references through E.ON/MVM legacy pages.

Power evidence to capture:

- requested/contracted demand in MW or MVA;
- grid voltage, substation, transformer station, redundant feeds;
- DSO/TSO connection point;
- backup generators and fuel;
- energy-storage or on-site solar/BESS references;
- whether the evidence is a load connection, an energy project, or only market/grid context.

Power evidence is often harder to search publicly for demand-side datacenters than renewable generators. Use it for corroboration and site-suitability, not as a standalone facility proof unless the document names the project.

### 2.6 Public procurement: EKR, Közbeszerzési Hatóság, TED

Primary sources:

- Public Procurement Authority of Hungary: https://www.kozbeszerzes.hu/ and English page https://english.kozbeszerzes.hu/. **Grade A**.
- EKR public contract/procedure portal: https://ekr.gov.hu/. **Grade A**.
- EU TED: https://ted.europa.eu/. **Grade A/B** for EU-threshold notices and English discovery.

High-yield public-sector terms:

```text
adatkozpont
kormanyzati adatkozpont
FEAK
NISZ
IdomSoft
DKU
szerverterem
gepterem
szerver hosting
hosting szolgaltatas
adatkozpont uzemeltetes
adatkozpont bovites
hutesi rendszer
szunetmentes tapegyseg
halozati kapcsoloeszkoz
sotetszal
BIX
```

Useful examples from public procurement search results include:

- EKR contract titled `Adatkozpont uzemeltetes tamogatas 2024` at https://ekr.gov.hu/ekr-szerzodestar/hu/szerzodes/951653. **Grade A for the public contract**, facility status depends on content.
- Közbeszerzés attachments naming `NISZ Kormanyzati Adatkozpont`, `Wigner Datacenter`, `Kormanyzati Adatkozpont bovites`, and `FEAK Fuggetlen Energetikai Adatkozpont Zrt.`. **Grade A** when document text names facility locations and work scope.

Procurement often describes equipment/services, not new construction. Use it to identify public-sector datacenters, expansions, hosting sites, dark-fiber interconnects, and exact facility addresses.

### 2.7 Official cloud-region and hyperscaler checks

Cloud pages are **A for logical cloud-region/local-zone existence**, but usually **C for exact physical facility** unless an official record names the site.

| Provider | Official source | Hungary signal as of 2026-08-12 | Enumeration use |
|---|---|---|---|
| Microsoft Azure | Regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list and geographies https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No official Hungary public Azure region found in official region/geography lists. | Use as a negative-control search. Do not count "Azure Hungary" sales/partner activity as a datacenter. Search Microsoft partner, sovereign/government cloud, and colocation only if official docs change. |
| AWS | Regions https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No official AWS Hungary Region or Budapest Local Zone found; AWS opened a Budapest office in 2023 via official Amazon/AWS news. | Office = market presence only. Do not infer AWS datacenter. Search Direct Connect / edge / partners separately. |
| Google Cloud | Locations https://cloud.google.com/about/locations and Compute regions/zones https://docs.cloud.google.com/compute/docs/regions-zones | No official Google Cloud Hungary region found. | Market/partner presence only unless official locations change. |
| Oracle Cloud | OCI regions docs https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and CLI/support docs | `eu-budapest-1` appears in some Oracle tooling/support-region lists; a Visual Builder Studio public-IP page references `IdomSoft Budapest Hungary (JSK)`. | Treat as an Oracle/IdomSoft sovereign/dedicated-region lead requiring official Oracle region confirmation, procurement, and local records. Do not treat as ordinary public OCI region without current Oracle docs. |

Cloud query templates:

```text
"Azure Hungary" "datacenter region" site:microsoft.com OR site:learn.microsoft.com
"AWS Hungary" "Local Zone" site:aws.amazon.com
"AWS Budapest" "Direct Connect"
"Google Cloud Hungary" "region" site:cloud.google.com
"Oracle Cloud" "eu-budapest-1"
"IdomSoft" "Budapest" "Oracle Cloud"
"IdomSoft" "adatkozpont" "Oracle"
```

---

## 3. Official operator and public-infrastructure seed list

Official operator pages are **A for operator-claimed facility existence/current marketed footprint**; capacities still need facility-level statements or strong corroboration.

| Operator / facility | Official / primary URL | Official signal | Use |
|---|---|---|---|
| Magyar Telekom / T-Systems / Dataplex / Adatpark | https://www.telekom.hu/about_us/services/wholesale/national_fixed_line_solutions/ip_and_data/hosting | Telekom lists data centers in Budapest, Budaors, Victor Hugo Budapest, Gyor, and Szeged with addresses and facility/service features. | Highest-priority official seed for Budapest, Pest, Gyor, Szeged. |
| 2Connect / former Invitech network units | https://2connect.hu/adatkozpont | More than 6,500 sqm capacity across 12 locations, 3 commercial and 9 telecom datacenters. | Use as official seed for Invitech/4iG/One-era facilities; pivot to NMHH, EKR, Uptime, and addresses. |
| NMHH Debrecen BMW DC1 optical connection | https://nmhh.hu/cikk/237142/Ertesites_epitesi_engedely_megadasarol__CD605322023_szamu_hatarozat_Debrecen_BMW_Hungary_Kft_DC1_adatkozpont_optikai_csatlakozas | Official telecom construction notice for BMW Hungary Kft. DC1 datacenter optical connection in Debrecen. | Confirms datacenter-related infrastructure inside BMW Debrecen campus; classify as enterprise/campus unless independent facility evidence appears. |
| Wigner Data Center / CERN | https://home.cern/cern-and-the-wigner-research-centre-for-physics-inaugurate-cern-data-centres-extension-in-budapest-hungary/ | CERN primary source for Budapest extension to CERN data centre. | Official HPC/research datacenter; not commercial colo. |
| University / KIFU / HPC facilities | KIFU/HPC pages such as https://www.hpc.kifu.hu/en and university pages | National HPC and research-compute facilities in Debrecen/Szeged/Budapest ecosystem. | Count separately if scope includes research/public-sector compute. |
| Government datacenter / NISZ / FEAK / IdomSoft | EKR, Közbeszerzés, TED, NISZ/IdomSoft official pages | Public procurement frequently names government datacenter locations, expansions, hosting and dark-fiber links. | Strong official channel for public-sector facilities; exact public disclosure may be partial. |

---

## 4. Division-level official enumeration method

For each division, run four passes:

1. **Known-operator pass**: Magyar Telekom, 2Connect/Invitech, RackForest/Rackhost, VIVAnet, Servergarden, Datacenter.hu / DP Data Center, local ISP, university/HPC, public-sector names.
2. **Official permit pass**: ETDR/E-epites public data, city/district portals, county government office notices, `kormanyhivatalok.hu`, zoning/HESZ/council minutes.
3. **Regulatory/infrastructure pass**: NMHH telecom-construction notices, MAVIR/DSO/MEKH power clues, OKIR/environment, disaster-management, EKR/Közbeszerzés/TED.
4. **Cross-check pass**: operator page, certification, procurement address, PeeringDB/BIX, DataCenterMap/Baxtel/Inflect only as weak leads.

Universal division templates:

```text
"{division}" "adatkozpont"
"{division}" "adatközpont"
"{division}" "szerverkozpont"
"{division}" "szerverterem"
"{division}" "kolokacio"
"{division}" "data center" Hungary
"{division}" "epitesi engedely" "adatkozpont"
"{division}" "hasznalatbaveteli engedely" "szerverterem"
"{division}" "kornyezeti" "adatkozpont"
"{division}" "NMHH" "adatkozpont"
"{division}" "MAVIR" "transzformatorallomas"
"{division}" "EKR" "adatkozpont"
site:kormanyhivatalok.hu "{division}" "adatkozpont"
site:kozbeszerzes.hu "{division}" "adatkozpont"
site:ekr.gov.hu "{division}" "adatkozpont"
```

### 4.1 Priority divisions and official pivots

| Division | Official search focus | Seed operators / projects |
|---|---|---|
| Budapest | District portals, E-epites/ETDR, NMHH, EKR, OKIR, BIX/PeeringDB, public-sector procurement. Query districts XIII, VIII, XI, X, XIV, IX. | Magyar Telekom Dataplex / Victor Hugo, RackForest/Rackhost, VIVAnet, Wigner/CERN, NISZ/FEAK/IdomSoft, Servergarden/Systech/Ilka, 2Connect/Invitech. |
| Pest | Budaors, Torokbalint, Dunakeszi/Fot, Vecses, Szigetszentmiklos, Biatorbagy; county government and municipal portals. | Magyar Telekom Budaors, 2Connect/Invitech Budaors/DC10 leads, KBC Torokbalint enterprise DC, potential Budapest-suburb cloud/enterprise sites. |
| Debrecen / Hajdu-Bihar | Debrecen city, Hajdu-Bihar government office, NMHH, EKR, BMW industrial-zone records, university/HPC pages. | DP Data Center / Dryvit Profi, BMW DC1 optical connection, University of Debrecen / Komondor HPC. |
| Gyor / Gyor-Moson-Sopron | Gyor city, county government, telecom/industrial campus permits. | Magyar Telekom Adatpark Gyor; Audi/industrial enterprise server-room leads. |
| Szeged / Csongrad-Csanad | Szeged city, county government, university/HPC records. | Magyar Telekom Adatpark Szeged, Rackhost/RackForest Szeged, University of Szeged / Komondor ecosystem. |
| Baranya / Pecs | Pecs city, county government, local telco/ISP permits. | Dravanet Pecs, university/public-sector server rooms. |
| Szabolcs-Szatmar-Bereg / Nyiregyhaza | Nyiregyhaza city, county government, ISP/NMHH records. | Giganet Nyiregyhaza. |
| Jasz-Nagykun-Szolnok / Szolnok | Szolnok city, county government, local company registry/procurement. | KMAK / Kelet-Magyarorszagi Adatkozpont. |
| Heves / Eger | Eger city and county government; small hosting/server-room records. | Data Center Solutions / DC Hosting Eger lead. |
| Vas / Szombathely | Szombathely city and county government. | ISIS-COM Szombathely. |
| Zala / Zalaegerszeg | Zalaegerszeg city, ZalaZONE, university/R&D official records. | ZalaZONE EMAK energy-management data platform; classify as R&D/industrial compute. |
| Tolna / Szekszard | Paks and Tolna county official notices, energy/regulator, MAVIR/MEKH, Paks nuclear-adjacent land/power records. | Planned Paks AI/datacenter/BESS/agro-PV leads; do not upgrade beyond planned until permit/grid/operator evidence appears. |

### 4.2 Lower-yield divisions still requiring a negative-control pass

Run the universal templates for all remaining divisions, then add local industrial/university terms:

```text
Baranya, Bekescsaba, Bekes, Bacs-Kiskun, Borsod-Abauj-Zemplen, Dunaujvaros,
Eger, Erd, Fejer, Hodmezovasarhely, Komarom-Esztergom, Kecskemet,
Kaposvar, Miskolc, Nagykanizsa, Nograd, Sopron, Somogy, Szekszard,
Salgotarjan, Tatabanya, Veszprem
```

Add these local pivots where relevant:

```text
"{division}" "ipari park" "szerverterem"
"{division}" "egyetem" "szerverterem"
"{division}" "onkormanyzat" "adatkozpont"
"{division}" "kormanyhivatal" "szerverterem"
"{division}" "telekom" "adatpark"
"{division}" "optikai csatlakozas" "DC1"
```

Negative result guidance: mark `no_projects` only after checking Hungarian and English datacenter terms, local government/ETDR/NMHH/ERK search, and known operator/directories. Small server-room contractor references are **C** unless an official/operator page names a facility function.

---

## 5. Evidence and deduping rules

- Marketed "Budapest" facilities may physically be in **Pest county**. Always normalize by actual municipality/address: Budapest district vs Budaors/Torokbalint/etc.
- Count enterprise/campus/server-room projects separately from commercial colocation/hyperscale. Examples: BMW Debrecen DC1 optical connection, KBC Torokbalint, SK Innovation Komarom power-supply reference.
- Count research/HPC separately from commercial datacenters: Wigner/CERN, KIFU/Komondor, university supercomputers, ZalaZONE EMAK.
- Do not assign a national/procurement capacity to one site unless the source is facility-specific.
- Do not treat BIX/PeeringDB/ISP registry as facility proof unless matched to an address/operator facility page.
- Store power fields separately: `requested_connection_mw`, `contracted_mva`, `it_load_mw`, `generator_mw`, `facility_power_mw`, and `source_power_term`.
- For Paks/Tolna AI campus claims, require at least two of: official developer announcement, local/county permit, grid/energy approval, land/municipal record, or credible construction start. A letter of intent remains planned **B/C**.
