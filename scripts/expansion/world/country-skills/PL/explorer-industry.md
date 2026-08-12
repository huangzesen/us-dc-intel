# PL Explorer - Industry, Trade Press, Vendors, and Voivodeship Query Patterns

Date: 2026-08-12. Scope: Poland datacenter enumeration methodology focused on industry/trade press, Polish search patterns, major developers/operators, and voivodeship-level query templates. Reliability grades: **A** = official/primary source or operator-owned current page; **B** = established trade press, association, legal/market analysis, or government program page that should be verified; **C** = aggregators, market snippets, event pages, or weak secondary leads.

---

## 0. Poland-specific frame

- Poland has no single public national facility register for commercial data centers. Enumeration should start with **operator/vendor pages and trade press**, then confirm with public building/environment records where a project is new, large, or not listed by the operator.
- The practical backbone is: **trade/industry lead -> operator page -> municipality/powiat BIP -> GUNB RWDZ building register -> environmental record/KIP/decision -> grid/utility/local press**.
- The market is Warsaw-heavy. Treat **Mazowieckie / Warsaw metropolitan area** as the first pass, especially Warsaw, Duchnice/Ozarow Mazowiecki, Jawczyce/Ozarow or Blonie area, Piaseczno, Lazy/Raszyn/Lesznowola, and other western/southern Warsaw suburbs. Secondary clusters are **Poznan (Wielkopolskie)**, **Krakow/Skawina/Alwernia (Malopolskie)**, **Katowice/Bytom/Silesian metro (Slaskie)**, **Wroclaw (Dolnoslaskie)**, and **Gdansk/Trojmiasto (Pomorskie)**.
- Use Polish terms first. Product pages often say "data center", but BIP and permit systems more often use **centrum danych**, **centrum przetwarzania danych**, **osrodek przetwarzania danych**, **serwerownia**, **kolokacja**, **chmura obliczeniowa**, **obiekt teleinformatyczny**, **infrastruktura krytyczna**, **agregaty pradotworcze**, **stacja transformatorowa**, **GPZ**, **przylacze energetyczne**, **decyzja srodowiskowa**, **decyzja o srodowiskowych uwarunkowaniach**, **KIP / karta informacyjna przedsiewziecia**, **pozwolenie na budowe**, **MPZP / miejscowy plan zagospodarowania przestrzennego**, **WZ / warunki zabudowy**, **uchwala**, **obwieszczenie**, **BIP**.
- Cloud-region pages are **A for logical region existence**, not for physical facility address. Microsoft, Google, OVHcloud, and AWS Local Zones can establish a Warsaw-region signal, but exact facilities need operator/permit/local evidence.

---

## 1. Industry, association, and trade-press sources

### 1.1 Association, events, and market context

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Polish Data Center Association (PLDCA) | https://pldca.pl/en/ | National association. Use member ecosystem as a seed list and for policy/market framing. It is not a facility registry. | B |
| Data Center Nation Warsaw | https://datacenternation.com/dcn-warsaw/ | Current conference ecosystem, sponsors, speakers, and market framing. Good for discovering active developers, engineers, contractors, and power/cooling vendors. | B/C |
| DATA CENTER Expo Poland | https://warsawexpo.eu/en/fair-calendar/data-center-expo-poland/ | Event/supplier map; useful for Polish-language vendor names and new entrants. Verify facility claims elsewhere. | C |
| PMR / Atman market notes | Example: https://atman.pl/en/blog-post/polish-data-center-market-2025-2030-pmr-atman-insight/ | Market shares, capacity trend, named top operators. Treat Atman-authored market material as strong lead/context, not neutral census. | B |
| Legal/real-estate analysis | Dudkowiak: https://www.dudkowiak.com/invest-in-poland/data-centers-investments-in-poland ; Miller Canfield: https://millercanfield.pl/en/legal-aspects-of-building-data-centres/ | Explains Polish permit, zoning, environmental-decision path. Useful for search vocabulary and process. | B |
| JLL/CBRE/Cundall/Haskoning/Baker McKenzie/Prime East | Example Haskoning: https://www.haskoning.com/en/newsroom/blogs/2023/unraveling-the-polish-data-centre-market ; Cundall: https://www.cundall.com/ideas/blog/poland-moves-into-next-data-centre-phase-in-2026 | Market geography, power/land constraints, hyperscale interest. Use as cluster context only. | B/C |

### 1.2 Polish trade and business press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| TELKO.in | https://www.telko.in/ ; query `site:telko.in "data center" Polska Atman DATA4 Microsoft` and `site:telko.in "centrum danych"` | Best telecom/DC sector feed for Polish market status, KCPD, Atman, 3S/Play, telco data centers, and capacity trend articles. | B |
| ITwiz | https://itwiz.pl/ ; query `site:itwiz.pl "centrum danych" Polska` | Strong Polish IT trade source. Good for KCPD, association formation, public-sector infrastructure, Microsoft/Google/Atman/Beyond.pl. | B |
| CRN Polska | https://crn.pl/ ; query `site:crn.pl "centrum danych" KCPD Atman Beyond` | Channel/business IT press. Useful for KCPD funding/procurement and vendor ecosystem. | B |
| Computerworld Polska | https://www.computerworld.pl/ ; query `site:computerworld.pl "centrum danych" Warszawa Google Microsoft Orange` | Cloud-region announcements, Orange Warsaw Data Hub, older but useful market articles. Verify current status with operators. | B |
| CyberDefence24 / Bankier / WNP / Rzeczpospolita | Queries: `site:cyberdefence24.pl Krajowe Centrum Przetwarzania Danych`, `site:wnp.pl "centrum danych" Polska`, `site:rp.pl "centrum danych" Polska` | Public-sector KCPD and investment-policy leads; less complete for commercial colo facilities. | B/C |
| InvestMap / PropertyNews / property portals | `site:investmap.pl "centrum danych"`, `site:propertynews.pl "data center" Polska` | Real-estate construction leads and land transactions. Always verify with BIP/GUNB/operator. | C+/B- |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Poland data center Warsaw Atman DATA4 Vantage` | International DC trade press. Good for hyperscale campus announcements, Warsaw market summary, 3S Katowice, funding programs. | B |
| Data Centre Magazine / DatacenterDynamics / Baxtel snippets | `Poland data center market Warsaw Poznan Krakow Katowice` | Useful for lead discovery and city/operator counts, but not source-of-record. | C |

### 1.3 Aggregators and directories

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/poland/ | City/operator seed list; good for older colo addresses. Coverage and status can lag. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/poland | Commercial provider/facility pages; useful for address/operator aliases. | C+ |
| Baxtel | https://baxtel.com/data-center/poland | Good for hyperscale/campus adjacency and likely Microsoft/Data4/EdgeConneX mapping, but verify exact claims. | C+ |
| PeeringDB | https://www.peeringdb.com/ | Confirms active peering facilities/IXPs. Grade B for active interconnection signal, C for completeness. | B/C |

---

## 2. Core Polish query patterns

### 2.1 National industry sweep

```text
"centrum danych" Polska "MW" "m2" operator
"centrum przetwarzania danych" Polska "pozwolenie na budowe"
"data center" Polska Warszawa Atman Beyond.pl Equinix DATA4 Vantage EdgeConneX
"rynek data center w Polsce" Atman Beyond DATA4 Microsoft Google
site:telko.in ("centrum danych" OR "data center") Polska
site:itwiz.pl ("centrum danych" OR "data center") Polska
site:crn.pl ("centrum danych" OR "data center") Polska
site:computerworld.pl ("centrum danych" OR "centrum przetwarzania danych")
site:datacenterdynamics.com Poland "data center" Warsaw
```

### 2.2 Permit and local-government vocabulary

```text
"centrum danych" "{gmina OR city}" "BIP"
"centrum przetwarzania danych" "{gmina}" "pozwolenie na budowe"
"osrodek przetwarzania danych" "{gmina}" "decyzja srodowiskowa"
"serwerownia" "{gmina}" "agregaty pradotworcze"
"data center" "{gmina}" "MPZP" OR "miejscowy plan"
"centrum danych" "{gmina}" "warunki zabudowy" OR "WZ"
"centrum danych" "{gmina}" "karta informacyjna przedsiewziecia" OR "KIP"
"centrum danych" "{gmina}" "stacja transformatorowa" OR "GPZ" OR "przylacze energetyczne"
site:bip.{gmina}.pl "centrum danych"
site:{gmina}.pl "centrum danych" "obwieszczenie"
site:{powiat}.pl "centrum danych" "pozwolenie na budowe"
```

### 2.3 Official/public-record surfaces

| Channel | URL / pattern | What it confirms | Grade |
|---|---|---|---|
| GUNB RWDZ public construction register | https://wyszukiwarka.gunb.gov.pl/ and map https://wyszukiwarka.gunb.gov.pl/mapa/ | Applications, decisions, and notices in construction matters. Search by address, parcel, municipality, investor, and keywords once a lead is known. | A |
| Municipal/powiat BIP | `site:bip.{gmina}.pl`, `site:{gmina}.pl/bip`, `site:bip.{powiat}.pl` | Council resolutions, zoning, WZ, environmental notices, building-admin records. | A |
| EKOportal / PDWD | https://www.ekoportal.gov.pl/ and https://www.ekoportal.gov.pl/aplikacje/pdwd-/-wykaz | Environmental-document registers and public lists for decisions and documents. Useful where local search is poor. | A/B |
| Voivodeship / regional gov.pl pages | `site:gov.pl/web/uw-{region-slug} "centrum danych"` | Voivode notices, special proceedings, regional environmental/administrative signals. | A/B |
| Public procurement | https://ezamowienia.gov.pl/ , https://ted.europa.eu/ | KCPD, public-sector data centers, local-government server rooms, design/build tenders. | A/B |
| Geoportal / parcel lookup | https://www.geoportal.gov.pl/ | Parcel IDs and land context after a local lead. Use with GUNB map/RWDZ. | A for parcel context |

---

## 3. Vendor/operator seed list by cluster

Operator pages are **A for existence/current marketed footprint** and **B for capacity**, unless the operator publishes formal spec sheets. Exact hyperscaler sites remain **C** until tied to a facility by operator, official local filing, or strong incident/interconnect evidence.

### 3.1 Mazowieckie: Warsaw, Ozarow Mazowiecki/Duchnice, Jawczyce, Piaseczno, Lazy/Raszyn/Lesznowola

- **Atman** - Warsaw-1, Warsaw-2, Warsaw-3/Duchnice, plus Katowice. Official colocation overview: https://atman.pl/en/services/colocation/ . WAW-3 official: https://atman.pl/en/atman-data-center/warsaw-3/ and construction/opening releases: https://atman.pl/en/construction-of-atman-data-center-warsaw-3-started/ , https://atman.pl/en/atman-opens-flagship-data-center-waw-3/ . Grade A/B.
- **Equinix** - Warsaw data centers. Official: https://www.equinix.com/data-centers/europe-colocation/poland-colocation/warsaw-data-centers . Grade A/B.
- **DATA4** - Warsaw/Jawczyce campus. Official: https://www.data4group.com/en/data-centers-warsaw-poland/ . DCD/Baxtel useful for phase/capacity leads; verify locally. Grade A/B.
- **Vantage Data Centers** - WAW1 campus near Warsaw, 48 MW planned/critical IT load. Official: https://vantage-dc.com/data-center-locations/emea/warsaw-poland/ . Grade A/B.
- **EdgeConneX** - Warsaw data center/campus. Official: https://www.edgeconnex.com/locations/emea/warsaw-pl/ . Grade A/B.
- **Microsoft Azure** - Poland Central cloud region around Warsaw, three physical locations. Official launch: https://news.microsoft.com/europe/2023/04/26/microsoft-launches-its-first-datacenter-region-in-poland-bringing-new-opportunities-to-develop-the-digital-economy/ ; local community: https://local.microsoft.com/communities/emea/warsaw-metropolitan-area-poland/ . Grade A for region/greater Warsaw operations, C for exact facilities.
- **Google Cloud** - Warsaw cloud region `europe-central2`. Official opening: https://cloud.google.com/blog/products/infrastructure/google-cloud-region-in-warsaw-poland-is-now-open ; Google Cloud interconnect docs identify Atman WAW-1 as a Warsaw facility for Cloud Interconnect: https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities . Grade A for region/interconnect, C/B for facility inference depending on record type.
- **OVHcloud** - Warsaw data center/region. Official location pages: https://www.ovhcloud.com/en/datacenter/ and https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ . Grade A/B.
- **T-Mobile Polska** - Piaseczno and Warsaw-area facilities. Official colocation page: https://biznes.t-mobile.pl/en/products-and-services/data-center/server-colocation ; Warsaw Szlachecka: https://biznes.t-mobile.pl/en/data-centers/warszawa-szlachecka-2 . Grade A/B.
- **Orange Polska** - Warsaw Data Hub, Lazy near Warsaw. Official: https://www.orange.pl/duze-firmy/data-center ; press: https://biuroprasowe.orange.pl/informacje-prasowe/nowe-data-center-orange-powstaje-pod-warszawa-za-rok-obsluzy-pierwszych-klientow/ . Grade A/B.
- **Netia** - Jawczyce / Netia Data Center MIND plus broader DC/cloud products. Official: https://www.netia.pl/en/for-business/products/data-center-cloud and https://www.netia.pl/en/operators/aktualnosci/netia-s-new-data-center-fills-up-at-a-record-pace . Grade A/B.
- Additional Warsaw pivots: Aruba Cloud PL1, Lukman, Free/Play/3S Warsaw, bank/financial-sector facilities, NASK/COI/KCPD public-sector sites.

Mazowieckie templates:

```text
"centrum danych" Warszawa Atman Equinix DATA4 Vantage EdgeConneX Microsoft Google
"centrum danych" Duchnice Ozarow Mazowiecki Atman "pozwolenie na budowe"
"centrum danych" Jawczyce DATA4 Netia "BIP" OR "pozwolenie na budowe"
"centrum danych" Lazy Orange "Warsaw Data Hub" "BIP"
"centrum danych" Piaseczno T-Mobile "BIP" OR "agregaty pradotworcze"
site:warszawa.pl "centrum danych" "pozwolenie na budowe"
site:bip.warszawa.pl "centrum danych"
site:ozarow-mazowiecki.pl "centrum danych" OR Atman OR Microsoft
site:bip.ozarow-mazowiecki.pl "centrum danych" OR "Duchnice"
site:piaseczno.eu "centrum danych" T-Mobile
site:lesznowola.pl "centrum danych" OR "data center"
site:wyszukiwarka.gunb.gov.pl "centrum danych" "mazowieckie"
```

### 3.2 Wielkopolskie: Poznan

- **Beyond.pl** - Poznan campus, DC1/DC2/DC3/DC4 positioning. Official: https://www.beyond.pl/ and DC2: https://www.beyond.pl/en/data-centers-campus/beyond-pl-data-center-2/ . Public claims include high-density campus and Rated 4/EN 50600 Class 4 certifications; use official pages/spec sheets for facility details. Grade A/B.
- **Poznan Supercomputing and Networking Center (PSNC/PCSS)** - research/HPC and national science infrastructure; useful for non-commercial data-center enumeration. Official PCSS pages should be used where relevant. Grade A.
- Search for regional telcos, municipal IT, university/HPC, and cloud/AI GPU colocations.

Wielkopolskie templates:

```text
"centrum danych" Poznan Beyond.pl "MW" OR "m2"
"centrum danych" Poznan "pozwolenie na budowe" "BIP"
site:poznan.pl "centrum danych" OR "serwerownia"
site:bip.poznan.pl "centrum danych" OR "centrum przetwarzania danych"
site:powiat.poznan.pl "centrum danych" "pozwolenie na budowe"
"A. Kreglewskiego" Beyond.pl "centrum danych"
"Dziadoszanska" Beyond.pl "centrum danych"
```

### 3.3 Malopolskie: Krakow, Skawina, Alwernia

- **Polcom** - data centers in Skawina and Alwernia. Official: https://polcom.com.pl/en/about-us/data-center/ , Skawina page https://polcom.com.pl/en/about-us/data-center/data-center-skawina/ . Grade A/B.
- **Google / engineering cloud presence** - Krakow engineering presence is not itself a data center; do not count as facility without infrastructure evidence. Use only as market context.
- **Cyfronet AGH** - academic/HPC data center infrastructure in Krakow; enumerate separately from commercial colo if scope includes research/public-sector facilities. Grade A.

Malopolskie templates:

```text
"centrum danych" Krakow Skawina Polcom
"centrum danych" Alwernia Polcom
site:krakow.pl "centrum danych" OR "serwerownia"
site:bip.krakow.pl "centrum danych" OR "centrum przetwarzania danych"
site:skawina.pl Polcom "centrum danych" OR "decyzja srodowiskowa"
site:alwernia.pl Polcom "centrum danych" OR "pozwolenie na budowe"
"agregaty pradotworcze" "centrum danych" Krakow
```

### 3.4 Slaskie: Katowice, Bytom, Silesian metro

- **3S / Play B2B** - facilities in Katowice, Bytom, Gdansk, Warsaw per operator pages; Katowice ul. Gospodarcza 12 page: https://3s.pl/infrastruktura/nasze-obiekty/ . DCD reported 3S expansion/new Katowice facility and plans for Warsaw, Gdansk, Wroclaw: https://www.datacenterdynamics.com/en/news/3s-group-announces-new-data-center-in-katowice-poland/ . Grade A/B.
- **Atman Katowice (KTW-1)** - listed in Atman market/service materials; verify with Atman official and local records. Grade A/B once official page found.
- **Polcom Alwernia** is geographically Malopolskie, but trade pages may say "near Katowice"; do not misassign to Slaskie.
- Search industrial brownfield, telecom, and edge/HPC sites across Katowice, Bytom, Gliwice, Tychy, Sosnowiec, Chorzow.

Slaskie templates:

```text
"centrum danych" Katowice 3S Play Atman
"centrum danych" Bytom 3S Play
site:katowice.eu "centrum danych" OR "serwerownia"
site:bip.katowice.eu "centrum danych" OR "agregaty pradotworcze"
site:bytom.pl "centrum danych" OR "centrum przetwarzania danych"
site:gliwice.eu "centrum danych" OR "data center"
"Gospodarcza 12" Katowice "centrum danych"
```

### 3.5 Dolnoslaskie: Wroclaw

- Wroclaw appears as a secondary/edge market in trade press and aggregator lists; 3S has previously mentioned Wroclaw expansion ambitions. Verify all Wroclaw leads through operator pages or local BIP/GUNB.
- Include Wroclaw Centre for Networking and Supercomputing for research/HPC scope if relevant.

Dolnoslaskie templates:

```text
"centrum danych" Wroclaw "kolokacja" OR "data center"
"centrum przetwarzania danych" Wroclaw "pozwolenie na budowe"
site:wroclaw.pl "centrum danych" OR "serwerownia"
site:bip.um.wroc.pl "centrum danych" OR "centrum przetwarzania danych"
site:duw.pl "centrum danych" "dolnoslaskie"
```

### 3.6 Pomorskie: Gdansk, Gdynia, Trojmiasto

- **3S / Play B2B** lists Gdansk among strategic data-center locations. Verify facility pages and Gdansk/Gdynia local records.
- **OVHcloud** has an office in Gdansk, but its official data center location is Warsaw; do not count office as DC.
- Include TASK / Academic Computer Centre in Gdansk for research/HPC scope if relevant.

Pomorskie templates:

```text
"centrum danych" Gdansk 3S Play TASK
"centrum danych" Gdynia "kolokacja" OR "serwerownia"
site:gdansk.pl "centrum danych" OR "centrum przetwarzania danych"
site:bip.gdansk.pl "centrum danych" OR "serwerownia"
site:gdynia.pl "centrum danych" OR "data center"
site:gov.pl/web/uw-pomorski "centrum danych" OR "pozwolenie na budowe"
```

### 3.7 Public-sector / KCPD

- **Krajowe Centrum Przetwarzania Danych (KCPD)** is a strategic government data-center program, not a commercial colo operator. NASK archive page: https://archiwum.nask.pl/pl/projekty-dofinansowane/projekty-ue/5337%2CKrajowe-Centrum-Przetwarzania-Danych-KCPD.html ; Ministry page: https://www.gov.pl/web/cyfryzacja/wieloletni-program-krajowe-centrum-przetwarzania-danych-kcpd-etap-i--wsparcie-procesu-przygotowania-projektu . Trade coverage from ITwiz/CRN/TELKO.in/DCD can seed schedule, funding, and contractors. Exact locations may be sensitive or obscured; use only public sources and mark confidence.

KCPD templates:

```text
"Krajowe Centrum Przetwarzania Danych" KCPD "pozwolenie na budowe"
"KCPD" "centrum danych" NASK COI Ministerstwo Cyfryzacji
site:gov.pl/web/cyfryzacja "Krajowe Centrum Przetwarzania Danych"
site:ezamowienia.gov.pl "Krajowe Centrum Przetwarzania Danych"
site:ted.europa.eu "Krajowe Centrum Przetwarzania Danych"
site:telko.in KCPD "centrum danych"
site:itwiz.pl KCPD "centrum danych"
```

---

## 4. Hyperscaler/cloud official pages

| Provider | Poland signal | URL | Grade |
|---|---|---|---|
| Microsoft Azure | Poland Central, near Warsaw; official launch says three independent physical locations around Warsaw. | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; https://news.microsoft.com/europe/2023/04/26/microsoft-launches-its-first-datacenter-region-in-poland-bringing-new-opportunities-to-develop-the-digital-economy/ ; https://local.microsoft.com/communities/emea/warsaw-metropolitan-area-poland/ | A region / C facility |
| Google Cloud | Warsaw region `europe-central2`; official opening and location docs. | https://cloud.google.com/blog/products/infrastructure/google-cloud-region-in-warsaw-poland-is-now-open ; https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | A region / C facility |
| Google Cloud Interconnect | Warsaw interconnect facilities include Atman Data Center Warsaw-1 in official docs. | https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities | A interconnect listing / B facility linkage |
| OVHcloud | Warsaw data center/region and public cloud availability. | https://www.ovhcloud.com/en/datacenter/ ; https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ | A/B |
| AWS | No full public Polish region in the operator pages found for this pass; AWS Local Zone/edge references in market press should be treated as region/edge signals only. | https://aws.amazon.com/about-aws/global-infrastructure/ | A for official region/local-zone listing only |
| Oracle Cloud / OCI | No Poland public cloud region found in this pass; verify official region list before counting. | https://www.oracle.com/cloud/public-cloud-regions/ | A for official region list |

Cloud pivot queries:

```text
"Poland Central" Azure "datacenter" Warsaw
"Microsoft" "Ozarow Mazowiecki" datacenter OR "centrum danych"
"Google Cloud" Warszawa "Atman" OR "europe-central2"
"Google Cloud" "centrum danych" Warszawa
"OVHcloud" Warszawa "data centre" OR "centrum danych"
"AWS Local Zone" Warsaw Poland data center
```

---

## 5. Voivodeship-by-voivodeship enumeration matrix

For each voivodeship, run three passes:

1. **Industry/operator pass (B/A)**: known operators, city names, DCD/TELKO/ITwiz/Computerworld.
2. **Local BIP/GUNB pass (A)**: city/gmina/powiat BIP plus GUNB RWDZ by address/parcel/investor.
3. **Environmental/grid pass (A/B)**: EKOportal/PDWD, local environmental decisions, substations, generator notices, district heating/heat reuse.

Use unaccented and accented variants: `Łódź/Lodz`, `Wrocław/Wroclaw`, `Poznań/Poznan`, `Gdańsk/Gdansk`, `Śląskie/Slaskie`, `Małopolskie/Malopolskie`.

| Voivodeship | Priority metros / known pivots | Query templates |
|---|---|---|
| Mazowieckie | Warsaw, Ozarow Mazowiecki/Duchnice, Jawczyce, Piaseczno, Lazy/Raszyn/Lesznowola; Atman, Equinix, DATA4, Vantage, EdgeConneX, Microsoft, Google, OVHcloud, T-Mobile, Orange, Netia | `+"centrum danych" "mazowieckie" Warszawa`, `site:mazowieckie.pl "centrum danych"`, `site:gov.pl/web/uw-mazowiecki "centrum danych"`, `site:bip.{gmina}.pl "centrum danych"`, `+"data center" Jawczyce DATA4`, `+"centrum danych" Duchnice Atman`, `+"centrum danych" Piaseczno T-Mobile` |
| Wielkopolskie | Poznan; Beyond.pl, PSNC/PCSS, regional telcos | `+"centrum danych" Poznan Beyond.pl`, `site:poznan.pl "centrum danych"`, `site:bip.poznan.pl "centrum danych"`, `site:powiat.poznan.pl "centrum danych"`, `+"centrum danych" "wielkopolskie" "pozwolenie na budowe"` |
| Malopolskie | Krakow, Skawina, Alwernia; Polcom, Cyfronet | `+"centrum danych" Krakow Skawina Polcom`, `site:krakow.pl "centrum danych"`, `site:skawina.pl Polcom`, `site:alwernia.pl "centrum danych"`, `site:malopolska.uw.gov.pl "centrum danych"` |
| Slaskie | Katowice, Bytom, Gliwice, Tychy, Sosnowiec; 3S/Play, Atman KTW leads | `+"centrum danych" Katowice 3S Play`, `site:katowice.eu "centrum danych"`, `site:bytom.pl "centrum danych"`, `+"Gospodarcza 12" Katowice`, `site:slaskie.pl "centrum danych"` |
| Dolnoslaskie | Wroclaw, Bielany Wroclawskie, Legnica; regional colo/HPC | `+"centrum danych" Wroclaw`, `site:wroclaw.pl "centrum danych"`, `site:bip.um.wroc.pl "centrum danych"`, `+"data center" "dolnoslaskie" "pozwolenie na budowe"` |
| Pomorskie | Gdansk, Gdynia, Sopot; 3S/Play, TASK | `+"centrum danych" Gdansk 3S Play TASK`, `site:gdansk.pl "centrum danych"`, `site:bip.gdansk.pl "centrum danych"`, `site:gdynia.pl "centrum danych"`, `site:gov.pl/web/uw-pomorski "centrum danych"` |
| Lodzkie | Lodz, Strykow, Pabianice; logistics/central-Poland power/land leads | `+"centrum danych" Lodz OR Łódź`, `site:lodz.pl "centrum danych"`, `site:bip.uml.lodz.pl "centrum danych"`, `+"data center" Strykow "pozwolenie na budowe"` |
| Kujawsko-Pomorskie | Bydgoszcz, Torun; Exea/Torun leads, public-sector/university | `+"centrum danych" Torun Exea`, `+"centrum danych" Bydgoszcz`, `site:torun.pl "centrum danych"`, `site:bip.bydgoszcz.pl "centrum danych"`, `site:gov.pl/web/uw-kujawsko-pomorski "centrum danych"` |
| Lubelskie | Lublin, Swidnik; low-density edge/public-sector | `+"centrum danych" Lublin`, `site:lublin.eu "centrum danych"`, `site:bip.lublin.eu "centrum przetwarzania danych"`, `+"serwerownia" Lublin "pozwolenie na budowe"` |
| Podkarpackie | Rzeszow, Jasionka; aviation/IT/public-sector leads | `+"centrum danych" Rzeszow`, `site:rzeszow.pl "centrum danych"`, `site:bip.erzeszow.pl "centrum danych"`, `+"data center" Jasionka Rzeszow` |
| Podlaskie | Bialystok; low-density edge/public-sector | `+"centrum danych" Bialystok`, `site:bialystok.pl "centrum danych"`, `site:bip.bialystok.pl "serwerownia"`, `site:gov.pl/web/uw-podlaski "centrum danych"` |
| Swietokrzyskie | Kielce; low-density public-sector/edge | `+"centrum danych" Kielce`, `site:kielce.eu "centrum danych"`, `site:bip.kielce.eu "serwerownia"`, `+"centrum przetwarzania danych" "swietokrzyskie"` |
| Warminsko-Mazurskie | Olsztyn, Elblag; low-density public-sector/edge | `+"centrum danych" Olsztyn`, `site:olsztyn.eu "centrum danych"`, `site:bip.olsztyn.eu "serwerownia"`, `+"data center" Elblag` |
| Zachodniopomorskie | Szczecin, Stargard; port/logistics/edge | `+"centrum danych" Szczecin`, `site:szczecin.eu "centrum danych"`, `site:bip.um.szczecin.pl "centrum danych"`, `+"data center" Stargard "pozwolenie na budowe"` |
| Lubuskie | Zielona Gora, Gorzow Wielkopolski; low-density edge | `+"centrum danych" Zielona Gora`, `+"centrum danych" Gorzow Wielkopolski`, `site:zielona-gora.pl "centrum danych"`, `site:gorzow.pl "centrum danych"` |
| Opolskie | Opole; low-density edge/public-sector | `+"centrum danych" Opole`, `site:opole.pl "centrum danych"`, `site:bip.um.opole.pl "serwerownia"`, `+"centrum przetwarzania danych" "opolskie"` |

---

## 6. Validation notes and pitfalls

- Do not count **sales offices, engineering offices, cloud partner offices, or network PoPs** as data centers unless the source explicitly describes data-center/colocation/processing infrastructure.
- Polish sources mix **data center**, **centrum danych**, and **centrum przetwarzania danych**. Search all variants and include no-accent versions because OCR/BIP search is inconsistent.
- **KCPD** locations and detailed security information may be intentionally limited. Record only public facts and mark status/location confidence conservatively.
- Building permits in GUNB/RWDZ may use a generic building category or investor SPV rather than the final operator. Search by parcel/address from operator announcements and by terms such as `budynek uslugowy`, `budynek techniczny`, `stacja transformatorowa`, and `agregaty pradotworcze`.
- Capacity from operator pages and market reports should be stored as "claimed/planned" unless backed by permit, grid connection, opening announcement, or formal spec sheet.
