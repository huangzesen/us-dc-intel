# KR Explorer — Official / Regulatory / Cloud Pipeline for South Korea Datacenter Enumeration

Date: 2026-08-11. Country: **KR South Korea**. Scope: methodology to enumerate datacenter projects across Korea's 17 first-level jurisdictions and 229 local governments (시/군/구) using official planning, building-permit, power, cloud-region, regulator, and operator sources. Reliability grades: **A** = official/primary legal or operator evidence, **B** = strong secondary / trade press / industry association, **C** = weak lead only.

---

## 0. Structural Facts That Shape KR Enumeration

- South Korean datacenter development is concentrated in the Seoul Capital Area (**수도권**: Seoul, Incheon, Gyeonggi), but power-grid scarcity and local opposition have pushed the government to promote non-capital locations. Search both mature 수도권 markets and new provincial AI/DC campuses.
- Building-permit evidence is unusually important because Korea added **데이터센터** as a sub-use under **방송통신시설** in the Building Act Enforcement Decree framework. Older operating DCs may still be permitted under 업무시설, 교육연구시설, 공장, or other mixed uses, so do not filter only on "데이터센터".
- Official energy evidence is less facility-public than in China. The key trail is **KEPCO/MOTIE large-load review**, **전기사용예정통지**, and, from the Distributed Energy Act era, **전력계통영향평가** for large new loads. These records are often visible indirectly through MOTIE releases, National Assembly requests, local-government minutes, and trade press rather than as a complete public project table.
- Disaster/regulatory oversight increased after the 2022 SK C&C Pangyo / Kakao outage. MSIT and KISA sources are important for operator resilience obligations, but they are not a full facility registry.
- Official cloud region pages provide operational cloud footprints: AWS Seoul, Azure Korea Central/Korea South, Google Cloud Seoul, NAVER Cloud Korea multi-zone, kt cloud, and local CSP/IDC operators.

---

## 1. Korean + English Query Patterns

Use Korean first; English results are strong for hyperscalers, REITs, global colos, and legal/regulatory summaries.

### 1.1 Building / Planning / Local-Government Searches

```
"{시군구}" 데이터센터 건축허가
"{시군구}" 데이터센터 착공 OR 준공 OR 사용승인
"{시군구}" 데이터센터 교통영향평가 OR 건축심의 OR 도시계획위원회
"{시군구}" 데이터센터 주민설명회 OR 주민반대 OR 민원
"{시군구}" 방송통신시설 데이터센터 건축
"{사업명}" 건축허가 OR 착공신고 OR 사용승인
site:{local-gov-domain}.go.kr 데이터센터 건축허가
site:{local-gov-domain}.go.kr 데이터센터 건축위원회
```

English variants:

```
"{city}" "data center" "building permit" Korea
"{city}" "data center" "construction permit" Korea
"{operator}" "{city}" "data center" "South Korea"
```

### 1.2 Power / KEPCO / MOTIE Searches

```
데이터센터 전기사용예정통지 한전 "{시군구}"
데이터센터 전력공급 한전 "{시군구}"
데이터센터 전력계통영향평가 "{시군구}"
데이터센터 수도권 집중 완화 방안
데이터센터 계통 여유 변전소 345kV
site:motie.go.kr 데이터센터 전력
site:kepco.co.kr 데이터센터 전기공급
```

English variants:

```
South Korea data center KEPCO power request
South Korea data center grid impact assessment
South Korea Distributed Energy Act data center
South Korea MOTIE data center power
```

### 1.3 Regulator / Disaster / Cloud-Security Searches

```
site:msit.go.kr 데이터센터 재난관리
site:msit.go.kr 데이터센터 보호조치
site:kisa.or.kr 데이터센터 클라우드 보안인증
클라우드 보안인증 CSAP 데이터센터
방송통신재난관리기본계획 데이터센터
```

English variants:

```
MSIT Korea data center disaster management
KISA CSAP cloud security Korea data center
Korea cloud security assurance program data residency
```

### 1.4 Cloud / Operator Searches

```
AWS 서울 리전 ap-northeast-2 가용 영역
Azure Korea Central Korea South Seoul Busan
Google Cloud 서울 리전 asia-northeast3
네이버클라우드 각 세종 춘천 데이터센터
카카오 데이터센터 안산 4,000랙 120,000서버
kt cloud IDC 용산 목동 분당 가산 AI DC
SK브로드밴드 IDC 서초 일산 분당 가산
LG CNS 데이터센터 상암 부산 가산 인천
KINX 데이터센터 가산 도곡 상암
Equinix SL1 Seoul data center
Digital Realty ICN data center Seoul
```

---

## 2. Grade-A Official Planning / Building-Permit Sources

### 2.1 Seumteo / e-AIS Building Administration System (세움터)

- Main portal: https://www.eais.go.kr/
- Mobile building-register search: https://m.eais.go.kr/mbi/mbi/adb02/MBIADB02V01
- Purpose: individual building-register and permitting records. Use when a candidate address or parcel is known.
- What to extract: building use (용도), gross floor area (연면적), floors, permit/approval dates, use approval (사용승인), owner/building name where disclosed.
- Caveat: the front-end is login/captcha/session-heavy. Use it for manual verification; use data.go.kr / HUB APIs for systematic search.
- Grade: **A** for permit/register facts.

### 2.2 MOLIT Building HUB / Public Data APIs

- Building service portal: https://www.hub.go.kr/portal/psg/idx-intro-openApi.do
- Public Data portal notices identify the relevant API family as **국토교통부_건축HUB_건축인허가정보 서비스** and related building-register / energy APIs: https://www.data.go.kr/bbs/ntc/selectNotice.do?originId=NOTICE_0000000004079
- Relevant datasets/API families:
  - **건축HUB_건축인허가정보 서비스**: permit ledger, land-location, building/floor/unit summaries, temporary structures, parking, road-name ledger, zoning/area records.
  - **건축HUB_건축물대장정보 서비스**: building-register title data after completion.
  - **건축HUB_건물에너지정보 서비스**: useful for operating buildings when accessible; may not disclose datacenter-specific load cleanly.
- Systematic method:
  1. Build a table of all 229 시/군/구 administrative codes.
  2. Query permit/building-register records where building name, use, or text fields contain `데이터센터`, `IDC`, `인터넷데이터센터`, `전산센터`, `클라우드센터`, `AI 데이터센터`, `방송통신시설`.
  3. Also search large buildings under ambiguous uses (`업무시설`, `교육연구시설`, `공장`, `지식산업센터`) if operator names match KT, SK, LG CNS, NAVER, Kakao, Samsung SDS, NHN, KINX, Equinix, Digital Realty, IGIS, ESR, Actis, Brookfield, Macquarie, etc.
  4. Join permit records to local-government agenda/minutes and operator PR for status.
- Grade: **A** for permit/register attributes; **B/C** if only inferred from ambiguous building use without operator confirmation.

### 2.3 Local Government Portals and Council Minutes

Korean city/county/district governments publish many practical project traces outside the national permit UI:

- 건축위원회 / 경관위원회 / 도시계획위원회 agendas and minutes.
- 교통영향평가, 환경/소음 civil complaint notices, 주민설명회 notices.
- Local council minutes where residents challenge datacenter approvals.
- Press releases under `보도자료`, `고시공고`, `입법예고`, `행정예고`.

Query per division:

```
site:{시군구}.go.kr 데이터센터
site:{시군구}.go.kr "데이터센터" "건축위원회"
site:{시군구}.go.kr "데이터센터" "도시계획위원회"
site:{시군구}.go.kr "데이터센터" "교통영향평가"
site:{시군구}.go.kr "방송통신시설" "데이터센터"
site:{시군구}.go.kr "데이터센터" "주민설명회"
```

High-priority localities to seed first:

- Seoul: Guro-gu, Geumcheon-gu/Gasan, Gangnam, Yeongdeungpo/Yeouido, Yongsan, Yangcheon/Mok-dong.
- Gyeonggi: Seongnam/Pangyo/Bundang, Anyang/Pyeongchon, Hanam, Ansan, Bucheon, Goyang/Ilsan, Yongin, Hwaseong, Paju, Gimpo.
- Incheon: Seo-gu, Yeonsu/Songdo, Namdong.
- Outside capital area: Busan Gangseo/Mieum, Gimhae, Daejeon, Sejong, Chuncheon, Yecheon/Gyeongbuk, Ulsan, Jeonbuk Saemangeum/Gunsan, Jeonnam, Gangwon AI clusters.

Grade: **A** for official agenda/minute/permit notices, **B** for mayoral PR on MOU/groundbreaking, **C** for resident-rumor-only claims.

---

## 3. Environmental and Land Cross-Checks

### 3.1 EIASS Environmental Impact Assessment System

- Main: https://www.eiass.go.kr/ and https://eiasas.eiass.go.kr/
- Ministry description: EIASS stores original EIA documents and consultation details for completed assessments and provides public search: https://mcee.go.kr/home/web/index.do?menuId=10145
- Use: search project names, industrial parks, and city/county names. Datacenters often do **not** trigger full EIA as standalone facilities, but EIASS can catch larger industrial-complex, urban-development, renewable-energy, or power-infrastructure projects that include datacenter campuses.
- Query terms: `데이터센터`, `AI 데이터센터`, `산업단지 데이터센터`, `전력`, `변전소`, `송전선로`, `집단에너지`.
- Grade: **A** for EIA records; absence from EIASS is not evidence that a DC does not exist.

### 3.2 Land and Industrial-Park Evidence

- Use local land-sale notices (토지매각, 산업단지 분양공고), Korea ONnara / land-use systems, and local development corporations.
- Query:

```
"{시군구}" 데이터센터 부지 매각
"{산업단지}" 데이터센터 입주
"{시군구}" AI 데이터센터 산업단지
"{시군구}" 데이터센터 투자협약 OR 업무협약
```

- Grade: **B** for land/development-corporation notices unless tied to permit or KEPCO power approval; **C** for MOU-only investment announcements.

---

## 4. Power / KEPCO / MOTIE Pipeline

### 4.1 MOTIE Policy Releases

- MOTIE site: https://www.motie.go.kr/
- Data-center power dispersion policy release/PDF surfaced under searches for **데이터센터 수도권 집중 완화 방안** (MOTIE, 2023): https://www.motie.go.kr/attach/down/095a2dda9c864e1d90d751f7668a1117/f44086d3d46f975295d5c584675b08ec/13055e35ba7465cb478c5b4be490c5a8
- 11th Basic Plan for Long-Term Electricity Supply and Demand references datacenter/AI datacenter additional demand: https://www.motie.go.kr/kor/article/ATCL3f49a5a8c/170183/view
- 2026 MOTIE "mega projects" release mentions publication of **345kV substations with grid spare capacity** to support datacenter dispersion: https://motie.go.kr/kor/article/ATCL8764a1224/155119172/view

Method:

1. Search MOTIE for `데이터센터 전력`, `전력계통영향평가`, `수도권 집중 완화`, `345kV 계통 여유 변전소`.
2. Extract any named provinces/cities receiving policy support or grid-capacity disclosure.
3. Treat government-supported non-capital AI/DC zones as a priority search list, but do not count capacity until permit/power/operator evidence exists.

Grade: **A** for policy rules and aggregate demand; **B/C** for project counts if not project-level.

### 4.2 KEPCO Large-Load Signals

- KEPCO main: https://www.kepco.co.kr/
- Key term: **전기사용예정통지**. Korea uses this as a pre-application path for large prospective electricity users; public reporting notes it is used by datacenters needing roughly 5MW+ class supply. A large share of notices can be speculative, so it is a weak project signal unless followed by actual electricity-use application/contract, permit, or construction.
- Key term: **전력계통영향평가**. Under distributed-energy/grid-impact rules, large users are assessed for distribution/transmission impact; useful for datacenter siting constraints.

Search:

```
"{사업명}" "전기사용예정통지"
"{주소}" "전기사용예정통지"
"{시군구}" 데이터센터 한전 전력공급
"{시군구}" 데이터센터 전력계통영향평가
"{시군구}" 데이터센터 변전소
```

Reliability:

- **A** if a KEPCO/MOTIE/National Assembly document names the project or legal procedure.
- **B** if a credible newspaper reports KEPCO approval/supply request with named address/operator.
- **C** for anonymous "power secured" claims; Korea has documented speculative/duplicate large-load notices.

Practical use: power evidence is a filter, not a census. Use it to prioritize which permit-stage projects are plausible and which 수도권 proposals may stall.

---

## 5. MSIT / KISA / Cloud-Regulatory Sources

### 5.1 MSIT Disaster and Digital-Service Oversight

- MSIT: https://www.msit.go.kr/
- Search terms: `데이터센터 재난관리`, `방송통신재난관리기본계획`, `데이터센터 보호조치`, `부가통신사업자 데이터센터`.
- Use after the 2022 Kakao/SK C&C fire to identify regulated "major broadcasting/communications service providers" and datacenter protective-measure obligations.
- Grade: **A** for named regulated entities/rules; usually operator-level, not facility census.

### 5.2 KISA / CSAP

- KISA: https://www.kisa.or.kr/
- CSAP context: cloud security certification for services serving public-sector workloads. Public CSP compliance pages are often clearer than KISA search results; examples:
  - AWS CSAP: https://aws.amazon.com/compliance/csap/
  - Google Cloud CSAP: https://cloud.google.com/security/compliance/csap
  - Microsoft Korea CSAP overview: https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-korea-csap
- Use: identify CSPs with Korean public-sector cloud posture and data-residency/local-operations constraints; pivot CSP names into local datacenter/region searches.
- Grade: **A** for certification/compliance claims on official pages; **not** facility-level.

---

## 6. Official Cloud Region and Operator Seed List

Cloud/provider official pages establish operational presence but usually hide addresses. Use them as seeds, then pivot to building permits, operator pages, investor materials, local minutes, and grid evidence.

| Provider / operator | Official evidence | KR locations / enumeration value | Grade |
|---|---|---|---|
| AWS | Region list shows `ap-northeast-2` Asia Pacific (Seoul), 4 AZs: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; fourth AZ blog: https://aws.amazon.com/blogs/aws/now-open-fourth-availability-zone-in-the-aws-asia-pacific-seoul-region/ | Operational Seoul region; addresses undisclosed. Search colos/landlords in Seoul/Gyeonggi/Incheon and AWS Direct Connect partners. | A for region/AZ count |
| Microsoft Azure | Azure regions list: Korea Central = Seoul, Korea South = Busan: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; region pairs: https://learn.microsoft.com/en-us/azure/reliability/regions-paired | Two-region footprint (Seoul/Busan). Korea Central has AZ support; Korea South is paired DR. | A |
| Google Cloud | `asia-northeast3` Seoul, three zones: https://docs.cloud.google.com/compute/docs/regions-zones ; launch blog: https://cloud.google.com/blog/products/infrastructure/new-gcp-region-in-seoul | Operational Seoul region; use `asia-northeast3-a/b/c` as evidence of three-zone region. | A |
| NAVER Cloud | Korea multi-zone docs: https://guide.ncloud-docs.com/docs/en/environment-environment-1-1 ; NAVER Cloud tech page names GAK Sejong and GAK Chuncheon: https://www.navercloudcorp.com/en/tech_service/ ; NAVER press release on GAK Sejong operation/LEED: https://www.navercorp.com/en/media/pressReleasesDetail?seq=31846 | Chuncheon and Sejong are confirmed first-party campuses. NAVER states GAK Sejong is hyperscale, 290,000 sqm and can house 60,000+ servers on Cloud page; press pages also describe Nov 2023 operation. | A |
| Kakao | Kakao official Ansan release: https://www.kakaocorp.com/page/detail/11140?lang=ENG ; sustainability page: https://sustainability.kakao.com/en/data-centers | Kakao Data Center Ansan, Hanyang University ERICA campus, completed Sep 2023, operating Jan 2024, 47,378 sqm, 4,000 racks, 120,000 servers, 6 EB. Search second Gyeonggi/80MW plan separately and treat as planned until permit evidence. | A |
| kt cloud | IDC official: https://www.kt-idc.com/ ; service page: https://www.ktcloud.com/service/idc?lan=eng | Official DC list includes Yongsan, Mokdong 1/2, Yeouido, Bundang, Gangnam, Namguro, Songjeong, Daejeon, Gimhae, Cheonan, Gyeongbuk, Gasan. Strong operator census. | A |
| SK Broadband | Official press/blog on Bundang smart IDC: https://blog.skbroadband.com/entry/%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C-SK%EB%B8%8C%EB%A1%9C%EB%93%9C%EB%B0%B4%EB%93%9C-%EB%B6%84%EB%8B%B9%EC%97%90-%EC%8A%A4%EB%A7%88%ED%8A%B8-%EC%9D%B8%ED%84%B0%EB%84%B7%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%84%BC%ED%84%B0-%EC%98%A4%ED%94%88 | Confirms Bundang center and earlier Seocho/Il-san centers; supplement with SKB pages, filings, and trade press for Gasan/Bundang 2. | A/B |
| LG CNS | Official data center page: https://www.lgcns.com/us/service/modern-it-infra-on-cloud/data-center.html | Names Sangam IT Center, Busan Global Cloud Data Center, Gasan IT Center, and Incheon history. | A |
| Korea Data Center Council (KDCC) | Association: https://kdcc.or.kr/ ; member list: https://kdcc.or.kr/kdcc/pageview.do?keyvalue=sub02&url=sub02a ; publications: https://kdcc.or.kr/kdcc/bbsNew_list.do?code=sub04b&keyvalue=sub04 | Best industry association for market report counts, member universe, and Green Data Center certification. Reports are partly member/password-gated; member list is a strong operator/vendor seed. | B+ |

Other operator seeds to search and verify: Samsung SDS, NHN Cloud, KINX, LG Uplus/Pyeongchon Mega Center, SK C&C/Pangyo, Equinix Korea (SL1/SL2/ICN), Digital Realty Seoul/ICN, DEUS, OneAsia/Empyrion, Macquarie-backed Hanam Data Center, ESR/Actis/IGIS datacenter real-estate vehicles.

---

## 7. Per-Division Enumeration Workflow (229 시/군/구)

1. **Seed operators and official cloud regions.** Start from kt cloud, NAVER, Kakao, LG CNS, SK Broadband, AWS/Azure/GCP, KDCC member list, and global colo pages.
2. **Build a 229-division matrix.** For each 시/군/구, run Korean queries for `데이터센터`, `IDC`, `인터넷데이터센터`, `AI 데이터센터`, `전산센터`, `클라우드센터`, and `방송통신시설`.
3. **Pull building-permit/register evidence.** Use Building HUB/data.go.kr APIs for broad search; use Seumteo for manual address validation. Record permit date, use approval, building use, gross floor area, and address.
4. **Search local government/council records.** Capture 건축위원회, 도시계획위원회, 교통영향평가, 주민설명회, 고시공고, and council minutes. These often reveal stalled or controversial projects before operator PR.
5. **Power plausibility check.** Search KEPCO/MOTIE terms around each site. Mark `전기사용예정통지` as "power-request lead" unless confirmed by supply contract, permit progression, or construction.
6. **Regulatory/cloud cross-check.** Use MSIT/KISA only to identify regulated CSP/operator universe; do not count them as facility evidence.
7. **Status resolution.** Suggested lifecycle: MOU/투자협약 < permit/건축허가 < 착공/공사중 < 준공/사용승인 < operator "open/operation" announcement. Count as operational only with use approval or first-party/trade press operation evidence.
8. **Dedupe.** Korea often has one physical campus described by landlord, investor SPV, operator, cloud brand, district nickname, and building name. Dedupe on parcel/address + operator/tenant graph + power-supply point.

---

## 8. Evidence Grades and Pitfalls

| Evidence | Grade | Notes |
|---|---|---|
| Seumteo / Building HUB permit and building-register records | A | Best source for legal building existence and completion; watch older non-DC use categories. |
| Local-government committee minutes, notices, ordinances | A | Good for proposed and contested projects; status may be pre-construction. |
| MOTIE / KEPCO named power records | A | Often aggregate; project-level detail is scattered. |
| EIASS records | A | Strong where applicable, but many standalone DCs do not appear. |
| Official cloud region docs | A | Region/city/AZ existence only; no address/capacity. |
| Operator official DC pages / press releases | A for existence/status; B for design capacity | First-party, but capacity is often design maximum. |
| KDCC market reports / member list | B+ | Best association source; not a free facility registry. |
| Trade press (DCD, ETNews, Digital Daily, ChosunBiz, Korea Herald, Maeil/Pulse) | B | Excellent discovery feed; verify with permit/power/operator evidence. |
| Resident opposition articles, blogs, real-estate brokerage decks | C | Useful leads; high rate of speculative projects. |

Pitfalls:

- **전기사용예정통지 is not a project approval.** Korea has reported large speculative/duplicate power notices. Require construction, permit, owner, or operator corroboration.
- **Building use is inconsistent.** Post-2019 "데이터센터" under 방송통신시설 helps new builds, but legacy DCs can appear as office, research, factory, or education uses.
- **MOU inflation.** Provincial AI datacenter announcements can cite KRW trillions and future MW before land/power/permit are secured.
- **Cloud regions hide physical sites.** Do not infer addresses from latency/AZ codes.
- **Capacity units vary.** Record source units verbatim: MW/MVA, racks (랙/상면), servers, gross floor area, storage EB, or GPU count. Distinguish IT load from utility supply capacity.

---

## 9. Quick-Start Sweep

1. Seed table from kt cloud official DC list, NAVER GAK Chuncheon/Sejong, Kakao Ansan, LG CNS centers, SKB centers, Azure Seoul/Busan, AWS Seoul, Google Cloud Seoul.
2. For each seed, search Seumteo/Building HUB by address/operator/project name; record building use and approval status.
3. Run `site:{local-gov}.go.kr 데이터센터 건축위원회` for the host district and neighboring districts.
4. Run MOTIE/KEPCO queries for power constraints and `전력계통영향평가`.
5. Add KDCC members and reports as operator backlog, then repeat division-by-division for the 229 시/군/구 list.
