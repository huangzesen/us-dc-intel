# IL Explorer Official - Israel Datacenter Enumeration via Planning, Energy, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Scope: Israel (IL), six district divisions: HaDarom, Hefa, Yerushalayim, HaMerkaz, Tel Aviv, HaTsafon. Angle: **official/regulatory/cloud pipeline**. Reliability grades: **A** = official/primary source (government planning portal, Electricity Authority/IEC/Noga, operator official page, cloud provider documentation, securities filing), **B** = strong secondary/trade press with named parties, **C** = weak aggregate/marketing-only/unverified.

---

## 0. Israel-specific structural facts

- Israel has a usable national planning backbone through the Planning Administration, but datacenter enumeration is still a **Hebrew-first statutory-plan and local-committee exercise**. Use national systems to find plans and documents, then pivot to the relevant district/local planning committee, municipality, industrial-zone company, and operator.
- The main public planning systems are **Mavat / Planning Information** (`מידע תכנוני`) and **XPlan / blue-line map** (`קווים כחולים`). Mavat is the statutory record for plans, requests, appeals, committee agendas, protocols, and decisions. XPlan is a map helper for online-submitted plans from 2011 onward and warns that statutory/current data must be checked in Mavat.
- Large projects may move through national-infrastructure treatment. Government decision 3907 of 2026 (`קידום הקמת חוות שרתים מתקדמות לחיזוק ההובלה של ישראל בתחום הבינה המלאכותית`) frames advanced data centers as strategic AI infrastructure and references transmission-grid connection deadlines and mapping of candidate areas against national/district plans.
- Electricity is the gating official source. In 2026 the Electricity Authority published a temporary decision suspending examination/response procedures for connecting data-center facilities of **8 MVA and above**, and a separate hearing on adding standards for consumers with connection size of **50 MVA and above** to the transmission grid. Treat these as Grade A context and as prompts to search project names in grid/connection proceedings.
- Cloud regions prove only region existence and metro-level demand. AWS, Google Cloud, Microsoft Azure, and Oracle have Israel/Tel Aviv/Jerusalem region signals, but they do not publish exact AZ/building locations. Use cloud pages as seed evidence, then verify facilities through planning, energy, operator, or filings.

Key Hebrew lifecycle vocabulary:

`יוזמה` < `תכנית` / `תב"ע` < `הפקדה` < `פרסום להתנגדויות` < `דיון בוועדה` < `אישור תכנית` < `בקשה להיתר` < `היתר בנייה` < `תחילת עבודות` / `עלייה לקרקע` < `הפעלה מסחרית`

Only count `היתר בנייה`, construction-start, operator commissioning, or stronger as construction evidence. Treat announced land, plan filing, grid request, or cloud-region language as planned/lead evidence until cross-checked.

---

## 1. Hebrew and English query patterns

### 1.1 Core Hebrew search terms

Use Hebrew first for planning, grid, municipal, and exchange filings.

```
חוות שרתים
מרכז נתונים
דאטה סנטר
דטה סנטר
מתקן מחשוב
מתקן מחשוב על
תשתיות מחשוב
בינה מלאכותית חוות שרתים
בקשה להיתר חוות שרתים
היתר בנייה חוות שרתים
תכנית חוות שרתים
תב"ע חוות שרתים
מתחם חוות שרתים
אזור תעשייה חוות שרתים
תחנת משנה חוות שרתים
חיבור לרשת החשמל חוות שרתים
מו"א חוות שרתים
מגה-ואט חוות שרתים
גנרטורים חוות שרתים
מיגון תת קרקעי חוות שרתים
```

### 1.2 English search terms

English is better for hyperscale, international operators, and trade press.

```
"Israel" "data center" "planning"
"Israel" "data center" "building permit"
"Israel" "data center" "grid connection"
"Israel" "data center" "MVA"
"Israel" "data center" "substation"
"Tel Aviv" "data center" "MW"
"Petah Tikva" "data center" "Digital Realty"
"Kfar Yona" "data center" "MedOne"
"Beit Shemesh" "data center" "Mega DC"
"Ashdod" "data center" "Dalia" "Serverfarm"
```

### 1.3 Portal-scoped query templates

```
site:iplan.gov.il "חוות שרתים"
site:mavat.iplan.gov.il "חוות שרתים"
site:ags.iplan.gov.il "חוות שרתים"
site:gov.il "חוות שרתים" "רשות החשמל"
site:gov.il "חוות שרתים" "מינהל התכנון"
site:gov.il "חיבור" "חוות שרתים" "מו\"א"
site:iec.co.il "חוות שרתים"
site:noga-iso.co.il "חוות שרתים"
site:maya.tase.co.il "חוות שרתים"
site:mayafiles.tase.co.il "Digital Realty Mivne"
site:mayafiles.tase.co.il "חוות שרתים" "מגה אור"
```

---

## 2. Grade A official/regulatory sources

### 2.1 Planning Administration: national planning and permit backbone

- **Planning Administration / IPlan**: https://www.iplan.gov.il/. Grade A national planning authority. Use for planning-policy pages, national/district plan context, and links into plan-search tools.
- **Mavat - Planning Information**: https://mavat.iplan.gov.il/ and plan/request/hearing search entry https://mavat.iplan.gov.il/SV3?searchEntity=3&searchMethod=2. Grade A. Search Hebrew keywords, exact operator/SPV, industrial-zone names, and plan numbers. Extract plan number, district/local committee, land block/parcel, purpose, permitted uses, building rights, committee decisions, and attached PDFs.
- **XPlan / blue-line map**: https://ags.iplan.gov.il/xplan/. Grade A map helper, not final statutory evidence. Use to map plan polygons and identify neighboring substations/industrial zones; confirm details in Mavat.
- **Planning map services**: https://ags.iplan.gov.il/services/. Grade A GIS route for spatial checks. Use when a plan number or area is known and Mavat text search is insufficient.
- **Government decision 3907 (2026)**: https://www.gov.il/he/pages/dec3907-2026. Grade A policy source for advanced datacenter acceleration, AI infrastructure, preferred-grid geography, and national-infrastructure treatment.

Mavat workflow:

1. Search by Hebrew terms (`חוות שרתים`, `מרכז נתונים`, `מתקן מחשוב על`) and by English operator names.
2. Filter/inspect by district: Southern (`דרום`), Haifa (`חיפה`), Jerusalem (`ירושלים`), Central (`מרכז`), Tel Aviv (`תל אביב`), Northern (`צפון`).
3. Open plan details and attached documents: `הוראות`, `תשריט`, `נספחים`, `פרוטוקולים`, `החלטות`.
4. Extract: plan number, site locality, industrial zone, block/parcel, applicant/developer, land-use designation, built area sqm, underground floors, power/MVA/MW, generator/fuel/cooling notes, committee status, publication/approval dates.
5. Search the exact plan number on the municipality/local committee site and in web search. Local pages may expose building-permit (`בקשה להיתר`) details not obvious in Mavat.

Official planning document phrases to look for:

```
מטרת התכנית
עיקרי הוראות התכנית
שימושים מותרים
זכויות בנייה
קומות תת קרקעיות
תחנת משנה
חדרי חשמל
גנרטורים
מערכות קירור
נספח סביבתי
נספח תנועה
נספח תשתיות
החלטת ועדה
פרוטוקול
```

### 2.2 Electricity Authority, IEC, and Noga

- **Electricity Authority decisions/hearings hub**: https://www.gov.il/he/departments/topics/decisions-and-hearings. Grade A. Search decisions and hearings for datacenters, large consumers, connection queues, and grid-allocation criteria.
- **Decision 74506 (temporary suspension for data-center connections of 8 MVA+)**: https://www.gov.il/he/pages/74506. Grade A. Use as a 2026 rule/context source and as a reason to check whether a project has already secured power.
- **Hearing on adding standards for consumers of 50 MVA+ connected to the transmission grid**: https://www.gov.il/he/pages/shimam50hibur. Grade A. The attached review (`skira_shim_50.pdf`) is especially useful for national grid impacts and the phrase `תשתיות מחשוב על`.
- **Ministry of Finance/Energy interim recommendations press release (2026-02-19)**: https://www.gov.il/he/pages/press_190226. Grade A. It recommends prioritizing datacenters outside central Israel, shortening planning in preferred areas, and preventing speculative grid reservations.
- **IEC connection-probability map**: https://www.iec.co.il/content/renewableenergy/contentpages/probabilitymap. Grade A map helper. It is designed for connection probability by address; use for early geography screening, then verify with project-specific IEC/Noga/Electricity Authority evidence.
- **IEC corporate site**: https://www.iec.co.il/ and English/global page https://iec-global.com/. Grade A for IEC role and project references when published.
- **Noga, Israel Independent System Operator**: https://www.noga-iso.co.il/. Grade A for transmission-system planning context and official materials when searchable by project/operator.

Energy workflow:

1. For every planned or construction project, search exact project/operator plus `חיבור לרשת`, `מו"א`, `MVA`, `תחנת משנה`, `רשת ההולכה`, `חברת החשמל`, `נגה`, and `רשות החשמל`.
2. Record whether power is secured, requested, suspended, or speculative. This is critical in Israel because official policy changed for 8 MVA+ data-center connections in 2026.
3. Treat trade claims such as "secured power" as B unless confirmed by an Electricity Authority decision, IEC/Noga material, planning document, or securities filing.
4. Extract connection size separately from IT load. Israeli documents may state `מו"א`/MVA, total facility MW, or IT MW; do not convert without noting the assumption.

### 2.3 Ministry of Communications and telecom licensing

- **Ministry of Communications**: https://www.gov.il/en/departments/ministry_of_communications and Hebrew site https://www.gov.il/he/departments/ministry_of_communications. Grade A for telecom regulatory context.
- **General/unified license page**: https://www.gov.il/he/pages/lic. Grade A for telecom licensees and service categories, including Bezeq International and other carriers that may operate datacenter, hosting, transmission, or submarine-cable-adjacent services.
- **Communications Law page**: https://www.gov.il/he/pages/communication_law. Grade A for legal context.
- Example Bezeq International unified license PDF: https://www.gov.il/BlobFolder/policy/09062022_9/he/fix-Licenses-bezeq-27.pdf. Grade A for licensee identity; not facility evidence by itself.

Use Ministry of Communications sources to validate telecom operators, submarine/fiber providers, and license status. Do not treat a communications license as evidence that a datacenter exists at a specific site.

### 2.4 Securities filings and public-company disclosures

- **TASE/MAYA disclosures**: https://maya.tase.co.il/ and file host https://mayafiles.tase.co.il/. Grade A when the filing is by the listed company. Search Hebrew and English for `חוות שרתים`, `Data Center`, `Digital Realty Mivne`, `מגה אור`, `מבנה`, `לוינשטין`, `נבידיה`, `Nebius`.
- Example Digital Realty/Mivne filing PDF: https://mayafiles.tase.co.il/rpdf/1456001-1457000/P1456371-00.pdf. Grade A for the JV announcement; it states Digital Realty Mivne was formed to develop and operate a major colocation datacenter campus in Israel.

Use filings for capacity, capex, tenant/leasing, land acquisition, and delivery timing. Cross-check with planning and grid evidence before marking construction.

---

## 3. Official cloud-region seed list

Cloud regions are Grade A for provider/region existence only; they are not facility addresses.

| Provider | Official source | Israel signal | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/local/israel/ and AWS regions doc https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | AWS Israel (Tel Aviv) Region, `il-central-1`, 3 Availability Zones | Seed Tel Aviv/Central searches; connect to Project Nimbus; do not infer exact AZ towns. |
| Google Cloud | Locations https://cloud.google.com/about/locations and Compute zones https://docs.cloud.google.com/compute/docs/regions-zones | Tel Aviv, Israel region `me-west1` with zones `me-west1-a/b/c` | Seed Tel Aviv/Central and Nimbus searches; verify physical facilities separately. |
| Microsoft Azure | Azure regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list and Microsoft Israel region announcement https://news.microsoft.com/source/emea/features/microsoft-to-launch-new-cloud-datacenter-region-in-israel/ | Israel Central / Israel geography, local datacenter region | Treat as a cloud-market seed. DCD/local press mention Modi'in-area speculation, but exact sites need primary confirmation. |
| Oracle Cloud | OCI regions https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and public cloud regions https://www.oracle.com/cloud/public-cloud-regions/ | Israel/Jerusalem region signal in Oracle materials and trade coverage | Known public reporting ties Oracle/Bynet to an underground Jerusalem facility; use operator/planning evidence for facility record. |
| Project Nimbus | Government press page https://www.gov.il/en/pages/press_01082023_b and Google Cloud Nimbus post https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-selected-to-provide-cloud-services-to-the-state-of-israel | Government cloud procurement led by AWS and Google | Use as demand/tenant context, not a facility address list. |

---

## 4. Colo/operator official seed list

Operator pages are Grade A for facilities and capacity when directly stated by the operator. Still pivot to planning/grid for permit and construction status.

| Operator | Official source | High-yield divisions/sites | Notes |
|---|---|---|---|
| MedOne | https://medone.co.il/, about https://medone.co.il/about-medone, expansion/news pages | HaMerkaz: Kfar Yona, Ramle/Ramla, Petah Tikva; Hefa: Tirat HaCarmel; HaDarom: Dimona lead | Official site says 25,000+ sqm across four secure underground sites and seven additional sites under development/construction. |
| Bynet Data Centers | https://bynetdcs.co.il/ | Yerushalayim: Jerusalem of Gold/Silver/Light; HaMerkaz: Shoham, Lod; Tel Aviv | Official site lists protected underground facilities in Jerusalem, TLV, Shoham, and Lod, with rack/MW/sqm details by site. |
| Bezeq International | https://www.bezeqint.net/en and MOC license sources | Tel Aviv, Petah Tikva/Central, submarine/fiber-adjacent sites | Official telecom/operator source; use MOC license and operator pages for identity, aggregators only as C/B for individual facility addresses. |
| Serverfarm | ISR1 official page https://www.serverfarmllc.com/tel-aviv-data-center/ and locations https://www.serverfarmllc.com/data-centers/ | Tel Aviv / north Tel Aviv / Herzliya-Hof HaSharon area; HaDarom: Dalia/Ofek lead via trade press | Official ISR1 page confirms first Middle East facility in North Tel Aviv. |
| Digital Realty / Mivne | Official press release https://www.digitalrealty.com/about/newsroom/press-releases/122655/digital-realty-announces-joint-venture-with-mivne-to-develop-new-colocation-and-connectivity-hub-in-israel-and-expand-mediterranean-presence; Mivne https://en.mivnegroup.co.il/ | HaMerkaz: Petah Tikva | Digital Realty states JV with Mivne for a multi-tenant campus in Petah Tikva up to 20 MW IT load. |
| Equinix | EMEA official page https://www.equinix.com/data-centers/europe-colocation | Israel/Tel Aviv only if official marketplace/location pages appear | No clear official Tel Aviv facility page found in first-pass search; treat `Equinix TL` claims from aggregators as unverified until an Equinix source is found. |
| DigiTel / spelling check | No official Israeli datacenter operator source found for `DigiTel` in first-pass search | N/A | Likely confusion with **Digital Realty** or Hebrew `דיגיטל ריאלטי`. Keep `DigiTel` as a search alias, but do not create a facility from it without a primary source. |
| Mega Data Centers / Mega DC | https://www.megadc.com/our-sites | Hefa: MATAM Haifa; HaMerkaz/Yerushalayim boundary: Beit Shemesh, Modi'in; HaDarom: Idan HaNegev; Tel Aviv/Central: Masmia; HaTsafon/Hadera lead | Official sites page lists Israeli AI datacenter projects and power/size/site information. |
| Global Technical Realty | https://globaltechnicalrealty.com/ and project news | HaMerkaz: Petah Tikva IS One | Operator news is Grade A for announced facility details; check Mavat and local committee for permit proof. |
| NED Data Centers | https://www.ned-dc.com/ | HaMerkaz: Netanya | Official project pages plus TASE/partner filings are stronger than trade coverage. |
| IDCA Israel Data Center Association | https://idca.org.il/ | National | Industry ecosystem source. Use for contacts/events/market visibility, not as a primary facility census unless it publishes named facility data. |

---

## 5. District-by-district enumeration routing

Israel divisions in the repo use English district names, but searches should include Hebrew district/locality names.

| Repo division | Hebrew district/locality anchors | Primary official route | Priority datacenter pivots |
|---|---|---|---|
| HaDarom | `מחוז דרום`, Ashdod `אשדוד`, Dimona `דימונה`, Idan HaNegev `עידן הנגב`, Yoav/Masmia `מסמיה` | Mavat district filter + IEC/Noga grid searches + district/municipal plans | Dalia/Serverfarm/IIF Ofek near Ashdod; Mega DC Idan HaNegev; MedOne Dimona; energy siting outside central Israel. |
| Hefa | `מחוז חיפה`, Haifa `חיפה`, MATAM `מת"ם`, Tirat HaCarmel `טירת כרמל`, Hadera `חדרה` | Mavat + Haifa/Tirat HaCarmel local committee + port/subsea/IEC sources | MedOne Tirat HaCarmel; Mega DC MATAM Haifa; Bynet/edge and subsea-cable adjacency leads. |
| Yerushalayim | `מחוז ירושלים`, Jerusalem `ירושלים`, Har Hotzvim `הר חוצבים`, Beit Shemesh `בית שמש` | Mavat + Jerusalem/Beit Shemesh local planning + operator official pages | Bynet Jerusalem sites; Oracle/Bynet Jerusalem region/facility; Mega DC Beit Shemesh (check division boundary carefully). |
| HaMerkaz | `מחוז מרכז`, Petah Tikva `פתח תקווה`, Kfar Yona `כפר יונה`, Ramle/Ramla `רמלה`, Lod `לוד`, Shoham `שוהם`, Netanya `נתניה`, Modi'in `מודיעין` | Mavat + Central District/local committees + TASE filings + Electricity Authority/IEC | Digital Realty Mivne Petah Tikva; MedOne Kfar Yona/Ramle/Petah Tikva; GTR IS One; NED Netanya; Bynet Lod/Shoham; Mega Or/Nebius Modi'in. |
| Tel Aviv | `מחוז תל אביב`, Tel Aviv `תל אביב`, Herzliya `הרצליה`, Ramat Gan/Bnei Brak/Petah Tikva edge | Mavat + Tel Aviv/Herzliya local permits + cloud region/provider pages | Serverfarm ISR1 North Tel Aviv; Bynet TLV; AWS/GCP/Azure Tel Aviv cloud-region seed; Bezeq/IX/submarine connectivity leads. |
| HaTsafon | `מחוז צפון`, Yokneam `יקנעם`, Mevo Carmel `מבוא כרמל`, Galilee industrial zones | Mavat + Northern District/local committees + grid proceedings | Nvidia/Yokneam and Mevo Carmel leads; search for AI/HPC and industrial-zone power allocations. |

Boundary caution: market materials may call Central, Herzliya, Petah Tikva, Bnei Zion, or Beit Shemesh "Tel Aviv". Map every facility to the repo district by municipality/coordinates, not by marketing metro.

---

## 6. Evidence grading and extraction rules

### 6.1 Grade A evidence

Use as primary evidence:

- Mavat plan/request/hearing page or attached statutory document.
- Local/district planning committee decision, protocol, building permit, or official municipality publication.
- Electricity Authority decision/hearing, IEC/Noga grid material, or official connection document.
- Operator official facility page that states location/capacity/status.
- Cloud provider official region docs for region/AZ count only.
- TASE/MAYA listed-company filing.
- Ministry of Communications license for telecom/operator identity only.

### 6.2 Grade B evidence

Use as strong secondary evidence:

- DatacenterDynamics, Globes, Calcalist, TheMarker, Jerusalem Post, Data Center Frontier, Data Centre Magazine, Data Center Dynamics when they cite named operator, filing, or government decision.
- Investor/owner pages for infrastructure funds if they name project status and operator.
- Vendor/contractor case studies where site/operator is explicit.

### 6.3 Grade C evidence

Use only as leads:

- DataCenterMap, Baxtel, Datacenters.com, Cloudscene, Ocolo, Newby Ventures, MLQ.ai, LinkedIn posts, Facebook/Instagram, broker listings, SEO facility pages.
- Aggregator capacity/address values without a primary source.

### 6.4 Fields to extract

For each candidate facility/project:

```
name
operator/developer/SPV
district and municipality
industrial zone / campus / parcel if public
status: planned | permitted | construction | operational | expansion | cancelled/paused
planning reference: plan number, permit number, committee, decision date
energy reference: requested/secured MVA, IT MW, total power MW, substation/grid connection
building scale: sqm, racks, floors, underground/protected status
tenants/cloud links: AWS/GCP/Azure/Oracle/Nebius/Nvidia etc.
evidence URLs and evidence date
confidence notes and unresolved gaps
```

---

## 7. Practical enumeration playbook

1. Start with the repo result seeds and operator seed list: MedOne, Bynet, Bezeq International, Serverfarm, Digital Realty Mivne, Mega DC/Mega Or, GTR, NED, Oracle/Bynet, AWS, Google Cloud, Microsoft, Nvidia/Nebius.
2. Normalize locality and district. Translate marketing metro names into municipality/district using Mavat/XPlan or maps.
3. Search Mavat for the exact Hebrew/English project/operator and generic Hebrew terms. Save plan numbers and committee status.
4. Search Electricity Authority, IEC, and Noga for the project/operator/locality plus `מו"א`, `MVA`, `תחנת משנה`, and `חיבור לרשת`.
5. Search MAYA/TASE for listed entities: Mivne, Mega Or, Levinstein, Dalia, Electra, Shikun & Binui, Azrieli, or other owner/developer names.
6. Check operator official pages for facility/campus status and capacity. Prefer operator pages over aggregators.
7. Use trade press to fill gaps and identify hidden SPVs, but downgrade to B unless primary documentation is linked and checked.
8. For each project above 8 MVA or 50 MVA, explicitly note whether the 2026 Electricity Authority suspension/hearing may affect timing.

High-yield combined queries:

```
"{locality Hebrew}" "חוות שרתים" "היתר"
"{locality Hebrew}" "מרכז נתונים" "תכנית"
"{operator}" "חוות שרתים" "מו\"א"
"{operator}" "חוות שרתים" "תחנת משנה"
"{operator}" "חוות שרתים" "רשות החשמל"
"{operator}" "חוות שרתים" site:maya.tase.co.il
"{project}" "MVA" "Israel"
"{project}" "substation" "Israel"
"{project}" "planning" "Israel"
```

---

## 8. Known first-pass leads to verify

These are not a final facility census; they are priority pivots for official validation.

- **Digital Realty Mivne, Petah Tikva**: official Digital Realty press release says a multi-tenant campus up to 20 MW IT load; verify current permit and any MedOne/Mivne/DLR expansion in Mavat and TASE.
- **MedOne Kfar Yona, Ramle, Tirat HaCarmel, Petah Tikva, Dimona**: MedOne official pages provide strong facility/capacity seeds; verify with Mavat and local committees.
- **Mega DC / Mega Or**: official Mega DC sites list Haifa, Beit Shemesh, Idan HaNegev, Masmia, Modi'in, Hadera; verify plan/permit and grid status because projects are large and energy-sensitive.
- **Bynet Jerusalem/Shoham/Lod/TLV**: Bynet official site gives strong operational facility evidence; use planning only for expansions.
- **Serverfarm ISR1 and Dalia/Ofek near Ashdod**: Serverfarm official page confirms ISR1; Ofek/Ashdod is trade-press led and needs Mavat/Electricity Authority verification.
- **AWS Israel (Tel Aviv), Google Cloud Tel Aviv, Azure Israel Central, Oracle Jerusalem/Israel**: region pages are official but not exact facility proof; treat as tenant/demand/metro seeds.

---

## 9. Source index

Official/regulatory:

- Planning Administration: https://www.iplan.gov.il/
- Mavat Planning Information: https://mavat.iplan.gov.il/
- Mavat search: https://mavat.iplan.gov.il/SV3?searchEntity=3&searchMethod=2
- XPlan blue-line map: https://ags.iplan.gov.il/xplan/
- Planning GIS services: https://ags.iplan.gov.il/services/
- Government decision 3907: https://www.gov.il/he/pages/dec3907-2026
- Electricity Authority decisions/hearings: https://www.gov.il/he/departments/topics/decisions-and-hearings
- Electricity Authority decision 74506: https://www.gov.il/he/pages/74506
- Electricity Authority 50 MVA hearing: https://www.gov.il/he/pages/shimam50hibur
- Ministry press release on interim recommendations: https://www.gov.il/he/pages/press_190226
- IEC connection-probability map: https://www.iec.co.il/content/renewableenergy/contentpages/probabilitymap
- IEC: https://www.iec.co.il/
- Noga ISO: https://www.noga-iso.co.il/
- Ministry of Communications: https://www.gov.il/en/departments/ministry_of_communications
- Communications general licenses: https://www.gov.il/he/pages/lic
- Communications Law: https://www.gov.il/he/pages/communication_law
- TASE/MAYA: https://maya.tase.co.il/

Cloud/operator:

- AWS Israel: https://aws.amazon.com/local/israel/
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Google Cloud locations: https://cloud.google.com/about/locations
- Google Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones
- Google Cloud Project Nimbus post: https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-selected-to-provide-cloud-services-to-the-state-of-israel
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Microsoft Israel region announcement: https://news.microsoft.com/source/emea/features/microsoft-to-launch-new-cloud-datacenter-region-in-israel/
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Government Project Nimbus page: https://www.gov.il/en/pages/press_01082023_b
- MedOne: https://medone.co.il/
- MedOne about: https://medone.co.il/about-medone
- Bynet Data Centers: https://bynetdcs.co.il/
- Bezeq International: https://www.bezeqint.net/en
- Serverfarm ISR1: https://www.serverfarmllc.com/tel-aviv-data-center/
- Serverfarm locations: https://www.serverfarmllc.com/data-centers/
- Digital Realty/Mivne press release: https://www.digitalrealty.com/about/newsroom/press-releases/122655/digital-realty-announces-joint-venture-with-mivne-to-develop-new-colocation-and-connectivity-hub-in-israel-and-expand-mediterranean-presence
- Mivne Group: https://en.mivnegroup.co.il/
- Mega DC sites: https://www.megadc.com/our-sites
- IDCA Israel Data Center Association: https://idca.org.il/
