# TR Explorer Official - Turkiye Datacenter Enumeration via Planning, Energy, Cloud, Colo, and BTK Sources

Date: 2026-08-12. Country: **TR Turkiye**. Division model: **81 provinces**. Angle: **official / regulatory / cloud pipeline** for finding operational, under-construction, and planned datacenter projects.

Reliability grades:
- **A** = official / primary / legally accountable source: ministry portal, municipality planning file, e-CED record, TEIAS / TEDAS / utility record, EPDK decision, BTK registry, official cloud infrastructure page, official operator page, Borsa Istanbul / SEC filing, Uptime / TSE certification record.
- **B** = strong secondary source: Anadolu Agency, DCD, Data Centre Dynamics, Invest in Turkiye official investment-news page, reputable construction / engineering firm page, PeeringDB where facility identity is corroborated.
- **C** = weak lead: directories, maps, blogs, market reports, local news without permit / operator / registry confirmation.

---

## 0. Turkiye-specific structural facts

- Turkiye has **no single public national datacenter permit register**. Enumeration is a **province + municipality + industrial-zone** exercise, with national e-government layers used as indexes.
- Datacenters usually surface as **veri merkezi**, **data center**, **bulut bolgesi**, **sistem odasi**, **barindirma**, **sunucu merkezi**, **telekom / bilisim tesisi**, **teknoloji ve operasyon merkezi**, or **OSB technology infrastructure** rather than a separate datacenter license class.
- The highest-yield provinces are **Istanbul, Ankara, Izmir, Kocaeli, Tekirdag, Adana, Antalya, Kayseri, Konya, Samsun, Trabzon, Rize, Gaziantep, Eskisehir, Erzurum, and Mersin**. Most hyperscale / carrier-neutral evidence is in Istanbul-Ankara-Izmir-Kocaeli-Tekirdag.
- Power is a gating signal. Use **TEIAS** transmission-capacity / substation documents, **TEDAS** distribution-asset acceptance / standards, regional distribution companies, EPDK decisions, and operator sustainability / solar statements to validate MW-scale projects.
- **BTK Yer Saglayici** records are an operator / hosting-provider census, not a facility census. They are still useful for finding legal entities, addresses, phone numbers, and local hosting operators to pivot into facility searches.
- Cloud-region pages are **A-grade for cloud-region existence only**. They rarely prove exact physical address. Use them to seed Istanbul / Ankara / Izmir / Kocaeli / Tekirdag searches, then confirm with operator, permit, grid, or construction evidence.

Key Turkish search vocabulary:
```
veri merkezi
data center
datacenter
bulut bolgesi
hiper olcekli bulut
barindirma merkezi
sunucu merkezi
sistem odasi
bilgi islem merkezi
teknoloji ve operasyon merkezi
kesintisiz guc kaynagi
jenerator
trafo merkezi
elektrik kapasitesi
baglanti gorusu
imar ruhsati
yapi ruhsati
iskan / yapi kullanma izin belgesi
CED gerekli degildir
CED olumlu
OSB veri merkezi
```

Use ASCII forms for search (`Turkiye`, `Istanbul`, `Izmir`, `Kocaeli`, `Tekirdag`) and Turkish forms (`Turkiye`, `Istanbul`, `Izmir`, `Kocaeli`, `Tekirdag`) because Turkish sites vary in indexing.

---

## 1. Grade A official portals and how to use them

### 1.1 National e-government / planning backbone

- **e-Devlet Kapisi**: https://www.turkiye.gov.tr/. Government service gateway. Use for service discovery, not as an open permit scrape because many building-permit services require authentication.
- **e-Plan Otomasyon Sistemleri / Ministry GIS**: https://cbs.csb.gov.tr/. The Ministry of Environment, Urbanization and Climate Change describes e-Plan as the national platform where spatial-plan processes and plan data can be managed, viewed, queried, and objected to. Use it to inspect zoning / plan context around known large projects and to find plan amendments (`imar plani`, `nazim imar plani`, `uygulama imar plani`).
- **Municipal planning portals**: each metropolitan municipality (`buyuksehir belediyesi`), district municipality (`ilce belediyesi`), and organized industrial zone (`OSB`) may publish zoning-plan changes, building-permit notices, tenders, council decisions, or project pages. These are often more useful than national search.
- **Turkish Trade Registry Gazette**: https://www.ticaretsicil.gov.tr/. Use legal-entity names from BTK/operator/news to identify SPVs, address changes, capital increases, and purpose clauses mentioning `veri merkezi`, `bulut`, `barindirma`, or `telekomunikasyon`.
- **Central Registry / MERSIS via e-Devlet**: use when accessible for entity validation; public search may be constrained.

Planning query templates:
```
site:{municipality-domain} "veri merkezi" "imar"
site:{municipality-domain} "veri merkezi" "yapi ruhsati"
site:{municipality-domain} "data center" "ruhsat"
site:{municipality-domain} "trafo merkezi" "veri merkezi"
site:{municipality-domain} "jenerator" "veri merkezi"
site:{municipality-domain} "meclis karari" "veri merkezi"
site:{municipality-domain} "imar plani degisikligi" "veri merkezi"
site:{osb-domain} "veri merkezi"
site:{osb-domain} "data center"
"{province}" "{district}" "veri merkezi" "imar ruhsati"
"{project}" "yapi ruhsati" OR "yapi kullanma izin"
"{project}" "iskan" "veri merkezi"
```

Extract from planning / zoning documents: permit number, parcel / ada-parsel, district, neighborhood, applicant / SPV, land area, closed area (`kapali alan`), white space (`beyaz alan`), number of system halls, transformer / generator descriptions, parking / roof solar, phase schedule, and whether the record is only a plan amendment or a construction permit.

### 1.2 Environmental approvals - e-CED

- **e-CED portal**: https://eced.csb.gov.tr/.
- **e-CED public announcements**: https://eced-duyuru.csb.gov.tr/eced-prod/duyurular.xhtml.
- **CED Directorate online services**: https://ced.csb.gov.tr/online-islemler-111530.
- **CED process description**: https://ced.csb.gov.tr/ced-uygulamalari-82207.

Datacenters are not always a named CED category, so recall is low. Still search because large buildings, generator farms, substations, fuel storage, cooling systems, and solar / wind tie-ins may trigger CED or exemption notices.

CED query templates:
```
site:eced-duyuru.csb.gov.tr "veri merkezi"
site:eced.csb.gov.tr "veri merkezi"
site:ced.csb.gov.tr "veri merkezi"
site:csb.gov.tr "veri merkezi" "CED"
site:csb.gov.tr "data center" "CED"
"{operator}" "CED gerekli degildir" "veri merkezi"
"{project}" "proje tanitim dosyasi" "veri merkezi"
"{province}" "veri merkezi" "CED olumlu"
"{province}" "jenerator" "CED" "veri merkezi"
```

Grade **A** when the e-CED announcement, CED decision, project description file, or ministry page names the project / operator. Grade **B** if the environmental record only names an associated energy project near a known datacenter.

### 1.3 Public tenders and government projects

- **EKAP Public Procurement Authority**: https://ekap.kik.gov.tr/. Search for public-sector `veri merkezi`, `sistem odasi`, `sunucu odasi`, `felaket kurtarma merkezi`, UPS, generator, HVAC, and network-room construction tenders.
- **Local municipality tender portals**: high-yield for public / university / municipal datacenters and renovations. Example patterns include municipal `ihale` pages for server-room construction, cooling, UPS, BMS, fire suppression, and electrical works.
- **Investment Office of the Presidency**: https://www.invest.gov.tr/en/news/. Official investment news is **A-/B+**: it confirms announcements and investment intent, but still requires planning / power follow-up for construction status.

Tender query templates:
```
site:ekap.kik.gov.tr "veri merkezi"
site:ekap.kik.gov.tr "sistem odasi"
site:ekap.kik.gov.tr "sunucu odasi"
site:ekap.kik.gov.tr "felaket kurtarma merkezi"
site:{municipality-domain} "ihale" "veri merkezi"
site:{university-domain} "veri merkezi" "ihale"
site:{osb-domain} "veri merkezi" "ihale"
```

---

## 2. Energy / grid pipeline

### 2.1 TEIAS, TEDAS, EPDK, and distribution utilities

- **TEIAS official site**: https://www.teias.gov.tr/en-US and Turkish announcements https://www.teias.gov.tr/. TEIAS publishes transmission-system and capacity announcements, regional generation-connection capacity reports, substation / GIS environmental-social plans, contract awards, and connection-related reports. Use for transmission substations and grid capacity around MW-scale projects.
- **TEIAS capacity announcements**: examples include `Kapasite Duyurusu`, `Lisanssiz Uretim Duyurusu`, `Iletim Seviyesi Kalan Kapasite Tablosu`, and `Transformator Merkezi Bazli Tahsis Edilen Lisanssiz Uretim Kapasite Tablosu`.
- **TEDAS**: https://www.tedas.gov.tr/. Use for distribution-asset acceptance, technical specifications, and regional distribution links. Datacenter-specific hits are rare but electrical acceptance / distribution substation clues can appear.
- **EPDK**: https://www.epdk.gov.tr/. Search board decisions and license / connection context for energy projects tied to datacenters, especially captive solar / wind / storage and organized-industrial-zone supply constraints.
- **Regional distribution companies**: use province-specific DSOs for connection capacity, outages, investment plans, tender awards, and customer-connection clues. Examples: BEDAS / AYEDAS (Istanbul), SEDAS (Kocaeli/Sakarya/Duzce/Bolu), TREDAS (Tekirdag/Edirne/Kirklareli), Baskent EDAS (Ankara and central provinces), GDZ Elektrik (Izmir/Manisa), Toroslar EDAS (Adana/Mersin/Gaziantep/Hatay/Kilis/Osmaniye), Meram EDAS (Konya/Karaman/Nigde/Kirsehir/Nevsehir/Aksaray), ADM / AYDEM (Aydin/Denizli/Mugla), AKDENIZ EDAS (Antalya/Isparta/Burdur), Yesilirmak EDAS (Samsun/Amasya/Corum/Ordu/Sinop), etc.

Power query templates:
```
site:teias.gov.tr "veri merkezi"
site:teias.gov.tr "data center"
site:teias.gov.tr "{project}" OR "{operator}"
site:teias.gov.tr "{district}" "GIS TM"
site:teias.gov.tr "{district}" "trafo merkezi"
site:teias.gov.tr "Kapasite Duyurusu" "{province}"
site:tedas.gov.tr "veri merkezi"
site:epdk.gov.tr "veri merkezi"
site:{dso-domain} "veri merkezi" "baglanti"
site:{dso-domain} "trafo merkezi" "{operator}"
"{project}" "MW" "veri merkezi"
"{project}" "MVA" "veri merkezi"
"{project}" "elektrik kapasitesi"
"{project}" "baglanti gorusu"
"{district}" "154 kV" "veri merkezi"
"{district}" "34.5 kV" "veri merkezi"
```

What to extract: contracted demand, installed power (`kurulu guc`, `MVA`), IT load if stated, transformer substation name (`TM`), distribution company, connection voltage, renewable / rooftop solar MW, generator count and ratings, and whether the evidence supports operational status or only grid readiness.

### 2.2 Power sanity checks

- Treat `MVA` and installed electrical capacity as **not identical** to IT load. Record field-specific units.
- For operator pages with only sqm / cabinet counts, infer MW only as a note, not `capacity_mw`, unless the source gives IT load / installed power.
- Watch for marketing totals across all facilities. Turkcell, for example, publishes group-level datacenter claims; do not assign the total to one site.
- Former / planned power-station and industrial-zone locations can be datacenter leads, but require permit or operator confirmation before counting.

---

## 3. BTK / telecom-regulator pipeline

### 3.1 BTK hosting-provider registry

- **BTK main site**: https://www.btk.gov.tr/.
- **Yer Saglayicilik Bildiriminde Bulunanlar list**: https://internet.btk.gov.tr/yer-saglayici-listesi.
- **Yer Saglayiciligi Bildirimi via e-Devlet**: https://www.turkiye.gov.tr/btk-yer-saglayiciligi-bildirimi-4322.
- **BTK Yer Saglayici notification interface**: https://yersaglayici.btk.gov.tr/.
- **BTK operator authorization data**: https://kurumsal.btk.gov.tr/yetkilendirmeler.

Use the BTK hosting-provider list as a **legal-entity and address seed**. It can reveal small / regional hosting providers and exact office addresses, but it does not prove a purpose-built datacenter.

BTK query workflow:
1. Search the BTK list for major operators and local keywords: `Turkcell`, `Superonline`, `Turk Telekom`, `Vodafone`, `Equinix`, `IsNet`, `Radore`, `Mars`, `Pen`, `NGN`, `Veganet`, `FiberDC`, `Netdirekt`, `VeriTeknik`, `KocSistem`.
2. Capture legal name, address, province, contact, and registration number if shown.
3. Pivot legal name to official site, trade registry, Uptime / TSE certification, PeeringDB, municipal planning, and CED.
4. For ISP / telecom operators, also search BTK authorization data and annual reports.

BTK / registry query templates:
```
site:internet.btk.gov.tr/yer-saglayici-listesi "{operator}"
site:internet.btk.gov.tr/yer-saglayici-listesi "{province}"
site:btk.gov.tr "yer saglayici" "{operator}"
site:ticaretsicil.gov.tr "{legal name}" "veri merkezi"
"{legal name}" "yer saglayici"
"{legal name}" "barindirma"
```

Grade guidance:
- BTK list = **A** for entity / notification / address.
- BTK list alone = **C** for facility existence.
- BTK + operator facility page or permit = **A** for facility existence.

---

## 4. Official cloud and hyperscale seeds

| Provider | Official source | Turkiye signal | Enumeration use |
|---|---|---|---|
| AWS | Regions docs https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; Istanbul GA announcement https://aws.amazon.com/about-aws/whats-new/2026/05/aws-local-zones-istanbul-turkiye/ | AWS Local Zone in Istanbul became generally available on 2026-05-20; AWS Direct Connect location in Istanbul was announced in 2025 within Equinix IL4. | A for Istanbul Local Zone / Direct Connect presence. Search Equinix IL4, Istanbul / Umraniye / Dudullu, and AWS partner pages. Do not infer AWS-owned datacenter. |
| Microsoft Azure | Azure regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Azure geographies https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No official Azure public cloud region in Turkiye found in official region list as of 2026-08-12. A Microsoft community answer in Dec 2023 stated no announced Microsoft datacenter region in Turkey, but re-check official region list each run. | Treat `Azure Turkiye` as a negative-control search. Look for Azure Stack / partner / government cloud via Turkcell, Turk Telekom, Vodafone, KocSistem, IsNet, not a Microsoft-owned Azure region unless official docs change. |
| Google Cloud | Locations https://cloud.google.com/about/locations ; official blog https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-coming-to-turkiye | Google Cloud announced a new Turkiye cloud region with Turkcell as part of a multi-year investment; official page says the region is coming, not yet live. | A for announced region. Search Turkcell + Google Cloud + Ankara / Kocaeli / Tekirdag / Istanbul / Izmir, then require planning / construction / energy evidence for actual sites. |
| Oracle Cloud | OCI regions https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm ; public regions https://www.oracle.com/cloud/public-cloud-regions/ | No official OCI public region in Turkiye found in region list. Turkcell previously announced Oracle Cloud services from Gebze. | Use as partner / hosted-cloud seed, not an OCI region unless official region list changes. |
| Huawei Cloud / Alibaba / IBM / SAP | Official global-location pages | May have edge / partner / enterprise cloud signals, but exact facility ownership is often opaque. | Use only as metro / partner lead; confirm through Turkish operator pages and BTK / permits. |

Cloud query templates:
```
"AWS Local Zone" "Istanbul" "Turkiye"
"AWS Direct Connect" "Istanbul" "Equinix IL4"
"Google Cloud" "Turkiye region" "Turkcell"
"Google Cloud" "Turkiye" "veri merkezi" "Turkcell"
"Azure" "Turkiye" "region" site:learn.microsoft.com
"Oracle Cloud" "Turkcell" "Gebze Veri Merkezi"
"bulut bolgesi" "veri merkezi" "Ankara"
"hiper olcekli bulut bolgesi" "Turkcell" "veri merkezi"
```

---

## 5. Official colo / operator seed list

Operator pages are primary statements for existence and marketed footprint, but capacity often needs filings, certifications, or construction pages.

| Operator / owner | Official source | Known high-yield provinces | Follow-up |
|---|---|---|---|
| Turkcell / Superonline | Facility service page https://www.turkcell.com.tr/kurumsal/dijital-is-servisleri/veri-merkezi-data-center ; wholesale page https://www.turkcell.com.tr/hakkimizda/toptan/sabit-data-hizmetleri/barindirma-ve-veri-merkezi-hizmetleri-ve-yerel-ag-erisimi/detay ; media pages for Gebze, Izmir, Ankara, Avrupa / Corlu | Kocaeli/Gebze, Ankara/Temelli, Izmir/Menderes, Tekirdag/Corlu, Istanbul/Edirne legacy | Search operator pages plus municipal / OSB / TEIAS evidence. Turkcell states 4 new-generation and 8 total data centers; allocate by named facility only. |
| Turk Telekom | Official DC page https://kurumsal.turktelekom.com.tr/bilisim-teknolojileri/veri-merkezi-ve-bulut/veri-merkezi-hizmetleri/veri-merkezlerimiz ; TTI colocation https://www.turktelekomint.com/product/co-location/ | Istanbul/Esenyurt, Istanbul/Gayrettepe, Ankara/Umitkoy; announced Ankara project with Ronesans | Search Turk Telekom + Ronesans + Ankara; check BTK authorizations and annual reports. |
| Vodafone Turkiye | Official page https://www.vodafone.com.tr/vodafone-business/data-center-veri-merkezi ; Invest.gov.tr Edgnex JV page https://www.invest.gov.tr/en/news/news-from-turkey/pages/vodafone-and-damac-to-invest-usd-100-million-in-data-center-in-turkiye.aspx | Istanbul European side, Istanbul Asian side, Ankara, Izmir, Adana; new Izmir Edgnex / DAMAC JV | Confirm existing sites via Vodafone official page, TIA/Uptime certifications, and local permits. The 2024 Izmir JV is A for investment announcement; verify construction / operation separately. |
| Equinix | Istanbul page https://www.equinix.com/data-centers/europe-colocation/turkiye-colocation/istanbul-data-centers ; Turkish site https://www.equinixdatacenters.com.tr/ | Istanbul / Umraniye / Dudullu OSB, IL1-IL4 | Official page is A for campus. Use AWS Direct Connect / Local Zone and PeeringDB as extra evidence; search Umraniye municipality / OSB for IL4 permits. |
| Is Bankasi / IsNet Atlas | Isbank page https://www.isbank.com.tr/bankamizi-taniyin/is-bankasinin-veri-merkezine-dunya-capinda-birincilik-odulu ; IsNet certification / blog pages https://www.isnet.net.tr/ | Istanbul / Tuzla | A for Atlas facility; use Uptime, USGBC, TSE, and IsNet brochure for certification / sustainability details. |
| ENKA Data Solutions | ENKA progress page https://www.enka.com/progress-of-tuzla-data-center-as-of-december-2025/ ; company site https://enkadatasolutions.com/tr/ | Istanbul / Tuzla | ENKA page gives 11 MW IT load for Tuzla project progress; verify with Tuzla planning and TEIAS/DSO. |
| NGN / Star of Bosphorus | Company / datacenter event pages; verify through official NGN pages when live | Istanbul | Directories are only C unless NGN official, PeeringDB, BTK, or certification confirms. |
| Radore | https://radore.com/tr | Istanbul | Official page confirms hosting / datacenter operator; use BTK and address-level searches. |
| Mars Datacenter | https://marsdatacenter.com/ | Istanbul | Official page + TSE / TS EN 50600 if available; search BTK and local permits. |
| PenDC / Pen Veri Merkezi | company site / BTK / directory | Istanbul | Confirm through BTK and official operator materials. |
| Netdirekt | https://www.netdirekt.com.tr/ | Izmir | Regional colo / hosting seed; verify via BTK and facility pages. |
| KocSistem | https://www.kocsistem.com.tr/ | Istanbul, Ankara | Search official managed-services pages and local data-center mentions; directories alone are C. |
| TurkSat | https://www.turksat.com.tr/ and official ministry / TRT / AA announcements | Ankara / Golbasi | Public-sector strategic datacenter; search `Turksat Golbasi Veri Merkezi`, ministry, CED, and power evidence. |
| Trendyol / Castle Investments / Khazna | Company and official/trade announcements | Ankara / Temelli | Search `Ankara Data Hub`, `Trendyol Castle Investments`, `Khazna Turkiye`; require construction / permit evidence for status. |

Operator query templates:
```
"{operator}" "veri merkezi" "{province}"
"{operator}" "data center" "Turkiye"
"{operator}" "MW" "veri merkezi"
"{operator}" "MVA" "veri merkezi"
"{operator}" "beyaz alan"
"{operator}" "kabinet"
"{operator}" "Tier III" "veri merkezi"
"{operator}" "TS EN 50600"
"{operator}" "LEED Gold" "veri merkezi"
site:uptimeinstitute.com "{operator}" "Turkey"
site:usgbc.org "veri merkezi" "Turkey"
site:tse.org.tr "veri merkezi" "{operator}"
```

---

## 6. Province enumeration strategy

### 6.1 Standard workflow for each of 81 provinces

1. Search official / operator seeds:
   ```
   "{province}" "veri merkezi"
   "{province}" "data center"
   "{province}" "sunucu merkezi"
   "{province}" "sistem odasi"
   "{province}" "bulut" "veri merkezi"
   "{province}" "OSB" "veri merkezi"
   ```
2. Search the province's metropolitan municipality, district municipalities, and OSBs:
   ```
   site:{province-municipality-domain} "veri merkezi"
   site:{district-domain} "veri merkezi" "imar"
   site:{osb-domain} "veri merkezi" OR "data center"
   site:{osb-domain} "trafo merkezi" "bilisim"
   ```
3. Search e-CED and Ministry pages for environmental records:
   ```
   site:eced-duyuru.csb.gov.tr "{province}" "veri merkezi"
   site:csb.gov.tr "{province}" "veri merkezi" "CED"
   ```
4. Search power / grid:
   ```
   site:teias.gov.tr "{province}" "trafo merkezi"
   site:teias.gov.tr "{district}" "GIS TM"
   site:{dso-domain} "{province}" "veri merkezi"
   "{province}" "{operator}" "MVA" OR "MW"
   ```
5. Search BTK for local operators and addresses:
   ```
   site:internet.btk.gov.tr/yer-saglayici-listesi "{province}"
   site:internet.btk.gov.tr/yer-saglayici-listesi "{local operator}"
   ```
6. Search certifications and network directories only after official/operator seeds:
   ```
   site:uptimeinstitute.com "Turkey" "{province}"
   site:peeringdb.com/fac "{province}" "{operator}"
   site:datacentermap.com/turkey "{province}"
   ```
7. Assign status:
   - `announced`: MoU / investment announcement only.
   - `planned`: site, district, or project name known; no construction evidence.
   - `construction`: foundation, contractor progress, building permit, CED approval, utility connection, or official construction update.
   - `operational`: opening announcement, operator facility page, active service page, certification, PeeringDB facility with corroboration, or customer/government commissioning.

### 6.2 High-yield province clusters

- **Istanbul**: Equinix IL1-IL4 / Umraniye-Dudullu, Turk Telekom Esenyurt and Gayrettepe, Vodafone, Is Bankasi Atlas / Tuzla, ENKA Tuzla, Radore, Mars, PenDC, NGN, Telehouse / Teknotel, KocSistem Camlica, public / airport facilities. Search district portals: Umraniye, Tuzla, Esenyurt, Besiktas, Basaksehir, Pendik, Sancaktepe, Kadikoy, Atasehir.
- **Ankara**: Turkcell Temelli, Turk Telekom Umitkoy, Turksat Golbasi, Trendyol / Castle / Khazna Ankara Data Hub, Vodafone Ankara, KocSistem, VeriTeknik, university / public-sector datacenters. Search Golbasi, Sincan / Temelli, Cankaya, Yenimahalle, OSTIM, Baskent OSB, Ankara Anadolu OSB.
- **Izmir**: Turkcell Menderes, Vodafone / Edgnex DAMAC Izmir, Netdirekt and regional hosting. Search Menderes, Gaziemir, Cigli, Bornova, Izmir Ataturk OSB, GDZ Elektrik.
- **Kocaeli**: Turkcell Gebze and industrial-zone / Istanbul-edge spillover. Search Gebze, Cayirova, Dilovasi, Kocaeli Gebze GOSB, SEDAS, TEIAS substations, Google Cloud / Turkcell expansion references.
- **Tekirdag / Corlu**: Turkcell Avrupa Veri Merkezi / Corlu; search Corlu municipality, Ergene, Velimese OSB, TREDAS, TEIAS.
- **Adana, Antalya, Kayseri, Konya, Samsun, Trabzon**: often regional / telco / public-sector facilities. Search Vodafone, Turk Telekom, Turkcell edge, OSB announcements, municipality / university server-room tenders.
- **Rize / Gaziantep / Eskisehir / Erzurum / Mersin**: mostly regional hosting, municipal, university, or planned projects. Prioritize official university / municipality pages and BTK over directories.

---

## 7. Evidence hierarchy and pitfalls

### 7.1 Evidence hierarchy

1. **A - physical/regulatory proof**: municipality building permit / zoning decision, e-CED decision, TEIAS / DSO connection evidence, TEDAS acceptance, official opening / commissioning, TSE / Uptime / LEED record naming the facility.
2. **A - operator official**: named facility page with province / district and service status.
3. **A-/B+ - government investment news**: Invest.gov.tr, ministry, AA / TRT statements naming project cost, location, MW, and schedule. Use for announcement / construction status but still seek permits.
4. **B - trade press / engineering contractors**: DCD, ENKA project progress, contractor portfolios, certification pages.
5. **C - directories / market reports**: DataCenterMap, Baxtel, Data Center Catalog, Ocolo, Datacenters.com. Use as leads; verify before counting.

### 7.2 Common pitfalls

- **BTK hosting provider != datacenter**. It may be an office, reseller, web host, or virtual provider.
- **Province-only claims hide multiple sites**. Turkcell and Vodafone publish multi-facility totals; assign only named site details to individual records.
- **Cloud region != owned datacenter**. AWS Istanbul Local Zone and Direct Connect are local infrastructure signals, but the physical facility may be Equinix / partner-operated. Google Cloud Turkiye is announced / coming; Azure Turkiye is not in the official Azure region list as of this methodology date.
- **MW vs MVA vs total facility power**. Store source unit exactly. Use `capacity_mw` only for IT load when the source says IT MW; otherwise note installed power separately.
- **Turkish characters affect recall**. Always search both `Istanbul` and `Istanbul`, `Izmir` and `Izmir`, `Tekirdag` and `Tekirdag`, `Turkiye` and `Turkiye`.
- **Public-sector server rooms are not always commercial datacenters**. Record them if the project scope is a dedicated data center / disaster-recovery / main system room, but tag as public / enterprise rather than colo/hyperscale.

---

## 8. Recommended actionable pipeline

1. **Seed the facility universe** from official operator pages: Turkcell, Turk Telekom, Vodafone, Equinix, IsNet / Atlas, ENKA, TurkSat, plus official cloud pages for AWS and Google Cloud.
2. **Run high-yield province sweeps** for Istanbul, Ankara, Izmir, Kocaeli, Tekirdag first using planning + e-CED + TEIAS/DSO + BTK queries.
3. **Use BTK Yer Saglayici** to find smaller regional operators by province, then pivot each legal name to official facility, trade registry, PeeringDB, certification, and municipal evidence.
4. **Validate power and status** using TEIAS / DSO / EPDK / operator capacity statements before recording MW.
5. **Expand to remaining provinces** with municipal / university / OSB tenders for `sistem odasi`, `sunucu odasi`, `felaket kurtarma merkezi`, and `veri merkezi`.
6. **Grade each data point separately**: a facility may be A for existence, B for capacity, and C for exact address.

