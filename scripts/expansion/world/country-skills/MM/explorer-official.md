# MM Explorer Official - Myanmar Datacenter Enumeration Methodology

Date: 2026-08-12. Scope: official, regulator, utility, registry, cloud-list, IXP, and operator-primary methods for enumerating datacenter facilities and projects in Myanmar (MM). Reliability grades: **A** = official government/registry/law/utility/cloud-list, operator-primary page, or primary IXP/PeeringDB fact; **B** = strong trade, legal, or operator-parent source that names a project fact; **C** = directory, aggregate, social, broker, or unsourced press lead.

## 0. Administrative and market baseline

Myanmar has **15 first-level units for this census**: 7 Regions (Ayeyarwady, Bago, Magway, Mandalay, Sagaing, Tanintharyi, Yangon), 7 States (Chin, Kachin, Kayah, Kayin, Mon, Rakhine, Shan), and the Naypyidaw Union Territory. Self-administered zones/divisions sit below or within these units for practical enumeration; do not count them as extra first-level coverage unless a source names the self-administered area.

The market is small and highly concentrated in Yangon, Naypyidaw, and Mandalay. There is no national datacenter registry, no DC-specific public approval list, and no usable public national building-permit search. Build the census by joining:

- PTD telecom law/licensing framework.
- DICA/MyCO legal-entity searches and MIC/Region-State investment approval releases.
- YCDC/YBPS building-permit evidence for Yangon only, plus city/township permit news where available.
- MONREC/ECD environmental records only if a project, power plant, substation, or SEZ filing names the facility.
- MOEP/YESC/MESC/ESE power evidence for feasibility and locality validation.
- Operator-primary pages, MMIX/PeeringDB, and official cloud-region lists.

Search in English and Burmese. High-value Burmese pivots: `ဒေတာစင်တာ` (data center), `အိုင်ဒီစီ` (IDC), `ကလောက်` (cloud), `ဆာဗာ` / `ဆာဗာခန်း` (server/server room), `လိုင်စင်` (licence), `ရင်းနှီးမြှုပ်နှံမှု` (investment), `ဆောက်လုပ်ရေး` (construction), `ခွင့်ပြုချက်` (permit), `လျှပ်စစ်` (electricity), `ရန်ကုန်` (Yangon), `မန္တလေး` (Mandalay), `နေပြည်တော်` (Naypyidaw). Also search Vietnamese for Mytel/Viettel, Thai for True IDC, and Chinese for Huawei/Campana/SEZ leads.

## 1. Official source surfaces

### 1.1 PTD / MOTC telecom regulation

Primary routes:

- PTD: https://www.ptd.gov.mm/
- Telecommunications Law 2013 English PDF: https://ptd.gov.mm/Uploads/Services/Attach/22018/2096121422018_2.+Telecom+Law%28Eng%29.pdf
- Licensing Rules mirror: https://myanmar-law-library.org/IMG/pdf/1_-_mcit_-_final_licensing_rules_-_122013_clean.pdf
- NFS licence template: https://www.ptd.gov.mm/ckfinder/userfiles/files/ns+license+template.pdf
- Spectrum roadmap: https://ptd.gov.mm/Uploads/LawFP/Attach/22018/1869221022018_1.+Spectrum+Roadmap.pdf

Use: PTD proves telecom-law categories and regulator identity. Myanmar telecom licences cover Network Facilities Service, Network Service Provider, and Service / Value-Added Service Provider activities; datacenter-only space/power rental may not itself identify as a telecom licence. PTD is not a reliable public licensee database, so use it as legal context and join licence mentions to MyCO, MIC, operator pages, and press.

Queries:

```text
site:ptd.gov.mm ("data center" OR "datacenter" OR "IDC" OR "colocation")
site:ptd.gov.mm "Network Facilities Service" Myanmar license
site:ptd.gov.mm "Service and Value Added" license Myanmar
"PTD" Myanmar "{operator}" ("licence" OR "license")
"ဒေတာစင်တာ" "လိုင်စင်" Myanmar
```

Grade: **A** for laws, rules, templates, and official PTD notices; **B/C** for inferred facility ownership unless another primary source names the facility.

### 1.2 DICA, MyCO, MIC, and Region/State investment committees

Primary routes:

- DICA: https://www.dica.gov.mm/
- MyCO company search: https://www.myco.dica.gov.mm/corp/search.aspx
- GNLM state paper for MIC batches: https://www.gnlm.com.mm/
- Myanmar Digital News: https://www.mdn.gov.mm/en
- Project Bank: https://www.projectbank.gov.mm/
- DICA field-visit record for MTG DC: https://www.dica.gov.mm/23016/

Use: MyCO is the official legal-entity search surface. Search exact SPV names and variants: `True IDC Myanmar`, `True Internet Data Center`, `MPT`, `Myanmar Posts and Telecommunications`, `Telecom International Myanmar`, `Mytel`, `MTG DC`, `Myanmar Technology Gateway`, `MICTDC`, `Myanmar ICT Development Corporation`, `Ocean Wave`, `IT Spectrum`, `Burst Myanmar`, `Campana`, `Nine Communications`, `Atom Myanmar`. DICA/MIC records are **A** when they name a DC project, entity, township, or field visit; news summaries without facility detail are only batch leads.

Confirmed official leads:

- MTG DC Co., Ltd: DICA reported a Nay Pyi Taw Investment Monitoring Team field visit to MTG DC's data center and related services at Dekkhinathiri Township, Nay Pyi Taw on 2019-08-29. Grade **A** for project/entity/locality.
- Project Bank e-Government Integrated Data Center: https://www.projectbank.gov.mm/en/profiles/activity/PB-ID-1126/ describes a main national-level data center in Naypyidaw and a disaster recovery center in Yangon. Grade **A** for government project lead; verify current status before recording operational capacity.

Queries:

```text
site:dica.gov.mm ("data center" OR "datacenter" OR "ICT" OR "IT services")
site:dica.gov.mm "MTG DC"
site:projectbank.gov.mm "data center" Myanmar
site:gnlm.com.mm ("Myanmar Investment Commission" OR MIC) "data center"
site:mdn.gov.mm "data center" investment
"Yangon Region Investment Committee" "data center"
myco.dica.gov.mm "{company name}"
```

Grade: **A** for official entity and approval facts; **B** for state-paper summaries that omit facility identifiers.

### 1.3 Construction permits and city development committees

Primary routes:

- Yangon Building Permit System (YBPS): https://ybps.ycdc.gov.mm/
- YCDC: https://www.ycdc.gov.mm/
- Mandalay City Development Committee: verify current portal before use; no reliable keyword public permit search was confirmed.
- Naypyidaw Development Committee / Nay Pyi Taw Council: no public keyword permit search confirmed.
- Ministry of Construction / DHSHD: use only when a project is named in an official release.

Use: YBPS is real and usable for permit process/statistics, but not as a DC keyword database. Treat aggregate statistics as locality context only. A building permit becomes **A** facility evidence only when it names the owner/project, plot, building, or township tied to the DC.

Queries:

```text
site:ybps.ycdc.gov.mm "Building Permit"
site:ybps.ycdc.gov.mm "{township}"
"YCDC" "building permit" "{company}" Myanmar
"building completion certificate" "{project}" Yangon
"Mandalay City Development Committee" "{company}" "data center"
"Nay Pyi Taw Development Committee" "data center"
```

Grade: **A** for named permits; **C** for generic permit-process or statistic pages.

### 1.4 Environment and SEZ review

Primary routes:

- MONREC: https://www.monrec.gov.mm/
- Environmental Conservation Law / EIA Procedure: search MONREC/ECD and Myanmar Law Library.
- Thilawa SEZ Management Committee: https://www.thilawasez.gov.mm/

Use: Datacenters are not reliably surfaced in public EIA lists. Search EIA/environment records by project/entity and by related power/substation/generator works. For Thilawa, use SEZ committee pages and investor lists as official context. Absence of EIA evidence is not negative evidence.

Queries:

```text
site:monrec.gov.mm ("data center" OR "EIA" OR "environmental impact")
"Environmental Impact Assessment" Myanmar "{company}" ("data center" OR "Thilawa")
site:thilawasez.gov.mm ("data center" OR "datacenter" OR "ICT" OR "Burst")
"Thilawa" "{company}" "environmental"
```

Grade: **A** if official environmental/SEZ evidence names the project; **C** for directory-only Thilawa DC leads.

### 1.5 Power and energy evidence

Primary routes:

- MOEP: https://www.moep.gov.mm/
- YESC: https://www.yesc.gov.mm/ (verify per crawl; official pages can be intermittent)
- MESC and ESE links are usually reachable through MOEP pages.
- US ITA Burma Digital Economy guide: https://www.trade.gov/country-commercial-guides/burma-digital-economy

Use: Utility sources prove tariff, transformer/meter processes, outages, and locality power conditions; they rarely name datacenters. Myanmar grid reliability is a material operating constraint. Treat UPS/generator claims on operator pages as facility features, but do not infer MW load unless stated.

Queries:

```text
site:moep.gov.mm "YESC" "MESC" "Electricity Supply Enterprise"
site:yesc.gov.mm "{township}" ("မီး" OR "လျှပ်စစ်" OR "rotation")
"Yangon Electricity Supply Corporation" "{township}" "data center"
"Myanmar" "electricity blackouts" "data center"
site:trade.gov "Burma" "Digital Economy" blackouts fuel shortages
```

Grade: **A** for official utility/tariff/outage statements; **B** for US ITA and strong press on reliability context.

### 1.6 Cybersecurity and data-localization drivers

Primary and strong secondary routes:

- Cybersecurity Law 1/2025, part 1: https://www.moi.gov.mm/moi%3Aeng/news/16633
- Cybersecurity Law 1/2025, part 2: https://www.moi.gov.mm/moi%3Aeng/news/16656
- Baker McKenzie analysis: https://connectontech.bakermckenzie.com/myanmar-cybersecurity-law-enacted-on-1-january-2025/
- Hogan Lovells in-force note: https://www.hlc.com/en/publications/myanmars-cybersecurity-law-comes-into-effect-key-implications-for-international-stakeholders
- DLA Piper Myanmar data-protection tracker: https://www.dlapiperdataprotection.com/?c=MM&t=law

Use: The law is a demand and compliance driver, not a facility list. It creates registration/licensing obligations for digital platform and cybersecurity service providers, addresses critical information infrastructure, and came into force on 2025-07-30 per legal analyses. DLA Piper states Myanmar has no general standalone data-protection law. Always separate legal demand from physical DC evidence.

Queries:

```text
site:moi.gov.mm "Cybersecurity Law" "digital platform"
"Cybersecurity Law" Myanmar "data localization" 2025
site:bakermckenzie.com Myanmar cybersecurity law 2025 "100,000"
site:dlapiperdataprotection.com Myanmar "no general data protection law"
```

Grade: **A** for law text; **B** for law-firm interpretation.

## 2. Cloud-region and cloud-connectivity handling

No official AWS, Google Cloud, Microsoft Azure, Alibaba Cloud, Tencent Cloud, or Huawei Cloud public region is listed in Myanmar as of 2026-08-12. Verify against official global infrastructure pages before each run:

- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Google Cloud locations: https://cloud.google.com/about/locations
- Azure geographies/regions: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Alibaba Cloud regions: https://www.alibabacloud.com/help/en/ecs/product-overview/regions-and-zones
- Huawei Cloud global regions: https://www.huaweicloud.com/intl/en-us/about/regions/

Do not create a hyperscaler-region record for Myanmar. Record local cloud/colo/interconnect evidence instead:

| Provider | Primary URL | What it proves | Grade |
|---|---|---|---|
| MPT Cloud | https://mpt.com.mm/en/business-home/b2b-cloud-service/ | IaaS hosted at a data center in Myanmar. | A for service existence; B for SLA/marketing claims. |
| MPT Data Center | https://mpt.com.mm/en/business-home/data-center-en/ | MPT provides data-center service in Yangon (Hantharwady; Bayintnaung new/ready) and Naypyitaw (Dekkhina). | A |
| True IDC Myanmar | https://www.trueidc.com/en/myanmar | Myanmar colo/managed services at MICT Park, Yangon, established 2015; SLA/industry-certification marketing. | A for facility/service; B for certification equivalence. |
| Zenlayer Yangon | https://cloud.zenlayer.com/datacenters/yangon | Bare metal/cloud-connectivity availability in Yangon; host facility not named. | A- for Yangon presence; B/C for inferred physical host. |

Queries:

```text
"Myanmar" "cloud region" ("AWS" OR "Azure" OR "Google Cloud" OR "Alibaba Cloud" OR "Huawei Cloud")
"MPT Cloud" "hosted at Data Center in Myanmar"
"True IDC" Myanmar ("AWS Direct Connect" OR "Google Cloud Interconnect" OR "Alibaba Cloud Express Connect")
"Zenlayer" Yangon ("bare metal" OR "Cloud Connect")
```

## 3. Primary facility seeds to enumerate first

| Facility/operator | Primary source(s) | Locality | Evidence and grade |
|---|---|---|---|
| True IDC Myanmar | https://www.trueidc.com/en/myanmar ; PeeringDB facility https://www.peeringdb.com/fac/5031 | Building 17, Ground Floor, MICT Park, Hlaing Township, Yangon | Operator says first commercial Myanmar DC, established 2015, colo/managed services; PeeringDB gives address and MMIX Yangon exchange. **A** for existence/location. |
| MICT Data Center | https://mictdc.com.mm/mict-data-center/ | Main Building, ICT Park, Universities' Hlaing Campus, Hlaing Township, Yangon | Operator page says Tier III, up to 162 racks, MICT Park, operated with Japanese expert support. **A** for existence/location; **B** for Tier/capacity if not third-party certified. |
| MPT Data Centers | https://mpt.com.mm/en/business-home/data-center-en/ ; https://mpt.com.mm/en/business-home/b2b-cloud-service/ | Yangon (Hantharwady/Bayintnaung) and Naypyitaw (Dekkhina) | MPT official page names operating service locations and colocation features; cloud page says IaaS hosted in Myanmar. **A**. |
| Mytel Data Center | https://viettelfamily.com/news/mytel-khai-truong-data-center-so-1-tai-myanmar | Yangon | Viettel-family news says opening on 2023-08-26 in Yangon, Tier 3-standard claim, 600 racks expandable to 1,000. **B+**; treat capacity as claimed. |
| MTG DC / MTG Datacenter | https://www.mtg.com.mm/co-location-services.php ; https://www.dica.gov.mm/23016/ | Dekkhinathiri / Dekkhina Thiri, Naypyidaw | MTG page states NayPyiTaw MTGDC colocation; DICA field visit confirms MTG DC project at Dekkhinathiri. **A**. |
| e-Government Integrated Data Center | https://www.projectbank.gov.mm/en/profiles/activity/PB-ID-1126/ | Main DC in Naypyidaw; DR center in Yangon | Government Project Bank project lead. **A** for planned/approved government project; verify implementation status separately. |
| MMIX Yangon at True IDC | https://www.peeringdb.com/ix/2102 ; https://www.peeringdb.com/fac/5031 | MICT Park, Hlaing, Yangon | PeeringDB names MMIX POP at MICT Park and facility at True IDC. **A** for IXP/facility mapping. |
| Ocean Wave IDC / MMIX Mandalay | MMIX materials and PeeringDB/DataCenterMap leads; Facebook opening video is social lead | Mandalay | Operational IXP/facility lead; primary web evidence is weaker than True IDC. **B** until official MMIX PDF/operator page is archived with URL and facts. |
| IT Spectrum DC-2 / MMIX Naypyitaw POP | MMIX AGM materials | Naypyidaw | POP/facility lead. **B** unless official operator/government page names it. |
| Burst Myanmar / Thilawa SEZ Datacenter | https://baxtel.com/data-center/burst-myanmar ; https://datacentercatalog.com/myanmar-burma/thilawa-sez-datacenter ; verify against Thilawa/Uptime | Thilawa SEZ, Thanlyin/Kyauktan area, Yangon Region | Directory lead only unless confirmed by SEZ, operator, Uptime award, or permit. **C** now; do not promote without primary evidence. |
| Campana cable landing / modular DC lead | https://www.submarinenetworks.com/en/systems/intra-asia/sigmar ; Delta case-study pages | Thanlyin/Yangon corridor | UMO/SIGMAR landing is real; modular data-center case studies are infrastructure leads, not automatically commercial colo. **B/C**. |

Avoid double counting: MMIX nodes, Zenlayer PoPs, cloud interconnects, and cable landing stations may sit inside another facility. Match by physical locality, operator, address, and IXP/ASN evidence before creating separate records.

## 4. Complete division-by-division strategy

### Yangon Region

Priority localities: Hlaing/MICT Park, Hantharwady/Bayintnaung, downtown carrier buildings, Mayangone/Kamayut/Sanchaung, Thanlyin and Thilawa SEZ/Kyauktan. Power: YESC. Confirmed/seed facilities: True IDC Myanmar, MICT Data Center, MPT Yangon/Hantharwady/Bayintnaung, Mytel DC, Zenlayer Yangon, MMIX Yangon, Burst/Thilawa lead, Campana/UMO lead, Seanet MICT Park satellite lead.

```text
"MICT Park" ("data center" OR "IDC" OR "colocation")
"True IDC" Myanmar MICT Park Hlaing
"MPT" "Bayintnaung Data Center" OR "Hantharwady"
"Mytel" "data center" Yangon 2023
"ရန်ကုန်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Thilawa" OR "Thanlyin" ("data center" OR "datacenter" OR "cable landing")
site:ybps.ycdc.gov.mm (Hlaing OR Thanlyin OR Mayangone OR Bayintnaung)
```

### Naypyidaw Union Territory

Priority localities: Dekkhinathiri/Dekkhina Thiri, Zabuthiri, Pyinmana, ministry zone. Confirmed/seed facilities: MTG DC, MPT Naypyitaw/Dekkhina, e-Government Integrated Data Center, IT Spectrum DC-2/MMIX Naypyitaw POP.

```text
"Nay Pyi Taw" OR "Naypyidaw" ("data center" OR "datacenter" OR "IDC" OR "server room")
"နေပြည်တော်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ဆာဗာခန်း")
"MTG DC" "Dekkhinathiri"
"MPT" "Naypyitaw" "Dekkhina" "Data Center"
"e-Government Integrated Data Center" Myanmar
"IT Spectrum" "DC-2" MMIX
```

### Mandalay Region

Priority localities: Mandalay city, Chanayethazan, Aungmyaythazan, Pyigyidagun, Amarapura/Myitnge, Pyin Oo Lwin. Seed: Ocean Wave IDC/MMIX Mandalay; possible MMC DC / Myanmar Country DC leads require verification.

```text
"Mandalay" ("data center" OR "datacenter" OR "IDC" OR "colocation")
"မန္တလေး" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ဆာဗာခန်း")
"Ocean Wave" Mandalay IDC
"MMIX" Mandalay "Ocean Wave"
"Mandalay City Development Committee" "data center"
```

### Ayeyarwady Region

Priority localities: Ngwe Saung cable landing, Pathein. Connectivity: SMW5 and AAE-1 at Ngwe Saung; SMW3 is listed by Submarine Networks at Pyapon. Treat cable landing stations as telecom infrastructure, not commercial DCs unless a colo/server facility is named.

```text
"Ayeyarwady" OR "Irrawaddy" ("data center" OR "IDC" OR "server room")
"ဧရာဝတီ" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Ngwe Saung" ("cable landing" OR "landing station" OR "data center")
"Pyapon" "SMW3" "data center"
```

### Bago Region

Priority localities: Bago city, Pyay corridor, industrial zones near Yangon. No confirmed DC seed; sweep for spillover industrial/DR facilities and telecom server rooms.

```text
"Bago" OR "Pegu" ("data center" OR "IDC" OR "server room" OR "cloud")
"ပဲခူး" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ဆာဗာခန်း")
"Bago" ("MPT" OR "Mytel" OR "Atom" OR "U9") "data center"
```

### Magway Region

Priority localities: Magway/Magwe, Pakokku, Chauk energy corridor. No confirmed DC seed; sweep government DR, universities, and telco edge only.

```text
"Magway" OR "Magwe" ("data center" OR "IDC" OR "server room")
"မကွေး" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ဆာဗာခန်း")
"Magway" "ICT" "investment" Myanmar
```

### Sagaing Region

Priority localities: Sagaing, Monywa, Tamu/India corridor, Naga SAZ. No confirmed DC seed; conflict risk is high, so verify current control/access before field assumptions.

```text
"Sagaing" OR "Monywa" ("data center" OR "IDC" OR "server room")
"စစ်ကိုင်း" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Tamu" Myanmar ("fiber" OR "Internet Exchange" OR "data center")
```

### Tanintharyi Region

Priority localities: Dawei, Myeik, Kawthaung; Dawei SEZ is a policy/infrastructure lead only. No confirmed DC seed.

```text
"Tanintharyi" OR "Tenasserim" OR "Dawei" ("data center" OR "IDC" OR "server room")
"တနင်္သာရီ" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Dawei SEZ" ("ICT" OR "data center" OR "digital")
```

### Chin State

Priority localities: Hakha, Falam; lowest signal. No confirmed DC seed.

```text
"Chin State" OR "Hakha" ("data center" OR "IDC" OR "server room")
"ချင်း" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ" OR "ဆာဗာခန်း")
```

### Kachin State

Priority localities: Myitkyina, Bhamo, China-border routes. No confirmed commercial DC seed; check telecom/backhaul nodes and government server rooms.

```text
"Kachin" OR "Myitkyina" ("data center" OR "IDC" OR "server room")
"ကချင်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Myitkyina" ("MPT" OR "Mytel" OR "fiber") "data center"
```

### Kayah State

Priority localities: Loikaw. No confirmed DC seed; conflict/access risk high.

```text
"Kayah" OR "Loikaw" ("data center" OR "IDC" OR "server room")
"ကယား" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
```

### Kayin State

Priority localities: Hpa-An, Myawaddy, Shwe Kokko corridor. Treat server-farm/scam-hub reports separately from legitimate commercial DC enumeration.

```text
"Kayin" OR "Karen State" OR "Hpa-An" OR "Myawaddy" ("data center" OR "IDC" OR "server room")
"ကရင်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Myawaddy" ("server farm" OR "data center" OR "online scam")
```

### Mon State

Priority localities: Mawlamyine/Mawlamyaing, Thaton. No confirmed DC seed; sweep regional telco nodes.

```text
"Mon State" OR "Mawlamyine" OR "Mawlamyaing" ("data center" OR "IDC" OR "server room")
"မွန်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
```

### Rakhine State

Priority localities: Sittwe, Kyaukphyu SEZ. SEZ/digital plans are not DC projects without permit/operator evidence.

```text
"Rakhine" OR "Arakan" OR "Sittwe" OR "Kyaukphyu" ("data center" OR "IDC" OR "server room")
"ရခိုင်" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Kyaukphyu SEZ" ("ICT" OR "data center" OR "digital")
```

### Shan State

Priority localities: Taunggyi, Muse/Ruili corridor, Tachileik/Mae Sai, Laukkai/Kokang, Wa areas. High border-connectivity and illicit-server risk; verify legal owner/status before recording.

```text
"Shan State" OR "Taunggyi" OR "Muse" OR "Tachileik" OR "Laukkai" ("data center" OR "IDC" OR "server room")
"ရှမ်း" ("ဒေတာစင်တာ" OR "အိုင်ဒီစီ")
"Muse" OR "Tachileik" ("fiber" OR "Internet Exchange" OR "data center")
```

## 5. Reliability and status rules

| Source | Grade | Use |
|---|---|---|
| PTD laws, licence rules/templates, notifications | A | Legal framework and licence category facts. |
| MyCO/DICA/MIC/Project Bank | A | Entity, project, approval, monitoring, and government-program facts. |
| YCDC/YBPS/MCDC/NDC/DHSHD named permit | A | Construction evidence only when the facility/project is named. |
| MOEP/YESC/MESC/ESE | A | Power/tariff/outage/locality context; rarely facility proof. |
| MONREC/ECD/SEZ official records | A | Environmental/SEZ status when the project is named. |
| Operator-primary pages | A for existence/location/service; B for capacity/Tier/SLA marketing unless certified | Facility seed and current service. |
| MMIX/PeeringDB | A for IXP and facility mapping; B for implied host if not separately named | Avoid double counting. |
| Law-firm/regulatory analysis | B | Interpretation; verify on law text. |
| Trade/local press | B | Discovery and event facts; cross-check. |
| Directories/aggregators/social/brokers | C | Leads only. |

Status vocabulary:

- **Operational**: operator service page, official opening, active IXP/PeeringDB facility, or verified customer-facing colocation/cloud service.
- **Construction**: named permit, utility connection, official groundbreaking, or SEZ construction notice.
- **Approved/planned**: MIC/Project Bank/official approval or policy project without proof of operation.
- **Lead only**: directory/social/marketing mention without primary confirmation.
- **No projects found**: only after English+Burmese sweep, operator sweep, official registry/approval search, and IXP/connectivity search for that division.

## 6. Official-first workflow

1. Extract confirmed facilities from operator-primary pages and MMIX/PeeringDB.
2. Search MyCO/DICA for every SPV and legal-entity variant.
3. Search MIC/Project Bank/GNLM/MDN for project approvals and government DC programs.
4. For Yangon, check YBPS/YCDC locality evidence for Hlaing, Hantharwady/Bayintnaung, Mayangone, Thanlyin, Kyauktan, and Thilawa.
5. Use MOEP/YESC/MESC/ESE and US ITA for power feasibility, not for capacity unless a source names the site load.
6. Run the full 15-division sweep above. Log negative evidence per division with date, query set, and source class.
7. Assign field-level grades. Do not raise a facility above the weakest material fact being asserted.

## 7. Quick URL index

- PTD: https://www.ptd.gov.mm/
- MyCO: https://www.myco.dica.gov.mm/corp/search.aspx
- DICA: https://www.dica.gov.mm/
- Project Bank e-GIDC: https://www.projectbank.gov.mm/en/profiles/activity/PB-ID-1126/
- YBPS: https://ybps.ycdc.gov.mm/
- MOEP: https://www.moep.gov.mm/
- Cybersecurity Law: https://www.moi.gov.mm/moi%3Aeng/news/16633 and https://www.moi.gov.mm/moi%3Aeng/news/16656
- MPT DC/cloud: https://mpt.com.mm/en/business-home/data-center-en/ and https://mpt.com.mm/en/business-home/b2b-cloud-service/
- True IDC Myanmar: https://www.trueidc.com/en/myanmar
- MICTDC: https://mictdc.com.mm/mict-data-center/
- MTG colocation: https://www.mtg.com.mm/co-location-services.php
- DICA MTG field visit: https://www.dica.gov.mm/23016/
- Mytel/Viettel DC opening: https://viettelfamily.com/news/mytel-khai-truong-data-center-so-1-tai-myanmar
- Zenlayer Yangon: https://cloud.zenlayer.com/datacenters/yangon
- PeeringDB MMIX Yangon: https://www.peeringdb.com/ix/2102
- PeeringDB True IDC facility: https://www.peeringdb.com/fac/5031
- Submarine Networks Myanmar: https://www.submarinenetworks.com/en/stations/asia/myanmar
- UMO/SIGMAR cable: https://www.submarinenetworks.com/en/systems/intra-asia/sigmar
- US ITA Burma Digital Economy: https://www.trade.gov/country-commercial-guides/burma-digital-economy
