# GE Explorer Industry - Georgia Datacenter Enumeration

Date: 2026-08-12. Scope: Georgia (GE), all 12 top-level units in `world-manifest.jsonl`: Abkhazia, Adjara, Guria, Imereti, K'akheti, Kvemo Kartli, Mtskheta-Mtianeti, Rach'a-Lechkhumi-Kvemo Svaneti, Samtskhe-Javakheti, Shida Kartli, Samegrelo-Zemo Svaneti, Tbilisi.

Angle: operators, developers, trade press, catalogs, interconnection records, certifications, contractor pages, FIZ/resident signals and market context that seed official verification. This file discovers leads; `explorer-official.md` decides whether a facility is countable.

Reliability grades used here:

- **A**: first-party operator/developer/service page; official certification body page; official cloud-region list; official FIZ page; official IXP/association page.
- **B**: established trade/local press, public broadcaster, contractor/project case study, investment agency, conference deck from a named operator, IEA/Internet Society/Euro-IX context.
- **C**: DataCenterMap, Baxtel, Datacenters.com, Cloudscene, DC Hub, Inflect, colo.exchange, PeeringDB facility page, LinkedIn/social, business directories, snippets and unsourced market lists.

Catalogs are useful in Georgia because the market is small and operator pages are sparse, but they are not reliable enough for final counting or capacity by themselves.

---

## 0. Market Shape

- Georgia is a small, Tbilisi-centric data-center market with a few operating commercial colo/hosting facilities, several private bank/state data centers, historical crypto/HPC sites, and a small number of planned public or commercial projects.
- DataCenterMap currently lists 5 Georgia facilities across 2 markets, Tbilisi and Batumi: `https://www.datacentermap.com/georgia/` (C). Cloudscene lists a small Tbilisi market with several providers/fabrics: `https://cloudscene.com/market/data-centers-in-georgia/georgia-regional-981` (C). Use these only as seed lists.
- The best first-party commercial operating lead is Cloud9 Dinamo Arena in Tbilisi: `https://cloud9.ge/en/data-center/` and `https://cloud9.ge/` (A).
- The most important pipeline lead is Silknet/Silk Cloud's Tier III commercial data center in Tbilisi. Silknet's own release says it is introducing Georgia's first certified Tier 3 data center through its Orange Polska/Integrated Solutions partnership: `https://silknet.com/en/media/singleview/2310-silknetis-da-orange-is-globaluri-mnishvnelobis-tanamshromloba-akhal-etapze-gadadis` (A for plan). BM.ge reports Aug 2026 groundbreaking, Silk Cloud operation, 2 MW high-resilience capacity and expected 2027 operation: `https://bm.ge/en/news/silknet-breaks-ground-on-georgias-first-tier-iii-certified-commercial-data-center` (B).
- Caucasus Online remains a major incumbent colo/Internet-infrastructure lead. First-party service page: `https://www.co.ge/en/426/` (A); company home page references data center/.GE services: `https://www.co.ge/en/` (A). PeeringDB/catalogs add ecosystem/address leads (C).
- NewTelco Georgia is a strong carrier-neutral lead. NewTelco's group site says NewTelco Georgia has been used as a neutral data center since February 2016 and provides Georgia contact context: `https://newtelco.com/` (A/B). ENOG/NewTelco material and catalogs place it in Tbilisi on A. Politkovskaia Street (B/C).
- Bitfury's Georgia facilities are historically important but must not be treated as current commercial colo without fresh proof. Sources describe Gori (~20 MW) and Gldani/Tbilisi FIZ (40 MW, later media references 60 MW) crypto-mining/HPC infrastructure. First-party historical sale PDF: `https://bitfury.com/content/4-press/2_13_18_bitfury_group_sells_gldani_release.pdf` (A/B); BM.ge TFZ ownership article: `https://bm.ge/en/news/bitfury-is-no-longer-the-owner-of-tbilisi-fiz/130069` (B).
- Uptime Institute has Georgia certification leads: `https://uptimeinstitute.com/uptime-institute-awards/country/id/GE` (A). It lists G Data Data-Center #1 in Tbilisi with Tier III Design certification, Bank of Georgia Main DC (Lilo) with Design and Constructed Facility certification, and TBC TBL-01 with Constructed Facility certification. These are certification leads; bank DCs are private context unless commercial services are found.
- Official public-sector pipeline exists outside Tbilisi: the Ministry of Economy says the former Parliament building in Kutaisi will become a Technology Hub including a powerful data center for Georgian AI: `https://www.economy.ge/?lang=en&nw=2613&page=news` and progress page `https://www.economy.ge/?lang=en&nw=2998&page=news` (A).
- Smaller/regional first-party service leads exist but need site verification: GDKHOST says it hosts services from its own small data center in Georgia: `https://gdkhost.net/pages/about` and `https://gdkhost.net/` (A for claim). Innovative Technology LLC/Telavi was identified in prior batch output at `https://intechnologyllc.com/service/datacenter.html`; re-check live status before using.
- Batumi has only a catalog lead in this review: Cloud9 - Batumi Arena, Shartava Ave 13, listed under construction by DataCenterMap: `https://www.datacentermap.com/georgia/batumi/cloud9-batimu-arena/ecosystem/` (C).
- Free Industrial Zones remain important watchlist buckets: Tbilisi FIZ `https://tfz.ge`, Kutaisi FIZ `https://kutaisifreezone.ge`, Poti FIZ `https://potifreezone.ge` (A for FIZ operator/resident information, not facility proof).
- No AWS, Azure, Google Cloud or Oracle public cloud region is in Georgia (country) unless official location pages change. Use only official lists: AWS `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; Azure `https://azure.microsoft.com/en-us/explore/global-infrastructure/`; Google Cloud `https://cloud.google.com/about/locations`; Google data-center locations `https://datacenters.google/locations`; Oracle `https://www.oracle.com/cloud/public-cloud-regions/`.
- Abkhazia is a separate de-facto/occupied-territory problem. DCD/JAMnews-style crypto-mining/technopark reports can be noted, but exclude from Georgia official enumeration unless the project scope explicitly includes de-facto records.

---

## 1. Industry Search Patterns

### 1.1 English

```
"Georgia" "data center" Tbilisi -Atlanta -USA
"Georgia" "data centre" Tbilisi -Atlanta -USA
"Tbilisi" "data center" colocation
"Tbilisi" "data centre" "carrier neutral"
"Tbilisi" "data center" MW
"Georgia" "data center" "free industrial zone"
"Georgia" "data center" Bitfury Gldani
"Georgia" "data center" Silknet "Silk Cloud"
"Silk Cloud" "data center" Georgia
"Cloud9" "Dinamo Arena" "data center"
"Caucasus Online" "data center" "colocation"
"NewTelco Georgia" "neutral data center"
"G Data Data-Center #1" Tbilisi
"Bank of Georgia Main DC" Lilo
"TBC TBL-01" "data center"
"Kutaisi Technology Hub" "data center"
"GDKHOST" "own small data center"
"Batumi Arena" "data center" Cloud9
site:bm.ge Georgia "data center"
site:georgiatoday.ge Georgia "data center"
site:forbes.ge Georgia "data center"
site:datacenterdynamics.com Georgia Bitfury
```

### 1.2 Georgian

```
მონაცემთა ცენტრი საქართველო
მონაცემთა ცენტრი თბილისი
მონაცემთა ცენტრი მშენებლობა
მონაცემთა ცენტრი ინვესტიცია
სილქნეთი მონაცემთა ცენტრი
სილქ ქლაუდი მონაცემთა ცენტრი
Cloud9 მონაცემთა ცენტრი
კავკასუს ონლაინ მონაცემთა ცენტრი
ნიუტელკო მონაცემთა ცენტრი
ბითფიური მონაცემთა ცენტრი
გლდანი მონაცემთა ცენტრი
ქუთაისის ტექნოლოგიური ჰაბი მონაცემთა ცენტრი
კოლოკაცია საქართველო
სერვერული თბილისი
site:bm.ge მონაცემთა ცენტრი
site:commersant.ge მონაცემთა ცენტრი
site:forbes.ge მონაცემთა ცენტრი
```

### 1.3 Catalog, Certification and Interconnection Seeds

```
site:datacentermap.com/georgia "Data Centers"
site:datacentermap.com/georgia/tbilisi Cloud9
site:datacentermap.com/georgia/batumi Cloud9
site:baxtel.com "Georgia" "Bitfury"
site:datacenters.com/locations/georgia/tbilisi
site:cloudscene.com "Georgia" "data center"
site:dchub.cloud/facilities GE Tbilisi
site:inflect.com Tbilisi NewTelco
site:peeringdb.com/fac Tbilisi Georgia
site:uptimeinstitute.com/uptime-institute-awards Georgia Tbilisi
"Georgia" "IXP" "Tbilisi" "data center"
```

---

## 2. Source List by Grade

### 2.1 Grade A / First-Party or Official Industry Sources

- Cloud9 Tbilisi data center: `https://cloud9.ge/en/data-center/`; Cloud9 home/contact: `https://cloud9.ge/`, `https://cloud9.ge/en/company/contact/`.
- Caucasus Online data center service: `https://www.co.ge/en/426/`; Caucasus Online home: `https://www.co.ge/en/`.
- NewTelco group site with NewTelco Georgia neutral-DC reference: `https://newtelco.com/`.
- Silknet first-party Silk Cloud/Orange partnership and Tier 3 DC plan: `https://silknet.com/en/media/singleview/2310-silknetis-da-orange-is-globaluri-mnishvnelobis-tanamshromloba-akhal-etapze-gadadis`.
- GDKHOST first-party pages: `https://gdkhost.net/pages/about`, `https://gdkhost.net/`.
- Uptime Institute Georgia awards: `https://uptimeinstitute.com/uptime-institute-awards/country/id/GE`; G Data page: `https://uptimeinstitute.com/uptime-institute-awards/datacenter/g-data-datacenter-1/2214`.
- Ministry of Economy Kutaisi Technology Hub pages: `https://www.economy.ge/?lang=en&nw=2613&page=news`, `https://www.economy.ge/?lang=en&nw=2998&page=news`.
- Bitfury first-party historical Gldani sale PDF: `https://bitfury.com/content/4-press/2_13_18_bitfury_group_sells_gldani_release.pdf`; Bitfury corporate `https://bitfury.com`.
- FIZ operator pages: Tbilisi `https://tfz.ge`, Kutaisi `https://kutaisifreezone.ge`, Poti `https://potifreezone.ge`.
- Official negative hyperscale checks: AWS `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; Azure `https://azure.microsoft.com/en-us/explore/global-infrastructure/`; Google Cloud `https://cloud.google.com/about/locations`; Google data centers `https://datacenters.google/locations`; Oracle `https://www.oracle.com/cloud/public-cloud-regions/`.

### 2.2 Grade B / Trade, Press, Conference, Context

- BM.ge Silknet groundbreaking: `https://bm.ge/en/news/silknet-breaks-ground-on-georgias-first-tier-iii-certified-commercial-data-center`; Georgian version `https://bm.ge/news/silqnetma-saqartveloshi-pirveli-tier-iii-sertifitsirebuli-komertsiuli-monatsemta-tsentris-mshenebloba-daitsyo`.
- BM.ge Bitfury/TFZ ownership and capacity context: `https://bm.ge/en/news/bitfury-is-no-longer-the-owner-of-tbilisi-fiz/130069`; Bitfury cooling/electricity context `https://bm.ge/en/news/crypto-miner-bitfury-is-using-magic-baths-to-keep-machines-cool/24425`; electricity-consumer context `https://bm.ge/en/news/which-companies-consume-the-most-electricity-in-georgia/82908`.
- Government of Georgia 2015 Bitfury/Gldani/FIZ appearance: `https://www.gov.ge/index.php?info_id=52950&lang_id=ENG&sec_id=412` (official context; still historical).
- Georgia Today Silk Cloud/Orange article: `https://georgiatoday.ge/silk-cloud-partners-with-orange-polskas-integrated-solutions-to-boost-georgias-digital-transformation/`; Kutaisi tech hub mirror/reporting `https://georgiatoday.ge/tech-hub-to-open-in-kutaisi/`.
- Forbes Georgia FIZ/Bitfury context: `https://forbes.ge/what-factors-hinder-the-development-of-free-industrial-zones/`.
- Bitcoin.com / DCD historical Bitfury coverage: `https://news.bitcoin.com/bitfurys-georgian-technology-park-create-new-jobs/`; `https://www.datacenterdynamics.com/en/news/bitcoin-miners-build-worlds-largest-liquid-cooling-set-up/`.
- ENOG/NewTelco presentation: `https://www.enog.org/wp-content/uploads/presentations/enog-16/16-For-ENOG-16.pdf`.
- Internet Society IXP tracker for Georgia: `https://pulse.internetsociety.org/en/ixp-tracker/country/GE/`.
- IEA Georgia Energy Profile: `https://www.iea.org/reports/georgia-energy-profile`.

### 2.3 Grade C / Catalogs and Directories

- DataCenterMap Georgia and markets: `https://www.datacentermap.com/georgia/`; Tbilisi `https://www.datacentermap.com/georgia/tbilisi/`; Cloud9 Tbilisi `https://www.datacentermap.com/georgia/tbilisi/cloud9-dc/`; Batumi `https://www.datacentermap.com/georgia/batumi/`; Cloud9 Batumi `https://www.datacentermap.com/georgia/batumi/cloud9-batimu-arena/ecosystem/`.
- Cloudscene Georgia/Tbilisi market: `https://cloudscene.com/market/data-centers-in-georgia/georgia-regional-981`.
- DC Hub examples: Cloud9 `https://dchub.cloud/facilities/cloud9-ltd-cloud9-dinamo-arena-dee4f858`; NewTelco `https://dchub.cloud/facilities/newtelco-georgia-newtelco-tbilisi-9c4b71bb`.
- Inflect NewTelco: `https://inflect.com/building/ana-politkovskaia-street-tbilisi/newtelco/datacenter/newtelco-georgia`.
- Datacenters.com Tbilisi market and provider pages: `https://www.datacenters.com/locations/georgia/tbilisi`; `https://www.datacenters.com/cloud9-georgia-tbilisi`; `https://www.datacenters.com/newtelco-georgia`; `https://www.datacenters.com/worldbus-georgia`.
- PeeringDB Caucasus Online facility: `https://www.peeringdb.com/fac/8513`.
- Baxtel Georgia/Bitfury: `https://baxtel.com/data-center/republic-of-georgia`.
- colo.exchange Tbilisi/NewTelco pages: `https://colo.exchange/locations/ge/tbilisi/tbilisi`; `https://colo.exchange/data-centers/newtelco-georgia-newtelco-tbilisi`.

---

## 3. Player and Facility Lead Inventory

| Lead | Division / municipality | Status from industry sources | Grade | Official follow-up |
|---|---|---|---|---|
| Cloud9 Dinamo Arena | Tbilisi | First-party operator markets a carrier-neutral Tbilisi data center at 2 Akaki Tsereteli Ave, Dinamo Stadium Gate 5, with colocation/racks, 3 independent power substations, backup 630 kVA generator, N+N power feed and connectivity services. | A for existence/service; C for catalog capacity | Tbilisi permit/cadastre, NAPR Cloud9 LLC, Telasi/utility evidence, MEPA/NEA generator/fuel if available. |
| Silknet / Silk Cloud Tier III DC | Tbilisi | First-party Silknet plan plus BM.ge groundbreaking. Reported 2 MW, under construction, expected operational in 2027, operated by Silk Cloud. | A for first-party plan; B for groundbreaking/capacity | Tbilisi construction permit, NAPR Silk Cloud JSC, address/cadastre, grid/DSO connection, Uptime certification once published. |
| Caucasus Online data center / colocation | Tbilisi | First-party CO page markets data-center colocation services; catalogs/PeeringDB list facility. | A for service; C for catalogs/specs | Exact site/address, NAPR ID, Tbilisi permit/cadastre, ComCom authorization, PeeringDB de-dupe. |
| NewTelco Georgia / NewTelco Tbilisi | Tbilisi | NewTelco group page and ENOG deck support a neutral data center in Tbilisi; catalogs place it on Ana Politkovskaia Street and report 3 MW. | A/B for existence; C for MW/address detail unless operator confirms | Georgian legal entity, operator page, Tbilisi permit/cadastre, utility evidence. |
| G Data Data-Center #1 | Tbilisi | Uptime Institute lists Tier III Certification of Design Documents for G Data LLC's Tbilisi project. | A for certification | Find operator/project page, NAPR, Tbilisi permit, constructed-facility/operation evidence. |
| JSC Bank of Georgia Main DC (Lilo) | Tbilisi / Lilo | Uptime lists Tier III Design and Constructed Facility certification. | A for certification | Private bank DC. Keep as non-commercial context unless public service scope requires private enterprise DCs. |
| JSC TBC Bank TBL-01 | Tbilisi | Uptime lists Tier III Constructed Facility certification. | A for certification | Private bank DC. Context/non-commercial. |
| Bitfury Gldani / Tbilisi FIZ crypto DC | Tbilisi / Gldani | Historical 40-60 MW crypto/HPC DC in/near Tbilisi Free Zone; Bitfury sale PDF and press confirm historical build/sale. | A/B historical; C for current catalog-only status | Current owner/operator, TFZ resident/land record, NAPR/cadastre, GSE/Telasi connection, current operations. |
| WORLDBUS Data Center | Tbilisi | Catalogs list a WORLDBUS Tbilisi DC, including Oqromchedelebi St leads. | C | Operator page, NAPR, Tbilisi permit/cadastre. Do not count from catalogs alone. |
| Proservice Data Center | Tbilisi | Architecture/project and catalog leads identify a Tbilisi project; public operator/source trail weak. | B/C | Confirm Georgian operator page or permit/cadastre; filter out US/Hawaii ProService noise. |
| Bitfury Gori DC | Shida Kartli / Gori | Historical trade reports cite ~20 MW Gori bitcoin-mining DC. | B/C historical | Gori municipality, NAPR/cadastre, Energo-Pro/GSE evidence, current status. |
| Kutaisi Technology Hub data center | Imereti / Kutaisi | Official Economy Ministry says former Parliament building Technology Hub will include a powerful data center for Georgian AI; renovation works ongoing in later update. | A | Public procurement/rehabilitation records, Kutaisi permits, GITA/operator, power/cooling details. |
| Cloud9 Batumi Arena | Adjara / Batumi | DataCenterMap lists under-construction Cloud9 Batumi Arena at Shartava Ave 13. | C | Cloud9 confirmation, Batumi permit/cadastre, utility connection. Do not count yet. |
| GDKHOST.NET small data center | Samegrelo-Zemo Svaneti / likely Zugdidi to verify | First-party site claims own small data center in Georgia and markets VPS/colocation/hosting. Exact municipality not published on the checked pages. | A for service claim; B/C for Zugdidi assignment | Contact/legal entity/AS203136/Ordunet, NAPR, Zugdidi municipal permit/cadastre. |
| Innovative Technology LLC datacenter services | K'akheti / Telavi-Ruispiri to verify | Prior batch found a first-party service URL; needs live re-check and official tie. | A/B if live; otherwise C | Verify page, NAPR, Telavi municipal permit/cadastre, exact facility/service scope. |
| Abkhazia mining/technopark claims | Abkhazia | De-facto/occupation-zone crypto-mining reports; not Georgian official coverage. | B context | Exclude from Georgian official enumeration; separate de-facto note only. |

---

## 4. Division-by-Division Industry Workflow

| Division | Industry sweep focus | Current lead posture |
|---|---|---|
| Abkhazia | DCD/JAMnews/de-facto crypto-mining terms only if scope explicitly wants occupied-territory context | Excluded from Georgian count; no reliable Georgian official public data. |
| Adjara | `Batumi data center`, `ბათუმი მონაცემთა ცენტრი`, Cloud9 Batumi Arena, Batumi port/hosting/MSPs | One catalog-only under-construction Cloud9 Batumi lead. Needs first-party/permit confirmation. |
| Guria | Ozurgeti/Lanchkhuti hosting searches, `გურია მონაცემთა ცენტრი`, `ოზურგეთი სერვერული` | No confirmed lead. |
| Imereti | Kutaisi Technology Hub, Kutaisi FIZ, Kutaisi airport/industrial zone, `ქუთაისი მონაცემთა ცენტრი` | Official Kutaisi tech-hub data-center component is a planned public project; no commercial colo lead confirmed. |
| K'akheti | Innovative Technology/Ruispiri/Telavi, local hosting/MSPs, `თელავი მონაცემთა ცენტრი`, `კახეთი კოლოკაცია` | One service-provider lead needing live and official verification. |
| Kvemo Kartli | Rustavi industrial zone, Gardabani power area, `რუსთავი მონაცემთა ცენტრი`, `გარდაბანი data center` | No confirmed lead; industrial/power watchlist. |
| Mtskheta-Mtianeti | Mtskheta/Dusheti industrial and telecom searches, Gudauri tech/event false positives | No confirmed lead. |
| Rach'a-Lechkhumi-Kvemo Svaneti | Ambrolauri/Oni hosting searches and de-facto-overlap caution | No confirmed lead. |
| Samtskhe-Javakheti | Borjomi/Akhaltsikhe hosting searches, `ახალციხე data center` | No confirmed lead. |
| Shida Kartli | Bitfury Gori, Gori/Kaspi industrial searches, `გორი მონაცემთა ცენტრი` | Historical Bitfury Gori lead only; current status unresolved. |
| Samegrelo-Zemo Svaneti | GDKHOST/Ordunet/Zugdidi, Poti FIZ, port-area hosting, `ზუგდიდი მონაცემთა ცენტრი`, `ფოთი მონაცემთა ცენტრი` | GDKHOST first-party small-DC claim; municipality/site still needs verification. |
| Tbilisi | Cloud9, Silk Cloud, Caucasus Online, NewTelco, G Data, Bank of Georgia/TBC private DCs, Bitfury/Gldani, WORLDBUS, Proservice, Magti/Silknet hosting/PoPs | Highest yield. Most records require de-duplication and official permit/cadastre checks. |

Low-yield sweep:

```
"{division}" "მონაცემთა ცენტრი"
"{division}" "data center" Georgia -Atlanta -USA
"{division}" "კოლოკაცია"
"{main_town}" "მონაცემთა ცენტრი"
"{main_town}" "data center" colocation Georgia
"{main_town}" hosting "Georgia"
site:bm.ge "{division}" "მონაცემთა ცენტრი"
site:commersant.ge "{division}" "მონაცემთა ცენტრი"
site:datacentermap.com/georgia "{main_town}"
```

---

## 5. Watchlist and False-Positive Rules

Re-check quarterly:

- Silknet/Silk Cloud: permit, site address, Uptime certification, commissioning, public operator page, capacity changes beyond 2 MW.
- Cloud9: Tbilisi operator page changes, any first-party Batumi confirmation, catalog capacity vs official/operator specs.
- Caucasus Online and Silknet consolidation: whether Caucasus Online DC remains separate or is merged into Silk Cloud offering.
- NewTelco: current Georgian operator page, legal entity, exact address and capacity.
- G Data/Uptime: movement from Design certification to Constructed Facility/operating launch.
- Bitfury/Gldani and Gori: current owner/operator/status; crypto-to-HPC/AI pivot; TFZ records.
- Kutaisi Technology Hub: procurement, rehabilitation milestones, operator, data-center size/capacity.
- GDKHOST and Innovative Technology: exact facility location and municipal evidence.
- FIZs: new IT/HPC/crypto tenants in Tbilisi, Kutaisi and Poti.
- Official hyperscale location lists only; ignore US-state Georgia pages.

Common false positives:

- US state of Georgia results, especially Atlanta, Douglas County, Effingham County and Georgia Power.
- `მონაცემთა ცენტრი` meaning an information/statistical/customer-service center.
- Ordinary enterprise server rooms in banks, ministries, hotels or telco offices.
- Internet exchanges, CDN caches, carrier PoPs or submarine-cable landing/network nodes without facility services.
- Catalog duplicates of one Tbilisi facility under different provider names.
- Registered office addresses for hosting companies that resell remote infrastructure.
- Crypto-mining farms counted as commercial colocation without current facility/service proof.
- Uptime Design certification treated as operational status.
- FIZ resident status treated as data-center operation.

Recommended fields:

```
name
country
region
municipality
address
operator_or_developer
legal_entity
status
capacity_mw
capacity_source_grade
white_space_m2
racks
operator_evidence_url
certification_url
trade_press_url
catalog_seed_url
official_followup_url
evidence_date
evidence_grade
candidate_or_countable
notes
```
