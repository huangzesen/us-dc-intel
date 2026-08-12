# VN Explorer - Industry, Press, Vendors, and Province Query Patterns

Date: 2026-08-12. Scope: Viet Nam datacenter enumeration from Vietnamese-language search, industry/trade press, operator/vendor pages, market reports, and repeatable province/municipality query templates. Reliability grades: **A** = primary source such as operator page/release, government portal, investment-registration/planning record, cloud-provider infrastructure page, or exchange filing; **B** = established trade press, Vietnamese business press, broker/market report, or named local press with specific project facts; **C** = aggregator, directory, social post, unsourced repost, investment-attraction article without follow-up, or vendor marketing that does not name a facility.

---

## 0. Vietnam-specific search model

Vietnam does not have a single public commercial datacenter registry. Enumeration works best as a triangulation exercise:

1. Seed the known commercial operator universe from Viettel IDC, VNPT, FPT Telecom/Fornix, CMC Telecom, STT VNG, NTT/QD.TEK, Edge Centres, Hanoi Telecom, VNTT/Becamex, Gaw, Saigontel, SAM/VSIP, VNG, MobiFone, and industrial-park developers.
2. Use Vietnamese business/ICT press for announcements, power-tariff disputes, MoUs, investment certificates, and hyperscale pipeline.
3. Query each province with Vietnamese project terms plus local industrial-park, high-tech-park, and People's Committee terms.
4. Verify status from official operator pages, provincial portals, investment certificates, industrial park pages, or direct company announcements. For MoUs, keep status as `announced` or `planned` until there is land, investment registration, groundbreaking, construction, or opening evidence.

Vietnamese search is mandatory. English searches find DCD, NTT, STT GDC, ITA, and real-estate reports, but they miss many provincial `trung tâm tích hợp dữ liệu` and local industrial-park announcements.

Core Vietnamese terms:

```text
trung tâm dữ liệu
trung tâm du lieu
TTDL
data center
data centre
IDC
Internet Data Center
trung tâm dữ liệu Internet
trung tâm tích hợp dữ liệu
trung tâm dữ liệu tỉnh
trung tâm dữ liệu quốc gia
siêu trung tâm dữ liệu
trung tâm dữ liệu AI
trung tâm dữ liệu xanh
điện toán đám mây
hạ tầng số
nhà máy dữ liệu
server farm
```

Status and evidence terms:

```text
khởi công
động thổ
khánh thành
khai trương
đưa vào vận hành
chính thức vận hành
đi vào hoạt động
được phê duyệt
chủ trương đầu tư
giấy chứng nhận đăng ký đầu tư
IRC
MOU
biên bản ghi nhớ
thỏa thuận hợp tác
ký kết hợp tác
đề xuất dự án
khảo sát địa điểm
quỹ đất
khu công nghiệp
khu công nghệ cao
khu chế xuất
khu kinh tế
trạm biến áp
công suất điện
phụ tải điện
giá điện
đường truyền
cáp quang biển
```

Capacity / facility words:

```text
MW
MW IT
công suất thiết kế
công suất IT
công suất điện
tủ rack
rack
máy chủ
diện tích sàn
diện tích phòng máy
ha
m2
Tier III
Tier 3
Uptime
PUE
LEED
Rated-3
Rated-4
ANSI/TIA-942
```

Common false positives:

- Provincial e-government `trung tâm tích hợp dữ liệu` are often small public-sector facilities. Capture them only if the enumeration scope includes government datacenters; do not count them as commercial colocation/hyperscale supply.
- `Trung tâm Dữ liệu quốc gia` usually refers to the national public-sector data platform under the Ministry of Public Security. It is relevant for sovereign data infrastructure but can drown out commercial datacenter searches.
- `IDC` can also mean Industrial Development Corporation or an unrelated company name; combine with `trung tâm dữ liệu`, `rack`, `Uptime`, `Tier`, or operator names.
- Project articles in Vietnam often announce MoUs long before licensing/construction. Record exact verbs.

## 1. High-signal industry and press sources

Use press as the discovery feed, then verify facility facts through primary operator/government sources where possible.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics Vietnam tag | `https://www.datacenterdynamics.com/en/tags/vietnam/`, `site:datacenterdynamics.com Vietnam "data center" "{operator}"` | Best global trade feed for Viettel, CMC, FPT, STT VNG, NTT/QD.TEK, Edge Centres, Gaw, Saigontel, cloud local zones, and HCMC hyperscale projects. | B+ |
| International Trade Administration market intelligence | `https://www.trade.gov/market-intelligence/vietnam-data-centers` | Concise market snapshot; cites MOST count of 41 active commercial DCs / 221 MW and lists 12 investors. Good seed list, not facility-level proof. | B+ |
| Viet Nam Government Portal | `https://en.baochinhphu.vn/`, `https://thanglong.chinhphu.vn/` | Government-level context, especially national capacity counts, Viettel projects in Ha Noi/Hoa Lac, and public-sector digital infrastructure. | A-/B+ |
| Ministry / MIC / MOST English pages | `https://english.mic.gov.vn/`, `https://mst.gov.vn/` | Policy, telecom/digital-infrastructure strategy, cloud/data-center regulation, sector statistics. Direct facility details are uncommon. | A-/B |
| Viet Nam Investment Review / VIR | `https://vir.com.vn/` | Strong English-language investment press; useful for KBC/AIC, CMC, G42, Saigontel, industrial-park and foreign-investor projects. | B |
| The Investor Vietnam | `https://theinvestor.vn/` | Strong business press for power-pricing disputes, SAM DigitalHub, VNPT/FPT openings, G42, Saigontel, foreign investment. | B |
| VietnamPlus / VNA | `https://en.vietnamplus.vn/`, `https://www.vietnamplus.vn/` | State news agency; good for national policy, CMC approval, government-facing digital infrastructure, provincial announcements. | B+ |
| VnExpress / VnExpress International | `https://vnexpress.net/`, `https://e.vnexpress.net/` | High-yield Vietnamese tech/business coverage for Viettel Hoa Lac, Tan Phu Trung, CMC, national statistics, AI datacenter narrative. | B |
| VietnamNet / ICTNews | `https://vietnamnet.vn/`, `https://ictnews.vietnamnet.vn/` | Excellent Vietnamese-language feed for electricity tariff disputes, policy, operator list, government IDC references, older facility openings. | B |
| ICT Vietnam / Tap chi TT&TT | `https://ictvietnam.vn/` | Industry/policy magazine; good for local IDC market, cloud, submarine cables, telecom infrastructure. | B |
| Bao Dau Tu / baodautu.vn | `https://baodautu.vn/` | Investment newspaper; useful for CMC, Viettel, provincial smart-city/data-center investments, industrial parks. | B |
| Tuoi Tre / Tuoi Tre News | `https://tuoitre.vn/`, `https://news.tuoitre.vn/` | Good for local business/regional projects such as Ba Ria - Vung Tau Digital Hub, Long An, HCMC. | B |
| VOV | `https://vov.vn/`, `https://vov.gov.vn/` | State broadcaster; useful for provincial data strategies, Ba Ria - Vung Tau, local government announcements. | B |
| W.Media / Dgtl Infra / Light Reading / Capacity Media / TechNode Global | site-scoped search | Useful APAC/investor trade feeds for STT GDC, SAM, Sembcorp, Evolution, Edge Centres, G42. Verify locally. | B/C+ |
| CBRE, Cushman & Wakefield, Savills, JLL, Arizton, Mordor, ResearchAndMarkets | site-scoped search | Market sizing, capacity by city, pipeline estimates, investor/operator lists. Good for context and leads; not final facility proof unless named. | B for aggregate, C for paywalled snippets |
| DataCenterMap / Baxtel / PeeringDB / Datacenters.com / OCOLO / Cloudscene | site-scoped search | Facility-address discovery and cross-checking. Use as lead/directory evidence only. PeeringDB can be stronger for network-carrier facilities with exact addresses. | C, sometimes B- |

Useful press queries:

```text
site:datacenterdynamics.com Vietnam "data center" "{operator}"
site:theinvestor.vn Vietnam "data center" "{province_or_city}"
site:vir.com.vn "data centre" "Vietnam" "{operator}"
site:vietnamnet.vn "trung tâm dữ liệu" "{operator}"
site:vnexpress.net "trung tâm dữ liệu" "{operator}"
site:ictvietnam.vn "trung tâm dữ liệu" "{province_or_city}"
site:baodautu.vn "trung tâm dữ liệu" "{province_or_city}"
site:tuoitre.vn "trung tâm dữ liệu" "{province_or_city}"
site:vov.vn "trung tâm dữ liệu" "{province_or_city}"
```

## 2. Operator and developer seed list

Official operator pages are **A** for existence, branding, and broad location. Treat capacity as **A-** only when facility-specific, and **B/C** when it is a rounded buildout target repeated from press.

| Operator / developer | Official URL / evidence route | Search pivots | Notes |
|---|---|---|---|
| Viettel IDC / Viettel Group | `https://viettelidc.com.vn/`, Hoa Lac article `https://viettelidc.com.vn/tin-tuc/viettel-khai-truong-trung-tam-du-lieu-lon-nhat-viet-nam-trien-khai-cong-nghe-xanh-san-sang-cho-phat-trien-ai`, Tan Phu Trung release `https://viettel.com.vn/en/news-events/news/viettel-breaks-ground-on-vietnams-first-hyperscale-data-center/` | `Viettel IDC Hòa Lạc`, `Viettel IDC Bình Dương`, `Viettel Hoàng Hoa Thám`, `Viettel Đà Nẵng`, `Viettel Tân Phú Trung 140MW`, `Viettel 24 data centers 560MW` | Most important domestic operator. Known anchors: Hoa Lac/Ha Noi 30 MW, Binh Duong, HCMC Hoang Hoa Tham, Da Nang, Tan Phu Trung/Cu Chi hyperscale campus. |
| VNPT / VNPT IDC | `https://vnptidc.vn/`, `https://vnpt.vn/doanh-nghiep/tu-van/trung-tam-du-lieu.html` | `VNPT IDC Hòa Lạc`, `VNPT IDC Cầu Giấy`, `VNPT IDC Tân Thuận`, `VNPT IDC Đà Nẵng`, `VNPT Bình Dương data center` | Major state telco; DCD reports Hoa Lac launch outside Hanoi. Official pages and Baxtel/DataCenterMap help enumerate older sites. |
| FPT Telecom / Fornix | `https://fpt.com/en/news/fpt-news/fpt-khanh-thanh-trung-tam-du-lieu-quy-mo-lon-nhat-viet-nam`, `https://fornix.fpt.work/en/about-dc/` | `FPT Fornix HN01`, `FPT Fornix HN02`, `FPT Fornix HCM01`, `FPT Fornix HCM02`, `FPT 3600 racks HCMC` | Four large Fornix sites in Ha Noi and HCMC; HCM02 at/near Saigon Hi-Tech Park is a key 2025 opening. |
| CMC Telecom / CMC Corporation | `https://cmctelecom.vn/san-pham/data-center/`, `https://cmctelecom.vn/bai-viet/cmc-telecom-launches-vnix-pop-at-tan-thuan-data-centre/` | `CMC Data Center Tân Thuận`, `CMC SHTP HCMC01`, `CMC Cầu Giấy data center`, `CMC hyperscale Saigon Hi-Tech Park 120MW`, `CMC 250 triệu USD trung tâm dữ liệu` | Three-site current portfolio in Hanoi/HCMC plus approved/planned hyperscale at Saigon Hi-Tech Park. |
| ST Telemedia Global Data Centres / VNG | `https://www.sttelemediagdc.com/vn-en/locations/ho-chi-minh-city` | `STT VNG Ho Chi Minh City 1`, `STT VNG Ho Chi Minh City 2`, `VNG Data Center Tân Thuận`, `60MW STT VNG` | Official page lists STT VNG HCMC1 and planned HCMC2 in Tan Thuan cluster; HCMC2 up to 60 MW IT load. |
| NTT Global Data Centers + QD.TEK | NTT release `https://group.ntt/en/newsrelease/2022/03/29/220329a.html`, facility page `https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/ho-chi-minh-city-1-data-center` | `NTT QD.TEK HCMC1`, `NTT Ho Chi Minh City 1 Data Center`, `Saigon Hi-Tech Park 6MW NTT` | HCMC1 in Saigon Hi-Tech Park: official NTT page gives 6 MW critical IT load and 3,100 sqm server space. |
| Edge Centres | `https://edgecentre.com/` plus DCD | `Edge Centres EC51 Ho Chi Minh`, `Edge Centres Vietnam`, `EC51 HCMC data center` | Edge/colo presence in HCMC; verify exact address/status through operator pages and directories. |
| Hanoi Telecom / HTC / Evolution | company releases plus DCD | `Hanoi Telecom data center`, `HTC Evolution data center Vietnam`, `Evolution HCMC data center`, `VN02 52MW` | Evolution/HTC/Hathor pipeline appears in trade press; verify any investment registration certificate and HCMC High-Tech Park location. |
| VNTT / Becamex IDC | `https://vntt.com.vn/`, Becamex ecosystem pages | `VNTT eDatacenter`, `Becamex data center`, `Bình Dương eDatacenter`, `VSIP data center` | Binh Duong industrial/smart-city ecosystem; useful for both commercial and government-adjacent facilities. |
| SAM / VSIP / Sembcorp / Becamex | SAM/VSIP releases plus The Investor/DCD | `SAM DigitalHub`, `VSIP 3 data center`, `Bình Dương 150MW data center`, `Saigon Asset Management data center` | SAM DigitalHub at VSIP 3, Binh Duong: widely reported as 150 MW / ~50 ha / USD 1.5bn. Treat as announced/planned until construction proof. |
| Saigontel / Saigon Invest Group | `https://www.saigontel.vn/` | `Saigontel data center Nam Tân Tập Long An`, `Saigontel Tân Phú Trung data center`, `P&G Tech Saigontel data center` | Industrial-park/telecom developer; Long An and HCMC/Tan Phu Trung are key pivots. |
| Gaw Capital / Infracrowd / Worldwide DC Solution / OneHub Saigon | company pages, DCD, HCMC investment press | `Gaw Saigon Hi-Tech Park 20MW`, `Infracrowd Vietnam data center`, `OneHub Saigon data center`, `Worldwide DC Solution Vietnam` | Foreign-investor pipeline often appears before operator pages; grade carefully. |
| KBC / Accelerated Infrastructure Capital / VietinBank | VIR, DCD, The Tech Capital | `KBC AIC VietinBank data centre`, `SGI-HCM AI Data Center Campus`, `Kinh Bắc Tân Phú Trung data center 200MW` | HCMC/Tan Phu Trung AI campus MoU. MoU evidence is not construction proof. |
| G42 / FPT / Viet Thai Group | The Investor, VnExpress, VIR | `G42 FPT Viet Thai AI data center`, `sovereign AI cloud Vietnam`, `2 billion hyperscale data center Vietnam` | Large AI/sovereign cloud proposal; verify project vehicle, location, investment certificate. |
| MobiFone | `https://mobifone.vn/` plus Vietnamese ICT press | `MobiFone trung tâm dữ liệu Hải Phòng`, `MobiFone Đà Nẵng data center`, `MobiFone Đồng Nai data center`, `MobiFone 7 trung tâm dữ liệu` | National telco data center buildout; facility detail may be thin. |
| True IDC Vietnam | `https://www.trueidc.com/` / local pages plus directories | `True IDC Vietnam Tân Thuận`, `True IDC Ho Chi Minh data center` | HCMC facility lead; verify beyond directories. |
| QTSC / Quang Trung Software City | `https://qtsc.com.vn/` | `QTSC Data Center`, `Quang Trung Software City data center`, `Công viên phần mềm Quang Trung trung tâm dữ liệu` | HCMC software park data center; usually smaller than hyperscale projects. |
| VNG Cloud | `https://vngcloud.vn/`, STT GDC pages | `VNG Cloud data center`, `VNG Data Center Tân Thuận`, `VNG Cloud HCMC data center` | Legacy VNG Data Center now STT VNG HCMC1; watch for duplicate entries. |

## 3. Cloud and network-region signals

Cloud-region pages prove cloud availability at a region/local-zone level, not facility ownership or exact address. Use them as **A** for service availability and then pivot to colocations, Direct Connect/ExpressRoute/Interconnect nodes, or local operator partnerships.

| Provider | Official source | Vietnam signal |
|---|---|---|
| AWS | Local Zones locations `https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/`; GA announcement `https://aws.amazon.com/about-aws/whats-new/2026/06/aws-local-zones-hanoi-vietnam/`; Direct Connect Hanoi `https://aws.amazon.com/about-aws/whats-new/2025/12/aws-direct-connect-hanoi/` | Hanoi Local Zone generally available in June 2026; first Direct Connect location in Vietnam within CMC Tower, Hanoi. Query CMC/Viettel/VNPT/Hanoi facility links. |
| Microsoft Azure | Region list `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; Azure geographies `https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies` | No public Azure Vietnam region on official region list as of this methodology date. Use partner/on-ramp claims as network leads only. |
| Google Cloud | Locations `https://cloud.google.com/about/locations`; Google datacenter locations `https://datacenters.google/locations` | No official Google Cloud Vietnam region/facility listed. Reuters/press rumors about Google Vietnam DC should be treated as C until official/permit evidence appears. |
| Oracle Cloud | Public cloud regions `https://www.oracle.com/cloud/public-cloud-regions/` | No official OCI Vietnam public region listed. Use OCI partner/connectivity claims only as demand signal. |
| Cloudflare / Akamai / CDN / IX | official network maps, PeeringDB | Useful for interconnection and edge presence in Hanoi/HCMC, not standalone datacenter facility proof. |

Pivot queries:

```text
"AWS Local Zone" Hanoi Vietnam "data center"
"AWS Direct Connect" "CMC Tower" Hanoi
"AWS" "Hà Nội" "trung tâm dữ liệu"
"Azure" Vietnam "data center" "ExpressRoute"
"Google Cloud" Vietnam "data center" "HCMC" OR "Ho Chi Minh"
"Oracle Cloud" Vietnam "data center"
site:peeringdb.com Vietnam "Ho Chi Minh City" "Data Center"
```

## 4. Regional developer clusters

### 4.1 Ha Noi / Hoa Lac / northern metro

Priority areas: Ha Noi municipality, Hoa Lac Hi-Tech Park, Cau Giay, Thanh Xuan, Thang Long Industrial Park, and nearby Bac Ninh/Bac Giang/Hung Yen/Hai Duong electronics corridors.

Known/pivotal operators and leads:

- Viettel IDC Hoa Lac: 30 MW / 2,400+ racks official Viettel release.
- VNPT IDC Hoa Lac, Cau Giay, and older Hanoi portfolio.
- FPT Fornix HN01/HN02.
- CMC Tower / CMC Hanoi sites, including AWS Direct Connect location in CMC Tower.
- Hanoi Telecom / HTC and Evolution-related leads.
- National Data Center and provincial/state government data platforms can create many public-sector results.

Search:

```text
"Hà Nội" "trung tâm dữ liệu" ("Viettel" OR "VNPT" OR "FPT" OR "CMC" OR "Hanoi Telecom")
"Hòa Lạc" "trung tâm dữ liệu" ("MW" OR "rack" OR "Uptime")
"Khu Công nghệ cao Hòa Lạc" "data center"
"Cầu Giấy" "trung tâm dữ liệu" "CMC" OR "VNPT"
"Thăng Long" "khu công nghiệp" "trung tâm dữ liệu" "VNPT"
"AWS Direct Connect" "CMC Tower" "Hanoi"
site:hanoi.gov.vn "trung tâm dữ liệu"
site:hhtp.gov.vn "trung tâm dữ liệu"
```

### 4.2 Ho Chi Minh City / Tan Thuan / Saigon Hi-Tech Park / Tan Phu Trung

This is the highest-yield commercial region and should be enumerated by cluster: Tan Thuan Export Processing Zone/District 7, Saigon Hi-Tech Park/Thu Duc, Tan Phu Trung Industrial Park/Cu Chi, Quang Trung Software City/District 12, and older telco urban sites.

Known/pivotal operators and leads:

- Viettel Tan Phu Trung: 140 MW / ~10,000 racks / 4 ha, first phase targeted 2026, full buildout before 2030.
- STT VNG HCMC1 operational and STT VNG HCMC2 planned 60 MW in Tan Thuan cluster.
- CMC Tan Thuan operational; CMC hyperscale Saigon Hi-Tech Park approved/planned.
- NTT HCMC1 with QD.TEK at Saigon Hi-Tech Park, 6 MW official NTT facility page.
- FPT Fornix HCM01/HCM02; HCM02 3,600 racks / 10,000 sqm.
- KBC/AIC/VietinBank SGI-HCM AI campus at Tan Phu Trung, reported 200 MW/MoU.
- Evolution/Hathor/Frontier and StarMason/Sembcorp/BB Holdings hyperscale projects in Saigon Hi-Tech Park reported in 2026 press.
- Edge Centres, Gaw Capital, True IDC, QTSC, VNG Cloud, MobiFone, Saigontel.

Search:

```text
"TP.HCM" "trung tâm dữ liệu" ("khởi công" OR "khánh thành" OR "giấy chứng nhận đăng ký đầu tư")
"Thành phố Hồ Chí Minh" "data center" ("MW" OR "rack" OR "Uptime")
"Khu chế xuất Tân Thuận" "trung tâm dữ liệu"
"Tan Thuan" "data center" "Ho Chi Minh"
"Khu Công nghệ cao TP.HCM" "trung tâm dữ liệu"
"Saigon Hi-Tech Park" "data center" ("CMC" OR "NTT" OR "Evolution" OR "Sembcorp" OR "Gaw")
"Tân Phú Trung" "trung tâm dữ liệu" ("Viettel" OR "KBC" OR "Saigontel")
"Củ Chi" "trung tâm dữ liệu" "140 MW"
site:shtp.hochiminhcity.gov.vn "trung tâm dữ liệu"
site:hepza.hochiminhcity.gov.vn "trung tâm dữ liệu"
site:hochiminhcity.gov.vn "trung tâm dữ liệu"
```

### 4.3 Binh Duong / Dong Nai / Long An / Ba Ria - Vung Tau southern industrial belt

This belt is the main spillover zone for HCMC power, land, and industrial-park campuses.

Known/pivotal operators and leads:

- Binh Duong: SAM DigitalHub at VSIP 3 (150 MW, ~50 ha), Viettel IDC Binh Duong, VNTT/Becamex eDatacenter, possible VNPT Binh Duong expansion.
- Dong Nai: MobiFone and provincial/enterprise leads; search Amata, Long Thanh, Nhon Trach, Bien Hoa industrial zones.
- Long An: Saigontel + P&G Tech data center at Nam Tan Tap Green Industrial Park.
- Ba Ria - Vung Tau: Digital Hub / DCH super data center and submarine cable station in Chau Duc district; cable landing and power are key evidence.

Search:

```text
"Bình Dương" "trung tâm dữ liệu" ("VSIP 3" OR "SAM DigitalHub" OR "VNTT" OR "Becamex")
"VSIP 3" "data center" "150MW"
"Đồng Nai" "trung tâm dữ liệu" ("MobiFone" OR "Amata" OR "Long Thành" OR "Nhơn Trạch")
"Long An" "trung tâm dữ liệu" ("Saigontel" OR "P&G Tech" OR "Nam Tân Tập")
"Bà Rịa Vũng Tàu" "trung tâm dữ liệu" ("Digital Hub" OR "DCH" OR "cáp quang biển")
"Châu Đức" "Digital Hub" "trung tâm dữ liệu"
site:binhduong.gov.vn "trung tâm dữ liệu"
site:dongnai.gov.vn "trung tâm dữ liệu"
site:longan.gov.vn "trung tâm dữ liệu"
site:baria-vungtau.gov.vn "trung tâm dữ liệu"
```

### 4.4 Da Nang / central coast / central highlands

Da Nang is the established central-region DC hub; the central coast also has investment-attraction leads tied to economic zones, software parks, and submarine-cable strategy.

Known/pivotal operators and leads:

- Da Nang: VNPT IDC An Don, Viettel IDC Da Nang, MobiFone, Hoa Khanh/Software Park directory leads, local government data center.
- Binh Dinh: Nhon Hoi Economic Zone big-data/data-center investment-seeking articles.
- Khanh Hoa, Quang Nam, Quang Ngai, Thua Thien-Hue: mostly provincial integrated data centers unless a new industrial-park/high-tech project appears.
- Gia Lai/Dak Lak/Lam Dong: public-sector/provincial data strategies; monitor AI/agritech/data platform projects rather than expecting commercial colocation.

Search:

```text
"Đà Nẵng" "trung tâm dữ liệu" ("Viettel" OR "VNPT" OR "MobiFone" OR "FPT")
"Da Nang" "data center" ("VNPT" OR "Viettel" OR "Hoa Khanh")
"Công viên phần mềm Đà Nẵng" "trung tâm dữ liệu"
"Khu công nghệ thông tin tập trung Đà Nẵng" "data center"
"Bình Định" "trung tâm dữ liệu" ("Nhon Hoi" OR "Nhơn Hội" OR "Korean")
"Khánh Hòa" "trung tâm dữ liệu" ("khu kinh tế" OR "Vân Phong")
"Quảng Nam" "trung tâm dữ liệu" ("Chu Lai" OR "khu kinh tế")
site:danang.gov.vn "trung tâm dữ liệu"
site:dic.danang.gov.vn "trung tâm dữ liệu"
site:binhdinh.gov.vn "trung tâm dữ liệu"
```

### 4.5 Other northern / Mekong / provincial government sweep

Outside the major clusters, most hits are provincial integrated data centers, IOC/smart-city control centers, SOC upgrades, or enterprise IT rooms. Still query every province because local government sources sometimes expose planned industrial-park DCs early.

Search:

```text
"{province_vietnamese}" "trung tâm tích hợp dữ liệu"
"{province_vietnamese}" "trung tâm dữ liệu tỉnh"
"{province_vietnamese}" "trung tâm điều hành thông minh" "dữ liệu"
"{province_vietnamese}" "chuyển đổi số" "trung tâm dữ liệu"
"{province_vietnamese}" "khu công nghiệp" "trung tâm dữ liệu"
"{province_vietnamese}" "khu công nghệ cao" "trung tâm dữ liệu"
"{province_vietnamese}" "MOU" "trung tâm dữ liệu"
"{province_vietnamese}" "giấy chứng nhận đăng ký đầu tư" "trung tâm dữ liệu"
site:{province-domain}.gov.vn "trung tâm dữ liệu"
site:{province-domain}.gov.vn "trung tâm tích hợp dữ liệu"
```

## 5. Province/municipality query matrix

Run each division with both ASCII and Vietnamese diacritics. The table gives a first-pass Vietnamese name and the highest-yield local pivots. For post-2025 administrative changes, also search the old province/city names because most older press and facility pages use pre-merger geography.

| Manifest division | Vietnamese query name | First-pass local pivots |
|---|---|---|
| Lai Chau | Lai Châu | `trung tâm tích hợp dữ liệu`, `chính quyền số`, provincial portal |
| Lao Cai | Lào Cai | `trung tâm dữ liệu tỉnh`, `chiến lược dữ liệu`, border logistics |
| Ha Giang | Hà Giang | `trung tâm tích hợp dữ liệu`, `IOC`, `chuyển đổi số` |
| Cao Bang | Cao Bằng | `trung tâm dữ liệu tỉnh`, password/security regulation, provincial portal |
| Son La | Sơn La | `trung tâm tích hợp dữ liệu`, state procurement, firewall/SOC upgrade |
| Yen Bai | Yên Bái | `trung tâm tích hợp dữ liệu`, `IOC`, `chính quyền điện tử` |
| Tuyen Quang | Tuyên Quang | `trung tâm dữ liệu tỉnh`, `IOC`, `chuyển đổi số` |
| Lang Son | Lạng Sơn | `trung tâm tích hợp dữ liệu`, border-gate digital platform |
| Quang Ninh | Quảng Ninh | QNICT, `trung tâm tích hợp dữ liệu`, Ha Long/Cai Lan industrial/logistics |
| Hoa Binh | Hòa Bình | `trung tâm dữ liệu`, industrial park, Hoa Lac spillover |
| Ninh Binh | Ninh Bình | `trung tâm dữ liệu tỉnh`, industrial parks |
| Thai Binh | Thái Bình | `trung tâm tích hợp dữ liệu`, Thai Binh Economic Zone |
| Thanh Hoa | Thanh Hóa | `Nghi Sơn`, `trung tâm dữ liệu`, provincial data center |
| Nghe An | Nghệ An | `trung tâm dữ liệu`, VSIP Nghe An, WHA, Vinh |
| Ha Tinh | Hà Tĩnh | `Vũng Áng`, `trung tâm dữ liệu`, provincial data center |
| Quang Binh | Quảng Bình | `trung tâm tích hợp dữ liệu`, `khu kinh tế Hòn La` |
| Quang Tri | Quảng Trị | `trung tâm dữ liệu`, `Đông Nam Quảng Trị`, energy/power |
| Thua Thien-Hue | Thừa Thiên Huế / Huế | Hue-S, smart city, `trung tâm dữ liệu`, software park |
| Quang Nam | Quảng Nam | `Chu Lai`, `trung tâm dữ liệu`, industrial zone |
| Kon Tum | Kon Tum | `trung tâm tích hợp dữ liệu`, provincial data strategy |
| Quang Ngai | Quảng Ngãi | QNICT, `Dung Quất`, `trung tâm tích hợp dữ liệu` |
| Gia Lai | Gia Lai | National Data Center pilot, FPT IS, provincial data strategy |
| Binh Dinh | Bình Định | `Nhơn Hội`, `Big Data`, Korean investor, Quy Nhon |
| Phu Yen | Phú Yên | `trung tâm tích hợp dữ liệu`, Tuy Hoa, ICT plans |
| Dak Lak | Đắk Lắk | `trung tâm dữ liệu`, Buon Ma Thuot, provincial digital platforms |
| Khanh Hoa | Khánh Hòa | `Vân Phong`, Nha Trang, `trung tâm dữ liệu`, smart city |
| Lam Dong | Lâm Đồng | Da Lat, Duc Trong, `trung tâm dữ liệu`, provincial IOC |
| Ninh Thuan | Ninh Thuận | energy/power, `trung tâm dữ liệu`, `Cà Ná` |
| Tay Ninh | Tây Ninh | HCMC spillover, border logistics, industrial park |
| Dong Nai | Đồng Nai | Amata, Long Thanh, Nhon Trach, MobiFone, industrial park |
| Binh Thuan | Bình Thuận | `trung tâm dữ liệu`, digital-government project list, energy |
| Long An | Long An | Saigontel, P&G Tech, Nam Tan Tap, HCMC spillover |
| Ba Ria - Vung Tau | Bà Rịa - Vũng Tàu | Digital Hub, DCH, Chau Duc, submarine cable, Cai Mep |
| An Giang | An Giang | smart-city data infrastructure, provincial IOC |
| Dong Thap | Đồng Tháp | provincial data center, police/government digital systems |
| Tien Giang | Tiền Giang | smart-city plan, integrated data center |
| Kien Giang | Kiên Giang | provincial data center, Phu Quoc digital infrastructure |
| Vinh Long | Vĩnh Long | provincial data center, digital government |
| Ben Tre | Bến Tre | provincial data center upgrade, SOC |
| Tra Vinh | Trà Vinh | provincial data center, coastal energy |
| Soc Trang | Sóc Trăng | provincial digital government; low commercial expectation |
| Bac Kan | Bắc Kạn | provincial integrated data center, VNPT IOC |
| Bac Giang | Bắc Giang | electronics industrial parks, Foxconn/Luxshare/Goertek, provincial data center |
| Bac Lieu | Bạc Liêu | provincial digital government, energy/power |
| Bac Ninh | Bắc Ninh | VSIP, Yen Phong, electronics parks, smart-city data center |
| Binh Duong | Bình Dương | SAM DigitalHub, VSIP 3, Becamex/VNTT, Viettel IDC, VNPT |
| Binh Phuoc | Bình Phước | provincial data center, Dong Xoai, industrial parks |
| Ca Mau | Cà Mau | enterprise DCs such as PVCFC, provincial digital government |
| Hai Duong | Hải Dương | industrial parks, Hanoi-Hai Phong corridor |
| Ha Nam | Hà Nam | VNPT/IOC, Dong Van industrial parks |
| Hung Yen | Hưng Yên | Hanoi spillover, Pho Noi/Thang Long II industrial parks |
| Nam Dinh | Nam Định | provincial integrated data center, industrial zones |
| Phu Tho | Phú Thọ | provincial data center, Viet Tri |
| Thai Nguyen | Thái Nguyên | Samsung/electronics ecosystem, provincial data center |
| Vinh Phuc | Vĩnh Phúc | Binh Xuyen/Ba Thien industrial parks, Hanoi spillover |
| Dien Bien | Điện Biên | provincial data center/IOC; low commercial expectation |
| Dak Nong | Đắk Nông | provincial digital government, energy |
| Hau Giang | Hậu Giang | provincial digital government, industrial park |
| Can Tho | Cần Thơ | Mekong hub, VNPT/MobiFone/FPT/CMC searches, software park |
| Da Nang | Đà Nẵng | VNPT, Viettel, MobiFone, Hoa Khanh, software park |
| Ha Noi | Hà Nội | Viettel Hoa Lac, VNPT Hoa Lac/Cau Giay, FPT HN01/HN02, CMC Tower, AWS Direct Connect |
| Hai Phong | Hải Phòng | MobiFone, VNPT/Viettel, Deep C, Cat Hai, Lach Huyen, industrial parks |
| Ho Chi Minh | Thành phố Hồ Chí Minh / TP.HCM | Tan Thuan, Saigon Hi-Tech Park, Tan Phu Trung, Viettel, CMC, FPT, STT VNG, NTT, Gaw, Edge Centres, KBC/AIC |

## 6. Generic query templates for every province

### 6.1 Commercial/hyperscale sweep

```text
"{province_vietnamese}" ("trung tâm dữ liệu" OR "data center" OR "data centre") ("MW" OR "rack" OR "công suất")
"{province_vietnamese}" ("siêu trung tâm dữ liệu" OR "trung tâm dữ liệu AI" OR "hyperscale")
"{province_vietnamese}" ("trung tâm dữ liệu" OR "data center") ("khu công nghiệp" OR "khu công nghệ cao" OR "khu kinh tế" OR "khu chế xuất")
"{province_vietnamese}" ("trung tâm dữ liệu" OR "data center") ("khởi công" OR "khánh thành" OR "đưa vào vận hành")
"{province_vietnamese}" ("trung tâm dữ liệu" OR "data center") ("chủ trương đầu tư" OR "giấy chứng nhận đăng ký đầu tư" OR "IRC")
"{province_vietnamese}" ("trung tâm dữ liệu" OR "data center") ("MOU" OR "biên bản ghi nhớ" OR "ký kết hợp tác")
"{industrial_park_name}" ("trung tâm dữ liệu" OR "data center") ("MW" OR "rack" OR "ha")
```

### 6.2 Operator-specific sweep

```text
"{operator}" "{province_vietnamese}" ("trung tâm dữ liệu" OR "data center" OR "IDC")
"{operator}" "{city_or_district_vietnamese}" ("MW" OR "rack" OR "Uptime" OR "Tier III")
site:{operator-domain} "{province_vietnamese}" ("trung tâm dữ liệu" OR "data center")
site:viettelidc.com.vn "{province_vietnamese}" "trung tâm dữ liệu"
site:vnptidc.vn "{province_vietnamese}" "IDC"
site:fpt.com "{province_vietnamese}" "data center"
site:cmctelecom.vn "{province_vietnamese}" "Data Center"
site:sttelemediagdc.com Vietnam "{city_english}"
site:services.global.ntt Vietnam "{city_english}" "Data Center"
```

### 6.3 Government and local confirmation

```text
site:{province-domain}.gov.vn "trung tâm dữ liệu"
site:{province-domain}.gov.vn "trung tâm tích hợp dữ liệu"
site:{province-domain}.gov.vn "trung tâm điều hành thông minh" "dữ liệu"
site:{province-domain}.gov.vn "chủ trương đầu tư" "trung tâm dữ liệu"
site:{province-domain}.gov.vn "giấy chứng nhận đăng ký đầu tư" "trung tâm dữ liệu"
site:{province-domain}.gov.vn "khu công nghiệp" "trung tâm dữ liệu"
site:{province-domain}.gov.vn "trạm biến áp" "trung tâm dữ liệu"
site:dpi.{province-domain}.gov.vn "trung tâm dữ liệu"
site:sct.{province-domain}.gov.vn "trung tâm dữ liệu" "điện"
site:stttt.{province-domain}.gov.vn "trung tâm dữ liệu"
```

If a province subdomain pattern fails, search the province name plus the department name:

```text
"Sở Kế hoạch và Đầu tư" "{province_vietnamese}" "trung tâm dữ liệu"
"Sở Thông tin và Truyền thông" "{province_vietnamese}" "trung tâm dữ liệu"
"Ban Quản lý các khu công nghiệp" "{province_vietnamese}" "trung tâm dữ liệu"
"Ban Quản lý Khu công nghệ cao" "{province_vietnamese}" "trung tâm dữ liệu"
```

### 6.4 Power, cooling, and cable evidence

```text
"{project_name}" ("công suất điện" OR "phụ tải điện" OR "trạm biến áp" OR "110kV" OR "220kV")
"{project_name}" ("PUE" OR "làm mát" OR "cooling" OR "green data center")
"{province_vietnamese}" "trung tâm dữ liệu" ("EVN" OR "điện lực" OR "giá điện")
"{province_vietnamese}" "trung tâm dữ liệu" ("cáp quang biển" OR "submarine cable" OR "landing station")
"{province_vietnamese}" "data center" ("substation" OR "power capacity" OR "grid")
```

### 6.5 Status downgrade / cancellation sweep

```text
"{project_name}" ("chậm tiến độ" OR "tạm dừng" OR "dừng triển khai" OR "thu hồi" OR "hủy bỏ")
"{project_name}" ("khó khăn" OR "vướng mắc" OR "chưa triển khai" OR "điều chỉnh quy hoạch")
"{project_name}" ("phản đối" OR "khiếu nại" OR "môi trường" OR "thiếu điện")
"{developer}" "{province_vietnamese}" "data center" ("cancelled" OR "delayed" OR "suspended")
```

## 7. Evidence handling and grading notes

- **A**: official operator facility page/release; provincial People's Committee or department page naming project/location/status; investment registration certificate; high-tech park/industrial park authority page; cloud-provider official infrastructure page; PeeringDB only for exact interconnection-facility address when maintained by the operator.
- **B**: DCD, ITA, VIR, The Investor, VietnamPlus/VNA, VnExpress, VietnamNet, ICTVietnam, Tuoi Tre, VOV, Bao Dau Tu, CBRE/Cushman/Savills/JLL reports with named projects.
- **C**: Baxtel/DataCenterMap/Datacenters.com/OCOLO/Cloudscene alone, LinkedIn/social posts, paywalled market-report snippets, republished articles without original source, investment-attraction articles that only say the province is seeking investors.
- Capacity fields must distinguish `IT load`, `total power`, `designed capacity`, `rack capacity`, and `full buildout`. Vietnam articles frequently report future full-campus MW as if current capacity.
- Keep provincial integrated data centers separate from commercial colocation/hyperscale facilities in notes. Many provinces have small public-sector data centers with no MW disclosure; they are real facilities but not market supply.
- For 2025-2026 hyperscale projects, require at least one of: investment registration certificate, official operator release, high-tech/industrial park authority announcement, or construction/groundbreaking evidence before marking as `approved` or `construction`.
