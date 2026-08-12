# SO Explorer - Industry / Press / Vendor Discovery for Somalia Datacentres

Date: 2026-08-12. Scope: Somalia (SO) datacentre enumeration from industry media, local business press, operator/vendor pages, IXP/subsea/interconnection records, development-partner reports, procurement mirrors, and region-level search patterns. Reliability grades: **A** = official/primary source (operator page or press release, government agency, NCA/MOCT/NIRA document, World Bank/UNDP/IFC/TaiwanICDF document, cloud provider page), **B** = strong secondary/trade press (DCD, Bloomberg, Techpoint, SONNA, Goobjoog, Garowe Online, AllAfrica/Horn Diplomat), established local press, official procurement mirror, industry association, or credible vendor case study, **C** = aggregator, social post, old MoU, market-report snippet, or unverifiable local mention.

---

## 0. Somalia-specific frame

- Somalia has **no national facility registry and no public planning-permit database**. Discovery works by triangulating **operator pages** (Hormuud, Somtel/Somtel FGC, Telesom, Golis, NationLink, Wingu, SomaliREN), **trade press** (DCD Somalia tag, Bloomberg, Techpoint), **local press** (SONNA, Goobjoog, Garowe Online, Horseed, Somaliland press), **official procurement mirrors** (SomaliJobs for FGS/World Bank tenders when MoF/MOCT PDFs are inaccessible), **IXP/subsea records** (SoIXP/MogIX, DARE1 Mogadishu/Bosaso leads, Somcable 2Africa Berbera landing), **aggregators** (datacentermap, Baxtel, OCOLO, datacenters.com, DataCenterPlanet, PeeringDB), and **development-partner reports** (World Bank Somalia Digital Economy Diagnostic 2022, UNDP DPI work, IFC-NCA subsea framework, TaiwanICDF Somaliland government data-center project).
- Commercial activity is concentrated in a few clusters:
  - **Banaadir / Mogadishu**: federal National Data Center (SCALED-UP procurement 2023/2024, under construction Apr 2024, near completion May 2025, operations hiring Apr 2025), Hormuud portfolio (11 DCs, ~10 MW stated), NationLink, SomaliREN DC/services (Hodan/Taleh Road), NIRA HUBIYE/eAqoonsi and ABIS, SoIXP, DARE1 landing station, Hormuud/Somtel 5G launches.
  - **Northwest / Woqooyi Galbeed (Somaliland)**: Hargeisa (Somaliland Government Data and Cybersecurity Center / National Data Center, ground broken 22 Sep 2025; Telesom; Somtel 3-DC claim; EGS/S-Road e-government services) and Berbera/Sahil (Wingu Berbera SL01 - the only confirmed commercial carrier-neutral colo found; Somcable 2Africa landing).
  - **Puntland (Bari/Nugaal/Mudug)**: Golis Telecom (Bosaso HQ, Garowe), telecom core nodes, DARE1/G2A/Somtel landing-point leads, Puntland government e-services; no confirmed commercial DC found.
  - Other regions: expect negative results or government/UN ICT rooms.
- Sources use both **data centre** and **data center**; also search **datacentre**, **colocation**, **carrier-neutral**, **hyperscale**, **AI-ready**, **sovereign cloud**, **data sovereignty**, **server infrastructure**, **Tier III**, **Uptime Institute**, **MW**, **MVA**, **racks**, **landing station**, **IXP**, **peering**, **solar**, **substation**. Somali terms: `xarunta xogta` (data centre), `kaydinta xogta` (data storage), `seefar` (server), `xog-ballaarinta` (digitalisation), `wasaaradda isgaarsiinta` (ministry of communications). Arabic (govt documents): `مركز البيانات` (data centre).
- **No hyperscaler operates in Somalia** (AWS/Azure/GCP/OCI region lists omit it). Treat cloud-region news as seeds only; government "sovereign cloud"/NDC projects are government infrastructure, not hyperscaler regions.
- Security context: telecom attacks by Al-Shabab are documented (Hormuud blamed the group for destroyed infrastructure; 6 Hormuud staff killed May 2024). Treat unverified capacity/status claims cautiously and date-check everything.

---

## 1. Industry and trade press sources

Use press to discover project names, operators, regions, capacity claims, and status verbs; then verify with an operator, ministry/regulator, or development-partner source.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | Somalia tag: https://www.datacenterdynamics.com/en/tags/somalia/ and news search https://www.datacenterdynamics.com/en/news/?tag=somalia | Best global trade feed for Somalia: Hormuud green DC plans (Dec 2024), NCA-IFC subsea framework (Sep 2024), Hormuud 5G (Mar 2024), Somtel first 5G (Jan 2024), Hormuud spectrum licence (Nov 2022), Hormuud DARE1 landing station (Nov 2022), security incidents. | B; A only for linked/quoted primary docs |
| Bloomberg | Hormuud CEO green data centres piece (Dec 2024): https://www.bloomberg.com/news/articles/2024-12-06/top-internet-provider-to-somalia-eyes-green-data-centers-for-ai | Primary-ish interview quotes for Hormuud 11-DC/10 MW portfolio and solar claims. | B/A- for CEO quotes |
| Techpoint Africa | https://techpoint.africa/news/hormuud-telecom-launches-5g-somalia/ | Pan-African tech press covering Hormuud 5G and Somali fintech/ICT. | B/C |
| Horn Economic Review | https://horneconomicreview.com/2026/05/23/somalia-emerges-as-east-africas-core-digital-gateway-capitalizing-on-africas-longest-coastline/ | Regional economic analysis framing Somalia as digital gateway (cables, SIXP); use as context, not facility evidence. | B/C |
| Submarine Networks (submarinenetworks.com) | https://www.submarinenetworks.com/en/systems/asia-europe-africa/2africa/somcable-lands-2africa-in-berbera-somaliland | Somcable 2Africa Berbera landing (May 2022); DARE1 system pages for Mogadishu landing; cable facts. | B |
| SONNA (state news) | https://sonna.so/en/ | Federal government statements: National Data Center near-completion (May 2025), BECO solar plant, minister tours. | B/A when quoting ministry |
| Goobjoog News | https://en.goobjoog.com/ | Federal affairs + NDC inspections; good for status updates. | B |
| Garowe Online | https://www.garoweonline.com/ | Puntland politics/ICT/e-services; GSMA certification of Hormuud/Golis mobile money. | B/C |
| Dawan Africa | https://www.dawan.africa/ ; NDC article https://www.dawan.africa/news/somalia-plans-national-data-centre-to-strengthen-digital-infrastructure | Somali/African business press; Aug 7, 2026 National Data Centre "plans" + Garad.ai launch coverage. Use only as a current-policy/possible-next-phase lead because it conflicts with 2024-2025 federal NDC construction evidence. | B/C |
| TaiwanICDF | https://www.icdf.org.tw/wSite/ct?ctNode=31572&mp=2&xItem=74053 | Primary development-partner confirmation of Somaliland Government Data and Cybersecurity Center groundbreaking at MICT in Hargeisa on 22 Sep 2025; says it is Somaliland's first government data center with server facilities and cybersecurity systems. | A |
| AllAfrica / Horn Diplomat | https://allafrica.com/stories/202509230049.html ; https://www.horndiplomat.com/somaliland-breaks-ground-on-national-data-center-with-taiwans-support/ | Reprints/coverage of Somaliland National Data Center groundbreaking and approximate USD 1M value; route to TaiwanICDF/MICT primary. | B (reprint/press) |
| Somaliland press (Somaliland Sun, Waaheen, SomalilandCurrent, Saxafi) | site-scoped search | Somaliland operator news (Telesom 5G, EGS, telecom investment). | B/C |
| Biometric Update | https://www.biometricupdate.com/202503/nadra-and-nira-work-to-advance-somalias-digital-identification-program ; ABIS RFI https://www.biometricupdate.com/202501/fbi-seeks-vendors-for-its-somalia-abis | NIRA/NADRA identity infrastructure detail; ABIS RFI says secure facility at Aden Adde International Airport and secondary backup server. | B |
| Hiiraan Online / HOL / HigherGov | https://www.hiiraan.com/news4/2025/Jan/199793/fbi_seeks_vendors_to_support_somalia_s_biometric_identification_system.aspx ; https://www.highergov.com/contract-opportunity/cjis-somalia-abis-rfi-fy-2025-djf-25-rfi-01102025-r-78ef3/ | ABIS vendor solicitation - identity/law-enforcement infrastructure evidence; HigherGov mirrors SAM.gov fields including place of performance in Mogadishu, SO-BN. | B/C |
| UbuntuNet / TCC-Africa | https://ubuntunet.net/members/somaliren-succeeds-in-implementing-the-international-service-of-eduroam/ ; https://www.tcc-africa.org/s2-ep-11-building-somalias-scholarly-infrastructure-post-civil-conflict-a-conversation-with-mr-mohamud-mohamed-siad-and-eng-ahmed-siyad/ | SomaliREN data centre, eduroam, SORA repository, education-network infrastructure. | B |
| Africa Data Centres Association | https://africadca.org/ | Pan-African association news; Somalia rarely appears - sweep periodically for membership/announcements. | B/C |
| DC Byte / Baxtel / DataCenterMap / OCOLO / DataCenterPlanet / datacenters.com / PeeringDB | baxtel.com/data-center/wingu-africa-berbera-sl01 ; datacentermap.com/somalia/berbera/wingu-africa-data-center-berbera/ ; ocolo.io/colocation/winguafrica/berbera-somaliland/ ; datacenterplanet.com/listings/wingu-berbera ; datacenters.com/hormuud-telecom-hormuud-mogadishu ; peeringdb.com/fac/13450 | Lead indexes; Somalia listings are sparse (Wingu Berbera; Hormuud Mogadishu entry). PeeringDB is useful for Wingu Berbera address (Batalaale Beach, Zone 20 / Beach Road) and Somcable ASN 37425. Aggregators can misplace cities and stale capacities; never use alone for final capacity. | C/B- |
| Vendor case studies | Huawei, Vertiv, Schneider Electric, Siemens, solar/energy vendors, cable operators (Somcable, Hormuud cable) | Equipment/construction/cable delivery evidence; capacity often absent. | B/C |

Trade-press query templates:
```text
site:datacenterdynamics.com/en/news/ Somalia "data center" OR "data centre" "{operator OR city}"
site:techpoint.africa Somalia "data centre" OR "data center"
site:sonna.so "data centre" OR "data center" OR "National Data Center"
site:garoweonline.com "data centre" OR "data center" OR ICT
site:allafrica.com Somalia "data centre" OR "data center"
site:submarinenetworks.com Somalia OR Somaliland landing
"Somalia" "data centre" "{operator}" MW
"SO-MOF-374369-GO-RFB" "Data Centre"
"SO-MOF-425074-CS-INDV" "Data Center"
"Somaliland" "Government Data and Cybersecurity Center"
```

When reading press, capture the exact lifecycle verb: `announces`, `plans`, `MoU`, `feasibility` = intent (C/B); `breaks ground`, `starts construction`, `completes` = stronger pipeline (B unless official); `opened`, `commissioned`, `operational`, `ready for service`, `launches` = operational signal (verify with operator/government page for A).

---

## 2. Operator and developer sweep

Official operator pages are **A for current claimed locations and facility existence**. Capacity on marketing pages is **A-/B** unless the page gives facility-level IT load or is backed by a primary announcement.

| Operator / developer | Official / primary URL | Somalia locality signals | Notes |
|---|---|---|---|
| Hormuud Telecom | https://hormuud.com/ ; DC ops jobs https://hormuud.com/Jobs/12 | Mogadishu (Banaadir) core + regional nodes; 11 DCs / ~10 MW stated (CEO via Bloomberg/DCD Dec 2024); up to 95% solar by day; DARE1 landing station Mogadishu (completed Nov 2022); first national spectrum licence (Nov 2022); 5G since Mar 2024. | Core Mogadishu lead. Search `Hormuud "data centre"`, Hormuud enterprise/cloud, Hormuud solar, Hormuud landing station. Do not mint 11 facility records from the aggregate. |
| Somtel FGC / Somtel (Dahabshiil) | https://somtelfgc.com/about/ ; subsea/fibre page https://www.somtelnetwork.net/Submarrine-cable | Hargeisa-headquartered FGC; FGC page offers colocation data-center facilities; network page states "3 Data Centers", existing landing points at Mogadishu, Bosaso, Wajaale, Djibouti, Mombasa and planned Berbera (2025); first 5G in Somalia (Jan 2024); eDahab mobile money. | Verify each of the 3 DC sites; search Somtel FGC colocation, Somtel enterprise/cloud and fibre. Do not turn landing points or 5G launches into DC records. |
| Telesom | https://www.telesom.com/ | Hargeisa; 5G 1 Jan 2024 (Somaliland first); group spans gas/electricity/banking (Somgas, TEC, Dara Salaam Bank); e-government service partner. | DC-specific evidence thin; search `Telesom "data centre"`, Telesom EGS, Telesom enterprise. |
| Golis Telecom | https://golistelecom.com/ (HQ Biyo Kulule road, Bosaso); GSMA mobile-money cert (with Hormuud) via Garowe Online | Bosaso (Bari), Garowe (Nugaal), Galkayo (Mudug), Qardho, Erigavo (Sanaag) and other Puntland towns; ~750 km Bosaso-Galkayo backbone. | Search `Golis Telecom "data centre"`, Golis enterprise, Puntland e-gov. |
| NationLink Telecom | Wikipedia: https://en.wikipedia.org/wiki/NationLink_Telecom ; D&B profile | Mogadishu HQ (founded 1997); southern presence incl. Kismayo; ~16% market share (2022, industry). | DC evidence thin; search NationLink enterprise/internet/colocation. |
| Wingu Africa | https://www.wingu.africa/ ; Berbera news https://www.wingu.africa/latest-news/wingu-opens-carrier-neutral-data-centre-in-berbera-somaliland ; PeeringDB https://www.peeringdb.com/fac/13450 | Berbera SL01 (Somaliland/Sahil): first phase commissioned 13 Feb 2021, ready for service per Wingu announcement published Feb 2022; first/only commercial carrier-neutral DC in Somaliland at announcement; PeeringDB lists Batalaale Beach, Zone 20 / Beach Road and Somcable ASN 37425. | Anchor commercial colo lead for "Northwest"; verify current status/capacity directly because Wingu's current homepage market cards omit Somaliland. Join Somcable 2Africa landing and Berbera port/SEZ. |
| SomaliREN | https://somaliren.org/ | Mogadishu (TCC Building, Taleh Road, Hodan); data centre + eduroam + SORA/SORER repository; AS327764; 33 members by 2026. | Education-network DC; record separately from commercial colo. |
| Somcable | https://www.submarinenetworks.com/en/systems/asia-europe-africa/2africa/somcable-lands-2africa-in-berbera-somaliland | Berbera landing (May 2022); Somaliland connectivity provider. | Landing station, not DC; use as interconnect anchor. |
| NIRA | https://nira.gov.so/ ; DPI launch https://nira.gov.so/news/nira-launches-key-digital-public-infrastructure-for-national-id-system ; World Bank mass registration blog https://blogs.worldbank.org/en/nasikiliza/federal-republic-of-somalia-launches-mass-registration-drive-for-its-digital-id | Mogadishu identity/DPI systems; HUBIYE verifier, Certificate Delivery System, eAqoonsi app; World Bank-supported mass registration; ABIS separate law-enforcement lead. | Government/identity infrastructure; do not merge with commercial DCs. |
| Federal National Data Center procurement/ops | Tender mirror https://somalijobs.com/tenders/somalia/16504385293277024/amendment-to-submision-deadline-and-response%3A-request-for-bids-for-supply%2C-installation%2C-commissioning-of-data-centre-for-ministry-of-communications-and-technology ; facility engineer REOI https://somalijobs.com/jobs/mogadishu/9974656767534180/data-center-%28dc%29-facility-engineer-%28individual-consultant%29 ; project-manager REOI https://somalijobs.com/jobs/mogadishu/14313715612190546/national-data-center-project-manager-%28individual-consultant%29 | Mogadishu, SCALED-UP P168115; tender for supply/installation/commissioning/support; 2025 REOIs for project manager and facility engineer show operational planning and consolidation of scattered FGS hosting infrastructure. | B mirrors of official procurement; search MoF/MOCT/World Bank for primary PDFs and contract award. |
| Arkaan AI Centre / Garad.ai | launch coverage via Dawan Aug 2026: https://www.dawan.africa/news/somalia-plans-national-data-centre-to-strengthen-digital-infrastructure | Mogadishu AI initiative; tied to NDC "plans" statement. | C-level lead; verify any compute facility claims. |

Vendor/operator query templates:
```text
"{operator}" Somalia "data centre" OR "data center" MW
"{operator}" "{town}" "data centre" racks
site:{operator-domain} "data centre" OR "data center"
"{operator}" "landing station" OR "IXP" OR "peering" Somalia
"{operator}" "Uptime" OR "Tier III" Somalia
"{operator}" Somalia solar OR "backup power" "data centre"
site:somalijobs.com Somalia "Data Center" "Ministry of Communications"
```

---

## 3. Official and semi-official channels to pivot from press

This file focuses industry/press/vendor discovery, but every press lead should be verified against one or more of these primary routes.

| Channel | URL / route | How to use | Grade |
|---|---|---|---|
| NCA (federal regulator) | https://nca.gov.so/ | Operator licences, spectrum, SOMCERT, IXP and subsea regulation (incl. IFC framework Sep 2024). Use for operator/service authority evidence. | A when record found |
| MOCT (federal ICT ministry) | https://moct.gov.so/en/ | National Data Center project, e-gov agenda, ICT policy. Search site for NDC tours/status. | A when record found |
| Ministry of Finance / SCALED-UP procurement mirrors | MoF: https://mof.gov.so/ ; SomaliJobs tender/REOI mirrors listed above | Federal NDC tender, data-center project-manager and facility-engineer REOIs; use RFB/REOI IDs to find primary World Bank procurement and contract-award records. | A when MoF/World Bank primary found, B for SomaliJobs mirror |
| Federal government portal | https://www.somalia.gov.so/ | General government info; no facility register. | A for context |
| NIRA | https://nira.gov.so/ | National ID/ABIS infrastructure; eAqoonsi. | A when record found |
| SOMINVEST | https://sominvest.gov.so/ and ICT Sector Study https://sominvest.gov.so/ict-sector-study/ | Investment framing, sector study; may name priority sectors for data-centre investment. | A for study |
| Somaliland government portal / MOIID / MICT / TaiwanICDF | https://govsomaliland.org/ ; https://moiid.govsomaliland.org/ ; TaiwanICDF data-center page https://www.icdf.org.tw/wSite/ct?ctNode=31572&mp=2&xItem=74053 | Somaliland Government Data and Cybersecurity Center / National Data Center, EGS/S-Road, Wingu announcement. Portal may be intermittently under maintenance; TaiwanICDF is primary for Taiwan-supported project facts. | A when record found |
| Puntland Ministry of Finance | https://mof.pl.so/ | Tenders (ICT/data-centre procurement) in Garowe; use with Garowe Online for government statements. | A when record found |
| World Bank / UNDP / IFC project pages | Digital Economy Diagnostic 2022 PDF: https://thedocs.worldbank.org/en/doc/61714f214ed04bcd6e9623ad0e215897-0400012021/related/IDU105f167fa1085214f8b1919f141249b1e8fae.pdf ; digital ID blog: https://blogs.worldbank.org/en/nasikiliza/federal-republic-of-somalia-launches-mass-registration-drive-for-its-digital-id ; UNDP: https://www.undp.org/somalia/stories/driving-digital-transformation-somalia-2025-highlights | Market/regulatory context; project documents can name data-centre/government-cloud components. | A for documents |
| MOEWR / SESRP (energy) | https://sesrp.moewr.gov.so/ ; BECO https://beco.so/ | Power-plant tenders (Daynile), utility context; solar/diesel power reality near DC sites. | A for tenders |
| Uptime Institute Awards | https://uptimeinstitute.com/uptime-institute-awards/ | Check for any Somali certified facility (none known as of this date; re-check periodically). | A for certification record |

Official-search templates:
```text
site:nca.gov.so "data centre" OR "data center" OR datacentre
site:moct.gov.so "National Data Center" OR "data centre"
site:govsomaliland.org "data centre" OR "data center" OR "National Data Center"
site:moiid.govsomaliland.org "data centre" OR "data center" OR Wingu
site:mof.pl.so "data" OR ICT tender
site:sominvest.gov.so "data centre" OR ICT
"Somaliland" "National Data Center" 2025
"Somaliland" "Government Data and Cybersecurity Center" MICT
"Puntland" "data centre" OR "data center" e-government
"P168115" "Data Centre" Somalia
"SO-MOF-374369-GO-RFB" OR "SO-MOF-425074-CS-INDV"
```

---

## 4. English, Somali, and Arabic search patterns

### 4.1 English discovery templates

Use region + city + operator terms. For Mogadishu-market projects, run a second pass with Hargeisa/Berbera (Somaliland) and Bosaso/Garowe (Puntland) because the federal press often omits Somaliland/Puntland facilities and vice versa.

```text
"{region}" Somalia ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks OR "IT load")
"{city}" Somalia ("data centre" OR "data center") ("opened" OR launched OR operational OR construction OR "breaks ground")
"{city}" Somalia ("colocation" OR "carrier-neutral" OR hyperscale OR "AI-ready")
"Somalia" ("cloud region" OR "sovereign cloud" OR "data sovereignty") "data centre"
"Somalia" ("Tier III" OR "Uptime Institute") "data centre"
"Somalia" ("landing station" OR "subsea" OR IXP) "data centre"
"{operator}" "{region OR city}" Somalia "data centre"
```

Capacity/status pivot:
```text
"{project name}" ("MW" OR "IT load" OR MVA OR racks OR sqm)
"{project name}" ("phase one" OR "phase 1" OR expansion OR "ready for service")
"{project name}" ("commissioned" OR "operational" OR "breaks ground" OR "under construction")
"{project name}" ("solar" OR "diesel" OR "backup power" OR "substation")
```

### 4.2 Somali / Arabic secondary checks

Use Somali and Arabic only as secondary discovery on government sites and local press; verify with English/official documents. Useful terms:

- data centre: `xarunta xogta`, `xarun xogeed`; Arabic `مركز البيانات` (markaz al-bayanat)
- data storage: `kaydinta xogta`
- server: `seefar`; server room: `qolka seefaraha`
- ICT/digitalisation: `xog-ballaarinta`, `TEHAMA`/`teknolojiyada macluumaadka`
- communications ministry: `wasaaradda isgaarsiinta`; regulator: `maamulka isgaarsiinta`
- launch/opening: `kicinta`, `furfurista`, `laga bilaabay`; construction: `dhismaha`
- government: `dawladda`; cloud: usually English `cloud`

Templates:
```text
"{city}" "xarunta xogta" OR "kaydinta xogta"
"{city}" "qolka seefaraha" OR seefar "xog"
"{region}" "xog-ballaarinta" "dawladda"
"{city}" "مركز البيانات" الصومال
"{city}" "مركز بيانات"
```

Do not count a Somali/Arabic hit as a commercial datacentre unless it identifies a physical facility with compute/hosting function, operator/developer, and stage.

---

## 5. Regional-level enumeration method

For each of the 18 divisions, run four passes:

1. **Commercial press/vendor pass**: region + main cities + `data centre/data center/datacentre/colocation/hyperscale/cloud region`.
2. **Operator pass**: known Somalia operators + region/city (`Hormuud`, `Somtel`, `Telesom`, `Golis`, `NationLink`, `Wingu`, `SomaliREN`, `Somcable`, `NIRA`, `Amtel`, `Dalkom`).
3. **Official pass**: NCA/MOCT (federal), govsomaliland/moiid (Somaliland), mof.pl.so/Garowe Online (Puntland), donor documents.
4. **Interconnection/aggregator pass**: SIXP/MogIX, DARE1/2Africa landing records, PeeringDB, Baxtel, DataCenterMap, OCOLO, DataCenterPlanet; verify before grading above C/B-.

Universal region recipe:
```text
"{region}" Somalia "data centre" OR "data center" OR datacentre
"{region}" Somalia colocation OR "carrier-neutral" OR hyperscale
"{region}" Somalia "server room" OR "server farm"
"{region}" Somalia "cloud" "government" OR "e-government"
"{region}" Somalia "Tier III" OR "Uptime" "data"
"{region}" Somalia "landing station" OR IXP OR "subsea"
site:datacenterdynamics.com/en/news/ Somalia "{region}"
site:sonna.so "{region}" "data centre"
site:garoweonline.com "{region}" "data centre"
```

### 5.1 Priority clusters

| Division | Main towns/localities | Operator/developer seeds | Notes |
|---|---|---|---|
| Banaadir | Mogadishu (Hodan, Taleh Rd, 26 June analogues, industrial areas) | Hormuud, NationLink, SomaliREN, NIRA, federal NDC (MOCT/NCA), Somtel, SIXP, DARE1 landing | Highest density. Query federal NDC status, Hormuud DCs, SomaliREN DC, NIRA ABIS, enterprise server rooms. |
| Northwest (Woqooyi Galbeed) | Hargeisa, Berbera (Sahil) | Somaliland Government Data and Cybersecurity Center (Hargeisa), Wingu SL01 (Berbera), Telesom, Somtel, Somcable 2Africa (Berbera), EGS/S-Road | Second cluster. Watch "Northwest" vs "Sahil" attribution; keep Wingu in Northwest with Sahil note. |
| Awdal | Borama | Telesom/Somtel nodes, universities, SESRP education-facility solar work | Low probability; no confirmed DC found. |
| Togdheer | Burao | Telesom/Somtel coverage; Somtel contact-page "Togdheer" wording - flag | Verify any Somtel site physically; Burao likely network node only. |
| Bari | Bosaso, Qardho | Golis HQ (Bosaso), telecom core, DARE1/G2A/Somtel landing-point leads | Low-medium; search `Bosaso data centre`, `Bosaso landing station`; cable landing is not a DC. |
| Nugaal | Garowe | Golis, Puntland e-gov, mof.pl.so tenders | Low-medium; no confirmed DC found. |
| Mudug | Galkayo | Golis nodes, Hormuud 5G city, GECO/SESRP power project | Low; no confirmed DC found. |
| Lower Juba | Kismayo | NationLink/Hormuud presence, port, Peace cable landing chatter | Low; no confirmed DC found. |
| Bay | Baidoa | ATMIS/UN ICT, government offices, NIRA registration scale-up leads | Very low; expect negative for commercial DC. |
| Bakool | Hudur | telecom nodes, humanitarian/ID programme ICT | Very low; no confirmed DC found. |
| Gedo | Garbahaarey, Beled Hawo | telecom nodes, border connectivity | Very low; no confirmed DC found. |
| Hiiraan | Beledweyne | telecom nodes, humanitarian ICT | Very low; no confirmed DC found. |
| Middle Juba | Bu'aale | telecom nodes only | Very low; no confirmed DC found. |
| Middle Shabelle | Jowhar | telecom nodes, BECO service-area/power leads | Very low; no confirmed DC found. |
| Lower Shabelle | Afgooye, Merca | telecom nodes, BECO service-area/power leads | Very low; no confirmed DC found. |
| Sanaag | Erigavo | Golis/Telesom/Somtel nodes; contested administration | Very low; no confirmed DC found. |
| Sool | Las Anod | telecom nodes; conflict/contested administration | Very low; no confirmed DC found. |
| Galguduud | Dhusamareb | telecom nodes, NIRA/World Bank survey context, Galmudug e-gov | Very low; no confirmed DC found. |

### 5.2 Exact 18-division quick queries

```text
Awdal Somalia "data centre" OR "data center" OR datacentre
Bakool Somalia "data centre" OR "data center" OR datacentre
Banaadir Somalia (Hormuud OR NationLink OR SomaliREN OR NIRA OR "National Data Center") "data"
Bari Somalia (Golis OR Bosaso) "data centre"
Bay Somalia "data centre" OR "data center"
Galguduud Somalia "data centre" OR "data center"
Gedo Somalia "data centre" OR "data center"
Hiiraan Somalia "data centre" OR "data center"
"Middle Juba" Somalia "data centre" OR "data center"
"Lower Juba" Somalia (Kismayo OR NationLink) "data centre"
Mudug Somalia (Galkayo OR Golis) "data centre"
Nugaal Somalia (Garowe OR Golis OR "Puntland") "data centre"
Sanaag Somalia "data centre" OR "data center"
"Middle Shabelle" Somalia "data centre" OR "data center"
"Lower Shabelle" Somalia "data centre" OR "data center"
Sool Somalia "data centre" OR "data center"
Togdheer Somalia (Burao OR Telesom OR Somtel) "data centre"
"Northwest" OR "Woqooyi Galbeed" OR Hargeisa OR Berbera Somalia (Wingu OR Telesom OR Somtel OR "National Data Center") "data centre"
```

---

## 6. Hyperscaler and cloud-region handling

Cloud-provider pages prove region/service existence, not physical facility addresses. No hyperscaler has a Somalia region as of this methodology date.

| Provider | Official/primary URL | Somalia signal | How to use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Somalia region/Local Zone listed. | Tenant/partner/edge lead only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Somalia region listed. | Tenant/edge lead only. |
| Google Cloud | https://cloud.google.com/about/locations | No Somalia region listed. | Tenant/edge lead only. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Somalia region listed. | Tenant lead only. |
| Sovereign/government cloud | moct.gov.so ; NIRA ; govsomaliland.org ; Telesom/Somtel enterprise cloud | Federal data-sovereignty push (National Data Center), Somaliland e-gov (EGS, Somaliland NDC), operator enterprise cloud services. | Government/operator infrastructure, not hyperscaler regions; record separately with operator evidence. |

Cloud query templates:
```text
"Somalia" "cloud region" OR "public cloud" AWS OR Azure OR Google OR Oracle
"Somalia" "sovereign cloud" OR "data sovereignty" "data centre"
"Telesom" OR "Somtel" Somalia cloud "data centre"
"Somaliland" "Electronic Government Services" "data centre"
```

---

## 7. Evidence grading and common pitfalls

### 7.1 Grade per data point

- **A**: operator official location page or press release (Wingu, Somtel FGC, SomaliREN, etc.); official government/regulator document (NCA, MOCT, NIRA, SOMINVEST, World Bank/UNDP/IFC/TaiwanICDF); Uptime certification record if ever issued; ministry press release or primary procurement notice.
- **B**: DCD, Bloomberg (for quoted CEO statements), Techpoint, SONNA, Goobjoog, Garowe Online, AllAfrica/Horn Diplomat reprints, Submarine Networks, UbuntuNet, Biometric Update, Hiiraan, HigherGov/SomaliJobs procurement mirrors, credible vendor case studies.
- **C**: aggregator facility pages (datacentermap, Baxtel, OCOLO, DataCenterPlanet, datacenters.com; PeeringDB only as a lead unless it is corroborating address/interconnect for a known facility), market-report snippets, social/LinkedIn capacity claims, old MoUs, forum chatter.

### 7.2 Somalia-specific pitfalls

- **Somaliland vs federal attribution**: Wingu/Telesom/Somtel/Somcable and the Somaliland NDC belong to the Somaliland-administered context; federal NCA/MOCT records do not cleanly cover them. Keep separate, do not merge, and do not assume NCA licensing applies in Somaliland.
- **"Northwest" division mapping**: the manifest's Northwest = Woqooyi Galbeed (Hargeisa; Somaliland splits off Sahil/Berbera). Assign Wingu Berbera SL01 to Northwest with a Sahil note; avoid creating a phantom region or double-counting.
- **Portfolio vs facility**: Hormuud's "11 data centres / 10 MW" and Somtel's "3 Data Centers" are operator-level claims; per-facility records need per-site evidence (address, capacity, status). Somtel landing points and CDN plans are not facility records.
- **5G launches are not data centres**: Hormuud (Mar 2024), Somtel (Jan 2024), Telesom (Jan 2024 Hargeisa) 5G news prove network rollouts, not new DC facilities - do not mint records from them.
- **Landing stations/IXPs are not DCs**: DARE1 landing (Mogadishu, Hormuud), Somcable 2Africa (Berbera, May 2022), SIXP/MogIX - interconnect anchors only.
- **Government "data centre" ambiguity**: e-gov server rooms, NIRA enrolment centres, university labs, NGO data-collection offices are not commercial datacenters unless they host compute/storage with a named operator and location.
- **Capacity inflation and units**: no public facility-level IT-load figures found for Somali facilities; distinguish MW total power, MWp generation, MWh battery storage, and IT load. Hormuud's 10 MW is portfolio-level; BECO/SESRP solar tenders are power infrastructure, not DC capacity.
- **Stale/aspirational items**: pre-2020 fibre/ICT MoUs, LAPSSET-adjacent digital-corridor chatter, Somtel CDN plans for Mogadishu/Bosaso/Berbera, and the Aug 2026 "NDC plans" statement are intent only unless tied to a named physical site.
- **Security-driven silence**: operators underreport infrastructure details for security reasons; absence of public detail is not evidence against existence, but never assert existence without a source.
- **Aggregator errors**: Wingu Berbera is sometimes listed under "Somalia" generally or with wrong city; Hormuud entries may be single records for a multi-site portfolio. Cross-check with official pages.

### 7.3 Minimum record fields

For each project, capture: canonical facility/campus name and aliases; division (region) and town/locality (Hargeisa vs Berbera vs Mogadishu matters); administration (federal/Somaliland/Puntland); owner/operator/developer and local SPV if visible; status and status-evidence date; capacity with unit (IT MW, total power/MVA, racks, sqm, data halls); source URLs and evidence grade by field; notes on phase, solar/diesel power mix, and whether commercial, government, education-network, or enterprise-only.

---

## 8. Recommended Somalia discovery order

1. Seed from operator official pages: Hormuud, Somtel, Telesom, Golis, NationLink, Wingu, SomaliREN, Somcable, NIRA.
2. Search DCD Somalia tag, Bloomberg, Techpoint, SONNA, Goobjoog, Garowe Online, AllAfrica, Somaliland press for each seed; extract aliases, MW, phase, status verbs, and dates.
3. Verify high-value items (federal NDC, Somaliland NDC, Wingu SL01, Hormuud portfolio claims, Somtel 3-DC claim) via NCA/MOCT, govsomaliland/moiid, mof.pl.so, donor documents, or official operator releases.
4. Run the universal region recipe for all 18 divisions; stop early for low-probability regions after press/vendor + official negative sweep unless a named operator or facility emerges.
5. Resolve administration/attribution (federal vs Somaliland vs Puntland; Northwest/Sahil nuance) before deduplication, and mark every record with its grade and date.
