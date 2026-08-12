# KP Explorer Industry - North Korean Press, OSINT, Think-Tank, And Media Discovery

Date verified: 2026-08-12. Scope: DPRK datacenter/IT-infrastructure enumeration from local and regional press, defector-run outlets, specialist North Korea tech media, think-tank OSINT (38 North/Stimson, CSIS), satellite geodata, wikis/blogs/video, and division-level search patterns. Pair with `explorer-official.md`; UN/MSMT/OFAC/ROK-government documents decide final facility status where conflicts exist.

Verifiability warning: KP has no independent domestic press, no operator disclosure, no public registries, and no foreign operators. External verifiability is near zero. There is **no confirmed commercial datacenter anywhere in KP**; the "industry" is the state IT apparatus plus its supporting networks. State-media claims are propaganda-grade (C at most until independently corroborated); wiki/blog/video claims are U.

Reliability grades:
- **A** = primary/operator/official/donor: in practice nearly absent for KP (no operator pages, no official DPRK disclosures usable from outside). Reserved for cases where an official document is quoted directly by a strong source.
- **B** = strong secondary OSINT: 38 North (Stimson) with satellite analysis, NK News, Daily NK (English), North Korea Tech, Dong-A Ilbo quoting named officials, CSIS reports with cited primary material.
- **C** = lead only: state-media relays (NK Economy, Tongil News relaying KCNA/Chosun Today/Rodong Sinmun), Korea IT Times, Sand Times, ROK media, Naver blog, Wikipedia summaries.
- **U** = unverified: NamuWiki, YouTube field video, single in-country source claims, aggregator-style claims; re-check before grading up. `no_projects` negative records are recorded as U with a negative note and search date.

---

## 0. KP Industry Frame

- No commercial datacenter market exists. All IT infrastructure is state-run: Korea Computer Center (KCC), Naenara Information Center (Kwangmyong intranet operator), provincial Electronic Affairs Research Institutes (전자업무연구소), state universities (Hamhung Computer Technology University), and telco operators (KPTC-led Koryolink JV with Orascom; Sunnet/Loxley Pacific 2002; Kang Song/Byol 2015+). For low-exposure review, use city/province labels only; do not turn sanctions or OSINT leads into precise facility coordinates, security details, or targeting information.
- The Pyongyang cluster is the only credible IT concentration: KCC HQ (Mangyongdae District), Kwangmyong intranet operations, mobile cores, and the densest base-station coverage in the country (1000+ cells mapped by satellite, densest around Pyongyang, per 38 North 2022).
- Networks are the real enumeration surface: Koryolink 3G (launched Dec 2008, Pyongyang-first), Sunnet 2G (Nov 2002, Rason + Pyongyang; suspended May 2004), Kang Song (~3.0M subs) vs Koryolink (~1.7M subs) as of 2025, Mirae Wi-Fi intranet (>=33 Mbps, 2017; Pyongyang + Pyongsong + Nampo). None of these is a datacenter; all are network/edge context.
- Sanctions are the frame: OFAC-designated KCC; MSMT 2nd report (2025-10-22) and UN Panel of Experts document the IT-worker export apparatus ($3,500-$10,000/month per worker; $350-800M/yr aggregate per CSIS 2024). IT-labor export creates overseas "remote IT" presence without any in-country facility record.
- Connectivity: landlocked; internet egress via China (and Russia per recent reporting); Kwangmyong is a closed state intranet, NOT the public internet. No public IXP. No hyperscaler region. No submarine landing.
- Language: English gives the best recall in OSINT; Korean is required for ROK-government portals and state-media relays. Key Korean terms: 정보통신 (ICT), 데이터센터, 서버실, 전자업무연구소, 국가자료통신망, 광명 (Kwangmyong), 나진 (Naenara), 정보화 (informatization).

---

## 1. Local And Regional Press

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Daily NK (English/Korean) | https://www.dailynk.com/english/ ; https://www.dailynk.com/ | Defector-run outlet, strongest in-country-sourced reporting. Verified: Mirae Wi-Fi operation incl. IT dept of Bureau 95, State Affairs Commission (2022-10-04); Wonsan 'smishing' arrests (2026-08-05); Hamhung student illicit-software case (2026-08); Chongjin IT-training surge (2024-07-29). | B for reporting; C for single-source claims |
| NK News | https://www.nknews.org/ | English-language specialist outlet. Verified: 37 universities opened 85 IT/robotics/nano departments (2019-09-03, citing Rodong Sinmun); DPRK websites offline amid web-presence overhaul (2024-01-24, Pro); ROK closure of KIC (2016-02-10). | B; A when quoting official documents |
| Korea Herald | https://www.koreaherald.com/ | ROK English daily. Samtaesong 8 (삼태성) smartphone, Android 11, shown on Korean Central TV (2023-07-13) - evidence of a Pyongyang hardware ecosystem, NOT a datacenter. | U for facility relevance |
| Korea IT Times | https://www.koreaittimes.com/news/articleView.html?idxno=11397 | KCC profile: Mangyongdae District, Pyongyang; operates Naenara Information Center (Kwangmyong intranet operator) and a quality management center. | C |
| Sand Times | https://www.sandtimes.co.kr/news/articleView.html?idxno=1949 | Kang Song ~3.0M vs Koryolink ~1.7M subscribers (2025-08-21); three mobile operators (Koryolink/Kang Song/Byol). Subscriber metrics for Pyongyang-centric networks. | C |
| The Diplomat | https://thediplomat.com/2021/07/north-korea-may-be-using-5g-technology-to-monitor-its-border-with-china/ | Sinuiju border surveillance cameras, '5G technology' claim from a single in-country source (2021-07-15); only tech item found for North Pyongan; NO datacenter evidence. | U |
| Dong-A Ilbo | https://www.donga.com/news/Economy/article/all/20060207/8272742/1 | KT announced a ~3,000-pyong (~9,900 m²) communications center inside the Kaesong Industrial Complex by 2007 for tenant voice/internet services (2006-02-07); real telecom/data-communications facility at Kaesong, complex closed Feb 2016. | B for 2006 build; U for current status |
| Tongil News | http://www.tongilnews.com/news/articleView.html?idxno=104053 | Relays DPRK state media: Hyesan Youth Mine (Ryanggang) computer control systems across production (2013-09-08) - mining automation, NOT a datacenter. | C (state-media relay) |
| NK Economy | http://www.nkeconomy.com/ | Relays DPRK state media: North Hwanghae forest-fire surveillance system w/ provincial electronic-affairs research institute (2019-09-29); North Hamgyong Province Electronic Affairs Research Institute built in Chongjin (2022-11-10, Kim Jong-un reviewed plans) - real provincial IT facility per state media, externally unverifiable. | C (state-media relay) |

Queries:
```text
site:dailynk.com North Korea (internet OR IT OR 정보통신 OR Mirae OR Wi-Fi OR computer)
site:nknews.org North Korea (internet OR telecom OR IT OR "data center" OR Kwangmyong)
site:koreaherald.com North Korea (smartphone OR IT OR internet)
site:koreaittimes.com "North Korea" OR "Korea Computer Center"
"North Korea" OR "DPRK" ("data center" OR server OR datacenter) 2025 OR 2026
```

Lifecycle verbs to capture: 설립/founded, 착공/construction, 준공/completed, 개통/launched (networks), 폐쇄/closed, 중단/suspended, 검토/planned, 확충/expanded.

---

## 2. Think Tanks And OSINT

| Source | URL / route | Use | Grade |
|---|---|---|---|
| 38 North (Stimson Center) | https://www.38north.org/ | Satellite and field analysis. Verified: twenty years of mobile communications (2022-11-15) - Koryolink/Sunnet/Mirae history, 1000+ base stations via satellite, densest around Pyongyang; KIC satellite imagery - renewed activity 2021-2023 incl. electronics/telecom sectors (2024-09-04); assessment of MSMT IT-worker report (2025-12) - $3,500-$10,000/month per worker. | B |
| 38 North DPRK Digital Atlas | https://38northdigitalatlas.org/ | Open-source geospatial dataset incl. telecom infrastructure; recommended for satellite-based enumeration of base stations/facilities nationwide and in the Rason SEZ. | B |
| CSIS | https://www.csis.org/ ; Cha report PDF: http://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/151216_Cha_NorthKoreasCyberOperations_Web.pdf | North Korea's Cyber Operations (2015-12-16): KCC located in Sunlae-Dong, Mangyong District, Pyongyang (est. Oct 1990); Pyongyang Informatics Center listed among state IT institutions; KCC supports DPRK IT contract workers abroad. Responding to the DPRK IT Worker Threat (2024): $350-800M/yr IT-labor revenue; Pyongyang institutions coordinate IT labor export. | B |
| North Korea Tech (Martyn Williams) | https://www.northkoreatech.org/tag/kwangmyong/ | Long-running OSINT tracking of Kwangmyong intranet upgrades (search/translation functions) and NK digital infrastructure. | B |
| Wikipedia | KCC: https://en.wikipedia.org/wiki/Korea_Computer_Center ; Kwangmyong: https://en.wikipedia.org/wiki/Kwangmyong_(network) | KCC founded 24 Oct 1990 as government IT research center (HQ Pyongyang); Kwangmyong opened early 2000s, domestic sites on .kp, operated through Naenara Information Center; no public datacenter specifications. Aggregate/secondary. | C |
| NamuWiki | https://namu.wiki/w/고려링크 | Claims Koryolink serves nationwide WCDMA, mainly Pyongyang/inland; full 3G data only for approved officials/foreigners. Unverifiable wiki source. | U |
| Naver blog (seadjk) | https://blog.naver.com/seadjk/222035658593 | Profile of Hamhung Computer Technology University (함흥컴퓨터기술대학): founded 1985 as 함흥전자계산기단과대학; trains computer/applied-computer engineers. Personal blog, low authority. | C |
| YouTube field video | https://www.youtube.com/watch?v=QiODmdA03KY | Field video showing Kang Song network available in Rason (KANGSONG NET). Unverifiable video. | U |

Queries:
```text
site:38north.org North Korea (telecom OR Kwangmyong OR Koryolink OR "base station" OR KIC)
site:csis.org DPRK OR "North Korea" IT workers OR cyber operations
site:northkoreatech.org Kwangmyong OR telecom OR internet OR "data"
site:en.wikipedia.org North Korea (telecommunications OR internet OR computer)
38northdigitalatlas.org DPRK telecom base stations OR facilities
```

---

## 3. State IT Entities And "Operators"

| Entity | Primary or lead URL | Industry signal | Grade and handling |
|---|---|---|---|
| Korea Computer Center (KCC) | OFAC sm0099; CSIS Cha; Korea IT Times; Wikipedia | State IT R&D center, est. Oct 1990, HQ Pyongyang (Mangyongdae District); OFAC-designated 2017; developer of Red Star OS; operates Naenara/Kwangmyong intranet ecosystem; overseas offices reported. | A designation; C for facility details; U for any capacity figure |
| KPTC (Korea Posts and Telecommunications Corp) | 38 North 2022 | State telco; 25% owner of Koryolink JV with Orascom (75%). | B for JV facts |
| Koryolink (CHEO Technology JV) | 38 North 2022; NamuWiki; Sand Times 2025 | 3G launched Dec 2008, Pyongyang coverage first; ~1.7M subscribers 2025. | B for launch/coverage; U for wiki specifics |
| Sunnet (Loxley Pacific, Thailand) | 38 North 2022 | 2G network switched on Nov 2002 in Rason AND Pyongyang (first mobile deployment in Rason); suspended May 2004. | B |
| Kang Song / Byol | Sand Times 2025; YouTube Rason video | Newer operators; Kang Song ~3.0M subscribers (2025); Kang Song coverage in Rason per field video. | C/U |
| Naenara Information Center | Korea IT Times; Wikipedia; North Korea Tech | Operates the Kwangmyong intranet and Naenara portal; state web presence. | C |
| Pyongyang Informatics Center (PIC) | CSIS Cha 2015 | Listed among state IT institutions; coordinates IT-related activities. | B (named in CSIS); C for details |
| Provincial Electronic Affairs Research Institutes | NK Economy (state-media relays) | e.g., North Hamgyong Province Electronic Affairs Research Institute (Chongjin, 2022, newly built); North Hwanghae institute technicians deployed for surveillance systems (2019). Provincial state IT facilities; state-media claim only. | C |
| Hamhung Computer Technology University | ROK MOU portal (B); Naver blog (C); NK News 2019 | One of two DPRK computer-technology universities (with Pyongyang); est. 1985 per blog vs 2001 per ROK compilation (sources differ - flag); graduates IT workers into the sector. | B/C |
| Bureau 95 (State Affairs Commission) | Daily NK 2022-10-04 | In-country claim: its IT department handles Mirae Wi-Fi R&D. | C |
| KT (ROK) telecom center at KIC | Dong-A Ilbo 2006-02-07 | ~3,000-pyong (~9,900 m²) communications center built inside KIC by 2007 for tenant voice/internet; historical (KIC closed Feb 2016). | B for 2006 build; U for current status |

Operator queries:
```text
"Korea Computer Center" North Korea (Kwangmyong OR Naenara OR Red Star)
"Koryolink" OR "Kang Song" OR "Byol" North Korea subscribers OR launch OR network
"Loxley Pacific" OR Sunnet North Korea 2G Rason
"electronic affairs research institute" OR 전자업무연구소 North Korea
"Hamhung Computer Technology University" OR 함흥컴퓨터기술대학
```

---

## 4. Interconnection, Networks, And Negative Evidence

| Channel | URL | Use | Grade |
|---|---|---|---|
| Kwangmyong intranet | K2Base (official file); North Korea Tech; Wikipedia | State intranet (early 2000s), operated via Naenara; domestic .kp sites; fiber expanded Pyongyang-wide 2004, Hamhung/Chongjin 2005 (K2Base); OSINT tracks upgrades. Government hosting context, NOT a commercial DC. | C/B |
| Mirae Wi-Fi | Daily NK 2022-10-04; 38 North 2022-11-15 | Wireless intranet (>=33 Mbps) set up in Pyongyang 2017; works well in Pyongyang, Pyongsong, Nampo; SIM registration at service centers/post offices; Bureau 95 handles R&D. | B |
| Mobile networks | 38 North 2022; Sand Times 2025 | Koryolink 3G (2008), Sunnet 2G (2002-2004), Kang Song/Byol; 1000+ base stations mapped via satellite, densest around Pyongyang. Telco cores are network context only. | B |
| .kp registry | Wikipedia; OSINT | KCC-operated claim; no public whois/registry data. | U |
| IXP | none found | No public KP internet exchange; egress via China (and Russia per recent reporting). | U/negative |
| Submarine cables | geography (landlocked) | No landing; cross-border fibre to China/Russia only. | A negative (geography) |
| Hyperscaler regions | AWS/Azure/GCP/OCI official region pages (official file section 3) | No KP region; negative evidence for any local hyperscale. | A negative |
| 38 North DPRK Digital Atlas | https://38northdigitalatlas.org/ | Satellite-based enumeration of base stations/infrastructure (incl. Rason SEZ). | B |

Aggregator/IXP queries:
```text
38northdigitalatlas.org DPRK telecom OR "base station"
"Kwangmyong" intranet North Korea upgrades OR expansion
"North Korea" internet exchange OR IXP OR egress China OR Russia
"DPRK" "data center" OR datacenter OR "server farm" (site:38north.org OR site:nknews.org OR site:northkoreatech.org)
```

---

## 5. Search Templates

### 5.1 English templates

```text
"North Korea" OR "DPRK" ("data center" OR datacenter OR "server room" OR "server farm" OR hosting OR colocation)
"North Korea" (Kwangmyong OR Naenara OR KCC OR "Korea Computer Center") (intranet OR server OR hosting OR IT)
"North Korea" ("electronic affairs research institute" OR 전자업무연구소 OR informatization) facility
"DPRK" IT workers (MSMT OR OFAC OR sanctions OR "remote IT") 2024 OR 2025 OR 2026
"North Korea" semiconductor OR "computer technology university" OR "IT training"
"Pyongyang" OR "Hamhung" OR "Chongjin" OR "Haeju" ("data center" OR datacenter OR "server room" OR IT facility)
filetype:pdf "North Korea" OR DPRK ("data center" OR IT infrastructure OR telecom)
```

### 5.2 Korean templates (ROK portal + state-media relay recall)

```text
북한 데이터센터 OR 서버실 OR 정보통신 OR 전자업무연구소
평양 정보센터 OR 한국컴퓨터센터 OR 국가자료통신망
광명망 OR 광명 네트워크 OR 나진 정보센터 확충
해주반도체공장 OR 함흥컴퓨터기술대학 OR 청진 전자업무연구소
북한 IT인력 OR 정보통신 인력 파견 OR 해외 IT
```

### 5.3 Low-yield checks (use only as recall aids; verify positives in EN/KO)

```text
조선 데이터센터 OR 서버
량강도 OR 자강도 컴퓨터 OR 정보화
```

---

## 6. Division Enumeration (13 divisions)

| Division | Seeds and expectations | Sources in this file |
|---|---|---|
| Pyongyang | The only credible cluster: KCC (Mangyongdae District), Naenara/Kwangmyong intranet, Koryolink 3G core (2008), Sunnet 2G (2002), Mirae Wi-Fi (2017), densest base-station coverage, Samtaesong 8 hardware ecosystem (2023), website-outage campaign (2024), MSMT/CSIS IT-worker economics. Highest yield - but all facility claims remain C/U; no physical datacenter confirmed. | 13 |
| South Pyongan | Pyongsong: Mirae Wi-Fi works well (provincial capital, Daily NK 2022); cellular coverage per 38 North Atlas. No facility; no commercial DC known. | 2 |
| North Pyongan | Sinuiju: '5G surveillance cameras' claim from single in-country source (The Diplomat 2021, U). NO datacenter evidence; effectively negative for facilities. | 1 |
| Chagang | Kanggye: EN+KO searches returned nothing (searched 2026-08-12). Industrial/military province, no public ICT records. Record as `no_projects: true`. | 1 (negative) |
| South Hwanghae | Haeju: Haeju Semiconductor Factory (ROK MOU portal) - manufacturing, NOT DC; no datacenter evidence; treat as negative for DC with plant context. | 1 (negative for DC) |
| North Hwanghae | Sariwon: forest-fire surveillance system with provincial electronic-affairs institute technicians (NK Economy 2019) - app-level IT, NOT DC; treat as U/negative for facilities. | 2 |
| Kangwon | Wonsan: 'smishing' arrests indicate local IT/cyber-capable actors (Daily NK 2026-08); Wonsan universities not IT-focused. No facility; treat as U. | 2 |
| South Hamgyong | Hamhung: Hamhung Computer Technology University (ROK MOU portal B; Naver blog C); national IT-education expansion (NK News 2019); Hamhung student illicit-software case (Daily NK 2026-08). Education/grassroots IT; no DC facility. | 3 |
| North Hamgyong | Chongjin: North Hamgyong Province Electronic Affairs Research Institute newly built (NK Economy 2022, state-media claim, C); IT-training surge (Daily NK 2024-07-29). Real provincial IT facility per state media; externally unverifiable. | 2 |
| Ryanggang | Hyesan: Hyesan Youth Mine computer control systems (Tongil News 2013) - mining automation, NOT DC; treat as U/negative. | 2 |
| Rason | Sunnet 2G switched on Nov 2002 in Rason AND Pyongyang, suspended May 2004 (38 North B); Kang Song available in Rason (YouTube U); 38 North Digital Atlas for SEZ enumeration. No facility; network history only. | 3 |
| Nampo | Mirae Wi-Fi works well in Nampo (Daily NK 2022); cellular coverage per 38 North Atlas. Telecom node on west coast; no commercial DC evidence. | 2 |
| Kaesong | KT ~3,000-pyong communications center inside KIC by 2007 (Dong-A Ilbo 2006, B); KIC closed Feb 2016 (NK News 2016, B); renewed activity 2021-2023 incl. electronics/telecom per 38 North satellite imagery (2024, B). Historical telecom/data facility; closed; no operating DC. | 3 |

Division query block:
```text
"Pyongyang" (KCC OR "Korea Computer Center" OR Naenara OR Kwangmyong OR Koryolink OR Mirae) (IT OR server OR intranet OR "data")
"Pyongsong" OR "South Pyongan" North Korea (Mirae OR Wi-Fi OR telecom OR IT)
"Sinuiju" OR "North Pyongan" North Korea (surveillance OR 5G OR IT OR telecom)
"Chagang" OR "Kanggye" North Korea (computer OR IT OR 정보통신 OR 데이터센터)
"Haeju" OR "South Hwanghae" North Korea (semiconductor OR 반도체 OR IT OR computer)
"Sariwon" OR "North Hwanghae" North Korea (IT OR 전자업무연구소 OR surveillance)
"Wonsan" OR "Kangwon" North Korea (IT OR cyber OR smishing OR computer)
"Hamhung" OR "South Hamgyong" North Korea (computer university OR IT OR 정보통신)
"Chongjin" OR "North Hamgyong" North Korea (전자업무연구소 OR IT OR computer)
"Hyesan" OR "Ryanggang" North Korea (computer OR mine OR IT)
"Rason" North Korea (Sunnet OR Kang Song OR telecom OR "base station")
"Nampo" OR "Nampho" North Korea (Mirae OR Wi-Fi OR telecom OR IT)
"Kaesong" North Korea (KIC OR telecom OR communications center OR IT)
```

Negative-search rule: do not count ICT offices, cybercafes, computer labs, university IT departments, mine automation, forest-fire surveillance, semiconductor factories, or smartphone products unless a source describes hosting/colo/compute infrastructure with a named operator and location.

---

## 7. Grading And Verification Rules

- KP external verifiability is near zero: no independent domestic press, no operator disclosure, no public registries. Assume any DPRK-sourced claim may be propaganda until independently corroborated.
- **A operating facility**: essentially unattainable for KP; no source in this pass names an operating datacenter with location. Do not record one.
- **B operating facility**: strong OSINT (38 North satellite analysis, NK News/Daily NK citing officials or documents) names infrastructure with location. Current B records are networks (Koryolink, Sunnet, Mirae), institutions (Hamhung Computer Technology University), and the historical KT KIC communications center - none is an operating commercial DC.
- **C lead**: state-media relays (NK Economy, Tongil News), Korea IT Times, Sand Times, ROK media, Naver blog, Wikipedia - keep C until corroborated (e.g., North Hamgyong Electronic Affairs Research Institute needs satellite/defector/sanctions corroboration).
- **U**: NamuWiki, YouTube video, The Diplomat single-source 5G claim, Samtaesong smartphone, any aggregator-style claim. Re-check before promotion.
- **no_projects**: Chagang (searched 2026-08-12) and DC-negative provinces (South/North Hwanghae, Kangwon, Ryanggang) recorded with U grade and the search date; a negative is a real finding, not a gap.
- **Telco network vs datacenter**: Koryolink/Kang Song/Mirae/Sunnet coverage is network context; count as facility only if a source describes core/server/hosting infrastructure with a named operator and location.
- **State institutions vs facilities**: universities (Hamhung), research institutes (Chongjin), and the Haeju semiconductor plant are state computing institutions, not datacenters; record with precise facility_type.
- **Capacity**: keep null everywhere. No source states MW/racks for any KP facility; the only floor-area figure (KT KIC ~9,900 m², 2006) is historical press, B for the 2006 build.
- **De-dup**: KCC is ONE entity (Mangyongdae District / Sunlae-Dong Mangyong District = same district, different romanization); Mirae Wi-Fi in Daily NK + 38 North = one network, two corroborating sources; Koryolink subscriber figures appear in Sand Times and 38 North - do not double-count.
- **Sanctions cross-check**: any new "data center" claim for KP must be checked against OFAC designations, UN Panel/MSMT reports, and 38 North satellite analysis before grading above C.

---

## 8. Verified Source Anchors (industry side, as of 2026-08)

- 38 North mobile communications history (2022-11-15): https://www.38north.org/2022/11/twenty-years-of-mobile-communications-in-north-korea/ ; KIC satellite analysis (2024-09-04): https://www.38north.org/2024/09/kaesong-industrial-complex-a-tortured-history-and-uncertain-future/ ; MSMT report assessment (2025-12): https://www.38north.org/2025/12/assessing-the-msmts-dprk-it-worker-threat-report/
- 38 North DPRK Digital Atlas: https://38northdigitalatlas.org/
- CSIS Cha, North Korea's Cyber Operations (2015-12-16): http://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/publication/151216_Cha_NorthKoreasCyberOperations_Web.pdf ; CSIS DPRK IT Worker Threat (2024): https://www.csis.org/analysis/responding-evolution-and-global-expansion-dprk-it-worker-threat
- Daily NK - Mirae Wi-Fi (2022-10-04): https://www.dailynk.com/english/north-korea-focuses-efforts-preventing-illegal-use-mirae-popular-wi-fi-network/ ; Wonsan smishing (2026-08-05): https://www.dailynk.com/english/wonsan-smishing-voice-phishing-donju-arrests/ ; Ryongaksan illicit software (2026-08): https://www.dailynk.com/english/north-korea-ryongaksan-program-illicit-software/ ; Chongjin IT surge (2024-07-29): https://www.dailynk.com/20240729-4/
- NK News - universities IT departments (2019-09-03): https://www.nknews.org/2019/09/37-north-korean-universities-open-departments-focusing-on-it-engineering-media/ ; web-presence overhaul (2024-01-24): https://www.nknews.org/pro/north-korean-sites-experience-outages-amid-campaign-to-overhaul-web-presence/ ; KIC closure (2016-02-10): https://www.nknews.org/2016/02/breaking-south-korea-temporarily-closes-the-kic/
- North Korea Tech (Kwangmyong tag): https://www.northkoreatech.org/tag/kwangmyong/
- Korea IT Times - KCC: https://www.koreaittimes.com/news/articleView.html?idxno=11397
- Korea Herald - Samtaesong 8 (2023-07-13): https://www.koreaherald.com/article/3168828
- Sand Times - Kang Song vs Koryolink (2025-08-21): https://www.sandtimes.co.kr/news/articleView.html?idxno=1949
- The Diplomat - Sinuiju surveillance (2021-07-15): https://thediplomat.com/2021/07/north-korea-may-be-using-5g-technology-to-monitor-its-border-with-china/
- Dong-A Ilbo - KT KIC communications center (2006-02-07): https://www.donga.com/news/Economy/article/all/20060207/8272742/1
- Tongil News - Hyesan mine automation (2013-09-08): http://www.tongilnews.com/news/articleView.html?idxno=104053
- NK Economy - North Hwanghae surveillance (2019-09-29): http://www.nkeconomy.com/news/articleView.html?idxno=1993 ; North Hamgyong research institute (2022-11-10): http://www.nkeconomy.com/news/articleView.html?idxno=11057
- Wikipedia - KCC: https://en.wikipedia.org/wiki/Korea_Computer_Center ; Kwangmyong: https://en.wikipedia.org/wiki/Kwangmyong_(network)
- NamuWiki - Koryolink: https://namu.wiki/w/고려링크
- Naver blog (seadjk) - Hamhung Computer Technology University: https://blog.naver.com/seadjk/222035658593
- YouTube - Kang Song in Rason: https://www.youtube.com/watch?v=QiODmdA03KY
- ROK Ministry of Unification NK Information Portal (ICT overview 2023-07): https://nkinfo.unikorea.go.kr/nkp/pge/view.do?menuId=MENU_49
- OFAC KCC designation: https://home.treasury.gov/news/press-releases/sm0099 ; MSMT 2nd report (Japan MOFA): https://www.mofa.go.jp/press/release/pressite_000001_01758.html ; UNSCR 2270: https://main.un.org/securitycouncil/en/s/res/2270-(2016)

Final note: KP is a sanctions-isolated, state-controlled market with no verified commercial datacenter. The industry-angle yield is 37 source records across all 13 divisions - networks (Koryolink, Sunnet, Mirae, Kang Song), state institutions (KCC, Hamhung Computer Technology University, Chongjin research institute), historical/closed facilities (KT KIC center), and honest negatives (Chagang; DC-negative provinces). Keep everything above C/U flagged until corroborated by satellite analysis (38 North Digital Atlas), defector reporting (Daily NK), or sanctions documentation (UN/MSMT/OFAC).

## Review record

- Date: 2026-08-12
- Reviewer: gpt5.6-luna
- Conclusion: **REVISED**
- Key changes: confirmed all 13 manifest divisions are enumerated with explicit negatives where appropriate; aligned state-media, ROK-government, sanctions, and OSINT grades; added low-exposure handling to keep facility discovery at city/province context and exclude precise coordinates, security details, and targeting inferences.
