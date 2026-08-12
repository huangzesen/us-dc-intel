# TR Explorer Industry - Turkiye Datacenter Enumeration via Trade Press, Vendors, and Province Query Patterns

Date: 2026-08-11. Scope: industry/trade-press and vendor-led methodology for enumerating datacenter projects in Turkiye at province level. Reliability grades: **A** = official/primary source (operator page, BTK/e-Devlet/e-CED/municipal filing, investor/regulator announcement); **B** = strong secondary/trade press (DCD, Anadolu Agency, BThaber, Turk-internet, Cloud7, TechInside, operator quoted in reputable press); **C** = directories/aggregators/blogs/social posts requiring confirmation.

---

## 0. Market structure to frame searches

- Turkiye is not evenly distributed. Search effort should start with **Istanbul**, **Ankara**, **Izmir**, **Kocaeli/Gebze**, and **Tekirdag/Corlu-Kapakli**. Current industry coverage repeatedly says most facilities are in Istanbul, with Ankara and Izmir as the main secondary hubs.
- The market is a mix of telcos, carrier-neutral/colo providers, bank/enterprise campuses, and new Gulf-backed/hyperscale-oriented projects. Major names to seed first: **Turkcell/TDC Veri Hizmetleri**, **Turk Telekom**, **Vodafone Turkiye**, **Equinix**, **NGN / Star of Bosphorus**, **Radore**, **Teknotel / Telehouse Istanbul**, **Sparkle**, **Comnet**, **TurkNet**, **Netdirekt**, **PlusLayer**, **VeriTeknik**, **KocSistem**, **IsNet / Is Bankasi Atlas**, **ENKA Data Solutions**, **PenDC**, **Khazna**, **Edgnex by DAMAC**, **Trendyol x Castle Investments**, **TURKSAT**.
- Turkey-specific terms matter. Always search both English and Turkish: `data center`, `datacenter`, `colocation`, `cloud region`, plus `veri merkezi`, `veri merkezleri`, `sunucu barindirma`, `sunucu merkezi`, `bulut`, `ortak yerlesim`, `beyaz alan`, `kabinet`, `kabin`, `rack`, `MW`, `MVA`, `Uptime Tier III`, `TSE 50600`, `LEED Gold`.
- Do not rely on directories alone. Baxtel, DataCenterMap, DataCenters.com, Data Center Catalog, PeeringDB, DCHub, and local-map listings are useful **C-grade lead sources**; promote only after vendor/press/official corroboration.

---

## 1. Trade press and industry discovery sources

### 1.1 International and English-language press

| Source | URL / query | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) Turkey tag | `https://www.datacenterdynamics.com/en/news/?tag=turkey` | Best English feed for Equinix IL4, Khazna Ankara, Edgnex/Vodafone, Google Cloud/Turkcell, Alibaba/Trendyol rumors, sector context. | B |
| Anadolu Agency / AA | `site:aa.com.tr veri merkezi Türkiye`, `site:aa.com.tr data center Turkey` | Often carries minister/operator quotes, inauguration dates, province counts, public projects. Treat as strong press; when quoting a minister or official ceremony, evidence can be A-/B+. | B+ |
| Daily Sabah / TRT Haber | `site:dailysabah.com data center Ankara Turkey`, `site:trthaber.com veri merkezi Ankara` | English/Turkish republication of AA and ministry announcements. Useful for Ankara/TURKSAT/Trendyol/Castle. | B |
| Invest in Turkiye | `site:invest.gov.tr data center Turkiye Vodafone DAMAC` | Official investment agency republishes strategic foreign-investment projects; good for JV/capex validation. | A- |
| Market-research press releases | GlobeNewswire, BusinessWire, Yahoo Finance, Arizton, Mordor, ResearchAndMarkets | Good for operator universe and hotspot ranking, weak for facility facts unless a project is named. | C/B |

### 1.2 Turkish ICT/trade press

| Source | URL / query | Use | Grade |
|---|---|---|---|
| BThaber | `https://bthaber.com`, query `site:bthaber.com veri merkezi Turkcell Equinix NGN` | Local enterprise ICT publication; useful for market commentary, events, operator interviews. | B |
| Turk-internet | `https://turk-internet.com/kategori/telekom/operatorler/hosting/`, query `site:turk-internet.com veri merkezi` | Turkish telecom/hosting press; useful for Equinix, NGN, hosting/cloud vendors, regulatory commentary. | B |
| Cloud7 | `https://cloud7.news`, query `site:cloud7.news "veri merkezi" Türkiye` and English `site:cloud7.news Turkey data center` | Hosting/cloud trade press; strong for local hosting vendors, cloud launches, outages, sector events. | B |
| TechInside | `https://www.techinside.com`, query `site:techinside.com Turkcell veri merkezi`, `site:techinside.com veri merkezi açıldı` | Good for Turkcell openings and funding. Older articles often include white-space sqm and planned phases. | B |
| BT Gunlugu / CIO / Digital Age / Webrazzi | queries with `veri merkezi`, `bulut`, vendor name | Secondary corroboration for Turkish enterprise-IT launches, investment rounds, cloud partnerships. | B-/C+ |
| DC Network Turkiye / DCD>Turkey / Data Center Eurasia events | `dcnetworkturkiye.com`, `datacentereurasia.com`, DCD event pages | Participant lists reveal active vendors and project managers. Use as leads, not facility proof. | C/B |

### 1.3 Directory and ecosystem lead sources

- **Baxtel**: `https://baxtel.com/data-center/turkey` - good capacity hints and operator list, but capacity must be confirmed.
- **DataCenterMap**: `https://www.datacentermap.com/turkey/` - often catches small regional facilities (Rize, Samsun, etc.).
- **DataCenters.com**: `https://www.datacenters.com/locations/turkiye` - broader provider list; watch duplicates and reseller listings.
- **Data Center Catalog**: `https://datacentercatalog.com/turkey` - useful for municipal, bank, and small colo facilities.
- **PeeringDB**: query facilities by country TR and city; good for network-active facilities such as regional ISPs. Grade B for network existence, C for datacenter capacity/status.

---

## 2. Turkish query patterns

### 2.1 Discovery queries

Use `{province}` as manifest name and `{il}` as Turkish spelling with diacritics where useful (e.g. Istanbul/Istanbul, Izmir/Izmir, Kocaeli/Gebze, Tekirdag/Tekirdag, Sanliurfa/Sanliurfa; also try Turkish: `İstanbul`, `İzmir`, `Tekirdağ`, `Şanlıurfa`).

```text
"{il}" +"veri merkezi" +(açıldı OR acildi OR temel OR yatırım OR yatirim OR inşaat OR insaat OR kapasite OR "beyaz alan")
"{il}" +"data center" +(opened OR launch OR construction OR MW OR capacity OR investment)
"{il}" +"veri merkezi" +(MW OR MVA OR kabinet OR kabin OR rack OR "beyaz alan" OR "kapalı alan")
"{il}" +"veri merkezi" +(Tier OR "Uptime" OR "TSE 50600" OR "LEED Gold")
"{il}" +"bulut" +"veri merkezi" +(Turkcell OR "Türk Telekom" OR Vodafone OR Equinix OR NGN)
site:aa.com.tr "{il}" "veri merkezi"
site:datacenterdynamics.com "{il}" "data center" Turkey
site:turk-internet.com "{il}" "veri merkezi"
site:cloud7.news "{il}" "veri merkezi"
site:techinside.com "{il}" "veri merkezi"
```

### 2.2 Vendor-specific queries

```text
site:turkcell.com.tr "veri merkezi" (Gebze OR Ankara OR İzmir OR Tekirdağ OR Çorlu OR Edirne)
site:medya.turkcell.com.tr "veri merkezi" (açıldı OR yatırım OR finansman OR Google)
site:turktelekom.com.tr "veri merkezlerimiz" OR "Esenyurt Veri Merkezi" OR "Ümitköy"
site:vodafone.com.tr "data center" OR "veri merkezi" (Adana OR Ankara OR İzmir OR İstanbul)
site:equinix.com "Istanbul data centers" OR "IL2" OR "IL4"
site:equinixdatacenters.com.tr "BTK" "AIH" "İSS"
site:ngn.com.tr "Star of Bosphorus" "16 MW"
site:radore.com "veri merkezi" "MetroCity"
site:teknotel.com "Telehouse İstanbul" "veri merkezi"
site:pluslayer.com "İzmir" "veri merkezi"
site:netdirekt.com.tr "veri merkezi" "İzmir"
site:comnet.com.tr "veri merkezi"
site:kocsistem.com.tr "veri merkezi" Ankara İstanbul
site:isbank.com.tr "Atlas Veri Merkezi" Tuzla
site:enkadatasolutions.com "Tuzla" "data center"
site:turksat.com.tr "Gölbaşı" "Veri Merkezi"
```

### 2.3 Regulatory/validation pivots after a press lead

These are not the primary angle of this explorer, but they are the best way to harden trade-press/vendor leads:

```text
site:btk.gov.tr "{operator legal name}" "İnternet Servis Sağlayıcılığı"
site:btk.gov.tr "{operator legal name}" "Altyapı İşletmeciliği"
site:internet.btk.gov.tr "{operator}" "Yer Sağlayıcılık Bildiriminde Bulunanlar"
site:eced.csb.gov.tr "{project name}" OR "{il}" "veri merkezi"
site:csb.gov.tr "{il}" "veri merkezi" "ÇED"
site:{municipality}.bel.tr "veri merkezi" "ruhsat"
site:{province}.gov.tr "veri merkezi" "yatırım" OR "OSB"
site:sanayi.gov.tr "{il}" "veri merkezi" "OSB"
```

Notes:
- **BTK** authorization is operator-level, not facility-level. Look for `İSS` (Internet Service Provider), `AİH/AIH` (Infrastructure Operation Service), and sometimes hosting notification under **Yer Sağlayıcılık Bildiriminde Bulunanlar** (`https://internet.btk.gov.tr/yer-saglayici-listesi`). BTK/hosting notification is **not** a datacenter license, but it confirms the legal operator.
- **e-CED / Ministry of Environment** (`https://eced.csb.gov.tr/`) may catch larger construction projects, generators, and energy infrastructure, but many datacenters appear only through municipal/OSB building permits and press.
- Municipal sites often use Turkish dotted letters and district names more than province names: `Ümraniye`, `Tuzla`, `Esenyurt`, `Başakşehir`, `Gebze`, `Temelli`, `Gölbaşı`, `Menderes`, `Çorlu`, `Kapaklı`, `Karaağaç OSB`.

---

## 3. Vendor/operator seed list by geography

### 3.1 Istanbul / Marmara core

| Operator/project | Search anchor | Notes | Grade seed |
|---|---|---|---|
| Equinix Istanbul campus IL2/IL4 | `https://www.equinix.com/data-centers/europe-colocation/turkiye-colocation/istanbul-data-centers`; DCD `Equinix launches data center in Istanbul` | Official page lists IL2 and IL4. Turkish legal page confirms BTK ISP/AIH authorizations. DCD/Turk-internet report IL4 AI/high-density expansion. | A |
| Turk Telekom Istanbul | `Turk Telekom Esenyurt Veri Merkezi`, `Gayrettepe Veri Merkezi` | Official page says Istanbul Esenyurt/Gayrettepe and Ankara Umitkoy, with 12,700 sqm white space across three facilities. | A |
| Turkcell Istanbul legacy facilities | `Dudullu Kartal Maltepe Yenibosna Davutpaşa Turkcell veri merkezi` | Older Turkcell/TechInside articles list legacy Istanbul white-space footprint; confirm each facility because some may be DR/network nodes. | B |
| NGN Star of Bosphorus | `https://www.ngn.com.tr/tr/star-of-bosphorus-veri-merkezi/` | Official page states operator-neutral commercial DC, Uptime Tier III design/facility certification, 16 MW. | A |
| Radore | `https://radore.com/tr/veri-merkezi` | Istanbul MetroCity/Levent retail colo/hosting; official page gives location and service claims. | A |
| Teknotel / Telehouse Istanbul | `https://www.teknotel.com/tr/data-center-altyapisi-satin-al/` | Official Teknotel page describes Telehouse Istanbul Tier 3+ data center. | A |
| Is Bankasi Atlas / IsNet | `Atlas Veri Merkezi Tuzla`, `IsNet veri merkezi` | Bank/enterprise Tier IV-grade campus in Tuzla; useful because enterprise campuses can be missed by colocation directories. | A |
| ENKA Data Solutions Tuzla | `enkadatasolutions.com Tuzla data center` | Emerging Istanbul/Tuzla AI-ready colo provider; validate with official ENKA pages/events and construction references. | B/A- |
| KocSistem Camlica, IBB Basaksehir, Mars Datacenter, PenDC, Comnet, TurkNet, Sparkle | combine vendor name + `veri merkezi` + district | Mostly smaller colo/network facilities; directories are useful but require operator page or PeeringDB corroboration. | C/B |

### 3.2 Ankara cluster

| Operator/project | Search anchor | Notes | Grade seed |
|---|---|---|---|
| Turkcell Ankara / Temelli | `Turkcell Ankara Veri Merkezi Temelli Anadolu OSB` | Official/AA opening coverage; large white-space figures appear in press. | A |
| Khazna Ankara | DCD `Khazna to build data center near Ankara Turkey`; Khazna press release | UAE/G42-backed project near Ankara; official Khazna release says facility designed for AI/cloud workloads. | A/B |
| Trendyol x Castle Investments Ankara Data Hub | `Trendyol Castle Investments Ankara Data Hub Temelli 48 MW` | AA/Daily Sabah reports USD 500m, 48 MW total, Q3 2026 first phase; verify with construction/OSB/municipal records. | B+ |
| TURKSAT Golbasi Veri Merkezi | `TÜRKSAT Gölbaşı Veri Merkezi 33 MVA` | State-linked project; ministry/TRT/AA coverage gives capacity-style MVA and ceremony. | A |
| Turk Telekom Ankara / Umitkoy plus planned Ronesans project | `Türk Telekom Ümitköy Veri Merkezi`, `Rönesans Türk Telekom Ankara veri merkezi` | Official page confirms Umitkoy. Ronesans announcement is early-stage partnership. | A/B |
| Vodafone Ankara | `Vodafone Ankara veri merkezi kapasite` | AA quotes confirm existing facility and expansion investment; capacity not usually public. | B+ |
| VeriTeknik, KocSistem Ankara, Global Iletisim OSTIM, KKB Anadolu | vendor + `Ankara veri merkezi` | Smaller/operator/enterprise facilities; use directories as leads and vendor/PeeringDB for validation. | C/B |

### 3.3 Izmir / Aegean

| Operator/project | Search anchor | Notes | Grade seed |
|---|---|---|---|
| Turkcell Izmir / Menderes | `Turkcell İzmir Veri Merkezi Menderes` | Official and TechInside/DCD coverage; 2018 launch, white-space/certification details. | A/B |
| Vodafone-Edgnex Izmir | `Vodafone DAMAC Edgnex İzmir data center 6 MW 12 MW` | Official Invest in Turkiye and DCD coverage for USD 100m JV; initial 6 MW expandable to 12 MW. | A |
| Netdirekt | `Netdirekt İzmir veri merkezi` | Regional hosting/colo operator; verify official page, PeeringDB, directories. | B/C |
| PlusLayer | `PlusLayer İzmir Veri Merkezi` | Official page markets Izmir DC; good A-grade existence, capacity usually absent. | A |
| Vodafone Izmir | `Vodafone İzmir veri merkezi` | Existing Vodafone footprint via AA/operator quotes. | B |

### 3.4 Kocaeli/Gebze, Tekirdag/Corlu, and other regional cities

| Province | Operator/project anchors | Notes |
|---|---|---|
| Kocaeli | `Turkcell Gebze Veri Merkezi`, `Gebze veri merkezi`, `Kocaeli veri merkezi` | Gebze is a primary Turkcell campus. Use municipality/OSB and Turkcell official press for confirmation. |
| Tekirdag | `Turkcell Avrupa Veri Merkezi Çorlu`, `Kapaklı Karaağaç OSB veri merkezi` | Turkcell Europe Data Center is in Tekirdag/Kapakli-Corlu area; strong official/AA evidence. |
| Adana | `Vodafone Adana veri merkezi` | AA confirms Vodafone facility; operator page may not disclose city-specific detail. |
| Kayseri, Konya, Samsun, Trabzon, Isparta, Antalya | `"{il}" "bir veri merkezi çalışıyor"`, AA 2026 country roundup, local vendor names | AA mentions operating facilities in several provinces but often not operator names. Treat as lead until facility identity is confirmed. |
| Rize, Sakarya, Gaziantep, Edirne | province + `veri merkezi`, PeeringDB/DataCenterMap/vendor | Small regional ISP/hosting facilities appear in directories. Confirm with legal entity, address, BTK/hosting notification, and customer/network evidence. |

---

## 4. Per-province enumeration method

### 4.1 Province tiering

1. **Tier 1 - exhaustive vendor + press + official sweep**: Istanbul, Ankara, Izmir, Kocaeli, Tekirdag. Run all query families in sections 2.1-2.3 and every major vendor in section 3.
2. **Tier 2 - named regional facility sweep**: Adana, Antalya, Bursa, Edirne, Eskisehir, Gaziantep, Isparta, Kayseri, Konya, Rize, Sakarya, Samsun, Trabzon. Run province queries plus directories/PeeringDB and local university/municipal terms.
3. **Tier 3 - negative-control sweep**: remaining provinces. Search for commercial facilities, public-sector/university data rooms, OSB announcements, and local ISP hosting. If only institutional server rooms appear, record only if they are publicly described as `veri merkezi` and have a named operator/owner.

### 4.2 Copy-paste per-province workflow

For each manifest division:

```text
1. Convert ASCII division to Turkish search form:
   Istanbul->İstanbul, Izmir->İzmir, Tekirdag->Tekirdağ, Kocaeli also try Gebze, Ankara also try Temelli/Gölbaşı/Ümitköy, Sanliurfa->Şanlıurfa, Canakkale->Çanakkale, Eskisehir->Eskişehir, etc.

2. Run broad discovery:
   "{il}" "veri merkezi"
   "{il}" "data center" Turkey
   "{il}" "sunucu barındırma" "veri merkezi"
   "{il}" "bulut" "veri merkezi"

3. Run project/status terms:
   "{il}" "veri merkezi" "açıldı"
   "{il}" "veri merkezi" "temeli atıldı"
   "{il}" "veri merkezi" "yatırım"
   "{il}" "veri merkezi" "inşaat"
   "{il}" "veri merkezi" "MW" OR "MVA"

4. Run source-scoped press:
   site:aa.com.tr "{il}" "veri merkezi"
   site:datacenterdynamics.com "{il}" "data center"
   site:turk-internet.com "{il}" "veri merkezi"
   site:bthaber.com "{il}" "veri merkezi"
   site:cloud7.news "{il}" "veri merkezi"
   site:techinside.com "{il}" "veri merkezi"

5. Run directory/network checks:
   DataCenterMap country/city page, Baxtel Turkey, DataCenters.com Turkiye, Data Center Catalog Turkey, PeeringDB facilities country=TR city={city}.

6. Validate:
   operator official page, BTK operator/hosting notification, e-CED/CSB if construction-scale, municipality/OSB pages, and cross-check with at least one independent source.
```

### 4.3 Province aliases and district hints

| Manifest division | Also query | Why |
|---|---|---|
| Istanbul | `İstanbul`, `Ümraniye`, `Dudullu OSB`, `Tuzla`, `Esenyurt`, `Gayrettepe`, `Levent`, `Başakşehir`, `Çamlıca`, `Yenibosna`, `Davutpaşa`, `Kartal`, `Maltepe` | Most commercial/enterprise DCs are district-branded rather than province-branded. |
| Ankara | `Temelli`, `Anadolu OSB`, `Gölbaşı`, `Ümitköy`, `OSTİM`, `Söğütözü` | Turkcell, TURKSAT, Turk Telekom, Trendyol/Castle, and smaller Ankara facilities use district/OSB names. |
| Izmir | `İzmir`, `Menderes`, `Ege`, `Aegean`, `Netdirekt`, `PlusLayer` | Turkcell and several regional colo/hosting operators. |
| Kocaeli | `Gebze`, `Kocaeli`, `Gebze OSB` | Turkcell Gebze and industrial-zone projects. |
| Tekirdag | `Tekirdağ`, `Çorlu`, `Kapaklı`, `Karaağaç OSB`, `Avrupa Veri Merkezi` | Turkcell Europe Data Center. |
| Bursa | `Bursa veri merkezi`, `Uludağ`, `OSB veri merkezi` | Possible enterprise/public-sector facilities; not a primary colo hub. |
| Adana | `Vodafone Adana Veri Merkezi`, `Adana data center` | Vodafone city footprint reported by AA. |
| Antalya | `Antalya veri merkezi`, `turizm veri merkezi`, `belediye veri merkezi` | Regional facility lead; verify identity carefully. |
| Kayseri | `Kayseri veri merkezi`, `Erciyes Teknopark veri merkezi` | AA regional count lead; likely local/enterprise scale. |
| Konya | `Konya veri merkezi`, `Selçuk`, `belediye veri merkezi` | AA regional count lead; likely local/enterprise scale. |
| Samsun | `Samsun veri merkezi`, `Earth Veri Merkezi` | Known regional directory lead. |
| Trabzon | `Trabzon veri merkezi` | AA regional count lead; verify operator. |
| Isparta | `Isparta veri merkezi`, `Süleyman Demirel Üniversitesi veri merkezi` | AA regional count lead plus institutional possibility. |
| Rize | `Rize veri merkezi`, `FiberDC Rize` | Known small regional hosting lead. |
| Gaziantep | `Gaziantep veri merkezi`, `Veganet`, `Gaziantep Üniversitesi veri merkezi` | Regional ISP and university infrastructure. |
| Eskisehir | `Eskişehir veri merkezi`, `Anadolu Veri Merkezi`, `ESKİ veri merkezi` | University/municipality signals. |
| Edirne | `Edirne veri merkezi`, `Turkcell Edirne` | Directory/local-map lead; confirm with operator. |

For every other province, run the generic templates plus local university (`üniversitesi veri merkezi`), municipality (`belediye veri merkezi`), provincial governorate (`valiliği veri merkezi`), technopark (`teknopark veri merkezi`), and organized industrial zone (`OSB veri merkezi`) variants.

---

## 5. Evidence grading and pitfalls

### 5.1 Evidence hierarchy

1. **A** - operator official facility page or press room; BTK/hosting notification for legal operator existence; Invest.gov.tr/ministry/municipality/OSB/e-CED record; audited corporate/investor filing.
2. **B** - DCD, AA, BThaber, Turk-internet, Cloud7, TechInside, TRT/Daily Sabah carrying official quotes, trade-event materials with named project and operator.
3. **C** - Baxtel/DataCenterMap/DataCenters.com/Data Center Catalog/DCHub, PeeringDB-only entries, blogs, LinkedIn/social posts, Google Maps, reseller pages.

### 5.2 Status and capacity rules

- Treat `açıldı`, `hizmete açıldı`, `faaliyete geçti`, `devreye alındı` as operational if source is operator/official/strong press.
- Treat `temeli atıldı`, `inşaat başladı`, `yapımı sürüyor` as construction. `anlaşma imzaladı`, `yatırım planlıyor`, `kuracak` is announced/planned unless there is a construction permit or groundbreaking.
- Capacity terms differ: `MW` usually IT load only in hyperscale/trade-press contexts; `MVA` or `kurulu güç` is electrical installed capacity and should not be blindly converted to IT MW. `beyaz alan` is white space sqm, not total building area.
- Turkish articles often quote total investment and final-phase design capacity. Record whether capacity is initial phase (`ilk faz`, `1. faz`) or ultimate (`tam kapasite`, `nihai kapasite`).
- Do not double-count campuses under aliases: e.g. Equinix Istanbul IL2/IL4 campus vs former Zenium/Istanbul One; Turkcell Ankara vs Temelli/Anadolu OSB; Turkcell Europe Data Center vs Tekirdag/Corlu/Kapakli/Karaagac OSB.
- Many public-sector/university `veri merkezi` pages describe small server rooms. Include only if the task wants all datacenter-like facilities; otherwise separate commercial/colo/hyperscale from institutional IT rooms in notes.

---

## 6. Recommended discovery order

1. Seed Tier 1 provinces with official vendor pages and DCD/AA/TechInside coverage.
2. Sweep DCD Turkey tag, AA `veri merkezi`, and Turkish ICT press for 2024-2026 announcements: Equinix IL4, Khazna Ankara, Edgnex/Vodafone Izmir, Turkcell-Google, Trendyol/Castle Ankara, TURKSAT Golbasi, Turk Telekom/Ronesans.
3. Run each major vendor query across all known facility cities; capture legal entity names and local aliases.
4. Use directories/PeeringDB to catch regional/small facilities, then validate with official pages or BTK/hosting notification.
5. For every province with no lead, run the generic Turkish query templates plus university/municipality/OSB variants before marking `no_projects: true`.
6. Assign evidence grade per data point, not per record: a facility can have A-grade existence but C-grade capacity if MW came only from a directory.
