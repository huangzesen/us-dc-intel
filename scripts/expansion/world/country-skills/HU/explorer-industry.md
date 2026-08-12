# HU Explorer Industry - Hungary Datacenter Enumeration via Operators, Trade Press, Directories, Cloud Checks, and County Query Patterns

Date: 2026-08-12. Country: **HU Hungary**. Scope: industry / vendor / trade-press discovery for datacenters, colocation, hosting, enterprise server rooms, public-sector datacenters, and HPC facilities. Reliability grades: **A** = official/primary/operator-owned current source, **B** = strong trade press/vendor case study/certification, **C** = directory/aggregator/weak lead.

---

## 0. Hungary-specific industry frame

- Hungary is a **Budapest-first** market. Most commercial colocation and carrier-neutral/telecom datacenter evidence is in Budapest or the Pest-county agglomeration, with regional edge/telecom/hosting nodes in Gyor, Szeged, Debrecen, Pecs, Nyiregyhaza, Szolnok, Szombathely, Eger, and selected university/HPC sites.
- Use industry sources to discover names and addresses, then verify with **operator pages, NMHH telecom permits, EKR/Kozbeszerzes procurement, ETDR/local permits, OKIR/environment, and MAVIR/DSO power records**.
- Hungarian providers often market `szerver hosting`, `szerverbérlés`, `kolokáció`, `gépterem`, `szerverterem`, `felhő`, `adatközponti szolgáltatás`, or `virtualis adatkozpont` rather than "data center".
- Separate facility classes:
  - **commercial colocation / hosting**: Magyar Telekom, 2Connect/Invitech, RackForest/Rackhost, VIVAnet, Servergarden/Systech, Datacenter.hu / DP Data Center, local ISPs;
  - **public-sector/government**: NISZ, FEAK, IdomSoft, Wigner, KIFU/HPC, EESZT health infrastructure;
  - **enterprise/campus**: BMW Debrecen DC1, KBC Torokbalint, SK Innovation Komarom, bank/industrial server rooms;
  - **planned AI/energy campus**: Paks/Tolna leads requiring official confirmation.
- Directories are useful because many Hungarian local providers have sparse public pages. They must not be used alone above **C/C+** unless confirmed by an operator or official source.

---

## 1. Industry, trade press, and directory sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; queries `site:datacenterdynamics.com Hungary data center Budapest`, `site:datacenterdynamics.com Paks Hungary data center` | Historical Dataplex, Wigner/CERN, EuroHPC, 4iG, Paks AI/energy leads. | B |
| Magyar Telekom official hosting | https://www.telekom.hu/about_us/services/wholesale/national_fixed_line_solutions/ip_and_data/hosting | Best official source for Telekom facilities in Budapest, Budaors, Victor Hugo, Gyor, Szeged. | A |
| 2Connect official datacenter page | https://2connect.hu/adatkozpont | Official footprint for former Antenna/DIGI/Invitech/Vodafone network-infrastructure combination: 6,500+ sqm, 12 locations, 3 commercial + 9 telecom datacenters. | A |
| RackForest official | https://rackforest.com/ and service pages such as https://rackforest.com/szolgaltatasok/szerver-berles/ | Hungarian hosting/cloud provider. Service page states georedundancy, 5 rooms, 3 Budapest locations. | A/B |
| VIVAnet official | https://vivanet.hu/en/ | Carrier-neutral Budapest datacenter, opened/operating since July 2024, 140-rack first-phase room signal. | A |
| Datacenter.hu / DP Data Center / Dryvit Profi | https://datacenter.hu/ , Dryvit pages such as https://dryvitprofi.hu/tag/adatkozpont/ and https://dryvitprofi.hu/2021/02/19/dp-data-center-szerverkozpont-kiepitesi-munkalatai/ | Debrecen DP Data Center / Dryvit Profi lead; verify current operational status and address. | A/B depending page |
| EPS-Connect case/news | https://eps-connect.hu/egyedulallo-adatkozpont-epul-debrecenben/ | Debrecen construction/infrastructure lead for unique datacenter. | B |
| NMHH public notices | https://nmhh.hu/ | Industry-relevant telecom construction permits; BMW Debrecen DC1 optical connection is a high-signal example. | A |
| EKR / Kozbeszerzes | https://ekr.gov.hu/ , https://www.kozbeszerzes.hu/ | Public-sector datacenter operations, expansions, dark fiber, government cloud, FEAK/NISZ/IdomSoft clues. | A |
| DatacenterMap | https://www.datacentermap.com/hungary/ | Lists Hungary markets/facilities; current result showed 18 facilities across Budapest, Szeged, Nyiregyhaza, Pecs, Szombathely. | C+ |
| Baxtel | https://baxtel.com/data-center/hungary and https://baxtel.com/data-center/budapest | Market/facility seeds, capacity snippets such as Dataplex 8 MW; verify. | C+ |
| Inflect / DatacenterPlatform / Datacenters.com / Cloudscene | Country and city pages | Good for aliases like Invitech DC10, NTT/Budaors legacy, Servergarden, SZTAKI, PanTel; verify status and addresses. | C/C+ |
| PeeringDB / BIX | https://www.peeringdb.com/ and https://www.bix.hu/ | Confirms interconnection ecosystem and facilities used for peering; not complete facility census. | B/C |
| HIPA / IVSZ / events | https://hipa.hu/ and IVSZ/HIPA datacenter prospectus PDF | Market context, site-selection framing, investor leads; not a live facility registry. | B/C |
| Data Center Event Budapest | https://datacenterevent.eu/ | Current ecosystem, sponsors, contractors, market participants. | C |

Trade and local press query templates:

```text
site:datacenterdynamics.com Hungary "data center" Budapest
site:datacenterdynamics.com Hungary "data centre" Paks
site:dailynewshungary.com Hungary "data centre" Paks
site:magyarepitok.hu adatkozpont Debrecen
site:dehir.hu Debrecen adatkozpont
site:portfolio.hu adatkozpont Magyarorszag
site:hwsw.hu adatkozpont Magyarorszag
site:bitport.hu adatkozpont Magyarorszag
site:itbusiness.hu adatkozpont
site:ictglobal.hu adatkozpont
site:computerworld.hu adatkozpont
site:profitline.hu adatkozpont Magyarorszag
site:teol.hu Paks adatkozpont MI
site:vg.hu Paks adatkozpont mesterseges intelligencia
```

When reading press, record exact lifecycle terms:

- `bejelentette`, `szandeknyilatkozat`, `tervezett`, `vizsgaljak` = planned/intent.
- `epul`, `kivitelezes`, `alapkőletetel`, `beruhazas`, `engedely` = pipeline/construction lead.
- `atadtak`, `megnyilt`, `uzemel`, `szolgaltatas elerheto`, `hasznalatbavetel` = operational lead.

---

## 2. Operator and facility seed list

Official/operator pages are **A for existence when they name a facility or current footprint**. Capacity is **A/B only if facility-level**, otherwise keep null and note the claim.

### 2.1 Budapest and Pest county core operators

- **Magyar Telekom / T-Systems / Dataplex / Adatpark** - official hosting page lists:
  - T-Systems Cloud & DataCenter, Budapest, 1087 Budapest, Asztalos Sandor u. 13.
  - Budaors DC, 2040 Budaors, Ipartelep utca 13-15.
  - Victor Hugo DC, 1132 Budapest, Victor Hugo 18-22.
  - Adatpark Gyor, 9021 Gyor, Teleki Laszlo u. 36.
  - Adatpark Szeged, 6724 Szeged, Rokusi krt. 2-10.
  Official: https://www.telekom.hu/about_us/services/wholesale/national_fixed_line_solutions/ip_and_data/hosting . DCD reported Dataplex expansion/opening historically: https://www.datacenterdynamics.com/en/news/central-europes-largest-datacenter-opens-in-hungary-2/ . Grade A/B.
- **2Connect / Invitech / 4iG-One infrastructure** - official page says more than 6,500 sqm across 12 datacenter locations, 3 commercial and 9 telecom. Official: https://2connect.hu/adatkozpont . Use with Invitech/4iG pages, Uptime, and directory aliases such as DC10/Budaors/Budapest. Grade A/B.
- **RackForest / Rackhost / Rendszerinformatika** - official RackForest: https://rackforest.com/ ; server page states georedundancy across 5 rooms and 3 Budapest locations: https://rackforest.com/szolgaltatasok/szerver-berles/ . Rendszerinformatika Victor Hugo datacenter: https://rendszerinformatika.hu/en/datacenter-victor-hugo . Grade A/B.
- **VIVAnet DataCenter Kft.** - official: https://vivanet.hu/en/ . Carrier-neutral Budapest datacenter, operating since July 2024, first-phase room for 140 racks. Grade A.
- **Servergarden / Systech / Ilka utcai adatkozpont** - Systech official page: https://systech.hu/ilka-utcai-adatkozpont . Gives facility/network/cooling/security details and links DC10/DC14 virtual datacenter concept. Grade A/B.
- **KBC Torokbalint enterprise datacenter** - Cummins case study: https://www.cummins.com/news/2019/09/23/kbc-banks-data-centres-take-no-chances . Enterprise/bank facility, not public colo. Grade B.
- **Wigner Data Center / CERN** - CERN primary source: https://home.cern/cern-and-the-wigner-research-centre-for-physics-inaugurate-cern-data-centres-extension-in-budapest-hungary/ . Research/HPC data center. Grade A.
- **NISZ / FEAK / IdomSoft / government datacenter** - use EKR/Kozbeszerzes/TED, NISZ, DKU, IdomSoft, and Oracle/OCI clues. Procurement documents can name `Kormanyzati Adatkozpont`, `Wigner Datacenter`, `FEAK Fuggetlen Energetikai Adatkozpont Zrt.`, and Budapest addresses. Grade A when sourced to procurement or official operator.

Budapest/Pest templates:

```text
"Budapest" "adatkozpont" Magyar Telekom Dataplex RackForest VIVAnet Invitech Servergarden
"Budapest" "szerverterem" "Victor Hugo"
"Budapest" "adatkozpont" "Asztalos Sandor"
"Budapest" "adatkozpont" "Ilka utca"
"Budapest" "Wigner" "adatkozpont"
"Budaors" "adatkozpont" Telekom Invitech 2Connect
"Torokbalint" "data centre" KBC
"Pest" "adatkozpont" Budaors Torokbalint
site:2connect.hu "adatkozpont"
site:rackforest.com "Budapest" "georedundancia"
site:nmhh.hu Budapest "adatkozpont"
site:ekr.gov.hu Budapest "adatkozpont"
site:kozbeszerzes.hu "Kormanyzati Adatkozpont"
```

### 2.2 Debrecen / Hajdu-Bihar

- **DP Data Center / Dryvit Profi / Datacenter.hu** - official/related pages: https://datacenter.hu/ , https://dryvitprofi.hu/tag/adatkozpont/ , https://dryvitprofi.hu/2021/02/19/dp-data-center-szerverkozpont-kiepitesi-munkalatai/ . EPS-Connect reported a unique datacenter construction project in Debrecen: https://eps-connect.hu/egyedulallo-adatkozpont-epul-debrecenben/ . Grade A/B for lead; verify current operational status.
- **BMW Debrecen DC1** - NMHH official permit notice for BMW Hungary Kft. DC1 datacenter optical connection: https://nmhh.hu/cikk/237142/Ertesites_epitesi_engedely_megadasarol__CD605322023_szamu_hatarozat_Debrecen_BMW_Hungary_Kft_DC1_adatkozpont_optikai_csatlakozas . Enterprise/campus infrastructure. Grade A for optical connection and named DC1.
- **University of Debrecen / KIFU Komondor** - university/HPC pages and KIFU: https://www.hpc.kifu.hu/en . Research/HPC facility; separate from commercial colo. Grade A/B.

Debrecen templates:

```text
"Debrecen" "adatkozpont" "Dryvit Profi" OR "DP Data Center"
"Debrecen" "szerverkozpont" "Galamb"
"Debrecen" "BMW" "DC1 adatkozpont"
site:nmhh.hu Debrecen "DC1" "adatkozpont"
site:debrecen.hu "adatkozpont" OR "szerverterem"
site:kormanyhivatalok.hu "Hajdu-Bihar" "adatkozpont"
"University of Debrecen" Komondor supercomputer power
```

### 2.3 Gyor / Gyor-Moson-Sopron

- **Magyar Telekom Adatpark Gyor** - official Telekom hosting page lists the Gyor facility. Grade A.
- Industrial/enterprise server-room leads may appear through Audi, logistics, university, or contractor references; verify with operator or official records.

Templates:

```text
"Gyor" "Adatpark" "Magyar Telekom"
"Gyor" "adatkozpont" "Teleki Laszlo"
site:gyor.hu "adatkozpont" OR "szerverterem"
site:kormanyhivatalok.hu "Gyor-Moson-Sopron" "adatkozpont"
"Audi" Gyor "szerverterem" OR "adatkozpont"
```

### 2.4 Szeged / Csongrad-Csanad

- **Magyar Telekom Adatpark Szeged** - official Telekom page. Grade A.
- **Rackhost / RackForest Szeged** - directories and operator pages indicate a Szeged hosting/datacenter presence; verify against Rackhost/RackForest current pages and local records. Grade B/C until confirmed.
- **University of Szeged / Komondor ecosystem** - research/HPC or compute infrastructure; classify separately. Grade A/B.

Templates:

```text
"Szeged" "Adatpark" "Magyar Telekom"
"Szeged" "Rackhost" "adatkozpont"
"Szeged" "szerverterem" "Tisza Lajos"
site:szegedvaros.hu "adatkozpont" OR "szerverterem"
site:kormanyhivatalok.hu "Csongrad-Csanad" "adatkozpont"
"University of Szeged" "supercomputer" OR "Komondor"
```

### 2.5 Other regional operator leads

| Division / city | Operator/project seeds | Query notes |
|---|---|---|
| Pecs / Baranya | Dravanet Pecs | `Dravanet Pecs adatkozpont`, `site:pecs.hu adatkozpont`, `site:kormanyhivatalok.hu Baranya adatkozpont`. |
| Nyiregyhaza / Szabolcs-Szatmar-Bereg | Giganet Internet Kft. | `Giganet Nyiregyhaza adatkozpont`, `site:nyiregyhaza.hu szerverterem`, NMHH provider pivots. |
| Szolnok / Jasz-Nagykun-Szolnok | KMAK / Kelet-Magyarorszagi Adatkozpont Kft. | `KMAK Szolnok adatkozpont`, `Kelet-Magyarorszagi Adatkozpont`, company registry + operator page. |
| Eger / Heves | Data Center Solutions / DC Hosting | `DC Hosting Eger`, `Data Center Solutions Kft Eger`, local company and permit records. |
| Szombathely / Vas | ISIS-COM | `ISIS-COM Szombathely adatkozpont`, `site:szombathely.hu szerverterem`. |
| Komarom-Esztergom | SK Innovation Komarom enterprise DC power-supply lead | Contractor pages can identify UPS/power-supply work; require official/campus confirmation before counting. |
| Fejer / Szekesfehervar | Defence/enterprise server-room contractor references | Treat as C unless official military/public procurement or local permit confirms. |
| Zala / Zalaegerszeg | ZalaZONE EMAK energy-management data platform | R&D/industrial data platform; not commercial datacenter unless facility housing and compute scope are clear. |
| Tolna / Paks | AI/data-center/BESS/agro-PV campus leads | Use press only as B/C; require official land, grid, permit, or developer filing. |

---

## 3. Cloud and hyperscaler discovery

Cloud-region claims are frequent false positives in Hungary. Always compare with official infrastructure pages.

| Provider | Current official signal | Search/action |
|---|---|---|
| Azure | No Hungary public Azure region found in official Microsoft region/geography pages. | `Azure Hungary region site:learn.microsoft.com`; treat "Azure Hungary" as sales/partner unless region list changes. |
| AWS | No AWS Hungary Region or Budapest Local Zone found in AWS region/local-zone pages; AWS opened a Budapest office. | `AWS Hungary Local Zone`, `AWS Budapest Direct Connect`, `AWS office Budapest`. Office is not datacenter evidence. |
| Google Cloud | No Hungary GCP region found in official locations. | `Google Cloud Hungary region`, `Google Cloud Budapest partner`, no facility count without official location. |
| Oracle / OCI | `eu-budapest-1` appears in Oracle tooling/support-region lists; Visual Builder Studio docs reference `IdomSoft Budapest Hungary (JSK)`. | `Oracle eu-budapest-1`, `IdomSoft Oracle adatkozpont`, `OCI Budapest`. Treat as sovereign/dedicated-region lead requiring official and local confirmation. |
| CDN/edge providers | Cloudflare, Bunny, Akamai, Fastly, etc. may have Hungary PoPs. | Edge/PoP is not datacenter unless the physical host facility is named. Use PeeringDB/BIX to identify host facilities. |

Cloud templates:

```text
"Azure Hungary" "datacenter region"
"AWS Hungary" "Local Zone"
"AWS Budapest" "Direct Connect"
"Google Cloud Hungary" "region"
"Oracle Cloud" "Budapest" "eu-budapest-1"
"IdomSoft" "Oracle Cloud" "Budapest"
"Cloudflare" "Budapest" "data center" "BIX"
"BIX" "Budapest" "data center" RackForest Telekom Invitech
```

---

## 4. County / city query patterns

For every division, run the universal patterns below, then add the local seed terms in the table.

Universal Hungarian patterns:

```text
"{division}" "adatkozpont"
"{division}" "adatközpont"
"{division}" "szerverkozpont"
"{division}" "szerverterem"
"{division}" "szerver hosting"
"{division}" "kolokacio"
"{division}" "georedundans"
"{division}" "data center" Hungary
"{division}" "epitesi engedely" "adatkozpont"
"{division}" "optikai csatlakozas" "adatkozpont"
"{division}" "ipari park" "adatkozpont"
site:nmhh.hu "{division}" "adatkozpont"
site:ekr.gov.hu "{division}" "adatkozpont"
site:kormanyhivatalok.hu "{division}" "szerverterem"
```

Division-specific seeds:

| Division(s) | Add these operator/locality terms |
|---|---|
| Budapest | `Dataplex`, `Asztalos Sandor`, `Victor Hugo`, `RackForest`, `VIVAnet`, `Wigner`, `CERN`, `Servergarden`, `Ilka`, `BIX`, `NISZ`, `FEAK`, `IdomSoft`, district XIII/VIII/XI/X/XIV. |
| Pest / Erd | `Budaors`, `Torokbalint`, `Ipartelep`, `KBC`, `Invitech`, `2Connect`, `Magyar Telekom Budaors`, `Biatorbagy`, `Vecses`, `Dunakeszi`, `Fot`. |
| Debrecen / Hajdu-Bihar | `DP Data Center`, `Dryvit Profi`, `Galamb`, `BMW DC1`, `Komondor`, `KIFU`, `University of Debrecen`. |
| Gyor / Gyor-Moson-Sopron | `Adatpark Gyor`, `Teleki Laszlo`, `Audi`, `Szechenyi Istvan University`. |
| Szeged / Csongrad-Csanad | `Adatpark Szeged`, `Rackhost`, `Tisza Lajos`, `Rokusi`, `University of Szeged`, `Komondor`. |
| Pecs / Baranya | `Dravanet`, `Budai Nagy Antal`, `PTE`, `university server room`. |
| Nyiregyhaza / Szabolcs-Szatmar-Bereg | `Giganet`, `ISP`, `szerver hosting`. |
| Szolnok / Jasz-Nagykun-Szolnok | `KMAK`, `Kelet-Magyarorszagi Adatkozpont`, `hosting`. |
| Eger / Heves | `DC Hosting`, `Data Center Solutions`, `Eszterhazy`, `szerverterem`. |
| Szombathely / Vas | `ISIS-COM`, `szerver hosting`, `kolokacio`. |
| Zala / Zalaegerszeg | `ZalaZONE`, `EMAK`, `Szechenyi Istvan University`, `energy management data center`. |
| Tolna / Szekszard | `Paks`, `AI adatkozpont`, `mesterséges intelligencia`, `BESS`, `agro-photovoltaic`, `Paksi Atomeromu`. |
| Komarom-Esztergom / Tatabanya | `SK Innovation`, `Komarom`, `adatkozpont aramellatas`, `UPS`, `industrial campus`. |
| Fejer / Szekesfehervar / Dunaujvaros | `Szekesfehervar`, `MH OHP`, `honvedsegi szerverterem`, `Dunaujvaros ipari park`. |
| Borsod-Abauj-Zemplen / Miskolc | `University of Miskolc supercomputer`, `Miskolc szerverterem`, `Miskolci Egyetem`. |
| Bacs-Kiskun / Kecskemet | `Mercedes`, `Kecskemet ipari park`, `szerverterem`, `adatkozpont`. |
| Bekes / Bekescsaba | `Bekescsaba szerverterem`, `onkormanyzat adatkozpont`, `isp hosting`. |
| Somogy / Kaposvar | `Kaposvar szerverterem`, `ipari park`, `university IT`. |
| Nograd / Salgotarjan | `Salgotarjan szerverterem`, `Nograd adatkozpont`, low-yield negative-control. |
| Veszprem | `Veszprem szerverterem`, `Pannon Egyetem`, `ipari park`. |
| Sopron / Nagykanizsa / Hodmezovasarhely | local ISP + university/municipal server-room terms; likely low-yield unless official/operator evidence appears. |

---

## 5. Verification workflow and grading

1. Start with operator/directories to build seed names and addresses.
2. Confirm active facility existence through an official operator page, procurement record, NMHH permit, CERN/EuroHPC/university page, or local permit.
3. Normalize exact municipality and division. Many "Budapest" market listings physically belong to Pest county.
4. Classify facility type:
   - `commercial_colocation`
   - `telecom_datacenter`
   - `hosting_provider_facility`
   - `public_sector_datacenter`
   - `research_hpc`
   - `enterprise_campus_server_room`
   - `planned_ai_energy_campus`
5. Capture evidence-specific capacity only. Do not mix rack count, gross sqm, technical sqm, facility power, generator power, IT load, and MVA.
6. Upgrade a directory lead above C only after one primary confirmation. Upgrade a press lead above B only after operator/official confirmation.
7. For cloud/hyperscaler mentions, count only official region/local-zone/host-facility records. Sales offices, meetups, partner events, and CDN PoPs are context, not datacenters.

High-risk false positives:

- `adatkozpont` can mean database/data hub, not a physical datacenter.
- `szerverterem` can mean a small room inside an office, school, hospital, or factory.
- Government procurement often buys hardware for an existing datacenter rather than creating a new facility.
- Contractor references may omit owner, address, date, and scope; keep them **C** unless corroborated.
- Paks AI campus reports may cite LOI/mandate language. Treat as planned until permit/grid/land evidence appears.
