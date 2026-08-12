# TH Explorer - Industry / Trade Press / Vendor Discovery for Thailand Datacenters

Date: 2026-08-12. Scope: Thailand (TH) datacenter enumeration through Thai and English search, trade press, operator/vendor pages, industrial-estate sources, BOI/EEC investment approvals, and province-level query patterns. Reliability grades: **A** = primary operator, government, BOI/EEC/IEAT, SET filing, cloud-region documentation, or permit record; **B** = established trade press / Thai business press with named project facts; **C** = aggregators, broker summaries, social posts, local promotional MoUs, or unsourced reposts.

---

## 0. Thailand-specific search model

Thailand does not have a single public datacenter registry. Enumeration works by triangulating:

1. **BOI and investment approvals** for project company, province, investment amount, and sometimes IT load.
2. **Operator/developer pages** for facility names, marketed locations, current service status, capacity, and go-live dates.
3. **Thai business press** for the Thai legal names and province-level approval text.
4. **Global datacenter trade press** for hyperscale campuses, groundbreakings, financing, and international operator entries.
5. **Industrial-estate/EEC sources** for exact estate names in Chonburi, Rayong, Chachoengsao, Samut Prakan, Pathum Thani, and Ayutthaya.
6. **Power, water, EIA/EHIA, construction, and local opposition reporting** for large greenfield campuses whose operator pages are not yet public.

The core market is **Bangkok + Greater Bangkok + Eastern Economic Corridor (EEC)**:

- **Bangkok**: legacy carrier hotels/telco DCs, STT Bangkok campus, Telehouse Bangkok, True IDC, INET, NT/CAT, AIS/CSL, TCC Technology, NIPA/PROEN, exchange/interconnect sites, cloud-region control-plane references.
- **Samut Prakan**: Bang Na/Bang Phli corridor, True IDC East Bangna, ETIX Bangkok, GSA/AIS-Singtel-Gulf expansion, TikTok/data-hosting capacity, logistics/industrial sites close to Bangkok.
- **Pathum Thani / Nonthaburi**: North Muang Thong, AIS Tellus, OneAsia, Rangsit/Chaeng Watthana government-telco corridors.
- **Chonburi**: Amata City Chonburi, Digital Park Thailand/EECd, WHA/Amata/Pinthong estates, DayOne/GDS Chonburi Tech Park, Bridge DC, Google data center, Digital Edge/B.Grimm, NTT Amata/SUPERNAP/Datazone/TCC, CtrlS, True IDC, dense BOI pipeline.
- **Rayong**: WHA Eastern Seaboard estates, WHA ESIE 4/5, CPGC Industrial Estate, Amata City Rayong, Map Ta Phut/industrial power nodes, GSA, Stratus/Galaxy/Haoyang-style BOI projects, hyperscale land banks.
- **Chachoengsao**: Gateway City, Bang Pakong/Ban Pho, DAMAC/Skyline and TikTok/data-hosting approval trails, EEC spillover.

Outside this corridor, expect mostly smaller enterprise/telecom/edge facilities: **Chiang Mai, Khon Kaen, Phuket, Songkhla/Hat Yai, Nakhon Ratchasima, Ayutthaya, Nakhon Pathom, Surat Thani**. Still sweep every province because legacy NT/CAT, AIS, True, INET, university, and provincial cloud/government sites can appear under `IDC`, `ศูนย์ข้อมูล`, or `ศูนย์คอมพิวเตอร์` rather than "data center."

## 1. Thai language query vocabulary

Use Thai terms first for local approvals and business press. Search both Thai and English company names.

Core nouns:

```text
ดาต้าเซ็นเตอร์
ดาต้า เซ็นเตอร์
ดาต้าเซนเตอร์
ศูนย์ข้อมูล
ศูนย์ข้อมูลคอมพิวเตอร์
ศูนย์คอมพิวเตอร์
ศูนย์ประมวลผลข้อมูล
ศูนย์บริการข้อมูล
อินเทอร์เน็ตดาต้าเซ็นเตอร์
ไอดีซี
IDC
Data Center
Data Centre
Cloud Region
Cloud Service
Data Hosting
Hyperscale Data Center
AI Data Center
GPU
server
เซิร์ฟเวอร์
คลาวด์
```

Status and evidence words:

```text
ขอรับการส่งเสริมการลงทุน
ส่งเสริมการลงทุน
บีโอไอ
BOI
อนุมัติ
ไฟเขียว
โครงการ
มูลค่าลงทุน
ตั้งอยู่ที่จังหวัด
นิคมอุตสาหกรรม
เขตพัฒนาพิเศษภาคตะวันออก
EEC
EECd
เช่าพื้นที่
ซื้อที่ดิน
ลงนาม
MOU
วางศิลาฤกษ์
เริ่มก่อสร้าง
ก่อสร้าง
เปิดให้บริการ
เปิดดำเนินการ
ให้บริการเชิงพาณิชย์
รองรับ IT Load
กำลังการใช้ไฟฟ้า
เมกะวัตต์
MW
หม้อแปลง
สถานีไฟฟ้า
สายส่ง
น้ำ
EIA
EHIA
ผังเมือง
```

Thai templates:

```text
"{จังหวัดไทย}" ("ดาต้าเซ็นเตอร์" OR "ดาต้าเซนเตอร์" OR "ศูนย์ข้อมูล") ("บีโอไอ" OR "ส่งเสริมการลงทุน" OR "อนุมัติ")
"{จังหวัดไทย}" ("Data Center" OR "Data Centre" OR "Data Hosting") ("BOI" OR "IT Load" OR "MW")
"{จังหวัดไทย}" ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล") ("นิคมอุตสาหกรรม" OR "EEC" OR "ซื้อที่ดิน" OR "เช่าพื้นที่")
"{จังหวัดไทย}" ("ดาต้าเซ็นเตอร์" OR "AI Data Center") ("วางศิลาฤกษ์" OR "เริ่มก่อสร้าง" OR "เปิดให้บริการ")
"{บริษัทไทย}" ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล" OR "Data Center") ("{จังหวัดไทย}" OR "{นิคม}")
site:boi.go.th "{จังหวัดไทย}" "data center"
site:boi.go.th "{จังหวัดไทย}" "ดาต้าเซ็นเตอร์"
site:osos.boi.go.th "{จังหวัดไทย}" "Data Center"
site:eeco.or.th "{จังหวัดไทย}" ("Data Center" OR "ดาต้าเซ็นเตอร์")
site:ieat.go.th "{นิคม}" ("Data Center" OR "ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล")
```

Thai stage mapping:

- `ขอรับการส่งเสริมการลงทุน` / BOI application = pipeline only, **B/C** unless BOI approval is explicit.
- `อนุมัติ` / `ไฟเขียว` by BOI = approved project, **A-** for province, investment, and legal entity.
- `ลงนาม` / `MOU` = intent, **C** unless paired with land lease, BOI approval, or construction.
- `เช่าพื้นที่` / `ซื้อที่ดิน` / `ตั้งอยู่ที่นิคม...` = land/site signal, **A-/B** depending on source.
- `วางศิลาฤกษ์` / `เริ่มก่อสร้าง` = construction, **B** from press, **A** from operator/industrial-estate/government.
- `เปิดให้บริการ` / `เปิดดำเนินการ` / `commercial operation` = operational claim; verify with operator page, customer/network listing, or cloud-region page.

## 2. High-signal Thai business and tech press

Use Thai press to recover legal company names, Thai spellings, local province names, and BOI approval wording. Grade as **B** unless the article embeds a government/operator source.

| Source | Search route | Use | Grade |
|---|---|---|---|
| BOI News / OSOS BOI | `https://www.boi.go.th/`, `https://osos.boi.go.th/` | Best primary source for approved investment batches. Recent BOI releases name True IDC, GSA, Stellar DC, TikTok/data hosting, provinces, IT load, and investment amounts. | A |
| Bangkok Biz News | `site:bangkokbiznews.com ดาต้าเซ็นเตอร์ BOI จังหวัด` | Strong Thai business coverage of BOI approvals and province shares; often lists Thai legal names and IT load. | B+ |
| Prachachat | `site:prachachat.net ดาต้าเซ็นเตอร์ BOI ชลบุรี ระยอง` | High-yield for WHA/Google, BOI board approvals, and industrial-estate winners. | B+ |
| Thansettakij | `site:thansettakij.com ดาต้าเซ็นเตอร์ ชลบุรี ระยอง` | Useful for provincial investment clusters and industrial estate context. | B |
| The Standard Wealth | `site:thestandard.co ดาต้าเซ็นเตอร์ BOI` | Useful on TikTok/data-hosting distinctions, FastPass, resource regulation, and policy debates. | B |
| Bangkok Post | `site:bangkokpost.com "data centre" Thailand BOI` | English local business source; good for AWS, WHA, policy, utilities, and investment. | B |
| The Nation Thailand / Thai Enquirer / Krungthep Turakij English | site-scoped searches | Good secondary discovery for government announcements; verify details. | B-/C+ |
| Manager, Matichon, Daily News, Thai PBS, local provincial media | Thai site-scoped searches | Useful for local opposition, water/power, construction, zoning, and EIA leads. | C+/B- |

Useful Thai source queries:

```text
site:bangkokbiznews.com "ดาต้าเซ็นเตอร์" "IT Load"
site:prachachat.net "ดาต้าเซ็นเตอร์" "ชลบุรี"
site:prachachat.net "ดาต้าเซ็นเตอร์" "ระยอง"
site:thansettakij.com "ดาต้าเซ็นเตอร์" "บีโอไอ"
site:thestandard.co "Data Hosting" "TikTok" "กรุงเทพฯ"
site:bangkokpost.com Thailand "data centre" WHA
site:bangkokpost.com Thailand "data center" BOI "Rayong"
```

## 3. Global trade press and market sources

These are the fastest way to discover international operators. Use them as **B** for event facts; verify capacity and province through primary/operator/BOI sources.

| Source | Search route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | `site:datacenterdynamics.com Thailand "data center"` | Best live feed for STT, DayOne/GDS, Bridge DC, True IDC, BOI approvals, ByteDance/TikTok, Doma/DIG, CtrlS, Huawei, Empyrion, Gorilla, NTT. | B+ |
| W.Media | `site:w.media Thailand "data center"` | Strong APAC trade coverage of BOI batches, Digital Edge/B.Grimm, DIG, operator conferences, regional market context. | B |
| Dgtl Infra, Capacity Media, Light Reading, RCR Wireless, Data Centre Magazine | site-scoped queries | Good for hyperscaler/cloud announcements and financing; verify against official pages. | B-/C+ |
| Mongabay / environmental investigations | `site:mongabay.com Thailand data center Chonburi Rayong water` | Useful for local-impact, water, power, construction cluster leads. Not a facility registry. | B for reported facts, C for counts unless sourced |
| DC Byte, Cushman & Wakefield, JLL, CBRE, Knight Frank, Mordor, ResearchAndMarkets | site-scoped queries | Market capacity, pipeline, land/power context. Use aggregate values cautiously and do not treat paid database snippets as facility proof. | B/C |
| Baxtel, DataCenterMap, Datacenters.com, Cloudscene, PeeringDB, Console Connect | search by Thailand/province/operator | Useful for legacy facility addresses, interconnection-enabled sites, and nearby-facility discovery. Never use alone for final capacity. | C, sometimes B when sourced |

Trade-press templates:

```text
site:datacenterdynamics.com Thailand "{operator}" "data center"
site:datacenterdynamics.com Thailand "{province}" "MW"
site:w.media Thailand "{operator}" "{province}"
site:dgtlinfra.com Thailand "data center" "{operator}"
site:capacitymedia.com Thailand "data center" "{operator}"
"{operator}" Thailand "groundbreaking" "data center"
"{operator}" Thailand ("ready for service" OR "commercial operation" OR "IT load")
```

## 4. Primary government, industrial-estate, and regulatory sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Thailand Board of Investment (BOI) press releases | `https://www.boi.go.th/index.php?page=press_releases2&language=en`, Thai pages, OSOS mirror | Named approvals. Example: January 2026 BOI release lists True Internet Data Center in Chonburi/Samut Prakan, GSA Data Center 05 in WHA Eastern Seaboard Industrial Estate 5 Rayong and Samut Prakan, and Stellar DC in Bangkok. | A |
| BOI Promoted Company Database | `https://www.boi.go.th/index.php?language=en&page=form_promoted_companies` | Search legal names after press discovery. May expose promoted-company status, activity, province, approval date. | A-/B+ |
| EEC Office | `https://www.eeco.or.th/` | EECd/Digital Park Thailand, CtrlS lease, Chonburi/Rayong/Chachoengsao promotion areas, FastPass context. | A |
| Industrial Estate Authority of Thailand (IEAT) | `https://www.ieat.go.th/en` and estate pages | Exact estate names, location details, land-user files where posted, OSS/project announcements. Search Amata City Chonburi, WHA Eastern Seaboard, Gateway City, CPGC, Pinthong, Bang Pa-In, Hi-Tech. | A-/B |
| Industrial estate developers | Amata `https://amata.com/`, WHA `https://www.wha-industrialestate.com/`, Pinthong, Rojana, TFD, Asia Industrial Estate | Project announcements and estate data-center positioning. Amata has official GDS/DayOne Chonburi announcements; WHA is key for Google/Rayong. | A-/B |
| Provincial/governor and municipality pages | `site:{province}.go.th`, municipal domains | Local approvals, community meetings, zoning, water/power concern, groundbreaking ceremonies. | A-/B |
| ONEP / EIA / EHIA routes | ONEP/EIA portals and Thai queries with `EIA`, `EHIA`, `รายงานผลกระทบสิ่งแวดล้อม` | Large campuses may leave environmental assessment, water, drainage, building, and public-hearing traces. Search project company and estate names. | A when official |
| Energy/utility sources | MEA, PEA, EGAT, ERC, provincial electricity authority tenders | High-load connection, substation, grid capacity, direct PPA/third-party access policy. Search `สถานีไฟฟ้า`, `หม้อแปลง`, `สายส่ง`, `MW`, `MVA`. | A/B |
| SET filings / annual reports | SET/Thai listed-company IR pages: TRUE, ADVANC/AIS, GULF, BGRIM, AMATA, WHA, STECON, INET, PROEN | Best for capex, JV ownership, land, financing, and current operation. | A |

Official search templates:

```text
site:boi.go.th "Data Center" "Thailand" "IT load"
site:boi.go.th "ดาต้าเซ็นเตอร์" "IT Load"
site:boi.go.th "GSA Data Center" OR "จีเอสเอ ดาต้า"
site:boi.go.th "True Internet Data Center" "ชลบุรี"
site:boi.go.th "Stellar DC" "Bangkok"
site:osos.boi.go.th "TikTok System (Thailand)" "Data Hosting"
site:eeco.or.th CtrlS "data center" "Chonburi"
site:ieat.go.th "Amata City Chonburi" "data center"
site:ieat.go.th "WHA Eastern Seaboard" "data center"
site:amata.com "data center" "Chonburi"
site:wha-industrialestate.com "data center" "Chonburi" OR "Rayong"
site:set.or.th GULF "GSA Data Center"
site:set.or.th BGRIM "Digital Edge"
site:set.or.th AMATA "data center"
site:set.or.th WHA "Google" "data center"
```

## 5. Operator, developer, and vendor seed list

Official pages are **A** for claimed presence and marketed facility status. Capacity is **A-** when stated at named facility level by the operator; treat full-campus buildout and policy targets as **B/C** until phase-specific.

| Operator / developer | Primary routes | Thailand location signals and query pivots | Notes |
|---|---|---|---|
| ST Telemedia Global Data Centres Thailand | `https://www.sttelemediagdc.com/th-en/locations/bangkok` | `STT Bangkok 1 Hua Mak`, `STT Bangkok 2`, `STT Bangkok 3 One Bangkok`, `เอสที เทเลมีเดีย ดาต้าเซ็นเตอร์ กรุงเทพ` | Bangkok anchor. STT Bangkok 1 is Hua Mak; STT Bangkok 2 is under construction for Q4 2026 service in DCD/operator coverage; Bangkok 3 is in One Bangkok/CBD. |
| True IDC | `https://www.trueidc.com/en/`, Thai site and CP/TRUE filings | `True IDC East Bangna Samut Prakan`, `North Muangthong Nonthaburi`, `Midtown Ratchada`, `Pattanakarn`, `True IDC Chonburi Samut Prakan 223MW`, Thai `ทรู อินเทอร์เน็ต ดาต้า เซ็นเตอร์` | Major domestic operator and BOI-approved hyperscale pipeline. Watch duplicate legacy/current names. |
| GSA Data Center / AIS / Gulf / Singtel-Nxera | BOI, GULF/AIS/SET filings, Nxera/Singtel releases | `GSA Data Center 01 Samut Prakan`, `GSA Data Center 02 Chonburi`, `GSA Data Center 05 Rayong Samut Prakan`, Thai `จีเอสเอ ดาต้า เซนเตอร์` | Primary trail often through BOI and SET rather than a rich public facility page. JV ownership matters for developer field. |
| AIS Business / CSL / AIS Cloud | `https://www.ais.th/`, AIS Cloud page, Oracle announcement | `AIS DATA CENTER TELLUS Pathum Thani`, `AIS DATA CENTER CW Tower Ratchada`, `AIS Cloud Oracle Alloy Thailand`, Thai `เอไอเอส คลาวด์` | AIS Cloud/Oracle Alloy proves local hyperscale cloud service, not necessarily a new AIS-owned building unless facility is named. |
| Oracle / AIS Cloud | Oracle Alloy announcement and AIS Cloud page | `Oracle Alloy AIS Cloud Thailand`, `OCI AIS Cloud`, `AIS Cloud local cloud` | Use as cloud-service evidence; pivot to AIS/GSA facilities for physical DC enumeration. |
| AWS | About Amazon AWS Thailand Region announcement and AWS region docs | `AWS Asia Pacific Thailand Region`, `AWS 190 billion baht 2037`, `AWS data center Rayong`, Thai `AWS ดาต้าเซ็นเตอร์ ระยอง` | Officially announced Thailand Region and investment; physical provinces often require BOI/press/industrial-estate verification. |
| Google | Google Cloud Bangkok region blog; Google investment releases | `Google Cloud Bangkok region`, `Google Chonburi data center WHA`, Thai `กูเกิล ดาต้าเซ็นเตอร์ ชลบุรี WHA` | Official cloud region is Bangkok; Thai press reports WHA/Chonburi data center. Separate cloud region from physical campus. |
| Microsoft | Microsoft APAC Thailand commitment page and Azure region list | `Microsoft Thailand datacenter region`, `ไมโครซอฟท์ ศูนย์ข้อมูล ประเทศไทย` | Official commitment proves planned region; physical sites remain opaque until operator/permit/BOI evidence emerges. |
| DayOne / GDS International | `https://dayonedc.com/market/greater-bangkok`, DayOne releases, Amata release | `DayOne Chonburi Tech Park CTP1 CTP2`, `GDS International Amata City Chonburi`, `1GW power platform` | Key Chonburi greenfield campus. Treat 1GW as platform/MOU target; capture phase-specific CTP1/CTP2 status separately. |
| Bridge Data Centres / Bain Capital | Bridge pages, DCD, BOI | `Bridge Data Centres Thailand QH101 Chonburi`, `Bridge Data Centres IIO Thailand 134MW`, Thai `บริดจ์ ดาต้า เซ็นเตอร์ ไอไอโอ ชลบุรี` | BOI/trade press gives Chonburi capacity variants by entity/project; avoid merging QH101 and BOI entities without proof. |
| Digital Edge / B.Grimm Power | `https://www.digitaledgedc.com/products-services/data-centers/thailand/`, Digital Edge press | `Digital Edge B.Grimm Chonburi BKK1`, `100MW EEC`, Thai `ดิจิทัล เอดจ์ บีกริม ชลบุรี` | Official pages state BKK1/BKK Campus in EEC/Chonburi, 100MW, ready Q4 2026. |
| NTT Global Data Centers / NTT DATA | NTT pages, DCD, Baxtel/market directories, Amata/IEAT leads | `NTT Bangkok 2 Amata`, `NTT Bangkok 3 Chonburi`, `NTT Amata`, Thai `เอ็นทีที ดาต้าเซ็นเตอร์ อมตะ` | Facilities may be marketed as Bangkok while physically in Chonburi/Amata. Record province from estate/address. |
| Telehouse Bangkok / KDDI | `https://www.telehouse.com/` and Telehouse Bangkok pages | `Telehouse Bangkok`, Thai `เทเลเฮาส์ กรุงเทพ` | Central Bangkok carrier-neutral/interconnect site; official page high grade. |
| SUPERNAP Thailand | official site, Uptime, DCD | `SUPERNAP Thailand Chonburi`, `ซูเปอร์แนป ชลบุรี` | Operational Chonburi hyperscale colo since 2017; verify exact site and capacity via official/Uptime/trade sources. |
| ETIX Everywhere / ETIX Bangkok | ETIX pages, network listings | `ETIX Bangkok Samut Prakan`, Thai `อีทิกซ์ กรุงเทพ สมุทรปราการ` | Smaller but important Samut Prakan colo/edge signal. |
| OneAsia Network / One As1a | OneAsia pages, Console Connect, market directories | `OneAsia Thailand Pathum Thani`, `One As1a Pathum Thani` | Verify spelling and owner; directories can be noisy. |
| Internet Thailand (INET) | `https://www.inet.co.th/`, SET filings | `INET-IDC Bangkok`, `INET Saraburi`, `INET3`, Thai `อินเทอร์เน็ตประเทศไทย ศูนย์ข้อมูล` | Listed Thai cloud/DC operator; use annual reports for facilities and capacity. |
| NT / CAT / TOT legacy | NT official pages, government/telco docs, PeeringDB | `NT Data Center Bangrak`, `CAT Telecom Tower IDC`, `TOT Chaeng Watthana data center`, provincial CAT data centers | Legacy government/telco sites appear in many provinces and carrier hotels. Distinguish active commercial DC from old exchange/server rooms. |
| TCC Technology | `https://www.tcc-technology.com/` | `TCC Technology Bangna`, `TCC Technology Amata Nakorn`, `Empire Tower data center` | Enterprise/colo facilities in Bangkok/Chonburi. |
| NIPA / PROEN / Datazone / KIRZ / ISSP / SiamIDC / local ISPs | official pages, PeeringDB, DataCenterMap | Thai company name + `IDC`, `ศูนย์ข้อมูล`, `CAT Tower` | Useful for Bangkok carrier hotel enumeration; many are legacy colocation rooms. |
| Empyrion Digital, Doma Infrastructure Group (DIG), DAMAC/Skyline, Freyr, Vistas, Stratus, Galaxy Peak, Beijing Haoyang, CloudHQ, Gorilla | BOI, DCD/W.Media, Thai press, company pages | Legal entity + province + `BOI`, `IT Load`, `นิคม` | Often project-SPV led. Treat as approved/planned until operator confirms groundbreaking or service date. |

Operator query templates:

```text
"{operator}" Thailand ("data center" OR "data centre" OR "datacenter") ("MW" OR "IT load" OR "ready for service")
"{operator}" "{province}" ("data center" OR "data centre" OR "นิคมอุตสาหกรรม")
"{operator legal Thai}" ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล") ("บีโอไอ" OR "IT Load")
site:{operator-domain} Thailand "{province}"
site:{operator-domain} "Bangkok" "data center"
site:{operator-domain} "Chonburi" OR "Rayong" "data center"
```

## 6. Hyperscaler and cloud-region handling

Cloud regions prove service availability or planned sovereign/local infrastructure, not a physical facility address unless the source names a data center province.

| Provider | Official route | Thailand enumeration use |
|---|---|---|
| AWS | About Amazon Thailand Region announcement; AWS global infrastructure docs | **A** for Thailand region/investment. Search AWS + Rayong/Chonburi/Samut Prakan/BOI/industrial estate for physical-site evidence. |
| Google Cloud | Google Cloud Bangkok region blog; Google investment announcements | **A** for Bangkok cloud region and USD 1bn investment. Thai press says first data center is in Chonburi/WHA; verify with Google/WHA/BOI/local sources before facility record. |
| Microsoft Azure | Microsoft APAC May 1, 2024 Thailand commitment; Azure region list | **A** for announced Thailand datacenter region. Physical facilities are not public; use as demand signal until BOI/operator/permit evidence emerges. |
| Oracle / AIS Cloud | Oracle Alloy + AIS Cloud pages | **A** for AIS-operated local hyperscale cloud platform. Physical building should be mapped through AIS/GSA/operator pages, not assumed from Oracle. |
| TikTok / ByteDance | BOI/OSOS, Thai press, DCD | BOI/data-hosting approvals span Bangkok, Samut Prakan, Chachoengsao in Thai press. Distinguish `Data Hosting` from owned datacenter unless source states facility construction or server installation in specific DCs. |

Pivot queries:

```text
"AWS" Thailand Region "data centers located in Thailand"
"AWS" Thailand Rayong "data center" "BOI"
"Google" Thailand "Chonburi" "data center" WHA
"Google Cloud" "Bangkok region" Thailand "data center"
"Microsoft" Thailand "datacenter region" "Bangkok"
"TikTok System (Thailand)" "Data Hosting" "กรุงเทพฯ" "สมุทรปราการ" "ฉะเชิงเทรา"
"ByteDance" Thailand "data center" "BOI"
"Oracle Alloy" "AIS Cloud" Thailand data center
```

## 7. Province and regional enumeration playbook

For every province, run the generic English/Thai templates, then add the province-specific pivots below. Use Thai province names because local press and BOI reposts often use only Thai.

### 7.1 Highest-priority regions

| Province / region | Thai name | Hot localities / estates | Developer seeds | Query pivots |
|---|---|---|---|---|
| Bangkok | กรุงเทพมหานคร, กรุงเทพฯ | Hua Mak/Ramkhamhaeng, One Bangkok, Ratchada/Ratchadaphisek, Bang Rak/CAT Tower, Bang Na edge, Pattanakarn, Sathorn/Empire, Huai Khwang, CW Tower references | STT, Telehouse, True IDC, AIS/CSL, INET, NT/CAT/TOT, TCC, NIPA/PROEN, KIRZ, ISSP, Stellar DC, Google Cloud region | `"กรุงเทพฯ" "ดาต้าเซ็นเตอร์" "เปิดให้บริการ"`, `"Bangkok" "carrier-neutral data center"`, `"Stellar DC" Bangkok BOI`, `"STT Bangkok" "Hua Mak"` |
| Samut Prakan | สมุทรปราการ | Bang Phli, Bang Na-Trat corridor, Suvarnabhumi/logistics parks | True IDC East Bangna, GSA, ETIX, TikTok/data hosting, Freyr | `"สมุทรปราการ" "ดาต้าเซ็นเตอร์" "IT Load"`, `"Bang Phli" "data center"`, `"East Bangna" "True IDC"`, `"GSA" "Samut Prakan"` |
| Nonthaburi | นนทบุรี | Muang Thong Thani, Chaeng Watthana edge | True IDC North Muangthong, NT/TOT, government/enterprise | `"นนทบุรี" "ดาต้าเซ็นเตอร์"`, `"North Muangthong" "data center"`, `"เมืองทองธานี" "ดาต้าเซ็นเตอร์"` |
| Pathum Thani | ปทุมธานี | Rangsit, Khlong Luang, Lam Luk Ka, Tellus, OneAsia/One As1a | AIS Tellus, OneAsia/One As1a, BOI pipeline | `"ปทุมธานี" "ดาต้าเซ็นเตอร์" "บีโอไอ"`, `"AIS DATA CENTER TELLUS"`, `"One As1a" "Pathum Thani"` |
| Chonburi | ชลบุรี | Amata City Chonburi, EECd/Digital Park Thailand, Sriracha, Laem Chabang, Pinthong, WHA Chonburi, Datazone, Amata Nakorn | DayOne/GDS, Bridge DC, Google/WHA, Digital Edge/B.Grimm, True IDC, GSA, NTT, SUPERNAP, CtrlS, Doma/DIG, Vistas, Datazone, TCC | `"ชลบุรี" "ดาต้าเซ็นเตอร์" "IT Load"`, `"Amata City Chonburi" "data center"`, `"EECd" "data center"`, `"WHA" "Google" "Chonburi"`, `"DayOne" "Chonburi Tech Park"` |
| Rayong | ระยอง | WHA Eastern Seaboard Industrial Estate 4/5, CPGC Industrial Estate, Amata City Rayong, Map Ta Phut, Pluak Daeng | GSA, Stratus, Galaxy Peak, Beijing Haoyang, AWS site rumors, Freyr, DIG/Doma | `"ระยอง" "ดาต้าเซ็นเตอร์" "IT Load"`, `"WHA Eastern Seaboard Industrial Estate 5" "data center"`, `"CPGC Industrial Estate" "data center"`, `"GSA Data Center 05" Rayong` |
| Chachoengsao | ฉะเชิงเทรา | Gateway City, Bang Pakong, Ban Pho, EEC industrial clusters | DAMAC/Skyline, TikTok/data hosting, Doma/DIG, industrial-estate pipeline | `"ฉะเชิงเทรา" "ดาต้าเซ็นเตอร์"`, `"Gateway City" "data center"`, `"Skyline Data Center" "Chachoengsao"`, `"TikTok System" "ฉะเชิงเทรา"` |
| Phra Nakhon Si Ayutthaya | พระนครศรีอยุธยา, อยุธยา | Bang Pa-In, Hi-Tech Industrial Estate, Rojana, Wang Noi | Edge/industrial estate prospects, legacy enterprise/DR | `"อยุธยา" "ดาต้าเซ็นเตอร์"`, `"Bang Pa-In Industrial Estate" "data center"`, `"Hi-Tech Industrial Estate" "data center"` |

### 7.2 Secondary regional hubs and legacy telco/edge provinces

| Province | Thai name | Why query | Templates |
|---|---|---|---|
| Chiang Mai | เชียงใหม่ | NT/CAT legacy IDC, northern edge/cloud/government sites, university/DR | `"เชียงใหม่" ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล" OR "IDC")`, `"CAT" "Chiang Mai" "data center"` |
| Khon Kaen | ขอนแก่น | Northeast edge, NT/CAT legacy IDC, smart-city/cloud projects | `"ขอนแก่น" "ดาต้าเซ็นเตอร์"`, `"Khon Kaen" "data center" "CAT"` |
| Nakhon Ratchasima | นครราชสีมา, โคราช | Northeast industrial/logistics node, DR/edge potential | `"นครราชสีมา" "ดาต้าเซ็นเตอร์"`, `"โคราช" "ศูนย์ข้อมูล"` |
| Phuket | ภูเก็ต | NT/CAT legacy IDC, tourism/edge, subsea/connectivity references | `"ภูเก็ต" "ดาต้าเซ็นเตอร์"`, `"Phuket" "data center" "CAT"` |
| Songkhla / Hat Yai | สงขลา, หาดใหญ่ | Southern telco IDC, Malaysia route, Rubber City/Songkhla IE | `"หาดใหญ่" "ดาต้าเซ็นเตอร์"`, `"Songkhla" "data center" "NT"` |
| Surat Thani | สุราษฎร์ธานี | Southern edge/DR, provincial cloud | `"สุราษฎร์ธานี" "ศูนย์ข้อมูล"`, `"Surat Thani" "data center"` |
| Nakhon Pathom | นครปฐม | Bangkok west spillover, land/power, university/enterprise | `"นครปฐม" "ดาต้าเซ็นเตอร์"`, `"Nakhon Pathom" "data center"` |
| Ratchaburi | ราชบุรี | Power generation, Bangkok west spillover | `"ราชบุรี" "ดาต้าเซ็นเตอร์" "ไฟฟ้า"`, `"Ratchaburi" "data center"` |
| Saraburi | สระบุรี | INET/industrial/DR leads, central corridor | `"สระบุรี" "ดาต้าเซ็นเตอร์"`, `"INET" "Saraburi" "data center"` |
| Lopburi | ลพบุรี | Power/solar land, central corridor; low probability but cheap sweep | `"ลพบุรี" "ดาต้าเซ็นเตอร์"`, `"Lopburi" "data center"` |

### 7.3 All-province sweep strings

For complete coverage, iterate the 77 provinces. For each province, run:

```text
"{province_en}" Thailand ("data center" OR "data centre" OR datacenter OR "server farm" OR "cloud region" OR "data hosting")
"{province_th}" ("ดาต้าเซ็นเตอร์" OR "ดาต้าเซนเตอร์" OR "ศูนย์ข้อมูล" OR "IDC" OR "ไอดีซี")
"{province_th}" ("บีโอไอ" OR "ส่งเสริมการลงทุน" OR "นิคมอุตสาหกรรม") ("ดาต้าเซ็นเตอร์" OR "Data Center")
"{province_th}" ("เมกะวัตต์" OR "IT Load" OR "MW") ("ดาต้าเซ็นเตอร์" OR "Data Center")
"{province_th}" ("สถานีไฟฟ้า" OR "หม้อแปลง" OR "สายส่ง" OR "น้ำ") ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล")
```

Province Thai names to use:

```text
กรุงเทพมหานคร
กระบี่
กาญจนบุรี
กาฬสินธุ์
กำแพงเพชร
ขอนแก่น
จันทบุรี
ฉะเชิงเทรา
ชลบุรี
ชัยนาท
ชัยภูมิ
ชุมพร
เชียงราย
เชียงใหม่
ตรัง
ตราด
ตาก
นครนายก
นครปฐม
นครพนม
นครราชสีมา
นครศรีธรรมราช
นครสวรรค์
นนทบุรี
นราธิวาส
น่าน
บึงกาฬ
บุรีรัมย์
ปทุมธานี
ประจวบคีรีขันธ์
ปราจีนบุรี
ปัตตานี
พระนครศรีอยุธยา
พะเยา
พังงา
พัทลุง
พิจิตร
พิษณุโลก
เพชรบุรี
เพชรบูรณ์
แพร่
ภูเก็ต
มหาสารคาม
มุกดาหาร
แม่ฮ่องสอน
ยโสธร
ยะลา
ร้อยเอ็ด
ระนอง
ระยอง
ราชบุรี
ลพบุรี
ลำปาง
ลำพูน
เลย
ศรีสะเกษ
สกลนคร
สงขลา
สตูล
สมุทรปราการ
สมุทรสงคราม
สมุทรสาคร
สระแก้ว
สระบุรี
สิงห์บุรี
สุโขทัย
สุพรรณบุรี
สุราษฎร์ธานี
สุรินทร์
หนองคาย
หนองบัวลำภู
อ่างทอง
อำนาจเจริญ
อุดรธานี
อุตรดิตถ์
อุทัยธานี
อุบลราชธานี
```

## 8. Estate and locality pivots

Data center announcements often name the estate but not the district. Search these estate names with both English and Thai datacenter terms:

```text
Amata City Chonburi
Amata City Chonburi 2
Amata Smart City Chonburi
Amata City Rayong
นิคมอุตสาหกรรมอมตะซิตี้ ชลบุรี
นิคมอุตสาหกรรมอมตะซิตี้ ระยอง
WHA Eastern Seaboard Industrial Estate
WHA Eastern Seaboard Industrial Estate 4
WHA Eastern Seaboard Industrial Estate 5
WHA Industrial Estate Rayong
นิคมอุตสาหกรรมดับบลิวเอชเอ
CPGC Industrial Estate
นิคมอุตสาหกรรมซีพีจีซี
Gateway City Industrial Estate
นิคมอุตสาหกรรมเกตเวย์ซิตี้
Pinthong Industrial Estate
นิคมอุตสาหกรรมปิ่นทอง
Digital Park Thailand
EECd
เขตส่งเสริมอุตสาหกรรมและนวัตกรรมดิจิทัล
Bang Pa-In Industrial Estate
นิคมอุตสาหกรรมบางปะอิน
Hi-Tech Industrial Estate
นิคมอุตสาหกรรมไฮเทค
Rojana Industrial Park
สวนอุตสาหกรรมโรจนะ
TFD Industrial Estate
Laem Chabang
แหลมฉบัง
Bang Pakong
บางปะกง
Bang Phli
บางพลี
Bang Na
บางนา
Rangsit
รังสิต
```

Estate query examples:

```text
"Amata City Chonburi" ("data center" OR "data centre" OR "datacenter")
"นิคมอุตสาหกรรมอมตะซิตี้ ชลบุรี" ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล")
"WHA Eastern Seaboard Industrial Estate 5" "GSA Data Center"
"WHA Eastern Seaboard Industrial Estate 4" ("data center" OR "Haoyang" OR "AWS")
"Gateway City Industrial Estate" "Skyline Data Center"
"Digital Park Thailand" CtrlS "data center"
```

## 9. Evidence rules and common pitfalls

- **Do not equate "Bangkok" marketing with Bangkok province.** Many facilities marketed as Bangkok or Greater Bangkok are physically in Samut Prakan, Pathum Thani, Nonthaburi, Chonburi, or Rayong.
- **Separate cloud region, data hosting, and physical DC.** AWS/Google/Microsoft/AIS Cloud/TikTok announcements prove infrastructure demand; only count a physical facility when a source names a site/province or operator/campus.
- **Separate BOI project companies.** GSA Data Center 01/02/05, Bridge Data Centres IIO/III, True IDC project approvals, and Digital Edge SPVs may refer to different phases or sites. Do not merge unless the source links them.
- **Capacity language varies.** BOI often states `IT Load`; operators may state `power capacity`, `critical IT load`, `campus power`, `MVA`, or full-buildout MW. Store only phase-specific MW when possible; note buildout separately.
- **Thai press uses Buddhist Era dates.** Convert BE to CE by subtracting 543. Example: 15 มกราคม 2569 = 2026-01-15.
- **The BOI approval date is not the operational date.** Status should be `approved` unless construction/groundbreaking/opening is independently sourced.
- **MOU/GW platform announcements are pipeline.** DIG/Doma 1.5GW and DayOne 1GW platform language should not be recorded as a single operational facility.
- **Legacy carrier hotel lists are noisy.** CAT Tower, True Tower, TCC Empire, CSL/CAT/TOT entries may describe colocated rooms inside old telco buildings; verify current operator pages or network listings.
- **Environmental/resource articles are good leads, not registries.** Use them to find construction sites, communities, and provinces, then verify with operator/government sources.

## 10. Minimal enumeration workflow per province

1. Run the all-province Thai and English sweep.
2. Search BOI/OSOS for province + `Data Center` / `ดาต้าเซ็นเตอร์`.
3. Search the province with known operator seeds: STT, True IDC, GSA, AIS, Gulf, Singtel/Nxera, NTT, DayOne, GDS, Bridge, Digital Edge, B.Grimm, Google, AWS, Microsoft, TikTok, DAMAC/Skyline, Empyrion, SUPERNAP, Telehouse, INET, NT, TCC, ETIX, OneAsia.
4. If the province is in or near EEC/Greater Bangkok, add estate/locality terms.
5. Search Thai business press for the legal company name and province.
6. Search official/operator pages and SET/annual-report pages for confirmation.
7. Search power/water/EIA terms for large campuses or disputed sites.
8. If only an MoU or policy target exists, record as `announced`/`planned` with **C/B** evidence and notes. If no credible project exists, mark `no_projects`.

