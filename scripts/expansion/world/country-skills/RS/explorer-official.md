# RS Explorer Official - Serbia Datacenter Enumeration via CEOP Permits, RATEL, Energy, Cloud Regions, Procurement, and Local Environmental Records

Date: 2026-08-12. Country: **RS Serbia**. Division model from `world-manifest.jsonl`: **city / district / autonomous province**: Belgrade, Macva, Kolubara, Podunavlje, Branicevo, Sumadija, Pomoravlje, Bor, Zajecar, Zlatibor, Moravica, Raska, Rasina, Nisava, Toplica, Pirot, Jablanica, Pcinja, Kosovo-Metohija, Vojvodina. Angle: official/regulatory/cloud-first enumeration of operational, under-construction, and planned datacenter facilities.

Reliability grades:
- **A** = official / primary: CEOP/APR construction document, city/municipal permit or environmental decision, RATEL data-center record, EMS/EDS/AERS grid document, official procurement notice/award, official cloud-provider region page, official operator page.
- **B** = strong secondary: DataCenterDynamics, trade press, Uptime Institute, UNDP procurement, contractor case study, official association material that does not itself prove facility address/status.
- **C** = weak lead: directories, marketplace listings, generic hosting pages, old forum/news items, unverified capacity claims.

---

## 0. Serbia-specific structural facts

- Serbia has an unusually useful telecom-regulator lead source: **RATEL publishes a "List of Data Centers"** under its notification page for electronic communications activities. It is not a complete datacenter permit registry, but it is the first pass for commercial colocation/telecom facilities. Source: https://www.ratel.rs/en/obavestenje-o-obavljanju-delatnosti-elektronskix-komunikacija and linked `List of Data Centers` document. **Grade A**.
- Construction permitting runs through **CEOP / Centralna evidencija objedinjene procedure**, maintained by APR. The public portal is https://ceop.apr.gov.rs/eregistrationportal/public/home . Belgrade's city page also states that unified-procedure applications are submitted electronically through CEOP. Sources: https://www.beograd.rs/lat/usluge/a108977/Urbanizam-i-izgradnja.html and https://www.beograd.rs/lat/gradska-uprava/a88214/Sekretarijat-za-urbanizam-i-gradjevinske-poslove.html . **Grade A for process and documents**.
- The official construction lifecycle is usually: `informacija o lokaciji` / `lokacijski uslovi` < `građevinska dozvola` / `rešenje o odobrenju izvođenja radova` < `prijava radova` < `upotrebna dozvola`. In Cyrillic: `локацијски услови`, `грађевинска дозвола`, `решење о одобрењу извођења радова`, `пријава радова`, `употребна дозвола`.
- Environmental discovery is decentralized. Search the national Ministry of Environmental Protection site plus city/municipal `procena uticaja` pages. Datacenters often appear via backup generators, fuel tanks, chillers, radio base stations on the site, and EIA-screening notices. Example: Kragujevac city published notices for A1 Serbia at a "Data centar" location and for Telekom Srbija base station `KG - Data centar`. Source examples: https://kragujevac.ls.gov.rs/tekst/sr/46520/ and https://kragujevac.ls.gov.rs/tekst/sr/89460/ . **Grade A when official page/PDF names the site**.
- Public-sector datacenters are central in Serbia. The Office for IT and eGovernment operates the government datacenter campus in Kragujevac and first state data center in Belgrade. Sources: https://www.ite.gov.rs/tekst/en/34/government-data-centre-in-kragujevac.php , https://www.ite.gov.rs/tekst/en/1134/government-data-centre.php , https://www.ite.gov.rs/vest/en/190/first-government-data-centre-opens.php . **Grade A**.
- Cloud-region checking is not optional. Oracle now lists **Serbia Central (Jovanovac), region identifier `eu-jovanovac-1`, location Jovanovac, Serbia, realm OC20, 1 availability domain** in official OCI regions documentation. Source: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm . Treat the cloud region as **Grade A for logical cloud region presence**, then tie physical facility attribution to Office for IT/eGovernment, Oracle, and permit records separately.
- Kosovo-Metohija appears as a division in the manifest, but public sources normally treat facilities in Pristina/Fushe Kosove as Kosovo. Keep the manifest division for output compatibility, and note jurisdiction/source naming explicitly.

Strong facility evidence:

```text
RATEL List of Data Centers entry
CEOP lokacijski uslovi / građevinska dozvola / upotrebna dozvola naming data center or operator
city environmental EIA notice naming "data centar" or the operator at a known data-center parcel
official operator facility page with address and service scope
official cloud-provider region page plus operator/government confirmation of host facility
official public procurement / UNDP notice for datacenter design, construction, equipment, expansion
```

Status rule:
- **Planned**: MoU, feasibility study, land/urban-plan action, procurement planning, UNDP advisory/design tender, or announced expansion without construction permit.
- **Approved**: CEOP building permit, environmental decision, signed public procurement/construction contract, or official government approval naming scope.
- **Construction**: start-of-works notice, construction contract award, official groundbreaking, or operator/government statement that works are underway.
- **Operational**: RATEL list, official operator service page, official launch, use permit, official cloud-region availability, or official government page describing live service.

---

## 1. Serbian and English query patterns

Search Serbian in both Latin and Cyrillic. Use ASCII fallbacks because many portals omit diacritics.

### 1.1 Core Serbian terms

```text
data centar / data-centar
дата центар / дата-центар
centar podataka / центар података
državni data centar / државни дата центар
računarski centar / рачунарски центар
serverska sala / серверска сала
server sala / сервер сала
kolokacija / колокација
telehousing / server housing
cloud / klaud / клауд
ICT infrastruktura / IKT infrastruktura / ИКТ инфраструктура
superkompjuter / суперкомпјутер
veštačka inteligencija data centar / AI data centar
rezervni data centar / disaster recovery centar
katastarska parcela / KP / k.p. / катастарска парцела
trafostanica / transformatorska stanica / трафостаница
priključenje na elektroenergetsku mrežu / priključenje objekta
uslovi za projektovanje i priključenje
UPS / agregat / dizel agregat / rashladni sistem
procena uticaja na životnu sredinu
```

### 1.2 Construction, CEOP, and planning templates

Substitute `{district}`, `{city}`, `{municipality}`, `{operator}`, `{legal_entity}`, `{address}`, `{parcel}`.

```text
site:ceop.apr.gov.rs "data centar" "{city}"
site:ceop.apr.gov.rs "дата центар" "{city}"
site:ceop.apr.gov.rs "građevinska dozvola" "data centar"
site:ceop.apr.gov.rs "lokacijski uslovi" "data centar"
site:ceop.apr.gov.rs "upotrebna dozvola" "data centar"
site:ceop.apr.gov.rs "{operator}" "građevinska dozvola"
site:ceop.apr.gov.rs "{address}" "{city}"
"data centar" "{city}" "građevinska dozvola"
"data centar" "{city}" "lokacijski uslovi"
"data centar" "{city}" "upotrebna dozvola"
"data centar" "{municipality}" "urbanistički projekat"
"дата центар" "{city}" "грађевинска дозвола"
"дата центар" "{city}" "локацијски услови"
"серверска сала" "{city}" "грађевинска дозвола"
filetype:pdf "data centar" "građevinska dozvola" "{city}"
filetype:pdf "дата центар" "грађевинска дозвола" "{city}"
```

Local-government examples:

```text
site:beograd.rs "data centar" "procena uticaja"
site:beograd.rs "data centar" "urbanizam"
site:kragujevac.ls.gov.rs "data centar"
site:novisad.rs "data centar" OR "дата центар"
site:subotica.ls.gov.rs "data centar"
site:nis.rs "data centar" OR "серверска сала"
site:bor.rs "data centar" "građevinska dozvola"
site:uzice.rs "data centar" "lokacijski uslovi"
```

### 1.3 Environmental, energy, procurement, and regulator templates

```text
site:ekologija.gov.rs "data centar"
site:ekologija.gov.rs "дата центар"
"data centar" "procena uticaja na životnu sredinu" "{city}"
"data centar" "odlučivanje o potrebi procene uticaja" "{city}"
"dizel agregat" "data centar" "{city}"
"trafostanica" "data centar" "{city}"
site:ems.rs "data centar" OR "priključenje objekta"
site:eds.rs "data centar" OR "priključenje"
site:aers.rs "procedura za priključenje objekta" "prenosni sistem"
site:jnportal.ujn.gov.rs "data centar"
site:jnportal.ujn.gov.rs "дата центар"
site:ite.gov.rs "data centar" "javna nabavka"
site:undp.org/serbia "Government Data Center" "Kragujevac"
site:ratel.rs "List of Data Centers"
site:ratel.rs "data centar" "{operator}"
site:registar.ratel.rs "{operator}" "elektronske komunikacije"
```

### 1.4 English templates

```text
"Serbia" "data center" "building permit"
"Serbia" "data centre" "construction permit"
"Belgrade" "data center" "building permit"
"Kragujevac" "data center" "expansion" "MW"
"Serbia" "data center" "grid connection"
"Serbia" "data center" "environmental impact assessment"
"Serbia" "data center" "RATEL"
"Oracle Cloud" "Serbia Central" "eu-jovanovac-1"
"AWS" "Serbia" "Local Zone" site:aws.amazon.com
"Azure" "Serbia" "region" site:learn.microsoft.com
"Google Cloud" "Serbia" "region" site:cloud.google.com
"Serbia" "data center association" "DCAS"
```

---

## 2. Grade A official / regulatory source backbone

### 2.1 Construction permits and urban planning: CEOP/APR plus cities

Primary sources:

- CEOP public portal: https://ceop.apr.gov.rs/eregistrationportal/public/home . **Grade A** when a public CEOP record or attached document names the applicant, parcel, and project.
- Ministry of Construction, Transport and Infrastructure: https://www.mgsi.gov.rs/ . Use for sector ownership and planning/construction regulatory context. **Grade A process source**.
- Belgrade urbanism and construction pages: https://www.beograd.rs/lat/usluge/a108977/Urbanizam-i-izgradnja.html and https://www.beograd.rs/lat/gradska-uprava/a88214/Sekretarijat-za-urbanizam-i-gradjevinske-poslove.html . Belgrade says unified-procedure requests are submitted only electronically through CEOP. **Grade A process/source route**.
- City/municipality pages for urban plans, `urbanistički projekat`, construction notices, environmental notices, and public-inspection material. **Grade A** when official.

Fields to extract from CEOP/local permit records:

- issuing authority, procedure type, case/document number, date;
- applicant/investor (`investitor`, `nosilac projekta`, `podnosilac zahteva`);
- work title and function;
- address, cadastral municipality (`KO`), cadastral parcel (`katastarska parcela`, `k.p.`, `KP`);
- building category/classification if present;
- references to `trafostanica`, `agregat`, `UPS`, cooling, fuel tank, optical route, security fence, access roads;
- permit status and whether the record is `lokacijski uslovi`, `građevinska dozvola`, `rešenje o odobrenju izvođenja radova`, or `upotrebna dozvola`.

Do not require exact words `data centar`. Real records may say `IKT infrastruktura`, `računarski centar`, `serverska sala`, `tehnički objekat`, `telekomunikacioni objekat`, `centar za obradu podataka`, `objekat elektronskih komunikacija`, or only name the operator and a transformer/generator scope.

### 2.2 Environmental records

Primary routes:

- Ministry of Environmental Protection: https://www.ekologija.gov.rs/ . Example official item: the ministry reported the opening of the green data center in Vrsac and described lower cooling-energy use for `Zeleni data centar`. **Grade A/B: official event source; use operator/permit records for facility details**.
- City/municipal environmental protection pages, especially pages headed `Obaveštenje o postupku odlučivanja o potrebi procene uticaja na životnu sredinu` or `Zahtev za odlučivanje o potrebi procene uticaja`. Kragujevac examples explicitly name A1 Serbia at `Data centar` and Telekom Srbija `KG - Data centar`. **Grade A**.
- Belgrade `gradski oglasi i konkursi` and static PDFs under `static.beograd.rs/Binary/...` are useful for EIA-screening applications by telecom operators and infrastructure owners. **Grade A** when official.

What environmental records can reveal:

- project owner and exact site/parcel;
- diesel generator count/power and fuel storage;
- radio base stations or telecom towers on datacenter roofs;
- cooling/HVAC and noise controls;
- whether EIA study is required or waived;
- public-comment period and decision date.

Search with operator names from RATEL plus site names:

```text
"A1 Srbija" "Data centar" "procena uticaja"
"Telekom Srbija" "Data centar" "procena uticaja"
"CETIN" "data centar" "Zabrežje" OR "Obrenovac"
"Yettel" "data centar" "Omladinskih brigada"
"SBB" "Telepark" "procena uticaja"
"Orion Telekom" "Mala pruga" "građevinska dozvola"
```

### 2.3 Energy and grid

Primary sources:

- Elektromreža Srbije / EMS transmission connection page: https://ems.rs/en/connection-to-the-transmission-grid/ . EMS states the legal framework for connecting facilities to Serbia's transmission system and references the Energy Law, Planning and Construction Law, and electricity delivery/supply decree. **Grade A process source**.
- Energy Agency of the Republic of Serbia / AERS: https://www.aers.rs/ . Search for `Saglasnosti na proceduru za priključenje objekta na prenosni sistem` and development-plan approvals. AERS has public material on approval of the EMS transmission-system development plan for 2025-2034 and investment plan for 2025-2029. **Grade A process/planning source**.
- Elektrodistribucija Srbije / EDS: use the official distribution operator for medium/low-voltage connection process and local network context. **Grade A process/source; public project-name yield varies**.
- EPS / Elektroprivreda Srbije: useful for large-load and public-sector energy context. Trade press reported EPS joining Serbia's Data Center Association in 2026; treat association/trade confirmation as **B** unless EPS publishes it directly.

Use energy sources to support capacity and location, not to create standalone datacenter records unless the document names the datacenter. Capture:

- `requested_connection_MW`, `installed_power_MW`, voltage level, substation, DSO/TSO, connection study/contract status;
- whether the project is a datacenter load, generation/BESS project, or mixed industrial project;
- separate facility status from power-infrastructure status.

High-yield energy queries:

```text
"data centar" "MW" "Kragujevac"
"data centar" "trafostanica" "Kragujevac"
"data centar" "priključenje" "Elektromreža Srbije"
"data centar" "priključenje" "Elektrodistribucija Srbije"
"eu-jovanovac-1" "Jovanovac" "trafostanica"
"data centar" "instalisana snaga" "Srbija"
```

### 2.4 Public procurement and development-finance sources

Primary sources:

- Serbian Public Procurement Portal / Portal javnih nabavki: https://jnportal.ujn.gov.rs/ . **Grade A** for public tender notices, awards, plans, and contract changes.
- Office for IT and eGovernment procurement page: https://www.ite.gov.rs/tekst/sr/3214/javne-nabavke-.php . It has historical entries such as `IKT infrastruktura za državni Data centar`. **Grade A**.
- UNDP Serbia procurement: https://www.undp.org/serbia/procurement . UNDP has published procurement/advisory items for further expansion of the Government Data Center in Kragujevac, Phase III modules. **B/A depending on whether UNDP is the contracting route or only development support**.
- TED: https://ted.europa.eu/ . Use when Serbian public tenders are EU-noticed or easier to search in English. **Grade A/B**.

Procurement terms:

```text
"data centar"
"дата центар"
"IKT infrastruktura za državni Data centar"
"oprema za Data Centar"
"projektovanje" "data centar"
"izvođenje radova" "data centar"
"rekonstrukcija serverske sale"
"rezervni data centar"
"disaster recovery centar"
"superkompjuter" "Kragujevac"
"Government Data Center" "Kragujevac" "Modules"
```

### 2.5 RATEL regulator pipeline

Primary sources:

- RATEL main site: https://www.ratel.rs/ . **Grade A telecom regulator**.
- RATEL notification page with Data Center Records: https://www.ratel.rs/en/obavestenje-o-obavljanju-delatnosti-elektronskix-komunikacija . It says the regulator recognized the need for one-place information on existing data centers and compiled submitted operator data in a table. **Grade A for submitted data-center entries**.
- RATEL electronic communications operator registry: https://registar.ratel.rs/ and English operator page https://ratel.itcentar.rs/en/page/operators-of-electronic-communications . **Grade A for operator registration/services; not facility proof by itself**.
- RATEL broadband geography page: https://www.ratel.rs/en/geografski-pregled-rasprostranjenosti-sirokopojasnix-mreza . It is useful for network/fiber context and future broadband expansion; not a datacenter registry. **Grade A context**.
- RATEL infrastructure sharing page: https://www.ratel.rs/en/infrastruktura-za-zajednicko-koriscenje . Use for shared telecom-infrastructure routes around candidate sites. **Grade A context**.

RATEL list entries observed from the official linked document dated 2024-11-25:

| Operator/legal entity | Data-center location | Division | Use |
| --- | --- | --- | --- |
| Yettel d.o.o. Beograd | Omladinskih Brigada 92, Novi Beograd | Belgrade | Grade A lead; pivot to Yettel/CETIN pages and CEOP/environment records. |
| Beotelnet-ISP d.o.o. Beograd | Bulevar Vojvode Misica 37, Beograd | Belgrade | Grade A lead; verify current service page and facility scope. |
| Sat-Trakt d.o.o. Backa Topola | Jozefa Atile 132, Becej | Vojvodina | Grade A lead; pivot to Sat-Trakt colocation page and Becej municipality records. |
| Orion Telekom d.o.o. Beograd | Naselje Zemun Polje, Mala pruga 8 | Belgrade | Grade A lead; pivot to operator page, Schneider/Enel-PS case studies, CEOP. |
| A1 Srbija d.o.o. | Milutina Milankovica 1z, Novi Beograd | Belgrade | Grade A lead; pivot to A1 data-center page and environmental files. |
| Telekom Srbija a.d. | Katiceva 14-18 Belgrade; Darinke Radovic bb Belgrade; Atinska 1 Kragujevac | Belgrade, Sumadija | Grade A multi-site lead; separate physical records. |
| SBB Beograd | Bulevar Peka Dapcevica 19, Beograd | Belgrade | Grade A lead; pivot to Telepark/SBB cloud telehousing page. |
| Conexio d.o.o. Beograd | Milutina Milankovica 1i, Novi Beograd | Belgrade | Grade A lead; verify if independent facility, in-building suite, or operator node. |
| HiTeam d.o.o. | Beogradski put bb, Vrsac | Vojvodina | Grade A lead; official note identifies `ZELENDATA CENTAR`, first green data center in Serbia. |

RATEL query templates:

```text
site:ratel.rs "DATA centri_tabela"
site:ratel.rs "Data Center Records"
site:ratel.rs "data center" "operator"
site:registar.ratel.rs "YETTEL" "data centar"
site:registar.ratel.rs "A1 SRBIJA" "elektronske komunikacije"
site:registar.ratel.rs "TELEKOM SRBIJA" "kolokacija"
```

### 2.6 Cloud-region and interconnect checks

Cloud sources prove cloud geography or edge service availability. They do not always identify the physical colocation site.

| Provider | Official source | Serbia signal as of 2026-08-12 | Enumeration use |
| --- | --- | --- | --- |
| Oracle Cloud Infrastructure | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | **Serbia Central (Jovanovac), `eu-jovanovac-1`, Jovanovac, Serbia, region key BEG, realm OC20, 1 AD**. | Grade A for OCI region. Cross-check Office for IT/eGovernment, Kragujevac/Jovanovac CEOP, AERS/EMS, and Data Cloud Technology/Oracle announcements for physical host. |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No Serbia Region or Belgrade Local Zone visible in official region/local-zone pages checked; AWS Local Zones list nearby Athens/Istanbul etc., not Belgrade. | Use official pages to reject false Serbia-region claims; search AWS Direct Connect separately if needed. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Serbia public Azure region in official Azure regions list checked. | Use as negative control; do not count Microsoft Serbia office/availability as a datacenter. |
| Google Cloud | https://cloud.google.com/about/locations | No Serbia cloud region in official Google Cloud locations list checked. | Use as negative control; customer case studies in Serbia are not facility evidence. |
| Cloudflare/Akamai/Fastly/CDN/IX | official network maps and SOX/peering pages | Likely Belgrade edge/peering leads; verify provider page and PeeringDB/SOX. | Edge PoP is not a full datacenter unless tied to facility/operator. |

OCI caution: The official OCI documentation now names Jovanovac. The older Serbian government/commercial narrative often says Kragujevac government datacenter. Treat `Jovanovac/Kragujevac/Sumadija` as a cluster and verify exact parcel/facility before assigning a physical address.

---

## 3. Operator, association, and trade-press backbone

Official/operator pages:

- Office for IT and eGovernment government datacenter pages: https://www.ite.gov.rs/tekst/en/34/government-data-centre-in-kragujevac.php and https://www.ite.gov.rs/tekst/en/1134/government-data-centre.php . **Grade A**.
- e& enterprise announcement for Serbian Office for IT/eGovernment MoU: https://www.eand.com/en/news/17-sep-2025-eand-enterprise-and-serbias-office-and-egovernment-ink-landmark-deal.html and https://www.eandenterprise.com/en/press-release/eandenterprise-inks-landmark-deal-to-triple-serbias-data-center-capacity.html . It says the existing Tier-4 campus has 14 MW and 1,080 racks, with land secured for up to 40 MW expansion. **Grade A for operator/partner announcement; planned until permits/contracts prove construction**.
- CETIN/Yettel data-center services: https://www.cetin.rs/services/data-center and https://www.yettel.rs/sr/biznis/resenja/veleprodajne-usluge/yettel-data-centar/ . **Grade A** for operator service/location claims.
- A1 Serbia data center page: https://a1.rs/poslovni/poslovna_resenja/it_infrastructure/data_centar . **Grade A**.
- Telekom Srbija / MTS data-center services: https://mts.rs/Poslovni/Digital/Data-centar and https://www.telekom.rs/ . **Grade A for service existence; capacity/address needs RATEL/permits/directories**.
- SBB Telehousing / Cloud: https://poslovni.sbb.rs/sbb-cloud/telehousing/ . **Grade A**.
- Orion Telekom: https://oriontelekom.rs/ . **Grade A for operator; facility details often require RATEL/directories/case studies**.
- ZELEN DATA CENTAR / HiTeam: http://www.zelendata.rs/ and https://www.hiteam.co.rs/eng/vest/4/data-center-opened-in-vrsac . **Grade A/B**.
- Sat-Trakt colocation: http://www.sattrakt.rs/servisi/kolokacije-rack-and-server-housing/ . **Grade A/B**.
- NiNet/Webglobe Nis: use official NiNet/Webglobe pages first, then directories for capacity. **Grade B/C if only Baxtel/DataCenterMap is available**.
- E-CAPS / NEO Cloud / Neo Data Center Novi Sad: https://e-caps.net/neo-data-center/ . **Grade A** if page is active and names facility.
- BeeNet Vrsac: https://www.beenet.rs/en/data-center . **Grade A**.

Association and trade press:

- Data Centar Asocijacija Srbije / DCAS: search `Data Centar Asocijacija Srbije`, `DCAS`, and `data centri kao temelj digitalne i energetske tranzicije Srbije`. Treat member lists and event reports as **B** leads unless official member/operator pages prove facilities.
- DataCenterDynamics: useful for government center openings, Oracle/OCI, and e& expansion. **Grade B**, unless directly quoting official announcements.
- eKapija, Balkan Green Energy News, Energetski Portal, SeeNews, BIRN: useful for energy, capacity, public debate, procurement red flags, and expansion context. **Grade B/C** depending on sourcing.
- Uptime Institute awards/certifications: useful for Tier/Class evidence, **B** unless paired with owner page.
- Directories such as DataCenterMap, Baxtel, Inflect, datacenters.rs, datacenters.com: **C by default**. Use them for address/capacity leads, then upgrade only with RATEL/operator/permit evidence.

Known anchor inventory to use as seed candidates:

- **Belgrade**: State Data Center Belgrade; Yettel/CETIN Omladinskih Brigada 90/92; A1 Milutina Milankovica 1z; Conexio Milutina Milankovica 1i; Telekom/MTS Katiceva 14-18 and Darinke Radovic bb; SBB Telepark Bulevar Peka Dapcevica 19; Orion Mala pruga 8; Beotelnet Bulevar Vojvode Misica 37; NetCast Milentija Popovica 9; phoenixNAP Belgrade.
- **Sumadija**: Government Data Centre / Data Cloud Technology in Kragujevac/Jovanovac; OCI Serbia Central; e& enterprise planned capacity expansion; municipal City Data Center Kragujevac; Telekom site Atinska 1; A1/Telekom environmental records at `Data centar`.
- **Vojvodina**: ZELEN DATA CENTAR / HiTeam Vrsac; BeeNet RS-2 Vrsac; Sat-Trakt Becej; NEOplanta/Neo Data Center Novi Sad.
- **Nisava**: NiNet Data Center Nis / Webglobe, verify operator source and Nis city records.
- **Kosovo-Metohija**: IPKO data center in Fushe Kosove/Pristina and Telecom of Kosovo leads; label jurisdiction carefully as Kosovo in notes.

---

## 4. Division-by-division enumeration route

Use the same first-pass order for every division:

1. RATEL list/operator pivots for existing telecom/colo sites.
2. CEOP/APR exact phrase and operator/address searches.
3. City/municipal environmental `procena uticaja` pages.
4. Public procurement portal plus local procurement pages.
5. EMS/EDS/AERS grid and substation searches.
6. Trade press/directories only to fill leads and capacities after official pass.

### Belgrade

Priority because most commercial facilities are in Novi Beograd, Zemun, Vozdovac, Savski Venac, and central Belgrade.

Official routes:
- CEOP/APR plus Belgrade city urbanism page: https://www.beograd.rs/lat/gradska-uprava/a88214/Sekretarijat-za-urbanizam-i-gradjevinske-poslove.html .
- Belgrade city environmental notices/PDFs under `beograd.rs` and `static.beograd.rs`.
- RATEL list entries for Yettel, A1, Telekom Srbija, SBB, Orion, Conexio, Beotelnet.

Queries:

```text
site:ceop.apr.gov.rs "data centar" "Beograd"
site:ceop.apr.gov.rs "дата центар" "Београд"
site:beograd.rs "data centar" "procena uticaja"
site:beograd.rs "Omladinskih brigada 92" "data centar"
"Omladinskih Brigada 92" "data centar" "Novi Beograd"
"Milutina Milankovića 1ž" OR "Milutina Milankovica 1z" "data centar"
"Katićeva 14-18" "data centar"
"Bulevar Peka Dapčevića 19" "Telepark"
"Mala pruga 8" "Orion" "data centar"
"Bulevar Vojvode Mišića 37" "Beotelnet" "data centar"
"Milentija Popovića 9" "NetCast" "data centar"
```

### Sumadija

Priority because Kragujevac/Jovanovac is Serbia's government/cloud hub.

Official routes:
- Office for IT/eGovernment pages, Kragujevac city environmental pages, CEOP/APR, Oracle OCI official region list, UNDP procurement, EMS/AERS.
- Search both `Kragujevac` and `Jovanovac`; the OCI region uses Jovanovac while many government pages use Kragujevac.

Queries:

```text
site:ite.gov.rs "Government Data Centre" "Kragujevac"
site:kragujevac.ls.gov.rs "Data centar"
site:kragujevac.ls.gov.rs "data centar" "procena uticaja"
site:ceop.apr.gov.rs "data centar" "Kragujevac"
site:ceop.apr.gov.rs "Jovanovac" "data centar"
"eu-jovanovac-1" OR "Serbia Central" "Jovanovac"
"Atinska 1" "Telekom Srbija" "data centar"
"Save Kovačevića br. 1" "Data centar" "Kragujevac"
"Government Data Center" "Kragujevac" "Modules 5 6 7 8"
site:undp.org/serbia "Government Data Center" "Kragujevac"
```

### Vojvodina

Priority cities/municipalities: Novi Sad, Vrsac, Becej, Backa Topola, Subotica, Zrenjanin, Indjija, Sombor, Kikinda, Sremska Mitrovica, Pancevo.

Official routes:
- RATEL list entries for HiTeam/ZELENDATA and Sat-Trakt.
- Vrsac/Becej/Novi Sad municipal pages, provincial government (`vojvodina.gov.rs`) and planning/environment pages.
- Operator pages: ZELENDATA, BeeNet, Sat-Trakt, E-CAPS/NEO.

Queries:

```text
site:ceop.apr.gov.rs "data centar" "Vršac" OR "Vrsac"
site:ceop.apr.gov.rs "data centar" "Novi Sad"
site:ceop.apr.gov.rs "data centar" "Bečej" OR "Becej"
site:novisad.rs "data centar"
site:vrsac.com "data centar" OR site:vrsac.rs "data centar"
site:vojvodina.gov.rs "data centar"
"Beogradski put bb" "Vršac" "data centar"
"Jozefa Atile 132" "Bečej" "Sat-Trakt"
"NEOplanta" "Novi Sad" "data centar"
"BeeNet" "RS-2" "Vršac"
```

### Nisava

Priority city: Nis. Known lead: NiNet/Webglobe data center.

Queries:

```text
site:ceop.apr.gov.rs "data centar" "Niš" OR "Nis"
site:nis.rs "data centar"
site:nis.rs "serverska sala"
"Bulevar Nemanjića 25" "data centar"
"NiNet" "data center" "Nis"
"Webglobe" "NiNet" "data center"
"Niš" "kolokacija" "data centar"
```

### Macva

Priority municipalities: Sabac, Loznica, Bogatic, Mali Zvornik. No strong known datacenter anchor; use official no-hit protocol.

```text
site:ceop.apr.gov.rs "data centar" "Šabac" OR "Sabac"
site:sabac.rs "data centar" OR "server sala"
site:loznica.rs "data centar"
"data centar" "Mačva" OR "Macva"
"trafostanica" "data centar" "Šabac"
```

### Kolubara

Priority: Valjevo, Ub, Lajkovac, Lazarevac-adjacent energy corridor context.

```text
site:ceop.apr.gov.rs "data centar" "Valjevo"
site:valjevo.rs "data centar" OR "serverska sala"
"data centar" "Kolubara"
"Ub" "data centar" "građevinska dozvola"
"Lajkovac" "data centar" "trafostanica"
```

### Podunavlje

Priority: Smederevo, Smederevska Palanka, Velika Plana; industrial power sites can create false positives.

```text
site:ceop.apr.gov.rs "data centar" "Smederevo"
site:smederevo.org.rs "data centar"
"data centar" "Podunavlje"
"Smederevska Palanka" "serverska sala"
"Velika Plana" "data centar" "procena uticaja"
```

### Branicevo

Priority: Pozarevac, Kostolac, Petrovac na Mlavi. Watch energy-generation false positives.

```text
site:ceop.apr.gov.rs "data centar" "Požarevac" OR "Pozarevac"
site:pozarevac.rs "data centar"
"data centar" "Braničevo" OR "Branicevo"
"Kostolac" "data centar" "priključenje"
```

### Pomoravlje

Priority: Jagodina, Cuprija, Paracin.

```text
site:ceop.apr.gov.rs "data centar" "Jagodina"
site:jagodina.org.rs "data centar"
"Ćuprija" "data centar" OR "Cuprija" "data centar"
"Paraćin" "data centar" OR "Paracin" "data centar"
"Pomoravlje" "data centar"
```

### Bor

Priority: Bor, Kladovo, Majdanpek, Negotin. Strong mining/energy noise; require facility-specific proof.

```text
site:ceop.apr.gov.rs "data centar" "Bor"
site:bor.rs "data centar" "građevinska dozvola"
"data centar" "Bor" "procena uticaja"
"serverska sala" "Bor" "javna nabavka"
```

### Zajecar

Priority: Zajecar, Knjazevac, Sokobanja, Boljevac.

```text
site:ceop.apr.gov.rs "data centar" "Zaječar" OR "Zajecar"
site:zajecar.info "data centar" OR "serverska sala"
"data centar" "Zaječar"
"Knjaževac" "data centar" "građevinska dozvola"
```

### Zlatibor

Priority: Uzice, Cajetina/Zlatibor, Priboj, Prijepolje, Nova Varos. Look for municipal server rooms and tourism/industrial park leads.

```text
site:ceop.apr.gov.rs "data centar" "Užice" OR "Uzice"
site:uzice.rs "data centar" OR "serverska sala"
"Zlatibor" "data centar" "lokacijski uslovi"
"Priboj" "data centar" "industrijska zona"
"Prijepolje" "serverska sala" "javna nabavka"
```

### Moravica

Priority: Cacak, Gornji Milanovac, Ivanjica. Mainly official no-hit unless operator/procurement surfaces.

```text
site:ceop.apr.gov.rs "data centar" "Čačak" OR "Cacak"
site:cacak.org.rs "data centar"
"Moravica" "data centar"
"Gornji Milanovac" "serverska sala"
```

### Raska

Priority: Kraljevo, Novi Pazar, Raska. Watch telecom and municipal IT procurements.

```text
site:ceop.apr.gov.rs "data centar" "Kraljevo"
site:kraljevo.rs "data centar" OR "serverska sala"
"Novi Pazar" "data centar"
"Raška" "data centar" "građevinska dozvola"
```

### Rasina

Priority: Krusevac, Trstenik, Aleksandrovac.

```text
site:ceop.apr.gov.rs "data centar" "Kruševac" OR "Krusevac"
site:krusevac.ls.gov.rs "data centar"
"Rasina" "data centar"
"Trstenik" "serverska sala" "javna nabavka"
```

### Toplica

Priority: Prokuplje, Kursumlija, Blace. Likely low yield; use no-hit protocol.

```text
site:ceop.apr.gov.rs "data centar" "Prokuplje"
site:prokuplje.org.rs "data centar"
"Toplica" "data centar"
"Kuršumlija" "serverska sala"
```

### Pirot

Priority: Pirot, Dimitrovgrad. Industrial/free-zone leads need careful proof.

```text
site:ceop.apr.gov.rs "data centar" "Pirot"
site:pirot.rs "data centar" OR "serverska sala"
"Slobodna zona Pirot" "data centar"
"Dimitrovgrad" "data centar" "građevinska dozvola"
```

### Jablanica

Priority: Leskovac, Vlasotince, Lebane.

```text
site:ceop.apr.gov.rs "data centar" "Leskovac"
site:gradleskovac.org "data centar"
"Jablanica" "data centar"
"Vlasotince" "serverska sala"
```

### Pcinja

Priority: Vranje, Bujanovac, Presevo.

```text
site:ceop.apr.gov.rs "data centar" "Vranje"
site:vranje.org.rs "data centar"
"Pčinja" "data centar" OR "Pcinja" "data centar"
"Bujanovac" "data centar" "procena uticaja"
```

### Kosovo-Metohija

Keep output under the manifest division but note that most sources identify the jurisdiction as Kosovo. Search Serbian, Albanian, and English.

```text
"IPKO" "data center" "Fushë Kosovë" OR "Fushe Kosove"
"IPKO" "server colocation" "Pristina"
"Telecom of Kosovo" "data center" "Pristina"
"data center" "Kosovo" "building permit"
"qendër e të dhënave" "Prishtinë"
"server colocation" "Kosovo"
```

Grade official operator pages **A** for facility/service claims; directories **C**.

---

## 5. Cross-check workflow

For each candidate:

1. Start with RATEL/operator/cloud/procurement lead and normalize legal entity, address, division, and Serbian spellings.
2. Search CEOP/APR by exact address, legal entity, city, and `data centar`/`дата центар`; record case type and document numbers.
3. Search city/municipal environmental pages by legal entity and address; extract EIA decision dates, generator/cooling clues, and parcel IDs.
4. Search EMS/EDS/AERS by operator, city, substation, and `priključenje`; only record power facts when tied to the facility.
5. Search public procurement by exact project title and variants; public-sector facilities often appear through equipment, design, modules, supercomputer, or expansion contracts.
6. Use directories/trade press for missing power, rack, area, and launch dates; keep those fields with lower grade unless official corroboration exists.
7. De-duplicate colocated or same-building entries: Omladinskih Brigada 90/92 may show as Yettel/CETIN/phoenixNAP or interconnection hub; Milutina Milankovica buildings may have several operator suites; Telekom has multiple sites.

Minimum record fields:

```text
name
division
city/municipality
address
operator/developer/legal_entity
status
facility_type: government / cloud region / colo / telecom / enterprise / HPC / DR
capacity_mw
racks
area_sqm
permit_refs
environment_refs
energy_refs
cloud_refs
source_urls
evidence_grade
notes_on_uncertainty
```

Red flags:

- `data centar` can mean a small server room, network node, or application/data portal; require facility/infrastructure evidence.
- Telecom base-station environmental notices on an existing data-center site prove the site exists but may not prove new datacenter construction.
- Cloud billing/customer availability in Serbia is not a physical region. Count only official region/zone/location pages.
- Grid connection for renewable generation or industrial loads is not datacenter evidence unless the datacenter is explicitly named.
- Do not merge the state-owned Kragujevac/Jovanovac campus, OCI logical region, Data Cloud Technology legal/commercial entity, and future e& expansion unless sources prove they are the same physical block.
- Directory capacities for older Belgrade colo sites vary; grade capacity separately from facility existence.

---

## 6. Recommended source priority for Serbia runs

1. RATEL data-center list and operator pages for existing commercial/telecom colo sites.
2. Office for IT and eGovernment plus OCI official region docs for Kragujevac/Jovanovac/state cloud.
3. CEOP/APR and local urbanism pages for permit status and parcels.
4. Local environmental pages (`procena uticaja`) for generators, site details, and current activity.
5. JN portal, Office for IT procurement page, UNDP Serbia, and TED for public-sector expansions/equipment.
6. EMS/EDS/AERS for power and grid corroboration.
7. DCAS, eKapija, DCD, SeeNews, Balkan Green Energy News, Energetski Portal, Uptime, and directories for leads and missing specifications.

