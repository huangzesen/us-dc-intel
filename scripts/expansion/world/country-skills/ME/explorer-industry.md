# ME Explorer Industry - Montenegro Operator, Vendor, Trade-Press, and Municipality Query Methodology

Date: 2026-08-12. Scope: Montenegro (ME), municipality-level datacenter enumeration. Angle: **industry/vendor-led discovery** for colocation providers, telecom/cloud operators, state/utility projects, cloud-region exclusion, trade press, associations, and local-language query patterns. Reliability grades: **A** = operator official page, government/primary source, public procurement, regulator, corporate announcement; **B** = reputable local/international trade press, contractor case study with named site; **C** = directory/marketplace/SEO listing, unclear reseller page, or unverified aggregate.

---

## 0. Market Frame

- Montenegro is a **small telecom and government-led market**, not a hyperscale public-cloud region market. Expect a short census of operator-owned colocation/disaster-recovery sites, telecom technical headquarters facilities, public-sector/internal micro data centers, and one or two planned state/utility projects.
- Highest-yield municipalities are **Podgorica**, **Bijelo Polje**, **Niksic/Nikšić**, **Pljevlja**, and **Zabljak/Žabljak**. The coastal municipalities produce many tourism/real-estate and cable/fiber hits, but no reliable public colo/datacenter cluster was found in this pass.
- Local language is essential. Search both English and Montenegrin/Serbian/Croatian variants: `data centar`, `data center`, `podatkovni centar`, `kolokacija servera`, `telehousing`, `server sala`, `rezervni data centar`, `disaster recovery`, `DR lokacija`, `agregat`, `UPS`, `ISO 27001`, `Tier III`.
- Treat `cloud`, `virtual data center`, `VPS`, and `hosting` pages as **service leads only** unless the page names a physical Montenegro facility, address, municipality, or operator-owned colocation room.
- Hyperscale cloud-region pages reviewed as exclusion sources: AWS, Azure, Google Cloud, and Oracle Cloud do not list a Montenegro public cloud region/local zone. Use these official vendor lists to rule out cloud-region enumeration, not to find municipal projects.

---

## 1. Priority Operator and Facility Sweep

### 1.1 Confirmed or High-Value Operator Seeds

| Operator / facility lead | URL / source surface | Municipality focus | Evidence use |
|---|---|---|---|
| Crnogorski Telekom colocation / Data Centar Podgorica | https://telekom.me/poslovni-korisnici/kolokacija-servera | Podgorica; Bijelo Polje DR | Grade A for Telekom's own colocation offering and named Podgorica/Bijelo Polje facility pair. Search exact address and filings for capacity validation. |
| Crnogorski Telekom new Podgorica data center | https://en.vijesti.me/vijesti/ekonomija/448821/otvoren-novi-i-savremeni-data-centar-crnogorskog-telekoma | Podgorica | Grade B local press for 2020 opening; pair with Telekom page for Grade A facility existence. |
| Crnogorski Telekom Bijelo Polje DR center | https://en.vijesti.me/news-b/economy-d/363390/Telekom-opened-a-data-center-in-Bijelo-Polje | Bijelo Polje | Grade B local press for 2011 opening and Deutsche Telekom standards. Confirm current status through Telekom colocation page and directories. |
| One Montenegro / former Telenor data center | https://en.vijesti.me/news-b/society/578019/technical-and-safety-standards-tailored-to-the-user-of-the-promo | Podgorica | Grade B for reported 2015 Podgorica build, 780 sqm and ISO 27001/27701 context. Search One/Telenor domains for official current service details. |
| IBT Telenor Data Centar THQ reference | https://ibt.co.me/projects/telenor-data-centar-thq/ | Podgorica | Grade B/C contractor evidence for fire/safety works at Telenor technical HQ data center. Use as facility corroboration, not capacity proof. |
| IBT Telenor Data Centar u Pljevljima reference | https://ibt.co.me/projects/telenor-data-centar-u-pljevljima/ | Pljevlja | Grade C/B contractor evidence for a Pljevlja data-center work package. Needs operator or permit confirmation before strong enumeration. |
| Tehnopolis Data Center | https://tehnopolis.me/en/data-center/ | Niksic | Grade A official incubator/innovation-center facility page; likely small business/R&D data center, not wholesale colo. |
| EPCG/CEDIS/CGES Consolidated Data Center | https://balkangreenenergynews.com/montenegros-epcg-dso-tso-to-establish-consolidated-data-center/ and https://montenegrobusiness.eu/montenegros-key-energy-companies-sign-agreement-for-consolidated-data-center-kdc-project/ | Niksic / Zeljezara Niksic industrial complex | Grade B trade/business press for planned utility-sector KDC project announced in 2025. Seek EPCG/CEDIS/CGES official releases and procurement records for Grade A. |
| Montenegro state Tier III data center by 4iG | https://www.4ig.hu/digitalization-projects-montenegro | Podgorica until exact site is known | Grade A 4iG corporate project page for state digitalization/data-centre scope; DCD/trade press can add Tier III and context. Exact municipality/site remains unconfirmed if not disclosed. |
| m:tel / MTEL cloud and virtual data center | https://mtel.me/poslovni/ | Podgorica likely, but verify | Service lead. Search `Virtual Data Centar`, `cloud`, `kolokacija`, `data centar`; count only if physical room/facility evidence is found. |
| BeeNET Montenegro / regional hosting network | https://beenet.rs/ | Podgorica lead | Service/operator lead. Some regional pages reference data centers in Belgrade, Vrsac and Podgorica; verify Montenegro legal entity and physical facility before counting. |
| Cikom / Central Bank DR micro data center | https://www.vijesti.me/vijesti/714521/cikom-osnova-inovacija-i-uspjeha-u-it-industriji-crne-gore-promo and https://ictcortex.me/cikom/ | Zabljak | Grade B profile/association lead for a Central Bank disaster-recovery micro data center built by Cikom. Treat as enterprise DR unless official Central Bank/procurement evidence is found. |

### 1.2 Operator Search Templates

```text
"{operator}" "Crna Gora" "data centar"
"{operator}" Montenegro "data center"
"{operator}" "kolokacija servera"
"{operator}" telehousing Montenegro
"{operator}" "Podgorica" "data centar"
"{operator}" "Bijelo Polje" "data centar"
"{operator}" "Niksic" OR "Nikšić" "data centar"
"{operator}" "Pljevlja" "data centar"
"{operator}" "ISO 27001" "data centar"
"{operator}" "Tier III" Montenegro
"{operator}" "agregat" "UPS" "data centar"
site:{operator-domain} "data centar"
site:{operator-domain} "kolokacija"
site:{operator-domain} "telehousing"
```

Targeted strings:

```text
"Crnogorski Telekom" "kolokacija servera"
"Crnogorski Telekom" "Data Centar Podgorica"
"Crnogorski Telekom" "Bijelo Polje" "data centar"
"Telekom CG" "TGD01" Podgorica
"Telenor" "Data Centar THQ"
"Telenor" "data centar" "Pljevljima"
"One Montenegro" "data centar" "Podgorica"
"Tehnopolis" "data center" "Niksic"
"EPCG" "CEDIS" "CGES" "Konsolidovani data centar"
"Zeljezara Niksic" "data centar"
"4iG" "Montenegro" "data centre" "Tier III"
"m:tel" "Virtual Data Centar" "Crna Gora"
"BeeNET" "Podgorici" "data centar"
"Cikom" "mikro data centar" "Zabljak"
```

---

## 2. Trade Press, Associations, and Directories

| Source | URL / query surface | Montenegro use | Grade |
|---|---|---|---|
| Vijesti | https://www.vijesti.me/ and English mirror https://en.vijesti.me/ | Best local press for Telekom Podgorica/Bijelo Polje, One/Telenor certifications, Cikom/Central Bank DR, and project announcements. | B |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Search for 4iG state data center and Montenegro regional project coverage. | B |
| Balkan Green Energy News | https://balkangreenenergynews.com/ | Utility and energy-sector digital infrastructure leads such as EPCG/CEDIS/CGES KDC. | B |
| Montenegro Business | https://montenegrobusiness.eu/ | English-language business reposts and project summaries; useful for entity names and dates, but verify with primary sources. | B/C |
| ICT Cortex | https://ictcortex.me/ | Montenegro ICT association/member ecosystem. Useful for Cikom, system integrators, cloud/hosting providers and member names. Not a facility registry. | B/C |
| Chamber of Economy of Montenegro / PKCG | https://www.privrednakomora.me/ | ICT-sector and investor ecosystem context; search for `data centar`, `digitalna infrastruktura`, `cloud`. | B/C |
| EKIP - Agency for Electronic Communications and Postal Services | https://ekip.me/ | Telecom operator context, networks, market reports, license/operator names. Usually not a datacenter registry. | A for regulator data |
| Public procurement / CEJN | https://cejn.gov.me/ | Search tenders for `data centar`, `serverska sala`, `kolokacija`, `DR lokacija`, `UPS`, `agregat`, `klimatizacija`. | A |
| Government of Montenegro | https://www.gov.me/ | State digitalization, MUP/law-enforcement, e-government, 4iG and public-sector data-center leads. | A |
| DataCenterMap Montenegro | https://www.datacentermap.com/montenegro/ | Directory seeds for Podgorica and Bijelo Polje, including Victoria Group/Telekom-style listings. Verify every listing. | C |
| Data Center Catalog Montenegro | https://datacentercatalog.com/montenegro | Directory backup for facility names and addresses; never final proof by itself. | C |
| Inflect | https://inflect.com/ | Address/power seed for Telekom CG TGD01 or other facilities. Treat capacity as third-party until confirmed. | C |

Trade and association queries:

```text
site:vijesti.me "data centar" "Crnogorski Telekom"
site:vijesti.me "data centar" "Telenor" OR "One Montenegro"
site:vijesti.me "data centar" "Cikom" OR "Centralna banka"
site:datacenterdynamics.com Montenegro "data center" OR "data centre"
site:balkangreenenergynews.com Montenegro "data center"
site:montenegrobusiness.eu Montenegro "data center" "EPCG" OR "4iG"
site:ictcortex.me "data centar" OR "data center"
site:privrednakomora.me "data centar" "Crna Gora"
site:ekip.me "data centar" OR "kolokacija"
site:gov.me "data centar" "Crna Gora"
site:cejn.gov.me "data centar" OR "serverska sala" OR "kolokacija"
```

---

## 3. Cloud Region and Vendor Exclusion Pass

Use official hyperscale location pages as **A-grade negative evidence** for public cloud regions:

```text
site:aws.amazon.com/about-aws/global-infrastructure/ Montenegro
site:azure.microsoft.com/en-us/explore/global-infrastructure/geographies Montenegro
site:cloud.google.com/about/locations Montenegro
site:oracle.com/cloud/public-cloud-regions/ Montenegro
```

As of this methodology pass, no AWS/Azure/GCP/OCI Montenegro public cloud region/local zone was identified. Montenegro projects are therefore more likely to surface through telecom operator pages, government digitalization contracts, utility-sector projects, local press, contractor references, and directories.

For non-hyperscale vendors/integrators, search:

```text
"Schneider Electric" "data centar" "Crna Gora"
"Vertiv" "data centar" "Crna Gora"
"Huawei" "data centar" "Crna Gora"
"Cisco" "data centar" "Crna Gora"
"Nutanix" "data centar" "Crna Gora"
"VMware" "Cikom" "Zabljak" "data centar"
"HP" "Centralna banka" "Zabljak" "data centar"
"protivpozarni sistem" "data centar" "Crna Gora"
"hladjenje" "data centar" "Crna Gora"
```

---

## 4. Municipality Enumeration Recipes

### 4.1 Universal Municipality Sweep

Run for every municipality in the manifest, using both ASCII and diacritic variants where applicable.

```text
"{municipality}" "Crna Gora" "data centar"
"{municipality}" Montenegro "data center"
"{municipality}" Montenegro "data centre"
"{municipality}" "podatkovni centar"
"{municipality}" "kolokacija servera"
"{municipality}" "server sala"
"{municipality}" "rezervni data centar"
"{municipality}" "disaster recovery" Montenegro
"{municipality}" "DR lokacija"
"{municipality}" "ISO 27001" "data centar"
"{municipality}" "Tier III" "data centar"
"{municipality}" "UPS" "agregat" "data centar"
site:gov.me "{municipality}" "data centar"
site:cejn.gov.me "{municipality}" "data centar" OR "serverska sala"
site:vijesti.me "{municipality}" "data centar"
```

### 4.2 High-Yield Municipalities

**Podgorica** - highest priority. Search telecom HQs, state projects, government tenders, BeeNET/m:tel/One/Telekom, and 4iG.

```text
"Podgorica" "data centar" "Crnogorski Telekom"
"Podgorica" "kolokacija servera" Telekom
"Podgorica" "Telenor" "data centar"
"Podgorica" "One Montenegro" "data centar"
"Podgorica" "m:tel" "Virtual Data Centar"
"Podgorica" "BeeNET" "data centar"
"Podgorica" "4iG" "data centre"
"Podgorica" "drzavni data centar" OR "državni data centar"
"Podgorica" "serverska sala" "javna nabavka"
```

**Bijelo Polje** - Telekom disaster-recovery center is the main known lead.

```text
"Bijelo Polje" "data centar" "Crnogorski Telekom"
"Bijelo Polje" "rezervni data centar"
"Bijelo Polje" "disaster recovery" Telekom
"Data Centar Bijelo Polje"
"Victoria Group Bijelo Polje" "data center"
```

**Niksic / Nikšić** - Tehnopolis and utility consolidated data-center project.

```text
"Nikšić" "data centar" OR "Niksic" "data center"
"Tehnopolis" "data center" "Nikšić"
"Zeljezara Nikšić" "data centar"
"Željezara Nikšić" "Konsolidovani data centar"
"EPCG" "CEDIS" "CGES" "Nikšić" "data centar"
```

**Pljevlja** - contractor-lead Telenor facility; verify heavily.

```text
"Pljevlja" "data centar" "Telenor"
"Pljevljima" "data centar" "Telenor"
"Telenor Data Centar u Pljevljima"
"Pljevlja" "One Montenegro" "data centar"
"Pljevlja" "serverska sala" "UPS" "agregat"
```

**Zabljak / Žabljak** - Central Bank/Cikom DR micro data-center lead.

```text
"Žabljak" "mikro data centar"
"Zabljak" "micro data center" "Cikom"
"Centralna banka" "Žabljak" "data centar"
"Cikom" "Žabljak" "DCIM"
"Cikom" "Zabljak" "disaster recovery"
```

### 4.3 Medium- and Low-Yield Municipalities

For **Bar, Budva, Herceg-Novi/Herceg Novi, Kotor, Tivat, Ulcinj**, include port, submarine-cable, hotel/casino, marina and smart-city false positives but require physical facility evidence:

```text
"{municipality}" "data centar" "telekom"
"{municipality}" "server sala" hotel OR casino OR marina
"{municipality}" "kolokacija" Montenegro
"{municipality}" "submarine cable" "data center"
"{municipality}" "digitalna infrastruktura" "data centar"
```

For **Andrijevica, Berane, Cetinje, Danilovgrad, Kolasin/Kolašin, Mojkovac, Plav, Pluzine/Plužine, Rozaje/Rožaje, Savnik/Šavnik, Gusinje, Petnjica, Tuzi, Zeta**, a compact sweep is usually enough unless a procurement, utility, or telecom lead appears:

```text
"{municipality}" "data centar" "Crna Gora"
"{municipality}" "serverska sala"
"{municipality}" "javna nabavka" "UPS" OR "agregat"
"{municipality}" "telekomunikacioni objekat" "data centar"
```

Diacritic/variant handling:

```text
Niksic OR Nikšić
Zabljak OR Žabljak
Kolasin OR Kolašin
Pluzine OR Plužine
Rozaje OR Rožaje
Savnik OR Šavnik
Herceg-Novi OR Herceg Novi
```

---

## 5. Directory-to-Primary Verification Workflow

1. Seed from DataCenterMap, Data Center Catalog, Inflect, Cloudscene/PeeringDB if available, and contractor project pages.
2. Search the exact facility/operator string on the operator's official domain.
3. Search Montenegrin press (`Vijesti`, `CDM`, `Bankar.me`, `Investitor.me`, `Pobjeda`, `RTCG`) for opening/certification/project history.
4. Search CEJN/public procurement for construction, colocation, UPS, generator, cooling, fire suppression, and DR tenders.
5. Search GOV.ME and ministry pages for state data-center projects, especially `MJU`, `MUP`, `digitalizacija`, `e-uprava`, `4iG`.
6. Search EKIP and telecom market reports to confirm operator identity and active telecom status.
7. If still directory-only, record as Grade C and explicitly name missing proof: current operator page, address, permit/procurement, or opening announcement.

Directory queries:

```text
site:datacentermap.com/montenegro "{operator}" OR "{municipality}"
site:datacentercatalog.com/montenegro "{operator}" OR "{municipality}"
site:inflect.com Montenegro "{operator}" "data center"
site:peeringdb.com Montenegro "{operator}"
site:cloudscene.com Montenegro "{operator}" "data center"
```

---

## 6. Capacity and Status Extraction

- Montenegro sources rarely disclose MW. Preserve disclosed proxies instead of inventing capacity: square meters, rack count, certified standards, redundancy tier, ISO certificates, UPS/generator/fire-suppression scope, and project value.
- For Telekom Podgorica, third-party directory capacity such as `150 kW` should remain Grade C unless confirmed by Telekom or primary filings.
- For One/Telenor Podgorica, `780 square meters` and ISO certificate details from Vijesti are useful B-grade capacity/quality proxies.
- For 4iG and EPCG/CEDIS/CGES projects, status should remain `planned` until procurement, government acceptance, operator opening, or site-specific construction evidence appears.
- For Tehnopolis and Cikom/Central Bank, classify as small R&D/enterprise/internal data-center facilities unless a commercial colocation offer or measurable IT load is proven.

Capacity queries:

```text
"{facility}" "MW" OR "MVA" OR "kW"
"{facility}" "m2" OR "m²" OR "kvadrata"
"{facility}" "rack" OR "ormar"
"{facility}" "Tier III" OR "TIER 3"
"{facility}" "ISO 27001" OR "ISO 27701"
"{facility}" "UPS" OR "agregat" OR "dizel agregat"
"{facility}" "protivpožarni" OR "protivpozarni"
"{facility}" "investicija" "EUR" OR "miliona"
```

---

## 7. Known Seed List for Later Validation

This is a methodology seed list, not a final census. Re-check every item during enumeration.

| Seed | Municipality | Status tendency | Best evidence path |
|---|---|---|---|
| Crnogorski Telekom Data Centar Podgorica / Telekom CG TGD01 | Podgorica | Operational | Telekom official colocation page + Vijesti 2020 opening + directory capacity cross-check |
| Crnogorski Telekom Bijelo Polje DR Data Center | Bijelo Polje | Operational | Vijesti 2011 opening + Telekom official colocation page |
| One Montenegro / former Telenor Podgorica data center | Podgorica | Operational | Vijesti 2021 profile + One/Telenor official pages + IBT THQ contractor reference |
| Telenor Data Centar u Pljevljima | Pljevlja | Operational lead | IBT contractor page; seek One/Telenor or procurement corroboration |
| Tehnopolis Data Center | Niksic | Operational | Tehnopolis official page + local/EU project press |
| EPCG/CEDIS/CGES Consolidated Data Center at Zeljezara Niksic | Niksic | Planned | EPCG/CEDIS/CGES releases, Balkan Green Energy News, Montenegro Business |
| Montenegro state Tier III data center by 4iG | Podgorica placeholder | Planned | 4iG corporate project page + GOV.ME/MUP procurement + DCD |
| BeeNET Podgorica facility lead | Podgorica | Unverified service/facility lead | BeeNET official/regional pages + Montenegrin company/address proof |
| m:tel/MTEL physical data-center lead | Podgorica likely | Unverified service/facility lead | MTEL official pages + procurement/operator evidence |
| Central Bank DR micro data center by Cikom | Zabljak | Operational internal/enterprise lead | Vijesti/Cikom/ICT Cortex profile + Central Bank procurement confirmation |
