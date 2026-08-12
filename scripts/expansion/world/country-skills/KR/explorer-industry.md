# KR Explorer - Industry, Trade Press, Vendors, and Regional Query Patterns

Date: 2026-08-12. Scope: South Korea datacenter enumeration using Korean tech/trade press, vendor/operator pages, market reports, and repeatable province/city query templates. Reliability grades: **A** = primary/official operator, government, exchange filing, cloud-region documentation, or permitting record; **B** = established trade press / industry press / broker market report with named project details; **C** = aggregator, real-estate marketing, unsourced repost, or local promotional article that only proves intent.

---

## 0. Search model for Korea

South Korea discovery is not a single registry problem. The best workflow is:

1. Seed from large operators and official cloud-region pages (**A/A-**).
2. Add Korean trade press for new campuses, power constraints, and AI datacenter announcements (**B**).
3. Query each si/gun/gu with Korean project terms and local approval/status words.
4. Verify planned projects through company releases, local government MOU pages, construction permits, power/substation reporting, or follow-up articles.

Use Korean terms first. English searches find global colo players and broker reports, but they miss many provincial MOUs and industrial-park projects.

Core Korean terms:

```text
데이터센터
AI 데이터센터
인공지능 데이터센터
AIDC
인터넷데이터센터
IDC
클라우드센터
전산센터
통합전산센터
집적정보통신시설
서버팜
GPU 데이터센터
하이퍼스케일 데이터센터
```

Status / evidence words:

```text
건축허가
사업계획
투자협약
업무협약
MOU
착공
기공식
준공
개소
가동
운영
입주
수전용량
전력
변전소
송전선로
환경영향평가
교통영향평가
산업단지
도시첨단산업단지
지식산업센터
민원
주민반대
```

Capacity words:

```text
MW
메가와트
GW
기가와트
수전설비
IT부하
전산실
상면
랙
캐비닛
서버
연면적
부지면적
총사업비
투자액
```

## 1. Korean trade and industry press

Use these as the live-change feed. Grade project facts as **B** unless the article embeds or links an official release, permit, DART filing, or company announcement.

| Source | URL | Use | Grade |
|---|---|---|---|
| Electronic Times / 전자신문 | https://www.etnews.com/ | Best Korean ICT trade press for telcos, Naver/Kakao/Samsung SDS, national AI computing center, and new IDC construction. Search `site:etnews.com 데이터센터 {회사}`. | B |
| Digital Daily / 디지털데일리 | https://www.ddaily.co.kr/ | Strong cloud/IDC beat; good for KT/LG U+/SKB expansion, Google/MS lease rumors, weekly cloud roundups. Search mobile pages too: `site:ddaily.co.kr 데이터센터 평촌 부천 파주`. | B |
| ZDNet Korea | https://zdnet.co.kr/ | Good for AI infrastructure policy, national AI computing-center bidding, cloud operators, and site visits. | B |
| Bloter | https://www.bloter.net/ | Useful for telco earnings and IDC/AIDC revenue narratives; good secondary source for major-company strategy. | B |
| IT Chosun | https://it.chosun.com/ | Telecom/AI/datacenter business coverage; good on SKT/KT/LG U+ strategic comparisons. | B |
| KHARN / 칸 | https://www.kharn.kr/ | HVAC, cooling, RE100, energy, KDCC report coverage; useful for operator lists and policy constraints. | B |
| The Elec / 디일렉 | https://www.thelec.kr/ | Semiconductor/IT infrastructure angle; useful for disaster-management obligations and AI hardware links. | B |
| Yonhap / 연합뉴스 | https://www.yna.co.kr/ | Best broad Korean wire for provincial MOUs and city announcements. Use it to discover, then verify locally. | B+ |
| Maeil Business / 매일경제, Pulse | https://www.mk.co.kr/ and https://pulse.mk.co.kr/ | Strong on real-estate/developer-backed DC projects, AWS/international-capital entries, opposition stories. | B |
| Korea Herald / Korea JoongAng Daily / Chosun English | https://www.koreaherald.com/, https://koreajoongangdaily.joins.com/, https://www.chosun.com/english/ | English-language summaries of major Korean projects; good for global handoff but rarely first source. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Best global trade source for AWS, Equinix, Digital Realty, STT GDC, Naver, Kakao, KT Cloud, LG U+, and provincial mega-campuses. | B |
| W.Media | https://w.media/ | APAC datacenter investor/developer coverage; useful for international developers in Korea. | B/C+ |
| DataCenterMap / Baxtel / Datacenters.com / OCOLO / Cloudscene | https://www.datacentermap.com/, https://baxtel.com/, https://www.datacenters.com/, https://www.ocolo.io/, https://cloudscene.com/ | Facility address/capacity cross-checks and nearby-facility discovery. Never use alone for high-confidence capacity. | C, sometimes B when sourced |

High-value industry reports:

- Korea Data Center Council / 한국데이터센터연합회 (KDCC): https://kdcc.or.kr/ and publications page https://kdcc.or.kr/kdcc/bbsNew_list.do?code=sub04b&keyvalue=sub04. KDCC reports are the best domestic market census source, but public samples may expose only tables of contents. **A-/B+** for market counts, not facility-level proof unless a specific list is visible.
- Cushman & Wakefield Korea Seoul Data Centre MarketBeat: https://www.cushmanwakefield.com/en/south-korea/insights/seoul-data-center-marketbeat-report. Good for Greater Seoul Area operational MW, pipeline MW, and named construction pipeline snapshots. **B+**.
- Cushman & Wakefield "Data Centres & The Power Challenge" PDF: `assets.cushmanwakefield.com/.../cwresearchdatacentresthepowerchallenge2025eng.pdf`. Useful for grid-constraint logic and decentralization trend. **B+**.
- KESIS / Korea Energy Economics Institute summaries sometimes quote KDCC national DC counts, e.g. 500 sqm-plus DC counts. Use for national context only. **B**.

## 2. Operator and vendor seed list

Official operator pages are **A** for existence and broad location. Treat marketing capacity as **A-** when it gives a named facility and **B** if it gives rounded future capacity without a facility-level filing.

| Operator / developer | Official URL / evidence | Search pivots | Notes |
|---|---|---|---|
| NAVER / NAVER Cloud | NAVER Data Center GAK: https://datacenter.navercorp.com/ ; NAVER Cloud history: https://www.navercloudcorp.com/ko/info/ | `네이버 데이터센터 각 춘천`, `네이버 데이터센터 각 세종`, `NAVER GAK Sejong`, `각 세종 수전용량`, `각 세종 270MW` | Anchor sites: GAK Chuncheon, Gangwon-do; GAK Sejong, Sejong. DCD and DataCenterMap report Sejong as 270 MW, but verify status/capacity against NAVER release and local press. |
| Kakao | Official Ansan release: https://www.kakaocorp.com/page/detail/11140?lang=ENG ; sustainability page: https://sustainability.kakao.com/en/data-centers | `카카오 데이터센터 안산`, `카카오 안산 데이터센터 4000랙`, `카카오 제2 데이터센터`, `카카오 데이터센터 시흥 하남 경기` | Kakao Data Center Ansan is first in-house hyperscale facility: Hanyang University ERICA campus, Ansan, Gyeonggi-do; official release gives 47,378 sqm, 4,000 racks, 120,000 servers, operation from Jan 2024. |
| KT Cloud | IDC service: https://www.ktcloud.com/service/idc?lan=eng | `KT클라우드 IDC`, `KT 가산 IDC`, `KT 부천 IDC`, `KT 경북 AI 클라우드 데이터센터 예천`, `KT 목동 IDC`, `KT 용산 IDC` | KT Cloud is the most important domestic IDC operator. Official pages plus PeeringDB/OCOLO/DataCenterMap help enumerate Seoul/Gyeonggi/Busan/Daejeon/Daegu/Gyeongbuk sites. |
| LG U+ | AIDC page: https://www.lguplus.com/biz/solution/type/aidc ; Pyeongchon 2 completion: https://www.lguplus.com/biz/insight/trend/367 | `LG유플러스 평촌메가센터`, `LG유플러스 평촌2센터`, `LG유플러스 파주 AI 데이터센터`, `LG유플러스 논현 IDC` | Key clusters: Anyang/Pyeongchon, Seoul Nonhyeon, Paju AI-ready DC. Official Pyeongchon 2 article gives 40,450 sqm and 200,000-plus servers. LG Corp release says Pyeongchon Mega Center planned 165 MW power supply. |
| SK Broadband / SK Telecom | SKT older cloud DC release: https://www.sktelecom.com/en/press/press_detail.do?idx=941 ; use SKB site and trade press | `SK브로드밴드 가산 IDC`, `SK브로드밴드 일산 IDC`, `SK브로드밴드 분당 IDC`, `SKT AI 데이터센터 가산`, `SKB 울산 데이터센터`, `SKB 구로 데이터센터` | Gasan is a key Seoul AI/IDC site; DCD reported SKB Gasan 46 MW IT load and 44 kW/rack support in SKT/Lambda context. Verify new Guro/Ulsan plans through SKB/SKT releases or permits. |
| Samsung SDS | https://www.samsungsds.com/ plus DART filings | `삼성SDS 데이터센터 상암`, `삼성SDS 수원 데이터센터`, `삼성SDS 구미 AI 데이터센터`, `삼성SDS DART 데이터센터` | For listed-company projects, use DART (https://dart.fss.or.kr/) to verify board resolutions, land purchases, and investment amounts. |
| LG CNS | https://www.lgcns.com/ plus facility brochures | `LG CNS 상암 IT센터`, `LG CNS 부산 글로벌 클라우드 데이터센터`, `LG CNS 인천 데이터센터`, `LG CNS 가산 데이터센터` | Important enterprise/financial/cloud integrator. Older facility brochures expose locations; verify operational status with official pages and disaster-management lists. |
| SK C&C / SK Inc. C&C | https://www.skcc.co.kr/ | `SK C&C 판교 데이터센터`, `SK C&C 대덕 데이터센터`, `판교 데이터센터 화재` | Pangyo fire coverage can create duplicate/incident noise. Use for facility existence, not expansion pipeline unless sourced. |
| NHN Cloud | https://www.nhncloud.com/ | `NHN클라우드 데이터센터 광주`, `NHN클라우드 김해 데이터센터`, `NHN클라우드 순천 데이터센터`, `NHN클라우드 국가AI컴퓨팅센터` | Regional cloud/AI projects often appear first in local press and government releases. |
| KINX | https://www.kinx.net/infrastructure/dc/?lang=en | `KINX 도곡 IDC`, `KINX 가산 IDC`, `KINX 과천 IDC`, `케이아이엔엑스 데이터센터` | Official page lists Dogok, Gasan, Bundang, and Gwacheon. Strong interconnection operator; useful for cloud on-ramp discovery. |
| Digital Realty | Seoul page: https://www.digitalrealty.com/data-centers/asia-pacific/seoul ; ICN10: https://www.digitalrealty.com/data-centers/asia-pacific/seoul/icn10 | `Digital Realty ICN10`, `디지털리얼티 상암 데이터센터`, `디지털리얼티 김포 64MW` | ICN10 is Mapo/Sangam. Official Seoul page gives 132,000 ft2 / 12,263 sqm; 2026 press release says max 12 MW IT capacity. Digital Realty also announced a 64 MW Gimpo/Gurae-dong facility in 2021; verify current status separately. |
| Equinix | https://www.equinix.com/data-centers/asia-pacific-colocation/korea-colocation/seoul-data-center | `Equinix SL1 Seoul`, `Equinix SL2x`, `Equinix SL4`, `에퀴닉스 고양 데이터센터` | Official page lists SL1, SL2x, SL4; SL2x/SL4 are Goyang/Hyangdong area in Gyeonggi-do. |
| ST Telemedia Global Data Centres | https://www.sttelemediagdc.com/kr-en/locations/seoul | `STT Seoul 1`, `STT GDC 가산 데이터센터`, `ST텔레미디어 데이터센터 서울` | Official page says STT Seoul 1 is in Gasan-dong, Geumcheon-gu, Seoul and supports 30 MW IT load. |
| AWS | Official region docs: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | `AWS 인천 데이터센터`, `AWS 가좌 데이터센터`, `AWS 경기도 AI 데이터센터`, `아마존웹서비스 5조 데이터센터` | AWS official confirms Asia Pacific (Seoul), ap-northeast-2, 4 AZs. Physical facilities require press, permits, and market reports; DCD/Maeil reported Incheon and Gyeonggi AI DC investment. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | `Azure Korea Central Seoul`, `Azure Korea South Busan`, `MS 5673 코리아 데이터센터`, `마이크로소프트 부산 데이터센터` | Official page maps Korea Central to Seoul and Korea South to Busan. MS 5673 Korea appears on disaster-management lists; physical sites are usually leased/opaque. |
| Google Cloud | Locations: https://cloud.google.com/about/locations ; Compute zones: https://docs.cloud.google.com/compute/docs/regions-zones | `Google Cloud Seoul region`, `구글 클라우드 서울 리전 LG유플러스`, `구글 데이터센터 한국 임대` | Official region is `asia-northeast3` Seoul with zones a/b/c. DCD reported the region is colocated in existing DCs; use lease rumors cautiously. |
| Oracle Cloud | Regions: https://www.oracle.com/cloud/public-cloud-regions/ ; docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | `Oracle ap-seoul-1`, `Oracle ap-chuncheon-1`, `오라클 춘천 리전 데이터센터` | Official regions: South Korea Central (Seoul) and South Korea North (Chuncheon). |
| YIDO / IGIS / Pacific AMC / Keppel / DCI / AirTrunk / Vantage / NTT / Digital Edge | Company pages, DCD, W.Media, broker reports | `이도 청라 데이터센터`, `이지스 데이터센터 안산`, `퍼시픽자산운용 데이터센터`, `케펠 의정부 데이터센터`, English operator + Korea city | International-capital and real-estate developers often surface through market reports and permit lists before official facility pages. Grade carefully. |

## 3. Official-ish lists that help vendor enumeration

- Disaster-management obligated datacenter operators: Korea's MSIT designated major communications/disaster-management operators after the Kakao/SK C&C incident. KDI policy mirror of MSIT release lists datacenter operators: KT Cloud, LG U+, SK Broadband, Samsung SDS, LG CNS, SK C&C, NAVER Cloud, MS 5673 Korea. URL: https://eiec.kdi.re.kr/policy/materialView.do?num=241365&pg=&pp=20&topic=C. **A-/B+** as a government-policy mirror; use it as an operator seed, not facility census.
- ETNews coverage of the same designation includes the legal threshold: datacenter operators with computer-room floor area 22,500 sqm or usable max power capacity 40 MW plus revenue over KRW 10bn. URL: https://www.etnews.com/20230728000215. **B**, useful for interpreting why some operators are listed.
- DART filings: https://dart.fss.or.kr/. Use for Samsung SDS, LG U+, KT, SK Telecom/SKB, KINX, Kakao, NAVER, LG CNS parent-related disclosures, construction investment, asset sales, and board resolutions. **A**.
- Local government/IFEZ/GFEZ/industrial-park pages: **A** for public project facts if directly hosted by city/province/free economic zone; **C** if only an investment-attraction brochure without construction evidence.

## 4. Query templates

### 4.1 National operator sweep

```text
"{회사명}" ("데이터센터" OR "IDC" OR "AI 데이터센터") ("준공" OR "개소" OR "착공" OR "건축허가" OR "투자")
site:{operator-domain} ("데이터센터" OR "IDC") ("센터" OR "MW" OR "랙" OR "서버")
site:dart.fss.or.kr "{회사명}" 데이터센터 투자
site:etnews.com "{회사명}" 데이터센터
site:ddaily.co.kr "{회사명}" IDC
site:zdnet.co.kr "{회사명}" "AI 데이터센터"
site:datacenterdynamics.com Korea "{operator}" "data center"
```

### 4.2 Province / city / district sweep

Use both romanized and Hangul names. Hangul is higher yield.

```text
"{시군구_한글}" ("데이터센터" OR "AI 데이터센터" OR "IDC") ("건축허가" OR "착공" OR "준공" OR "가동")
"{시군구_한글}" ("데이터센터" OR "IDC") ("투자협약" OR "업무협약" OR "MOU")
"{시군구_한글}" ("데이터센터" OR "AI 데이터센터") ("산업단지" OR "도시첨단산업단지" OR "경제자유구역")
"{시군구_한글}" ("데이터센터" OR "IDC") ("수전용량" OR "변전소" OR "전력")
"{시군구_한글}" ("데이터센터" OR "IDC") ("주민반대" OR "민원" OR "소송" OR "공청회")
site:{city-domain}.go.kr 데이터센터
site:{province-domain}.go.kr "{시군구_한글}" 데이터센터
site:yna.co.kr "{시군구_한글}" 데이터센터
```

### 4.3 Capacity and status extraction

```text
"{프로젝트명}" ("MW" OR "메가와트" OR "수전용량" OR "IT부하")
"{프로젝트명}" ("연면적" OR "부지면적" OR "전산실" OR "상면")
"{프로젝트명}" ("랙" OR "캐비닛" OR "서버")
"{프로젝트명}" ("준공" OR "가동" OR "상업운영" OR "운영개시")
"{프로젝트명}" ("취소" OR "철회" OR "무산" OR "중단" OR "보류")
```

### 4.4 English fallback

```text
"{city}" Korea "data center" MW
"{city}" South Korea "AI data center"
"{operator}" Korea "data center" "{city}"
"Greater Seoul Area" "data center" pipeline MW
"Incheon" "data center" AWS YIDO Cheongna Gajwa
"Gyeonggi" "data center" "construction permit"
```

## 5. Regional enumeration playbook

For each GeoNames admin2 division, translate the prefix and city/district to Hangul, then run the generic templates. Prioritize these known clusters and operators.

### Greater Seoul Area: Seoul, Gyeonggi-do, Incheon

This is the highest-density market and should be enumerated gu/si by gu/si.

Seoul query clusters:

```text
서울 금천구 가산 데이터센터 OR IDC
서울 구로구 데이터센터 OR IDC
서울 양천구 목동 데이터센터 OR IDC
서울 용산구 데이터센터 OR IDC
서울 영등포구 여의도 데이터센터 OR IDC
서울 강남구 도곡 논현 데이터센터 OR IDC
서울 마포구 상암 데이터센터 OR IDC
서울 서초구 데이터센터 SK브로드밴드
```

Known/pivotal operators and places: KT Cloud Gasan/Mokdong/Yongsan/Yeouido/Namguro/Gangnam, SKB Gasan/Ilsan/Bundang/Seocho, KINX Dogok/Gasan, Digital Realty ICN10 Sangam/Mapo, Equinix SL1 Mapo/Sangam, STT Seoul 1 Gasan/Geumcheon, LG U+ Nonhyeon. Use official pages where possible.

Gyeonggi query clusters:

```text
경기도 안양 평촌 데이터센터 LG유플러스
경기도 안산 카카오 데이터센터 한양대 ERICA
경기도 성남 분당 판교 데이터센터 SK C&C KT KINX
경기도 고양 향동 에퀴닉스 SL2x SL4 데이터센터
경기도 부천 데이터센터 KT Tongyang
경기도 김포 구래동 디지털리얼티 64MW 데이터센터
경기도 과천 KINX 데이터센터
경기도 파주 LG유플러스 AI 데이터센터
경기도 의정부 케펠 데이터센터
경기도 용인 데이터센터
경기도 시흥 데이터센터
```

Known/pivotal operators and places: Kakao Ansan; LG U+ Pyeongchon/Paju; KT Bundang/Bucheon; SK C&C Pangyo; KINX Bundang/Gwacheon; Equinix Goyang/Hyangdong; Digital Realty Gimpo proposal; Keppel Uijeongbu; many real-estate backed developments in Bucheon/Ansan/Gimpo/Siheung/Yongin.

Incheon query clusters:

```text
인천 서구 가좌 데이터센터 AWS
인천 서구 청라 데이터센터 이도 YIDO
인천 서구 원창동 데이터센터
인천 미추홀구 도화동 데이터센터 건축허가
인천 남동구 구월 AI 허브 데이터센터
인천 중구 인천공항 AI 데이터센터
인천 연수구 송도 데이터센터
인천 계양구 LG CNS 인천 데이터센터
IFEZ 데이터센터 청라 송도
```

Known/pivotal operators and places: AWS Incheon/Gajwa reporting; YIDO Cheongna/Wonchang-dong; Hana Financial Cheongna integrated DC; Kyobo-IBM Songdo/IFEZ; LG CNS Incheon; airport AI hub reports. Incheon has frequent NIMBY and permit-delay stories, so search `주민반대`, `건축허가`, `소송`, and `변전소`.

### Gangwon-do

Core searches:

```text
강원 춘천 데이터센터 네이버 각 춘천
춘천 오라클 클라우드 리전 데이터센터
원주 데이터센터 AI 데이터센터
강릉 데이터센터 수열 에너지
동해 데이터센터 해저케이블
```

Known anchors: NAVER GAK Chuncheon, Oracle `ap-chuncheon-1`. Provincial prospects often cite cool climate, hydro/water cooling, or renewable energy; verify beyond tourism-style promotion.

### Sejong-si

Core searches:

```text
세종 데이터센터 각 세종 네이버
세종 AI 데이터센터 오케스트로
세종 데이터센터 금융센터 건축허가
세종 데이터센터 무산 철회
```

Known anchor: NAVER GAK Sejong. Treat other Sejong finance-center/office-conversion proposals carefully and search for `무산`, `철회`, `취소`.

### Chungcheongnam-do / Chungcheongbuk-do

Core searches:

```text
충남 당진 석문 데이터센터 AI 데이터센터
당진 데이터센터 300MW NFD Korea
천안 데이터센터 AI 데이터센터
아산 데이터센터 클라우드
내포 데이터센터 홍성 예산
충북 제천 데이터센터 4산업단지
음성 데이터센터 네이버 후보지
청주 데이터센터 AI 데이터센터
진천 데이터센터 산업단지
```

Known patterns: Dangjin/Seokmun and Jecheon industrial-park announcements; many are MOUs with long 2028-2031 horizons. Grade as **B/C** until power contract, building permit, or construction evidence appears.

### Daejeon

Core searches:

```text
대전 데이터센터 KT
대전 국가정보자원관리원 데이터센터
대전 유성구 데이터센터
대전 서구 IDC
```

Known anchors: public-sector/National Information Resources Service environment and KT Daejeon-type facilities. Distinguish government compute centers from commercial colo.

### Gyeongsangbuk-do / Daegu

Core searches:

```text
경북 예천 KT AI 클라우드 데이터센터
예천 데이터센터 KT클라우드 10MW
구미 삼성SDS AI 데이터센터
구미 하이테크밸리 AI 데이터센터
구미 데이터센터 300MW 1.3GW
포항 데이터센터 AI 데이터센터
안동 수열 AI 데이터센터
대구 데이터센터 KT IDC
```

Known anchors: KT Cloud Gyeongbuk/Yecheon AI Cloud DC; Samsung SDS Gumi AI DC; Gumi High-Tech Valley mega-cluster announcements. Large GW-scale Gumi claims need strict verification via DART/local government and phase-by-phase status.

### Gyeongsangnam-do / Busan / Ulsan

Core searches:

```text
부산 데이터센터 Azure Korea South
부산 강서구 데이터센터
부산 해운대 KT 송정 GHC 데이터센터
부산 글로벌 클라우드 데이터센터 LG CNS
김해 데이터센터 NHN클라우드
창원 데이터센터 AI 데이터센터
울산 SK브로드밴드 데이터센터
울산 AI 데이터센터
양산 데이터센터
```

Known anchors: Azure Korea South maps to Busan at cloud-region level; KT Songjeong/GHC and LG CNS Busan Global Cloud Data Center are recurring facility pivots; Ulsan appears in SKB expansion reporting. Use Busan city and district searches because "Korea South" cloud-region pages do not expose exact facilities.

### Jeollanam-do / Gwangju / Jeollabuk-do

Core searches:

```text
광주 국가 AI 데이터센터 NHN 클라우드
광주 첨단3지구 AI 데이터센터
전남 광양 클라우드 데이터센터
광양 황금산단 데이터센터 KT Microsoft
나주 데이터센터 한국전력
여수 데이터센터
전북 전주 데이터센터
군산 데이터센터 재생에너지
새만금 데이터센터 AI
```

Known patterns: Gwangju AI/NHN Cloud and Gwangyang/Hwanggeum industrial complex. For Jeolla projects, industrial-park and renewable-energy framing is common; separate signed investment agreements from permitted construction.

### Jeju-do

Core searches:

```text
제주 AI 데이터센터
제주 데이터센터 해상풍력
제주 BARO AI 데이터센터
제주 과학캠퍼스 데이터센터
제주 데이터센터 40MW
```

Likely to surface planned AI/renewable-energy proposals. Grade as **B/C** unless the project has a named developer, site, power plan, and construction schedule.

## 6. Verification rules and grading

Evidence hierarchy for each project field:

1. **A** - Operator official page/release; DART filing; government/municipal permit or investment-agreement page; official cloud-region docs for region existence; IFEZ/GFEZ/industrial-zone official project page.
2. **B+** - KDCC/Cushman/JLL/CBRE-style market report with named pipeline; Yonhap or established Korean trade press with named site, developer, and capacity.
3. **B** - DCD/W.Media/Korean business press based on company statements or local reporting.
4. **C** - DataCenterMap/Baxtel/OCOLO/Datacenters.com alone, real-estate marketing PDFs, local promo articles, unsourced blogs.

Status rules:

- `MOU`, `투자협약`, `업무협약`: planned/intent only. Do not mark construction without `착공`, `기공식`, `건축허가`, or visible construction evidence.
- `건축허가`: approved, not necessarily under construction.
- `착공` / `기공식`: construction.
- `준공`, `개소`, `가동`, `상업운영`: operational or opening; verify if it is whole campus vs phase 1.
- Search negative terms before finalizing: `{프로젝트명} 무산`, `{프로젝트명} 취소`, `{프로젝트명} 철회`, `{프로젝트명} 주민반대`, `{프로젝트명} 지연`.

Capacity sanity:

- Korean articles may report total future campus power (`1.3GW`, `300MW`) while phase 1 is much smaller. Store phase capacity separately when possible.
- `수전용량` / `power supply` is not always IT load. Prefer explicit `IT부하`, `IT load`, or operator market-report definitions.
- Server counts are marketing-friendly: 100,000+ servers may not imply live installed capacity.
- `상면`, `전산실`, and `연면적` are different area metrics. Do not compare them directly.

Common duplicate traps:

- Seoul market pages may list a facility by metro, while the physical site is in Goyang, Anyang, Seongnam, Bucheon, or Incheon.
- Operator, landlord, SPC, and brand names can differ: e.g. a project may appear under developer/asset manager, construction company, and future operator.
- Cloud regions prove service availability, not exact physical facility ownership.
- Public-sector "통계데이터센터" or "데이터 안심구역" pages are often data-access centers, not datacenter buildings.

## 7. Recommended enumeration order

1. Build the operator seed table from MSIT disaster-management list, KDCC materials, and official pages for NAVER, Kakao, KT Cloud, LG U+, SKB/SKT, Samsung SDS, LG CNS, SK C&C, NHN Cloud, KINX, Digital Realty, Equinix, STT GDC, AWS, Azure, Google, Oracle.
2. Sweep Greater Seoul Area by si/gun/gu first: Seoul gu, Gyeonggi cities, Incheon gu. Use Korean terms plus operator names.
3. Sweep provincial industrial-park projects: Dangjin, Jecheon, Yecheon, Gumi, Gwangju, Gwangyang, Busan, Ulsan, Jeju, Andong, Pohang, Saemangeum/Gunsan.
4. For every hit, run capacity/status/negative-term searches and assign evidence grade per field.
5. Cross-check with DART and local-government pages for listed-company or MOU projects.
6. Use aggregators only to fill address candidates or nearby aliases, then re-query the address in Korean.

## 8. Copy-paste Korean division aliases

Use these Hangul aliases with the manifest's admin2 names:

```text
Seoul = 서울특별시 / 서울
Busan = 부산광역시 / 부산
Daegu = 대구광역시 / 대구
Incheon = 인천광역시 / 인천
Gwangju = 광주광역시 / 광주
Daejeon = 대전광역시 / 대전
Ulsan = 울산광역시 / 울산
Sejong-si = 세종특별자치시 / 세종
Gyeonggi-do = 경기도 / 경기
Gangwon-do = 강원특별자치도 / 강원
Chungcheongnam-do = 충청남도 / 충남
North Chungcheong = 충청북도 / 충북
Gyeongsangbuk-do = 경상북도 / 경북
Gyeongsangnam-do = 경상남도 / 경남
Jeollabuk-do = 전북특별자치도 / 전북
Jeollanam-do = 전라남도 / 전남
Jeju-do = 제주특별자치도 / 제주
```

District/city examples that routinely matter:

```text
Geumcheon-gu = 금천구 / 가산동
Guro District = 구로구 / 남구로 / 개봉동
Yangcheon-gu = 양천구 / 목동
Mapo-gu = 마포구 / 상암동
Gangnam-gu = 강남구 / 도곡동 / 논현동
Anyang-si = 안양시 / 평촌 / 동안구 관양동
Ansan-si = 안산시 / 한양대 ERICA / 초지동
Seongnam-si = 성남시 / 분당 / 판교
Goyang-si = 고양시 / 향동 / 일산
Bucheon-si = 부천시
Gimpo-si = 김포시 / 구래동
Paju-si = 파주시
Incheon Seo-gu = 인천 서구 / 가좌동 / 원창동 / 청라
Incheon Michuhol = 인천 미추홀구 / 도화동
Incheon Jung-gu = 인천 중구 / 인천공항
Chuncheon-si = 춘천시
Dangjin-si = 당진시 / 석문국가산업단지
Jecheon-si = 제천시 / 제4산업단지
Yecheon-gun = 예천군
Gumi-si = 구미시 / 구미하이테크밸리
Gwangyang-si = 광양시 / 황금산단
Gwangju Gwangsan-gu/Buk-gu = 광주 광산구 / 북구 / 첨단3지구
Busan Haeundae-gu/Gangseo-gu = 부산 해운대구 / 강서구
Jeju-si = 제주시
```
