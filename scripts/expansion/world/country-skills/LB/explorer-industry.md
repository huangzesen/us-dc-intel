# LB Explorer Industry - Lebanon Datacenter Enumeration

Date: 2026-08-12. Country: **LB Lebanon**. Scope: industry, trade press, operator, vendor, directory, cable/IXP, CDN/edge, and local-media discovery for the 8 governorates: `Akkar`, `North Lebanon`, `Beirut`, `Baalbek-Hermel`, `Beqaa`, `South Lebanon`, `Mount Lebanon`, `Nabatieh`.

Reliability grades are fact-specific:
- **A** = operator/company official page, Uptime Institute award page, bank/company official release naming a facility, ministry/regulator/NNA primary source.
- **B** = established trade/business reporting with named parties: DCD, Telecom Review, Executive Magazine, ITP.net, Developing Telecoms, Arab News, RIPE NCC, IFEX, L'Orient.
- **C** = directories/marketplaces/social/vendor mirrors: DataCenterMap, Cloudscene, Inflect, GeoCables, whtop, LinkedIn, Wikipedia. Use for leads and aliases, not final facility status.
- **U** = unresolved; never create a facility from U-only evidence.

Industry discovery must end with official/operator verification. C-grade leads can seed candidates, aliases, and rough locations, but do not carry capacity, uptime, or operational claims into final records without better support.

---

## 0. Market frame

- Lebanon has a small in-country data-center market. The public evidence points to bank private facilities, small ISP/hosting/NOC colocation, Ogero/government institutional hosting, mobile core infrastructure, IXPs, cable landings, and CDN/edge POPs. It does not show a hyperscale campus or AWS/GCP/Azure/OCI public cloud region.
- The strongest confirmed private facility is **Byblos Bank / Byblos Tower B1 Data Center** in Beirut/Ashrafieh. Byblos announced it on 2019-06-24 and Uptime has a Lebanon award page for Byblos Tower B1. It is a bank-owned private facility, not a public colocation offer.
- **LFAIT** is the strongest commercial hosting/colo lead found in this review. Its operator portal advertises Lebanon servers and "enterprise infrastructure powered by VMware clusters across multiple datacenters" (`https://lfait.com/`), and its announcements refer to "Lebanon/Medyar DC" (`https://lfait.com/announcements/page/2`). DataCenterMap lists LFAIT Medyar in Shouf/Mount Lebanon and LFAIT Ras Beirut. Treat operator-owned service/location facts as A, but directory power/space/Tier values as C until operator-confirmed.
- **TerraNet** officially advertises co-location in its Network Operations Center, including UPS, automatic generators, climate control, and secure access (`https://www.terra.net.lb/products/Terraweb`). This is an A-grade small colo/NOC service claim, but not enough for a standalone data-center facility spec.
- **Ogero** operates the fixed backbone/international gateways and supports government/enterprise connectivity, but no public Ogero commercial DC specification page was found. Treat "Ogero data center" claims as U unless a facility-naming source appears.
- **Network layer matters but is not DC evidence.** Beirut-IX, LEB-IX, OpenIX Beirut, Cloudflare Beirut, IMEWE Tripoli, and CADMOS-2/Berytar landing points are useful anchors for connectivity, not data centers unless colocated facility evidence is found.
- **Crisis context gates status.** Power shortages, fuel interruptions, strikes, and 2024-2025 conflict damage have affected Ogero/mobile/ISP networks. Any pre-crisis facility outside Beirut/Mount Lebanon needs a current status check.

Core search vocabulary:

```text
data center / data centre / datacenter / server farm
colocation / co-location / collocation / hosting / cloud / VPS / DR / managed hosting
مركز بيانات / مراكز البيانات / مركز المعطيات / غرفة الخوادم
استضافة / استضافة الخوادم / استضافة المواقع / الحوسبة السحابية / السحابة
نقطة تبادل الإنترنت / تبادل / peering
الكابل البحري / الكوابل البحرية / محطة الإنزال
أوجيرو / ألفا / تاتش / وزارة الاتصالات
```

---

## 1. High-signal industry and media sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Byblos Bank | `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center` | Owner announcement for the Byblos Bank data center | A |
| Uptime Institute | `https://uptimeinstitute.com/uptime-institute-awards/country/id/LB`; `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681` | Certification/client evidence | A |
| LFAIT | `https://lfait.com/`; `https://lfait.com/announcements/page/2`; `https://lfait.com/announcements/8` | Operator-owned hosting/server/DC identity and Medyar lead | A for operator text |
| TerraNet | `https://www.terra.net.lb/products/Terraweb` | Operator-owned co-location-in-NOC service claim | A for service claim |
| Data Center Dynamics | `https://www.datacenterdynamics.com/en/news/lebanese-telco-ogero-hit-by-outages-amid-diesel-shortage/` | Ogero/power outage context | B |
| Telecom Review | `https://www.telecomreview.com/`; Ogero interviews `/articles/exclusive-interviews/2045-ogero-connecting-the-nation`, `/2210-ogero-committed-to-improving-the-telecoms-sector-in-lebanon/`; Touch `/3115-touch-playing-a-key-role-in-the-constantly-evolving-lebanese-telecom-sector` | Operator interviews/sector context | B |
| Executive Magazine | `https://www.executive-magazine.com/economics-policy/lebanon-telecommunications-growth` | Cables/capacity context | B |
| ITP.net | `https://www.itp.net/telecommunications/network-infrastructure/585338-imewe-cable-goes-live-in-lebanon`; `https://www.itp.net/news/472069-ogero-and-cisco-link-in-lebanon` | Cable/network infrastructure | B |
| Developing Telecoms | `https://developingtelecoms.com/telecom-business/operator-news/11304-blackouts-impacting-connectivity-in-lebanon-warns-ogero-boss.html`; `https://developingtelecoms.com/telecom-business/operator-news/14763-network-blackout-imminent-in-lebanon-as-ogero-workers-strike-over-pay.html` | Operational crisis and Ogero status | B |
| Arab News | `https://www.arabnews.com/node/2587374/business-economy` | Ogero expansion/restoration context | B |
| L'Orient Today | `https://today.lorientlejour.com/article/1265636/internet-connectivity-the-latest-in-a-line-of-services-falling-victim-to-lebanons-electricity-shortages.html` | Electricity/internet crisis context | B |
| IFEX | `https://ifex.org/everyone-else-owns-subsea-cables-why-doesnt-lebanon/` | Subsea ownership analysis | B |
| RIPE NCC / PeeringDB | RIPE Ogero pages; `https://www.peeringdb.com/asn/42003` | LIR/ASN/peering identity | B/C |
| DataCenterMap | `https://www.datacentermap.com/lebanon/`; `https://www.datacentermap.com/lebanon/shouf/medyar/`; `https://www.datacentermap.com/lebanon/beirut/leb-dc-1/` | Directory leads for LFAIT and markets | C |
| Cloudscene / Inflect | `https://cloudscene.com/market/data-centers-in-lebanon/beirut`; `https://inflect.com/datacenters/emea/lebanon/beirut` | Directory leads: Berytech, DOT/LBIX, Advanced IX, counts | C |
| SubmarineCableMap / GeoCables | `https://www.submarinecablemap.com/landing-point/tripoli-lebanon`; `https://geocables.com/locations/lb` | Cable landing leads | B/C |
| Cloudflare | `https://www.cloudflare.com/network/`; `https://www.cloudflare.com/press/press-releases/2021/cloudflare-grows-its-network-to-speed-up-and-secure-the-internet/` | Beirut CDN/edge city signal | A for Cloudflare network city |
| Local crisis media | This Is Beirut, Kataeb, The961, The Street Journal | Outage/restoration granularity | C/B; prefer NNA/operator if available |

Industry query templates:

```text
site:datacenterdynamics.com Lebanon "data center" OR Ogero OR Beirut
site:telecomreview.com Lebanon "data center" OR "مركز بيانات" OR cloud
site:developingtelecoms.com Lebanon Ogero OR Alfa OR outage
site:itp.net Lebanon cable OR Ogero
"Lebanon" "colocation" OR "co-location" "data center"
"Lebanon" "server farm" OR "hosting" OR "managed hosting"
"لبنان" "مركز بيانات" "افتتاح" OR "تدشين" OR "إطلاق"
"لبنان" "خوادم" "استضافة" "شركة"
"Ogero" "data center" OR "cloud" OR "استضافة"
"Alfa" OR "Touch" "لبنان" "مركز بيانات" OR "داتا سنتر"
"Byblos Bank" "Byblos Tower B1" "Uptime"
"LFAIT" OR "Lebanese For Advanced Information Technologies" "Medyar" "data center"
"TerraNet" Lebanon "Network Operations Center" "co-location"
"Cyberia" OR "IDM" OR "Sodetel" Lebanon "data center" OR "hosting"
"Beirut" "internet exchange" OR "IXP" OR "peering"
"Lebanon" "submarine cable" landing OR "landing station"
```

---

## 2. Operator and vendor seed list

| Entity | Source routes | Industry signal | Handling |
|---|---|---|---|
| Byblos Bank | Byblos newsroom; Uptime Byblos Tower B1 page | Private Tier III constructed bank DC at Ashrafieh HQ | Confirmed operational private DC; not colocation |
| LFAIT - Lebanese For Advanced Information Technologies SARL | `https://lfait.com/`; `https://lfait.com/announcements/page/2`; DataCenterMap LFAIT pages | Lebanon servers, VMware clusters across datacenters, Medyar DC, directory-listed Medyar and Ras Beirut | Commercial colo/hosting lead. A for operator claims; C for directory specs/Tier/power/space |
| TerraNet | `https://www.terra.net.lb/products/Terraweb` | Web hosting plus co-location in its NOC with UPS/generators/climate/security | A for NOC colocation service; site/facility scale unknown |
| Ogero | `https://www.ogero.gov.lb/`; `https://ogero.gov.lb/meet.php`; PeeringDB AS42003; RIPE | Backbone, international gateways, state telecom hosting context | A identity; no public commercial DC spec found |
| Alfa / Touch | `https://www.alfa.com.lb/`; `https://touch.com.lb/` | Mobile core network infrastructure | A identity; institutional only unless a DC site is named |
| Cyberia | `https://www.cyberia.net.lb/` | ISP and hosting lead | Service evidence only; no facility spec found |
| IDM | `https://www.idm.net.lb/` | ISP, fiber/corporate access, possible hosting lead | Service evidence only; no facility spec found |
| Sodetel | `https://sodetel.net.lb/our-story` | Data services/enterprise telecom history | Service evidence only; no facility spec found |
| Berytech / BDD | BDD/Berytech routes; Inflect/Cloudscene directories | Innovation district/technology pole; directory lists Berytech SCAL | C lead; not a DC without operator confirmation |
| Advanced IX / DOT LBIX | Inflect and IXP sources | IXP/network facility leads in Beirut suburbs | Network/IXP category, not DC unless operator confirms colocation |
| Banks other than Byblos | annual reports/news searches | Likely private core/DR rooms | U until official evidence names a facility |
| Universities | AUB/LAU/USJ/LU domains; Nature Middle East HPC article | Academic compute/server rooms | Institutional compute, not commercial DC |

Operator templates:

```text
site:ogero.gov.lb "مركز بيانات" OR "استضافة" OR "cloud" OR "data"
site:alfa.com.lb "مركز بيانات" OR "داتا سنتر" OR "cloud"
site:touch.com.lb "مركز بيانات" OR "cloud" OR "استضافة"
site:lfait.com "Medyar DC" OR "Datacenter" OR "Lebanon/Medyar" OR "Servers \"Lebanon\""
site:terra.net.lb "Co-location" OR "Network Operations Center" OR "data center"
site:cyberia.net.lb "hosting" OR "colocation" OR "cloud" OR "مركز بيانات"
site:idm.net.lb "hosting" OR "colocation" OR "data center"
site:sodetel.net.lb "hosting" OR "cloud" OR "data center"
site:byblosbank.com "data center" OR "Tier III"
site:beirutdigitaldistrict.com "data" OR "hosting" OR "infrastructure"
```

---

## 3. Confirmed and lead handling

### 3.1 Byblos Bank Data Center / Byblos Tower B1 (Beirut / Ashrafieh)

Verified source stack:
- Byblos Bank newsroom, 2019-06-24: `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center`.
- Uptime Institute data-center page: `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681`.
- Uptime Lebanon country route: `https://uptimeinstitute.com/uptime-institute-awards/country/id/LB`.

Record as:

```text
name: Byblos Bank Data Center / Byblos Tower B1 Data Center
operator: Byblos Bank s.a.l.
division: Beirut
municipality/site: Ashrafieh / Byblos Bank headquarters, if the record supports public site text
status: operational since 2019
capacity_mw: null
certification: Uptime Tier III constructed / Byblos Tower B1, per Uptime and Byblos
services: private bank infrastructure, not public colocation
confidence: high for existence, owner, private status, and Tier III constructed claim; no MW/rack data
```

### 3.2 LFAIT Medyar and Ras Beirut commercial DC leads

Verified source stack:
- Operator portal: `https://lfait.com/` advertises Lebanon servers and infrastructure across multiple datacenters.
- Operator announcement page: `https://lfait.com/announcements/page/2` references "Lebanon/Medyar DC" maintenance/migration.
- Operator identity page: `https://lfait.com/announcements/8` gives company registration and Medyar address.
- DataCenterMap country page says Lebanon has 2 listed data centers, one in Beirut and one in Shouf (`https://www.datacentermap.com/lebanon/`). Shouf page identifies LFAIT Medyar (`https://www.datacentermap.com/lebanon/shouf/medyar/`); search result also exposes LFAIT Ras Beirut (`https://www.datacentermap.com/lebanon/beirut/leb-dc-1/`).

Record cautiously:

```text
name: LFAIT Medyar
operator: Lebanese For Advanced Information Technologies SARL
division: Mount Lebanon
municipality/site: Medyar / Dibbieh Rd / Shouf, per operator and DataCenterMap
status: operational lead
capacity_mw: null unless operator confirms; directory MW values remain C-only
services: servers, cloud/VPS, colocation, remote hands, per operator/directory
confidence: medium; A for operator identity and Medyar DC reference, C for directory facility specs
```

```text
name: LFAIT Ras Beirut
operator: Lebanese For Advanced Information Technologies SARL
division: Beirut, if Kraitem/Ras Beirut address is confirmed
status: operational lead
capacity_mw: null unless operator confirms; directory MW values remain C-only
confidence: low-medium; C directory lead plus A operator multi-datacenter claim, but operator page did not expose a dedicated Ras Beirut facility page in this review
```

Do not copy DataCenterMap/ColocationM claims such as MW, sqm, Tier 1, PCI, ISO, or SAS70 into final facility records without operator or certification evidence.

### 3.3 TerraNet NOC co-location

TerraNet's official product page says its co-location service places customer servers in its Network Operations Center and lists internet connectivity, reliable power with redundant UPS and automatic generators, climate control, and secure access (`https://www.terra.net.lb/products/Terraweb`).

Record as a small colocation/NOC service lead:

```text
name: TerraNet Network Operations Center co-location
operator: TerraNet S.A.L.
division: null until address is verified; likely Greater Beirut but do not infer
status: operational service claim
capacity_mw: null
services: customer server placement / hosting
confidence: medium for service; low for facility geometry/site because no public address/spec was found on the product page
```

### 3.4 Ogero institutional hosting / "Ogero data center"

Ogero is central to Lebanon's backbone and international connectivity, but no public commercial colocation/DC page with specs was found. Keep Ogero as state telecom infrastructure and a procurement/source route. Promote only when a page names a data-center facility, address, or formal hosting/cloud product.

### 3.5 IXPs, edge POPs, and peering points

- Beirut-IX: `http://www.beirutix.net/`; DataCenterMap IXP page `https://www.datacentermap.com/ixp/beirut-internet-exchange/`.
- LEB-IX: `https://lebix.org.lb/`; verify any anomalous registration date text before quoting.
- OpenIX Beirut: P Foundation announcement `https://p.foundation/updates/IntroducingOpenIXBeirut`.
- Cloudflare Beirut: official Cloudflare press release lists Beirut, LB as a Middle East city in Cloudflare's network (`https://www.cloudflare.com/press/press-releases/2021/cloudflare-grows-its-network-to-speed-up-and-secure-the-internet/`).

These are network/edge facilities. Use them for connectivity context and colocation lead generation; do not count them as data centers without facility evidence.

### 3.6 Subsea cable landing stations

- Tripoli (North Lebanon): IMEWE landing; use SubmarineCableMap Tripoli (`https://www.submarinecablemap.com/landing-point/tripoli-lebanon`) plus Executive/ITP/IFEX for context.
- Beirut / Jdeideh / Saida / Tripoli: GeoCables lists Lebanon landing points (`https://geocables.com/locations/lb`); treat as C unless corroborated by cable owner/operator.
- Historical Berytar and CADMOS-2 are cable infrastructure, not DCs. Planned cable claims such as "Europa" need current confirmation before use.

### 3.7 Directory-only false positives

Downgrade or reject:
- US places named Lebanon, especially Meta's 2026 Lebanon, Indiana data center.
- Cloudscene/Inflect/DataCenterMap provider counts without operator support.
- Berytech/BDD office or incubator listings unless an operator page confirms a data-center service.
- IXP, ASN, cable landing, CDN POP, cloud reseller, or ISP licence records miscategorized as DCs.
- Any "15 MW" or similar Lebanon capacity from C-grade mirrors/directories unless operator/certification/procurement evidence confirms it.

---

## 4. Governorate-by-governorate industry matrix

| Division | Industry query anchors | Current result |
|---|---|---|
| `Beirut` | Beirut, بيروت, Ashrafieh, Ras Beirut, Kraitem, Sallim Salam, Jnah, Forn El Chebbak, Ogero, Alfa, Touch, Byblos, LFAIT, TerraNet, BDD, Beirut-IX, OpenIX, Cloudflare | Confirmed Byblos private bank DC. LFAIT Ras Beirut is a C/A commercial lead. TerraNet NOC co-location likely Greater Beirut but address not verified. IXPs/Cloudflare are network/edge only. |
| `Mount Lebanon` | Mount Lebanon, جبل لبنان, Shouf/Chouf, Medyar, Dibbieh, Sinn El Fil, Jdeideh, Metn, Baabda, Jounieh | LFAIT Medyar is the main commercial lead. Jdeideh cable landing is a C lead. No official registry. |
| `North Lebanon` | Tripoli, طرابلس, Koura, Batroun, IMEWE | IMEWE Tripoli landing station only; Ogero central offices. No verified DC. |
| `Akkar` | Akkar, عكار, Halba | No DC found. Use outage/restoration checks only. |
| `Baalbek-Hermel` | Baalbek, بعلبك, Hermel, الهرمل | No DC found. Conflict/restoration and power status required. |
| `Beqaa` | Beqaa/Bekaa, البقاع, Zahle, زحلة | No verified DC. Search bank/enterprise DR only with official evidence. |
| `South Lebanon` | Saida/Sidon, صيدا, Tyre, صور, Berytar, CADMOS | Saida cable landing leads only; telecom restoration context. No verified DC. |
| `Nabatieh` | Nabatieh, النبطية | No DC found. Use Ogero/mobile restoration checks only. |

Governorate query pattern:

```text
"{division}" "data center" Lebanon
"{division}" "colocation" Lebanon OR "hosting" Lebanon
"{division}" "Ogero" OR "Alfa" OR "Touch" "مركز بيانات" OR "استضافة"
"{Arabic governorate}" "مركز بيانات" OR "خوادم" OR "استضافة"
"{Arabic governorate}" "أوجيرو" OR "اتصالات" "انقطاع" OR "تضرر" OR "إعادة"
site:datacentermap.com "{division}" Lebanon
site:lfait.com "{division}" OR "Medyar" OR "Ras Beirut"
"{division}" "cable landing" OR "landing station"
```

---

## 5. Verification workflow

1. Seed from official/operator pages, then trade press, then directories.
2. Search exact entity name plus Arabic/French variants.
3. Verify operator identity on official company site, MoT ISP/DSP lists, RIPE/PeeringDB, or commercial register only as identity evidence.
4. Verify physical site from operator announcement, Uptime page, procurement notice, municipality/permit source, or credible named trade report.
5. Verify current operational status; pre-crisis non-Beirut items require outage/restoration checks.
6. Map governorate from the actual address, not marketing wording. Greater Beirut can mean Beirut or Mount Lebanon.
7. Extract power, area, racks, Tier, certifications, and MW only when the source states them and grade each field separately.
8. Keep a confidence note for every C-grade facility lead.

Status terms:

```text
افتتاح / إطلاق / تدشين = launched/opened, likely operational
قيد الإنشاء / يتم إنشاؤه = under construction
اتفاقية / مذكرة تفاهم = agreement/MoU, planned
مناقصة / عطاء / استدراج عروض = tendered/procurement
انقطاع / تضرر / توقف / تدمير = outage/damaged
إعادة إعمار = reconstruction concept unless award/site exists
```

---

## 6. Cloud and hosting interpretation

- `cloud`, `VPS`, `managed hosting`, `cloud storage`, `business solutions`, and `servers Lebanon` are service claims. They prove facility existence only when tied to a named site/operator evidence.
- LFAIT and TerraNet have stronger service evidence than generic ISP hosting leads, but still require careful field grading.
- Ogero/Alfa/Touch cloud-type language maps to facilities only when the source names a site.
- Hyperscaler partner/reseller pages in Lebanon are service usage, not in-country AWS/GCP/Azure/OCI regions.
- Cloudflare Beirut is edge/CDN network presence, not a cloud region and not a standalone DC record.

Cloud absence queries:

```text
"Lebanon" "cloud region" OR "availability zone"
AWS Azure Google Oracle "Lebanon" "region"
"لبنان" "منطقة سحابية" OR "مركز بيانات" "أمازون" OR "جوجل" OR "مايكروسوفت"
site:cloudflare.com Beirut Lebanon network data center
```

---

## 7. Source index

Verified live / usable during this review:
- Byblos Bank: `https://www.byblosbank.com/news-room/byblos-bank-inaugurates-its-new-data-center`
- Uptime: `https://uptimeinstitute.com/uptime-institute-awards/country/id/LB`; `https://uptimeinstitute.com/uptime-institute-awards/datacenter/byblos-tower-b1-data-center/681`
- LFAIT: `https://lfait.com/`; `https://lfait.com/announcements/page/2`; `https://lfait.com/announcements/8`
- TerraNet: `https://www.terra.net.lb/products/Terraweb`
- IDM: `https://www.idm.net.lb/`; Sodetel story: `https://sodetel.net.lb/our-story`; Cyberia: `https://www.cyberia.net.lb/`
- DCD: `https://www.datacenterdynamics.com/en/news/lebanese-telco-ogero-hit-by-outages-amid-diesel-shortage/`
- Telecom Review: `https://www.telecomreview.com/`; `https://www.telecomreview.com/articles/exclusive-interviews/2045-ogero-connecting-the-nation`; `https://www.telecomreview.com/articles/exclusive-interviews/2210-ogero-committed-to-improving-the-telecoms-sector-in-lebanon/`; `https://www.telecomreview.com/articles/exclusive-interviews/3115-touch-playing-a-key-role-in-the-constantly-evolving-lebanese-telecom-sector`
- Executive/ITP/Developing Telecoms/Arab News: `https://www.executive-magazine.com/economics-policy/lebanon-telecommunications-growth`; `https://www.itp.net/telecommunications/network-infrastructure/585338-imewe-cable-goes-live-in-lebanon`; `https://developingtelecoms.com/telecom-business/operator-news/11304-blackouts-impacting-connectivity-in-lebanon-warns-ogero-boss.html`; `https://developingtelecoms.com/telecom-business/operator-news/14763-network-blackout-imminent-in-lebanon-as-ogero-workers-strike-over-pay.html`; `https://www.arabnews.com/node/2587374/business-economy`
- RIPE/PeeringDB: `https://www.ripe.net/membership/member-support/list-of-members/lb/libantelecom/`; `https://www.ripe.net/publications/news/about-ripe-ncc-and-ripe/ogero-inaugurates-ipv6-deployment-in-lebanon-in-collaboration-with-the-ripe-ncc`; `https://www.peeringdb.com/asn/42003`
- IXPs/edge: `http://www.beirutix.net/`; `https://www.datacentermap.com/ixp/beirut-internet-exchange/`; `https://lebix.org.lb/`; `https://p.foundation/updates/IntroducingOpenIXBeirut`; `https://www.cloudflare.com/network/`; `https://www.cloudflare.com/press/press-releases/2021/cloudflare-grows-its-network-to-speed-up-and-secure-the-internet/`
- Cables/directories: `https://www.submarinecablemap.com/landing-point/tripoli-lebanon`; `https://geocables.com/locations/lb`; `https://www.datacentermap.com/lebanon/`; `https://www.datacentermap.com/lebanon/shouf/medyar/`; `https://www.datacentermap.com/lebanon/beirut/leb-dc-1/`; `https://cloudscene.com/market/data-centers-in-lebanon/beirut`; `https://inflect.com/datacenters/emea/lebanon/beirut`
- Local crisis context: `https://today.lorientlejour.com/article/1265636/internet-connectivity-the-latest-in-a-line-of-services-falling-victim-to-lebanons-electricity-shortages.html`; `https://thisisbeirut.com.lb/articles/1314211/telecom-coverage-restored-in-80-of-south-lebanon`; `https://en.kataeb.org/articles/ogero-announces-the-suspension-of-its-services-in-jeita-central`; `https://the961.com/ogero-and-alfa-outages-expected-to-continue/`; `https://thestreetjournal.org/north-lebanon-hospitals-grapple-with-power-telecom-outages/`

Re-check targets:
- Operator pages for dedicated facility details from LFAIT, TerraNet, Cyberia, IDM, Sodetel, WNet, TransGlobal.
- Ogero bids/business/cloud pages and any facility-naming announcement.
- DataCenterMap/Cloudscene/Inflect counts and names, but keep C unless operator-confirmed.
- Uptime Lebanon page for new awards.
- World Bank P506791/PPA for government cloud or data-center contracts.
- Cloudflare/Akamai/CDN POP lists only as edge/network signals.
