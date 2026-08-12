# JO Explorer Industry - Jordan Datacenter Operator, Press, Vendor, Directory, and Query Methodology

Date reviewed: 2026-08-12. Country: **JO Jordan**. Division model: **12 governorates**: Ajloun, Amman, Aqaba, Balqa, Irbid, Jerash, Karak, Madaba, Ma'an, Mafraq, Tafilah, Zarqa.

Use `explorer-official.md` for TRC, MoDEE, MOIN, ASEZA, municipal permits, environment, power, official cloud-region checks, and A-grade official routes. This file focuses on industry-side discovery, operator/vender pivots, press triage, directories, Arabic/English query patterns, and per-governorate industry strategy.

## Reliability Grades

- **A**: official operator/project page, official customer/case-study page, official financier/project page, Uptime Institute/certifier record, listed-company disclosure, or primary government/regulator page. Treat operator capacity/Tier wording as an **operator claim** unless independently certified or utility-confirmed.
- **B**: established trade or national business press: DCD, Capacity, W.Media, Telecom Review, Developing Telecoms, Total Telecom, The Fast Mode, SAMENA Council, TechAfrica News, Zawya, MENAFN, Jordan Times, Roya, Al-Mamlaka, Al-Ghad, Al-Rai, Addustour, Ammon, Xinhua/Royal Court syndication, FANA, and intaj.net newsroom. Grade as **B+** when it clearly republishes named operator/official statements and the primary page is not available.
- **C**: DataCenterMap, datacenters.com, colocationm, datacentercatalog, Cloudscene, PeeringDB, Baxtel, ocolo, LinkedIn/social posts, market-report snippets, and generic consultant/vendor marketing without a named facility. Use as leads and alias maps only.

Grade individual claims separately. A directory can be C for address/capacity while an operator page is A for existence. A press story can be B for a quoted capacity ceiling but not proof of delivered load.

## Market Frame

Jordan is a compact, telco-led and carrier-neutral emerging data-center market:

- **Amman** is the commercial/government cluster: Orange Jordan, Zain Jordan, Umniah, MoDEE/NITC government hosting, banks/universities, and directory leads.
- **Aqaba** is the new strategic hub: Aqaba Digital Hub (ADH), data center plus open-access cable landing, AqabaIX/interconnection, cloud, cybersecurity, and EBRD-backed expansion.
- **Balqa** became a real second hub through Orange Jordan's Ain Al-Basha data center.
- **Irbid** has digital-platform, university, and industrial-estate leads but no confirmed commercial colo seed in the reviewed evidence.
- **Zarqa, Mafraq, Karak, Ma'an, Madaba, Tafilah, Jerash, Ajloun** are low-yield and require Arabic-first negative sweeps. Expect institutional IT, telco edge, or no project.

No official AWS, Azure, Google Cloud, or OCI page lists a Jordan public cloud region as of this review. Do not count Bahrain/UAE/Israel/Qatar/Saudi regional cloud regions as Jordan facilities. Local cloud brands must be tied to physical Jordan DC evidence.

## 1. Operator and Facility Seeds

| Operator / facility | URLs | Geography | Status and grading |
|---|---|---|---|
| **Aqaba Digital Hub (ADH)** | https://adh.jo/ ; https://adh.jo/hub ; https://adh.jo/hub/mega-data-center ; https://adh.jo/hub/city-data-center ; https://adh.jo/about/company ; https://adh.jo/about/newsroom ; https://www.ebrd.com/home/work-with-us/projects/psd/56562.html ; https://north-africa-middle-east-gulf.ec.europa.eu/news/ebrd-and-eu-support-expansion-aqaba-digital-hub-jordan-2026-05-07_en ; https://uptimeinstitute.com/component/tierachievement/datacenter/aqaba-digital-hub-data-center-data-hall-1--cls-unit/1718 | Aqaba. ADH official pages describe City Data Center and Mega Data Center; EBRD describes ADH as a data-centre, fibre, broadband-connectivity, and subsea-cable operator in Aqaba. | Operational/expanding. **A** for official/EBRD/Uptime existence, Aqaba location, facility/certification names, and financing. ADH claims Jordan's largest carrier-neutral data center, Tier III-certified infrastructure, cloud/colo/connectivity/cyber services. EU/EBRD says loan supports fit-out/expansion and second hall. Capacity figures must be stored exactly by source and phase. |
| **ADH customer DR / bank and fintech colocations** | https://adh.jo/about/newsroom/madfoatcom-selects-35d-cloud-safeguard-their-business-continuity and ADH newsroom | Aqaba | **A operator/customer lead** for disaster-recovery colocation use cases at ADH. Useful for confirming service availability, not separate facilities. |
| **Orange Jordan - Marj Al-Hammam Data Center** | https://orange.jo/sites/default/files/documents/hosting_data_centers.pdf ; https://uptimeinstitute.com/component/tierachievement/datacenter/marj-alhammam-data-center/830 ; https://uptimeinstitute.com/uptime-institute-awards/client/jordan-telecom-group--orange-jordan/532 | Amman | Operational. **A** for Orange hosting/data-center service brochure and Uptime certificate page; capacity/address from directories remains C unless corroborated. |
| **Orange Jordan - Hashem Data Center** | https://www.thefastmode.com/technology-solutions/40316-orange-jordan-s-hashem-data-center-earns-tier-iii-design-certification ; https://www.samenacouncil.org/samena_daily_news?news=104925 ; https://www.datacenters.com/orange-business-hashem | Amman / Medical City area per press and directories | **B+** for Tier III Design certification announcement from telecom press/SAMENA; **C** for directory address/capacity. Check Uptime list/client pages before accepting certificate status and facility alias. |
| **Orange Jordan - Ain Al-Basha Data Center** | https://intaj.net/orange-jordan-announces-the-inauguration-of-the-kingdoms-newest-most-sustainable-and-secure-data-center/ ; https://www.fananews.com/language/en/minister-of-digital-economy-opens-orange-jordans-data-centre-in-ain-al-basha/ | Ain Al-Basha, Balqa; near Al-Baqa'a/Salt search geography | Operational/inaugurated 2025-05-28. **B+/A-** operator/official-syndicated evidence. Reported as designed/expandable to 500 racks and 5 MW total capacity. Need Orange primary, Uptime, JEPCO, and permit backfill. |
| **Zain Jordan - The Bunker** | https://www.jo.zain.com/english/Business/Pages/CloudandHosting_Thebunker.aspx ; https://www.jo.zain.com/english/Business/Pages/FinanceAndInsurance_CloudandHostingSolutions.aspx ; https://uptimeinstitute.com/uptime-institute-awards/datacenter/zain-data-center--disaster-recovery-bunker/966 ; https://www.intelligentcio.com/me/2019/09/18/zain-jordan-launches-the-bunker-first-of-its-kind-data-centre-in-the-arab-world/ | King Hussein Business Park, Amman | Operational. **A** for Zain official page naming The Bunker and location; **A** for Uptime facility/cert page where details load; **B** for launch/trade coverage. Directory 2 MW claim is C unless Zain/Uptime/utility confirms. |
| **Zain Jordan - Amman DC 2** | https://colocationm.com/jordan/amman-dc-2 and directory searches | Amman | **C candidate only**. Do not count separately until Zain official/Uptime/permit/customer evidence proves a second physical facility. |
| **Umniah - Data Center / Dahiyat Al-Rasheed colocation room** | https://www.umniah.com/business/cloud/datacenter-colocation-service/ ; https://cloud.umniah.com/datacenter.php ; https://www.umniah.com/explore-umniah/umniah-data-center-is-the-first-and-only-in-jordan-to-grant-the-tier-iii-constructed-facility-certification/ ; https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/dahiyat-alrasheed-colocation-room/921 | Amman / Dahiyat Al-Rasheed | Operational. **A** for official Umniah colocation/DC services and Uptime-listed facility; official pages mention industrial grid connection, redundancy, security/biometrics, and Tier III constructed-facility certification. Capacity not public. |
| **Umniah - South Amman / new large Tier III lead** | https://www.umniah.com/explore-umniah/umniah-data-center/ ; https://trismartgroup.com/new-page-60 | South Amman | **A-/B lead**. Umniah official page and Trismart announcement indicate a new South Amman data center / Tier III project. Verify construction/operational status and dedupe against existing Umniah facility before promotion. |
| **Kalaam Telecom** | https://kalaam-telecom.com/ ; DCD/regional searches | Jordan office/market presence; no verified Jordan DC | **C/B lead only**. Regional data-center/connectivity services do not prove a physical Jordan facility. Count only with a Jordan facility page, certificate, permit, or customer record. |
| **NITC / MoDEE government hosting / national cloud** | https://www.modee.gov.jo/Default/EN ; https://www.modee.gov.jo/En/Pages/eGovernment_Program ; https://nitc.gov.jo/Default/En | Amman likely; exact site usually not public | **A for policy/program**, **B/C for facility** unless tender/contract/facility page names infrastructure. Classify as government/institutional, not commercial colo. |
| **Directories - Amman/Jordan listings** | https://www.datacentermap.com/jordan/amman/ ; https://www.datacenters.com/locations/jordan/amman-governorate/amman ; https://datacentercatalog.com/jordan/zain-jordan-co-location-dc | Mostly Amman | **C leads**. Useful for aliases, old facility names, possible duplicate phases, and rough city signal. Every listing needs operator/certifier/permit backfill. |

## 2. Press and Trade Triage

| Source | URL/query | Use | Grade |
|---|---|---|---|
| intaj newsroom | https://intaj.net/newsroom/ and old paths under `https://www.intaj.net/media-center/newsroom/` | Jordan ICT association; often syndicates operator announcements for Orange/Zain. | B/B+ |
| Petra | https://petra.gov.jo/ | Official Jordan News Agency; search AR and EN for inaugurations, MoDEE, ASEZA, TRC, investment. | A/B depending primary status of text |
| Royal Court / jordan.gov.jo | https://rhc.jo/en and https://jordan.gov.jo/EN/Pages/About_Jordan | Official state facts and Royal Court announcements; useful for ADH inauguration trails and governorate list. | A |
| Zawya / MENAFN | https://www.zawya.com/ ; https://menafn.com/ | Regional business-wire versions of official/operator announcements. | B |
| Jordan Times / Roya / Al-Mamlaka / Al-Ghad / Al-Rai / Addustour / Ammon | site-scoped searches | Arabic/English national coverage and governorate-level stories. | B |
| DCD | https://www.datacenterdynamics.com/ | Regional DC/cable/operator coverage; search Jordan, Aqaba, Orange, Zain, Kalaam. | B |
| Capacity / Telecom Review / Developing Telecoms / Total Telecom / W.Media | site-scoped searches | Subsea cable, cloud, telco, ADH expansion, hyperscaler MoU watchlist. | B |
| The Fast Mode / SAMENA Council / Intelligent CIO / DCPost MEA / TechAfrica News | site-scoped searches | Operator press syndication, Tier/certification announcements, launch stories. | B |
| Uptime Institute | https://uptimeinstitute.com/uptime-institute-awards/list and country/client/facility pages | Certification validation. Search by Jordan, Orange, Zain, Umniah, Aqaba, Hashem, Marj, Bunker. | A for certificate data |
| EBRD / EU | https://www.ebrd.com/home/work-with-us/projects/psd/56562.html ; https://north-africa-middle-east-gulf.ec.europa.eu/news/ebrd-and-eu-support-expansion-aqaba-digital-hub-jordan-2026-05-07_en | ADH finance and expansion. | A for project/finance, B/A for EU newsroom summary |

Press queries:

```text
site:petra.gov.jo Jordan "data center" OR "مركز بيانات"
site:petra.gov.jo "مركز العقبة الرقمي" OR "مراكز البيانات" OR "السحابة"
site:zawya.com Jordan "data center" OR "Aqaba Digital Hub" OR "Orange Jordan" "data centre"
site:intaj.net "data center" Jordan Orange OR Zain OR Umniah
site:datacenterdynamics.com Jordan "data center" OR Aqaba OR Orange OR Zain OR Kalaam
site:capacitymedia.com Jordan Aqaba "data center" OR "cable landing"
site:telecomreviewarabia.com Jordan "data center" OR "cloud" OR "digital hub"
site:thefastmode.com "Jordan" "Tier III" "data center"
site:samenacouncil.org Jordan "data center" "Tier III"
site:uptimeinstitute.com Jordan OR "Aqaba Digital Hub" OR "Hashem Data Center" OR "The Bunker"
```

## 3. English and Arabic Discovery Queries

National broad sweep:

```text
"Jordan" ("data center" OR "data centre" OR datacenter OR datacentre) (MW OR megawatt OR racks OR colocation OR hosting OR cloud OR inaugurated OR launched OR "under construction")
"Jordan" "AI data center" OR "hyperscale" OR "carrier-neutral" OR "Tier III"
"Jordan" "data center" (Orange OR Zain OR Umniah OR "Aqaba Digital Hub" OR Kalaam)
"Jordan" "submarine cable" "data center" OR "cable landing" Aqaba
"Jordan" "government cloud" OR "national cloud" "data center"
```

Arabic broad sweep:

```text
"مركز بيانات" الأردن ("ميجاواط" OR "ميغاواط" OR "رفوف" OR "استضافة" OR "افتتاح" OR "قيد الإنشاء")
"مراكز البيانات" الأردن "أورنج" OR "زين" OR "أمنية" OR "العقبة"
"مركز العقبة الرقمي" OR "العقبة الرقمي" "مركز بيانات"
"أورنج الأردن" "مركز بيانات" OR "عين الباشا" OR "مرج الحمام" OR "هاشم"
"زين الأردن" "مركز بيانات" OR "ذا بنكر" OR "مجمع الملك الحسين للأعمال"
"أمنية" "مركز بيانات" OR "ضاحية الرشيد" OR "جنوب عمان"
"كابل بحري" العقبة "مركز بيانات" OR "نقطة تبادل"
```

Capacity/status extraction:

```text
"{project}" (MW OR megawatt OR MVA OR racks OR "IT load" OR "raised floor" OR sqm OR "square meters")
"{project}" ("capacity" OR expandable OR "up to" OR "phase 1" OR "second hall" OR "fit-out")
"{project}" ("Tier III" OR "Tier 3" OR Uptime OR TCDD OR TCCF OR "constructed facility")
"{project}" (inaugurated OR launched OR opened OR operational OR "under construction" OR "go live" OR financing OR EBRD)
"{project_ar}" ("ميجاواط" OR "ميغاواط" OR "رفوف" OR "سعة" OR "المرحلة الأولى" OR "القاعة الثانية")
"{project_ar}" ("افتتاح" OR "دشن" OR "أطلق" OR "قيد الإنشاء" OR "تمويل" OR "تشغيل")
```

Vendor/contractor/supplier backfill:

```text
"Jordan" "data center" (EPC OR MEP OR contractor OR Schneider OR Vertiv OR Huawei OR Nokia OR Trismart OR cooling OR chiller OR UPS OR generator)
"Amman" "data center" contractor OR MEP OR UPS OR "Tier III"
"Aqaba Digital Hub" contractor OR MEP OR UPS OR generator OR cooling OR Schneider OR Vertiv
"مركز بيانات" الأردن ("مقاول" OR "أنظمة تبريد" OR "مولدات" OR "مزود" OR "ترسية")
```

Subsea/connectivity angle:

```text
Aqaba "cable landing" "data center" OR "Aqaba Digital Hub"
Aqaba "submarine cable" Jordan "gateway" OR "open access"
"AqabaIX" OR "Jordan IXP" OR "internet exchange" Aqaba
"مركز العقبة الرقمي" "كابل بحري" OR "محطة هبوط" OR "نقطة تبادل"
```

## 4. Governorate-by-Governorate Industry Strategy

| Governorate | Arabic / locality anchors | Industry route |
|---|---|---|
| Ajloun | عجلون; جامعة عجلون الوطنية | Low yield. Search university IT/procurement, telco edge, municipality, IDECO, Arabic press. Expected no commercial DC unless a future edge/cloud site is named. |
| Amman | عمان; مرج الحمام; ضاحية الرشيد; جنوب عمان; مجمع الملك الحسين للأعمال; المدينة الطبية; سحاب; الموقر | Highest yield. Search Orange Marj/Hashem, Zain Bunker, Umniah, Kalaam, NITC/MoDEE, banks, CBJ, universities, GAM permits, JEPCO power, directories for aliases. Dedupe aggressively. |
| Aqaba | العقبة; مركز العقبة الرقمي; مدينة العقبة; محطة هبوط الكابلات; AqabaIX | Highest yield outside Amman. ADH official/EBRD/Uptime first, then customer pages, cable/IXP, ASEZA, EDCO/NEPCO, investment and expansion press. Distinguish City DC vs Mega DC vs CLS/IXP. |
| Balqa | البلقاء; السلط; عين الباشا; البقعة | Orange Ain Al-Basha is confirmed. Search Orange/intaj/FANA, Al-Baqa'a satellite-station history, Salt/Balqa municipality, JEPCO, Uptime, local Arabic press. |
| Irbid | إربد; اربد; جامعة اليرموك; جامعة العلوم والتكنولوجيا; الحسن الصناعية; منصة الشمال | Medium institutional yield. Search MoDEE Northern Platform, Yarmouk/JUST, Al-Hassan Industrial Estate, IDECO, telco edge. Require data-center infrastructure before counting. |
| Jerash | جرش; جامعة جرش | Low yield. Search university, municipality, IDECO, telco/operator names in Arabic. Expected institutional/edge only. |
| Karak | الكرك; جامعة مؤتة; مؤتة; الحسين بن عبد الله الثاني الصناعية | Low yield. Search Mutah University, industrial estate, EDCO, municipality, Arabic press. Avoid counting ordinary e-services centers. |
| Madaba | مادبا; جامعة مادبا الأمريكية | Low yield. Search municipal/institutional IT and Amman spillover; verify any fintech/cloud MoU carefully. |
| Ma'an | معان; Maan; منطقة معان التنموية; جامعة الحسين بن طلال | Low-medium pipeline yield. Search development area, renewables-adjacent projects, EDCO/NEPCO, university, MOIN/Invest Jordan, Arabic press. Keep MoUs as planned only. |
| Mafraq | المفرق; مدينة الأمير حسن الصناعية; الزعتري | Low yield. Search industrial city, logistics/refugee-response digital infrastructure, IDECO/EDCO, telco edge, local press. Do not count communications rooms. |
| Tafilah | الطفيلة; Tafila; جامعة الطفيلة التقنية | Low yield. Search university, EDCO, wind/renewables context, municipality. Renewables are context, not DC evidence. |
| Zarqa | الزرقاء; الرصيفة; المدينة الصناعية; الهاشمية | Medium-low. Search industrial city/QIZ, JEPCO, municipality, telco edge, banks/government services. Amman spillover may create false positives. |

Per-governorate template:

```text
"{governorate}" Jordan ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "cloud services")
"{governorate}" Jordan (MW OR MVA OR racks OR "Tier III" OR Uptime) "data center"
"{governorate_ar}" ("مركز بيانات" OR "مراكز البيانات" OR "داتا سنتر" OR "استضافة" OR "الخدمات السحابية")
"{governorate_ar}" ("ميجاواط" OR "رفوف" OR "افتتاح" OR "قيد الإنشاء" OR "ترسية")
"{governorate_ar}" "أورنج" OR "زين" OR "أمنية" OR "مركز العقبة الرقمي"
site:petra.gov.jo "{governorate_ar}" "مركز بيانات" OR "سحابة"
site:intaj.net "{governorate}" OR "{governorate_ar}" "data center" OR "مركز بيانات"
site:datacenterdynamics.com Jordan "{governorate}" "data center"
site:uptimeinstitute.com "{governorate}" Jordan OR "{known_facility_alias}"
```

## 5. Directory Reconciliation Rules

- Treat DataCenterMap's Amman page, datacenters.com, colocationm, datacentercatalog, and ocolo as **C leads**. They are useful for facility aliases, operator names, and possible hidden phases, but not enough for final records.
- Do not copy directory MW/Tier/address values unless an operator, Uptime, permit, power, or customer source corroborates the same named facility.
- Keep old and alternate names: Orange Business/Jordan Telecom Group, Umniah/Batelco/Beyon, Zain Jordan, Al Mirnaah/35D/ADH, Marj Al-Hammam/Marj Al-Hamam, Dahiyat Al-Rasheed/Dahiet Al Rasheed.
- If two sources disagree on capacity, preserve both source-specific claims and do not average/normalize them. ADH especially has hall-level and campus-level figures in different articles.
- PeeringDB/IXP/cable records prove interconnection or cable landing, not data-center status.

## 6. Status Normalization

- `strategy`, `investment opportunity`, `MoU`, `agreement`, `partnership`, `academy`, `digital platform`: planned/context unless facility evidence exists.
- `financing`, `loan`, `fit-out`, `second hall`, `supplier commitments`: expansion/planned or construction depending source verb.
- `commenced construction`, `under construction`, `EPC awarded`: construction.
- `inaugurated`, `opened`, `launched`, `available`, `hosting customers`, `customer selects for DR`: operational/service-available as of source date.
- `Tier III-certified` from operator: operator claim until matched to Uptime/certifier record. Uptime list is A for certificate class and facility name.

## 7. Recommended Industry Pipeline

1. Start with accepted seeds: ADH City/Mega, Orange Marj, Orange Hashem, Orange Ain Al-Basha, Zain Bunker, Umniah Dahiyat Al-Rasheed, Umniah South Amman lead, MoDEE/NITC institutional lead, Kalaam lead.
2. Pull Uptime Institute Jordan/list/client pages and reconcile certificate names against operator aliases.
3. Search operator sites and intaj/SAMENA/Fast Mode/FANA for Orange, Zain, Umniah, ADH status changes.
4. Search EBRD/EU, DCD, Capacity, Telecom Review, Zawya, Jordan Times, Petra, Roya, Al-Mamlaka, Ammon for ADH expansion, cable landing, and new operator projects.
5. Run Amman/Aqaba/Balqa deep dives with Arabic and locality terms.
6. Run all remaining governorates and record negative sweeps. Promote only if a named facility has infrastructure vocabulary and at least B-grade support.
7. Join official methodology evidence: TRC/legal status, municipal/ASEZA permit, Ministry of Environment, NEPCO/JEPCO/IDECO/EDCO, MOIN/Invest Jordan/JIEC.
8. Dedupe by `(operator/legal owner, campus/facility alias, governorate, phase/data hall)`, not by brand or article headline.
9. Re-check official cloud region pages and keep hyperscaler claims separate from local colo/cloud facilities.

## 8. Pitfalls

- Do not count an Aqaba cable landing station, AqabaIX, a POP, or a cloud product as a separate data center.
- Do not count every telco exchange, bank server room, university IT lab, or government service center.
- Do not accept "Jordan's first/largest/only" marketing without source-specific context; multiple operators make scoped claims.
- Do not promote Kalaam Jordan from regional service pages alone.
- Do not treat Umniah South Amman as a separate operational facility until its status and relationship to Dahiyat Al-Rasheed are clear.
- Do not mark Orange Ain Al-Basha's 5 MW as delivered utilization; it is source-stated designed/expandable/total capacity.
- Do not let Amman directories create duplicate Orange/Zain/Umniah records without operator/certifier confirmation.
- Search Arabic before declaring low-yield governorates negative.

<!-- END -->
