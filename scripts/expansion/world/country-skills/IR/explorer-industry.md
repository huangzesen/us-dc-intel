# IR Explorer - Industry / Vendor Discovery for Iran Datacenters

Date: 2026-08-12. Scope: how to enumerate Iran (IR) datacenter projects through Iranian colo/cloud providers, telecom operators, cloud-region/product pages, Persian trade press, ICT associations, directories, and province-by-province query patterns. Reliability grades: **A** = official regulator/government/operator/certification source; **B** = established trade press, exchange/company disclosure, or strong technical directory used with corroboration; **C** = weak directory, reseller page, social post, SEO hosting page, or unverified aggregator lead.

---

## 0. Iran-specific frame

- Iran does **not** have a clean public facility registry comparable to some Gulf regulator lists. Enumeration works by triangulating: CRA telecom license holders, ITOI/datacenter audit or cloud-provider qualification material, operator pages, Persian tech press, public tenders, network directories, and cloud/server product pages.
- The commercial market is **Tehran-heavy**. DataCenterMap lists 19 Iran facilities across 6 markets: Tehran (14), Isfahan, Rasht, Shiraz, Hamedan, and Qom: https://www.datacentermap.com/iran/ . Treat this as a lead index, not final proof.
- Public "cloud region" language inside Iran often means a domestic provider's product availability zone or named datacenter, not AWS/Azure/GCP/OCI hyperscale. Official global cloud-region lists from AWS, Microsoft Azure, Google Cloud, and Oracle do **not** show an Iran public region; use them mainly to document a negative check:
  - AWS global infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/
  - Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
  - Google Cloud locations: https://cloud.google.com/about/locations
  - Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Iran's most useful local terms are Persian: `مرکز داده`, `مراکز داده`, `دیتاسنتر`, `دیتا سنتر`, `مرکزداده`, `خدمات دیتاسنتر`, `فضای دیتاسنتر`, `هم‌مکانی`, `کولوکیشن`, `اجاره رک`, `سرور اختصاصی`, `سرور ابری`, `زیرساخت ابری`, `ابر خصوصی`, `گواهینامه رتبه‌بندی`, `ممیزی مرکز داده`, `شبکه ملی اطلاعات`, `ابر دولت`.
- Common failure mode: resellers advertise "Iran server / Tehran datacenter" without owning the facility. Record reseller pages only as **C leads**; pivot to the actual network/operator name, AS number, address, CRA license, or official facility page.

---

## 1. Primary and quasi-primary sources

### 1.1 Communications Regulatory Authority (CRA) license holders (Grade A)

- CRA "license holders" page: https://www.cra.ir/Portal/View/Page.aspx?PageId=6cc5b5bb-ee32-494f-b2c5-00494e81abba
- CRA service desk / license services: https://www.cra.ir/195 and https://www.cra.ir/service-desk/license/

Use CRA for the licensed telecom/operator universe, especially FCP and other communications-service licensees. It is an operator census, not a facility census. Key operators to pivot from CRA and RIPE records include Asiatech, Pars Online, Afranet, HiWEB, Shatel, Pishgaman, Fanava, Datak, Respina, Mobinnet, Irancell, MCI, and TCI.

Queries:

```text
site:cra.ir "دارندگان پروانه" "FCP" "{operator_fa}"
site:cra.ir "ایجاد و بهره برداری از شبکه ارتباطات ثابت" "{operator_fa}"
site:cra.ir "پروانه" "مرکز داده" OR "مراکز داده"
"{operator}" "FCP license" "Iran" "data center"
"{operator_fa}" "پروانه" "سازمان تنظیم مقررات" "دیتاسنتر"
```

### 1.2 Information Technology Organization of Iran / DCAS audit and cloud-provider programs (Grade A/B)

- ITOI / Ministry ecosystem: https://ito.gov.ir/ and https://www.ict.gov.ir/
- Government service surface mentioning datacenter service-provider ranking certificate: https://khadamat.mardom.ir/Service/Details?ServiceId=190918084538
- DCD reported in July 2025 that ITOI sought at least three cloud providers for government agencies: https://www.datacenterdynamics.com/en/news/iran-seeks-cloud-computing-providers-for-government-agencies/
- Persian coverage of cloud-provider identification/screening: https://www.aftana.ir/news/20748/

Use ITOI/ICT/official service pages to find:

- `گواهینامه رتبه‌بندی ارائه‌دهندگان خدمات مرکز داده` (ranking certificate for datacenter service providers).
- `ممیزی مراکز داده` / DCAS audit references.
- Government-cloud qualification calls: `ابر دولت`, `فراهم‌کنندگان خدمات ابری`, `ارائه‌دهندگان خدمات پرظرفیت مراکز داده`.

Queries:

```text
site:ito.gov.ir "مرکز داده" "گواهینامه رتبه‌بندی"
site:ito.gov.ir "فراهم‌کنندگان خدمات ابری"
site:ict.gov.ir "ابر دولت" "مرکز داده"
site:khadamat.mardom.ir "گواهینامه رتبه‌بندی ارائه‌دهندگان خدمات مرکز داده"
"گواهینامه رتبه بندی ارائه دهندگان خدمات مراکز داده" "{operator_fa}"
"ممیزی مراکز داده" "{operator_fa}" "سازمان فناوری اطلاعات"
```

### 1.3 Operator official pages (Grade A for existence/services; B for capacity)

Operator pages often give the best durable evidence for facilities and cities, but capacity is usually marketing-rounded. Use contact/address pages, service pages, and incident reports to separate owned sites from partner sites.

| Operator / cloud | Primary URLs | Location / enumeration signal | Grade notes |
|---|---|---|---|
| **ArvanCloud / Abr Arvan** | https://www.arvancloud.ir/fa ; VPS Iran page https://www.arvancloud.ir/fa/products/vps/iran ; docs https://docs.arvancloud.ir/fa/cloud-server/instance/datacenter-plans/ | Official page states 40 PoP sites in 30+ countries and 4 datacenters in Iran; VPS Iran page names Iranian datacenters in **Tabriz, Isfahan, Tehran**. Product pages include named DCs such as Bamdad and Shahriar. | A for product availability/city; B for ownership/capacity unless exact facility details appear. |
| **Afranet** | English datacenter page https://afranet.ir/en/services/datacenter ; Persian page https://afranet.ir/fa/services/datacenter ; contact https://afranet.ir/en/contact | Tehran operator with colocation, dedicated server, cloud, GPU services. Contact page gives central office on Dr. Beheshti/Sahand St. | A for services/address; B for rack classes/capacity. |
| **Pars Online** | https://www.parsonline.com/ ; about page https://www.parsonline.com/about-us/ | Official site advertises datacenter, hosting, co-location, dedicated server, cage, and cloud services; Tehran office now under HiWEB group address. | A for service/operator; verify exact facility via directories/press. |
| **Asiatech / cloud.ir** | https://asiatech.ir/ ; https://cloud.ir/ ; Milad Tower press example https://www.tasnimnews.ir/fa/news/1396/04/31/1471195/ | National datacenter in **Milad Tower, Tehran** reported at opening as >900 sqm; cloud.ir is the product pivot. | B+ for older press; seek operator/current page for live status. |
| **Mobinnet** | Business datacenter page https://business.mobinnet.ir/data-center ; about https://mobinnet.ir/p/5021/ | Official pages describe rack rental, VDC/private cloud, and a central datacenter. | A for services; location/capacity often undisclosed. |
| **Irancell** | Datacenter/hosting https://business.irancell.ir/p/14542/ ; cloud services https://business.irancell.ir/p/4808/ ; IaaS https://business.irancell.ir/p/28743/ | Mobile operator enterprise datacenter and cloud services. Commercial cloud launch covered by official Irancell page. | A for service existence; verify facility location separately. |
| **MCI / Hamrah-e Aval** | News example https://mci.ir/news/-/view/926440 and https://mci.ir/news/-/view/926245 | Officially announced the largest west/northwest datacenter outside the capital in **Tabriz, East Azerbaijan** in 2020. | A for opening/status at announcement; update with current MCI/press search. |
| **TCI / Mokhaberat** | https://www.tci.ir/ plus provincial TCI pages | Legacy telecom and government/enterprise datacenters; often provincial and poorly indexed. | A when official provincial TCI source; otherwise B/C. |
| **Shatel / Pishgaman / HiWEB / Fanava / Respina / Datak / SabaNet** | operator sites + CRA + RIPE/PeeringDB | Important FCP/ISP pivots; may operate hosting/colo or partner-hosted services. | A for licensed operator, B/C until facility page found. |
| **Amin IDC / Chakavak / HostIran / Pars Data / Mahan Server / SamaPardaz / Radcom / Abre Nik** | official sites and DCAS/certification pages | Smaller commercial hosting/cloud/datacenter operators and resellers; useful for non-Tehran leads and certification breadcrumbs. | A for own pages; C for reseller location claims without operator proof. |

Operator query patterns:

```text
site:{operator-domain} ("مرکز داده" OR "دیتاسنتر" OR "فضای دیتاسنتر" OR "کولوکیشن")
site:{operator-domain} ("سرور ابری" OR "زیرساخت ابری" OR "ابر خصوصی") ("تهران" OR "تبریز" OR "اصفهان" OR "شیراز")
site:{operator-domain} ("گواهینامه رتبه‌بندی" OR "ممیزی مرکز داده" OR "DCAS")
"{operator_fa}" ("افتتاح" OR "بهره‌برداری" OR "راه‌اندازی") ("مرکز داده" OR "دیتاسنتر")
"{operator_fa}" ("رک" OR "اجاره رک" OR "فضای رک" OR "کولوکیشن") ("SLA" OR "Tier" OR "استاندارد")
"{operator}" "Uptime Institute" "Iran"
"{operator}" "RIPE" "FCP license" "Iran"
```

---

## 2. Trade press, associations, and directories

### 2.1 Persian ICT / business press (Grade B)

Use these for discovery, launch dates, project names, executive quotes, and cross-checks against operator pages:

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Peivast | https://peivast.com/ | Strongest Iranian digital-economy press; good for `ابر دولت`, ITOI policy, operator launches, market context. | B |
| CITNA | https://www.citna.ir/ | ICT/telecom event coverage; useful for launches, photo reports, ministry quotes. | B |
| Digiato | https://digiato.com/ | Startup/cloud coverage; good for ArvanCloud product/DC launches. | B |
| Zoomit | https://www.zoomit.ir/ | Tech press; useful for ArvanCloud, datacenter ranking policy, cloud product updates. | B |
| ITMen | https://www.itmen.ir/ | ICT trade/news; useful for cloud/data-center controversy and project context. | B-/C+ |
| Tasnim / Mehr / Fars / IRNA / ISNA | official-ish news agencies | Useful for opening ceremonies and ministerial statements; often repeats PR. | B |
| Way2Pay / Donya-e-Eqtesad | https://way2pay.ir/ ; https://donya-e-eqtesad.com/ | Banking/cloud and listed-company context. | B-/C+ |
| Aftana | https://www.aftana.ir/ | Security/cloud policy, ITOI calls, local cyber/cloud reports. | B-/C+ |

Press queries:

```text
site:peivast.com "مرکز داده" "ابر دولت"
site:peivast.com "فراهم‌کنندگان خدمات ابری"
site:citna.ir "دیتاسنتر" "{operator_fa}" "{province_fa}"
site:digiato.com "دیتاسنتر" "ابر آروان" OR "ایرانسل" OR "مبین‌نت"
site:zoomit.ir "دیتاسنتر" "آروان" OR "رتبه‌بندی مراکز داده"
site:itmen.ir "دیتاسنتر" "ابر ایران"
site:tasnimnews.ir "دیتاسنتر" "افتتاح" "تهران" OR "تبریز"
site:mehrnews.com "ارائه دهندگان خدمات پرظرفیت مراکز داده"
```

### 2.2 Associations / communities (Grade B/C)

- Iranian ICT Guild / IranNSR (`سازمان نظام صنفی رایانه‌ای کشور`) is the main private-sector ICT association. LinkedIn states it has 27k+ members across 30 provinces and is the legal interface between government and private ICT: https://ir.linkedin.com/company/iranian-ict-guild-nasr . Use it for association events, DCAS/ranking discussions, and provincial ICT-company leads, not facility proof.
- Search the national and provincial ICT Guild pages for `مرکز داده`, `دیتاسنتر`, `ابر`, and `مراکز داده`. Provincial branches can reveal local operators that do not rank in English search.

Queries:

```text
"سازمان نظام صنفی رایانه‌ای" "مرکز داده" "{province_fa}"
"نصر" "{province_fa}" "دیتاسنتر"
"انجمن شرکت‌های انفورماتیک" "مرکز داده" "ابر"
"datacenter@irannsr.org" "مرکز داده"
```

### 2.3 Directories and network intelligence (Grade C leads; sometimes B for address)

- DataCenterMap Iran: https://www.datacentermap.com/iran/ . Useful market count and old facility pages; cross-check every facility.
- Cloudscene Iran: https://cloudscene.com/market/iran/all . Lists Pars Online and Afranet in Tehran and service categories.
- Data Center Platform Iran: https://datacenterplatform.com/countries/iran/ and Afranet example https://datacenterplatform.com/data-centers/afranet/ .
- Datacenters.com / Inflect / Baxtel / Cloudscene / PeeringDB / RIPEstat / bgp.tools / bgp.he.net: useful for facility aliases, ASNs, carrier-neutral signals, and addresses.

Directory/network queries:

```text
site:datacentermap.com/iran/ "{city_en}" "{operator}"
site:cloudscene.com/market/iran "{operator}"
site:datacenterplatform.com "Iran" "{operator}" "data center"
site:peeringdb.com "Tehran" "data center"
site:bgp.he.net "{operator}" "Iran"
site:ripe.net "{operator}" "Tehran" "FCP license"
```

---

## 3. Cloud-region and product-page handling

### 3.1 Foreign hyperscalers

Official AWS/Azure/GCP/Oracle region pages are **A evidence for no listed Iran public region** as of this research. Do not infer an Iranian facility from edge PoPs, sanctions reporting, reseller marketing, or regional Gulf cloud activity.

Negative-check queries:

```text
site:aws.amazon.com/about-aws/global-infrastructure Iran "Region"
site:learn.microsoft.com/azure/reliability "Iran" "region"
site:cloud.google.com/about/locations "Iran"
site:oracle.com/cloud/public-cloud-regions "Iran"
"AWS" "Iran" "data center" -Bahrain -UAE -Saudi
"Azure" "Iran" "datacenter region"
"Google Cloud" "Iran" "region"
"Oracle Cloud" "Iran" "public cloud region"
```

### 3.2 Domestic cloud regions / availability zones

Domestic providers use region/AZ-like product language. Treat it as facility lead evidence, then verify the underlying datacenter.

High-signal examples:

- ArvanCloud official VPS Iran page names Iranian datacenter cities **Tabriz, Isfahan, Tehran** and its main page says it has 4 datacenters in Iran: https://www.arvancloud.ir/fa/products/vps/iran and https://www.arvancloud.ir/fa .
- ArvanCloud product/press pages name DCs such as **Bamdad** and **Shahriar**; Persian trade press reported Bamdad in the Payam Special Economic Zone and a roadmap including Tehran, Tabriz, Isfahan, Shiraz, and Ahvaz: https://digiato.com/article/2022/04/17/opening-bamdad-data-center and https://www.zoomit.ir/tech-iran/381284-arvan-launches-bamdad-datacenter/ .
- Afranet, Mobinnet, Irancell, Pars Online, Asiatech/cloud.ir, and other FCPs sell IaaS/VDC/cloud-server products that imply datacenter infrastructure but may not expose physical location.

Domestic-cloud queries:

```text
"{operator_fa}" ("Availability Zone" OR "AZ" OR "ناحیه" OR "ریجن" OR "Region") "ایران"
"{operator_fa}" ("سرور ابری" OR "زیرساخت ابری") ("تهران" OR "تبریز" OR "اصفهان" OR "شیراز" OR "اهواز")
"ابر آروان" ("فروغ" OR "سیمین" OR "بامداد" OR "شهریار" OR "سهراب" OR "سعدی" OR "قیصر")
"cloud.ir" "دیتاسنتر" "برج میلاد" OR "میرعماد"
"ایرانسل" "زیرساخت ابری" "دیتاسنتر"
"مبین‌نت" "VDC" "مرکز داده"
```

---

## 4. Province-by-province enumeration approach

Use the repo's exact division labels, but search with Persian province/city names. For every province, run the generic Persian templates plus the local anchors below. If there is no result, document a negative search with `no_projects: true` only after checking CRA/FCP operators, provincial ICT Guild, provincial ICT office, and major cities.

Generic templates:

```text
"{province_fa}" ("مرکز داده" OR "دیتاسنتر" OR "دیتا سنتر" OR "مرکزداده")
"{city_fa}" ("مرکز داده" OR "دیتاسنتر") ("افتتاح" OR "بهره‌برداری" OR "راه‌اندازی" OR "احداث" OR "ساخت")
"{city_fa}" ("سرور ابری" OR "زیرساخت ابری" OR "کولوکیشن" OR "اجاره رک")
"{province_fa}" "سازمان نظام صنفی رایانه‌ای" ("مرکز داده" OR "ابر")
"{province_fa}" "اداره کل ارتباطات و فناوری اطلاعات" ("مرکز داده" OR "ابر" OR "شبکه ملی اطلاعات")
site:{province_governor_or_ict_domain} ("مرکز داده" OR "دیتاسنتر" OR "ابر دولت")
```

| Repo division | Persian search names | Priority anchors / method |
|---|---|---|
| Markazi | مرکزی، اراک | Search Arak industrial/telecom and provincial ICT office; likely government/enterprise DR rather than public colo. |
| Gilan | گیلان، رشت | DataCenterMap lists Rasht market; search Rasht hosters, TCI/Mokhaberat Gilan, ICT Guild Gilan. |
| Mazandaran | مازندران، ساری، بابل، آمل | Search provincial ICT and bank/health/government datacenter terms; public colo likely sparse. |
| East Azerbaijan | آذربایجان شرقی، تبریز | High priority. MCI opened west/northwest datacenter in Tabriz; ArvanCloud Shahriar/Tabriz appears on official product pages. |
| West Azerbaijan | آذربایجان غربی، ارومیه | Search Urmia + ICT office + telco datacenter; expect few public colo results. |
| Kermanshah | کرمانشاه | Search west-region disaster recovery, MCI/TCI, local government cloud. |
| Khuzestan | خوزستان، اهواز | ArvanCloud roadmap/press mentioned Ahvaz/Qeisar; search Ahvaz energy/industrial users, TCI/Irancell, and provincial ICT. |
| Fars | فارس، شیراز | High priority. DataCenterMap lists Shiraz market; ArvanCloud roadmap/product references Shiraz/Saadi. Search local hosters and ICT Guild Fars. |
| Kerman | کرمان | Search Kerman ICT/industrial/mining datacenter, public-sector DC, and crypto-mining false positives. |
| Central Khorasan | خراسان رضوی، مشهد | Repo label likely means Khorasan Razavi. Search Mashhad as a major market, ICT Guild Khorasan Razavi, TCI/hosting providers. |
| Isfahan | اصفهان | High priority. DataCenterMap lists Isfahan; ArvanCloud official VPS page names Isfahan; search Sahrab/Isfahan cloud and local hosters. |
| Sistan and Baluchestan | سیستان و بلوچستان، زاهدان، چابهار | Search Chabahar/free-zone telecom, Zahedan government DC, and national network nodes; many results may be telecom POPs. |
| Kurdistan | کردستان، سنندج | Search provincial ICT/government cloud and TCI; beware Iraqi Kurdistan false positives in English. |
| Hamadan | همدان | DataCenterMap lists Hamedan market; search local hosters/TCI and provincial ICT. |
| Chaharmahal and Bakhtiari | چهارمحال و بختیاری، شهرکرد | Search Shahrekord public-sector/ICT; likely negative unless government DC. |
| Lorestan | لرستان، خرم‌آباد | Search provincial ICT, TCI, government service datacenter. |
| Ilam | ایلام | Search local ICT/TCI; likely negative or edge/DR only. |
| Kohgiluyeh and Boyer-Ahmad | کهگیلویه و بویراحمد، یاسوج | Search Yasuj government/ICT; likely negative. |
| Bushehr | بوشهر، عسلویه | Search energy/industrial datacenter, port/special-zone ICT, TCI; exclude unrelated oil/gas control rooms unless compute facility. |
| Zanjan | زنجان | Search provincial ICT, industrial parks, TCI. |
| Semnan | سمنان | Search Semnan ICT, industrial/mining/crypto false positives, TCI. |
| Yazd | یزد | Search Yazd ICT, industrial/mining/crypto false positives, local hosting. |
| Hormozgan | هرمزگان، بندرعباس، کیش، قشم | Search port/free-zone/cable/telecom hubs, Kish/Qeshm datacenter claims; verify commercial facility vs enterprise server room. |
| Tehran | تهران، کرج? | Highest priority for Tehran proper. Operators: Afranet, Pars Online, Asiatech/Milad Tower, ArvanCloud Tehran DCs, Irancell, Mobinnet, Shatel, Respina, Fanava, Datak, Mahan Server, SamaPardaz. Avoid assigning Alborz/Karaj sites to Tehran. |
| Ardabil | اردبیل | Search local ICT/TCI; likely negative. |
| Qom | قم | DataCenterMap lists Qom market; search Qom hosters, seminary/government DC, ICT Guild Qom. |
| Qazvin | قزوین | Search industrial corridor/datacenter, TCI, provincial ICT. |
| Golestan | گلستان، گرگان | Search Gorgan ICT/TCI. |
| North Khorasan | خراسان شمالی، بجنورد | Search Bojnurd ICT/TCI; likely negative. |
| South Khorasan | خراسان جنوبی، بیرجند | Search Birjand ICT/TCI; likely negative. |
| Alborz | البرز، کرج، پیام، منطقه ویژه اقتصادی پیام | High priority. ArvanCloud Bamdad was reported in Payam Special Economic Zone; search Karaj/Payam cloud and DCAS/certification evidence. |

---

## 5. Verification and grading recipe

1. **Start with operator universe**: CRA license holders + major FCP/mobile operators + IranNSR provincial members. This finds names even where facility pages are weak.
2. **Seed known facility markets**: DataCenterMap/Cloudscene/Data Center Platform for Tehran, Isfahan, Rasht, Shiraz, Hamedan, Qom, then cross-check with official pages or press.
3. **Run vendor sweeps**: ArvanCloud, Afranet, Pars Online, Asiatech/cloud.ir, Mobinnet, Irancell, MCI, TCI, Shatel, HiWEB, Respina, Fanava, Pishgaman, HostIran/ParsData, Mahan Server/SamaPardaz/Amin/Chakavak.
4. **Extract facility evidence**: city, address or named campus, status verb, service type, owner/operator, capacity/racks/sqm/power if present, and whether the claim is owned facility vs reseller/tenant.
5. **Cross-check through network evidence**: RIPE/PeeringDB/ASNs, looking glasses, Cloudflare Radar/Arvan Radar, and BGP prefixes can confirm operator presence but should not be used alone for physical facility inventory.
6. **Grade per data point**:
   - **A**: CRA/ITOI/official government service, operator facility/service page, official company news, official MCI/Irancell/Mobinnet/Afranet/Arvan pages, formal certification page.
   - **B**: Peivast/CITNA/Digiato/Zoomit/Tasnim/Mehr/Fars/IRNA/ISNA, DCD, strong opening-event coverage, exchange/company report, Uptime certificate.
   - **C**: DataCenterMap/Cloudscene/Datacenters.com/Inflect directories, reseller pages, social posts, SEO hosting pages, market-research summaries.

Pitfalls:

- `ابر` can mean cloud software/SaaS, storage, or CDN rather than a physical datacenter.
- `مرکز داده سازمانی` may be an enterprise server room, not a commercial colo facility.
- Crypto-mining and GPU/HPC announcements can look like datacenters; require hosting/colo/cloud service evidence before counting.
- Persian dates use the Solar Hijri calendar; convert dates before comparing lifecycle events.
- In English, "Kurdistan" often returns Iraq/KRG; add `Iran`, `Sanandaj`, or `کردستان ایران`.
- Sanctions and national-network politics create biased reporting around ArvanCloud and government cloud. Use source grading and record exact claim/status, not inference.

