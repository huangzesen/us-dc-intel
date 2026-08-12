# ZM Explorer Industry - Zambia Datacenter Enumeration via Operators, Colo, Telco, IXP, and Trade Press

Date: 2026-08-12. Country: **ZM Zambia**. Division model: **10 provinces**: Central; Copperbelt; Eastern; Luapula; Lusaka; Muchinga; Northern; North-Western; Southern; Western. Angle: **industry/operator-first discovery**, reconciled against official records.

Reliability grades are field-level:
- **A** = operator-owned page, official government/regulator page, council permit, ZEMA/ERB/ZICTA/ZDA/DPC record, official cloud-region page, signed government/operator announcement for the exact claim.
- **B** = strong named secondary/trade source: DCD, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, ZANIS, Lusaka Times, Zambia Daily Mail, Times of Zambia, News Diggers, vendor case study, PeeringDB/IXP pages for network presence.
- **C** = lead only: directory entry, social media, generic market report, AI-generated/aggregator content, unsupported capacity/address, regional expansion article with no Zambia site.

Use B/C sources to find candidates, then promote only the specific fields that are confirmed by A-grade sources. A single facility can have A-grade operator existence, B-grade MW/rack data, and C-grade address until each field is independently verified.

---

## 0. Zambia Market Structure

Zambia is a small, early-stage, **Lusaka-centred** datacenter market. The verified industry seed set is stronger than the original draft suggested because **INFRATEL / Zambia National Data Centre** has official pages stating it operates three national Tier III data centres and offers colocation/cloud/backup services. Commercial open-colo evidence is led by **Paratus Zambia** and **INFRATEL**, with **Liquid Intelligent Technologies Zambia** providing local cloud/Azure Stack and a still-to-be-verified new-data-centre MoU pipeline.

Operational/high-confidence seeds:
- **INFRATEL / Zambia National Data Centre**: official INFRATEL pages state three national Tier III data centres and data-centre/cloud/backup services. Parliament records tie ZNDC to three Smart Zambia Phase I data centres and government/private-sector cloud/data services. Grade A for operator/service existence; addresses/capacity require field-specific sources.
- **Paratus Zambia**: official Paratus pages state a Tier III-by-design data center in Lusaka with colocation/cloud/DR services and ISO/PCI certifications. DCD reported the 2021 Lusaka facility as 1 MW and carrier-neutral. Grade A for operator/facility/service; B for 1 MW unless an operator/government page gives the same number.
- **Liquid Intelligent Technologies Zambia / Liquid C2**: official Liquid pages state Azure Stack launch in Zambia and a 2023 MoU committing Liquid Zambia to launch a new data centre. Grade A for Azure Stack/local cloud and MoU intent; do not count a new Liquid DC as operational until site/permit/power/commissioning evidence is found.
- **Smart Zambia / Huawei National AI Data Centre MoU**: Office of the Vice President and Smart Zambia coverage confirms a May 2026 MoU for a National AI Data Centre and training. Grade A for MoU only; status is `MoU/intent`.

Telco and network leads:
- **Zamtel**, **MTN Zambia**, and **Airtel Zambia** have core network sites and enterprise services, but facility details are usually closed. Count only explicit hosting/DC products or named facilities.
- **Lusaka IXP** is a neutral interconnection signal. PeeringDB/Lusaka IXP membership is A/B for network presence, not datacenter proof.
- Zambia is landlocked; terrestrial fibre and international gateway licences are important for DC viability but do not prove facility existence.

No official hyperscale public region is listed in Zambia by AWS, Azure, Google Cloud, or Oracle OCI as of 2026-08-12. Nearest public regions are in South Africa/Johannesburg or Cape Town depending on provider. Azure Stack in Zambia is local/hybrid cloud, not an Azure public region.

---

## 1. Operator and Facility Seed List

| Operator / platform | URLs | Zambia signal | Likely locations | Grade discipline |
|---|---|---|---|---|
| **INFRATEL / Zambia National Data Centre** | https://infratel.co.zm/ ; https://infratel.co.zm/data-center-services/ ; https://infratel.co.zm/company-profile/ ; https://infratel.co.zm/faqs/ | Three national Tier III data centres; colocation, cloud, backup, digital services; ZNDC government heritage | Lusaka primary; backup/DR sites may include Roma/Lusaka and Kitwe references in Parliament records | A for official service/operator existence; C/B for directory addresses/capacity until official |
| **Paratus Zambia** | https://paratus.africa/zambia/ ; https://paratus.africa/zambia/business-solutions/data-center-and-cloud-services/ ; https://paratus.africa/services/data-center-services/ | Tier III-by-design data center in Lusaka; colocation/cloud/DR; group page says Zambia DC is ISO 9001, ISO/IEC 27001 and PCI DSS certified | Lusaka | A for facility/services/certification wording; B for DCD-reported 1 MW and 2021 launch |
| **Liquid Intelligent Technologies Zambia / Liquid C2** | https://liquid.tech/local-offices/country/zambia/ ; https://liquid.tech/about-us/news/liquid-intelligent-technologies-zambia-launches-azure-stack/ ; https://liquid.tech/about-us/news/liquid-intelligent-technologies-signs-memorandum-of-understanding-with-zambia/ | Azure Stack/local cloud; 2023 MoU to launch a new data centre; fibre routes | Lusaka first; watch Ndola/Kitwe/Livingstone/Solwezi edge claims | A for Azure Stack and MoU; facility status remains unconfirmed unless site evidence appears |
| **Smart Zambia / Huawei AI DC** | https://www.szi.gov.zm/ ; https://www.ovp.gov.zm/?p=10669 | May 2026 MoU for National AI Data Centre and AI services/training | Site not yet public in verified sources | A for MoU/intent only |
| **Zamtel** | https://www.zamtel.zm/ | State telco, fixed/mobile/core network, enterprise services | Lusaka HQ and exchanges nationally | A for operator/service; C for DC specifics unless named |
| **MTN Zambia** | https://www.mtn.zm/ | Mobile/enterprise network; possible core/DR hosting | Lusaka, national | A for operator/service; C for facility specifics |
| **Airtel Zambia** | https://www.airtel.co.zm/ | Mobile/enterprise network; possible core/DR hosting | Lusaka, national | A for operator/service; C for facility specifics |
| **Lusaka IXP** | https://lusakaixp.co.zm/ ; https://www.peeringdb.com/ix/615 | Neutral exchange point and peer/member discovery | Lusaka | A/B for IXP/network presence; not DC proof |
| **Raxio, Africa Data Centres, Teraco/Digital Realty, Equinix/iColo, Vantage, NTT, Wingu** | Official portfolio pages | No verified Zambia facility found in this review | Watch Lusaka only | C until official Zambia project/source appears |

Operator queries:
```text
"{operator}" Zambia "data centre" OR "data center" OR "colocation"
"{operator}" Zambia "Tier III" OR "Tier 3" OR "by design"
"{operator}" Zambia "MW" OR "MVA" OR "racks" OR "cabinets"
"{operator}" Zambia "Azure Stack" OR "local cloud" OR "sovereign cloud"
"{operator}" "ZICTA" OR "ZEMA" OR "ERB" OR "ZDA" Zambia
"{operator}" "Lusaka" "data centre"
"{operator}" "MoU" "data centre" Zambia
```

---

## 2. Trade Press and Industry Media

Use trade press for discovery and date/capacity leads, then reconcile against operator/government sources.

High-yield verified examples:
- DCD reported Paratus' Lusaka facility in April 2021 as a 1 MW carrier-neutral data center due for completion by July 2021: https://www.datacenterdynamics.com/en/news/paratus-zambia-close-to-completing-lusaka-data-center/
- ITWeb Africa and TechAfrica News reported Paratus' ZICTA data gateway licence in 2023. Use as B unless the ZICTA licence record is opened.
- Liquid's own announcement is A for its 2023 Zambia MoU; ITWeb Africa/TechCabal/Telecompaper are B repeats.
- Developing Telecoms and ITWeb Africa reported the May 2026 Smart Zambia-Huawei AI data-centre MoU; Office of the Vice President/Smart Zambia pages are preferred A sources.

Local/national press:
- Lusaka Times: https://www.lusakatimes.com/
- News Diggers: https://diggers.news/
- Zambia Daily Mail: https://www.daily-mail.co.zm/
- Times of Zambia: https://www.times.co.zm/
- ZANIS: https://www.zanis.gov.zm/
- ZNBC: https://www.znbc.co.zm/
- Techtrends Zambia: https://www.techtrends.co.zm/

Regional/international trade:
- DCD: https://www.datacenterdynamics.com/
- ITWeb Africa: https://itweb.africa/
- Developing Telecoms: https://developingtelecoms.com/
- Connecting Africa: https://www.connectingafrica.com/
- Capacity: https://www.capacitymedia.com/
- W.Media: https://w.media/
- TechCabal: https://techcabal.com/

Press queries:
```text
site:datacenterdynamics.com Zambia "data center" OR "data centre"
site:itweb.africa Zambia "data centre" OR "gateway licence"
site:developingtelecoms.com Zambia "data centre" OR "AI data centre"
site:lusakatimes.com "data centre" OR "data center" OR "INFRATEL" OR "Paratus" OR "Liquid"
site:zanis.gov.zm "{province}" "ICT" OR "digital" OR "data centre"
site:techtrends.co.zm Zambia "cloud" OR "hosting" OR "data centre"
"Zambia" "first Tier III" "data centre"
"Zambia" "new data centre" "Lusaka"
```

---

## 3. Network, Peering, and CDN Evidence

Network evidence identifies where to look; it rarely proves a datacenter by itself.

- **Lusaka IXP**: use members/peers and PeeringDB IX ID 615 to identify networks present in Lusaka.
- **PeeringDB facility/network pages**: B for network presence, C for facility detail unless matched to an operator site.
- **Directory sites**: datacentermap lists Lusaka entries including Paratus and INFRATEL, but directories are C until checked against operator pages.
- **CDN/cache clues**: Google Global Cache, Meta, Akamai, Netflix OCA, Alibaba/PCCW access-point references can reveal hosted infrastructure. Grade as network/edge evidence only unless the hosting facility is named.

Queries:
```text
"Lusaka IXP" members OR peers OR peering
site:peeringdb.com Zambia OR Lusaka
"Lusaka Internet Exchange Point" "colocation" OR "data centre"
"Google Global Cache" OR "Akamai" OR "Netflix OCA" OR "Meta CDN" Zambia Lusaka
"Alibaba Cloud" "Lusaka" "Liquid Telecom"
datacentermap Zambia Lusaka Paratus INFRATEL Liquid
"{network}" "Lusaka IXP" Zambia
```

Extract: ASN, network name, IXP status, facility/address if stated, source date, and whether the evidence is facility, network, or cache-only.

---

## 4. Enterprise, Financial, Government, and Mining Leads

These often reveal closed facilities or demand, not commercial supply.

- **Government/parastatal**: Smart Zambia, INFRATEL/ZNDC, ZRA, NAPSA, PACRA, Immigration, NRC, health and education systems. Parliament and Auditor-General/PAC reports can mention hosting, backup, or DR weaknesses.
- **Financial sector**: Bank of Zambia, Zanaco, Stanbic, ABSA, Standard Chartered, FNB, Indo-Zambia, mobile-money platforms. Treat DR/server-room mentions as C unless physical facility details are public.
- **Mining**: Copperbelt and North-Western mine operators and suppliers may run OT/IT rooms or DR sites. CEC/NWEC power records and ZEMA project docs are stronger than press statements.
- **Universities/research**: UNZA, CBU, Mulungushi University and colleges may have server rooms/HPC/AI projects. Count only if public facility evidence exists.

Queries:
```text
"Bank of Zambia" "data centre" OR "disaster recovery" OR "server room"
"ZRA" OR "NAPSA" OR "PACRA" "data centre" Zambia
site:parliament.gov.zm "data centre" "INFRATEL" OR "ZNDC"
"{bank}" Zambia "data centre" OR "DR site" OR "business continuity"
"{mine}" Zambia "data centre" OR "ICT infrastructure" OR "control room"
"Copperbelt" "data centre" "mine" OR "disaster recovery"
"Solwezi" OR "Kalumbila" "data centre" OR "ICT" OR "server"
```

---

## 5. Associations and Events

- **ICTAZ**: https://ictaz.org.zm/ - professional body and Digital Excellence Awards. Use for project/member leads; grade association claims B unless backed by operator/regulator evidence.
- **Ministry of Technology and Science**: https://www.mots.gov.zm/ - ICT policy and digital-economy announcements.
- **Zambia Mobile Congress**: useful for MoU-stage announcements such as the 2026 Smart Zambia-Huawei AI data-centre deal.
- **ISPAZ/GSMAZ**: ISP/telco association leads; verify current websites and members before relying on them.

Queries:
```text
site:ictaz.org.zm "data centre" OR "cloud" OR "infrastructure"
"ICTAZ" "Digital Excellence Awards" "data centre" Zambia
site:mots.gov.zm "data centre" OR "cloud" OR "AI"
"Zambia Mobile Congress" "data centre" OR "Huawei" OR "AI"
"ISPAZ" "Internet Exchange" Zambia hosting
"GSMAZ" Zambia data network hosting
```

---

## 6. Per-Province Industry Strategy

| Province | Capital | Industry anchors | Strategy and expected yield |
|---|---|---|---|
| **Lusaka** | Lusaka | INFRATEL/ZNDC, Paratus, Liquid, Smart Zambia, Lusaka IXP, telco HQs, banks, ZICTA/ERB/ZEMA/ZDA | **Primary cluster.** Start with operator pages, then DCD/Liquid/INFRATEL/Paratus announcements, directories, IXP members, council and ZEMA/power confirmation. |
| **Copperbelt** | Ndola | CEC, Ndola/Kitwe, Chambishi MFEZ/ZCCZ, mining ICT, possible INFRATEL/DR references | **Second priority.** Search Ndola/Kitwe/Chambishi plus CEC, mines, Kitwe DR, telco exchanges, and ZANIS/local press. |
| **Southern** | Choma | Livingstone tourism/border, Liquid/Zamtel routes, banks/hotels, ZESCO | **Low watch.** Search Livingstone/Choma for hosting, DR, hotel/tourism ICT, telco route PoPs. |
| **Central** | Kabwe | Kabwe, Chibombo/Jiangxi MFEZ, agriculture/parastatal ICT, railway/logistics | **Low watch.** Search Kabwe/Chibombo, MFEZ tenants, and government server-room leads. |
| **Eastern** | Chipata | Malawi-border trade, provincial government, banks/mobile money | **Low watch.** Search Chipata/Eastern for ICT projects, branch DR, telco upgrades. |
| **Luapula** | Mansa | Provincial government, fisheries/agriculture, ZESCO/telco towers | **Very low watch.** Search Mansa/Luapula only to close coverage gaps. |
| **Muchinga** | Chinsali | Chinsali/Mpika corridor, government connectivity, telco towers | **Very low watch.** Search Chinsali/Mpika for backbone and government systems; facility count unlikely. |
| **Northern** | Kasama | Kasama/Mbala/Mpulungu, logistics/tourism, government systems | **Very low watch.** Search for server rooms, e-government, logistics ICT. |
| **North-Western** | Solwezi | NWEC, Kalumbila MFEZ, FQM/mining suppliers, Solwezi council | **Medium-low watch.** Stronger than most provinces because of mining power and demand. Search Solwezi/Kalumbila/NWEC and mine DR/ICT procurement. |
| **Western** | Mongu | Provincial administration, Lozi/Barotseland press, government connectivity | **Very low watch.** Search Mongu/Western for e-government and council/telco evidence. |

Province query block:
```text
"{capital}" "data centre" OR "data center" OR "server room" OR "hosting" Zambia
"{province}" "cloud" OR "ICT" OR "digital" Zambia
"{capital}" "INFRATEL" OR "Paratus" OR "Liquid" OR "Zamtel" OR "MTN" OR "Airtel"
"{province}" "disaster recovery" OR "business continuity" Zambia
site:zanis.gov.zm "{capital}" "ICT" OR "digital"
site:datacenterdynamics.com "{province}" Zambia
"{capital}" "substation" "data" Zambia
```

---

## 7. Confirmation Workflow

1. Seed from operator pages: INFRATEL, Paratus, Liquid, Smart Zambia/Huawei, Zamtel, MTN, Airtel.
2. Search directories and PeeringDB only to find leads; keep them C until reconciled.
3. Cross-check each facility through official trails: ZICTA licence/gateway, ZEMA EIA/EPB/EIS, ERB/ZESCO/CEC/NWEC power, ZDA/SEZ, council planning/building, DPC only as demand context.
4. Run the full ten-province sweep; record `no confirmed facility found` for provinces with no hits rather than dropping them.
5. Store field-level grades and exact source wording. Never upgrade `Tier III by design` to certified Tier III unless Uptime/certification evidence says so.

Master query bank:
```text
"Zambia" "data centre" "Lusaka" "Tier III"
"Zambia" "data center" "MW" "Lusaka"
"INFRATEL" "three" "data centres" Zambia
"Paratus Zambia" "data center" "Lusaka" "Tier III"
"Liquid Zambia" "Azure Stack" OR "new data centre"
"SMART Zambia" "National AI Data Centre" Huawei
"Zambia National Data Centre" "three data centres"
"Lusaka IXP" "data centre" OR "colocation"
"Copperbelt" OR "Ndola" OR "Kitwe" "data centre" Zambia
"Solwezi" OR "Kalumbila" "data centre" OR "ICT infrastructure" Zambia
"{operator}" "ZICTA" OR "ZEMA" OR "ERB" OR "ZDA" Zambia
```

---

## 8. Source Notes From This Review

Verified A-grade URLs used in this methodology: INFRATEL data-centre/company/FAQ pages; Paratus Zambia and Paratus Group data-center pages; Liquid Azure Stack and Zambia MoU announcements; Smart Zambia/Office of the Vice President AI data-centre MoU pages; ZICTA licensing; ZEMA services and EIA document pages; ERB licensing; CEC local-power page; ZDA SEZ page; DPC registration portal; LCC planning page; MLGRD local-authority index; official AWS/Azure/Google/Oracle region pages.

Honest downgraded items: Paratus 1 MW is B unless matched to operator/official source; Liquid's new data centre is MoU/intent, not operational; directory addresses/capacities for INFRATEL/Paratus are C until operator/council/regulator confirmation; telco core sites are leads, not countable colo; hyperscale cloud region claims for Zambia are false unless an official cloud-provider region page changes.
