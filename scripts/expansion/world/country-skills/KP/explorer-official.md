# KP Explorer Official - Datacenter Enumeration, Democratic People's Republic of Korea

Date verified: 2026-08-12. Country: **KP - Korea, Democratic People's Republic of (North Korea)**. Angle: official/regulatory/government sources for identifying state IT centers, government hosting infrastructure (Kwangmyong intranet / Naenara), telco core facilities, semiconductor/electronics plants, and sanctions documentation of the state IT apparatus.

Verifiability warning (read first): KP is a closed state. There is no public licensing authority, no public facility registry, no independent domestic press, and no operator disclosure. For this country, "official" evidence means (a) international sanctions documentation (UN Security Council resolutions and panel/Monitoring Team reports, US Treasury OFAC designations), and (b) ROK/Korean-government compilations (ROK Ministry of Unification North Korea Information Portal; NIA K2Base research portal). DPRK state media are NOT treated as official evidence - they are propaganda-grade and count at most as C (see `explorer-industry.md` for state-media-relay handling).

Reliability grades:
- **A** = official or primary: UN Security Council resolutions and Panel of Experts reports, UNSCR-2270-based Multilateral Sanctions Monitoring Team (MSMT) official releases, US Treasury OFAC press releases/designations, ROK Ministry of Unification NK Information Portal records, NIA K2Base government research portal records.
- **B** = strong secondary quoting official material: 38 North (Stimson) analysis of MSMT/UN reports, NK News / North Korea Tech citing official documents, ROK major-daily reporting with named official sources.
- **C** = lead only: ROK government compilations without primary linkage, state-media-relayed summaries, aggregator/secondary pages.
- **U** = unverified: single weak source, wiki claims, video evidence, in-country single-source claims; re-check before grading up.

Rule: an entry's grade covers only the fact actually supported. An OFAC designation (A) proves the entity's sanctions status and stated function at designation time, NOT current physical operation. UNSCR text (A) proves the resolution's obligations, NOT the current state of Kaesong-area facilities. Sanctions documents are the closest thing KP has to a facility census; keep every operational claim flagged with its true status.

---

## 0. Structure Facts

### 0.1 Administrative divisions (world-manifest model)

KP's subnational model in `world-manifest.jsonl` is **capital city/province/special city/metropolitan city** with exactly 13 divisions: Pyongyang, South Pyongan, North Pyongan, Chagang, South Hwanghae, North Hwanghae, Kangwon, South Hamgyong, North Hamgyong, Ryanggang, Rason, Nampo, Kaesong. This matches the manifest model: **1 capital city (Pyongyang) + 9 provinces + 1 metropolitan city (Nampo) + 2 special cities (Rason, Kaesong) = 13 divisions**. The manifest is the authoritative enumeration model; do not add a second Pyongyang category under metropolitan/special cities.

| Division | Capital / anchor | Official-angle status |
|---|---|---|
| Pyongyang | Pyongyang (capital city) | Only credible IT cluster: KCC (OFAC-designated), Naenara/Kwangmyong intranet operator, telco cores; official sources: OFAC sm0099, NIA K2Base, Japan MOFA/MSMT |
| South Pyongan | Pyongsong | No official-angle source; Mirae Wi-Fi coverage only (industry file) |
| North Pyongan | Sinuiju | No official-angle source; border-surveillance claim only (U, industry file) |
| Chagang | Kanggye | Negative - no open-source evidence of any IT/datacenter facility (industry file, searched 2026-08-12) |
| South Hwanghae | Haeju | Official-angle source: ROK MOU portal lists Haeju Semiconductor Factory (computing-hardware plant, NOT a datacenter) |
| North Hwanghae | Sariwon | No official-angle source; app-level IT only (industry file) |
| Kangwon | Wonsan | No official-angle source; local cyber-actor reports only (industry file) |
| South Hamgyong | Hamhung | Official-angle source: ROK MOU portal - Hamhung Computer Technology University (IT education) |
| North Hamgyong | Chongjin | No official-angle source; state-media claim of provincial Electronic Affairs Research Institute (C, industry file) |
| Ryanggang | Hyesan | No official-angle source; mine-automation computing only (industry file) |
| Rason | Rason (special city) | No official-angle source; Sunnet 2G history + Kang Song coverage (industry file) |
| Nampo | Nampo (metropolitan city) | No official-angle source; Mirae Wi-Fi coverage only (industry file) |
| Kaesong | Kaesong (special city) | Official-angle source: UNSCR 2270 (sanctions/closure framework for Kaesong Industrial Complex) |

Korean/Chinese names for search recall: 평양 (Pyongyang); 평안남도 (South Pyongan); 평안북도 (North Pyongan); 자강도 (Chagang); 황해남도 (South Hwanghae); 황해북도 (North Hwanghae); 강원도 (Kangwon); 함경남도 (South Hamgyong); 함경북도 (North Hamgyong); 량강도/양강도 (Ryanggang); 라선 (Rason); 남포 (Nampo); 개성 (Kaesong). Administrative verification is not possible against a DPRK government source; use the ROK Ministry of Unification portal (below) as the canonical administrative reference.

### 0.2 Registries: what exists and what does not

- **No public national datacenter registry.** No DPRK ministry, regulator, or operator publishes facility information accessible from outside.
- **No construction-permit or EIA search.** DPRK domestic planning/EIA records are not publicly accessible; there is no equivalent of REMA/City permits.
- The closest things to a census for KP are: (1) UN Panel of Experts reports on DPRK sanctions; (2) MSMT 2nd report (released 2025-10-22); (3) US OFAC designations of state IT entities; (4) ROK Ministry of Unification NK Information Portal ICT-industry overview (updated 2023-07); (5) NIA K2Base (Korean government research portal) records on the Kwangmyong intranet and .kp domain.
- **Cloud-region official lists are negative evidence** for hyperscale facilities (section 3).

### 0.3 Legal and regulatory basis

- UN sanctions regime on the DPRK: UNSCR 1718 (2006) and successors, incl. UNSCR 2270 (2016). Official text: https://main.un.org/securitycouncil/en/s/res/2270-(2016) . UNSCR 2270 required member states to close joint ventures/cooperative entities with designated DPRK entities, freeze DPRK-designated assets, and (per ROK action) close the Kaesong Industrial Complex (Feb 2016).
- Multilateral Sanctions Monitoring Team (MSMT): mechanism established under UNSCR 2270 para. 28 to monitor sanctions on DPRK cyber activities, WMD, and IT-worker deployments. Japan MOFA official release of the 2nd MSMT report (2025-10-22): https://www.mofa.go.jp/press/release/pressite_000001_01758.html . MSMT findings ($3,500-$10,000/month per DPRK IT worker; $350-800M/yr aggregate estimates) are the primary official quantification of the state IT apparatus.
- US Treasury OFAC designations: e.g., Korea Computer Center (KCC) designated 2017-06-01 as the state-run IT R&D center (HQ Pyongyang), developer of Red Star OS, with reported overseas offices: https://home.treasury.gov/news/press-releases/sm0099 . Designations under Executive Orders 13382/13687/13722 are A-grade primary evidence of entity existence/function at designation time.
- DPRK domestic ICT law: not publicly accessible. DPRK institutional claims (Ministry of Information Industry per K2Base; State Affairs Commission Bureau 95 per Daily NK - in-country claim, C) are context only and must not be cited as legal authority.
- ROK government compilations: Ministry of Unification NK Information Portal (https://nkinfo.unikorea.go.kr/) - systematic government compilation of DPRK industry data (ICT overview updated 2023-07); NIA K2Base (https://www.k2base.re.kr/) - Korean government research portal holding DPRK telecom/intranet records.

---

## 1. Search Vocabulary

English (best recall): data center, data centre, datacenter, server room, server farm, hosting, colocation, cloud, digital infrastructure, intranet, Kwangmyong, Naenara, internet exchange, fibre, point of presence, core network, base station, informatization, electronic affairs research institute, semiconductor plant, IT workers, sanctions, designation.

Korean (needed for ROK/government-portal recall): 데이터센터 (data center), 서버실 (server room), 정보통신 (information/telecom, ICT), 전자업무연구소 (electronic affairs research institute), 국가자료통신망 (state data communications network), 내각 (cabinet), 평양정보센터 (Pyongyang Informatics Center), 한국컴퓨터센터 (Korea Computer Center), 광명 (Kwangmyong), 나진 (Naenara), 해주반도체공장 (Haeju Semiconductor Factory), 함흥컴퓨터기술대학 (Hamhung Computer Technology University), 정보화 (informatization).

Lifecycle verbs to capture: 지정/designated (sanctions), 제재 (sanctions), 폐쇄/closed (KIC), 설립/founded (institutions), 확충/expanded (networks), 착공/construction (state-media claims - treat as C).

---

## 2. Official And Regulatory Pipeline

### 2.1 UN Security Council sanctions regime

- UNSCR 2270 official text (A): https://main.un.org/securitycouncil/en/s/res/2270-(2016) - the legal anchor for the Kaesong closure and asset freezes; dates: 2016-03-02.
- UN Panel of Experts reports on DPRK (published via https://www.un.org/securitycouncil/sanctions/1718/panel_experts/reports ) - recurring A-grade census of DPRK cyber/IT infrastructure and IT-worker networks. Check each new report for named IT entities and locations.

Queries:
```text
site:un.org securitycouncil 1718 panel experts DPRK IT workers OR cyber OR "data center"
site:un.org "S/RES/2270" Korea
"UN Panel of Experts" DPRK IT workers OR Korea Computer Center OR Kwangmyong
```

### 2.2 US Treasury OFAC designations

- KCC designation (2017-06-01): https://home.treasury.gov/news/press-releases/sm0099 (A). Also covers state IT entities generally - monitor https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions and the DPRK sanctions list: https://sanctionssearch.ofac.treas.gov/ .
- Designations name entities and stated functions (e.g., "state-run IT R&D center, developer of Red Star OS, HQ Pyongyang") - A for entity/function, but rarely give street-level facility data; do not convert designation to physical-facility status.

Queries:
```text
site:home.treasury.gov press-releases Korea Computer Center OR "DPRK" IT OR cyber
treasury sanctions DPRK "Korea Computer Center" OR "Korea Expo" OR "IT"
sanctionssearch.ofac.treas.gov DPRK IT OR Korea
```

### 2.3 Multilateral Sanctions Monitoring Team (MSMT) / Japan MOFA

- Japan MOFA official release of MSMT 2nd report (2025-10-22, A): https://www.mofa.go.jp/press/release/pressite_000001_01758.html . MSMT tracks DPRK cyber operations and IT-worker deployment (sanctions-evasion angle).
- 38 North's assessment of the MSMT report (2025-12, B) provides read-across to IT-worker economics ($3,500-$10,000/month) - see industry file for the URL.

### 2.4 ROK government compilations

- ROK Ministry of Unification - North Korea Information Portal (정보통신/ICT industry overview, updated 2023-07): https://nkinfo.unikorea.go.kr/nkp/pge/view.do?menuId=MENU_49 . Verified records: Haeju Semiconductor Factory (South Hwanghae, C) and Hamhung Computer Technology University (South Hamgyong, B; corroborated by multiple sources). Systematic first stop for DPRK industry/entity facts.
- NIA K2Base (Korean government research portal): https://www.k2base.re.kr/ - verified record: Kwangmyong fiber network expanded Pyongyang-wide 2004, to Hamhung/Chongjin 2005; intranet under Ministry of Information Industry (C-grade lead, KO-language).

Queries:
```text
site:nkinfo.unikorea.go.kr 정보통신 OR ICT OR 데이터센터 OR 반도체
site:k2base.re.kr 광명 OR 정보통신 OR 컴퓨터 OR 도메인
"정부통신망" OR "국가자료통신망" 북한
```

### 2.5 Explicit exclusion: DPRK state media are not official evidence

DPRK state media (KCNA, Rodong Sinmun, Chosun Today, Arirang Meare) are propaganda outlets. Their ICT claims (e.g., "electronic affairs research institute built in Chongjin") are relayed by NK Economy/Tongil News and graded C at most until corroborated by satellite analysis, defector reporting, or sanctions documentation. Do not accept a DPRK state-media claim as A/B on its own.

**Low-exposure handling:** Sanctions, ROK-government compilations, and state-media relays are used only for entity/function/context discovery. Do not publish or infer precise coordinates, security-sensitive layouts, access controls, personnel identities, or operational vulnerabilities. A named city or district is the maximum location granularity unless a public source explicitly provides a non-sensitive facility context; physical-facility status remains separate from entity-level sanctions evidence.

---

## 3. Cloud, Edge, And Interconnection Signals (negative evidence where applicable)

| Signal | Source | KP interpretation |
|---|---|---|
| AWS regions | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No KP region; negative evidence for local hyperscale. |
| Azure regions | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No KP region. |
| Google Cloud locations | https://cloud.google.com/about/locations | No KP region. |
| Oracle OCI regions | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No KP region. |
| IXP | none found | No public KP internet exchange point; OSINT indicates internet egress via China (and Russia per recent reporting). No IXP evidence. |
| .kp registry | KCC-operated per OSINT (Wikipedia); no public registry/whois data | Registry infrastructure claim, U; do not treat as facility evidence. |
| International connectivity | Landlocked; cross-border fibre to China/Russia; no submarine landing | Connectivity context only; never count as datacenter capacity. |
| Kwangmyong intranet | K2Base (C), North Korea Tech (B), Wikipedia (C) | State intranet (early 2000s), operated through Naenara Information Center; domestic .kp sites. Government-hosting context - the closest thing to "government cloud" in KP; NOT a commercial datacenter. |
| Foreign LEO/satellite service | none | No evidence of Starlink or similar operating in KP; sanctions preclude it. |

---

## 4. Facility And Project Seed List (official angle, evidence status as of 2026-08)

| Candidate | Status | Grade | Location handling | Why it matters / evidence |
|---|---|---|---|---|
| Korea Computer Center (KCC) | OFAC-designated state IT R&D center | A for designation; C for facility details | Pyongyang (Mangyongdae District; CSIS romanizes Sunlae-Dong, Mangyong District - same district, different romanization) | OFAC sm0099 designated KCC 2017-06-01 as state-run IT R&D center, developer of Red Star OS, HQ Pyongyang, reported overseas offices (Germany/China/Syria/India/Middle East): https://home.treasury.gov/news/press-releases/sm0099 ; KCC supports DPRK IT contract workers abroad (CSIS, B). Anchor entity of the Pyongyang IT cluster. |
| Kwangmyong intranet / Naenara Information Center | Government hosting platform (operational per OSINT) | C (K2Base); B (North Korea Tech long-running OSINT tracking) | Pyongyang, national reach | K2Base: Kwangmyong fiber expanded Pyongyang-wide 2004, Hamhung/Chongjin 2005, under Ministry of Information Industry; Wikipedia: intranet opened early 2000s, domestic sites on .kp, operated through Naenara Information Center. State intranet = government hosting context, not a commercial DC. |
| MSMT 2nd report / IT-worker apparatus | Sanctions-monitoring documentation | A for report; U for any facility-level inference | Pyongyang-centric state apparatus | Japan MOFA official release (2025-10-22) of MSMT 2nd report: https://www.mofa.go.jp/press/release/pressite_000001_01758.html ; 38 North analysis (2025-12): IT workers earn roughly $3,500-$10,000/month; CSIS (2024): $350-800M/yr. Official quantification of the state IT apparatus; does not name physical facilities. |
| Haeju Semiconductor Factory (South Hwanghae) | Computing-hardware manufacturing plant listed in ROK gov compilation | C | Haeju | ROK MOU portal (2023-07) lists 해주반도체공장 among DPRK semiconductor plants (with Pyongyang IC plant, Tanchon plant). Manufacturing facility, NOT a datacenter; no datacenter evidence in South Hwanghae. |
| Hamhung Computer Technology University (South Hamgyong) | IT-education institution (real, corroborated) | B | Hamhung | ROK MOU portal (2023-07): established 2001 as one of two DPRK computer-technology universities (with Pyongyang); with Pyongsong Science Univ. and ~10 central universities graduates 5,000-10,000 IT workers/yr. Education evidence, not a facility. |
| Kaesong Industrial Complex (KIC) telecom/data infrastructure | Closed (Feb 2016) | A for UNSCR 2270 framework; B for 2006 KT build (industry file); U for current status | Kaesong | UNSCR 2270 (2016-03-02) official text frames the closure and asset freezes: https://main.un.org/securitycouncil/en/s/res/2270-(2016) ; KT-built ~3,000-pyong (~9,900 m²) communications center inside KIC (Dong-A Ilbo 2006-02-07, B - industry file); KIC closed since Feb 2016, renewed activity per 38 North satellite analysis 2024 (B - industry file). |

---

## 5. Per-Division Enumeration Approach (official angle)

Run every enumeration cycle across all 13 divisions; record negatives as `no_projects: true` where a division genuinely has no activity. The official angle adds sanctions/compilation framing to 4 divisions; the other 9 divisions are carried entirely by the industry file (press/OSINT). Expect a heavily Pyongyang-centred picture with no commercial market anywhere.

1. **Pyongyang**: the ONLY credible IT cluster. Official-angle sources: OFAC KCC designation, Japan MOFA/MSMT release, NIA K2Base Kwangmyong records. Everything else (Koryolink/Sunnet/Mirae, Samtaesong hardware) lives in the industry file. Expected official yield: entity-level records (KCC), sanctions context (MSMT), intranet/government-hosting context (Kwangmyong).
2. **South Pyongan / Nampo / North Pyongan / Chagang / Kangwon / North Hwanghae / Ryanggang / Rason**: no official-angle sources. Official searches return nothing; all leads (Mirae Wi-Fi, Sunnet 2G, Kang Song, mine automation, surveillance systems, 5G claim) are C/U in the industry file. Chagang = negative (no_projects).
3. **South Hwanghae**: one official compilation record - Haeju Semiconductor Factory (manufacturing, NOT DC). No datacenter evidence; treat as negative for DC with the plant as computing-hardware context.
4. **South Hamgyong**: Hamhung Computer Technology University (official compilation, B). Education context; negative for DC facilities.
5. **North Hamgyong**: no official-angle source; state-media claim of provincial Electronic Affairs Research Institute (C, industry file). Official searches negative.
6. **Kaesong**: UNSCR 2270 framework (A). KIC closed 2016; no operating facility. KT communications center is historical (industry file, B for 2006 build).

Copy/paste query block (official angle; keep domain-restricted queries separate):
```text
site:un.org 1718 panel experts Korea IT OR cyber OR "data center"
site:home.treasury.gov DPRK OR "Korea Computer Center" OR IT designation
site:mofa.go.jp MSMT OR DPRK OR North Korea
site:nkinfo.unikorea.go.kr 정보통신 OR 반도체 OR 컴퓨터
site:k2base.re.kr 광명 OR 정보통신 OR 컴퓨터
"North Korea" OR "DPRK" "data center" sanctions OR OFAC OR UNSCR OR MSMT
"Korea Computer Center" designation OR OFAC OR sanctions
```

---

## 6. Counting, Grading, And De-Dup Rules (official angle)

- A facility exists only when a source names infrastructure AND location with enough specificity to distinguish a physical site. Sanctions designations name entities and stated functions, rarely street-level addresses - keep entity-level records separate from facility-level records.
- Keep `facility_type` precise: `state_it_center`, `government_hosting_intranet`, `telco_core`, `semiconductor_factory`, `university_computing`, `sanctions_monitoring_context`, `planned_or_closed_facility`, `lead_only`, `negative`.
- Keep status precise: `operational` (only where independently corroborated), `designated` (sanctions), `closed` (KIC), `historical` (KT center 2007), `unverified`, `negative`.
- KCC de-dup: OFAC (2017), Korea IT Times (Mangyongdae District) and CSIS (Sunlae-Dong, Mangyong District) describe the same district under different romanizations - ONE entity, do not multiply. KCC, Naenara Information Center and the Kwangmyong intranet operator are related state entities but distinct records.
- Mirae Wi-Fi appears in Daily NK and 38 North (2022) - two sources corroborating ONE network, not two facilities.
- Capacity fields (MW/racks/floor area) stay null everywhere: no official source states capacity for any KP facility. The only floor-area figure anywhere (KT KIC ~9,900 m²) comes from a 2006 press report (B, historical, industry file).
- Negative searches: state-media "informatization" claims, university computer rooms, mine automation, forest-fire surveillance systems, and semiconductor manufacturing are NOT datacenters unless a source describes hosting/colo/compute infrastructure with a named operator and location.
- The MSMT/UN/OFAC apparatus documents the state IT sector's existence and scale; it does not by itself prove any physical datacenter. Never convert sanctions evidence into an operational-facility record.

---

## 7. Source Priority Checklist (official angle)

1. UN Security Council resolutions (1718/2270 and successors) and Panel of Experts reports.
2. MSMT official reports (released via Japan MOFA / UN channels) - 2nd report 2025-10-22.
3. US Treasury OFAC designations and sanctions list (KCC 2017-06-01 and successors).
4. ROK Ministry of Unification NK Information Portal (industry/entity compilations).
5. NIA K2Base research portal (DPRK telecom/intranet records).
6. 38 North / CSIS analyses of official reports (B-grade corroboration of MSMT/UN material).
7. Trade press quoting official documents (e.g., ROK dailies on KIC closure) as B-grade corroboration.
8. DPRK state media via relays (NK Economy, Tongil News) as C-only, never A/B.

---

## 8. Update / Re-Check Cadence

- **Quarterly**: UN Panel of Experts reports; MSMT releases; OFAC DPRK sanctions actions (https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions).
- **Semi-annual**: ROK MOU NK Information Portal ICT overview for updated entity/industry entries.
- **Annual**: NIA K2Base DPRK telecom/intranet records; re-verify all U/C facility claims (KCC facility details, Kwangmyong hosting specifics).
- **Event-driven**: new UNSCR, new OFAC designation, MSMT/UN panel naming a physical facility, or any report of a DPRK "data center" - would be the single biggest change; verify against sanctions documents before recording.

## 9. Verified Source Anchors (as of 2026-08)

- UNSCR 2270 official text: https://main.un.org/securitycouncil/en/s/res/2270-(2016) ; UN 1718 Committee/Panel reports: https://www.un.org/securitycouncil/sanctions/1718/panel_experts/reports
- US Treasury OFAC - KCC designation sm0099 (2017-06-01): https://home.treasury.gov/news/press-releases/sm0099 ; OFAC sanctions search: https://sanctionssearch.ofac.treas.gov/ ; recent actions: https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions
- Japan MOFA - MSMT 2nd report release (2025-10-22): https://www.mofa.go.jp/press/release/pressite_000001_01758.html
- ROK Ministry of Unification - NK Information Portal (정보통신/ICT overview, 2023-07): https://nkinfo.unikorea.go.kr/nkp/pge/view.do?menuId=MENU_49
- NIA K2Base (DPRK tech research portal): https://www.k2base.re.kr/ ; Kwangmyong/.kp record: https://www.k2base.re.kr/north/tech/pds12ANDpds13/view.do?recordCountPerPage=10&pageUnit=10&pageSize=10&pageIndex=18&nttId=5383&nttId2=69979&menuNo=&viewType=&schScale=IN2_TITLE/CONTENT/FILE&searchCont=
- Hyperscaler region lists (negative evidence): AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; GCP https://cloud.google.com/about/locations ; OCI https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Final note: KP has no commercial datacenter market and no official facility registry. The official-angle yield is entity- and sanctions-level: KCC (designated), Kwangmyong/Naenara (state intranet), MSMT/UN documentation of the IT-worker apparatus, one semiconductor plant listing (Haeju), one IT-university record (Hamhung), and the Kaesong closure framework. Everything else is C/U and lives in the industry file. Do not upgrade any KP record on the strength of state media or aggregator-style claims alone.

## Review record

- Date: 2026-08-12
- Reviewer: gpt5.6-luna
- Conclusion: **REVISED**
- Key changes: corrected the manifest arithmetic to 1 capital + 9 provinces + 1 metropolitan city + 2 special cities = 13 divisions; retained all-division enumeration and sanctions/ROK-government/state-media source separation; added a low-exposure guard limiting outputs to city/province context and prohibiting precise coordinates, security details, or targeting inferences.
