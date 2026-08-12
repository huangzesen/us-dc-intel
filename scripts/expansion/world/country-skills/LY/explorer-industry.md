# LY Explorer Industry - Libya Datacenter Enumeration via Colo Providers, Cloud Checks, Trade Press, Associations, and District Queries

Date: 2026-08-12. Country: **LY Libya**. Scope: industry / vendor-led discovery for Libyan data centers, colocation, hosted cloud, government digital-sovereignty sites, and district-level search patterns. Reliability grades: **A** = official / primary source (operator page, GACI / LPTIC / ministry / municipality / UN procurement / official cloud-region page / contractor project page), **B** = established trade press or strong local press quoting named authorities, **C** = directory, marketplace, social post, generic vendor landing page, or market-report snippet used as a lead only.

---

## 0. Libya market frame

- Libya has **no single public data-center registry**. Enumeration must triangulate telecom holding-company pages, GACI regulatory material, local operator pages, trade press, directories, UN / development procurements, and Arabic state-news searches.
- Publicly visible facility evidence is concentrated in **Tripoli**, **Benghazi**, **Misrata**, and **Sabha**. Treat other popularates as low-yield unless tied to municipal data hubs, telecom exchanges, universities, oil/gas infrastructure, or free-zone / port initiatives.
- The most useful local keywords are mixed English / Arabic: `data center`, `data centre`, `datacenter`, `colocation`, `cloud computing`, `hosting`, `server room`, `modular data center`, `Tier 3`, `مركز بيانات`, `مراكز البيانات`, `الحوسبة السحابية`, `استضافة`, `مركز معلومات`, `مركز البيانات`, `مركز وطني للبيانات`.
- Separate record types: **commercial colo/cloud facility**, **telecom operator IDC**, **cloud-service provider without disclosed facility**, **government or municipal data hub**, **university/server-room/HPC site**, **root-server or IXP node**, and **vendor-built modular facility**.
- Libya's regulator is actively building a framework. LANA and Libyan Technology Foundation coverage of the February 15, 2026 GACI workshop says the agenda covered regulation, accreditation, provider registration, cloud-computing conditions, cybersecurity, and data governance. Use this as an official/regulatory route, not as proof that any individual facility is licensed.

Core national query set:

```text
Libya ("data center" OR "data centre" OR datacenter OR colocation OR "cloud computing")
Libya ("Tier 3" OR "Tier III" OR modular) ("Tripoli" OR Benghazi OR Misrata OR Sabha)
"Libya" "cloud services" "data center" operator
"Libya Telecom and Technology" "data center" Tripoli Benghazi
"LPTIC" "data centers" Tripoli Misrata
"GACI" Libya "data center" "cloud computing"
"General Authority for Communications and Informatics" Libya "data center"
"مراكز البيانات" ليبيا "الحوسبة السحابية"
"مركز بيانات" طرابلس OR بنغازي OR مصراتة OR سبها
```

---

## 1. High-signal source classes

| Source | URL / route | Use | Grade |
|---|---|---|---|
| General Authority for Communications and Informatics (GACI) / Libya regulator | Search official GACI channels and Arabic press; IANA .LY report confirms GACI as proposed .LY manager: https://www.iana.org/reports/2025/ly-report-20251030.html | Regulator, future accreditation, telecom/cloud rules, national strategy. | A when official; B when quoted by LANA / local press |
| Libyan News Agency (LANA) | https://lana.gov.ly/ ; example GACI workshop: https://lana.gov.ly/post.php?id=351103&lang=ar | Arabic official/state-news source for GACI workshops, regulations, investment pushes, ministerial statements. | A/B |
| Libyan Technology Foundation (LTF) | https://technology.ly/en/session-with-cim/ | Association / civil-society technical ecosystem; useful for workshop participants, standards, policy terms, and GACI strategy references. | B |
| LPTIC | https://lptic.ly/ ; digital transformation page: https://lptic.ly/digital-transformation/ | State telecom holding-company source; names Tripoli and Misrata data-center plans under digital-transformation program. | A |
| LPTIC subsidiaries | LTT https://www.ltt.ly/ ; Almadar via LPTIC https://lptic.ly/our-companies/almadar/ ; Libyana, Hatif Libya, LITC | Telecom operator IDCs, root-server hosting sites, cable / international gateway pivots. | A for corporate structure; facility evidence varies |
| Operator pages | Qabas https://qbs.ly/our-expertise/data-center-in-libya/ ; TransSahara https://it.transahara.com/ ; Digital Cloud https://www.dcloud.ly/index-en.html ; Altaqnya https://altaqnya.com.ly/ | Commercial data-center / cloud / integrator seed list. Operator pages are A for self-claimed services but must be checked for physical site and status. | A/B |
| Trade press | DCD https://www.datacenterdynamics.com/ ; Libya Herald https://libyaherald.com/ ; Libya Observer https://libyaobserver.ly/ ; Libya Review https://libyareview.com/ ; Libya Monitor | Project discovery, root-server milestones, TransSahara/Tatweer, telecom investment claims. | B |
| Directories | DataCenterMap https://www.datacentermap.com/libya/ ; datacenters.com Libya pages; Cloudscene; ColocationM | Good for addresses / aliases in Tripoli, Benghazi, Misrata, Sabha. Always downgrade to C until corroborated. | C |
| UN / development procurement | UNGM https://www.ungm.org/ | Municipal / university data hubs, rehabilitation projects, governance data platforms. | A for procurement scope |
| Official hyperscaler region pages | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/ | Confirm whether Libya has a public cloud region. Current official pages do not show a Libya region; partner/cloud service claims are not region evidence. | A |

---

## 2. Operator and vendor sweep

Use this seed list first, then pivot by city / address / Arabic company name. Operator pages can prove services, but facility count, power, commissioning, and Tier claims need independent support.

| Operator / vendor | Primary URLs | Geography signals | Enumeration notes |
|---|---|---|---|
| **LPTIC** | https://lptic.ly/digital-transformation/ | Tripoli, Misrata | Digital-transformation page explicitly includes setting up comprehensive data centers in Tripoli and Misrata. Treat as planned / program evidence unless separate commissioning source appears. |
| **Libya Telecom and Technology (LTT)** | https://www.ltt.ly/ ; directories; contractor page https://in-site.it/en/progetto/data-center-en/libya-telecom-tech | Tripoli, Benghazi | Directories list LTT Internet Data Center in Tripoli; In-Site says it integrated modular data-center containers for LTT projects in Tripoli and Benghazi. Verify through LTT / LPTIC / GACI before upgrading from C/B. |
| **TransSahara / Trans-Saharan Telecommunications** | https://it.transahara.com/ ; DCD; Libya Herald; directories | Tripoli / Janzur, Benghazi, Misrata, Sabha | DCD and Libya Herald report 2019 TransSahara + Tatweer Tier 3 prefabricated facility for Tripoli. DataCenterMap lists facilities in Benghazi, Misrata, Sabha, and Tripoli; directory data is C unless matched to TransSahara pages or press. |
| **Tatweer Research** | https://tatweerresearch.org/ | Benghazi agreement, Tripoli deployment | Public-sector partner in TransSahara Tier 3 announcement. Use as project backer / innovation-center pivot. |
| **Qabas** | https://qbs.ly/our-expertise/data-center-in-libya/ | Tripoli | Operator page says Tripoli-based data centers with backup generators, independent links, CCTV, fire detection/suppression, colocation, cloud, and private enterprise services; also says new Tripoli facility targeted mid-2025. Confirm completion before counting a separate new site. |
| **Al-Madar Al-Jadid** | https://lptic.ly/our-companies/almadar/ ; GACI / Libya Herald / Libya Review root-server stories | Tripoli, Benghazi | Local press says Libya root servers run from Al-Madar data centers in Tripoli and Benghazi. Treat as strong B until GACI primary page is found. |
| **Libyana Mobile Phone** | LPTIC subsidiary pages; operator search | Tripoli plus mobile core sites | Likely telecom core / data rooms, but do not count without data-center language. Search for core-network, 5G, cloud, and hosting terms. |
| **Libyan International Telecom Company (LITC)** | LPTIC subsidiary / cable and international gateway searches | Tripoli, cable landing / gateway sites | Useful for submarine-cable and international gateway pivots; facility evidence usually indirect. |
| **Digital Cloud Libya** | https://www.dcloud.ly/index-en.html | Tripoli, Bab Bin Ghashir | Markets network engineering, cybersecurity, data-center solutions, SOC, sovereign networks. Treat as integrator / provider lead unless a specific operated facility is named. |
| **Altaqnya for Data Communication** | https://altaqnya.com.ly/ | Libya, location to verify | Markets network, data center, and cloud supply. Use as integrator lead only unless facility-specific evidence appears. |
| **Agathon / Alada / legacy systems integrators** | Company / biography / press searches | Tripoli, oil, banking, NOC, GECOL | Historical integrator lead for bank/oil/government data centers; useful for older institutional facilities, not necessarily current colo. |
| **Huawei, In-Site, Retelit Med, Cisco/Fortinet/Schneider/Vertiv-style vendors** | Vendor case studies and local partner pages | Tripoli, Benghazi, operator sites | Vendor pages often disclose modular facilities before local operators do. Grade as B unless customer/operator confirms. |

Operator query patterns:

```text
"{operator}" Libya ("data center" OR datacenter OR "data centre" OR colocation OR cloud)
"{operator}" Libya ("مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية" OR "استضافة")
"{operator}" Tripoli OR Benghazi OR Misrata OR Sabha "data center"
"{operator}" Libya ("Tier 3" OR "Tier III" OR modular OR "FusionModule")
"{operator}" Libya ("backup generators" OR UPS OR cooling OR "fire suppression" OR CCTV)
"{operator}" GACI Libya "cloud" OR "data center"
site:lptic.ly "{operator}" "data center"
site:lana.gov.ly "{operator}" "مركز بيانات"
site:technology.ly "{operator}" "data center"
```

Facility-address pivots:

```text
"Innovation Centre" Janzur TransSahara "data center"
"Janzur" "TransSahara" "data center"
"Soug Aljouma" "LTT Internet Data Center"
"Tripoli St 025" Misrata TransSahara
"Jamal Abdelnaser Street" Sabha TransSahara
"Bab Bin Ghashir" "Digital Cloud" "data center"
"Al-Madar" Tripoli Benghazi "root servers" "data centres"
```

---

## 3. Cloud-region methodology

Libya public cloud-region evidence should be checked against official region pages before accepting market claims.

| Provider | Current Libya signal | Method |
|---|---|---|
| AWS | No Libya public Region found on the official AWS Regions and AZs page checked 2026-08-12. | Search official AWS global infrastructure page and `site:aws.amazon.com Libya "Region" "Local Zone"`; exclude partner reselling and Outposts unless site is named. |
| Microsoft Azure | No Libya geography / public region found on official Azure global infrastructure geography pages checked 2026-08-12. | Search Azure region list and `site:microsoft.com Libya Azure "region"`; edge / CDN POPs are not regions. |
| Google Cloud | No Libya public cloud region found on official Google Cloud locations page checked 2026-08-12. | Search Google locations and Compute regions; do not infer from reseller or Google Workspace presence. |
| Oracle Cloud | No Libya public OCI region found on official Oracle public cloud regions page checked 2026-08-12. | Search OCI region list and Qabas / Oracle partner claims separately; partner status is not a cloud region. |
| Huawei / regional cloud vendors | No official Libya public cloud region found in this pass; Huawei appears as modular data-center / telecom equipment partner in Libya-related sources. | Search Huawei Libya + operator names; count only if Huawei names a Libya cloud region / AZ or an operator identifies the physical facility. |

Cloud query templates:

```text
site:aws.amazon.com Libya "Region" "Availability Zone"
site:learn.microsoft.com Azure Libya "region"
site:azure.microsoft.com Libya "cloud region"
site:cloud.google.com Libya "region" "Google Cloud"
site:oracle.com Libya "cloud region" OR "public cloud"
"Huawei Cloud" Libya "region" OR "availability zone"
"Oracle" Libya Qabas "cloud"
"AWS" Libya Qabas "partner" -jobs
```

---

## 4. Trade press, association, and regulatory workflows

### 4.1 Trade press

Use trade press for leads and status language, then verify with operator / GACI / LPTIC / procurement sources.

```text
site:datacenterdynamics.com/en/news Libya "data center"
site:datacenterdynamics.com/en/news TransSaharan Tatweer Libya
site:libyaherald.com Libya "data centre" OR "data center"
site:libyaherald.com "root servers" "data centres" Tripoli Benghazi
site:libyaobserver.ly Libya "data centers" "GACI"
site:libyareview.com Libya "root server" "Tripoli" "Benghazi"
site:libyamonitor.com Libya "data center" OR "data centres"
```

Status interpretation:

- `agreement`, `signed`, `workshop`, `roadmap`, `strategy`, `future vision`, `needs investment` = lead / policy signal, not a facility.
- `setting up`, `to establish`, `plans`, `project`, `mid-2025`, `will deploy` = planned unless completion evidence appears.
- `launched`, `opened`, `operating sites`, `in service`, `operational`, `installed`, `integrated modular data centre technology` = stronger operational signal, but still verify physical site / operator.
- Arabic equivalents: `توقيع`, `اتفاق`, `رؤية مستقبلية`, `تنظيم`, `تشريعات`, `اعتماد`, `مراكز معتمدة`, `إطلاق`, `تشغيل`, `افتتاح`, `استضافة`.

### 4.2 Association / ecosystem checks

- **Libyan Technology Foundation**: search `technology.ly` for `data center`, `GACI`, `cloud computing`, `National Telecommunications Strategy`, `provider accreditation`, and Arabic pages. Good for standards / stakeholder lists.
- **ISOC Libya / Internet Society Libya** and DNS community: use for root-server, .LY, IXP, and governance leads; verify facility sites through GACI / operator.
- **Libyan Academy for Telecom and Informatics (LATI)**: https://lati.ly/ has Tripoli, Benghazi, and Misrata branches; search for labs, cloud training, and telecom academy infrastructure, but do not count training labs as data centers without explicit facility language.
- **Misrata Free Zone / port and industrial entities**: https://mfzly.com/ can identify investor and port/free-zone context; data-center projects still need facility-specific proof.

Association queries:

```text
site:technology.ly Libya "data center" OR "cloud computing"
site:technology.ly "GACI" "data center"
site:technology.ly "National Telecommunications Strategy" "cloud storage"
site:lati.ly "مركز بيانات" OR "الحوسبة السحابية"
site:mfzly.com "data center" OR "مركز بيانات" OR "cloud"
"Libya" "Internet Society" "root server" "data center"
```

---

## 5. Directory and aggregator handling

Directories are high-yield in Libya because operator pages are sparse, but they are not sufficient for final facility enumeration.

| Directory | What it provides | Caveat |
|---|---|---|
| DataCenterMap Libya: https://www.datacentermap.com/libya/ | Market count by city and facility leads. Current snapshot seen in search results: Tripoli 3, Benghazi 1, Misrata 1, Sabha 1. | C; page-view limitations and possible stale entries. |
| Datacenters.com | TransSahara Tripoli / Tripoli market aliases and commercial service language. | C; quote marketplace, verify with operator. |
| Cloudscene | LTT Tripoli / network-service marketplace evidence. | C for facility specifics. |
| ColocationM | Repackages LTT and TransSahara facility claims with service details. | C; useful only as a discovery index. |
| PeeringDB / IXP directories | Networks, facilities, IXPs if records exist. | Proves interconnection metadata only, not MW / construction status. |

Directory upgrade workflow:

1. Capture exact facility name, operator, address, city, services, power/capacity, and directory URL.
2. Search the exact name in English and Arabic.
3. Search operator site and LPTIC / GACI / LANA for the operator and city.
4. Search vendor / contractor names if equipment is mentioned.
5. If only directories support the facility, retain **C** and flag as unverified.

Directory query templates:

```text
site:datacentermap.com/libya "Libya" "data center"
site:datacentermap.com/libya "{city}" "{operator}"
site:datacenters.com Libya "{operator}" "data center"
site:cloudscene.com "Libya" "{operator}"
site:colocationm.com/libya "{operator}" "{city}"
site:peeringdb.com Libya "{operator}" OR "{facility}"
```

---

## 6. Division-level industry search matrix

Run the universal English and Arabic templates for all 22 popularates from `world-manifest.jsonl`. Use district spelling variants because search results mix English transliterations, city names, and Arabic names.

Universal templates:

```text
"{division}" Libya ("data center" OR "data centre" OR datacenter OR colocation OR "cloud computing" OR hosting)
"{division}" Libya ("server room" OR "IT infrastructure" OR "modular data center" OR "Tier 3")
"{city_ar}" ليبيا ("مركز بيانات" OR "مراكز البيانات" OR "مركز معلومات" OR "الحوسبة السحابية" OR "استضافة")
site:lana.gov.ly "{city_ar}" "مركز بيانات"
site:ungm.org Libya "{division}" "data center"
site:lptic.ly "{division}" "data center"
```

| Popularate | Localities / Arabic pivots | Industry / vendor approach |
|---|---|---|
| **Tripoli** | Tripoli, Tarabulus, طرابلس, Soug Aljouma, Janzur, Bab Bin Ghashir | Highest priority. Sweep LTT IDC, TransSahara/Tatweer, Qabas, Al-Madar root-server site, Digital Cloud, GACI workshops, LPTIC, government agencies, bank data centers, and vendor case studies. |
| **Benghazi** | Benghazi, بنغازي, Benina, Hawari, Al Kish | High priority. Sweep TransSahara directory lead, Al-Madar root-server site, LTT modular container lead, Tatweer Research, eastern-government digital projects, universities, and Arabic press. |
| **Misrata** | Misrata, Misurata, مصراتة, port, free zone, Tripoli Street | High priority. Sweep LPTIC planned comprehensive data center, TransSahara Misrata directory lead, LATI Misrata, Misrata Free Zone / port investor leads, municipality pages. |
| **Sabha** | Sabha, Sebha, سبها, Sebha University, Jamal Abdelnaser Street | High priority. Sweep UN / municipality-university data hub procurements, TransSahara Sabha directory lead, Fezzan / southern-governance projects. |
| **Murzuq** | Murzuq, Murzuk, مرزق, Fezzan University | High priority for public-sector data hubs. UNGM procurement mentions Murzuq municipal data center / governance data hub; verify municipality and university follow-up. |
| **Zawiya** | Zawiya, Az Zawiyah, الزاوية, refinery | Medium/low. Search telecom exchanges, refinery / NOC IT, municipal digital services; avoid false positives from oil-infrastructure news and proxy-hosting spam. |
| **Jafara** | Jafara, Al Jfara, الجفارة, Aziziyah, Qasr bin Ghashir | Medium. Near Tripoli spillover; search industrial zones, telco exchange sites, government data stores, and logistics parks. |
| **Murqub** | Al Khoms, Khoms, الخمس, ترهونة, Qasr Al Akhyar | Medium. Search port / cable / municipal digitization and telecom exchange language; no known strong colo seed. |
| **Butnan** | Tobruk, طبرق, امساعد, Bardia | Medium. Search border / port / government systems, telecom core, possible cable or gateway references. |
| **Derna** | Derna, درنة | Low/medium. Search reconstruction procurements, municipal data hubs, university / health system server rooms; disaster-recovery and governance terms may surface. |
| **Green Mountain** | Jabal al Akhdar, Al Bayda, البيضاء, الجبل الأخضر | Low/medium. Search Al Bayda government / university / municipal digitization; watch for generic `green data center` false positives. |
| **Western Mountain** | Jabal al Gharbi, Gharyan, غريان, Yefren, الزنتان | Low/medium. Search telecom exchanges, municipal systems, solar / energy investment; likely no public colo. |
| **Jufra** | Hun, الجفرة, Waddan, Sokna | Low. Search strategic central telecom, government data collection, airport / military-adjacent infrastructure; expect sparse public evidence. |
| **Kufra** | Kufra, الكفرة | Low. Search border / airport / satellite / government telecom infrastructure; verify carefully. |
| **Ghat** | Ghat, غات | Low. Search municipal digitization and cross-border / tourism infrastructure; likely no facility leads. |
| **Nalut** | Nalut, نالوت, Ghadames, غدامس | Low. Search border / tourism / municipal IT and telecom exchanges; no known commercial seeds. |
| **Nuqat al Khams** | Nuqat al Khams, Al Ajaylat, Zuwara, زوارة, الجميل | Low/medium. Search port, border, cable, telco exchange, municipal data-center terms. |
| **Sirte** | Sirte, سرت | Low/medium. Search reconstruction, university, municipal governance, and telecom backbone nodes. |
| **Oases** | Wahat, Al Wahat, الواحات, Ajdabiya, Jalu, Awjila | Low/medium. Search oil/gas / NOC / field-data systems and municipal projects; distinguish industrial SCADA rooms from data centers. |
| **Wadi al Hayaa** | Wadi al Hayaa, Ubari, أوباري | Low. Search southern municipal digitization, university / health systems, and telecom/satellite infrastructure. |
| **Wadi ash Shati** | Wadi ash Shati, Brak, براك الشاطئ | Low. Search Brak municipality, university, airport/telecom nodes; record no-project only after Arabic and English passes. |
| **Meadows** | Al Marj, المرج | Low/medium. Search municipality / university / telecom exchange terms; no strong industry seed found in current pass. |

Arabic locality terms:

```text
طرابلس بنغازي مصراتة سبها مرزق الزاوية الجفارة الخمس طبرق درنة البيضاء الجبل الأخضر غريان الجبل الغربي هون الجفرة الكفرة غات نالوت زوارة سرت الواحات أجدابيا أوباري براك الشاطئ المرج
```

---

## 7. Validation checklist for final facility records

- Is the source describing a **physical data center** rather than cloud consulting, VPS resale, cybersecurity services, training, or a generic data-center solution?
- Is the status verb clear: planned, under construction, installed, launched, operational, or merely discussed?
- Is the geography tied to a popularate / city / address? If only `Libya` is stated, keep as country-level lead until localized.
- Is the operator the facility owner/operator, a JV partner, an integrator, or only a technology vendor?
- Does capacity come from a primary operator / contractor / certification source? If only a directory lists MW, grade C.
- Have AWS / Azure / Google / Oracle official region pages been checked before recording any public cloud-region claim?
- For Arabic results, preserve exact Arabic title / agency and translate status cautiously. `تنظيم القطاع` and `اعتماد المراكز` are regulatory evidence, not proof of a licensed facility unless a named operator is present.

