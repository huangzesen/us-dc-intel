# IR Explorer — Official / Regulatory / Cloud Pipeline for Iran Datacenter Enumeration

Date: 2026-08-12. Scope: practical methodology to enumerate datacenter projects and operating sites in Iran using official/regulatory sources first, then cloud/operator/trade-press corroboration. Reliability grades: **A** = official/primary, **B** = strong secondary or operator self-disclosure, **C** = weak/aggregate lead only.

---

## 0. Country-Specific Structure

- Iran does **not** have a single open national planning-permit database comparable to UK/US municipal portals. Building permits are municipal, land-use approvals are fragmented, and telecom/cloud authorization is split across ICT regulators and government service portals. Enumerate by combining telecom licenses, ITO datacenter/rating records, state datacenter projects, power/grid signals, operator pages, and province/city Persian searches.
- The strongest official technology trail is from the **Ministry of ICT ecosystem**: CRA/Ratel license holders, Iran Information Technology Organization (ITO) datacenter rating and cloud-service programs, Telecommunication Infrastructure Company (TIC) / IXP announcements, provincial ICT directorates, and MCI/TCI/ISP official announcements.
- Many historic provincial "مرکز داده استان" records are **government / National Information Network (NIN)** facilities, usually small by global colocation standards. Count them as facilities only when the source confirms racks, servers, operator, or operational status; otherwise keep as government-infrastructure leads.
- Modern private-sector capacity is concentrated around **Tehran / Alborz / Qom / Isfahan / Fars / East Azerbaijan / Khorasan Razavi / Khuzestan / Hamadan**, matching Tehran demand, IXP locations, provincial cloud-overhaul sites, and major carrier/ISP footprints.
- Use Persian terms first. English searches miss most official pages.

---

## 1. Persian and English Query Vocabulary

Core facility terms:

```text
مرکز داده
دیتاسنتر
دیتا سنتر
مرکز داده استانی
مرکز داده ملی
زیرساخت ابری
رایانش ابری
ابر ایران
خدمات مرکز داده
کولوکیشن
میزبانی سرور
اشتراک مکانی
مرکز تبادل ترافیک
IXP
NIX
```

Lifecycle / evidence terms:

```text
افتتاح
بهره برداری
راه اندازی
احداث
توسعه
فاز دوم
مزایده
مناقصه
فراخوان
قرارداد BOT
گواهینامه رتبه‌بندی
پروانه بهره‌برداری
پروانه
مجوز
تعرفه برق
مصرف برق
انشعاب برق
مولد اضطراری
پست برق
```

English fallbacks:

```text
"Iran" "data center" "Tehran" colocation
"Iran" "cloud" "data center" Asiatech OR Afranet OR Pars Online OR Shatel
"Iran Cloud" "data centers" "Information Technology Organization"
"Iran" "Internet Exchange" Tehran Mashhad Shiraz Tabriz
```

---

## 2. Highest-Value Official Sources

### 2.1 CRA / Ratel License Holders — operator census, not facility census

- **Communications Regulatory Authority (CRA / سازمان تنظیم مقررات و ارتباطات رادیویی)** license holders page: https://www.cra.ir/Portal/View/Page.aspx?PageId=6cc5b5bb-ee32-494f-b2c5-00494e81abba
- CRA main services / licensing portal: https://www.cra.ir/195
- What it gives: licensed telecom/ICT operators. For datacenter enumeration, use it to seed FCP, Servco, PAP, mobile, and fixed operators that may run datacenters or cloud/colocation services. It does **not** reliably list each datacenter building.
- Query patterns:

```text
site:cra.ir "دارندگان پروانه" "FCP" "آسیاتک"
site:cra.ir "دارندگان پروانه" "شاتل"
site:cra.ir "پروانه" "مرکز داده"
site:cra.ir "شماره پروانه" "دیتاسنتر"
"شماره پروانه" "سامانه ۱۹۵" "دیتاسنتر"
```

Grade: **A** for company authorization, **C** for facility existence unless linked to an operator facility page or filing.

### 2.2 Iran Information Technology Organization (ITO) — datacenter rating and Iran Cloud

- ITO official site: https://ito.gov.ir/
- Government service page for "گواهینامه رتبه‌بندی ارائه‌دهندگان خدمات مرکز داده" appears in the national government-service catalog: https://khadamat.mardom.ir/Service/Details?ServiceId=190918084538
- ITO-related reporting says datacenter evaluation/rating registration was to be connected to the **National Licenses Portal** and that ITO began rating public and private datacenters. Use this as a named-provider lead source, then verify the named center on official/operator pages.
- Search patterns:

```text
site:ito.gov.ir "رتبه‌بندی" "مرکز داده"
site:ito.gov.ir "گواهینامه رتبه‌بندی" "مرکز داده"
site:ito.gov.ir "ابر ایران" "دیتاسنتر"
site:khadamat.mardom.ir "گواهینامه رتبه‌بندی" "مرکز داده"
"گواهینامه رتبه‌بندی ارائه‌دهندگان خدمات مرکز داده" "سازمان فناوری اطلاعات"
```

Grade: **A** for certificate/service existence and named recipients on official ITO/gov pages; **B** for media copies of award ceremonies.

### 2.3 National Licenses Portal / business permits

- National Licenses Portal: https://mojavez.ir/ (historically G4B / درگاه ملی مجوزها)
- This is a useful route for permit categories and status proof, not a clean searchable datacenter map. Search both the portal and indexed QR/tracking pages.
- Query patterns:

```text
site:mojavez.ir "مرکز داده"
site:mojavez.ir "دیتاسنتر"
site:mojavez.ir "خدمات مرکز داده"
"درگاه ملی مجوزها" "مرکز داده"
"درگاه ملی مجوزها" "گواهینامه رتبه‌بندی" "مرکز داده"
```

Grade: **A** when it returns a specific license/certificate record; otherwise use as regulatory context.

### 2.4 Ministry of ICT and provincial ICT directorates — state datacenters and IXP anchors

- Ministry of ICT: https://www.ict.gov.ir/
- Provincial subdomains often mirror or preserve local announcements, e.g. `ostanha.ict.gov.ir`, `zanjan.ict.gov.ir`, `yazd.ict.gov.ir`, `wa.ict.gov.ir`.
- Verified useful examples:
  - Ministry ICT article on Tabriz datacenter: https://www.ict.gov.ir/fa/newsagency/24406/ — states MCI opened the largest west/northwest datacenter in Tabriz with 3,000 m2, 250 racks expandable to 350, 1,500 physical servers, and 16,000 virtual servers.
  - Ministry ICT article on IXP launches in Mashhad, Shiraz, and Tabriz: https://www.ict.gov.ir/fa/news/19522/
  - Ministry/provincial articles for Qom, Semnan, Yazd, Hamadan, Golestan, Zanjan, Birjand and other provinces appear under `ict.gov.ir` and provincial ICT domains.
- Query patterns:

```text
site:ict.gov.ir "مرکز داده استان" "{استان}"
site:ostanha.ict.gov.ir "مرکز داده" "{استان}"
site:{province_subdomain}.ict.gov.ir "مرکز داده"
site:ict.gov.ir "مرکز تبادل ترافیک" "{شهر}"
site:ict.gov.ir "دیتاسنتر" "همراه اول" "{شهر}"
```

Grade: **A** for official opening/status and stated rack/server counts; treat old announcements as needing current operator confirmation.

### 2.5 Telecommunication Infrastructure Company / IXPs

- TIC official site: https://www.tic.ir/
- IXPs are not datacenters, but in Iran they are strong geography anchors because local content/cloud/datacenter programs cluster around Tehran, Mashhad, Shiraz, Tabriz, Isfahan, Qom, and Ahvaz.
- Query patterns:

```text
site:tic.ir "مرکز تبادل ترافیک" "{شهر}"
site:ict.gov.ir "مرکز تبادل ترافیک داخلی" "تهران" "مشهد" "شیراز" "تبریز"
"IXP" "Iran" "Mashhad" "Shiraz" "Tabriz"
```

Grade: **A** for IXP existence/location; **B/C** only as a proxy for nearby datacenter potential.

### 2.6 Power / energy evidence

- Tavanir news / Ministry of Energy distribution-company pages: https://news.tavanir.org.ir/
- Tavanir has public discussion of datacenter, AI, and crypto loads; one Tavanir article states electricity consumption for datacenters, AI, and crypto is expected to double over five years and emphasizes renewables and backup generation.
- Search national and local distribution-company pages. Most useful signals are new substations, dedicated feeds, consumption-management notices, or large standby-generation references.

```text
site:news.tavanir.org.ir "مرکز داده" "مصرف برق"
site:news.tavanir.org.ir "هوش مصنوعی" "مرکز داده"
site:news.tavanir.org.ir "دیتاسنتر" "برق"
site:{regional_power_site} "مرکز داده" "انشعاب"
"مرکز داده" "پست برق" "{شهر}"
"دیتاسنتر" "مولد اضطراری" "{استان}"
```

Grade: **A** for official power-system statements and project interconnection notices; **B** for press interviews without project identifiers.

### 2.7 Environmental / land / construction permits

- Department of Environment: https://www.doe.ir/ and province subdomains such as `gilan.doe.ir`, `mazandaran.doe.ir`, `markazi.doe.ir`.
- Land Management single-window references appear in government digital-service reporting. Search it as context, but expect limited public data for specific datacenters.
- Municipal construction-permit portals are city-specific and usually not full-text public. For Tehran and major cities, search municipal law/budget/permit pages for "مرکز داده" and the operator/campus name; do not expect a complete project list.

```text
site:doe.ir "مرکز داده" "ارزیابی اثرات زیست محیطی"
site:environment.ir "مرکز داده" "ارزیابی"
site:{province}.doe.ir "مرکز داده"
site:tehran.ir "مرکز داده" "پروانه ساختمانی"
site:tehran.ir "دیتاسنتر" "مجوز"
"پنجره واحد مدیریت زمین" "مرکز داده"
"پروانه ساختمانی" "دیتاسنتر" "{شهر}"
```

Grade: **A** if a specific environmental/building permit is found; in practice these sources are sparse for datacenter enumeration.

---

## 3. Official Cloud / Operator Pipeline

### 3.1 Global hyperscalers

Official public-region pages for AWS, Azure, Google Cloud, and Oracle list Middle East regions but no Iran public cloud region as of 2026-08-12:

- AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/ and AWS regions table: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

Use these as **negative controls**: do not infer AWS/Azure/GCP/OCI datacenters in Iran from regional Middle East presence. Any Iran cloud evidence should come from domestic providers or government cloud programs.

### 3.2 Domestic cloud / colo players to sweep

Use official pages first, then cross-check CRA/ITO/trade press.

| Operator / brand | Main source pattern | Notes | Grade |
|---|---|---|---|
| ArvanCloud / ابر آروان | https://www.arvancloud.ir/ and docs https://docs.arvancloud.ir/ | Official docs mention region/datacenter/zone concepts; app docs showed "بامداد" and "شهریار" regions; the Iran Cloud page explains the ITO BOT project and names the private winners. | B for self-disclosed cloud regions; A only when paired with ITO/gov contract |
| Asiatech / آسیاتک | `site:asiatech.ir دیتاسنتر`, plus official corporate/licensing pages | Known Tehran/Milad Tower datacenter references; Iran Cloud participant; search for "تراز 10-" and "برج میلاد". | B; A if official or listed-company disclosure |
| Afranet / افرانت | https://www.afranet.com/en and `site:afranet.com datacenter` | Official site advertises colocation, cloud, and datacenter services. Also known datacenter rating recipient in press. | B |
| Pars Online / پارس آنلاین | https://www.parsonline.com/ | Official home page advertises datacenter and hosting services; acquired by HiWEB historically, so verify current ownership/brand. | B |
| Shatel / شاتل | https://www.shatel.ir/b2b/data-center/colocation/ | Official colocation page; footer shows CRA license and 195 reference; customer quotes mention Tehran/Shiraz links and Payam Special Economic Zone. | B |
| MCI / Hamrah-e Aval / همراه اول | https://mci.ir/ and ICT ministry pages | Official Tabriz datacenter is strong facility seed; also search Mashhad, Tehran, Shiraz, Ahvaz. | A/B |
| TCI / مخابرات ایران | https://www.tci.ir/ | Search province-specific telecom pages for "مرکز داده" and "مخابرات منطقه". | B |
| Mobinnet / مبین‌نت | https://www.mobinnet.ir/ | ISP with datacenter services; parent MCI. | B |
| HostIran / هاست ایران | https://hostiran.net/datacenter | Says Tehran datacenter and rating status; verify against ITO. | B |
| Amin IDC / مرکز داده امین | https://www.aminidc.com/ | Rating-certificate recipient; search for GPU/cloud expansion. | B |
| Tebyan / تبیان, Respina / رسپینا, Sefroyek / صفرویک, Noor IDC / نور | official pages + CRA/ITO | Mostly Tehran/major-city colocation; use as operator seed list. | B/C until verified |

Operator query templates:

```text
site:{operator_domain} "دیتاسنتر"
site:{operator_domain} "مرکز داده"
site:{operator_domain} "کولوکیشن"
site:{operator_domain} "میزبانی سرور"
"{operator}" "گواهینامه رتبه‌بندی" "مرکز داده"
"{operator}" "شماره پروانه" "سامانه ۱۹۵"
"{operator}" "مرکز داده" "رک"
"{operator}" "مرکز داده" "مگاوات" OR "برق"
```

---

## 4. Iran Cloud / Government Cloud Enumeration

The "ابر ایران" project is a high-value source because it ties government-owned provincial datacenters to private cloud operators.

Known details from ArvanCloud's public Iran Cloud explainer (operator-side but detailed): contract between ITO and Asiatech, Zharfnegar, Abr ZS, ArvanCloud, and Fanap; selected from 20 applicants; intended to cloud/overhaul 10 existing datacenters; locations named include Tabriz, Ahvaz, Karaj, Isfahan, Shiraz, Mashhad, Qom, Hamadan, and Isfahan appears twice in that page's wording. Use this as a **lead list**, then verify each city through ICT/ITO tender, opening, or operator evidence.

Queries:

```text
"ابر ایران" "تبریز" "دیتاسنتر"
"ابر ایران" "اهواز" "دیتاسنتر"
"ابر ایران" "کرج" "دیتاسنتر"
"ابر ایران" "اصفهان" "دیتاسنتر"
"ابر ایران" "شیراز" "دیتاسنتر"
"ابر ایران" "مشهد" "دیتاسنتر"
"ابر ایران" "قم" "دیتاسنتر"
"ابر ایران" "همدان" "دیتاسنتر"
"شبکه ابری یکپارچه توزیع شده" "سازمان فناوری اطلاعات"
"مزایده" "ابر ایران" "دیتاسنتر"
```

Grade: **B** from operator explainer; upgrade to **A** when the specific facility is confirmed by ITO/ICT/TIC/tender records.

---

## 5. Province-by-Province Search Plan

Use the Persian province and capital names. For each province run the four searches below, then add city/operator terms from the notes.

Base template per province:

```text
site:ict.gov.ir "مرکز داده استان {province_fa}"
site:{ict_province_subdomain}.ict.gov.ir "مرکز داده"
"مرکز داده" "{province_fa}" "{capital_fa}" (افتتاح OR بهره‌برداری OR راه‌اندازی OR توسعه)
"دیتاسنتر" "{capital_fa}" (رک OR سرور OR کولوکیشن OR برق)
site:news.tavanir.org.ir "مرکز داده" "{province_fa}"
site:{province}.doe.ir "مرکز داده"
```

Priority table:

| Province | Persian | Capital / city terms | Why it matters / extra query terms |
|---|---|---|---|
| Tehran | تهران | تهران، برج میلاد، منطقه ویژه پیام | Primary market. Search Asiatech, Afranet, Pars Online, Shatel, HostIran, Amin, Tebyan, Respina, Arvan "بامداد/شهریار", Milad Tower. |
| Alborz | البرز | کرج، پیام، شهریار (near Tehran/Alborz edge) | Iran Cloud city lead; Payam Special Economic Zone and Tehran overflow. |
| Qom | قم | قم | Official provincial datacenter opening pages exist; IXP/NIN anchor. |
| Isfahan | اصفهان | اصفهان | Iran Cloud lead and IXP city; search municipal/ICT/province pages. |
| Khorasan Razavi | خراسان رضوی | مشهد | IXP city and Iran Cloud lead; search Mashhad cloud/datacenter and TIC/ICT. |
| East Azerbaijan | آذربایجان شرقی | تبریز | Strong official seed: MCI Tabriz datacenter, IXP, Iran Cloud lead. |
| Fars | فارس | شیراز | IXP and Iran Cloud lead; search Shatel/MCI/TIC/ICT pages plus "مرکز داده استان فارس". |
| Khuzestan | خوزستان | اهواز | IXP and Iran Cloud lead; hot power-grid province; search "اهواز دیتاسنتر" and power feeds. |
| Hamadan | همدان | همدان | Official provincial datacenter opening pages exist; Iran Cloud lead. |
| Markazi | مرکزی | اراک، ساوه، شهر صنعتی کاوه | Not a known DC hub; use industrial/power signals. Query "اراک مرکز داده", "ساوه دیتاسنتر", and Tavanir/industrial-estate terms. |
| Gilan | گیلان | رشت، انزلی | Likely smaller/enterprise facilities. Search provincial ICT, free-zone/port, and operator colocation pages. |
| Mazandaran | مازندران | ساری، بابل، آمل | Search provincial ICT and university/government datacenters; treat as low-confidence unless operator or permit backed. |
| Semnan | سمنان | سمنان | Official ICT opening page exists; verify current status. |
| Yazd | یزد | یزد | Official ICT opening/announcement pages exist; search provincial ICT archive. |
| Golestan | گلستان | گرگان | Official 2014 provincial datacenter opening article references multiple provinces. |
| South Khorasan | خراسان جنوبی | بیرجند | 2025 ICT article is more equipment manufacturing + datacenter lead; verify whether facility hosts third-party workloads. |
| Zanjan | زنجان | زنجان | Official ICT article references investment in provincial datacenter; verify operational stage. |
| Kerman | کرمان | کرمان | Historic provincial datacenter mention in multi-province opening; search ICT archive. |
| Ardabil | اردبیل | اردبیل | Lower priority; use ICT provincial directorate and municipal/company queries. |
| West Azerbaijan | آذربایجان غربی | ارومیه | Lower priority; search ICT/TIC/TCI province pages. |
| Kurdistan | کردستان | سنندج | Lower priority; search provincial ICT and e-government datacenter. |
| Kermanshah | کرمانشاه | کرمانشاه | Western-region backup to Tabriz/Hamadan; search MCI/TCI and ICT pages. |
| Lorestan | لرستان | خرم‌آباد | Low priority; government/enterprise datacenter searches. |
| Ilam | ایلام | ایلام | Low priority; search only official ICT/municipal first. |
| Chaharmahal and Bakhtiari | چهارمحال و بختیاری | شهرکرد | Low priority; search province ICT/DOE. |
| Kohgiluyeh and Boyer-Ahmad | کهگیلویه و بویراحمد | یاسوج | Low priority; official-only sweep. |
| Bushehr | بوشهر | بوشهر | Search port/energy/industrial records; distinguish telecom DC from oil/gas control rooms. |
| Hormozgan | هرمزگان | بندرعباس، قشم، کیش | Ports/free zones; search Kish/Qeshm cloud/colo, but beware office IT rooms. |
| Sistan and Baluchestan | سیستان و بلوچستان | زاهدان، چابهار | Search Chabahar/free-zone connectivity; likely sparse. |
| North Khorasan | خراسان شمالی | بجنورد | Low priority; official-only sweep. |
| Razavi-adjacent / other named cities | نیشابور، سبزوار | Only if operator pages mention them. |

Province subdomain guess pattern: many ICT provincial pages are not consistent. Try both `site:ict.gov.ir "{province}" "مرکز داده"` and `site:{shortcode}.ict.gov.ir`. Use search engine results to discover the exact subdomain rather than hard-coding.

---

## 6. Trade Press and Secondary Sources

Use these for discovery and status changes, then verify with official/operator records.

- **Peivast / پیوست**: https://peivast.com/ — strongest domestic tech-policy trade press. Search: `site:peivast.com دیتاسنتر`, `site:peivast.com "ابر ایران"`.
- **Digiato / دیجیاتو**: https://digiato.com/ — good on ArvanCloud/Asiatech incidents and cloud infrastructure context.
- **Zoomit / زومیت**: https://www.zoomit.ir/ — good on Iran Cloud, IXP, outages, domestic operator context.
- **IRNA / ایرنا**: https://www.irna.ir/ — semi-official news; useful for ITO statements. Example: datacenter ecosystem/rating article at https://www.irna.ir/news/85205898/
- **Mehr / مهر**, **Tasnim / تسنیم**, **Donya-e Eqtesad / دنیای اقتصاد** — useful for operator announcements and regulator quotes; grade by specificity.
- **Data Center Dynamics**: https://www.datacenterdynamics.com/ — English market overviews; one article notes Iran is a small market with DataCenterMap listing about 20 facilities and names MTN, Pars Online, Asiatech, Afranet.
- **DataCenterMap / Datacenters.com / Inflect** — aggregate facility leads only. Use to discover names/addresses, then verify from operator/official sources.

Grade: **B** for named project announcements from established press; **C** for aggregate lists and unsourced market reports.

---

## 7. Verification Rules

1. Record identity should be keyed by `(operator ultimate parent, facility/campus name, city/province, source date)`. Iran sources often mix brand names, legal company names, and government project labels.
2. Status hierarchy: `فراخوان/مزایده` < `قرارداد` < `احداث/توسعه` < `افتتاح/راه‌اندازی/بهره‌برداری` < operator service page with current sales/contact. Count operational only at the last two levels.
3. Capacity hierarchy: rack/server/m2/MW from official ICT/operator pages > tender/procurement > trade press > aggregate database. Prefer exact Persian numerals conversion; note if numbers are expandable design capacity.
4. Government provincial datacenters may be small NIN/e-government nodes, not commercial colocation. Mark owner/operator and use `notes` to avoid comparing them with commercial IDC capacity.
5. Power sanity checks matter. If a source claims large AI/cloud scale without a matching substation, interconnection, or generator/cooling story, keep confidence at **B/C**.
6. Do not count global hyperscaler nearby regions in UAE/Bahrain/Qatar/Saudi Arabia as Iran facilities.
7. Treat "cloud region" as a service geography, not a physical address, unless an official source names the datacenter/city.

---

## 8. Recommended Enumeration Workflow

1. **Operator seed:** pull CRA/Ratel license holders and known ISP/FCP names; add ITO datacenter rating recipients and Iran Cloud winners.
2. **Official facility seed:** search ICT/ITO/TIC for provincial datacenters, MCI/TCI datacenters, IXP-adjacent facilities, and Iran Cloud city records.
3. **Province sweep:** run the province table queries, starting with Tehran, Alborz, Qom, Isfahan, Khorasan Razavi, East Azerbaijan, Fars, Khuzestan, Hamadan, then Markazi/Gilan/Mazandaran and the remaining provinces.
4. **Power / permit sweep:** search Tavanir, regional distribution companies, DOE, municipality, and land-management terms for each candidate project.
5. **Operator confirmation:** search each candidate operator's official site for colocation/cloud pages, rack counts, facility photos, certificates, customer-access language, and license footer.
6. **Secondary fill:** use Peivast/Digiato/Zoomit/IRNA/DCD and aggregate databases to catch missed facilities; downgrade if no primary corroboration.
7. **Output fields:** `country_code=IR`, `country_name=Iran`, `division=province`, `city`, `name`, `operator`, `status`, `capacity_mw`, `racks`, `area_m2`, `source_urls`, `evidence_date`, `evidence_grade`, `notes`.

---

## 9. Quick Source Grade Summary

| Source | Grade | Use |
|---|---|---|
| CRA/Ratel license-holder pages | A for operator license | Build operator universe; not facility count |
| ITO / khadamat.mardom datacenter rating service | A for certificate/official service | Identify certified/rated datacenter providers |
| ICT ministry/provincial ICT announcements | A | Official facility openings, rack/server counts |
| TIC / IXP announcements | A for IXP | Geographic anchor for cloud/DC search |
| Tavanir / regional power companies | A for power facts | MW/interconnection plausibility |
| DOE / municipality / land portals | A if project-specific | Sparse but high-confidence permit evidence |
| Operator official pages | B, sometimes A- for current service | Existence, services, sometimes capacity/location |
| Peivast, Digiato, Zoomit, IRNA, Mehr, Tasnim, Donya-e Eqtesad | B | Discovery and event/status cross-check |
| DataCenterMap, Datacenters.com, Inflect, market reports | C | Lead generation only |

