# PS Explorer Industry - Palestine Datacenter Enumeration

Date: 2026-08-12. Country: **PS Palestine, State of**. Scope: industry, trade-press, operator, vendor, directory, and local-media discovery for the 16 governorates: `Bethlehem`, `Deir El Balah`, `Gaza`, `Hebron`, `Jerusalem`, `Jenin`, `Jericho and Al Aghwar`, `Khan Yunis`, `Nablus`, `North Gaza`, `Qalqilya`, `Ramallah`, `Rafah`, `Salfit`, `Tubas`, `Tulkarm`.

Reliability grades:
- **A** = operator/company official page, PEX filing, Uptime certification, MTDE/WAFA/Shiraa/PCBS/World Bank/UN primary source.
- **B** = established trade/business/humanitarian reporting with named parties: DCD, Bloomberg/Data Center Knowledge, Telecompaper, SAMENA, Al Jazeera, Reuters/NYT, Access Now, 7amleh, PITA when it names companies/projects.
- **C** = directories, marketplaces, LinkedIn/social, vendor success stories without buyer confirmation, market reports, SEO/broker listings, academic concepts.

Industry discovery must end with official verification. C-grade leads are useful for aliases and locations, not for final operational status.

---

## 0. Market frame

- Palestine does **not** have a hyperscale data-center market or a hyperscaler public-cloud region. The in-country universe is local telecom/government/enterprise infrastructure.
- The best confirmed commercial/operator leads are **Paltel**: Al-Bireh/Ramallah Tier III Design data center launched in 2019 and a prior Paltel data-center project at the general-management headquarters in Nablus. Paltel also had main data centers and switches in Gaza, but those must be treated through damage/recovery evidence after October 2023.
- The best confirmed government lead is **MTIT/MTDE Government Computer Center / National Data Center** in Ramallah context, now described by the MTDE/NDC page as a government collocation, DR-hosting, and private-cloud environment.
- Small providers such as **Zone Technologies** may offer local VPS/cloud/data-center hosting. Treat them as small enterprise/hosting facilities unless capacity, power, site, and status are verified.
- Arabic is the highest-yield language for local openings, tenders, and vendor case studies. English is strongest for Paltel 2019 trade coverage, World Bank/UN documents, and Gaza-damage reporting.

Core search vocabulary:

```text
data center / data centre / datacenter
colocation / collocation / hosting / cloud / VPS / DR
مركز بيانات / مركز البيانات / مراكز البيانات
استضافة / استضافة الخوادم / استضافة المواقع
الحوسبة السحابية / خوادم افتراضية / تخزين سحابي
التعافي من الكوارث / مركز احتياطي
افتتاح / إطلاق / تدشين / تنفيذ / توقيع
تدمير / تضرر / انقطاع / إعادة إعمار
```

---

## 1. High-signal industry and media sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/?tag=palestine | Paltel second DC, outages, cloud-region-related Palestine items | B+ |
| Bloomberg / Data Center Knowledge | https://www.datacenterknowledge.com/cloud/palestinian-phone-company-offers-cloud-computing-from-ramallah | USD 10m Paltel Ramallah data-center/cloud story | B |
| Telecompaper / SAMENA | site-scoped searches | Regional telecom repeats of Paltel/Ooredoo stories | B |
| Al Jazeera | Gaza telecom reporting | Paltel Gaza data-center redundancy and wartime operations | B |
| WAFA | https://english.wafa.ps/ and https://www.wafa.ps/ | Official news agency; useful for Paltel Gaza statements and government digital programs | A/B |
| 7amleh | https://7amleh.org/ | Gaza telecom damage assessments; cites Paltel/Ooredoo/MTDE | B |
| PCBS | https://www.pcbs.gov.ps/ | Official telecom/digital-resilience indicators; not facility registry | A |
| PITA | https://pita.ps/ | ICT company discovery and event leads | B-/C |
| Local Arabic press | Palsawa, QudsNet, Maan, Bnews, Hadf | Operator openings, tenders, vendor awards; verify upstream | B-/C |
| DataCenterMap | https://www.datacentermap.com/palestine/ | Zone Ramallah and other directory seeds | C+ |
| Inflect / Data Center Platform / Datacenter Catalog | site-scoped | Gaza/Jenin/Bethlehem/Zone claims; alias discovery only | C |
| LinkedIn / social pages | company pages/posts | Current service claims; no facility status unless independently backed | C |

Industry query templates:

```text
site:datacenterdynamics.com Palestine "data center"
site:datacenterknowledge.com Palestine "data center"
"Paltel" "data center" "Ramallah" OR "Al-Bireh"
"Paltel" "Tier III" "Uptime" Palestine
"Paltel Cloud" "Palestine" "data center"
"Zone Technologies" Ramallah "data center" OR "cloud"
"Ooredoo Palestine" "data center" OR "cloud"
"Digital Communication" Gaza "data center"
"Paltel Data Center" Bethlehem OR Jenin OR Nablus
"Gaza" "data centers" Paltel damage OR fuel OR batteries
"بالتل" "مركز البيانات" "البيرة" OR "نابلس"
"غزة" "مراكز البيانات" "بالتل"
"زون تكنولوجيز" OR "Zone Technologies" "مركز بيانات"
```

---

## 2. Operator and vendor seed list

| Entity | Source routes | Industry signal | Handling |
|---|---|---|---|
| Paltel Group / Paltel | https://www.paltelgroup.ps/ ; https://www.paltel.ps/ ; PEX filings | Main private data-center operator. Al-Bireh/Ramallah Tier III Design site; prior Nablus HQ data center; cloud/colocation/DR services. | A/B when supported by Paltel/Uptime/DCD/Bloomberg. |
| Jawwal | https://www.jawwal.ps/ | Paltel mobile arm; may mirror Paltel infrastructure news. | Do not create separate Jawwal DC unless named. |
| Hadara | Hadara/Paltel routes; ASN/ISP records | ISP arm and hosting/service lead. | Service identity only; no separate facility without primary source. |
| Ooredoo Palestine | https://www.ooredoo.ps/ | Mobile operator; business/cloud/managed services; Ooredoo Group has regional data-center strategy. | No verified Palestine facility in this pass. Generic group data-center news is not PS evidence. |
| MTDE / NDC | https://mtde.online/national-data-center/ ; World Bank assessment | Government collocation, DR hosting, private cloud. | A-/A after cross-check; institutional government DC. |
| PalCERT / Gov-SOC | https://mtde.online/palcert/ | Government SOC monitoring systems and websites. | Not a separate facility. |
| Zone Technologies | https://zone.ps/ ; DataCenterMap Ramallah | Local cloud/VPS/storage provider; DataCenterMap lists "Zone Data Center" at Masrouji Building / Al Madaen Street, Ramallah/Al-Bireh. | C+/B- lead. Need operator facility page, power, capacity, or customer evidence before final operational DC. |
| Digital Communication Gaza | Inflect/directories | Directory-only Gaza City DC lead. | C. Must not override Gaza damage evidence. |
| Hebron Municipality / Telnet Systems | vendor success-story searches | Municipal data-center implementation lead. | C/B until municipal or procurement source confirms. |
| Universities | Birzeit, An-Najah, Al-Aqsa, AAUP | Server rooms, HPC/e-learning, NSDI concepts. | Usually C institutional compute. Academic concepts are not facilities. |
| Banks / fintech | PMA, Arab Bank, local banks | DR/core banking rooms; outsourcing contracts. | C/B unless annual report/procurement names a site. |
| Industrial-zone operators | PIPA/PIEFZA, BMIP, JAIP, Jenin Free Zone, Tarqumiya | Possible future sites. | Lead only; no facility without investment/permit/tender. |

Operator templates:

```text
site:paltelgroup.ps "مركز البيانات" OR "استضافة الخوادم" OR "الحوسبة السحابية"
site:paltelgroup.ps "نابلس" "مركز البيانات"
site:paltelgroup.ps "البيرة" "Tier-3"
site:zone.ps "Cloud Server" OR "VPS" OR "Data" OR "Ramallah"
site:ooredoo.ps "cloud" OR "سحابية" OR "استضافة"
site:telnet.ps "data center" "Hebron" OR "بلدية الخليل"
site:pita.ps "data center" OR "cloud" OR "استضافة"
```

---

## 3. Confirmed and weak lead handling

### 3.1 Paltel Al-Bireh/Ramallah data center

Verified source stack:
- Paltel Arabic construction/service announcement: https://www.paltelgroup.ps/pginfo/?p=58225
- Uptime award: https://uptimeinstitute.com/uptime-institute-awards/datacenter/paltel-data-center--albireh/1115
- DCD 2019 launch: https://www.datacenterdynamics.com/en/news/paltel-group-opens-second-palestine-data-center/
- Bloomberg/DCK 2019: https://www.datacenterknowledge.com/cloud/palestinian-phone-company-offers-cloud-computing-from-ramallah

Record as:

```text
name: Paltel Data Center - Al-Bireh / Ramallah
developer: Palestine Telecommunications Company PLC / Paltel Group
division: Ramallah
status: operational
capacity_mw: null
area: 65,000 sq ft / about 6,000 sq m when citing DCD
certification: Uptime Tier III Design (award page)
services: colocation, DR, virtual servers, IaaS/PaaS/SaaS, storage
notes: Uptime page location text is inconsistent; project name and operator/trade coverage point to Al-Bireh/Ramallah.
```

### 3.2 Paltel first data center - Nablus

Paltel's own announcement says it had previously implemented a strategic data-center project at the company's general-management headquarters in **Nablus**. That is enough for a lead and possibly an operational institutional/operator DC, but not enough for public capacity/Tier/current-status claims.

Record with:
- division `Nablus`
- capacity null
- status `operational` only if citing Paltel's own text and notes make clear it is historical/limited-spec
- no MW, no Tier, no address beyond public HQ context unless independently verified

### 3.3 Government NDC / Government Computer Center

Use official file routes. Industry output should not duplicate NDC as multiple facilities unless a source distinguishes Government Computer Center, NDC, DR site, and private cloud as separate physical sites.

### 3.4 Zone Ramallah

DataCenterMap lists a Zone Technologies data center at Masrouji Building / Al Madaen Street in Ramallah and Zone's own website markets cloud, VPS, cloud storage, and Ramallah/Masrouji contact details. This is a useful small-provider lead, but still lacks a public facility spec, Uptime/Tier, utility/power, commissioning date, or official permit.

Recommended record handling:

```text
name: Zone Ramallah Data Center / Zone Technologies cloud-hosting site
division: Ramallah
status: operational_lead or operational with evidence_grade C only, depending schema
capacity_mw: null
evidence_grade: C or C+
notes: Directory and marketing evidence only; verify with Zone, municipality, customer contract, or telecom license before promoting.
```

### 3.5 Gaza facilities

Gaza entries require special status discipline:
- WAFA 2023 reported Paltel's main data centers and switches gradually shutting down due to fuel depletion.
- Al Jazeera reported Paltel Gaza data centers had generators, solar panels, and batteries.
- 7amleh 2024 reported 75% telecom infrastructure damaged and at least 50% destroyed.
- PCBS/MTDE/TRA 2026 reported partial connectivity/resilience interventions, but not DC commissioning.

Therefore:
- pre-war Gaza Paltel DCs = `damaged` / `intermittent` / `unknown-current-status`, not normal `operational`.
- directory-only Gaza providers = C leads; do not count in final census without 2025-2026 operator or official confirmation.
- redevelopment/AI-city/data-center-zone concepts = `announced concept` only; not construction.

### 3.6 Directory-only false positives

Watch for and downgrade:
- `Paltel Data Center - Bethlehem` from weak third-party news/directories.
- `Paltel Data Center - Jenin` from Inflect/directory pages.
- `Digital Communication Gaza` from Inflect.
- `New Gaza redevelopment data centres` from broad reconstruction vision stories.
- `Al-Aqsa University Gaza Data Centre` from academic/NSDI paper.
- Israeli facilities near Jerusalem, Atarot, Modi'in, Har Tuv, Beit Shemesh, Tel Aviv, and Jerusalem cloud regions. These are not PS facilities.

---

## 4. Governorate-by-governorate industry matrix

| Division | Industry query anchors | Expected result |
|---|---|---|
| `Ramallah` | Ramallah, Al-Bireh, Beitunia, رام الله، البيرة, Paltel, Zone, MTDE, NDC | Highest priority. Paltel Al-Bireh, NDC/Government Computer Center, Zone C lead, operator HQ/server rooms. |
| `Nablus` | Nablus, نابلس, Paltel HQ, An-Najah | Paltel first DC lead; university/server-room leads only. |
| `Hebron` | Hebron, الخليل, Tarqumiya, Telnet, municipality | Municipal/vendor data-center lead; industrial-zone future leads. |
| `Bethlehem` | Bethlehem, بيت لحم, BMIP, Hindaza | No verified DC. Treat Paltel Bethlehem claims as C until primary source. |
| `Jerusalem` | Jerusalem, القدس, Abu Dis, Al-Ram, East Jerusalem | No verified PS DC. Filter out Israeli results and cloud regions. |
| `Jenin` | Jenin, جنين, Jenin Free Zone | No verified DC. Paltel Jenin directory lead is C. |
| `Jericho and Al Aghwar` | Jericho, أريحا, JAIP, solar | No verified DC; future land/solar leads only. |
| `Tulkarm` | Tulkarm, طولكرم | No verified DC; small ISP/university leads only. |
| `Qalqilya` | Qalqilya, قلقيلية | No verified DC. |
| `Salfit` | Salfit, سلفيت | No verified DC. |
| `Tubas` | Tubas, طوباس | No verified DC. |
| `Gaza` | Gaza City, غزة, Paltel, Digital Communication, NetStream, SpeedClick | Damaged/recovery tracking; no normal operational status without current primary source. |
| `North Gaza` | Beit Hanoun, Beit Lahia, شمال غزة | Damage/rebuild only; concept leads are not projects. |
| `Deir El Balah` | Deir El Balah, دير البلح, الوسطى | Damage/rebuild and telecom emergency nodes only. |
| `Khan Yunis` | Khan Yunis, خان يونس, Al-Aqsa University | Academic concepts/server rooms; no confirmed DC. |
| `Rafah` | Rafah, رفح, Egypt fiber, border connectivity | Connectivity/rebuild lead only. |

Governorate query pattern:

```text
"{division}" "data center" Palestine
"{division}" "Paltel" "data center"
"{Arabic governorate}" "مركز بيانات" OR "استضافة" OR "خوادم"
"{Arabic governorate}" "بالتل" OR "أوريدو" OR "جوال"
site:datacentermap.com/palestine "{division}"
site:inflect.com/datacenters/emea/palestine "{division}"
```

---

## 5. Verification workflow

1. Seed from trade/directories/local Arabic press.
2. Search exact name + Arabic variants.
3. Verify operator identity on official company site, PEX filing, or registry.
4. Verify physical site from operator announcement, Uptime page, government source, Shiraa notice, municipality, or credible trade article.
5. Verify status. `Opening/launch` can be operational; `agreement/MoU/strategy` is planned; `tender` is tendered; Gaza pre-war items need current damage/recovery status.
6. Verify governorate and municipality. Do not map Israeli facilities or Israeli cloud regions into Palestine.
7. Extract scale only when source states it. Palestine records usually have `capacity_mw: null`.
8. Record a confidence note explaining any C-grade or conflict.

Status terms:

```text
افتتاح / إطلاق / تدشين = launched/opened, likely operational
يتم انشاؤه / قيد الإنشاء = under construction
اتفاقية / مذكرة تفاهم = agreement/MoU, planned or construction only if scope says implementation
عطاء / مناقصة = tendered/procurement
انقطاع / توقف / تضرر / تدمير = outage/damaged
إعادة إعمار = reconstruction concept unless award/site exists
```

---

## 6. Cloud and hosting interpretation

- `cloud`, `VPS`, `managed hosting`, `cloud storage`, and `business solutions` are **service claims**, not facility evidence.
- Paltel cloud services can be tied to Paltel data centers only when the source says so or when the service is in the same Paltel data-center announcement.
- Zone cloud/VPS/storage services are a local hosting lead; physical facility evidence remains C/C+.
- Ooredoo Group data-center financing/partnerships are regional and do not prove an Ooredoo Palestine data center.
- Hyperscaler cloud use by Palestinian customers is customer/service usage, not in-country region presence.

Cloud absence queries:

```text
"Palestine" "cloud region"
"Palestine" "availability zone"
AWS Azure Google Oracle "Palestine" "region"
"الحوسبة السحابية" "فلسطين" "مركز البيانات"
```

---

## 7. Source index

Verified private/operator:
- Paltel Group: https://www.paltelgroup.ps/
- Paltel Arabic data-center announcement: https://www.paltelgroup.ps/pginfo/?p=58225
- Uptime award, Paltel Data Center - Al-Bireh: https://uptimeinstitute.com/uptime-institute-awards/datacenter/paltel-data-center--albireh/1115
- DCD Paltel second DC: https://www.datacenterdynamics.com/en/news/paltel-group-opens-second-palestine-data-center/
- Bloomberg/Data Center Knowledge: https://www.datacenterknowledge.com/cloud/palestinian-phone-company-offers-cloud-computing-from-ramallah
- Ooredoo Palestine: https://www.ooredoo.ps/
- Zone Technologies: https://zone.ps/
- DataCenterMap Zone Ramallah: https://www.datacentermap.com/palestine/ramallah/zone-ramallah/

Official / institutional:
- MTDE: https://mtde.gov.ps/
- MTDE DWBG project: https://mtde.gov.ps/home/ads/23032?culture=en-US
- MTDE Cloud/Data Hosting Strategy EOI: https://mtde.gov.ps/home/ads/23047?culture=ar-SA
- National Data Center: https://mtde.online/national-data-center/
- PalCERT: https://mtde.online/palcert/
- World Bank Palestinian Digital Economy Assessment: https://documents1.worldbank.org/curated/en/472671640152521943/pdf/Palestinian-Digital-Economy-Assessment.pdf
- World Bank DWBG restructuring: https://documents1.worldbank.org/curated/en/099121925070028162/pdf/P174355-6255b6cc-7a74-47c6-90c7-e5d7b4e67043.pdf
- Shiraa procurement portal: https://www.shiraa.gov.ps/
- WAFA: https://english.wafa.ps/ and https://www.wafa.ps/
- PCBS ICT release: https://www.pcbs.gov.ps/en/post-details/?postId=26011

Gaza damage / recovery:
- WAFA Paltel Gaza blackout: https://english.wafa.ps/Pages/Details/139337
- 7amleh Gaza telecom damage: https://7amleh.org/post/impact-of-war-on-gaza-s-telecommunications-infrastructure-en
- Al Jazeera Gaza telecom redundancy: https://www.aljazeera.com/news/2023/11/21/keeping-gaza-online-gazas-telecom-heroes-risk-life-and-limb-under-israels-bombs
- World Bank / EU / UN Gaza RDNA 2026: https://thedocs.worldbank.org/en/doc/e539cbf23b348c3d4fc69b8a7e9c9d7d-0280062026/rapid-damage-and-needs-assessment-gaza-strip-april-2026

Directories / C-grade lead surfaces:
- DataCenterMap Palestine: https://www.datacentermap.com/palestine/
- Inflect Palestine: https://inflect.com/datacenters/emea/palestine/
- Data Center Platform: https://datacenterplatform.com/
- Datacenter Catalog / other brokers: use only for aliases and then verify.
