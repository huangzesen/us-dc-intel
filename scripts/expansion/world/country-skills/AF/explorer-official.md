# AF Explorer Official - Afghanistan Datacenter Enumeration

Date: 2026-08-12. Country: **AF Afghanistan**. Division model: **province, 34 provinces** from `world-manifest.jsonl`. Scope: official, regulator, procurement, state-IT, power, and cloud-region methodology for finding operational, under-construction, planned, and tender-only data-center facilities.

Reliability grades:
- **A** = primary or controlling source: MCIT/MoCIT, ANDC, ATRA, DABS, Afghan Telecom/Salaam, e& Afghanistan/Etisalat Afghanistan tenders, official operator facility page, World Bank/IFI procurement, government-company statement, Uptime Institute certificate.
- **B** = strong secondary source with named project/operator/location: DCD, Network World, Pajhwok, Ariana, Bakhtar, TOLOnews, APNIC, Chatham House, vendor case study from the named contractor.
- **C** = lead only: DataCenterMap, DataCenterCatalog, datacenters.com, PeeringDB, Cloudscene, Mordor/market reports, hosting marketing, directories, social posts, or fiber/IXP-only evidence.

Key rule: **do not promote a facility above the weakest necessary link**. ATRA licenses, telecom fiber, NIXA membership, cloud procurement, or "Tier III" marketing are not facility proof by themselves.

---

## 0. Afghanistan-specific findings

- Afghanistan has **no public national data-center register, construction-permit register, or searchable municipal building-permit portal**. Enumeration must be built from MCIT/ANDC procurement, ATRA entity licensing, operator facility pages, DABS/energy evidence, NIXA, IFI/USAID/World Bank records, and local press.
- The highest-confidence market is **Kabul**. Verified Kabul anchors include ANDC, MCIT second-DC/DR tenders, Ministry of Mines and Petroleum data center, NIXA, ALEF Technology, AryanICT, ACG Kabul, DABS/Tarakhil DR plan, and several Kabul-centered contractor/vendor case-study leads.
- **Nangarhar** has an official MCIT plan signal: MCIT said a second National Data Center would be created in Nangarhar province, but no completion/capacity evidence was found. Treat as **planned/tender-intent unless refreshed evidence proves commissioning**.
- **Balkh, Herat, Kandahar, and Kunduz** have connectivity or directory claims, but live verification did not find primary facility pages for named DCs in those provinces. Treat ACG multi-city claims as **C leads** unless independently confirmed; ACG's own page only clearly confirms its Kabul data center.
- No official AWS, Azure, Google Cloud, or Oracle Cloud public region/local zone was found in Afghanistan during this review. Telco/state "cloud" language is local workload or service evidence, not hyperscaler-owned DC evidence.
- Uptime Institute has an Afghanistan country page, but no public Afghanistan award was found during this review. Any Afghan "Tier III" claim is **C** unless a certificate is located.

---

## 1. Official / state-IT sources

### 1.1 MCIT / MoCIT and ANDC

Primary URLs:
- MCIT portal: https://mcit.gov.af/en
- MCIT tenders: https://mcit.gov.af/en/all-tenders
- MCIT homepage footer still links ANDC, but the standalone ANDC site was serving a default/test page or 404 during URL validation. Use MCIT's live ANDC procurement/visit pages as the official source of record until `andc.gov.af` is restored.

Verified official anchors:
- ANDC annual maintenance tender, Kabul/MCIT: https://www.mcit.gov.af/en/tender-annual-maintenance-non-it-infrastructure-afghanistan-national-data-center-andc
- ANDC critical upgrade tender, Digital CASA / World Bank grant IDA-D2820, Kabul: https://mcit.gov.af/en/invitation-bid-procurement-critical-upgrade-afghanistan-national-data-center-andc-non-it-equipment
- MCIT contract award notice for ANDC critical upgrade: https://mcit.gov.af/en/contract-award-notice-1
- MCIT second data-center tender in Kabul: https://mcit.gov.af/index.php/en/announcement-second-project-data-center-kabul-city
- MCIT alternate second-DC tender URL: https://mcit.gov.af/index.php/en/announcement-bid-create-second-datacenter-center-kabul-1
- Acting minister visit to Afghan National Information Center / Data Center: https://www.mcit.gov.af/en/acting-minister-mcit-visits-different-parts-data-center
- Ministry of Mines and Petroleum data center and MCRS, with MCIT statement about a second National Data Center in Nangarhar: https://mcit.gov.af/en/ministry-mines-and-petroleum-inaugurates-data-center-and-mcrs-system
- NIXA official brief: https://mcit.gov.af/en/nixa-national-internet-exchange-afghanistan-8
- NIXA infrastructure/status page: https://mcit.gov.af/en/node/7048
- NIXA enhancement procurement under Digital CASA: https://mcit.gov.af/en/procurement-enhancement-national-internet-exchange-afghanistan-nixa
- Afghan Telecom / government cloud-email procurement lead: https://mcit.gov.af/index.php/en/procurement-google-workspace-cloud-email-services

Use:
1. Search MCIT first for `data center`, `datacenter`, `ANDC`, `National Data Center`, `NIXA`, `DRDC`, `cloud`, `server`, `UPS`, `generator`, `مرکز داده`, `مرکز معلوماتی`, `ډیټا مرکز`, and `د معلوماتو مرکز`.
2. Treat MCIT/ANDC pages as **A** for the named government facility, tender, procurement, or official plan.
3. Treat tenders as **A for procurement event**, but only **B/C for built status** until award, handover, commissioning, or operating page exists.
4. For the MCIT Nangarhar statement, record **Nangarhar / planned / no capacity** until a later source proves that the second National Data Center was built.

Query templates:
```text
site:mcit.gov.af "data center"
site:mcit.gov.af "datacenter"
site:mcit.gov.af "National Data Center"
site:mcit.gov.af "ANDC"
site:mcit.gov.af "DRDC" OR "disaster recovery"
site:mcit.gov.af "مرکز داده"
site:mcit.gov.af "ډیټا مرکز"
site:mcit.gov.af "data center" "{province}"
site:mcit.gov.af tender "server" "{province}"
site:mcit.gov.af "Afghanistan National Data Center" "hosting" OR "co-location"
```

### 1.2 ATRA

Primary URLs:
- ATRA portal: https://atra.gov.af/
- MCIT/ATRA legacy procurement/regulatory records: https://mcit.gov.af/index.php/en/atra-needs-adviser-mobile-number-portability
- Telecommunications Services Regulation Act reference copy: https://kakaradvocates.com/uploads/laws/translation-Law_on_Regulating_Telecommunication_Services_EN.pdf

Use:
1. ATRA is useful for **entity authorization**, not facility enumeration. It can confirm telecom/ISP/VAS context for AWCC, Roshan/TDCA, e&/Etisalat Afghanistan, M1/MTN, Afghan Telecom/Salaam, Wasel, satellite providers, and ISPs.
2. Search both `atra.gov.af` and MCIT pages because older ATRA procurement/licensing notices are sometimes hosted under MCIT.
3. ATRA license or regulatory notice = **A for license/entity status**, **C for data-center facility** unless the notice names a physical data center.

Query templates:
```text
site:atra.gov.af license OR licensees OR "Internet service"
site:atra.gov.af "data center" OR hosting OR cloud
site:atra.gov.af "{operator}"
"ATRA" "{operator}" license Afghanistan
"Afghanistan Telecom Regulatory Authority" "data center"
"ATRA" "Telecom Development Fund" "{province}"
```

### 1.3 State companies, e-government, and identity infrastructure

Primary / high-yield sources:
- Afghan Telecom: https://www.afghantelecom.af/en/
- Grand Technology Resources Afghanistan projects: https://www.gtr.ae/major-projects-central-asia/

Known source-graded records:
- Afghan Telecom FTTX/internet pages confirm national fiber/data services and NOC/support language, but **not a public data-center facility**: https://www.afghantelecom.af/en/service-list/internet/fttx
- GTR states it delivered ANDC, UNDP WEPS DR Data Center, AUAF server farm, and AFMIS Data Center in Afghanistan. Treat as **B vendor case-study evidence** unless a matching government page names the same site.
- Asan Khedmat and NSIA/e-Tazkira are useful search targets, but their public sites were not reliable source anchors in URL validation; use MCIT-hosted Asan/e-government documents or local press when citing them.

Queries:
```text
site:afghantelecom.af "data center" OR datacenter OR "server"
site:afghantelecom.af "cloud" OR "NOC"
site:nsia.gov.af "data center" OR "مرکز داده" OR "server"
site:asan.gov.af "data center" OR "مرکز داده"
"Asan Khedmat" "{province}" "data center" OR server
"e-Tazkira" "data center" Afghanistan
"AFMIS" "Data Center" Afghanistan
"UNDP WEPS" "DR Data Center" Afghanistan
```

---

## 2. Permits, registration, and procurement

### 2.1 Business / investment registration

Primary sources:
- Ministry of Industry and Commerce: https://moci.gov.af/en
- Org-ID reference for Afghanistan Central Business Registry: http://org-id.guide/list/AF-CBR

Use: business registration/licensing is **A for legal entity existence** and **C for a facility**. It is most useful for resolving legal names and ownership: Telecom Development Company Afghanistan (Roshan), Afghan Telecom Corporation, Etisalat Afghanistan/e& Afghanistan, M1 New Ventures/MTN Afghanistan successor, Asia Consultancy Group, ALEF Technology, AryanICT, Pamir Alpha Technologies.

```text
site:moci.gov.af "{operator}"
"ACBR" "{operator}" Afghanistan
"AISA" "{operator}" Afghanistan
"{operator}" "business license" Afghanistan
```

### 2.2 Construction / municipal permits

There is no reliable public construction-permit portal for Afghan provinces. Kabul Municipality (`https://km.gov.af/`) and provincial/governor pages may mention public buildings, but they should be treated as discovery surfaces only.

```text
site:km.gov.af "data center" OR "server"
"{province}" municipality "data center" Afghanistan
"{province}" governor "data center" OR "مرکز داده"
"{operator}" "{province}" "inaugurated" OR "opened" OR "construction"
```

### 2.3 Procurement

Use MCIT and Afghan Telecom procurement before broad web search.

```text
site:mcit.gov.af/en/all-tenders "data center"
site:mcit.gov.af "Procurement" "Data Center"
site:mcit.gov.af "UPS" OR "generator" "data center"
site:afghantelecom.af "procurement" "server"
site:etisalat.af "Public Cloud data center"
"Digital CASA Afghanistan" "data center"
"World Bank" "Afghanistan" "NIXA" "data center"
```

---

## 3. Energy and grid validation

Primary sources:
- DABS main site: https://main.dabs.af/
- Legacy DABS site: https://bereshna.com/
- DCD Tarakhil/DABS DR data-center article: https://www.datacenterdynamics.com/en/news/usaid-plans-disaster-recovery-data-center-troubled-tarakhil-power-plant-afghanistan/

Known energy anchor:
- DCD reported a USAID/DABS plan for a Disaster Recovery Data Center at Tarakhil Power Plant and an existing DABS data center in Chaman Hazouri, Kabul. Treat as **B plan evidence** until DABS/USAID completion proof is found.

Power rules:
- Do not infer IT MW from transformer, generator, MVA, or power-plant capacity.
- For Kabul facilities, capture DABS/grid, transformer, generator, UPS, HVAC, and fuel evidence where stated.
- For Panjshir, Nuristan, and Paktika, the lack of active DABS operations is an important negative-control context, not proof that no private generator-backed server room exists.

Queries:
```text
site:main.dabs.af "data center"
site:bereshna.com "data center"
"DABS" "data center" Kabul
"Tarakhil" "data center"
"Chaman Hazouri" "DABS" "data center"
"{facility}" "generator" OR "UPS" OR "transformer"
"{province}" "substation" "data center" Afghanistan
```

---

## 4. Official cloud / edge controls

Check these each run because public regions and edge cities change.

| Provider | Official source | Afghanistan result to record |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No Afghanistan Region or Local Zone found; negative control. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Afghanistan public cloud region found; negative control. |
| Google Cloud | https://cloud.google.com/about/locations | No Afghanistan cloud region found; negative control. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Afghanistan OCI public region found; negative control. |
| Cloudflare | https://www.cloudflare.com/network/ and https://www.cloudflarestatus.com/locations | No confirmed in-country Afghanistan DC city found; treat as edge/network only if future source appears. |
| e& Afghanistan / Etisalat Afghanistan | https://www.etisalat.af/ and tender PDFs under `/images/Tenders/` | 2025-2026 RFPs mention a Public Cloud data center hosted in Afghanistan and not movable without Etisalat approval. This is **A/B procurement/service evidence**, **C facility evidence** until address/operator is public. |

Queries:
```text
"Afghanistan" "AWS Region" site:aws.amazon.com
"Afghanistan" "Azure region" site:learn.microsoft.com
"Afghanistan" "Google Cloud region" site:cloud.google.com
"Afghanistan" "Oracle Cloud" site:oracle.com
"Etisalat Afghanistan" "Public Cloud data center"
"e& Afghanistan" "data center" Kabul
```

---

## 5. NIXA and network infrastructure

Primary / strong sources:
- MCIT NIXA brief: https://mcit.gov.af/en/nixa-national-internet-exchange-afghanistan-8
- MCIT NIXA infrastructure/status: https://mcit.gov.af/en/node/7048
- MCIT NIXA procurement: https://mcit.gov.af/en/procurement-enhancement-national-internet-exchange-afghanistan-nixa
- Internet Society IXP tracker: https://pulse.internetsociety.org/en/ixp-tracker/country/AF/
- PCH NIXA page: https://www.pch.net/ixp/details/1705
- APNIC NIXA blog: https://blog.apnic.net/2022/05/20/ixp-seeks-to-sustainably-lower-the-cost-of-internet-in-afghanistan/

Use:
- NIXA is a physical IXP infrastructure in Kabul and a strong signal for carrier concentration, caches, and DNS/root-server infrastructure.
- NIXA membership is **not** a datacenter facility for the member. Use it to pivot to AWCC, Afghan Telecom, Io-Global, Ankabut, Network Zone, Cyber Telecom, Vital Telecom, and other ISPs.

```text
site:mcit.gov.af "NIXA"
"National Internet Exchange of Afghanistan" "{operator}"
site:pch.net "National Internet Exchange of Afghanistan"
site:pulse.internetsociety.org Afghanistan IXP
"NIXA" "Google Cache" "Facebook Localization"
```

---

## 6. Per-province official strategy, all 34 provinces

For every province run: MCIT/ANDC, ATRA, DABS, Afghan Telecom, governor/municipality, NIXA/fiber context, official state news, and Dari/Pashto terms. Record "no public project found" only after the compact sweep is complete.

| Province | Official strategy and current posture |
|---|---|
| Balkh | Query `Balkh`, `Mazar-e-Sharif`, `مزارشریف`, `Hairatan`, `Wasel`, `Kabul-Mazar-Hairatan`. Current posture: no verified official DC; fiber/market-growth/ACG multi-city claims are C until confirmed. |
| Bamyan | Negative-control sweep; watch MCIT/e-services and DABS solar/off-grid false positives. |
| Badghis | Negative-control sweep; expect power/telecom access hits, not DCs. |
| Badakhshan | Negative-control sweep; separate Afghanistan-wide "data" and provincial connectivity hits. |
| Baghlan | Query `Pul-e-Khumri`, DABS substations, Afghan Telecom coverage; no verified DC lead. |
| Daykundi | Query `Daykundi`, `Daikundi`, `دایکندی`; negative-control posture. |
| Farah | Query `فراه`, border/transit and DABS terms; no verified DC lead. |
| Faryab | Query `Faryab`, `Maymana`, `فاریاب`; negative-control posture. |
| Ghazni | Query `غزنی`, Afghan Telecom/fiber and DABS; telecom projects are false positives unless facility named. |
| Ghor | Query `غور`, `Chaghcharan`; negative-control posture. |
| Helmand | Query `هلمند`, `Lashkargah`; expect tower/power false positives, no verified DC lead. |
| Herat | Query `Herat`, `هرات`, `Islam Qala`, `Herat Host`, `Asan Khedmat`. Current posture: no verified official facility; treat ISP/ACG claims as leads. |
| Jowzjan | Query `Jowzjan`, `Jawzjan`, `Sheberghan`, `جوزجان`; negative-control posture. |
| Kabul | Exhaustive sweep. Confirm ANDC, MCIT second-DC/DR tenders, MoMP DC, NIXA, DABS/Tarakhil, ALEF, AryanICT, ACG, e& cloud RFP, Afghan Telecom/Salaam core, and contractor case studies. |
| Kandahar | Query `Kandahar`, `قندهار`, `Spin Boldak`, e&/AWCC/ATRA. Current posture: no verified DC; telecom gateway/4G/fiber only unless facility named. |
| Kapisa | Query `Kapisa`, `Mahmud Raqi`, `کاپیسا`; negative-control posture. |
| Kunduz | Query `Kunduz`, `Konduz`, `کندز`; no verified official DC; ACG multi-city claim remains C. |
| Khost | Query `خوست`, `Ghulam Khan`, Asan Khedmat, ATRA; no verified DC lead. |
| Kunar | Query `Kunar`, `Asadabad`, `کنر`; negative-control posture. |
| Laghman | Query `Laghman`, `Mehtar Lam`, `لغمان`; negative-control posture. |
| Logar | Query `Logar`, `Pul-e-Alam`, `لوگر`; negative-control posture. |
| Nangarhar | Query `Nangarhar`, `Jalalabad`, `Torkham`, `ننگرهار`, `جلال آباد`. MCIT says a second National Data Center would be created here; record as planned until built-status proof is found. |
| Nimruz | Query `Nimruz`, `Zaranj`, `نیمروز`, Chabahar corridor; no verified DC lead. |
| Nuristan | Query `Nuristan`, `نورستان`; DABS-coverage constraint; negative-control posture. |
| Panjshir | Query `Panjshir`, `پنجشیر`; DABS-coverage constraint; negative-control posture. |
| Parwan | Query `Parwan`, `Charikar`, `Bagram`, `پروان`; no verified DC lead. |
| Paktia | Query `Paktia`, `Gardez`, `پکتیا`, Asan Khedmat; no verified DC lead. |
| Paktika | Query `Paktika`, `Sharana`, `پکتیکا`; DABS-coverage constraint; negative-control posture. |
| Samangan | Query `Samangan`, `Aybak`, `سمنگان`; negative-control posture. |
| Sar-e Pol | Query `Sar-e Pol`, `Sari Pul`, `سرپل`; negative-control posture. |
| Takhar | Query `Takhar`, `Taloqan`, `تخار`; negative-control posture. |
| Urozgan | Query `Urozgan`, `Uruzgan`, `Tarin Kot`, `ارزگان`; negative-control posture. |
| Maidan Wardak | Query `Maidan Wardak`, `Wardak`, `میدان وردک`, `وردک`; negative-control posture. |
| Zabul | Query `Zabul`, `Qalat`, `زابل`; negative-control posture. |

Compact sweep for every province:
```text
site:mcit.gov.af "{province}" "data center"
site:mcit.gov.af "{province}" "server" OR "cloud"
site:atra.gov.af "{province}" "Internet service"
site:main.dabs.af "{province}" "substation" OR "electricity"
"{province}" "data center" Afghanistan
"{dari}" "مرکز داده"
"{pashto}" "د معلوماتو مرکز" OR "ډیټا مرکز"
site:pajhwok.com "{province}" "data center"
site:bakhtarnews.af "{province}" "data center"
```

---

## 7. False positives and grading discipline

- Telecom towers, BTS sites, 4G/5G launches, microwave/fiber routes, and ring-road fiber are connectivity, not data centers.
- NIXA, PeeringDB, caches, root DNS, CDN nodes, and IXP membership are edge/network infrastructure unless a host facility is named.
- Cloud-email, SaaS, Oracle/Linux/VMware support, D365, and Google Workspace tenders are service/procurement evidence; they do not prove a new facility.
- "Tier III", "world-class", or "N+1" marketing is not Uptime evidence. Require Uptime certificate URL for certification.
- "Data" in NSIA/open-data/statistical pages is not a data center unless paired with `center`, `server`, `hosting`, `facility`, `cloud`, `DR`, or facility equipment.
- Province assignment requires explicit province/locality. If a vendor says "Afghanistan" only and the client is central government, default to **Kabul with a note**, not a province-specific claim.
