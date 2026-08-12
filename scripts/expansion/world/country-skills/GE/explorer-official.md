# GE Explorer Official - Georgia Datacenter Enumeration

Date: 2026-08-12. Scope: Georgia (GE), all 12 top-level units in `world-manifest.jsonl`: Abkhazia, Adjara, Guria, Imereti, K'akheti, Kvemo Kartli, Mtskheta-Mtianeti, Rach'a-Lechkhumi-Kvemo Svaneti, Samtskhe-Javakheti, Shida Kartli, Samegrelo-Zemo Svaneti, Tbilisi.

Angle: official, regulator, municipal, cadastral, environmental, energy-grid, public procurement, investment-agency and other primary-source evidence for data-center facilities and projects. This file is the counting gate. Industry/catalog evidence can seed a record, but the preferred countable evidence is a municipal construction/commissioning record, NAPR cadastre/company record tied to a site, MEPA/NEA environmental decision, GSE/DSO connection record, GNCC authorization where relevant, an official government project page, or a first-party operator page that clearly advertises a live facility.

Reliability grades used here:

- **A**: Georgian official portal/register/agency/municipality; Matsne legal text; NAPR/cadastre; ComCom/GNCC, GNERC, GSE, Telasi/Energo-Pro official records; MEPA/NEA/EI environmental records; official FIZ/operator resident pages; official Uptime Institute certification page; first-party operator page with facility address/service.
- **B**: established trade or local press, investment-promotion article, contractor case study, IXP/association page, or first-party corporate page that proves entity/service but not the physical facility.
- **C**: catalog/aggregator/search snippet/social media/directory mirror. Never count from C alone.

Do not upgrade a source merely because it gives MW/rack figures. If capacity comes from DC Hub, Baxtel, DataCenterMap, Datacenters.com, Cloudscene, Inflect or similar, keep the capacity as catalog-reported and mark the record `evidence_grade=C` or `capacity_source_grade=C` unless an operator or official source confirms it.

---

## 0. Georgia Ground Rules

- Georgia's top-level enumeration buckets are 2 autonomous republics, 9 regions and Tbilisi. The 12 buckets in this repo are complete: Abkhazia, Adjara, Guria, Imereti, K'akheti, Kvemo Kartli, Mtskheta-Mtianeti, Rach'a-Lechkhumi-Kvemo Svaneti, Samtskhe-Javakheti, Shida Kartli, Samegrelo-Zemo Svaneti, Tbilisi. Official/admin context: Geostat `https://geostat.ge`; NAPR/maps `https://www.napr.gov.ge` and `https://maps.gov.ge`; Georgian administrative law on Matsne.
- Georgia is centralized and small, but building control is municipal. Tbilisi City Hall handles Tbilisi. Batumi, Kutaisi, Rustavi and Poti are self-governing city/municipal portals. Other towns use municipal `*.gov.ge` portals. Searches must go municipality-by-municipality for permits and commissioning.
- Abkhazia is outside Georgia's effective control. Georgian public registries and regulators cannot be assumed to have current facility coverage there. Record Abkhazia as "no reliable Georgian official coverage"; do not fabricate Georgian permit/cadastre evidence. De-facto/occupation-zone crypto-mining evidence belongs in a separate note and should not be mixed with countable Georgian official records.
- Parts of Shida Kartli, Mtskheta-Mtianeti, Imereti and Rach'a-Lechkhumi-Kvemo Svaneti overlap the former South Ossetian autonomous area and are not fully under Georgian control. For facilities in those portions, require extra location precision and treat de-facto-zone evidence separately.
- Georgian-language evidence is mandatory for high-recall official work. Use both Mkhedruli and English terms. In Georgian, `მონაცემთა ცენტრი` can mean "information center" in a municipal/statistical/customer-service sense, so always verify the object is an IT/server facility.
- No hyperscale cloud region is known in Georgia (country) from official cloud-region lists. Re-check official provider lists only: AWS `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; Azure `https://azure.microsoft.com/en-us/explore/global-infrastructure/`; Google Cloud `https://cloud.google.com/about/locations`; Google data-center locations `https://datacenters.google/locations`; Oracle `https://www.oracle.com/cloud/public-cloud-regions/`. Beware US-state "Georgia" pages.

Core Georgian terms:

```
მონაცემთა ცენტრი = data center
მონაცემთა დამუშავების ცენტრი = data processing center
სერვერული ოთახი / სერვერული = server room
სერვერი = server
კოლოკაცია = colocation
ჰოსტინგი / ვებ-ჰოსტინგი = hosting / web hosting
სამშენებლო ნებართვა / მშენებლობის ნებართვა = construction permit
ნებართვის გაცემა = permit issuance
ექსპლუატაციაში მიღება = commissioning / acceptance into operation
გარემოზე ზემოქმედების შეფასება = environmental impact assessment
გარემოსდაცვითი გადაწყვეტილება = environmental decision
ელექტროენერგიის ქსელთან მიერთება = electricity grid connection
მაღალი ძაბვა = high voltage
თავისუფალი ინდუსტრიული ზონა = free industrial zone
საკადასტრო კოდი = cadastral code
საიდენტიფიკაციო კოდი = company identification code
```

---

## 1. Official Source Backbone

### 1.1 Construction, Land and Municipal Planning

- **Matsne legal base**: `https://matsne.gov.ge`. Use the Code of Georgia on Spatial Planning, Architectural and Construction Activities, English PDF `https://matsne.gov.ge/en/document/download/4276845/32/en/pdf`, plus Georgian version when Georgian legal wording is needed. Grade A.
- **MS.GOV.GE**: `https://ms.gov.ge`. Unified electronic service/permit environment referenced for municipal services. Grade A if a record page is reachable; otherwise use it as a process pointer and pivot to the municipality.
- **TCSA**: `https://tcsa.gov.ge`; development/building permits page `https://tcsa.gov.ge/pages/development`. Grade A for national construction-supervision/process records.
- **Tbilisi City Hall**: `https://tbilisi.gov.ge`. Grade A for Tbilisi permits, architecture/urban decisions, commissioning records.
- **Municipal portals**: use exact portals, not guessed records. Common high-value portals: Batumi `https://batumi.gov.ge`, Kutaisi `https://kutaisi.gov.ge`, Rustavi `https://rustavi.gov.ge`, Poti `https://poti.gov.ge`, Zugdidi `https://zugdidi.gov.ge`, Gori `https://gori.gov.ge`, Telavi `https://telavi.gov.ge`.
- **NAPR / Public Registry**: `https://www.napr.gov.ge` and cadastral/spatial `https://maps.gov.ge`. Grade A for company identity, legal form, cadastral parcel and real-estate purpose. NAPR alone proves entity/site ownership, not live DC operation.

Permit/cadastre extraction fields:

```
permit/decision number
decision date
issuing municipality/agency
applicant/developer
legal entity name and ID
address and cadastral code
building purpose
building area / land area
commissioning status
linked substation/generator/fuel/cooling works
source URL and capture date
```

### 1.2 Telecom and Internet Regulation

- **Communications Commission / ComCom / GNCC**: `https://comcom.ge`, English `https://comcom.ge/en`. Grade A.
- **Electronic communications authorization page**: `https://comcom.ge/en/regulation/eleqtronuli-komunikaciebi/authorization-of-activity-in-the-field-of-electronic-communications-sector`. It confirms authorization mechanics for electronic communications sector participants. Grade A.
- **Law on Electronic Communications**: ComCom PDF `https://www.comcom.ge/uploads/other/1/1222.pdf` and Matsne English download `https://www.matsne.gov.ge/en/document/download/29620/26/en/pdf`. Grade A.
- **Register pivots**: search ComCom/GNCC for operator names and authorizations. A telecom authorization supports sector identity, but it is not facility evidence unless the record names a data-center/colo site.

Telecom extraction fields:

```
authorized person / licensee
authorization or licence type
company ID
service scope
registered address
facility/service address if published
decision number/date
```

### 1.3 Environment

- **MEPA**: `https://mepa.gov.ge`. Grade A for ministry policy and legacy pages.
- **National Environment Agency (NEA)**: `https://nea.gov.ge`. Grade A for environmental procedures.
- **Environmental information portal**: `https://ei.gov.ge` is the current high-value portal for public hearings and EIA/EP decisions per NEA public guidance. Grade A when records are found.
- **Environmental Assessment Code**: `https://www.matsne.gov.ge/en/document/view/3691981`. Grade A.
- **Law on Environmental Impact Permits**: `https://www.matsne.gov.ge/en/document/view/20206`. Grade A for older permit context.

Environmental extraction fields:

```
screening/scoping/EIA/environmental decision number
applicant/operator
site address and cadastral code
backup generator count and kW/MW
fuel storage volume
water/cooling demand
noise/air modelling
decision status/date
public hearing date
```

### 1.4 Electricity and Energy

- **GNERC**: `https://gnerc.org`. Grade A for electricity licences, tariffs and licensee decisions.
- **GSE**: `https://www.gse.com.ge`; grid-connection page `https://www.gse.com.ge/for-customers/for-connection-to-our-grid`; legal framework `https://www.gse.com.ge/about-us/legal-framework/legislation`. Grade A. GSE says connection to the transmission grid is regulated by Chapter II of the Grid Code.
- **Telasi**: `https://www.telasi.ge`. Tbilisi DSO. Grade A.
- **Energo-Pro Georgia**: `https://www.energo-pro.ge`. Main regional DSO. Grade A.
- **ESCO**: `https://esco.ge`. Commercial operator/market context. Grade A.

Energy extraction fields:

```
connection agreement / technical condition number
customer/developer
connection voltage
substation name
requested/approved MW or MVA
DSO/TSO
decision/status/date
```

Grid evidence without a named DC customer is context only.

### 1.5 State ICT, FIZ and Investment Sources

- **Ministry of Economy and Sustainable Development**: `https://www.economy.ge`. Grade A for government project announcements, including the Kutaisi Technology Hub.
- **GITA**: `https://gita.gov.ge`. Grade A/B depending on whether it is a direct project owner/source or investment context.
- **Digital Governance Agency / historical Data Exchange Agency function**: `https://dga.gov.ge`. Grade A context for state ICT/e-government products; do not count state server rooms unless the project is explicitly a data center facility. Older third-party records may still refer to the LEPL Data Exchange Agency at `dea.gov.ge`, but that host did not resolve during this review.
- **Revenue Service**: `https://www.rs.ge`. Grade A for tax/FIZ legal context.
- **Tbilisi Free Zone**: `https://tfz.ge`; **Kutaisi FIZ**: `https://kutaisifreezone.ge`; **Poti FIZ**: `https://potifreezone.ge`. Grade A for FIZ operator/resident information, but resident status does not prove a DC without a facility/service/permit record.
- **Uptime Institute awards**: Georgia country page `https://uptimeinstitute.com/uptime-institute-awards/country/id/GE`. Grade A for certification status only. Tier Design certification is not proof that a facility is operating.

---

## 2. Query Templates

Use Georgian first, then English. Replace `{division}`, `{municipality}`, `{operator}`, `{address}`, `{cadastral}`, `{company_id}`.

### 2.1 Official Georgian Searches

```
site:ms.gov.ge "მონაცემთა ცენტრი"
site:tcsa.gov.ge "მონაცემთა ცენტრი"
site:tbilisi.gov.ge "მონაცემთა ცენტრი"
site:tbilisi.gov.ge "სამშენებლო ნებართვა" "{operator}"
site:tbilisi.gov.ge "{address}" "ნებართვა"
site:{municipality}.gov.ge "მონაცემთა ცენტრი"
site:{municipality}.gov.ge "სერვერული"
site:{municipality}.gov.ge "სამშენებლო ნებართვა" "{operator}"
site:{municipality}.gov.ge "{cadastral}"
site:napr.gov.ge "{operator}" "{company_id}"
site:maps.gov.ge "{cadastral}"
site:ei.gov.ge "მონაცემთა ცენტრი"
site:ei.gov.ge "{operator}" "გარემოზე ზემოქმედების შეფასება"
site:mepa.gov.ge "მონაცემთა ცენტრი"
site:nea.gov.ge "მონაცემთა ცენტრი"
site:gse.com.ge "მონაცემთა ცენტრი"
site:gnerc.org "მონაცემთა ცენტრი"
site:comcom.ge "{operator}" "ავტორიზაცია"
"{operator}" "საიდენტიფიკაციო კოდი"
"{operator}" "საკადასტრო კოდი"
"{operator}" "ექსპლუატაციაში მიღება"
"{address}" "მონაცემთა ცენტრი"
```

### 2.2 English Official-Adjacent Searches

```
"Georgia" "data center" "building permit" Tbilisi
"Georgia" "data centre" "construction permit" Tbilisi
"Georgia" "data center" "environmental decision"
"Georgia" "data center" "grid connection" GSE
"Tbilisi" "data center" "cadastral"
"Kutaisi Technology Hub" "data center" site:economy.ge
"G Data Data-Center #1" Tbilisi Uptime
"Bank of Georgia Main DC" Lilo Uptime
"TBC TBL-01" Uptime Georgia
site:comcom.ge "{operator}" "electronic communications"
site:gnerc.org "{operator}" "electricity"
```

### 2.3 Low-Yield Division Sweep

```
"{division}" "მონაცემთა ცენტრი"
"{division}" "data center" Georgia -Atlanta -USA
"{division}" "სერვერული"
"{main_town}" "მონაცემთა ცენტრი"
"{main_town}" "data center" colocation Georgia
site:bm.ge "{division}" "მონაცემთა ცენტრი"
site:commersant.ge "{division}" "მონაცემთა ცენტრი"
site:{municipality}.gov.ge "სერვერული"
```

---

## 3. Officially Actionable Leads

This is not a final inventory. It is the official-verification queue.

| Lead | Division / municipality | Best verified source trail | Official-use status |
|---|---|---|---|
| Silknet / Silk Cloud Tier III commercial DC | Tbilisi | Silknet first-party partnership note says it will introduce Georgia's first certified Tier 3 DC: `https://silknet.com/en/media/singleview/2310-silknetis-da-orange-is-globaluri-mnishvnelobis-tanamshromloba-akhal-etapze-gadadis` (A for company plan). BM.ge says Silknet broke ground in Aug 2026, Silk Cloud will operate it, 2 MW high-resilience capacity, operational expected 2027: `https://bm.ge/en/news/silknet-breaks-ground-on-georgias-first-tier-iii-certified-commercial-data-center` (B). | Planned/under construction by first-party plus press. Countable as planned only if accepting operator/press; Grade A count needs Tbilisi permit, NAPR Silk Cloud JSC record, cadastre, grid/DSO evidence. |
| Cloud9 Dinamo Arena data center | Tbilisi | First-party Cloud9 data-center page: `https://cloud9.ge/en/data-center/`; contact/address page `https://cloud9.ge/en/company/contact/`; home page says professional web hosting provider and data-center operator `https://cloud9.ge/` (A). DataCenterMap has capacity/details `https://www.datacentermap.com/georgia/tbilisi/cloud9-dc/` (C). | Operating commercial DC by first-party evidence. Grade A for existence/address/service; catalog-only capacity (0.5 MW/630 kVA generator) needs operator/permit confirmation before using as official capacity. |
| Caucasus Online Data Center / colocation | Tbilisi | First-party service page `https://www.co.ge/en/426/` (A for service); company site `https://www.co.ge/en/` (A); PeeringDB facility `https://www.peeringdb.com/fac/8513` (C); catalogs (C). | Operating colo candidate with first-party service evidence. Need exact current site/address, Tbilisi permit/cadastre and NAPR company record before high-confidence facility record. |
| NewTelco Georgia / NewTelco Tbilisi | Tbilisi | NewTelco group site `https://newtelco.com/` states NewTelco Georgia has been a neutral data center since Feb 2016 and gives A. Politkovskaia contact context (A/B); ENOG presentation PDF mentions purpose-built NewTelco Georgia DC (B); DataCenterMap/Inflect/DC Hub provide address/spec leads (C). | Operating carrier-neutral DC likely. Treat first-party group page as existence support, but official count should verify Georgian legal entity, Tbilisi permit/cadastre and current operator page. Catalog MW stays C. |
| G Data Data-Center #1 | Tbilisi | Uptime Institute Georgia awards page `https://uptimeinstitute.com/uptime-institute-awards/country/id/GE`; facility page `https://uptimeinstitute.com/uptime-institute-awards/datacenter/g-data-datacenter-1/2214` (A for Tier III Design certification). | Planned/design-certified only unless constructed/operating source is found. Do not infer address, MW or operation from design certification. |
| JSC Bank of Georgia Main DC (Lilo) | Tbilisi / Lilo | Uptime Institute Georgia awards page lists Tier III Design and Constructed Facility certification for Bank of Georgia Main DC (Lilo) (A for certification). | Private enterprise DC; context only, not commercial colo unless first-party commercial service evidence appears. |
| TBC Bank TBL-01 | Tbilisi | Uptime Institute Georgia awards page lists Tier III Constructed Facility certification (A for certification). | Private bank DC; context only, not commercial colo. |
| Bitfury / Gldani / Tbilisi FIZ crypto data center | Tbilisi / Gldani | Government 2015 appearance says BitFury started independent Gldani FIZ/technology park project: `https://www.gov.ge/index.php?info_id=52950&lang_id=ENG&sec_id=412` (A context). Bitfury press-release PDF says it built the Gldani data center in 2016 and sold it to Chong Sing Holdings: `https://bitfury.com/content/4-press/2_13_18_bitfury_group_sells_gldani_release.pdf` (A/B first-party historical). BM.ge says former TFZ owner Bitfury owned a 60 MW crypto DC on site: `https://bm.ge/en/news/bitfury-is-no-longer-the-owner-of-tbilisi-fiz/130069` (B). | Historical crypto/HPC facility. Current live status and ownership are unresolved; do not count as live commercial colo without current operator/FIZ/NAPR/grid confirmation. |
| Bitfury Gori bitcoin-mining DC | Shida Kartli / Gori | Historical trade sources cite a 20 MW Gori facility; no official Georgian permit/cadastre found in this review. | Historical only until Gori municipality/NAPR/grid/current operator evidence is found. |
| Kutaisi Technology Hub data center component | Imereti / Kutaisi | Ministry of Economy official pages say the former Parliament building will house a Technology Hub with a powerful data center for Georgian AI: `https://www.economy.ge/?lang=en&nw=2613&page=news`; progress update `https://www.economy.ge/?lang=en&nw=2998&page=news` (A). | Official planned public/tech-hub data-center component. Count as planned government project only; no MW, operator or commercial colo status published. |
| Cloud9 Batumi Arena | Adjara / Batumi | DataCenterMap lists Cloud9 - Batumi Arena at Shartava Ave 13, D10, under construction: `https://www.datacentermap.com/georgia/batumi/cloud9-batimu-arena/ecosystem/` and market page `https://www.datacentermap.com/georgia/batumi/` (C). | Catalog lead only. Must verify with Cloud9 first-party page and Batumi municipal permit before counting. |
| GDKHOST.NET small data center | Samegrelo-Zemo Svaneti / likely Zugdidi area | First-party about page says GDKHOST provides hosting from its own small data center in Georgia: `https://gdkhost.net/pages/about`; home page markets VPS/colocation/hosting in Georgia `https://gdkhost.net/` (A for service claim, not exact municipality). Prior network/business-directory leads tie Ordunet/GDKHOST to Zugdidi (B/C). | Small operating hosting DC by first-party claim. Need exact site/municipality, legal entity and municipal/cadastre evidence before assigning definitively to Zugdidi/Samegrelo-Zemo Svaneti. |
| Innovative Technology LLC data-center services | K'akheti / Telavi, Ruispiri | First-party service page reported in prior batch: `https://intechnologyllc.com/service/datacenter.html` (check live before use). | Candidate service provider. If live, first-party service evidence is A/B, but exact facility status/capacity needs NAPR/municipal verification. |
| Proservice Data Center | Tbilisi | Architecture/project and catalog leads only; search noise is high. | C/B lead only until a reliable Georgian operator/project page or permit is found. |
| WORLDBUS Data Center | Tbilisi | DataCenterMap/Datacenters.com/DC Hub-style catalog leads only, e.g. `https://www.datacenters.com/worldbus-georgia` (C). | Catalog candidate. Do not count without operator page, NAPR and Tbilisi permit/cadastre. |
| Abkhazia crypto/mining technopark claims | Abkhazia | DCD/JAMnews-style de-facto/occupation-zone reporting only. | Exclude from Georgian official enumeration; separate de-facto handling. |

---

## 4. Division-by-Division Official Strategy

| Division | Municipal coverage | Official strategy and current posture |
|---|---|---|
| Abkhazia | Georgian official coverage unreliable; de-facto districts are not Georgian permit buckets | Do not enumerate from Georgian official records. Record "no reliable Georgian official data"; flag crypto/mining claims for de-facto handling only. |
| Adjara | Batumi, Khelvachauri, Kobuleti, Keda, Shuakhevi, Khulo | Batumi is the only current lead area because DataCenterMap lists Cloud9 Batumi Arena. Verify at `batumi.gov.ge`, Cloud9 first-party pages, NAPR/cadastre for Shartava Ave 13/D10, and Energo-Pro/municipal utility evidence. Other municipalities get low-yield sweeps. |
| Guria | Ozurgeti, Lanchkhuti, Chokhatauri | No verified DC leads. Sweep municipal permits for `მონაცემთა ცენტრი`, `სერვერული`, hosting company addresses and telecom buildings; classify no-project if no official/first-party evidence appears. |
| Imereti | Kutaisi, Tskaltubo, Zestaponi, Samtredia, Chiatura, Tkibuli, Sachkhere, Baghdati, Vani, Terjola, Kharagauli, Khoni | Highest lead is official Kutaisi Technology Hub in former Parliament building. Use Economy Ministry/GITA pages, Kutaisi municipal permits, public procurement, NAPR/cadastre and energy records. Also sweep Kutaisi FIZ resident lists at `kutaisifreezone.ge` for IT/HPC/crypto tenants. |
| K'akheti | Telavi, Sighnaghi, Gurjaani, Kvareli, Lagodekhi, Dedoplistskaro, Sagarejo, Akhmeta | Validate Innovative Technology/Ruispiri lead: first-party page, NAPR entity, Telavi municipal permit/cadastre, Energo-Pro connection if visible. Otherwise low-yield municipal sweep. |
| Kvemo Kartli | Rustavi, Gardabani, Marneuli, Bolnisi, Dmanisi, Tsalka, Tetritskaro | No confirmed lead. Rustavi industrial land and Gardabani power area are watchlist buckets. Search Rustavi/Gardabani permits, GSE/GNERC records and NAPR for IT/HPC/hosting entities. |
| Mtskheta-Mtianeti | Mtskheta, Dusheti, Tianeti, Kazbegi | No confirmed lead. Be precise because parts overlap occupied/de-facto South Ossetia context. Sweep Mtskheta/Dusheti permits and telecom infrastructure; do not count ordinary mountain resort IT/server rooms. |
| Rach'a-Lechkhumi-Kvemo Svaneti | Ambrolauri, Oni, Tsageri, Lentekhi | No confirmed lead. Low-yield sweep only; note occupied/de-facto overlap around Oni if a lead appears. |
| Samtskhe-Javakheti | Akhaltsikhe, Borjomi, Akhalkalaki, Ninotsminda, Adigeni, Aspindza | No confirmed lead. Sweep Borjomi/Akhaltsikhe permits and hosting/telecom terms; likely no-project. |
| Shida Kartli | Gori, Kaspi, Kareli, Khashuri | Bitfury Gori is the historical lead. Verify Gori municipal permits, NAPR/cadastre, GSE/Energo-Pro connection and current ownership/status. Treat occupied/de-facto-zone locations separately. |
| Samegrelo-Zemo Svaneti | Poti, Zugdidi, Senaki, Martvili, Abasha, Khobi, Chkhorotsku, Tsalenjikha, Mestia | GDKHOST/Ordunet small DC lead likely points to Zugdidi; verify exact site through first-party contact, NAPR and Zugdidi permits. Poti FIZ is the industrial watchlist: check `potifreezone.ge`, Poti permits and port/grid records. |
| Tbilisi | Tbilisi districts, especially Didube/Dinamo, Saburtalo/Politkovskaia, Gldani/TFZ, Lilo, central ISP/IX addresses | Highest yield. Verify Silk Cloud, Cloud9, Caucasus Online, NewTelco, G Data, Bank of Georgia Lilo, TBC TBL-01, Bitfury/Gldani, WORLDBUS, Proservice. Use Tbilisi City Hall/MS.GOV, NAPR/cadastre, ComCom authorization, Telasi/GSE connection, MEPA/NEA/EI and Uptime. De-duplicate central-office/PoP/server-room claims from commercial DCs. |

---

## 5. Record Rules

- Municipal construction permit, commissioning record, cadastral building purpose, official government project page, or first-party operator page clearly advertising a live facility: `candidate_or_countable=countable`, grade according to source.
- First-party operator page with data-center service but no permit/cadastre: countable as operating if the page gives a facility/service/address, but set `official_status=permit_unverified`.
- Uptime Design certification: `status=planned_or_design_certified`, not operating. Constructed Facility certification proves a built certified facility, but private bank/government facilities remain non-commercial context unless service is marketed.
- Trade press or operator plan says "breaks ground": `status=planned` or `construction`; require permit/cadastre/grid for Grade A construction evidence.
- Catalog-only facility: `candidate_or_countable=candidate`, `do_not_count=true`, `evidence_grade=C`.
- Catalog capacity attached to first-party existence evidence: keep the facility grade from first-party evidence, but set capacity note to `catalog-reported; unverified`.
- Crypto-mining/HPC: record separately from commercial colocation. Count only when current operation, site and operator are confirmed; historical Bitfury leads need current verification.
- Government/bank/state enterprise DCs: context unless externally sell colocation/cloud or are part of the requested inventory scope.
- Abkhazia/de-facto territory: do not mix with Georgian official enumeration.

Recommended output fields:

```
name
country
region
municipality
settlement
address
cadastral_code
operator_or_developer
legal_entity
company_id
status
status_basis
capacity_mw
capacity_source_grade
white_space_m2
building_area_m2
racks
construction_evidence_url
planning_evidence_url
environment_evidence_url
energy_evidence_url
telecom_evidence_url
operator_evidence_url
trade_press_url
catalog_seed_url
evidence_date
evidence_grade
candidate_or_countable
do_not_count_reason
notes
```
