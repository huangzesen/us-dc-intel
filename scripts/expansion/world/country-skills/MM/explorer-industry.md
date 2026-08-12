# MM Explorer Industry - Myanmar Datacenter Discovery Methodology

Date: 2026-08-12. Scope: industry, trade press, operator-parent, vendor, directory, IXP, connectivity, and multilingual search methods for Myanmar datacenter enumeration. Reliability grades: **A** = primary operator/government/cloud-list/IXP/PeeringDB record; **B** = credible trade, local, legal, or parent-company source with named facts; **C** = aggregate market report, directory, broker listing, social post, or weak repost.

## 0. Search model

Myanmar has no public datacenter registry. Enumerate by triangulating:

1. Operator pages: MPT, True IDC Myanmar, MICTDC, MTG, Mytel, Zenlayer, Ocean Wave, IT Spectrum, Campana/UMO, Seanet.
2. IXP evidence: MMIX/PeeringDB maps the strongest facility cluster at True IDC/MICT Park; Mandalay and Naypyidaw POPs are important but need stronger source archiving.
3. Official investment/entity signals: MyCO, DICA/MIC, Region/State Investment Committees, Project Bank.
4. Trade/local press: DatacenterDynamics, W.Media, Frontier Myanmar, Eleven, The Irrawaddy, GNLM, MDN, Myanmar Now, Mizzima, Myanmar Insider, Myanmar Tech Press.
5. Regional-language evidence: Vietnamese for Mytel/Viettel, Thai for True IDC, Chinese for Huawei/Campana/SEZ/investment leads.
6. Connectivity: cable landings, IXPs, carrier-neutral interconnects, satellite teleports, and CDN/cache nodes.

Market context is a **B/C** lead, not facility proof. Myanmar demand is driven by local telecom/cloud needs, banking and government workloads, cybersecurity/data-localization rules, content caching, and poor international latency from foreign cloud regions. Expansion is constrained by power instability, fuel availability, sanctions/compliance risk, currency controls, and conflict/security conditions.

## 1. Language vocabulary and query templates

Core terms:

```text
data center / datacenter / data centre
ဒေတာစင်တာ
IDC / အိုင်ဒီစီ
colocation / co-location / ကိုလိုကေးရှင်း
cloud / ကလောက်
server / server room / ဆာဗာ / ဆာဗာခန်း
hosting / ဟိုစတင်း
Internet Exchange / IXP
license / licence / လိုင်စင်
opening / launch / ဖွင့်ပွဲ
construction / ဆောက်လုပ်ရေး
investment / ရင်းနှီးမြှုပ်နှံမှု
permit / approval / ခွင့်ပြုချက်
power / electricity / လျှပ်စစ် / ဓာတ်အား
```

Division names:

```text
Yangon ရန်ကုန်
Mandalay မန္တလေး
Naypyidaw နေပြည်တော်
Ayeyarwady ဧရာဝတီ
Bago ပဲခူး
Magway မကွေး
Sagaing စစ်ကိုင်း
Tanintharyi တနင်္သာရီ
Chin ချင်း
Kachin ကချင်
Kayah ကယား
Kayin ကရင်
Mon မွန်
Rakhine ရခိုင်
Shan ရှမ်း
```

General templates:

```text
"{division_en}" Myanmar ("data center" OR "datacenter" OR "IDC" OR "colocation" OR "cloud" OR "server room")
"{division_my}" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ကလောက်" OR "ဆာဗာခန်း")
"{company}" Myanmar ("data center" OR "IDC" OR "colocation" OR "racks" OR "MW" OR "Tier")
"{company}" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"{township}" ("data center" OR "ဒေတာစင်တာ") ("opening" OR "launch" OR "ဖွင့်ပွဲ")
"{operator}" ("Yangon" OR "Mandalay" OR "Nay Pyi Taw") ("colocation" OR "server")
```

Stage mapping:

- PTD licence, MIC approval, Project Bank profile: **approved/planned** unless construction/operation is separately shown.
- Groundbreaking/construction permit/utility connection: **construction**.
- Operator service page, official opening, active IXP facility, or colocation price sheet: **operational**.
- Directory, social video, market report: **lead only** unless cross-checked.

## 2. High-signal industry and press sources

| Source | Route | Use | Grade |
|---|---|---|---|
| DatacenterDynamics | https://www.datacenterdynamics.com/ ; `site:datacenterdynamics.com Myanmar data center` | Regional DC/connectivity, operator exits, cable/private-network context. | B |
| W.Media | https://w.media/ ; `site:w.media Myanmar data center` | APAC DC market leads. | B |
| Frontier Myanmar / Frontier Energy | https://www.frontiermyanmar.net/ ; https://energy.frontiermyanmar.com/ | Power, telecom, sanctions, economy context. | B |
| Eleven Myanmar | https://elevenmyanmar.com/ | Power rotations, telecom, business news. | B |
| The Irrawaddy | https://www.irrawaddy.com/ | Digital policy, investment, conflict risk. | B |
| GNLM | https://www.gnlm.com.mm/ | State paper for MIC approvals, official openings, policy. | A-/B; verify claims. |
| MDN | https://www.mdn.gov.mm/en | State news and investment-committee releases. | A-/B |
| Myanmar Now / Mizzima / DVB | site-scoped searches | MyCO restrictions, sanctions, cyber controls, conflict/scam risk. | B |
| Myanmar Insider | https://www.myanmarinsider.com/ | Telecom licensing/regulatory updates. | B |
| Myanmar Tech Press | https://en.myanmartechpress.com/ | Local IT/company/product leads. | B/C |
| MMNOG / MMIX | https://mmnog.net.mm/ ; https://www.mm-ix.net/ | AGM decks, IXP POP facts, member lists. | A for IXP facts when direct. |
| Viettel / Viettel Family | https://viettelfamily.com/ ; https://viettel.com.vn/ | Mytel DC opening and Viettel-operated Myanmar infrastructure. | B+ for parent-family facts; capacity remains claimed. |
| True IDC / Thai tech press | https://www.trueidc.com/en/myanmar | True IDC Myanmar facility and interconnect service leads. | A for operator page. |
| Chinese/state wires | `site:xinhuanet.com Myanmar data center`, Huawei scoped searches | Investment/ICT leads; verify with official/operator source. | B/C |

Queries:

```text
site:datacenterdynamics.com (Myanmar OR Burma) ("data center" OR datacenter OR submarine)
site:w.media Myanmar ("data center" OR "digital infrastructure")
site:gnlm.com.mm ("data center" OR "ICT") ("investment" OR "opening")
site:frontiermyanmar.net ("power" OR "blackout" OR "telecom")
site:elevenmyanmar.com ("YESC" OR "electricity" OR "data center")
"Mytel" "data center" "Yangon" "26/8"
"True IDC" "Myanmar" "MICT Park"
```

## 3. Market and aggregate sources

Use these for leads and context only. Do not let them set final location/status/capacity without cross-check.

| Source | URL/search | Use | Grade |
|---|---|---|---|
| Mordor Intelligence Myanmar DC report | https://www.mordorintelligence.com/industry-reports/myanmar-data-center-market | Market sizing and operator list leads. | C |
| US ITA Burma Digital Economy | https://www.trade.gov/country-commercial-guides/burma-digital-economy | Digital-economy, blackouts, fuel/internet restriction context. | B |
| DLA Piper Data Protection | https://www.dlapiperdataprotection.com/?c=MM&t=law | No general data-protection law; related legal framework. | B |
| DataCenterMap | https://www.datacentermap.com/myanmar/ | Facility discovery; Myanmar total/market counts are leads. | C |
| Baxtel | https://baxtel.com/data-center/true-idc-myanmar-mict-park ; https://baxtel.com/data-center/burst-myanmar | True IDC and Burst leads; cross-check with operator/PeeringDB/SEZ. | C |
| PeeringDB | https://www.peeringdb.com/ix/2102 ; https://www.peeringdb.com/fac/5031 | IX and facility mapping. | A for active self-reported IXP/facility facts. |
| Inflect / Datacenters.com / Cloudscene | site-scoped Myanmar searches | Additional leads. | C |
| Blackridge and tender trackers | site-scoped Myanmar DC searches | Announced/upcoming leads; verify. | C |

## 4. Operator and facility seed list

| Operator/facility | URLs | Evidence handling |
|---|---|---|
| True IDC Myanmar | https://www.trueidc.com/en/myanmar ; https://www.peeringdb.com/fac/5031 | Operator page confirms a Myanmar DC at MICT Park, Yangon, established 2015, colo/managed services, 99.95% SLA claim. PeeringDB confirms Building 17, Ground Floor, MICT Park, Hlaing, Yangon and MMIX Yangon. **A** for existence/location; **B** for marketing SLA/certification claims. |
| MICT Data Center | https://mictdc.com.mm/mict-data-center/ | MICTDC page confirms Main Building, ICT Park, Universities' Hlaing Campus, Hlaing Township, Yangon; claims Tier III and up to 162 racks. **A** for existence/location; **B** for Tier/capacity unless certificate found. |
| MPT Data Center / MPT Cloud | https://mpt.com.mm/en/business-home/data-center-en/ ; https://mpt.com.mm/en/business-home/b2b-cloud-service/ | MPT says it provides DC service in Yangon (Hantharwady; Bayintnaung new/ready) and Naypyitaw (Dekkhina), and IaaS hosted in a Myanmar data center. **A**. |
| Mytel Data Center | https://viettelfamily.com/news/mytel-khai-truong-data-center-so-1-tai-myanmar | Viettel Family says Mytel opened Myanmar's largest DC in Yangon on 2023-08-26, Tier 3-standard, 600 racks expandable to 1,000. **B+**; capacity is claimed, not certified. |
| MTG DC / MTG Datacenter | https://www.mtg.com.mm/co-location-services.php ; https://www.dica.gov.mm/23016/ ; https://corporate.mtg.com.mm/ | MTG page gives NayPyiTaw MTGDC colocation pricing/features; DICA confirms official field visit to MTG DC at Dekkhinathiri Township in 2019. **A**. |
| e-Government Integrated Data Center | https://www.projectbank.gov.mm/en/profiles/activity/PB-ID-1126/ | Government project for main national data center in Naypyidaw and DR center in Yangon. **A** for planned/approved lead; status must be verified. |
| Ocean Wave IDC / MMIX Mandalay | MMIX/MMNOG materials; PeeringDB/DataCenterMap leads; social opening video | Mandalay IXP/facility lead. **B** until archived official MMIX/operator source is cited for exact address/status. |
| IT Spectrum DC-2 | MMIX AGM materials | Naypyidaw POP/facility lead. **B** until operator/official confirmation. |
| Zenlayer Yangon | https://cloud.zenlayer.com/datacenters/yangon | Confirms Zenlayer service availability in Yangon; physical host not disclosed. **A-** for service city, **B/C** for host-facility inference. |
| Burst Myanmar / Thilawa SEZ Datacenter | https://baxtel.com/data-center/burst-myanmar ; https://datacentercatalog.com/myanmar-burma/thilawa-sez-datacenter ; search Uptime/Thilawa | Directory lead in Thilawa SEZ. **C** until operator, SEZ, permit, or Uptime listing is verified. |
| Campana / UMO / SIGMAR | https://www.submarinenetworks.com/en/systems/intra-asia/sigmar ; Delta case studies | Thanlyin cable landing and modular/cable-infrastructure lead. Separate cable landing station from commercial DC unless customer colo is proven. **B/C**. |
| Seanet teleport | https://seanetmyanmar.com/teleport.php?idx=4 | MICT Park satellite earth-station lead; not a colocation DC by itself. **B/C**. |
| GDMS | https://www.global-dms.com/colocation-services/ | Claims Myanmar colocation services but no named facility in the verified page. **C**. |

Operator census for legal/SPV matching: MPT, Mytel / Telecom International Myanmar, Atom Myanmar (ex-Telenor), U9 (ex-Ooredoo Myanmar), True IDC Myanmar, MICTDC, Myanmar Technology Gateway / MTG DC, Ocean Wave, IT Spectrum, Campana, Burst Myanmar, Seanet, 5BB/Global Net, Frontiir, Redlink, NetCom, YGATE, Golden Internet.

## 5. Connectivity evidence

Connectivity clusters are strong search pivots but not DC records on their own.

- Submarine Networks lists Myanmar cables including SMW3 at Pyapon and SMW5/AAE-1 at Ngwe Saung: https://www.submarinenetworks.com/en/stations/asia/myanmar
- UMO/SIGMAR connects Tuas, Singapore and Thanlyin, Myanmar, 2,227 km: https://www.submarinenetworks.com/en/systems/intra-asia/sigmar
- TeleGeography/Submarine Cable Map has current landing pages for UMO, SMW5, and Ngwe Saung: https://www.submarinecablemap.com/
- MMIX Yangon at MICT Park/True IDC: https://www.peeringdb.com/ix/2102 and https://www.peeringdb.com/fac/5031
- Mandalay and Naypyidaw IXP leads should be checked through MMIX/MMNOG decks, PeeringDB, and operator pages before recording.
- Border-fiber pivots: Muse/Ruili (China), Myawaddy/Mae Sot and Tachileik/Mae Sai (Thailand), Tamu (India). These are edge/cache/server-room leads only.

Queries:

```text
site:submarinenetworks.com Myanmar "Ngwe Saung" OR "Thanlyin" OR "Pyapon"
"UMO" OR "SIGMAR" "Thanlyin" "True IDC" OR "Yangon"
"AAE-1" OR "SEA-ME-WE 5" "Ngwe Saung" "data center"
"MMIX" ("Yangon" OR "Mandalay" OR "Naypyitaw" OR "Nay Pyi Taw")
site:peeringdb.com Myanmar "True IDC" OR "Ocean Wave" OR "IT Spectrum"
```

Grade: **A** for cable/IX existence from primary databases; **B/C** for facility inference.

## 6. Hyperscaler and cloud handling

As of 2026-08-12, official region lists for AWS, Google Cloud, Azure, Alibaba Cloud, and Huawei Cloud do not list a Myanmar public cloud region. Record:

- In-country cloud: MPT Cloud (IaaS hosted at a Myanmar data center).
- In-country colo and interconnect: True IDC Myanmar, MPT, MICTDC, MTG, Mytel, Zenlayer Yangon.
- Foreign cloud access: cloud interconnect/direct links through Singapore/Thailand/other APAC regions.

Queries:

```text
"Myanmar" "cloud region" ("AWS" OR "Google Cloud" OR "Azure" OR "Alibaba Cloud" OR "Huawei Cloud")
"MPT Cloud" "hosted at Data Center in Myanmar"
"True IDC" Myanmar ("Direct Connect" OR "Interconnect" OR "Express Connect")
"Zenlayer" Yangon "Cloud Connect"
```

## 7. Complete division playbook

| Division | Priority localities | Seeds and search posture |
|---|---|---|
| Yangon Region | Hlaing/MICT Park, Hantharwady/Bayintnaung, downtown, Mayangone/Kamayut, Thanlyin, Thilawa/Kyauktan | Highest priority. Confirm True IDC, MICTDC, MPT Yangon, Mytel, Zenlayer, MMIX Yangon, Burst/Thilawa lead, Campana/UMO lead, Seanet. |
| Naypyidaw UT | Dekkhinathiri/Dekkhina Thiri, Zabuthiri, Pyinmana, ministry zone | High priority. Confirm MTG DC, MPT Naypyitaw, e-GIDC, IT Spectrum DC-2/MMIX POP. |
| Mandalay Region | Mandalay city, Chanayethazan, Aungmyaythazan, Pyigyidagun, Amarapura, Pyin Oo Lwin | High/medium priority. Verify Ocean Wave IDC/MMIX Mandalay and any MMC/Myanmar Country DC leads. |
| Ayeyarwady Region | Ngwe Saung, Pyapon, Pathein | Cable landing sweep: SMW5/AAE-1 at Ngwe Saung, SMW3 at Pyapon. Do not convert cable station to DC without facility evidence. |
| Bago Region | Bago, Pyay, Yangon corridor industrial zones | Negative sweep for spillover DR/industrial telco rooms; no confirmed DC seed. |
| Magway Region | Magway/Magwe, Pakokku, Chauk | Negative sweep for government/university/telco edge; no confirmed seed. |
| Sagaing Region | Sagaing, Monywa, Tamu, Naga SAZ | Negative sweep plus India-border fiber; conflict risk. |
| Tanintharyi Region | Dawei, Myeik, Kawthaung | Dawei SEZ is a weak policy lead; no confirmed seed. |
| Chin State | Hakha, Falam | Lowest-signal negative sweep. |
| Kachin State | Myitkyina, Bhamo, China border | Search telecom/backhaul and border-fiber leads; no confirmed commercial seed. |
| Kayah State | Loikaw | Lowest-signal negative sweep; conflict/access risk. |
| Kayin State | Hpa-An, Myawaddy, Shwe Kokko | Separate legitimate DCs from illicit server-farm/scam-hub reporting. |
| Mon State | Mawlamyine/Mawlamyaing, Thaton | Regional telco-node sweep; no confirmed seed. |
| Rakhine State | Sittwe, Kyaukphyu SEZ | SEZ/digital plans are leads only; no confirmed DC seed. |
| Shan State | Taunggyi, Muse, Tachileik, Laukkai/Kokang, Wa areas | Border connectivity plus illicit-server risk; verify legal owner/status carefully. |

Per-division query pack:

```text
"{division_en}" ("data center" OR "datacenter" OR "IDC" OR "colocation" OR "cloud" OR "server room")
"{division_my}" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ကလောက်" OR "ဆာဗာခန်း")
"{division_en}" ("MPT" OR "Mytel" OR "Atom" OR "U9" OR "MMIX") ("data center" OR "server" OR "NOC")
"{division_en}" ("Internet Exchange" OR "IXP" OR "cable landing" OR "fiber")
"{division_en}" ("MIC" OR "investment committee" OR "DICA") ("data center" OR "ICT")
```

## 8. Evidence rules and pitfalls

- Do not infer a datacenter from mobile-network coverage or a telco office.
- Do not double count IXP nodes, cloud PoPs, CDN caches, and underlying host facilities.
- Treat "Myanmar" marketing as Yangon unless the page names Naypyidaw or Mandalay; MPT and MTG are important Naypyidaw exceptions.
- Treat rack/MW/Tier/SLA claims as **B** unless an official certificate or engineering filing confirms them.
- Directory-only Burst/Thilawa, GDMS, and broker listings stay **C** until cross-checked.
- Cable landing stations are telecom infrastructure; record as DCs only when a source names commercial colocation, server hosting, or a data-center building.
- Cybersecurity Law localization is a demand signal, not proof of construction.
- Scam-hub/server-farm areas in Kayin/Shan require legal-owner and lawful-service verification before inclusion.
- Conflict, sanctions, power, and fuel risks should be recorded as risk fields, not used to erase verified facilities.

## 9. Minimal workflow

1. Seed from operator-primary pages and PeeringDB/MMIX.
2. Search MyCO/DICA/MIC/Project Bank for every entity and project.
3. Search high-signal press and regional-language sources for openings, construction, exits, and rebrands.
4. Run cable/IXP/connectivity pivots for Yangon, Ayeyarwady, Mandalay, Naypyidaw, Shan, and Kayin.
5. Run all 15 division sweeps with English and Burmese terms.
6. Assign field-level grades. Use **no_projects** only after logging negative searches, not by assumption.
