# ME Explorer Official - Montenegro Datacenter Enumeration via Planning, Energy, EKIP, Cloud, and Trade Sources

Date: 2026-08-12. Scope: Montenegro (ME), municipality-level enumeration. Angle: **official/regulatory/cloud-first methodology** for finding operational, planned, and proposed datacenter facilities. Reliability grades: **A** = official/primary source (planning/permit authority, municipality, environmental authority, energy regulator/grid/operator, EKIP, operator official page, cloud-provider official region page), **B** = strong trade press or named-party business press, **C** = directory/aggregate/marketing-only lead.

---

## 0. Montenegro-specific frame

- Montenegro has no public national datacenter registry. Build the census by joining **Ministry of Spatial Planning, Urbanism and State Property permit indexes**, municipal planning/permit pages, public procurement, **EKIP** telecom evidence, **REGAGEN/CGES/CEDIS/EPCG** energy records, operator pages, official cloud-region lists, and trade press.
- Construction evidence is split between state and municipal sources. The national ministry publishes `urbanističko-tehnički uslovi` (UTU), `građevinske dozvole`, and related decisions at https://www.gov.me/mdup/urbanisticko-tehnicki-uslovi/urbanisticko-tehnicki-uslovi and https://www.gov.me/mdup/urbanisticko-tehnicki-uslovi/gradevinske-dozvole . Municipal pages publish local UTU/building/use-permit scans and year indexes, especially Podgorica, Bar, Kotor, and Nikšić.
- The key local terms are **Montenegrin/BCS**, not English: `data centar`, `državni data centar`, `konsolidovani data centar`, `kolokacija`, `server sala`, `računarski centar`, `cloud usluge`, `virtual data centar`, `građevinska dozvola`, `upotrebna dozvola`, `urbanističko-tehnički uslovi`, `trafostanica`, `agregat`, `UPS`, `hlađenje`.
- Current high-confidence physical leads are small-market and telecom/government/utility focused, not hyperscale: Crnogorski Telekom's Data Centar Podgorica, One Montenegro's carrier-neutral data center, state-government data-center/disaster-recovery planning, and the EPCG/CEDIS/CGES Consolidated Data Center at the Nikšić steelworks complex. Directory-only leads such as old Victoria Group listings require primary confirmation before counting.
- There is no official AWS/Azure/GCP/OCI public cloud region in Montenegro in the official region lists checked for this methodology pass. Treat local `cloud` or `virtual data centar` services as hosted/colo/cloud-service offerings unless a hyperscaler official page names Montenegro.

Lifecycle vocabulary:

`prostorni plan/DUP/LSL` < `UTU/urbanističko-tehnički uslovi` < `idejno rješenje/saglasnost glavnog arhitekte` < `građevinska dozvola/odobrenje za građenje` < `prijava radova/izvođenje radova` < `upotrebna dozvola` < `otvoren/pušten u rad/operativan`

Use planning and strategic documents as leads. Promote to strong facility evidence only with a building/use permit, official operator opening/tender, official government decision, official energy-company project note, or official telecom/regulator record that names a site.

---

## 1. Core query vocabulary

### 1.1 Montenegrin/local-language terms

```text
"data centar" +"Crna Gora"
"data centra" +"Crna Gora"
"državni data centar"
"Državni Data centar" "Disaster Recovery"
"konsolidovani Data Centar"
"KDC" "Željezara Nikšić"
"server sala" OR "serverska sala"
"računarski centar"
"kolokacija" OR "kolokacijski prostor"
"carrier neutral" "data centar"
"cloud usluge" "data centar"
"virtual data centar"
"agregat" "data centar"
"UPS" "data centar"
"hlađenje" "data centar"
"trafostanica" "data centar"
"građevinska dozvola" "data centar"
"upotrebna dozvola" "data centar"
"urbanističko-tehnički uslovi" "data centar"
"idejno rješenje" "data centar"
"procjena uticaja na životnu sredinu" "data centar"
```

### 1.2 English terms

```text
"Montenegro" "data center"
"Montenegro" "data centre"
"Montenegro" "colocation"
"Podgorica" "data center"
"Niksic" OR "Nikšić" "data center"
"Bar" "Montenegro" "data center"
"Budva" "data center" Montenegro
"Montenegro" "green data centers"
"Montenegro" "cloud region" AWS Azure Google Oracle
"Montenegro" "data center" "building permit"
"Montenegro" "data center" "grid connection"
```

### 1.3 Official-source query templates

Substitute `{municipality}`, `{operator}`, `{entity}`, `{site}`, `{address}`, `{parcel}`, `{industrial_zone}`.

```text
site:gov.me/mdup "data centar"
site:gov.me/mdup "građevinska dozvola" "data centar"
site:gov.me/mdup "urbanističko-tehnički uslovi" "{entity}"
site:gov.me "Državni data centar"
site:gov.me "Data centar" "Disaster Recovery"
site:gov.me "data center" "Hungary" "Montenegro"
site:podgorica.me "data centar"
site:sekretarijat-za-plurzs.podgorica.me "data centar"
site:sekretarijat-za-ppor.podgorica.me "data centar"
site:{municipal-domain} "građevinske dozvole" "{operator}"
site:{municipal-domain} "urbanističko-tehnički uslovi" "data centar"
site:{municipal-domain} "upotrebne dozvole" "data centar"
site:ekip.me "Data Centar Podgorica"
site:ekip.me "kolokacija" "Crnogorski Telekom"
site:ekip.me "Registrovani operatori elektronskih komunikacija"
site:telekom.me "DATA centra" "MTKC"
site:telekom.me "Data Centar Podgorica"
site:1.me "data centar"
site:mtel.me "Virtual data centar"
site:cedis.me "Konsolidovani Data Centar"
site:cges.me "Data Centar"
site:regagen.co.me "License Registry"
site:epa.org.me "data centar"
site:epa.org.me "agregat" "data centar"
```

---

## 2. Grade A official/regulatory backbone

### 2.1 National planning, construction, and permits

Primary sources:

- Ministry of Spatial Planning, Urbanism and State Property (`MUPD`) UTU page: https://www.gov.me/mdup/urbanisticko-tehnicki-uslovi/urbanisticko-tehnicki-uslovi . Grade A for issued and requested UTU records.
- MUPD building-permit page: https://www.gov.me/mdup/urbanisticko-tehnicki-uslovi/gradevinske-dozvole . Grade A for requested, issued, refused, suspended, or interrupted state-level building-permit proceedings.
- Government single point of contact construction service page: https://psc.gov.me/en/sektorske-informacije/ministarstvo-prostornog-planiranja-urbanizma-i-drzavne-imovine/izrada-tehnicke-dokumentacije-i-izvodenje-radova/ . Grade A process source for construction-documentation/rules routing.
- eParcela building-permit service front door: https://eparcela.me/en/postupci/gradjevinska-dozvola . Treat as Grade A/B service-routing evidence only; verify individual permits in MUPD or municipal records.

Extraction fields:

- authority, document type, request/decision number, publication date, applicant/investor, designer/reviewer, municipality, cadastral municipality, parcel/urban plot (`UP`), plan/DUP/LSL name, address/site;
- project description, gross floor area, building category, use, electrical/mechanical sections, transformer or generator references;
- status: requested, issued, refused, suspended, interrupted, changed investor, amended permit, use permit;
- related documents: UTU -> concept design (`idejno rješenje`) -> main design/revision -> building permit -> use permit.

Important caveat: Montenegro's planning records often describe generic `poslovni objekat`, `infrastrukturni objekat`, `telekomunikacioni objekat`, or `objekat od opšteg interesa` rather than saying `data centar`. For known operator sites, search by legal entity and address as well as by datacenter terms.

### 2.2 Municipal planning and permit portals

High-yield municipal sources:

- Podgorica planning/permit secretariat: https://sekretarijat-za-plurzs.podgorica.me/ . Year indexes include `Građevinske dozvole`, `Upotrebne dozvole`, `Odobrenje za građenje`, and `Urbanističko-tehnički uslovi`; examples: https://sekretarijat-za-plurzs.podgorica.me/gradevinske-dozvole/ and https://sekretarijat-za-plurzs.podgorica.me/urbanisticko-tehnicki-uslovi/ . Podgorica environment/planning notices are also at https://sekretarijat-za-ppor.podgorica.me/ .
- Bar urbanism page: https://bar.me/lokalna-uprava/sekretarijati/sekretarijat-za-urbanizam-i-prostorno-planiranje/gradevinske-dozvole/ . The Bar site has separate sections for building permits, use permits, UTU, public-interest-object decisions, temporary-object programs, and legalization.
- Kotor annual permit/UTU indexes: https://www.kotor.me/opstinakotor/gradevinske-upotrebne-dozvole-i-urbanisticko-tehnicki-uslovi-2025/ plus annual pages for 2024, 2023, etc. High relevance because Kotor/Tivat/Budva coastal development may host telecom nodes, cable landing support, or disaster-recovery sites.
- Nikšić document API/domain: `https://api.niksic.me/uploads/...` and https://niksic.me/ . Search direct PDFs for `građevinske dozvole`, `UTU`, `Željezara`, `KDC`, `EPCG`, `CEDIS`, `CGES`, and `data centar`.

Municipal query template:

```text
site:{municipal-domain} "{operator}" "građevinska dozvola"
site:{municipal-domain} "{operator}" "upotrebna dozvola"
site:{municipal-domain} "{operator}" "urbanističko-tehnički uslovi"
site:{municipal-domain} "data centar"
site:{municipal-domain} "server sala"
site:{municipal-domain} "agregat" "UPS"
site:{municipal-domain} "trafostanica" "{operator}"
site:{municipal-domain} "{industrial_zone}" "data centar"
site:{municipal-domain} "{parcel}" "{entity}"
```

### 2.3 Environmental permitting and EIA

Primary sources:

- Environmental Protection Agency (`Agencija za zaštitu životne sredine`): https://epa.org.me/ . Use for EIA studies/decisions, integrated permits, and environmental notices when a datacenter has generators, cooling plant, batteries, fuel storage, or a dedicated energy installation.
- Podgorica environmental notices: https://sekretarijat-za-ppor.podgorica.me/ . Useful for local EIA-screening notices and decisions.

Search terms:

```text
site:epa.org.me "data centar"
site:epa.org.me "server sala"
site:epa.org.me "agregat" "Podgorica"
site:epa.org.me "procjena uticaja" "data centar"
site:epa.org.me "elaborat procjene uticaja" "data centar"
site:sekretarijat-za-ppor.podgorica.me "data centar" "procjena uticaja"
site:{municipal-domain} "elaborat procjene uticaja" "data centar"
site:{municipal-domain} "agregat" "trafostanica" "{operator}"
```

What to extract:

- applicant/project owner, project location, coordinates/parcels, environmental authority, decision date;
- generator count/fuel, UPS/battery systems, cooling system, transformer/substation, water use, noise and air-emission conditions;
- whether the EIA authority requires a full `elaborat` or decides it is not required.

### 2.4 Energy and grid pipeline

Primary sources:

- REGAGEN, Energy and Water Regulatory Agency of Montenegro: https://regagen.co.me/en/pocetna-english/ and https://regagen.co.me/en/about-agency/ . Grade A for energy-regulator role, licensing, closed distribution systems, public hearings, and license registry.
- CGES, transmission system operator: https://cges.me/ . Development-plan PDFs and project pages are Grade A for transmission substations, major grid reinforcements, and TSO datacenter/disaster-recovery mentions.
- CEDIS, distribution system operator: https://cedis.me/ . Grade A for distribution context and its official statement that EPCG, CEDIS, and CGES are building a Consolidated Data Center.
- CEDIS official KDC announcement: https://cedis.me/najnovije-vijesti/epcg-cedis-i-cges-udruzuju-snage-za-digitalnu-buducnost/ . It states the **Konsolidovani Data Centar** will be in the **Željezara Nikšić industrial complex** and may later support other institutions/companies.
- CGES development-plan example: https://cges.me/wp-content/uploads/2025/12/Updated-Transmission-System-Development-Plan-2023-2032-1.pdf . Grade A for network planning context, not facility evidence by itself.

Energy query templates:

```text
site:cedis.me "Konsolidovani Data Centar"
site:epcg.com "Konsolidovani Data Centar"
site:cges.me "Konsolidovani Data Centar"
site:cges.me "DR Data Centar"
site:cges.me "serverske" "data centru"
site:cges.me "trafostanica" "Nikšić"
site:cges.me "trafostanica" "Podgorica"
site:cges.me "trafostanica" "Bar" OR "Budva" OR "Tivat"
site:regagen.co.me "zatvoreni distributivni sistem" "data centar"
site:regagen.co.me "licenca" "{entity}"
"data centar" "trafostanica" "Crna Gora"
"data centar" "MW" "Crna Gora"
"data centar" "MVA" "Crna Gora"
```

Use energy records for siting and capacity context. Do not infer a datacenter from a substation alone. Promote energy evidence only when it names a datacenter project, owner, or facility.

### 2.5 EKIP telecom regulator and network evidence

Primary sources:

- EKIP home/services: https://ekip.me/ and https://ekip.me/agency-services . Grade A for telecom-regulator functions and operator registration routing.
- EKIP competencies: https://ekip.me/page/about/competencies/content . Grade A for the agency's role in electronic-communications market regulation, registries, technical/security measures, numbering/frequencies, and consultations.
- EKIP operator-registration decisions: https://ekip.me/page/about/proactive-access-to-information/decisions-and-other-individual-acts-significant-for-the-rights-obligations-and-interests-of-the-third-parties/decision-on-entry-of-operators-in-the-register-of-operators . Use to verify licensed electronic-communications operators.
- EKIP service notices for Crnogorski Telekom works at `Data Centar Podgorica`, e.g. https://www.ekip.me/latest-informations/servisne-informacije/obavjestenje-o-pocetku-radova-60 . Grade A/B operational evidence for a named telecom data-center location; cross-check with Crnogorski Telekom official pages.
- EKIP-published Crnogorski Telekom reference offers mentioning `kolokacija` and Telekom premises; useful for network-colocation context but not a retail datacenter list.

EKIP query templates:

```text
site:ekip.me "Data Centar Podgorica"
site:ekip.me "Data Centar" "Crnogorski Telekom"
site:ekip.me "kolokacija" "Crnogorski Telekom"
site:ekip.me "Registrovani operatori elektronskih komunikacija"
site:ekip.me "One Crna Gora" "operator"
site:ekip.me "MTEL" "operator"
site:ekip.me "Telemach" "operator"
site:ekip.me "Domen" "operator"
site:ekip.me "internet exchange" OR "IXP"
```

Use EKIP to build the operator universe: Crnogorski Telekom, One Crna Gora, MTEL, Telemach, Domena/DoMEn, Čikom, Logate, Data Design, and ISPs/hosting firms. Then pivot each name to official facility, tender, permit, and procurement records.

### 2.6 Government, public procurement, and digital-state projects

Primary sources and leads:

- Government session material for State Data Center feasibility: https://www.gov.me/clanak/saopstenje-sa-71-sjednice-vlade-crne-gore-2 and the linked material `Informacija o izradi Studije izvodljivosti za Državni data centar i Državni Disaster Recovery centar` at https://wapi.gov.me/download/0ceb4521-b81c-415c-a5bc-bd13523d6964?version=1.0 . Grade A for government planning intent; facility status remains planned until location/permit/build evidence appears.
- Earlier state data-center feasibility material: https://wapi.gov.me/download/a05bd677-0269-46e0-914a-ca981b9925de?version=1.0 . Grade A for requirement that the State Data Center and DR location should be built to Tier3+ standards.
- Government session material mentioning cooperation/feasibility and location search is a key route; search `gov.me` and `wapi.gov.me` PDFs rather than relying on public news summaries.
- Public procurement portal legacy records: https://portalujn.gov.me/ . Search tender documents for `Data Centar`, `server sala`, `UPS`, `agregat`, `hlađenje`, `storage`, `virtualizacija`, and ministry names.

Procurement query templates:

```text
site:portalujn.gov.me "Data Centar"
site:portalujn.gov.me "server sala"
site:portalujn.gov.me "UPS" "data centar"
site:portalujn.gov.me "hlađenje" "data centar"
site:portalujn.gov.me "Ministarstvo javne uprave" "data centar"
site:gov.me "javna nabavka" "data centar"
site:gov.me "Studija izvodljivosti" "Državni data centar"
site:gov.me "Disaster Recovery centar"
```

---

## 3. Cloud region and operator pipeline

### 3.1 Official cloud-region checks

Use official pages only for public cloud region/local-zone evidence:

| Provider | Official page | Montenegro signal |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Montenegro public region found in this pass. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Montenegro public region found in this pass. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Montenegro public region found in this pass. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Montenegro public region found in this pass. |

Rule: a local `cloud`, `VPS`, `virtual data centar`, or reseller page is not hyperscale-region evidence unless the provider's official region/local-zone page names Montenegro.

### 3.2 Operator and colo leads

High-priority operator/source list:

- **Crnogorski Telekom**: official opening page for new Data Center, https://telekom.me/o-kompaniji/media-centar/otvoren-novi-i-savremeni-data-centar-crnogorskog-telekoma . It states the new data center was opened by Crnogorski Telekom and EKIP leadership on 2020-07-06. Tender page https://telekom.me/o-kompaniji/tenderi includes the 2019 tender for works on a new data center at `MTKC`; tender PDFs mention Podgorica/MTKC and data-center layouts. Grade A operator evidence.
- **One Crna Gora**: official `Data centar` page https://1.me/cg/biznis/data-centar/ describes One's carrier-neutral data center and meet-me interconnection. Grade A operator evidence; verify location/address through permits, EKIP, or company documents.
- **MTEL**: official site surfaces `Virtual data centar` and `Virtual private server`, e.g. https://mtel.me/a12521/Poslovni/m-fiskal/Virtual-data-center.html . Treat as Grade B/C service evidence until a physical MTEL facility address or official infrastructure record is found.
- **Kolo DC**: public site https://kolodc.com/ and directories mention a Kolo DC provider profile, but the current public site is broader Northern Europe focused and directory pages should be treated as Grade C for Montenegro unless Kolo publishes a Montenegro site/address or permit evidence appears.
- **Victoria Group Podgorica**: DataCenterMap/Inflect directory lead only; DataCenterMap indicates the old listing may be inactive. Grade C until confirmed by company, permit, or regulator evidence.
- **Domen / DoMEn, Čikom, Logate, Data Design, Telemach, ISPs**: operator universe leads from EKIP/ICT strategy materials; search official pages, tenders, and permits for physical server rooms or colocation.

Operator pivot query:

```text
"{operator}" "data centar" "Podgorica"
"{operator}" "data centar" "Crna Gora"
"{operator}" "kolokacija" "Crna Gora"
"{operator}" "server sala"
"{operator}" "UPS" "data centar"
"{operator}" "agregat" "data centar"
"{operator}" "MTKC" OR "Moskovska" OR "Bulevar Svetog Petra Cetinjskog"
"{operator}" "građevinska dozvola" "Podgorica"
"{operator}" "urbanističko-tehnički uslovi"
```

### 3.3 Trade press and business press

Use as Grade B leads, then backfill official records:

- Data Center Dynamics article on a Montenegro-Hungary infrastructure deal: https://www.datacenterdynamics.com/en/news/montenegro-to-get-data-center-as-part-of-hungary-infrastructure-deal/ . Grade B; location/capacity were not disclosed, so do not create a facility until a government agreement, location decision, permit, or tender is found.
- Balkan Green Energy News on Montenegro as a green-datacenter destination: https://balkangreenenergynews.com/spajic-montenegro-wants-to-be-country-of-green-data-centers/ . Grade B policy/market lead.
- Balkan Green Energy News on EPCG/CEDIS/CGES Consolidated Data Center: https://balkangreenenergynews.com/montenegros-epcg-dso-tso-to-establish-consolidated-data-center/ . Grade B trade version; prefer the official CEDIS announcement for Grade A.
- Local press: Vijesti, Mina, CDM, RTCG, Bankar.me, Investitor.me, Montenegro Business. Search in local language and verify against official operator/government pages.

Trade query templates:

```text
"Crna Gora" "zeleni data centri"
"Spajić" "data centri"
"Mađarska" "data centar" "Crna Gora"
"Hungary" "Montenegro" "data center"
"EPCG" "CEDIS" "CGES" "Konsolidovani Data Centar"
"Željezara Nikšić" "data centar"
"Crnogorski Telekom" "Data Centar" "otvoren"
"One Crna Gora" "data centar" "carrier neutral"
```

---

## 4. Municipality enumeration workflow

For every municipality:

1. Search MUPD UTU/building-permit pages for the municipality, candidate operator names, `data centar`, and support-infrastructure terms.
2. Search the municipality's planning/urbanism site for year-index permit pages (`građevinske dozvole`, `upotrebne dozvole`, `urbanističko-tehnički uslovi`, `odobrenje za građenje`, `odluke za objekte od opšteg interesa`).
3. Search EKIP for telecom operators and notices tied to the municipality; pivot from licensed operators to official operator pages.
4. Search REGAGEN, CGES, CEDIS, EPCG and municipal utility records for grid connection, substations, closed distribution systems, generators, UPS, and energy-company datacenter projects.
5. Search EPA and municipal environment pages for `elaborat`, `procjena uticaja`, generator/cooling/fuel/battery records.
6. Search procurement for ministries, municipalities, public companies, universities, ports, airports, and telecoms.
7. Promote the candidate only after a primary record confirms the facility/project. Keep separate fields for physical site, administrative owner, operator/service brand, stage, and evidence grade.

High-priority municipalities:

| Municipality | Why high yield | Official-first route |
|---|---|---|
| Podgorica / Golubovci-Tuzi area | Capital, telecom HQs, Crnogorski Telekom Data Centar Podgorica, One data-center service, EKIP, government datacenter planning, municipal data-center budget items | Podgorica planning pages, EKIP `Data Centar Podgorica`, Crnogorski Telekom tender/opening pages, One official page, MUPD, gov.me, municipal environmental notices |
| Nikšić | EPCG/CEDIS/CGES Consolidated Data Center planned in Željezara Nikšić industrial complex; EPCG HQ/utility infrastructure; Tehnopolis/public-sector ICT leads | CEDIS/EPCG/CGES official announcements, Nikšić permit PDFs, MUPD UTU/building permits, REGAGEN, CGES substation/development docs, procurement |
| Bar | Port/cable/energy corridor relevance; municipal permit portal is well indexed; likely telecom nodes and disaster-recovery candidates | Bar building/use/UTU pages, Port of Bar/utility procurement, CGES Bar-Budva/Tivat grid queries, EKIP operator searches |
| Budva | Coastal telecom load, hotels, One/Telekom/MTEL network nodes, possible DR/edge hosting | Budva municipal permits, EKIP service notices, operator pages, hotel/telecom node searches; require strong evidence because many results are generic tourism IT |
| Kotor | Annual permit/UTU indexes, UNESCO/coastal planning constraints, telecom and cable-adjacent infrastructure | Kotor permit/UTU annual pages, MUPD, EPA, CGES coastal substations, operator searches |
| Tivat | Airport/Porto Montenegro/coastal infrastructure, Lastva grid corridor nearby, potential DR/edge leads | Tivat permits, CGES Lastva/Tivat grid records, municipal procurement, operator and airport/port ICT searches |
| Pljevlja | Major energy infrastructure and CGES/EPCG records; utility DR/data-center references may surface in corporate plans | EPCG/CGES/REGAGEN, municipal permits, EPA industrial permits; treat energy sites as leads only |
| Bijelo Polje / Berane / Plav / Rožaje | Northern regional government/telecom nodes, municipal digitization, potential DR/edge due to geography | Municipal permit/procurement pages, EKIP operators, MUPD, CGES/CEDIS local grid docs |
| Herceg Novi / Ulcinj | Coastal telecom/tourism load, border/cable/port-adjacent infrastructure | Municipal planning pages, EKIP, operator pages, CGES/CEDIS coastal grid, EPA |
| Cetinje / Danilovgrad | Administrative and military/public-sector leads; Danilovgrad appears in defense/telecom documents | Gov.me/ministry procurement, municipal permit pages, EKIP, defense/public-sector ICT searches |

Generic municipality query pattern:

```text
("{municipality}" OR "{municipal-local-name}") "data centar"
("{municipality}" OR "{municipal-local-name}") "server sala"
("{municipality}" OR "{municipal-local-name}") "kolokacija"
("{municipality}" OR "{municipal-local-name}") "građevinska dozvola" "data centar"
("{municipality}" OR "{municipal-local-name}") "urbanističko-tehnički uslovi" "data centar"
("{municipality}" OR "{municipal-local-name}") "upotrebna dozvola" "data centar"
("{municipality}" OR "{municipal-local-name}") "trafostanica" "data centar"
("{municipality}" OR "{municipal-local-name}") "agregat" "data centar"
site:{municipal-domain} "data centar"
site:{municipal-domain} "server sala"
site:{municipal-domain} "UPS"
site:{municipal-domain} "{operator}"
```

---

## 5. Reliability rules and pitfalls

Reliability:

- **Grade A**: MUPD or municipal UTU/building/use permit; EPA or municipal EIA decision; REGAGEN/CGES/CEDIS/EPCG official project or license record; EKIP regulator record; operator official datacenter/opening/tender page; government session material or official procurement document; official hyperscaler region page.
- **Grade B**: Data Center Dynamics, Balkan Green Energy News, Vijesti, RTCG, Mina, company quotes in reputable local press, stock-exchange/company announcements that name the parties but are not the original source.
- **Grade C**: DataCenterMap, Inflect, Datacenters.com, Cloudscene, Colomap, LinkedIn, SEO hosting pages, reseller `cloud` pages, generic virtual-server offers.

Pitfalls:

- `Data centar` can mean a server room inside a public body, a telecom network facility, a cloud-service product, or a true colocation facility. Capture the facility type and do not merge them.
- Telecom colocation in EKIP/Telekom reference offers can mean regulated access to exchanges/MDFs, not commercial datacenter colocation.
- Headquarters addresses such as operator offices in Podgorica are not datacenter addresses unless the source names the data-center site there.
- Government feasibility studies and policy statements are Grade A for intent, but not for operational status. Require permit, tender, construction, handover, or opening evidence.
- `Niksic`, `Nikšić`, `Zeljezara`, `Željezara`, `Podgorica`, `Glavni grad`, and Cyrillic variants may all be needed.
- Many municipal PDFs are scans; use OCR when text search misses likely permit PDFs.
- Montenegro uses both old and new construction procedures. Older records may say `odobrenje za građenje` or use legacy law references; do not discard them if the facility predates current laws.
