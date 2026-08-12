# LB Explorer Official - Lebanon Datacenter Enumeration

Date: 2026-08-12. Country: **LB Lebanon**. Division model: **8 governorates** from `world-manifest.jsonl`: `Akkar`, `North Lebanon`, `Beirut`, `Baalbek-Hermel`, `Beqaa`, `South Lebanon`, `Mount Lebanon`, `Nabatieh`. Angle: official, regulatory, procurement, state-operator, public-infrastructure, cloud-region, certification, and government-project evidence.

Reliability grades are fact-specific:
- **A** = primary/official/operator-owned source for the exact fact: ministry, regulator, state operator, PPA/e-procurement, World Bank project document, Uptime Institute award page, company/bank official page, NNA for official statements/outages.
- **B** = credible trade or established media with named parties: DCD, Telecom Review, Executive Magazine, ITP.net, Developing Telecoms, Arab News, L'Orient, RIPE NCC, IFEX.
- **C** = directory/aggregator/vendor/social/unreviewed secondary source: DataCenterMap, Cloudscene, Inflect, GeoCables, whtop, LinkedIn, Wikipedia. Use as leads only unless an operator or official source confirms.
- **U** = unresolved or contradicted. Do not create a facility from U-only evidence.

---

## 0. Lebanon-specific facts

- **Administrative coverage is fixed at 8 governorates**: Akkar; North Lebanon; Beirut; Baalbek-Hermel; Beqaa; South Lebanon; Nabatieh; Mount Lebanon. Beirut is both a governorate and municipality. Many ICT sources say "Beirut" when they mean Greater Beirut, which crosses into Mount Lebanon suburbs; record the municipality/site first, then map to the governorate.
- **No public national data-center registry was found.** The Ministry of Economy and Trade (`https://economy.gov.lb/`) and Commercial Register identify companies, not facilities. A company registration is identity evidence only.
- **Telecom authority is centralized.** MoT states that the 1959 regime gave the state telecommunications monopoly and that Law 431/2002 introduced telecom liberalization while fixed/mobile services remain state-controlled in practice (`https://www.mpt.gov.lb/ministry`). Ogero is the fixed/state operating arm; Alfa and Touch are mobile brands operating for the account of the state/MoT.
- **TRA was revived in 2025 after a long vacancy.** TRA says President Joseph Aoun received the newly appointed board on 2025-12-15 after appointment in September 2025 and 13 years of dormancy (`https://www.tra.gov.lb/NewsDetails.aspx?pageid=3738`). MoT announced the regulator's relaunch on 2025-10-06 (`https://www.mpt.gov.lb/the-ministry-news/48`). As of this review, no TRA data-center/cloud licensing registry was found; re-check TRA news before each annual pass.
- **Data protection exists, but supervision was weak as of the latest checked chapter.** Law No. 81 of 2018 is hosted by OMSAR (`https://omsar.gov.lb/en/publication/law-no-81-dated-10-10-2018electronic-transacti-ons-and-personal-data/`). DLA Piper's Lebanon chapter says there is no national data protection authority and that the Ministry of Economy and Trade issues permits/licenses where required (`https://www.dlapiperdataprotection.com/?c=LB&t=law`). Treat this as compliance context, not DC certification.
- **Public procurement route is live.** The Public Procurement Authority is at `https://www.ppa.gov.lb/`; its tenders page includes governorate filters covering Beirut, North Lebanon, Mount Lebanon, South Lebanon, Bekaa, Nabatiyeh, Baalbek Hermel, and Akaar (`https://www.ppa.gov.lb/en/tenders`). OMSAR's e-procurement platform is `https://omsar.eprocurement.gov.lb/` and says it is powered by Delta (`https://omsar.eprocurement.gov.lb/en/powered-by-delta/`). Data-center/server/cloud tenders are pipeline evidence unless an award/site is named.
- **Power is a gating constraint.** EDL is the grid utility (`https://www.edl.gov.lb/`), but the site timed out during validation on 2026-08-12. Official/trade reporting documents chronic electricity/fuel disruption affecting Ogero and ISPs. Facility records need explicit power evidence; do not infer MW or redundancy.
- **Recent conflict and crisis status must be checked outside Beirut/Mount Lebanon.** Akkar, North Lebanon, Beqaa, Baalbek-Hermel, South Lebanon, and Nabatieh require current telecom restoration/outage checks before asserting operational status.
- **The public-sector digital pipeline is real but mostly not yet site-specific.** MoT launched the draft National Telecommunications and Digital Infrastructure Policy 2026-2030 for consultation on 2026-03-10 and extended comments to 2026-04-30 (`https://www.mpt.gov.lb/the-ministry-news/49`, `https://www.mpt.gov.lb/the-ministry-news/50`, PDF at `https://cms.mpt.gov.lb/uploads/2026/3/10/17731505154557af70eca002e4cd4aca09c15a641ad3e.pdf`). The World Bank Lebanon Digital Acceleration Project P506791 was approved 2026-01-26; the 2026-04-28 ISR lists Component 1 Digital Foundations at USD 87.5m and indicators for government community cloud, data-center PUE, and USD 11m private capital enabled by data-center investments (`https://documents1.worldbank.org/curated/en/099042826062016422/pdf/P506791-1ef911fc-eee1-4600-92d2-7ca64987c2d5.pdf`). This is a planned/project signal, not an operational facility.

Arabic/French/English lifecycle vocabulary:

```text
مركز بيانات / مراكز البيانات / مركز المعطيات          = data center / centres de donnees
غرفة الخوادم / غرفة السيرفرات / خادم / خوادم          = server room / servers / serveurs
استضافة / استضافة المواقع / استضافة الخوادم          = hosting / hebergement
الحوسبة السحابية / السحابة / الخدمات السحابية         = cloud computing / nuage
البنية التحتية الرقمية / التحول الرقمي                = digital infrastructure / digital transformation
نقطة تبادل الإنترنت                                   = internet exchange point
الكابل البحري / الكوابل البحرية / كابل الألياف        = submarine cable / cable sous-marin
محطة الإنزال / محطة الهبوط                            = landing station
مزود خدمة الإنترنت / مزود خدمة نقل المعلومات          = ISP / DSP
هيئة تنظيم الاتصالات                                  = Telecommunications Regulatory Authority
رخصة بناء / ترخيص / إجازة                             = building permit / licence
مناقصة / عطاء / استدراج عروض / دورة العطاءات          = tender / procurement
الحكومة الإلكترونية / الخدمات الإلكترونية              = e-government / e-services
وزارة الاتصالات / أوجيرو                              = Ministry of Telecommunications / Ogero
```

---

## 1. Official query templates

Core bilingual searches:

```text
"لبنان" "مركز بيانات"
"مركز بيانات" "بيروت" OR "جبل لبنان"
"مركز المعطيات" لبنان
"مركز بيانات" "أوجيرو" OR "وزارة الاتصالات"
"مركز بيانات" "هيئة تنظيم الاتصالات" OR "TRA"
"الحوسبة السحابية" "لبنان" "حكومة"
"البنية التحتية الرقمية" لبنان 2026
"استضافة" "خوادم" "لبنان" "وزارة"
"مناقصة" "مركز بيانات" لبنان
"عطاء" "خوادم" OR "أرشفة" OR "مركز بيانات" لبنان
"Lebanon" "data center" government OR ministry
"Lebanon" "national data center" OR "government cloud"
"Lebanon" "digital infrastructure" "2026" policy
"Lebanon" "TRA" "data center" OR "cloud" licensing
```

Official-site scoped searches:

```text
site:tra.gov.lb "data center" OR "cloud" OR "مركز بيانات" OR "السحابة"
site:mpt.gov.lb "مركز بيانات" OR "استضافة" OR "البنية التحتية الرقمية"
site:mpt.gov.lb "عقود ومشاريع" OR "مناقصة"
site:ogero.gov.lb "data" OR "hosting" OR "استضافة" OR "خدمات"
site:ppa.gov.lb "data center" OR "مركز بيانات" OR "خوادم" OR "cloud" OR "استضافة"
site:omsar.eprocurement.gov.lb "data center" OR "مركز بيانات" OR "خوادم"
site:omsar.gov.lb "data center" OR "مركز بيانات" OR "digital" OR "cloud"
site:nna-leb.gov.lb "مركز بيانات" OR "أوجيرو" OR "اتصالات" OR "انقطاع"
site:bdl.gov.lb "data center" OR "مركز بيانات" OR "tender"
site:worldbank.org P506791 Lebanon "data center" OR "government community cloud"
```

---

## 2. Grade A official routes

### 2.1 TRA - Telecommunications Regulatory Authority

- TRA site: `https://www.tra.gov.lb/`. Use for legal/regulatory statements only.
- Board/current-status routes: `https://www.tra.gov.lb/NewsDetails.aspx?pageid=3738`, `https://www.tra.gov.lb/SubPage.aspx?pageid=120&PID=40&FPID=4`.
- Sector-context route: FTTX page `https://www.tra.gov.lb/SubPage.aspx?pageid=3595`.
- Extraction rule: TRA statements about telecom regulation are not facility evidence unless they name a data-center/cloud facility, licence, owner, or site.

### 2.2 Ministry of Telecommunications (MoT)

- MoT site: `https://www.mpt.gov.lb/`.
- Ministry role/legal history: `https://www.mpt.gov.lb/ministry`.
- TRA relaunch: `https://www.mpt.gov.lb/the-ministry-news/48`.
- Draft National Telecommunications and Digital Infrastructure Policy 2026-2030: `https://www.mpt.gov.lb/the-ministry-news/49`, `https://www.mpt.gov.lb/the-ministry-news/50`, PDF at `https://cms.mpt.gov.lb/uploads/2026/3/10/17731505154557af70eca002e4cd4aca09c15a641ad3e.pdf`.
- ISP/DSP lists under the MoT site are licensed-operator universe evidence, not facility evidence.

### 2.3 Ogero and mobile operators

- Ogero: `https://www.ogero.gov.lb/`, `https://ogero.gov.lb/meet.php`. A for Ogero identity/backbone statements. No public Ogero commercial colocation/data-center specification page was found during this review.
- Alfa: `https://www.alfa.com.lb/`. Touch: `https://touch.com.lb/`. A for identity/operator statements. Mobile core sites are institutional telecom infrastructure unless a source names a data-center site.
- Ogero outage/context routes are usually B unless NNA/operator-owned: DCD `https://www.datacenterdynamics.com/en/news/lebanese-telco-ogero-hit-by-outages-amid-diesel-shortage/`; Developing Telecoms `https://developingtelecoms.com/telecom-business/operator-news/11304-blackouts-impacting-connectivity-in-lebanon-warns-ogero-boss.html` and `https://developingtelecoms.com/telecom-business/operator-news/14763-network-blackout-imminent-in-lebanon-as-ogero-workers-strike-over-pay.html`; Arab News `https://www.arabnews.com/node/2587374/business-economy`.

### 2.4 Procurement and public digital programs

- PPA official portal: `https://www.ppa.gov.lb/`; tenders: `https://www.ppa.gov.lb/en/tenders`.
- OMSAR: `https://omsar.gov.lb/en/home/`; Law 81: `https://omsar.gov.lb/en/publication/law-no-81-dated-10-10-2018electronic-transacti-ons-and-personal-data/`; e-procurement: `https://omsar.eprocurement.gov.lb/`.
- BDL publishes tender notices through PPA per `https://bdl.gov.lb/pressrelease1.php?pressid=8592`.
- World Bank LDAP P506791: project-document route `https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099063025040018679`; ISR PDF `https://documents1.worldbank.org/curated/en/099042826062016422/pdf/P506791-1ef911fc-eee1-4600-92d2-7ca64987c2d5.pdf`; OMSAR project page `https://omsar.gov.lb/en/lebanon-digital-acceleration-project/`.
- Extraction rule: procurement or project indicators such as "government community cloud" or "data center investments" are planned/pipeline until a contract, site, operator, or operational launch is identified.

### 2.5 Energy, planning, and permits

- EDL: `https://www.edl.gov.lb/` timed out in validation; keep as official route but verify per pass.
- CDR: `https://www.cdr.gov.lb/` returned a Cloudflare challenge/403 in validation; use if accessible through browser/search.
- IDAL: `https://www.idal.com.lb/` returned HTTP 525 in validation; use as investment-promotion route only when accessible.
- Public Works/DGU candidate domain `https://www.public-works.gov.lb/` did not resolve in validation. There is no central online building-permit registry found. Permit research is only useful after a candidate site is known.

### 2.6 Certifications and public institutions

- Uptime Lebanon country page: `https://uptimeinstitute.com/uptime-institute-awards/country/id/LB`.
- Byblos Tower B1 Data Center Uptime page: `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681`; confirms Byblos Bank s.a.l. as client. The bank's newsroom gives the public inauguration and location context at `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center`.
- BDL: `https://bdl.gov.lb/`. BDL and other public institutions may operate server rooms, but no public facility-level DC evidence was found.
- NNA: `https://www.nna-leb.gov.lb/`; useful for official telecom outages/restoration and ministerial statements.

---

## 3. Cloud-region and edge handling

| Provider | Official source | LB signal as of 2026-08-12 | Handling |
|---|---|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html` | No Lebanon public cloud region or local zone found. Nearest region-class routes are elsewhere in the Middle East. | Do not map AWS region/AZ to LB. |
| Google Cloud | `https://cloud.google.com/about/locations`; `https://docs.cloud.google.com/compute/docs/regions-zones` | No Lebanon GCP region/zone found. | Do not map GCP region/zone to LB. |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; `https://azure.microsoft.com/en-us/explore/global-infrastructure` | No Lebanon Azure public cloud region found. | Do not map Azure region to LB. |
| Oracle Cloud | `https://www.oracle.com/cloud/public-cloud-regions/`; `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm` | No Lebanon OCI public cloud region found. | Do not map OCI region to LB. |
| Cloudflare | `https://www.cloudflare.com/network/`; 2021 press release lists Beirut, LB in Middle East network (`https://www.cloudflare.com/press/press-releases/2021/cloudflare-grows-its-network-to-speed-up-and-secure-the-internet/`) | CDN/edge POP signal in Beirut, not a public cloud region and not enough to identify a standalone data center. | Record as edge/network presence only if the schema supports it; do not count as hyperscale DC. |

---

## 4. Governorate coverage and routing

| Division | Official/local anchors | Current evidence and handling |
|---|---|---|
| `Beirut` | بيروت, Ashrafieh, Bir Hassan, Bachoura, Ras Beirut, Sallim Salam, Jnah, Forn El Chebbak | Main official/finance/telecom cluster. Confirmed Byblos Bank Data Center at Ashrafieh HQ. MoT/TRA/Ogero/OMSAR/BDL institutional hosting is context unless site-specific. IXPs and Cloudflare edge are network/edge signals, not DCs. |
| `Mount Lebanon` | جبل لبنان, Chouf/Shouf, Medyar, Dibbieh, Sinn El Fil, Jdeideh, Baabda, Jounieh, Metn | LFAIT Medyar lead in Shouf/Medyar has operator site plus DataCenterMap listing; facility details are mixed A/C. Jdeideh landing point is C via GeoCables. No official DC registry evidence. |
| `North Lebanon` | الشمال, طرابلس, Tripoli, Koura, Batroun | IMEWE landing station at Tripoli is cable infrastructure, not DC. Ogero central offices only unless a source names a DC. Current outage/restoration check required. |
| `Akkar` | عكار, Halba | No verified DC. Treat telecom/power outage items as status context only. Current status check required. |
| `Baalbek-Hermel` | بعلبك, الهرمل | No verified DC. Conflict/restoration check required before operational assumptions. |
| `Beqaa` | البقاع, Zahle, Bekaa | No verified DC. Conflict/restoration and power check required. |
| `South Lebanon` | الجنوب, Saida/Sidon, Tyre | Saida cable landing leads are cable infrastructure, not DC. Telecom restoration reports are status context. No verified DC. |
| `Nabatieh` | النبطية | No verified DC. Use NNA/local press for Ogero/mobile restoration/outage status only. |

Boundary rule: if a source says only "Beirut" and the address is a suburb such as Sinn El Fil, Forn El Chebbak, Jnah, or Chouf/Medyar, do not force it into Beirut governorate. Map by actual municipality/district when available.

---

## 5. Acceptance rules

Extract these fields:

```text
name
operator / owner / government body
division and municipality
site / building / zone if public
status: planned | tendered | permitted | construction | operational | damaged | cancelled | rejected
capacity_mw (usually null)
area_sqm / racks / servers / service claims if stated
power: grid, generator, UPS, solar, battery, multiple feeds
cloud/service links: colocation, DR, VPS, IaaS/PaaS/SaaS, government community cloud
primary evidence URL and date
evidence grade for each asserted fact
confidence notes
```

Acceptance thresholds:
- **Operational facility**: operator/government opening statement, official facility page, Uptime certification plus owner/trade corroboration, or official/procurement/World Bank text naming an existing data center.
- **Tendered/planned facility**: PPA/OMSAR/MoT/World Bank document naming data-center, cloud, government hosting, data center investment, or implementation; keep as pipeline if no site is named.
- **Damaged/intermittent facility**: NNA/operator/trade evidence of outage or conflict damage; never silently preserve old operational status in Akkar, North Lebanon, Beqaa, Baalbek-Hermel, South Lebanon, or Nabatieh.
- **Reject / no-project**: generic FTTH, ISP licence, network coverage, cable landing, tower, ASN, IXP, CDN POP, academic compute, or policy vision without facility evidence.

---

## 6. Known facilities/projects and evidence status

| Candidate | Evidence | Grade | Status |
|---|---|---|---|
| Byblos Bank Data Center / Byblos Tower B1 Data Center | Byblos newsroom `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center`; Uptime page `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681` | A for owner/inauguration/Uptime client; A for Uptime listing | Operational private bank DC in Beirut/Ashrafieh since 2019; not colocation |
| Lebanon Digital Acceleration Project government community cloud/data-center investments | World Bank ISR lines for Component 1, data-center PUE, government community cloud, private capital enabled by data-center investments | A | Planned/pipeline, no public site/operator yet |
| Ogero institutional/backbone hosting | Ogero/MoT identity and role pages | A for operator role; U for any DC spec | Institutional telecom hosting/backbone; do not record commercial DC specs |
| LFAIT Medyar / LFAIT Beirut sites | Operator portal `https://lfait.com/`; announcements include "Lebanon/Medyar DC" `https://lfait.com/announcements/page/2`; DataCenterMap listings for Shouf/Beirut | A for operator/service claims; C for directory facility details | Commercial hosting/colo lead; promote only facts supported by operator or corroborated directory notes |
| Government e-services hosting / Dawlati / ministry systems | OMSAR and Dawlati routes | A for program identity; U for facility | Institutional hosting, no public DC spec |
| Beirut-IX / LEB-IX / OpenIX Beirut | `http://www.beirutix.net/`, `https://lebix.org.lb/`, `https://p.foundation/updates/IntroducingOpenIXBeirut` | B/C depending source | Network facilities/IXPs, not DCs |
| Cloudflare Beirut | Cloudflare 2021 press release lists Beirut, LB | A for Cloudflare network city | CDN/edge POP, not a hyperscaler region or standalone DC record |
| IMEWE Tripoli landing; CADMOS-2/Berytar landings | SubmarineCableMap Tripoli; Executive/ITP; GeoCables/Wikipedia leads | B/C | Cable infrastructure, not DC |
| TerraNet colocation in NOC | TerraNet product page `https://www.terra.net.lb/products/Terraweb` says customer servers can be placed in its Network Operations Center with UPS/generators/climate/security | A for TerraNet service claim | Small colo/NOC service lead; no standalone data-center specs |
| DataCenterMap Lebanon country page | `https://www.datacentermap.com/lebanon/` says 2 DCs in Beirut and Shouf; detail page for Shouf names LFAIT Medyar | C | Directory lead only |
| Banks other than Byblos, universities, BDL core systems | No public facility-level evidence found | U | Do not record unless official/operator evidence appears |

---

## 7. Re-check cadence

- **Quarterly 2026-2027**: World Bank P506791, OMSAR, MoT policy implementation, PPA/e-procurement tenders, TRA news after the 2025 relaunch.
- **Quarterly**: Ogero news/bids, NNA telecom, DCD, Developing Telecoms, Telecom Review, L'Orient, Arab News.
- **Before any non-Beirut enumeration**: outage/restoration status for Akkar, North Lebanon, Beqaa, Baalbek-Hermel, South Lebanon, Nabatieh.
- **Semi-annual**: Uptime Lebanon country page; DataCenterMap/Cloudscene/Inflect as C-grade leads; SubmarineCableMap/GeoCables for landing changes; AWS/GCP/Azure/OCI region lists; Cloudflare network map/press.
- **Annual**: Law 81/DLA Piper implementation status; IDAL/CDR/EDL accessibility; bank annual reports for official DC mentions.

---

## 8. Source index

Official/primary checked live or reachable in search:
- TRA: `https://www.tra.gov.lb/`; `https://www.tra.gov.lb/NewsDetails.aspx?pageid=3738`; `https://www.tra.gov.lb/SubPage.aspx?pageid=120&PID=40&FPID=4`; `https://www.tra.gov.lb/SubPage.aspx?pageid=3595`
- MoT: `https://www.mpt.gov.lb/`; `https://www.mpt.gov.lb/ministry`; `https://www.mpt.gov.lb/the-ministry-news/48`; `https://www.mpt.gov.lb/the-ministry-news/49`; `https://www.mpt.gov.lb/the-ministry-news/50`; `https://cms.mpt.gov.lb/uploads/2026/3/10/17731505154557af70eca002e4cd4aca09c15a641ad3e.pdf`
- Ogero/Alfa/Touch: `https://www.ogero.gov.lb/`; `https://ogero.gov.lb/meet.php`; `https://www.alfa.com.lb/`; `https://touch.com.lb/`
- PPA/OMSAR/e-procurement: `https://www.ppa.gov.lb/`; `https://www.ppa.gov.lb/en/tenders`; `https://omsar.gov.lb/en/home/`; `https://omsar.eprocurement.gov.lb/`; `https://omsar.eprocurement.gov.lb/en/powered-by-delta/`; `https://omsar.gov.lb/en/lebanon-digital-acceleration-project/`
- Law/data protection: `https://omsar.gov.lb/en/publication/law-no-81-dated-10-10-2018electronic-transacti-ons-and-personal-data/`; `https://www.dlapiperdataprotection.com/?c=LB&t=law`; `https://economy.gov.lb/`
- World Bank: `https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099063025040018679`; `https://documents1.worldbank.org/curated/en/099042826062016422/pdf/P506791-1ef911fc-eee1-4600-92d2-7ca64987c2d5.pdf`
- Certifications/company primary: `https://uptimeinstitute.com/uptime-institute-awards/country/id/LB`; `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681`; `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center`; `https://lfait.com/`; `https://lfait.com/announcements/page/2`; `https://www.terra.net.lb/products/Terraweb`
- Cloud providers: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`; `https://cloud.google.com/about/locations`; `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; `https://www.oracle.com/cloud/public-cloud-regions/`; `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`; `https://www.cloudflare.com/network/`; `https://www.cloudflare.com/press/press-releases/2021/cloudflare-grows-its-network-to-speed-up-and-secure-the-internet/`
- Official but not fully accessible in validation: `https://www.edl.gov.lb/` timed out; `https://www.idal.com.lb/` returned 525; `https://www.cdr.gov.lb/` returned Cloudflare challenge/403; `https://www.public-works.gov.lb/` did not resolve.

Secondary/trade/directory routes:
- DCD: `https://www.datacenterdynamics.com/en/news/lebanese-telco-ogero-hit-by-outages-amid-diesel-shortage/`
- Developing Telecoms: `https://developingtelecoms.com/telecom-business/operator-news/11304-blackouts-impacting-connectivity-in-lebanon-warns-ogero-boss.html`; `https://developingtelecoms.com/telecom-business/operator-news/14763-network-blackout-imminent-in-lebanon-as-ogero-workers-strike-over-pay.html`
- Executive/ITP/IFEX: `https://www.executive-magazine.com/economics-policy/lebanon-telecommunications-growth`; `https://www.itp.net/telecommunications/network-infrastructure/585338-imewe-cable-goes-live-in-lebanon`; `https://ifex.org/everyone-else-owns-subsea-cables-why-doesnt-lebanon/`
- Cables/IXP/directories: `https://www.submarinecablemap.com/landing-point/tripoli-lebanon`; `https://geocables.com/locations/lb`; `http://www.beirutix.net/`; `https://lebix.org.lb/`; `https://p.foundation/updates/IntroducingOpenIXBeirut`; `https://www.datacentermap.com/lebanon/`; `https://cloudscene.com/market/data-centers-in-lebanon/beirut`; `https://inflect.com/datacenters/emea/lebanon/beirut`; `https://www.datacentermap.com/lebanon/shouf/medyar/`; `https://www.datacentermap.com/lebanon/beirut/leb-dc-1/`
