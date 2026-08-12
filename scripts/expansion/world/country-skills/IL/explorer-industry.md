# IL Explorer - Industry, Trade Press, Vendors, and District Query Patterns

Date: 2026-08-12. Scope: Israel datacenter enumeration from industry/trade press, vendor/operator pages, cloud-region pages, Hebrew/English search patterns, and district-level vendor/query tactics. Divisions from manifest: `HaDarom`, `Hefa`, `Yerushalayim`, `HaMerkaz`, `Tel Aviv`, `HaTsafon`. Reliability grades: **A** = operator/cloud-provider official page, company filing, or government/utility/planning primary source; **B** = established trade/business press or industry association; **C** = directories, broker pages, blogs, and market reports useful as leads only.

---

## 0. Israel-specific frame

- Israel has no single public datacenter facility registry. Enumerate by triangulating **operator portfolio pages + Globes/Calcalist/DCD leads + cloud-region official pages + local planning/power evidence**.
- The market is compact but not only "Tel Aviv." Major physical clusters are **Tel Aviv/Gush Dan**, **Petah Tikva/Shoham/Lod/Ramle/Modi'in/Netanya/Kfar Yona**, **Jerusalem/Har Hotzvim/Beit Shemesh**, **Haifa/Tirat Carmel/MATAM/Hadera**, **Yokneam/Mevo Carmel**, and **southern power/industrial sites near Ashdod, Be'er Tuvia, Masmia/Bnei Re'em, Idan HaNegev, Dimona**.
- Israel results are language-sensitive. English press uses `data center`, `data centre`, `cloud region`, `AI data center`, `hyperscale`, `underground data center`, `Project Nimbus`. Hebrew press and municipal docs use `חוות שרתים`, `דאטה סנטר`, `מרכז נתונים`, `חדרי שרתים`, `ענן`, `בינה מלאכותית`, `תב"ע`, `היתר בנייה`, `חיבור חשמל`, `תחנת משנה`, `מגה-וואט`.
- Power is now a gating variable. Calcalist reported in July 2026 that the Electricity Authority froze treatment of new grid-connection requests for data centers of 8MW+ for 140 days after Noga received very large new requests. Treat any 2026+ project announcement as **not fully validated** until there is evidence of secured power, Noga/IEC connection, onsite generation, or substation status. Source: https://www.calcalistech.com/ctechnews/article/tvp6729tr and Hebrew original https://www.calcalist.co.il/local_news/article/r1nnc0o4ge .
- Underground/fortified facilities are common and often market-facing. Search terms like `underground`, `fortified`, `bunker`, `ממוגן`, `תת קרקעי`, and `שרידות` find Israeli DC stories that generic `data center` searches miss.

---

## 1. Trade press and industry sources

### 1.1 High-signal English and Israeli business press

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Globes English / Hebrew | https://en.globes.co.il/ and https://www.globes.co.il/ ; query `site:en.globes.co.il Israel "data center" "{operator|city}"`, `site:globes.co.il "חוות שרתים" "{מפעיל|עיר}"` | Best business/real-estate/infrastructure source for Israeli DC deals, land purchases, power constraints, and AI-campus leads. Examples: Dalia/Serverfarm Ashdod 130MW, NED Netanya 42MW, Nvidia/Mega Or Mevo Carmel, Keystone Be'er Tuvia, Mega Or Hadera. | B+ |
| Calcalist / CTech | https://www.calcalist.co.il/ , https://www.calcalistech.com/ ; query `site:calcalist.co.il "חוות שרתים"`, `site:calcalistech.com Israel data center` | Strong on power regulation, investment, MedOne, AI demand, and sector bottlenecks. Good early warning for projects paused by grid limitations. | B+ |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com/en/news Israel data center "{operator}"` | Best international trade feed. Use for construction/site-selection announcements and cross-checks: Dalia, MedOne, NED, GTR, Keystone, AWS, Oracle. | B+ |
| The Times of Israel / JNS / Jerusalem Post / Ynetnews | site-scoped searches | Useful for cloud-region launches, Oracle/Bynet Jerusalem, Nvidia/Yokneam AI compute, and broader tech-infrastructure stories. Verify capacity with operator or business press. | B/C+ |
| Dgtl Infra / The Tech Capital / Data Centre Magazine / Data Center POST | site-scoped searches | Secondary trade coverage. Good for investor/developer context and specs; verify with operator page or Globes/DCD. | B-/C+ |
| Israeli Data Center Association (IDCA) | https://idca.org.il/ | Industry ecosystem, event speakers, sponsor/member leads. Good for identifying active developers/vendors, not a facility registry. | B-/C+ |

Trade-press query templates:

```text
site:en.globes.co.il Israel "data center" ("MW" OR "megawatt" OR "power") "{city|operator}"
site:globes.co.il "חוות שרתים" ("מגה וואט" OR "מגה-וואט" OR "חשמל") "{עיר|יזם}"
site:calcalist.co.il "חוות שרתים" ("רשות החשמל" OR "נגה" OR "חיבור")
site:calcalistech.com Israel "data center" ("electricity" OR "power" OR "Noga")
site:datacenterdynamics.com/en/news Israel "data center" "{operator}"
site:datacenterdynamics.com/en/news Israel "{city}" ("MW" OR "underground")
"Israel" "AI data center" ("Mega Or" OR "Mega DC" OR "Nebius" OR "Nvidia")
"חוות שרתים" ("תת קרקעי" OR "ממוגן" OR "שרידות") "{עיר}"
```

### 1.2 Directories and market reports

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/israel/ | Fast city/operator seed list and aliases. Useful for Bynet, Mega DC, AWS locality rumors. Do not treat physical AZ locations as confirmed without primary evidence. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/israel | Useful for marketed provider pages and facility aliases; commercial coverage can be uneven. | C+ |
| Baxtel | https://baxtel.com/data-centers/israel or operator pages | Good for relationship graph and planned campus leads, especially MedOne/NED/GTR. Verify details. | C+ |
| Mordor / ResearchAndMarkets / Arizton-style reports | Example: https://www.mordorintelligence.com/industry-reports/israel-data-center-market | Market sizing and operator-name discovery. Do not use for facility existence unless independently verified. | C |

---

## 2. Vendor/operator seed list

Official operator pages are **A for claimed presence/current marketed sites**, **B for capacity** unless the page provides facility-level specifications or a formal company filing.

| Operator / developer | Primary source(s) | Israel location signals | Grade notes |
|---|---|---|---|
| Bynet Data Centers | https://bynetdcs.co.il/ ; Bynet service page https://www.bynet.co.il/en/solutions/data-center/ | Seven underground sites around Jerusalem/Har Hotzvim, Tel Aviv, Lod, Shoham. Site pages expose rack/MW/sqm values for facilities such as Jerusalem of Gold/Silver/Light, TLV A/B, Lod, Ha'horesh Shoham. | A for own facility specs. |
| MedOne | https://www.medone.co.il/data-center-israel ; Kfar Yona news https://www.medone.co.il/news-events/with-an-investment-of-more-than-one-billion-ils-medone-is-building-two-data-centers-in-kfar-yona | Existing/expanding footprint around Tirat HaCarmel, Tel Aviv/Petah Tikva legacy, Ramle, Kfar Yona, Dimona/Tirat expansion roadmap. Official page says expansion plan exceeds 250MW IT and lists secured land/power for named sites. | A for official roadmap; verify each future phase/power status. |
| Mega Data Centers / Mega Or | https://www.megadc.com/our-sites | Official sites list Modi'in, Haifa/MATAM, Masmia/Bnei Re'em, Idan HaNegev, Beit Shemesh, Hadera. Strong AI/HPC orientation and large total-power claims. | A for own site list; B/C for future buildout until permits/power checked. |
| Serverfarm | https://www.serverfarmllc.com/tel-aviv-data-center/ ; locations page https://www.serverfarmllc.com/data-centers/ | ISR1 North Tel Aviv operational. Also linked via Globes/DCD to Dalia/IIF 130MW Ashdod project. | A for ISR1; B for Ashdod until operator/project page or permits mature. |
| Global Technical Realty (GTR) | https://globaltechnicalrealty.com/gtr-builds-momentum-with-tel-aviv-data-center/ | IS One, Petah Tikva, 10.5MW underground build-to-suit. | A for company announcement; verify operational status with current marketing/local docs. |
| NED Data Centers / Levinstein / Goldacre | https://www.ned-dc.com/projects/?ContentID=70652 ; Globes Netanya article https://en.globes.co.il/en/article-ned-levinstein-begin-construction-of-netanya-data-center-1001508989 | Alpha Campus, Netanya: 42MW AI-ready underground campus in construction; first facility expected early 2027 per Globes. | B+ with official project page; use local Netanya planning for A status. |
| Dalia Energy / Israel Infrastructure Fund / Serverfarm | DCD https://www.datacenterdynamics.com/en/news/dalia-energy-plans-israels-biggest-data-center/ ; Globes https://en.globes.co.il/en/article-israels-biggest-data-center-to-be-built-in-ashdod-1001535793 | 130MW AI data center outside/near Ashdod, reportedly $1.5B construction investment. | B until local planning and power documents are found. |
| Keystone Fund / IPM Be'er Tuvia | Globes https://en.globes.co.il/en/article-keystone-fund-plans-data-center-in-beer-tuvia-power-plant-1001499511 ; DCD https://www.datacenterdynamics.com/en/news/keystone-submits-application-for-two-data-centers-in-israel/ | Two-data-center campus at/near Be'er Tuvia power plant, 40MW IT planned. | B; application/approval status must be checked locally. |
| Nvidia | Globes Mevo Carmel https://en.globes.co.il/en/article-nvidia-in-talks-with-mega-or-to-build-huge-data-center-1001529459 ; campus siting https://en.globes.co.il/en/article-mevo-carmel-in-pole-position-to-house-nvidia-israel-campus-1001515431 | Internal AI/HPC facilities around Yokneam/Mevo Carmel; potential Mega DC partnership for 64MW; reported existing 30MW and another 63/64MW build. | B; many details are press-only or internal-use. |
| Hyperscalers: AWS, Microsoft, Google, Oracle | AWS https://aws.amazon.com/local/israel/ and https://aws.amazon.com/blogs/aws/now-open-aws-israel-tel-aviv-region/ ; Azure list https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Microsoft launch https://news.microsoft.com/source/emea/features/microsoft-to-launch-new-cloud-datacenter-region-in-israel/ ; Oracle https://www.oracle.com/il-en/cloud/cloud-regions/israel/ | AWS Israel (Tel Aviv) `il-central-1` with 3 AZs; Microsoft `Israel Central`; Google selected for Project Nimbus and runs Israel region; Oracle Israel cloud region uses an underground Jerusalem facility via Bynet in press reports. | A for logical cloud-region existence; C for exact physical sites unless separately verified. |

Vendor query templates:

```text
site:{operator-domain} Israel "data center" "{city}"
site:{operator-domain} ישראל ("חוות שרתים" OR "דאטה סנטר") "{עיר}"
"{operator}" "{city}" ("MW" OR "MVA" OR "IT load" OR "racks" OR "sqm")
"{operator}" "{city}" ("opened" OR "launched" OR "operational" OR "construction" OR "groundbreaking")
"{operator}" "{עיר}" ("נפתח" OR "הושק" OR "החלה בנייה" OR "אבן פינה" OR "היתר")
"{operator}" ("Noga" OR "Israel Electric" OR "IEC" OR "substation" OR "grid connection")
"{operator}" ("נגה" OR "חברת החשמל" OR "תחנת משנה" OR "חיבור לרשת")
```

---

## 3. Hebrew and English search vocabulary

### 3.1 Core Hebrew terms

Use exact Hebrew terms because Israeli sources often call data centers "server farms" rather than "data centers."

- data center / data centre: `חוות שרתים`, `חוות השרתים`, `דאטה סנטר`, `דאטה סנטרים`, `מרכז נתונים`, `מרכזי נתונים`
- server room / enterprise facility: `חדר שרתים`, `חדרי שרתים`
- AI / HPC: `חוות שרתים לבינה מלאכותית`, `חוות שרתים ל-AI`, `מחשוב עתיר ביצועים`, `מעבדה`, `סופר-מחשב`, `GPU`, `Nvidia`, `אנבידיה`
- planning: `תב"ע`, `תכנית בניין עיר`, `היתר בנייה`, `בקשה להיתר`, `ועדה מקומית`, `ועדה מחוזית`, `שינוי ייעוד`, `אזור תעשייה`
- power: `חיבור חשמל`, `חיבור לרשת`, `נגה`, `חברת החשמל`, `רשות החשמל`, `תחנת משנה`, `קווי מתח`, `הספק`, `מגה וואט`, `מגה-וואט`, `MVA`
- status verbs: `החלה בנייה`, `אבן פינה`, `נחנך`, `הושק`, `נפתח`, `יוקם`, `מתוכנן`, `בקשה`, `הקפאה`

### 3.2 English templates

```text
"Israel" ("data center" OR "data centre") ("MW" OR "MVA" OR "IT load") "{city}"
"Israel" ("AI data center" OR "HPC data center" OR "GPU cluster") "{operator}"
"{city}" Israel ("underground data center" OR "fortified data center")
"{city}" Israel ("data center" OR "server farm") ("substation" OR "grid connection" OR "power plant")
"{city}" Israel ("data center" OR "cloud region") ("permit" OR "planning" OR "zoning")
"Project Nimbus" ("data center" OR "cloud region" OR "Israel")
"AWS Israel Tel Aviv Region" "Availability Zones"
"Azure Israel Central" "availability zones"
"Oracle Israel" "underground data center" Jerusalem Bynet
```

### 3.3 Hebrew templates

```text
"{עיר}" ("חוות שרתים" OR "דאטה סנטר") ("מגה וואט" OR "מגה-וואט" OR "MVA")
"{עיר}" ("חוות שרתים" OR "דאטה סנטר") ("היתר בנייה" OR "תב\"ע" OR "בקשה להיתר")
"{עיר}" ("חוות שרתים" OR "דאטה סנטר") ("תחנת משנה" OR "חיבור חשמל" OR "חיבור לרשת")
"{אזור תעשייה}" ("חוות שרתים" OR "דאטה סנטר") ("Mega DC" OR "מגה אור" OR "MedOne" OR "בינת")
"{יזם}" ("חוות שרתים" OR "דאטה סנטר") ("החלה בנייה" OR "אבן פינה" OR "נחנך" OR "יוקם")
site:globes.co.il "{עיר}" "חוות שרתים"
site:calcalist.co.il "{עיר}" "חוות שרתים"
site:ynet.co.il "{עיר}" "חוות שרתים"
site:gov.il "חוות שרתים" ("רשות החשמל" OR "משרד האנרגיה" OR "בינה מלאכותית")
```

---

## 4. District-by-district industry enumeration

### 4.1 `Tel Aviv` district - Tel Aviv/Gush Dan market

Primary operator/developer seeds:

- **Serverfarm ISR1 North Tel Aviv** - official page: https://www.serverfarmllc.com/tel-aviv-data-center/ . Grade A.
- **Bynet TLV A / TLV B** - official Bynet page: https://bynetdcs.co.il/ . Grade A.
- **Microsoft / AWS / Google cloud-region market labels** - AWS, Azure, and Google often label the logical market Tel Aviv/Israel while physical AZs are not publicly address-confirmed. Grade A for region, C for exact sites.
- Nearby Central District sites often appear in Tel Aviv-market press: Petah Tikva, Shoham, Lod, Ramle, Netanya, Kfar Yona, Modi'in.

Query:

```text
"Tel Aviv" Israel "data center" Serverfarm ISR1
"Tel Aviv" "Bynet" ("TLV A" OR "TLV B" OR "racks")
"תל אביב" ("חוות שרתים" OR "דאטה סנטר") ("בינת" OR "Serverfarm" OR "חיבור חשמל")
"Gush Dan" "data center" Israel ("Petah Tikva" OR "Shoham" OR "Lod")
"AWS Israel (Tel Aviv) Region" "three Availability Zones"
"Azure Israel Central" "Israel" "availability zones"
```

### 4.2 `HaMerkaz` district - Central District: Petah Tikva, Shoham, Lod, Ramle, Modi'in, Netanya, Kfar Yona, Beit Shemesh edge

Primary operator/developer seeds:

- **GTR IS One Petah Tikva** - company release: https://globaltechnicalrealty.com/gtr-builds-momentum-with-tel-aviv-data-center/ ; DCD: https://www.datacenterdynamics.com/en/news/gtr-kkr-to-build-underground-data-center-in-israel/ . Grade A/B.
- **NED Alpha Campus Netanya** - official project and Globes construction article: https://www.ned-dc.com/projects/?ContentID=70652 , https://en.globes.co.il/en/article-ned-levinstein-begin-construction-of-netanya-data-center-1001508989 . Grade B+.
- **MedOne Kfar Yona and Ramle** - official expansion page: https://www.medone.co.il/data-center-israel . Grade A.
- **Bynet Lod and Ha'horesh Shoham** - https://bynetdcs.co.il/ . Grade A.
- **Mega DC Modi'in and Beit Shemesh** - https://www.megadc.com/our-sites . Grade A for company listing.
- **Nebius/Mega Or Modi'in** - Jerusalem Post launch article: https://www.jpost.com/business-and-innovation/article-871239 . Grade B.

Query:

```text
"Petah Tikva" "data center" GTR "10.5MW"
"פתח תקווה" ("חוות שרתים" OR "דאטה סנטר") ("GTR" OR "תת קרקעי")
"Netanya" "Alpha Campus" NED "data center" 42MW
"נתניה" ("חוות שרתים" OR "דאטה סנטר") ("NED" OR "לווינשטיין" OR "אלפא")
"Kfar Yona" MedOne "data center" 21MW
"כפר יונה" "MedOne" ("חוות שרתים" OR "היתר")
"Ramle" MedOne "data center" ("31.5MW" OR "10.5MW")
"רמלה" "MedOne" "חוות שרתים"
"Shoham" Bynet "Ha'horesh" "20MW"
"Modiin" ("Mega DC" OR "Mega Or" OR "Nebius") "data center"
"מודיעין" ("מגה אור" OR "Nebius" OR "חוות שרתים")
"Beit Shemesh" "Mega DC" "240MW"
"בית שמש" ("Mega DC" OR "מגה אור") ("תחנת משנה" OR "חוות שרתים")
```

### 4.3 `Yerushalayim` district - Jerusalem, Har Hotzvim, Beit Shemesh

Primary operator/developer seeds:

- **Bynet Jerusalem of Gold / Silver / Light** - Bynet official specs: https://bynetdcs.co.il/ . Grade A.
- **Oracle Israel cloud region / Jerusalem underground facility** - Oracle region page: https://www.oracle.com/il-en/cloud/cloud-regions/israel/ ; DCD/Times of Israel reporting on underground Jerusalem facility: https://www.datacenterdynamics.com/en/news/oracles-data-center-israel-safra-catz/ , https://www.timesofisrael.com/during-war-visit-oracle-ceo-affirms-commitment-to-open-second-data-center-in-israel/ . Grade A for Oracle region, B for facility story.
- **Mega DC Beit Shemesh** may be administratively Central/Jerusalem-market depending source; keep district assignment consistent with manifest output and local authority evidence.

Query:

```text
"Jerusalem" "Bynet" ("Jerusalem of Gold" OR "Har Hotzvim") "data center"
"Har Hotzvim" ("data center" OR "server farm") Bynet Oracle
"הר חוצבים" ("חוות שרתים" OR "דאטה סנטר") ("בינת" OR "אורקל")
"Oracle Israel" "underground data center" Jerusalem
"ירושלים" ("חוות שרתים" OR "מרכז נתונים") ("אורקל" OR "בינת")
"בית שמש" ("חוות שרתים" OR "דאטה סנטר") ("Mega DC" OR "מגה אור")
```

### 4.4 `Hefa` district - Haifa, Tirat HaCarmel, MATAM, Hadera

Primary operator/developer seeds:

- **MedOne Tirat HaCarmel flagship and expansion** - https://www.medone.co.il/data-center-israel ; DCD MedOne expansion: https://www.datacenterdynamics.com/en/news/medone-to-build-two-underground-data-centers-in-israel/ . Grade A/B.
- **Mega DC MDCIL-3 MATAM Haifa** - https://www.megadc.com/our-sites . Grade A.
- **Mega Or / Mega DC Hadera** - Mega DC official lists Hadera; Globes reports Mega Or bought the former Alliance Tire site in Hadera and market sources expect a major DC: https://en.globes.co.il/en/article-mega-or-buys-alliance-tire-site-in-hadera-for-nis-1b-cash-1001540399 . Grade B until planning/power documents.

Query:

```text
"Haifa" "MATAM" "Mega DC" "data center"
"חיפה" "מתם" ("חוות שרתים" OR "דאטה סנטר") ("Mega DC" OR "מגה")
"Tirat HaCarmel" MedOne "data center"
"טירת הכרמל" "MedOne" ("חוות שרתים" OR "הרחבה" OR "תת קרקעי")
"Hadera" "Mega Or" "data center" "Alliance"
"חדרה" ("מגה אור" OR "Mega DC") ("חוות שרתים" OR "מפעל אליאנס")
"מחוז חיפה" ("חוות שרתים" OR "דאטה סנטר") ("תחנת משנה" OR "חיבור חשמל")
```

### 4.5 `HaTsafon` district - Yokneam, Mevo Carmel, Megiddo/Jezreel, Kiryat Tivon/Afula candidate area

Primary operator/developer seeds:

- **Nvidia internal AI/HPC facilities around Yokneam/Mevo Carmel** - Globes reports existing/under-construction AI compute facilities and Mega DC talks: https://en.globes.co.il/en/article-nvidia-in-talks-with-mega-or-to-build-huge-data-center-1001529459 and https://en.globes.co.il/en/article-mevo-carmel-in-pole-position-to-house-nvidia-israel-campus-1001515431 . Grade B.
- **Mega DC / Mega Or Mevo Carmel or northern pipeline** - search with both Mega DC and `מגה אור`. Grade B until operator/planning confirmation.
- Nvidia campus location searches produce many office/lab hits; only count a DC where article says `data center`, `AI processing facility`, `GPU`, `MW`, or `חוות שרתים`.

Query:

```text
"Yokneam" Nvidia ("data center" OR "HPC" OR "AI facility")
"יוקנעם" ("אנבידיה" OR "Nvidia") ("חוות שרתים" OR "סופר-מחשב" OR "מחשוב")
"Mevo Carmel" Nvidia "data center" "MW"
"מבוא כרמל" ("אנבידיה" OR "Mega DC" OR "מגה אור") ("חוות שרתים" OR "מגה וואט")
"Megiddo Regional Council" "data center" Nvidia
"מגידו" "חוות שרתים" "מבוא כרמל"
"Kiryat Tivon" Nvidia campus data center
"קריית טבעון" "אנבידיה" ("קמפוס" OR "חוות שרתים")
```

### 4.6 `HaDarom` district - Ashdod, Be'er Tuvia, Masmia/Bnei Re'em, Idan HaNegev, Dimona, Beersheba

Primary operator/developer seeds:

- **Dalia Energy / Serverfarm / IIF Ashdod 130MW** - DCD and Globes: https://www.datacenterdynamics.com/en/news/dalia-energy-plans-israels-biggest-data-center/ , https://en.globes.co.il/en/article-israels-biggest-data-center-to-be-built-in-ashdod-1001535793 . Grade B.
- **Mega DC Idan HaNegev and Masmia/Bnei Re'em** - https://www.megadc.com/our-sites . Grade A for company list; verify site boundaries and district assignment.
- **Keystone / IPM Be'er Tuvia 40MW** - Globes/DCD: https://en.globes.co.il/en/article-keystone-fund-plans-data-center-in-beer-tuvia-power-plant-1001499511 , https://www.datacenterdynamics.com/en/news/keystone-submits-application-for-two-data-centers-in-israel/ . Grade B.
- **MedOne Dimona** - aggregator lead only unless MedOne provides a specific Dimona page/status; current MedOne roadmap is useful but not enough for exact capacity. Grade C/B depending source.
- **Beersheba/Gav-Yam Negev Advanced Technologies Park** - search for edge/HPC and enterprise/server-room projects; most hits may be campus IT rather than commercial colocation.

Query:

```text
"Ashdod" "Dalia Energy" "data center" 130MW
"אשדוד" ("דליה" OR "Serverfarm" OR "IIF") ("חוות שרתים" OR "דאטה סנטר")
"Be'er Tuvia" Keystone "data center" "40MW"
"באר טוביה" ("Keystone" OR "קיסטון" OR "IPM") ("חוות שרתים" OR "תחנת כוח")
"Masmia" "Mega DC" "data center"
"מסמיה" ("Mega DC" OR "מגה אור") ("חוות שרתים" OR "תחנת משנה")
"Bnei Re'em" "Mega DC" "data center"
"Idan HaNegev" "Mega DC" "data center" 180MW
"עידן הנגב" ("Mega DC" OR "מגה אור") ("חוות שרתים" OR "דאטה סנטר")
"Dimona" MedOne "data center"
"דימונה" "MedOne" ("חוות שרתים" OR "דאטה סנטר")
"Beersheba" ("data center" OR "HPC" OR "server farm") Israel
```

---

## 5. Cloud-region handling

Cloud pages prove in-country service regions, not physical facilities. Store them as logical regions or demand signals unless local evidence identifies a facility.

| Provider | Official signal | How to use |
|---|---|---|
| AWS | AWS local Israel page and launch blog say the AWS Israel (Tel Aviv) Region is open with three AZs and API name `il-central-1`: https://aws.amazon.com/local/israel/ , https://aws.amazon.com/blogs/aws/now-open-aws-israel-tel-aviv-region/ . | A for region existence. Do not copy physical AZ locations from directories without primary corroboration. |
| Microsoft Azure | Microsoft announced first Israel cloud datacenter region in 2020; Azure regions list includes `Israel Central` / `israelcentral`: https://news.microsoft.com/source/emea/features/microsoft-to-launch-new-cloud-datacenter-region-in-israel/ , https://learn.microsoft.com/en-us/azure/reliability/regions-list . | A for region. Exact sites/capacity not public. |
| Google Cloud | Project Nimbus award/region news and Google Cloud locations pages establish Israel cloud presence; use official Google pages where possible: https://cloud.google.com/blog/topics/inside-google-cloud/google-cloud-selected-to-provide-cloud-services-to-the-state-of-israel . | A/B for region/contract; facility siting is opaque. |
| Oracle | Oracle Israel cloud-region page plus press on Jerusalem underground facility: https://www.oracle.com/il-en/cloud/cloud-regions/israel/ . | A for region; B for Jerusalem/Bynet facility specifics from DCD/Times of Israel. |

Cloud pivot queries:

```text
"Project Nimbus" ("AWS" OR "Google") Israel "data center"
"il-central-1" "Israel" "Availability Zones"
"Israel Central" Azure "data center region"
"Oracle Israel Cloud Region" Bynet Jerusalem underground
"Google Cloud" Israel region "Project Nimbus" "local cloud"
```

---

## 6. Validation workflow and reliability cautions

1. Start with trade/industry lead: Globes, Calcalist, DCD, operator news, IDCA speakers.
2. Confirm operator existence: official vendor page, project page, press release, TASE/company filing if applicable.
3. Confirm location/district: municipality, industrial park, regional council, power plant, or operator page. Israeli press often says "Tel Aviv" for a Central District suburb.
4. Confirm status: distinguish `announced`, `application submitted`, `land purchased`, `construction begun`, `opened`, `operational`. Many large AI campuses are power-reservation or land-deal stories, not active facilities.
5. Confirm power: look for `secured power`, `חיבור חשמל`, `נגה`, `חברת החשמל`, `תחנת משנה`, onsite generation, or power-plant adjacency. Current power freeze means high-MW projects without connection evidence should remain planned/speculative.
6. Use directories only to discover names/aliases. Upgrade to A/B only after operator, trade press, planning, or power evidence.

Useful official/power/planning pivots when industry sources are insufficient:

```text
site:gov.il "חוות שרתים" "רשות החשמל"
site:gov.il "קידום הקמת חוות שרתים" "בינה מלאכותית"
site:iec.co.il "חוות שרתים" OR "data center"
site:noga-iso.co.il "חוות שרתים" OR "data center"
site:iplan.gov.il "חוות שרתים" OR "דאטה סנטר"
site:mavat.iplan.gov.il "חוות שרתים" OR "דאטה סנטר"
"{עיר}" "חוות שרתים" "ועדה מקומית"
"{עיר}" "דאטה סנטר" "בקשה להיתר"
"{אזור תעשייה}" "חוות שרתים" "תב\"ע"
```

Government decision/policy lead: https://www.gov.il/he/pages/dec3907-2026 . Use it for national AI/datacenter policy context and follow-on ministry recommendations, not as a facility list.

---

## 7. Known lead universe to seed enumeration

Use these as starting points, then verify each record with current evidence:

- **Tel Aviv**: Serverfarm ISR1 North Tel Aviv; Bynet TLV A/B; logical AWS/Microsoft/Google region labels.
- **HaMerkaz**: GTR Petah Tikva; Bynet Lod/Shoham; MedOne Ramle/Kfar Yona; NED Alpha Netanya; Mega DC Modi'in/Beit Shemesh; Nebius/Mega Or AI site.
- **Yerushalayim**: Bynet Jerusalem of Gold/Silver/Light; Oracle/Bynet underground Jerusalem region; Beit Shemesh if classified to Jerusalem market in source.
- **Hefa**: MedOne Tirat HaCarmel; Mega DC MATAM Haifa; Mega Or/Mega DC Hadera lead.
- **HaTsafon**: Nvidia/Yokneam/Mevo Carmel AI/HPC facilities; Mega DC/Mega Or northern pipeline.
- **HaDarom**: Dalia/Serverfarm/IIF Ashdod; Mega DC Idan HaNegev and Masmia/Bnei Re'em; Keystone/IPM Be'er Tuvia; MedOne Dimona lead; Beersheba edge/HPC leads.

