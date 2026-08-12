# SI Explorer Industry - Slovenia Trade Press, Operators, Directories, and Statistical-Region Query Patterns

Date: 2026-08-12. Scope: Slovenia datacenter enumeration methodology focused on industry/trade press, operator/vendor seeds, English and Slovenian search patterns, and statistical-region sweeps. Reliability grades: **A** = official/primary or operator-owned current page, **B** = established trade press/association/contractor case study, **C** = aggregator/directory/market snippet.

---

## 0. Market frame

- Slovenia is a small market. Expect a census made of **many small colocation, telecom, public-sector, research/HPC and enterprise data rooms**, not a large hyperscale region pipeline. Hyperscale cloud-region pages reviewed for AWS, Azure, Google Cloud and Oracle do not show a Slovenia public cloud region/local zone; use them only to rule out cloud-region driven enumeration.
- The practical industry pipeline is: **directory/trade/operator lead -> operator page or official government/procurement page -> PIS construction act -> municipal/environment/energy cross-check -> AKOS/fiber context**.
- Known market clusters from public directories and official announcements are **Ljubljana**, **Maribor**, **Nova Gorica**, **Koper**, and a smaller set of company/industrial facilities such as Kranj or Sostanj. DataCenterMap currently lists Slovenia facilities in 4 markets: Ljubljana, Maribor, Nova Gorica and Koper (directory grade C).
- Slovenian pages use `podatkovni center` and `kolokacija`; English pages often use `data centre`, `data center`, `colocation`, `cloud`, `HPC`, `AI Factory`, `modular data center`.
- Be strict about false positives. Slovenian government has many "podatkovni portal", "podatkovna baza" and analytics pages that are not physical data centers. Corporate pages selling virtual private clouds are service leads only unless a physical site is named.

---

## 1. Industry, association, and trade-press sources

### 1.1 Slovenian and regional industry sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| DATA CENTER conference by Palsit | https://datacenter.palsit.com/en | Local data-center industry ecosystem, sponsors, speakers, facility-management vendors and Slovenian-language terms. Not a facility registry. | B/C |
| DCD - Data Center Dynamics | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Slovenia data center ARNES Posta Ljubljana Maribor` | Best international trade-press feed for ARNES Maribor, Posta/Ministry handover, University of Ljubljana modular DC, and regional project writeups. Verify with GOV.SI/operator/procurement. | B |
| The Slovenia Times / STA syndication | Query `"Slovenia Times" "data centre" "Maribor" ARNES` and `"Slovenia Times" "data center" "Posta Slovenije"` | Often source for English-language public-sector DC announcements. Verify against GOV.SI and operator pages. | B |
| Finance.si | Query `site:finance.si "podatkovni center" "Pošta Slovenije" OR Arnes OR Ljubljana` | Slovenian business press; useful for capacity/finance/launch detail, sometimes paywalled. | B/C |
| Monitor.si / Racunalniske novice / IKT-informator | `site:monitor.si "podatkovni center"`, `site:racunalniske-novice.com "podatkovni center"` | IT press and historical facility mentions; verify with operator/public records. | B/C |
| PostEurop | https://www.posteurop.org/blog/posta-slovenije-accelerates-expansion-of-data-centre-capacities/ | Useful corroboration for Posta Slovenije/Posita public-sector expansion and ministry handover. | B |
| EU / EuroHPC / EuroCC / SLING pages | Queries: `"Slovenian AI Factory" SLAIF data center Maribor`, `site:eurohpc-ju.eu Slovenia AI Factory`, `site:sling.si Maribor data center` | Research/HPC/AI Factory leads, funding, equipment, status. Verify with ARNES/GOV.SI. | A/B depending on issuer |
| Engineering/contractor references | NTR, Resalta, Siemens Energy, APC/Schneider, HVAC/security/fire contractors; query `"podatkovni center" "referenca" "{operator}"` | Often reveals small enterprise/industrial data centers absent from directories. | B |

### 1.2 Aggregators and directories

| Source | URL | Use | Grade |
|---|---|---|---|
| DataCenterMap Slovenia | https://www.datacentermap.com/slovenia/ | Broadest public facility seed list; as of review, lists 20 data centers in Ljubljana, Maribor, Nova Gorica, Koper. Use only as lead source. | C+ |
| DataCenterMap Ljubljana | https://www.datacentermap.com/slovenia/ljubljana/ | Facility/address seeds for Ljubljana: Posita, Perftech, Telemach, MegaTel, Softnet, Akton, Datacenter.si, ARNES, etc. | C+ |
| Cloudscene Ljubljana | https://cloudscene.com/market/data-centers-in-slovenia/ljubljana | Market-size and ecosystem indicators; useful for provider names, not authoritative for exact current status. | C+ |
| Datacenters.com Slovenia | https://www.datacenters.com/locations/slovenia | Commercial lead directory, useful for provider aliases and address hints. | C |
| Inflect Slovenia | https://inflect.com/datacenters/emea/slovenia | Facility/address/network lead directory. | C |
| Baxtel Slovenia/Ljubljana | https://baxtel.com/data-center/slovenia and https://baxtel.com/data-center/ljubljana | More conservative facility list; useful for ARNES research DCs and power snippets, but incomplete for commercial colo. | C+ |
| PeeringDB | https://www.peeringdb.com/ | Confirms active networks/facilities/IXP presence when facility records exist. Use for interconnection, not construction status. | B/C |

Directory caution: directory listings often mix physical data centers, cloud-service brands, interconnection locations, offices and customer-managed server rooms. Every C-grade lead needs an operator, PIS, government, procurement or strong trade-press confirmation.

---

## 2. Operator and facility seed list

Operator pages are **A for self-reported service/facility existence**, **B for capacity/service claims**, and not proof of construction status unless paired with an official opening, permit, procurement, or use permit.

### 2.1 Public-sector, research, and government operators

- **ARNES (Academic and Research Network of Slovenia)** - existing Ljubljana/SIX and Jožef Stefan/Technology Park infrastructure plus new Maribor data center. Official Maribor page: https://www.arnes.si/en/the-first-arnes-data-centre-of-the-future-will-be-located-in-maribor/ . GOV.SI groundbreaking/news: https://www.gov.si/novice/2025-05-06-odkrit-temeljni-kamen-za-arnesov-podatkovni-center-maribor/ and https://www.gov.si/novice/2025-05-06-slovenija-vstopa-v-digitalno-prihodnost-postavljen-temeljni-kamen-za-nov-podatkovni-center/ . e-JN tender seed: `JN003755/2024-EUe16/01`, `Podatkovni center Arnes - lokaciji Maribor in Ljubljana`. Grade A/B.
- **Ministry of Digital Transformation / Posta Slovenije / Posita** - GOV.SI confirms new Ljubljana postal-logistics-centre data center handed to the ministry on 2025-09-30: https://www.gov.si/novice/2025-09-30-posta-slovenije-ministrstvu-za-digitalno-preobrazbo-predala-v-uporabo-nov-podatkovni-center/ . Posita official service page: https://www.posita.si/storitve/podatkovni-center/ . Posta/Posita facility page with Ljubljana Vic and Maribor Tezno/Center capacities: https://www.posta.si/posita-podatkovni-centri . Grade A.
- **University of Ljubljana / Faculty of Computer and Information Science** - DCD reported a modular/containerized data center in 2025; University official page says the Faculty signed an agreement for a high-density hybrid data center: https://www.uni-lj.si/en/news/2025-03-14-the-university-of-ljubljana-will-play-a-key-role-in-establishing-the-slovenian-artificial-intelligence-factory . Verify with procurement/PIS and faculty pages. Grade A/B.
- **IZUM / SLING / Slovenian AI Factory (SLAIF)** - tied to ARNES Maribor and EuroHPC/AI Factory context. Use for project scope and timeline; physical facility remains ARNES Maribor unless separate site evidence appears. Grade A/B.

### 2.2 Commercial colocation, telecom, and IT operators

- **Datacenter.si / RVO** - official page lists colocation at Ljubljana Technology Park 18 - SIX and Ljubljana Center: https://datacenter.si/ and Slovenian page https://datacenter.si/index.sl.html . Grade A for service/facility claim; verify exact legal entity and PIS/address.
- **Posta Slovenije / Posita** - commercial/government DC services. Official pages: https://www.posita.si/storitve/podatkovni-center/ and https://www.posta.si/posita-podatkovni-centri . Grade A.
- **T-2** - official colocation page says customer ICT equipment is hosted in T-2's data center, with rack/power pricing and UPS/cooling/SLA: https://www.t-2.net/gostovanje-kolokacije . Grade A for service; search PIS/operator records for physical site.
- **Telekom Slovenije** - official virtual data center/cloud services: https://www.telekom.si/poslovni/it-in-oblacne-storitve/upravljane-storitve/najem-virtualnega-podatkovnega-centra . Service lead; verify physical sites through directories, AKOS, procurement and operator documents. Grade B unless facility named.
- **A1 Slovenija** - telecom/cloud services. Search official domain for `podatkovni center`, `kolokacija`, `oblak`, `data center`. Use AKOS for operator context. Grade B until a facility page is found.
- **Telemach** - DataCenterMap lists Telemach DC1/DC2 in Ljubljana; verify with Telemach official pages, AKOS and PIS before counting. Grade C until confirmed.
- **SoftNET** - directory leads include Ljubljana and Koper DCs, and SoftNET is an AKOS-listed telecom operator. Official site is https://www.softnet.si/ ; search official pages for `data center`, `podatkovni center`, `kolokacija`. Grade C/B depending on confirmation.
- **MEGA M / MegaTel** - DataCenterMap lists MegaTel facilities in Ljubljana; AKOS reference-offer page lists MEGA M among telecom operators. Verify with operator pages and PIS. Grade C/B.
- **PERFTECH, Akton, Mikrocop, NIL/Conscia, Kontron Slovenia** - IT/cloud/security operators and integrators that may have facility or customer data-center leads. Use as query pivots, but do not count service pages as physical sites without a facility/address/project record.
- **Arctur** - Nova Gorica HPC/cloud/data-center lead from directories and company context; verify with official Arctur pages, PIS and Nova Gorica municipal records.
- **Industrial/utility data centers** - examples can appear in contractor references, e.g., power-plant or enterprise server rooms. Count only if the reference describes a physical data center with location and completed works.

Operator query templates:

```text
"{operator}" "podatkovni center" Slovenija
"{operator}" "kolokacija" Slovenija
"{operator}" "data center" Slovenia
"{operator}" "Ljubljana" "podatkovni center"
"{operator}" "Maribor" "podatkovni center"
"{operator}" "referenca" "podatkovni center"
site:{operator-domain} "podatkovni center"
site:{operator-domain} "kolokacija"
site:{operator-domain} "data center"
site:pis.eprostor.gov.si/pis-ua-jv "{legal_entity}"
site:akos-rs.si "{operator}"
```

---

## 3. Core Slovenia query patterns

### 3.1 National sweep

```text
"podatkovni center" Slovenija "MW" OR "kVA" OR "MVA"
"podatkovni center" Slovenija "gradnja" OR "otvoritev" OR "predaja v uporabo"
"podatkovni center" "Ljubljana" "Maribor" "Koper" "Nova Gorica"
"podatkovni center" "odvecna toplota" Slovenija
"podatkovni center" "transformatorska postaja" Slovenija
"kolokacija" "podatkovni center" Slovenija
"strezniska soba" "UPS" "agregat" Slovenija
"Slovenia" "data center" "colocation" Ljubljana Maribor Koper
"Slovenia" "data centre" "AI Factory" Maribor
"Slovenia" "data center" "postal logistics center" Ljubljana
```

### 3.2 Trade and press sweep

```text
site:datacenterdynamics.com Slovenia "data center"
site:datacenterdynamics.com Slovenia ARNES OR Posta OR Ljubljana OR Maribor
site:finance.si "podatkovni center" "Pošta Slovenije" OR Arnes
site:monitor.si "podatkovni center"
site:racunalniske-novice.com "podatkovni center"
site:sta.si "podatkovni center" "Maribor" OR "Ljubljana"
site:sloveniatimes.com "data centre" Slovenia
site:posteurop.org "Slovenia" "data centre" "Posta Slovenije"
site:palsit.com "podatkovni center" OR "Data Center"
```

### 3.3 Contractor/reference sweep

```text
"podatkovni center" "referenca" "Slovenija"
"podatkovni center" "projektiranje" "Slovenija"
"podatkovni center" "izgradnja" "Slovenija"
"podatkovni center" "hlajenje" "referenca"
"podatkovni center" "UPS" "referenca"
"podatkovni center" "agregat" "referenca"
"data center cooling project" Slovenia
"modular data center" Slovenia NTR
"kontejnerski podatkovni center" Slovenija
```

### 3.4 Negative filters

Exclude or downgrade:

```text
"podatkovni portal"
"podatkovna baza"
"center za podatke" statistics-only
"virtualni podatkovni center" without physical site
"cloud partner" without facility/address
"pisarna" OR "office" only
"data center services" with no location
```

---

## 4. Statistical-region industry sweeps

Use both Slovenian names with diacritics and ASCII fallbacks. Add municipalities/cities from the project manifest as `{municipality}`.

### 4.1 Osrednjeslovenska / Central Slovenia

Primary markets: Ljubljana, Trzin, Domzale, Vrhnika, Logatec, Grosuplje. Highest density of telecom, colocation, SIX/IXP, state and university sites.

Seed operators: ARNES/SIX, Datacenter.si, Posita/Posta, T-2, Telekom Slovenije, Telemach, SoftNET, MegaTel/MEGA M, Akton, Perftech, Mikrocop, NIL/Conscia, University of Ljubljana.

```text
"Ljubljana" "podatkovni center" kolokacija
"Ljubljana" "data center" colocation "Slovenia"
"Tehnoloski park 18" "podatkovni center" OR SIX
"Cesta v Mestni log 81" "podatkovni center"
"Tivolska cesta 50" "data center" OR "podatkovni center"
"Vojkova 58" "data center" OR "podatkovni center"
"Brnciceva" Telemach "data center"
"Trzin" SoftNET "podatkovni center" OR kolokacija
"Univerza v Ljubljani" "modularni podatkovni center"
```

### 4.2 Podravska / Drava

Primary markets: Maribor, Tezno, Ptuj. Strong official ARNES/AI Factory and Posta/Posita evidence.

Seed operators/projects: ARNES Maribor, SLAIF/EuroHPC, Posta Slovenije/Posita Maribor Tezno and Maribor Center, IZUM, University of Maribor.

```text
"Maribor" "podatkovni center" Arnes
"Arnesov podatkovni center Maribor"
"Slovenian AI Factory" Maribor "data center"
"Maribor" "odvecna toplota" "podatkovni center"
"Posta Slovenije" "Maribor Tezno" "podatkovni center"
"IZUM" "podatkovni center" "Maribor"
"Univerza v Mariboru" "podatkovni center"
```

### 4.3 Goriska / Gorizia

Primary market: Nova Gorica. Smaller but known in directories through cloud/HPC/service-provider leads.

Seed operators/projects: Arctur, municipal/public-sector IT, cross-border Trieste/Nova Gorica connectivity.

```text
"Nova Gorica" "podatkovni center"
"Nova Gorica" "data center" Arctur
"Arctur" "podatkovni center" OR "data center"
"Sempeter-Vrtojba" "podatkovni center"
"Ajdovscina" "podatkovni center" OR "strezniska"
```

### 4.4 Obalno-kraska / Coastal-Karst

Primary market: Koper; include Izola, Piran, Ankaran, Sezana for port/logistics and cross-border telecom leads.

Seed operators/projects: SoftNET Koper directory lead, port/logistics IT, cross-border Trieste interconnect.

```text
"Koper" "podatkovni center" OR "data center"
"SoftNET Koper DC" OR "Vojkovo nabrezje 30"
"Luka Koper" "podatkovni center" OR "strezniska"
"Izola" "podatkovni center"
"Piran" "podatkovni center"
"Sezana" "podatkovni center" OR "data center"
```

### 4.5 Gorenjska / Upper Carniola

Primary market: Kranj. Expect enterprise/telecom/vendor data rooms rather than public colo campuses.

Seed operators/projects: Kontron Slovenia/Iskratel, telecom nodes, industrial IT.

```text
"Kranj" "podatkovni center"
"Kranj" "data center" Iskratel OR Kontron
"Iskratel" "data center cooling project" Kranj
"Kontron Slovenia" "podatkovni center"
"Skofja Loka" "podatkovni center"
"Jesenice" "podatkovni center"
```

### 4.6 Savinjska / Savinja

Primary markets: Celje, Velenje, Sostanj. Focus on industrial/utility facilities and telecom.

Seed operators/projects: power/utility server rooms, Mega M headquartered in Velenje, TE Sostanj contractor-reference leads.

```text
"Celje" "podatkovni center" OR "kolokacija"
"Velenje" "podatkovni center" "Mega M" OR MegaTel
"Sostanj" "podatkovni center" OR "data center"
"Termoelektrarna Sostanj" "podatkovni center"
"Savinja" "data center" Slovenia
```

### 4.7 Jugovzhodna Slovenija / Southeast Slovenia

Primary markets: Novo mesto, Kocevje, Crnomelj, Trebnje. Expect public-sector and enterprise server rooms.

```text
"Novo mesto" "podatkovni center"
"Novo mesto" "strezniska soba" "UPS"
"Kocevje" "podatkovni center"
"Crnomelj" "podatkovni center"
"Trebnje" "podatkovni center"
```

### 4.8 Pomurska / Mura

Primary markets: Murska Sobota, Lendava, Gornja Radgona. Lower probability; check municipal and telecom/service providers.

```text
"Murska Sobota" "podatkovni center"
"Murska Sobota" "strezniska soba"
"Lendava" "podatkovni center"
"Gornja Radgona" "podatkovni center"
```

### 4.9 Koroska / Carinthia

Primary markets: Slovenj Gradec, Ravne na Koroskem, Dravograd. Lower probability; focus on public-sector, hospital/utility and industry.

```text
"Slovenj Gradec" "podatkovni center"
"Ravne na Koroskem" "podatkovni center"
"Dravograd" "podatkovni center"
"Koroska" "podatkovni center" Slovenija
```

### 4.10 Posavska / Lower Sava

Primary markets: Krsko, Brezice, Sevnica. Energy/industrial region; require direct IT-facility evidence.

```text
"Krsko" "podatkovni center"
"Brezice" "podatkovni center"
"Sevnica" "podatkovni center"
"Posavje" "podatkovni center" Slovenija
"NEK" "podatkovni center" OR "strezniska"
```

### 4.11 Primorsko-notranjska / Littoral-Inner Carniola

Primary markets: Postojna, Ilirska Bistrica, Cerknica. Lower probability; search logistics, public-sector, and industrial zones.

```text
"Postojna" "podatkovni center"
"Ilirska Bistrica" "podatkovni center"
"Cerknica" "podatkovni center"
"Primorsko-notranjska" "data center"
```

### 4.12 Zasavska / Central Sava

Primary markets: Trbovlje, Hrastnik, Zagorje ob Savi. Lower probability; search industrial redevelopment and public-sector IT.

```text
"Trbovlje" "podatkovni center"
"Hrastnik" "podatkovni center"
"Zagorje ob Savi" "podatkovni center"
"Zasavje" "podatkovni center"
```

---

## 5. Known lead examples to seed validation

These are not a final facility list; they are starting pivots for official validation.

| Lead | Region / municipality | Source examples | How to validate |
|---|---|---|---|
| ARNES Maribor data center / Slovenian AI Factory | Podravska / Maribor | ARNES official page; GOV.SI 2025 groundbreaking; DCD; e-JN `JN003755/2024-EUe16/01` | PIS `GD/PG/UD`, Maribor municipal docs, ARNES updates, procurement award/completion, ELES/Energetika Maribor waste-heat docs |
| Posta Slovenije / Posita new Ljubljana DC for Ministry | Osrednjeslovenska / Ljubljana | GOV.SI 2025-09-30 handover; Posta/Posita pages; DCD/PostEurop | PIS, Posta/Posita official facility page, ministry procurement/lease docs, logistics-centre address |
| Posita Ljubljana Vic / Maribor Tezno / Maribor Center | Osrednjeslovenska and Podravska | Posta official page lists locations/capacities; Posita service page | Operator page is strong; cross-check PIS and procurement for expansions |
| Datacenter.si Ljubljana Technology Park/SIX and Ljubljana Center | Osrednjeslovenska / Ljubljana | Official Datacenter.si page | Verify legal entity, address, ARNES/SIX relation, PIS if expansion |
| T-2 colocation | Likely Osrednjeslovenska / Ljubljana | Official T-2 colocation pricing/service page | Identify physical site through operator docs, AKOS, PIS, directories |
| University of Ljubljana modular/high-density DC | Osrednjeslovenska / Ljubljana | University official AI Factory role page; DCD; contractor/procurement leads | Faculty procurement, PIS/start notification, rooftop/modular permit rules |
| SoftNET Koper/Ljubljana leads | Obalno-kraska and Osrednjeslovenska | DataCenterMap/Inflect/ColoMap; AKOS operator context | Need SoftNET official confirmation or PIS/address evidence |
| Arctur / Nova Gorica | Goriska / Nova Gorica | Directory/company lead | Verify official Arctur pages, PIS, Nova Gorica municipality |
| Iskratel/Kontron Kranj data-center cooling project | Gorenjska / Kranj | Contractor case-study/reference leads | Verify whether it is an enterprise data center only, and capture status/capacity as internal facility if in scope |
| TE Sostanj industrial data center | Savinjska / Sostanj | Contractor reference leads | Treat as internal/industrial DC; verify with operator/contractor and exclude from commercial colo count if scope requires |

---

## 6. Reliability and status resolution

Status labels:

- `operational`: operator/government handover/opening, use permit (`UD`), active colocation page, or completed contractor reference.
- `under_construction`: PIS start notification (`PG`), official groundbreaking, active construction procurement with site confirmation.
- `planned/permitted`: building permit (`GD`), OPN/OPPN with named investor, procurement design/build notice before award, or official project approval.
- `lead-only`: directory, trade article, cloud-service page, AKOS telecom context, or market-report mention without physical confirmation.
- `no_project`: targeted English + Slovenian searches and directories return no facility/project evidence for the municipality.

Minimum fields to store from industry leads:

- facility/project name and alias;
- operator/developer/legal entity;
- municipality, city/address, statistical region, cadastral/parcel if later found;
- status and status evidence date;
- source URLs and grade;
- capacity in kW/kVA/MVA/MW or rack count only when sourced;
- whether facility is commercial colo, telecom, public-sector, research/HPC, enterprise/internal, or cloud-region logical presence.

Do not count:

- cloud reseller/service offerings without a physical Slovenian facility;
- company headquarters or branch offices;
- data/statistics portals;
- ordinary server rooms unless the project scope includes enterprise/internal rooms and the evidence names a physical data center/server-room build.
