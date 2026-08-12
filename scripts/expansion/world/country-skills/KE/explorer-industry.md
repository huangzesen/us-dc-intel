# KE Explorer - Industry / Press / Vendor Discovery for Kenya Datacentres

Date: 2026-08-12. Scope: Kenya (KE) datacentre enumeration from industry media, local business press, operator/vendor pages, cloud-region announcements, and county-level search patterns. Reliability grades: **A** = official/primary source (operator page, government agency, county/NCA/NEMA/PPP document, cloud provider page), **B** = strong secondary/trade press, established local business press, industry association, or vendor case study, **C** = aggregator, social post, old MoU, market-report snippet, or unverifiable local mention.

---

## 0. Kenya-specific frame

- Kenya does not have a public national facility registry. Discovery works by triangulating **operator pages**, **DCD/African ICT press**, **county planning and construction approvals**, **NCA project registration**, **NEMA EIA/SEA notices**, **Konza/PPP disclosures**, **Tatu City/SEZ and industrial-park pages**, **power/geothermal announcements**, and **IXP/interconnection announcements**.
- Commercial activity is concentrated in a few county clusters:
  - **Nairobi City**: Africa Data Centres/EADC, iXAfrica NBOX1, iColo/Digital Realty Nairobi, PAIX, Telkom/Safaricom/legacy enterprise sites.
  - **Kiambu**: Tatu City/Ruiru, Thika, Limuru/Redhill, Tilisi; often marketed as "Nairobi" but physically outside Nairobi City County.
  - **Mombasa**: iColo Miritini/Nyali and subsea/IXP gateway infrastructure.
  - **Machakos / Kajiado / Makueni**: Konza Technopolis and Konza National Data Centre; county attribution needs parcel-level care because Konza is described across a multi-county buffer/SEZ.
  - **Nakuru**: Olkaria/Naivasha geothermal-powered projects, KenGen Green Energy Park, Microsoft/G42/G42-EcoCloud-style leads.
  - **Kisumu** and selected county capitals: mostly telco/government/edge data centres, not hyperscale.
- Kenya sources use both **data centre** and **data center**. Also search **datacentre**, **cloud region**, **colocation**, **carrier-neutral**, **hyperscale**, **AI-ready**, **sovereign cloud**, **server infrastructure**, **smart city data centre**, **Tier III**, **Uptime Institute**, **NCA project**, **EIA**, **NEMA**, **MW**, **MVA**, **racks**, **geothermal**, **substation**, and **SEZ**.
- English is the main language for business and permitting discovery. Swahili is rarely used for commercial datacentre announcements, but it can surface county-government ICT items. Use Swahili only as a secondary check and verify with English/official documents.

---

## 1. Industry and trade press sources

Use press to discover project names, operators, counties, capacity claims, and status verbs; then verify with an operator, county, NCA/NEMA, PPP, SEZ, or cloud-provider source.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Best global trade feed for Kenya projects: iColo Mombasa/Nairobi, PAIX Nairobi, Konza/Huawei, iXAfrica, Safaricom Limuru, Olkaria/EcoCloud, Microsoft/G42 delays. | B; A only for linked/quoted primary docs |
| CIO Africa | https://cioafrica.co/ | Kenya/Africa ICT trade press. Good for iXAfrica/Safaricom, LINX Nairobi, government cloud/data-centre forums, Oracle/iXAfrica, AI infrastructure. | B |
| Techweez | https://techweez.com/tag/data-center/ | Kenyan tech press; good historical local coverage of iColo, Konza, Telkom, Oracle, Safaricom/iXAfrica. | B/C depending on article detail |
| Business Daily Africa | https://www.businessdailyafrica.com/ | Strong local business/policy source for Konza, PPP expansion, government cloud procurement, county technopolis law, old Konza investor plans. | B |
| Nation / The Standard / The Star / Capital Business | site-scoped search | Useful for local investment, county smart-city, budget, and government project leads. Verify against official documents. | B/C |
| Africa Data Centres Association | https://africadca.org/ | Association news and vendor/member announcements; useful for Oracle/iXAfrica and Africa-wide industry participants. | B |
| LINX / KIXP / Asteroid / PeeringDB | https://www.linx.net/ , https://www.linx.net/ixps/linx-mombasa/ , https://www.kixp.net/ , https://www.peeringdb.com/ | Interconnection announcements often name active datacentres and metros. They prove network node presence, not facility capacity. | B |
| DC Byte / Baxtel / DataCenterMap / OCOLO / Inflect / Datacenters.com | market/location pages | Useful lead indexes for older enterprise and telco sites. Aggregators can misplace counties and stale capacities; never use alone for final capacity. | C/B- |
| Vendor case studies | Siemon, Schneider Electric, Huawei, Vertiv, Caterpillar, SPS Africa, electrical contractors | Good for facility existence, construction/equipment delivery, and rough timing; capacity often absent. | B/C |

Trade-press query templates:

```text
site:datacenterdynamics.com/en/news/ Kenya "data center" "{operator OR county OR town}"
site:datacenterdynamics.com/en/news/ Kenya "data centre" "MW"
site:cioafrica.co Kenya "data centre" "{operator OR county OR town}"
site:techweez.com Kenya "data centre" "{operator OR county OR town}"
site:businessdailyafrica.com Kenya "data centre" "{Konza OR Nairobi OR Olkaria OR Mombasa}"
site:africadca.org Kenya "data centre" Oracle iXAfrica
site:linx.net Kenya "data centers" Nairobi OR Mombasa
```

When reading press, capture the exact lifecycle verb:

- `announces`, `signs MoU`, `plans`, `seeks investors`, `feasibility stage` = planned/intent, usually **C/B**.
- `acquires land`, `breaks ground`, `starts construction`, `completes first phase` = stronger pipeline, **B** unless official.
- `opened`, `launched`, `operational`, `hosts`, `cloud region goes live`, `Uptime certified` = operational signal, verify with operator/Uptime/cloud page for **A**.

---

## 2. Operator and developer sweep

Official operator pages are **A for current claimed locations and facility existence**. Capacity on marketing pages is **A-/B** unless the page gives facility-level IT load or is backed by a primary announcement.

| Operator / developer | Official / primary URL | Kenya county/locality signals | Notes |
|---|---|---|---|
| iXAfrica Data Centres | https://ixafrica.co.ke/ | Nairobi NBOX1; Tilisi/Kiambu NBOX2 future campus | NBOX1 is a core Nairobi hyperscale/AI-ready lead. iXAfrica official news also covers Oracle collaboration and Safaricom AI-ready services. Search `NBOX1`, `NBOX2`, `Tilisi`, `Safaricom iXAfrica`, `Oracle iXAfrica`. |
| Africa Data Centres / Cassava / Liquid Intelligent Technologies | https://www.africadatacentres.com/ and Nairobi page https://www.africadatacentres.com/nairobi/ | Nairobi/Sameer/Mombasa Road area; possible second/third Nairobi facilities | Official page is strong for current NBO1/EADC. Cassava/ADC press releases are key for expansion plans. |
| iColo / Digital Realty | https://www.icolo.io/ , https://www.digitalrealty.com/data-centers/emea/nairobi | Mombasa MBA1/MBA2; Nairobi NBO1/NBO2 | Digital Realty/iColo pages split branding. Search both `iColo` and `Digital Realty`; county attribution can be Nairobi vs Kiambu depending site. |
| PAIX Data Centres | https://www.paix.io/ | Nairobi-1, Britam Tower/Upper Hill | DCD and Africa50 pages provide stronger project detail than the generic PAIX home page. |
| Safaricom | https://www.safaricom.co.ke/wholesale/wholesale_product_categories/data_centre/ | Nairobi, Thika/Kiambu, Kisumu, Limuru/Redhill/Kiambu, Nakuru references | Safaricom wholesale and press pages are official for its cloud/data-centre service. DCD is useful for Limuru/Redhill phase status and MW. |
| Konza Technopolis / Technopolis Development Authority | https://konza.go.ke/ , Konza Cloud https://konza.go.ke/konza-cloud/ | Konza National Data Centre; Machakos/Kajiado/Makueni boundary | Primary source for national data centre and cloud services. Also search PPP Directorate/National Treasury and Business Daily for expansion. |
| Airtel Africa / Nxtra | https://www.airtel.africa/data-centers | Tatu City, Ruiru, Kiambu | Airtel/Nxtra broke ground on East Africa data-centre hub at Tatu City; official Airtel page and Tatu City release are high-signal. |
| Tatu City SEZ | https://www.tatucity.com/ | Ruiru, Kiambu | Official industrial/SEZ source for Nxtra and future data-centre tenant announcements. |
| Tilisi Developments | https://tilisi.co.ke/ | Limuru/Kiambu, iXAfrica NBOX2 | Search Tilisi news plus iXAfrica official announcement; verify exact parcel and county. |
| KenGen Green Energy Park / EcoCloud / G42 | https://greenenergypark.kengen.co.ke/ , https://www.g42.ai/ | Olkaria/Naivasha/Nakuru geothermal campus leads | DCD and Microsoft/G42 releases are important. Treat power-availability disputes and delayed status carefully. |
| Microsoft / Azure | https://news.microsoft.com/ and Azure region docs https://learn.microsoft.com/en-us/azure/reliability/regions-list | Announced East Africa/Kenya cloud-region initiative tied to G42/Olkaria | Official announcement proves intent; physical facility status must be checked against G42/EcoCloud/KenGen and later press. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | Kenya / Nairobi region collaboration with iXAfrica | Official Oracle region pages and iXAfrica/Oracle announcements prove region/service status; do not infer street address beyond host/operator source. |
| Telkom Kenya / Liquid / SimbaNET / Wingu / Angani / Cloudoon / EverseTech | own sites + local press | Nairobi and enterprise/edge facilities | Often smaller or legacy facilities. Use as leads and verify via operator, IXP, Uptime, NCA/county records. |

Vendor/operator query templates:

```text
"{operator}" Kenya "data centre" "MW"
"{operator}" Kenya "data center" "racks"
"{operator}" "{county}" "data centre"
"{operator}" "{town}" ("opened" OR "launched" OR "operational" OR "construction" OR "breaks ground")
site:{operator-domain} Kenya "data centre"
site:{operator-domain} Nairobi OR Mombasa OR Tatu OR Tilisi OR Konza OR Olkaria
"{operator}" "Uptime Institute" Kenya
"{operator}" "Tier III" Kenya "data centre"
```

---

## 3. Official and semi-official channels to pivot from press

This file focuses industry/press/vendor discovery, but every press lead should be verified against one or more of these primary routes.

| Channel | URL / route | How to use | Grade |
|---|---|---|---|
| Nairobi Planning and Development Management System | https://edev.nairobiservices.go.ke/ and Nairobi notices https://nairobi.go.ke/public-notice-weekly-approvals-construction-permits | For Nairobi City County buildings. Search web-indexed weekly approvals and portal references for applicant/site names; portal may require account for deep records. | A when permit record found |
| Kenya eRegulations / InvestKenya eProcedures | https://eprocedures.investkenya.go.ke/ | Gives county construction permit process pages and participating counties. Use to identify correct county route. | A for process |
| National Construction Authority (NCA) | https://www.nca.go.ke/ | All construction projects should be registered. Public search is limited, but NCA references and contractor pages can confirm construction. | A when record found |
| NEMA / EIA public notices | https://www.nema.go.ke/ and `site:nema.go.ke "data centre"` | Large new datacentres may appear through EIA study reports, waste/noise/generator notices, or public comments. Also search project PDFs by operator/site. | A |
| PPP Directorate / National Treasury | https://www.pppunit.go.ke/ and Treasury pages | Konza expansion and other PPP proposals may appear at concept/feasibility/procurement stage. | A for project-stage disclosure |
| Konza / Technopolis Development Authority | https://konza.go.ke/ | National Data Centre, Konza Cloud, SEZ plans, investor and public notices. | A |
| Tatu City SEZ | https://www.tatucity.com/ | Tenant/developer announcements and data-centre hub language for Kiambu. | A/B |
| KenGen / Green Energy Park | https://www.kengen.co.ke/ , https://greenenergypark.kengen.co.ke/ | Olkaria geothermal-powered datacentre projects, energy park plots, power availability. | A/B |
| County CIDP / ADP / budget PDFs | county websites; aggregator https://countydevelopmentplan.com/ only as locator | County "data centre" may mean GIS, county stats, server room, call centre, or e-government centre. Count as datacentre only if it has hosting/colocation/computing function and location evidence. | A for county plan text; B/C for facility interpretation |
| Uptime Institute Awards | https://uptimeinstitute.com/uptime-institute-awards/ | Confirms named certified facilities such as Konza and Safaricom Thika. | A for certification record |

Official-search templates:

```text
site:nema.go.ke Kenya ("data centre" OR "data center" OR datacentre) EIA
site:nema.go.ke "{operator}" "{town}"
site:nairobi.go.ke "data centre" "construction permit"
site:nairobi.go.ke "{operator}" "permit"
site:nca.go.ke "{operator}" "data centre"
site:pppunit.go.ke Konza "Data Centre"
site:konza.go.ke "data centre" OR "data center" OR "cloud"
site:tatucity.com "data centre" OR "data center" OR Nxtra OR Airtel
site:greenenergypark.kengen.co.ke "data centre" OR "data center" OR EcoCloud
"{county}" "County Integrated Development Plan" "data centre"
"{county}" "Annual Development Plan" "data centre"
```

---

## 4. English and Swahili search patterns

### 4.1 English discovery templates

Use county + town + operator terms. For Nairobi-market projects, always run a second pass with the physical localities in Kiambu/Machakos/Kajiado/Nakuru because press often says "Nairobi" for nearby counties.

```text
"{county}" Kenya ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks OR "IT load")
"{town}" Kenya ("data centre" OR "data center") ("opened" OR launched OR operational OR construction OR "breaks ground")
"{town}" Kenya ("colocation" OR "carrier-neutral" OR hyperscale OR "AI-ready")
"{county}" Kenya ("cloud region" OR "sovereign cloud" OR "public cloud")
"{county}" Kenya ("Tier III" OR "Uptime Institute") "data centre"
"{county}" Kenya ("substation" OR geothermal OR "green energy") "data centre"
"{industrial park OR SEZ}" Kenya "data centre"
"{operator}" "{county OR town}" Kenya "data centre"
```

Capacity/status pivot:

```text
"{project name}" ("MW" OR "IT load" OR MVA OR racks OR sqm OR "square metres")
"{project name}" ("phase one" OR "phase 1" OR "phase two" OR expansion)
"{project name}" ("EIA" OR NEMA OR "construction permit" OR NCA OR "Uptime")
"{project name}" ("opened" OR operational OR "goes live" OR "ready for service")
```

### 4.2 Swahili / local-language secondary checks

Most Kenyan datacentre business reporting is English. Use Swahili only for county-government ICT projects and local press discovery, then verify against official English documents.

Useful terms:

- data centre: `kituo cha data`, `kituo cha kuhifadhi data`
- server room: `chumba cha seva`
- ICT centre: `kituo cha TEHAMA`
- cloud: `wingu`, usually appears as English `cloud`
- launch/opening: `kuzindua`, `uzinduzi`, `imezinduliwa`
- construction: `ujenzi`, `kujenga`

Templates:

```text
"{county}" "kituo cha data"
"{county}" "chumba cha seva"
"{county}" "kituo cha TEHAMA" "data"
"{town}" "kituo cha data" Kenya
```

Do not count a Swahili/local hit as a commercial datacentre unless it identifies a physical facility with compute/hosting function, operator/developer, and stage.

---

## 5. County-level enumeration method

For each of the 47 counties, run four passes:

1. **Commercial press/vendor pass**: county + main towns + `data centre/data center/datacentre/colocation/hyperscale/cloud region`.
2. **Operator pass**: known Kenya operators + county/town (`iXAfrica`, `Africa Data Centres`, `iColo`, `Digital Realty`, `PAIX`, `Safaricom`, `Airtel`, `Nxtra`, `Konza`, `KenGen`, `EcoCloud`, `G42`, `Oracle`, `Microsoft`, `Telkom`, `Liquid`, `SimbaNET`, `Wingu`, `Angani`).
3. **Permit/official pass**: county construction permit notices, NCA, NEMA, CIDP/ADP/budget PDFs, SEZ/industrial park pages.
4. **Interconnection/aggregator pass**: LINX, KIXP, PeeringDB, Baxtel, DataCenterMap, OCOLO, Inflect for legacy/edge sites; verify before grading above C/B-.

Universal county recipe:

```text
"{county}" Kenya "data centre"
"{county}" Kenya "data center"
"{county}" Kenya datacentre
"{county}" Kenya colocation
"{county}" Kenya hyperscale
"{county}" Kenya "cloud region"
"{county}" Kenya "Tier III" "data"
"{county}" Kenya "server room" "data centre"
"{county}" Kenya "construction permit" "data centre"
"{county}" Kenya NEMA "data centre"
"{county}" Kenya "County Integrated Development Plan" "data centre"
site:datacenterdynamics.com/en/news/ Kenya "{county}"
site:cioafrica.co Kenya "{county}" "data centre"
site:businessdailyafrica.com Kenya "{county}" "data centre"
site:techweez.com Kenya "{county}" "data centre"
```

### 5.1 Priority county clusters

| County | Main towns/localities | Developer/operator seeds | County query notes |
|---|---|---|---|
| Nairobi City | Sameer/Mombasa Road, Karen/Langata, Upper Hill, CBD/Moi Ave/Koinange, Embakasi/Industrial Area | iXAfrica NBOX1, Africa Data Centres/EADC, iColo/Digital Realty NBO1/NBO2, PAIX, Telkom, Safaricom, Liquid, SimbaNET, Angani/Wingu | Search Nairobi plus named roads and towers. Use Nairobi planning portal/weekly approvals, LINX Nairobi, KIXP, PeeringDB, Uptime. Watch for facilities marketed as Nairobi but physically in Kiambu. |
| Kiambu | Tatu City/Ruiru, Thika, Limuru, Redhill, Tilisi, Tigoni, Juja | Nxtra/Airtel, Safaricom Thika, Safaricom Limuru/Redhill, iXAfrica NBOX2/Tilisi, Tatu City, Tilisi | Highest non-Nairobi priority. Query `Tatu City data centre`, `Ruiru data center`, `Tilisi iXAfrica`, `Thika Safaricom`, `Limuru Redhill data centre`. |
| Mombasa | Miritini, Nyali, Mombasa Island/Port, Changamwe | iColo/Digital Realty MBA1/MBA2, LINX Mombasa, subsea cable operators, possible telco/enterprise sites | Search submarine cable and IXP terms. Mombasa results are often interconnection-focused; verify facility owner and exact site. |
| Machakos | Konza, Malili, Mlolongo/Athi River | Konza National Data Centre, Technopolis Development Authority, Huawei, Konza Cloud, older Equity/EACP Konza plans | Konza is commonly described as 64-80 km south of Nairobi along Mombasa Road. Use Konza official/PPP/Uptime first; press may say Machakos, Kajiado, or Makueni. |
| Kajiado | Konza buffer zone, Kitengela, Isinya, Athi River outskirts | Konza/Technopolis boundary, possible SEZ/industrial land | Include Konza boundary caveat. Search county planning and Konza public notices; do not double-count the same Konza National Data Centre across counties without parcel evidence. |
| Makueni | Konza buffer zone, Malili, Sultan Hamud | Konza/Technopolis boundary | Same Konza caveat. Treat Makueni as boundary/beneficiary unless primary documents locate the specific data-centre parcel in Makueni. |
| Nakuru | Naivasha, Olkaria, KenGen Green Energy Park, Nakuru town | EcoCloud Project Eagle, KenGen, G42, Microsoft, Safaricom Nakuru, geothermal-powered campuses | Search power and industrial-park terms: `Olkaria`, `Naivasha`, `geothermal`, `KenGen Green Energy Park`, `Project Eagle`, `G42 EcoCloud`. Verify if project is active, delayed, or scaled. |
| Kisumu | Kisumu town, Kiboswa/Daraja Mbili, Lake Victoria corridor | Safaricom Kisumu, telco/edge, county ICT | Likely edge/DR rather than hyperscale. Search Safaricom and aggregator leads, then verify with Safaricom/county docs. |
| Vihiga | Mbale, county GIS/data centre | County Government of Vihiga | Likely government GIS/statistics data centre. Capture separately from commercial colocation; use CIDP/ADP and county reports. |

Priority-cluster templates:

```text
"Nairobi" Kenya ("iXAfrica" OR "Africa Data Centres" OR iColo OR PAIX OR Safaricom) "data centre"
"Kiambu" OR "Tatu City" OR Ruiru OR Thika OR Limuru OR Redhill OR Tilisi "data centre" Kenya
"Mombasa" Kenya (iColo OR "Digital Realty" OR LINX OR "subsea cable") "data centre"
"Konza" ("data centre" OR "data center" OR "cloud" OR PPP OR Huawei OR Uptime)
"Olkaria" OR Naivasha OR "KenGen Green Energy Park" ("data centre" OR "data center" OR EcoCloud OR G42 OR Microsoft)
"Kisumu" Kenya Safaricom "data centre"
```

### 5.2 Secondary county sweep

These counties have lower commercial probability. Use the universal recipe plus the named county capital/industrial area, and expect mostly negative results or county-government ICT rooms.

| County group | Counties | Main query additions |
|---|---|---|
| Western and Lake Victoria | Bungoma, Busia, Homa Bay, Kakamega, Migori, Siaya, Vihiga | Add county capital, `county data centre`, `ICT centre`, `GIS`, `server room`, `Safaricom`, `Kisumu` for nearby spillover. |
| Rift Valley excluding Nakuru | Baringo, Bomet, Elgeyo/Marakwet, Kericho, Laikipia, Nandi, Narok, Samburu, Trans Nzoia, Turkana, Uasin Gishu, West Pokot | Add `geothermal`, `wind`, `solar`, `industrial park`, `Eldoret`, `Suswa`, but require datacentre-specific proof. Avoid counting power projects with no DC tenant. |
| Central and Mount Kenya | Embu, Kirinyaga, Meru, Murang'a, Nyandarua, Nyeri, Tharaka-Nithi | Add `county ICT`, `digital hub`, `server room`, `CIDP`; commercial hyperscale unlikely outside Kiambu spillover. |
| Coast excluding Mombasa | Kilifi, Kwale, Lamu, Taita/Taveta, Tana River | Add `SEZ`, `LAPSSET`, `subsea cable`, `port`, `Dongo Kundu`; watch for speculative LAPSSET/digital-infrastructure pages with no named facility. |
| Eastern and North Eastern | Garissa, Isiolo, Kitui, Mandera, Marsabit, Wajir | Add `county data centre`, `ICT hub`, `server room`, `CIDP`; most hits are e-government/data collection, not DC facilities. |
| South Eastern/Konza-adjacent | Machakos, Makueni, Kajiado | Search Konza-specific terms and county public notices. Keep one canonical Konza record unless parcel-level docs justify county-specific phases. |
| South Nyanza / Highlands | Kisii, Nyamira | Add `county ICT`, `server room`, `Safaricom`, `CIDP`; expect negative/edge only. |

### 5.3 Exact 47-county quick queries

Use these as first-pass copy/paste seeds:

```text
Baringo Kenya "data centre" OR "data center" OR datacentre
Bomet Kenya "data centre" OR "data center" OR datacentre
Bungoma Kenya "data centre" OR "data center" OR datacentre
Busia Kenya "data centre" OR "data center" OR datacentre
"Elgeyo Marakwet" Kenya "data centre" OR "data center" OR datacentre
Embu Kenya "data centre" OR "data center" OR datacentre
Garissa Kenya "data centre" OR "data center" OR datacentre
"Homa Bay" Kenya "data centre" OR "data center" OR datacentre
Isiolo Kenya "data centre" OR "data center" OR datacentre
Kajiado Kenya "Konza" "data centre"
Kakamega Kenya "data centre" OR "data center" OR datacentre
Kericho Kenya "data centre" OR "data center" OR datacentre
Kiambu Kenya ("Tatu City" OR Thika OR Limuru OR Redhill OR Tilisi) "data centre"
Kilifi Kenya "data centre" OR "data center" OR datacentre
Kirinyaga Kenya "data centre" OR "data center" OR datacentre
Kisii Kenya "data centre" OR "data center" OR datacentre
Kisumu Kenya Safaricom "data centre"
Kitui Kenya "data centre" OR "data center" OR datacentre
Kwale Kenya "data centre" OR "data center" OR datacentre
Laikipia Kenya "data centre" OR "data center" OR datacentre
Lamu Kenya "data centre" OR "data center" OR datacentre
Machakos Kenya "Konza" "data centre"
Makueni Kenya "Konza" "data centre"
Mandera Kenya "data centre" OR "data center" OR datacentre
Marsabit Kenya "data centre" OR "data center" OR datacentre
Meru Kenya "data centre" OR "data center" OR datacentre
Migori Kenya "data centre" OR "data center" OR datacentre
Mombasa Kenya (iColo OR "Digital Realty" OR LINX OR "subsea") "data centre"
"Murang'a" Kenya "data centre" OR "data center" OR datacentre
"Nairobi City" Kenya (iXAfrica OR iColo OR "Africa Data Centres" OR PAIX OR Safaricom) "data centre"
Nakuru Kenya (Olkaria OR Naivasha OR KenGen OR EcoCloud OR G42 OR Microsoft) "data centre"
Nandi Kenya "data centre" OR "data center" OR datacentre
Narok Kenya "data centre" OR "data center" OR datacentre
Nyamira Kenya "data centre" OR "data center" OR datacentre
Nyandarua Kenya "data centre" OR "data center" OR datacentre
Nyeri Kenya "data centre" OR "data center" OR datacentre
Samburu Kenya "data centre" OR "data center" OR datacentre
Siaya Kenya "data centre" OR "data center" OR datacentre
"Taita Taveta" Kenya "data centre" OR "data center" OR datacentre
"Tana River" Kenya "data centre" OR "data center" OR datacentre
"Tharaka Nithi" Kenya "data centre" OR "data center" OR datacentre
"Trans Nzoia" Kenya "data centre" OR "data center" OR datacentre
Turkana Kenya "data centre" OR "data center" OR datacentre
"Uasin Gishu" Kenya "data centre" OR "data center" OR datacentre
Vihiga Kenya "data centre" OR "data center" OR "county data center"
Wajir Kenya "data centre" OR "data center" OR datacentre
"West Pokot" Kenya "data centre" OR "data center" OR datacentre
```

---

## 6. Hyperscaler and cloud-region handling

Cloud-provider pages prove region/service existence, not physical facility addresses. Kenya cloud-region announcements often involve a local host/operator.

| Provider | Official/primary URL | Kenya signal | How to use |
|---|---|---|---|
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ plus iXAfrica/Oracle announcement on https://ixafrica.co.ke/ and https://africadca.org/ | Kenya/Nairobi public cloud region hosted with iXAfrica | Grade A for provider/host announcement; verify whether service is live and map to iXAfrica only if source says so. |
| Microsoft Azure / G42 | Microsoft announcement https://news.microsoft.com/source/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/ | Planned East Africa/Kenya cloud region tied to geothermal Olkaria campus | Grade A for announcement, but DCD/Semafor/Business Insider reporting in 2026 says project faced power-capacity delays. Status must be current before counting as construction/operational. |
| AWS / Google Cloud | official region pages | No public Kenya region in standard global region lists as of this methodology date | Search for local edge/Outposts/PoP partnerships separately; do not infer hyperscale DC. |
| Safaricom cloud / Konza Cloud / sovereign cloud | Safaricom wholesale/cloud pages; https://konza.go.ke/konza-cloud/ | Kenya-hosted cloud/data sovereignty services | Treat as operator/service evidence; physical facility must be mapped to Safaricom/Konza/iXAfrica pages. |

Cloud query templates:

```text
"Oracle" Kenya "cloud region" iXAfrica Nairobi
"Microsoft" G42 Kenya "data center" Olkaria
"Azure" "East Africa" Kenya "data centre"
"Safaricom" Kenya "cloud" "data centre" Nairobi Kisumu
"Konza Cloud" "data centre" Kenya
"sovereign cloud" Kenya "data centre"
```

---

## 7. Evidence grading and common pitfalls

### 7.1 Grade per data point

- **A**: operator official location page; official cloud-provider region page; Uptime Institute certification page; Konza/Tatu/KenGen/PPP/NCA/NEMA/county approval document; Safaricom/Airtel/Digital Realty/iXAfrica official release.
- **B**: DCD, CIO Africa, Business Daily, Techweez, Africa Data Centres Association, LINX/KIXP announcements, credible vendor case studies.
- **C**: aggregator facility pages, market-report snippets, social posts, LinkedIn capacity claims, old Konza investor-interest articles, LAPSSET/digital corridor pages without named facility.

### 7.2 Kenya-specific pitfalls

- **Nairobi market vs county**: Limuru, Thika, Tatu City, Tilisi, and Redhill may be called Nairobi in press but sit in Kiambu or nearby counties. Assign to the physical county when evidence allows.
- **Konza boundary ambiguity**: Konza is variously tied to Machakos, Kajiado, and Makueni. Keep a single canonical Konza facility record unless primary parcel or phase documents show distinct county locations.
- **Old Konza investor intentions**: 2013-2015 stories about Equity Bank, EACP/Kooba, JamboPay, and other booked parcels are intent only unless later construction/operator evidence appears.
- **Government "data centre" ambiguity**: CIDPs may use "data centre" for GIS/statistics office, records centre, contact centre, or server room. Count as a datacentre only if the facility stores/processes/hosts digital workloads and has site/operator/status evidence.
- **Aggregator county errors**: Nairobi/Mombasa/Kiambu addresses are often normalized incorrectly. Cross-check with roads, estates, and official operator pages.
- **Capacity inflation**: Campus ultimate buildout, MVA utility capacity, and IT load MW are not interchangeable. Record the unit and phase exactly.
- **Delayed mega-projects**: Microsoft/G42/Olkaria-style projects require current-status verification because power capacity and commercial terms can stall otherwise official announcements.

### 7.3 Minimum record fields

For each project, capture:

- canonical facility/campus name and aliases;
- physical county, town/locality, road/park/SEZ if known;
- owner/operator/developer and local SPV if visible;
- status and status evidence date;
- capacity with unit: IT MW, total power/MVA, racks, sqm, data halls;
- source URLs and evidence grade by field;
- notes on county ambiguity, phase/buildout, and whether it is commercial, government, edge, or enterprise-only.

---

## 8. Recommended Kenya discovery order

1. Seed Nairobi/Kiambu/Mombasa/Konza/Olkaria from operator official pages: iXAfrica, Africa Data Centres, iColo/Digital Realty, Safaricom, PAIX, Konza, Airtel/Nxtra, Tatu City, KenGen/EcoCloud/G42.
2. Search DCD, CIO Africa, Business Daily, Techweez, AfricaDCA, LINX/KIXP for each seed; extract aliases, MW, phase, and status verbs.
3. Verify high-value builds through NEMA/NCA/county planning, Uptime, PPP, SEZ, or official operator releases.
4. Run county recipes for all 47 counties. For low-probability counties, stop after press/vendor + CIDP/ADP + NEMA/NCA negative sweep unless a named operator or facility emerges.
5. Resolve county assignment manually for Nairobi-market spillover and Konza boundary projects before deduplication.
