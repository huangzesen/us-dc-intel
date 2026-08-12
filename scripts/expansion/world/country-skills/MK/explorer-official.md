# MK Explorer Official - North Macedonia Datacenter Enumeration via Permits, Energy, Telecom Regulator, Cloud, and Public Procurement

Date: 2026-08-12. Country: **MK North Macedonia**. Division model: **80 municipalities**. Angle: **official/regulatory methodology** for finding commercial, government, telecom, cloud, colocation, and disaster-recovery data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: e-building permit record, municipal urban-planning file, Official Gazette law text, ministry/government/EU project record, AEK/AEC operator record, ERC/MEPSO/EVN power source, public-procurement notice, official cloud-provider region page, operator-owned facility page.
- **B** = strong secondary source: MIA/SeeNews/CORD/BalkanEngineer report, Energy Community/EBRD/World Bank/ITU profile, Uptime/PeeringDB/interconnection record, vendor case study with identifiable site.
- **C** = weak lead: aggregator directory, social post, job ad, market note, investment-promotion page without a named facility, or unverified street/municipality assignment.

---

## 0. North Macedonia structure facts

- North Macedonia has **no public national datacenter registry**. Enumeration must join e-building permits, municipal urban plans, environmental/procurement records, AEK telecom operator evidence, energy-grid evidence, official cloud-region checks, and operator pages.
- Building control is municipal in practice, but new data-centre policy is now nationally relevant. In June 2026, amendments to the **Law on Construction** and **Law on Urban Planning** were reported as published in Official Gazette No. 134 dated 2026-06-18, explicitly recognizing facilities for storage and processing of digital data as a distinct facility type. Use the Official Gazette/legal text where available; BDK Advokati, MIA, SeeNews, CORD, and BalkanEngineer are useful leads, not substitutes for the Gazette.
- The national electronic building-permit system is **E-Odobrenie za gradenje / e-building permits**: https://www.gradezna-dozvola.mk/. The landing page states it is the information system for e-approval for construction. It is account-oriented, so public enumeration often needs municipal web-indexed decisions, permit notices, or applicant/operator names.
- The main data-centre geography is **Skopje**, especially **Aerodrom, Gazi Baba, Centar, Karpos** and nearby industrial/telecom addresses. Secondary official-confirmed or plausible municipalities are **Veles**, **Stip**, **Makedonska Kamenica**, **Prilep**, **Kavadarci** as a rejected/candidate BCDR scenario, and **Kriva Palanka/Deve Bair** as an aggregator/job-ad lead requiring primary confirmation.
- Use English, Macedonian Cyrillic, and Macedonian Latin transliteration. Albanian can matter in Tetovo/Gostivar/Skopje-area municipalities but is rarely necessary for datacenter-specific records.

---

## 1. Macedonian and English search vocabulary

Core terms:

```text
data center
data centre
datacenter
colocation
co-location
cloud
cloud region
server room
server farm
disaster recovery
business continuity
Tier III
Uptime
MW
MVA
substation
transformer station
backup generator
```

Macedonian Cyrillic terms:

```text
дата центар
дата центри
центар за податоци
центри за податоци
центар за обработка на податоци
складирање и обработка на дигитални податоци
серверска сала
серверска просторија
колокација
облак
клауд
дигитална инфраструктура
деловен континуитет
обнова од катастрофи
резервен дата центар
одобрение за градење
градежна дозвола
урбанистички план
детален урбанистички план
градежна парцела
трафостаница
приклучок на електродистрибутивна мрежа
приклучување на електроенергетска мрежа
агрегат
јавна набавка
```

Latin transliteration variants:

```text
data centar
data centri
centar za podatoci
server sala
server prostorija
odobrenie za gradenje
gradezna dozvola
urbanisticki plan
detalen urbanisticki plan
trafostanica
priklucok
javna nabavka
```

Albanian secondary terms:

```text
qender te dhenash
qendra e te dhenave
dhoma e servereve
leje ndertimi
plan urbanistik
nensatcion
```

---

## 2. Official permit, planning, and legal sources

### 2.1 E-building permits and municipal planning

Primary source:

- **E-Odobrenie za gradenje / e-building permit system**: https://www.gradezna-dozvola.mk/. Grade **A** for workflow and any permit/approval record obtained from it.
- User/institution instructions hosted by the system include PDF guidance under `https://www.gradezna-dozvola.mk/Documents/`, useful for terminology and process vocabulary.
- State Statistical Office issued-building-permit series: https://www.stat.mk/en/stat/industry-energy-and-environment/construction/issued-building-permits/ and monthly notices such as `prikazisoopstenie_en.aspx?rbrtxt=50`. Grade **A for aggregate construction statistics only**, not facility enumeration.

Permit queries:

```text
site:gradezna-dozvola.mk "дата центар"
site:gradezna-dozvola.mk "центар за податоци"
site:gradezna-dozvola.mk "серверска сала"
site:gradezna-dozvola.mk "{operator}"
"{municipality}" "дата центар" "одобрение за градење"
"{municipality}" "центар за податоци" "градежна дозвола"
"{municipality}" "серверска сала" "одобрение за градење"
"{operator}" "одобрение за градење" "Скопје"
"{address}" "одобрение за градење" "дата центар"
filetype:pdf "дата центар" "одобрение за градење"
filetype:pdf "центар за податоци" "градежна дозвола"
```

Municipal planning queries:

```text
site:{municipality-domain} "дата центар"
site:{municipality-domain} "центар за податоци"
site:{municipality-domain} "серверска сала"
site:{municipality-domain} "урбанистички план" "дата центар"
site:{municipality-domain} "детален урбанистички план" "{operator OR street}"
site:{municipality-domain} "градежна парцела" "центар за податоци"
"Општина {municipality}" "дата центар"
"Општина {municipality}" "серверска сала"
"Совет на Општина {municipality}" "дата центар"
```

Extract from permit/planning documents: municipality, cadastral municipality, plot/parcel, address/street, investor/proponent/SPV, facility category, data-centre wording under the 2026 law, floorspace, rack count, power demand, transformer/substation, generators/fuel, cooling, water demand, permit date, appeal/use permit, construction-stage terms.

### 2.2 2026 legal change for data centers

Primary/near-primary sources:

- Official Gazette portal should be checked for **Official Gazette of the Republic of North Macedonia No. 134, 2026-06-18**, amendments to the Law on Construction and Law on Urban Planning. Grade **A** when Gazette text is retrieved.
- MIA report: https://mia.mk/index.php/en/story/new-legislation-opens-way-for-stateowned-and-private-data-centers-says-deputy-pm. Grade **B**; confirms that new legislation filled a legal gap and that the government is considering a state-owned data center.
- SeeNews report: https://seenews.com/news/north-macedonia-plans-regulatory-shift-to-pave-way-for-data-centres-1295318. Grade **B**; lead for pre-adoption policy shift.
- BDK Advokati legal note: https://bdkadvokati.com/legislative-amendments-facilitating-development-of-data-centers-in-the-republic-of-north-macedonia. Grade **B**; useful summary of Gazette No. 134.

Legal/policy queries:

```text
"Службен весник" "134" "2026" "дата центар"
"Закон за градење" "дата центар"
"Закон за урбанистичко планирање" "дата центар"
"складирање и обработка на дигитални податоци" "Службен весник"
"data centers" "Official Gazette" "North Macedonia" "134" "2026"
site:mia.mk "data centers" "urban planning" "construction"
site:seenews.com "North Macedonia" "data centres" "construction"
```

Use this law change to improve future project searches after 2026-06-18. Older facilities may be described as telecom/technical/commercial buildings rather than `дата центар`.

### 2.3 Environment and spatial documents

North Macedonia environmental records are fragmented across ministry pages, project portals, municipal notices, EU/IFI documents, and PDFs. Use environmental evidence mainly for large greenfield campuses, major substations, generator/fuel storage, industrial-zone projects, and public-sector facilities.

Sources and routes:

- Ministry of Digital Transformation portal document host: https://portal.mdt.gov.mk/ can host IPA annual implementation and technical reports. Grade **A/B** depending on document owner.
- ENER public document register: https://ener.gov.mk/ often hosts draft strategies and laws. Grade **A for government consultation documents**, not facility operation.
- EU projects map: https://euprojects.mk/. Grade **A/B** for EU-funded government projects and contract/procurement leads.
- EU Enlargement IPA pages: https://enlargement.ec.europa.eu/funding-technical-assistance/overview-instrument-pre-accession-assistance/north-macedonia-financial-assistance-under-ipa_en. Grade **A** for EU programme documents.

Queries:

```text
site:ener.gov.mk "дата центар"
site:ener.gov.mk "центар за податоци"
site:portal.mdt.gov.mk "data centre"
site:portal.mdt.gov.mk "дата центар"
site:euprojects.mk "data centre" "North Macedonia"
site:euprojects.mk "Business Continuity and Disaster Recovery Data Centre"
site:enlargement.ec.europa.eu "North Macedonia" "data centre" "IPA"
"{operator}" "Environmental" "North Macedonia" "data center"
"{municipality}" "дата центар" "животна средина"
"{municipality}" "серверска сала" "агрегат"
```

### 2.4 Public procurement

Primary sources:

- Electronic System for Public Procurement (**ESJN/ЕСЈН**): https://www.e-nabavki.gov.mk/PublicAccess/Home.aspx. Grade **A** for notices, tenders, awards, and dossiers.
- Bureau of Public Procurement: https://www.bjn.gov.mk/. Grade **A** for procurement-system route.
- Ministry of Digital Transformation public procurement: https://mdt.gov.mk/en-GB/klucni-aktivnosti/javni-nabavki. Grade **A** for ministry-specific plans/contracts.
- TED/OP EU procurement details can surface North Macedonia public tenders, e.g. "Data center IT equipment" for the Assembly: https://op.europa.eu/en/web/public-procurement/. Grade **A/B** depending on whether linked to domestic tender.

Procurement queries:

```text
site:e-nabavki.gov.mk "дата центар"
site:e-nabavki.gov.mk "центар за податоци"
site:e-nabavki.gov.mk "серверска сала"
site:e-nabavki.gov.mk "disaster recovery"
site:e-nabavki.gov.mk "business continuity"
site:bjn.gov.mk "дата центар"
site:mdt.gov.mk "data center"
site:mdt.gov.mk "дата центар"
site:op.europa.eu "North Macedonia" "Data center IT equipment"
"јавна набавка" "серверска сала" "{municipality}"
"јавна набавка" "дата центар" "{ministry OR municipality}"
```

Procurement can identify public-sector server rooms, government data centres, IT equipment refreshes, design/supervision contracts, and data-centre modernization. Do not count equipment-only tenders as facility evidence unless they identify a physical data centre.

---

## 3. Telecom regulator and ICT authorities

### 3.1 Agency for Electronic Communications (AEK/AEC)

Primary sources:

- AEK English site: https://aek.mk/en/. Grade **A** for regulator identity, market reports, rules, and official publications.
- AEK GIS/infrastructure portal route mentioned in AEK materials: https://e-agencija.aek.mk/AEKGISPortal. Grade **A** for official infrastructure spatial context where accessible.
- AEK documents and presentations under `https://aek.mk/wp-content/uploads/` describe the electronic-communications infrastructure cadastre and WEB GIS Collector for newly constructed electronic communications networks and accompanying facilities.
- ITU Digital Development Country Profile for North Macedonia notes the role of AEK and electronic communications network/accompanying-assets data submission. Grade **B/A** depending on cited official source.

AEK queries:

```text
site:aek.mk "data center"
site:aek.mk "data centre"
site:aek.mk "дата центар"
site:aek.mk "центар за податоци"
site:aek.mk "колокација"
site:aek.mk "List of Notified Entities"
site:aek.mk "notified entities" "Neotel"
site:aek.mk "notified entities" "Telesmart"
site:aek.mk "notified entities" "Interspace"
site:aek.mk "notified entities" "Akton"
site:aek.mk "Macedonian Telecom" "Neotel" "Telesmart"
site:aek.mk "WEB GIS Collector"
site:aek.mk "newly constructed electronic communications network and accompanying"
```

AEK evidence supports operator identity, telecom service authorization, network and fibre context. It does **not** by itself prove a specific data-centre facility or capacity.

### 3.2 Ministry of Digital Transformation and government ICT

Sources:

- Ministry of Digital Transformation: https://mdt.gov.mk/ and document host https://portal.mdt.gov.mk/.
- ENER draft National ICT Strategy 2021-2025 included language about data centres located in secure locations and meeting EN 50600/international standards. Use as **policy context**.
- MIA 2026 report says the government is considering a state-owned data center for institutional protection and cybersecurity. Treat as **planned/policy lead** until procurement/permit appears.

Queries:

```text
site:mdt.gov.mk "data center"
site:mdt.gov.mk "data centre"
site:mdt.gov.mk "дата центар"
site:portal.mdt.gov.mk "Business Continuity and Disaster Recovery Data Centre"
site:ener.gov.mk "Национална Стратегија за ИКТ" "data centres"
site:ener.gov.mk "EN 50600" "data centres"
```

---

## 4. Energy, grid, and utility evidence

Primary sources:

- Energy and Water Services Regulatory Commission (**ERC/RKE**): https://www.erc.org.mk/default_en.aspx. Annual reports: https://www.erc.org.mk/page_en.aspx?id=342. Grade **A** for regulator, licensed energy-sector entities, market statistics, tariffs, and annual reports.
- MEPSO / Macedonian Electricity Transmission System Operator: https://www.mepso.com.mk/. Grade **A** for transmission grid, substations, 10-year development plans, network studies, and connection/transmission projects.
- EVN Macedonia / Elektrodistribucija: https://www.evn.mk/?lang=en-gb and https://elektrodistribucija.mk/About-us.aspx?lang=en-us. Grade **A** for distribution-grid connection route and distribution-company role.
- Ministry of Energy: https://energy.gov.mk/. Grade **A** for policy and public notices.
- Invest North Macedonia energy overview: https://investnorthmacedonia.gov.mk/invest-energy/. Grade **B/A-** for investment-promotion summary; it states EVN handles distribution and MEPSO operates transmission.

Energy queries:

```text
site:erc.org.mk "data center"
site:erc.org.mk "дата центар"
site:mepso.com.mk "data center"
site:mepso.com.mk "дата центар"
site:mepso.com.mk "{municipality}" "трафостаница"
site:mepso.com.mk "{operator}" "MW"
site:evn.mk "data center"
site:evn.mk "дата центар"
site:elektrodistribucija.mk "дата центар"
site:elektrodistribucija.mk "{municipality}" "приклучок"
site:energy.gov.mk "data centers"
"{operator}" "EVN" "data center" "North Macedonia"
"{operator}" "MEPSO" "MW" "North Macedonia"
"{municipality}" "дата центар" "трафостаница"
"{project}" "MVA" "Skopje"
```

Extract: requested/contracted MW or MVA, voltage level, substation/feeder, distribution vs transmission connection, backup-generation details, connection date, local grid constraints, and whether capacity is utility import, IT load, or marketing capacity.

Power evidence is especially important for post-2026 hyperscale/AI-campus leads because investment-promotion and policy sources may announce "data center" opportunities before a permit or site exists.

---

## 5. Official cloud-region and edge checks

Cloud pages prove logical region/edge presence only. They do not identify physical facilities unless the provider explicitly names a site/operator.

| Provider | Official source | North Macedonia signal as of 2026-08-12 | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and AWS docs regions list | No North Macedonia AWS Region found in official lists. | Do not infer AWS facility. Search only for partner/edge/tenant evidence if local operator source says so. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No North Macedonia Azure public cloud region found in the official region list. | Use for negative cloud-region check; nearby regions may influence latency but are not MK facilities. |
| Google Cloud | https://cloud.google.com/about/locations and Google data center locations https://datacenters.google/locations | No North Macedonia Google Cloud region or Google-owned data-center country location found. | Do not count Google office/partner/cloud use as facility evidence. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and OCI docs region list | No North Macedonia OCI public cloud region found in official region list. | Use as negative check unless Oracle announces a dedicated/sovereign/customer region. |

Cloud queries:

```text
site:aws.amazon.com "North Macedonia" "Local Zone"
site:learn.microsoft.com "North Macedonia" "Azure" "region"
site:cloud.google.com "North Macedonia" "cloud region"
site:oracle.com "North Macedonia" "cloud region"
"Skopje" "cloud region" AWS OR Azure OR Google OR Oracle
"North Macedonia" "sovereign cloud" "data center"
```

---

## 6. Official/operator facility seed list

Operator pages are **A for marketed facility existence** when they identify a data-centre service and location. They still need permit/AEK/power corroboration for construction status, legal address, municipality, and MW.

| Operator / project | Official source | Municipality signal | Official follow-up |
|---|---|---|---|
| Interspace data center colocation | https://interspace.com/en/data-center-colocation | Skopje; third-party records point to Pero Nakov/Gazi Baba and Jane Sandanski/Aerodrom | Search e-permits, Skopje/Gazi Baba/Aerodrom planning, AEK, EVN, address variants. |
| Telesmart Telekom SET / DC Skopje | https://en.telesmart.mk/colocation/ | Skopje; Kiro Gligorov / Nikola Parapunov address ambiguity between Gazi Baba/Karpos | Search AEK notified entities, PeeringDB, Skopje planning, EVN, facility address variants. |
| Neotel / neoDC / neoCloud | https://neodc.mk/ ; https://neocloud.mk/architecture/ ; https://neotel.com.mk/en/business-users/cloud-services/infrastructure-as-a-service/ | Skopje/Centar and Stip in official/third-party evidence | Search Neotel legal name, AEK records, Stip municipal permits, Skopje permits, EVN. |
| Net.Bit datacenter | https://netbit.mk/ and Veles/contact pages | Veles official address / possible Skopje older listing | Use Net.Bit own pages first; verify Veles address through municipality/e-permit/AEK. |
| Data Center DTS | https://www.datacenterdts.com/ | Makedonska Kamenica via vendor project evidence | Verify with Makedonska Kamenica municipal records, energy connection, AEK/operator company evidence. |
| Government Business Continuity and Disaster Recovery Data Centre | EU/project records via https://euprojects.mk/ and IPA documents | Prilep operational; Kavadarci was a candidate/rejected scenario | Use EU project record, Ministry of Finance/Interior procurement, Prilep permits, facility designer/contractor documents. |
| A1 Macedonia internal data center | A1 corporate: https://www.a1.mk/ ; third-party facility pages | Skopje, likely internal/telecom | Treat as C until A1 official facility-specific evidence or AEK/permit record found. |
| Makedonski Telekom | https://www.telekom.mk/ | Telecom network/core sites; not public colocation by default | Search annual reports, AEK, procurement, server-room terms; do not count all telecom core nodes as DCs. |

Operator official queries:

```text
site:interspace.com "data center" "Skopje"
site:telesmart.mk "colocation" "Skopje"
site:neotel.com.mk "data center" OR "data centre" OR "cloud"
site:neocloud.mk "data center" OR "Stip"
site:neodc.mk "Kuzman Josifovski Pitu"
site:netbit.mk "datacentar" OR "data center" OR "Veles"
site:datacenterdts.com "Makedonska Kamenica"
site:a1.mk "data center" OR "дата центар"
site:telekom.mk "data center" OR "дата центар" OR "серверска"
```

---

## 7. Municipality-level enumeration strategy

### 7.1 Universal municipality workflow

For each municipality:

1. Run English + Macedonian queries for `data center/data centre/datacenter`, `дата центар`, `центар за податоци`, `серверска сала`, `колокација`, `облак/клауд`, `деловен континуитет`, and `обнова од катастрофи`.
2. Run official-domain passes: `gradezna-dozvola.mk`, municipal site, `e-nabavki.gov.mk`, `bjn.gov.mk`, `aek.mk`, `erc.org.mk`, `mepso.com.mk`, `evn.mk`, `elektrodistribucija.mk`, `mdt.gov.mk`, `portal.mdt.gov.mk`, `ener.gov.mk`, `euprojects.mk`.
3. Search known operator names with municipality/street names: Interspace, Telesmart, Neotel, neoDC, neoCloud, Net.Bit, Data Center DTS, A1, Makedonski Telekom, Akton, Telekabel, MARNET, government BCDR.
4. Resolve Skopje municipal boundaries carefully. Many directories say "Skopje" only; assign to Aerodrom/Gazi Baba/Centar/Karpos only when address evidence supports it.
5. For any lead, require at least one primary source for A-grade status: operator-owned page, permit/planning record, procurement/project record, AEK record, or power-grid record.

Universal templates:

```text
"{municipality}" "data center" "North Macedonia"
"{municipality}" "data centre" Macedonia
"{municipality}" "datacenter" Macedonia
"{municipality}" "дата центар"
"{municipality}" "центар за податоци"
"{municipality}" "серверска сала"
"Општина {municipality}" "дата центар"
"Општина {municipality}" "центар за податоци"
"{municipality}" "{operator}" "data center"
"{municipality}" "{operator}" "дата центар"
"{municipality}" "јавна набавка" "серверска сала"
"{municipality}" "трафостаница" "дата центар"
```

### 7.2 High-priority municipalities and query notes

| Municipality | Known/likely signal | Official query focus |
|---|---|---|
| Aerodrom | Interspace Jane Sandanski and Akton SKP03 leads | Search `Јане Сандански`, `23-ти Октомври`, Aerodrom planning/permits, Interspace/Akton, EVN. |
| Gazi Baba | Interspace Pero Nakov, Telesmart Kiro Gligorov, Akton Belasitsa leads | Search `Перо Наков`, `Киро Глигоров`, `Беласица`, industrial-zone planning, AEK, EVN. |
| Centar | neoDC/Neotel Kuzman Josifovski Pitu, A1 internal lead | Search `Кузман Јосифовски Питу`, `Пресвета Богородица`, Neotel/neoDC/A1, Skopje city permits. |
| Karpos | Telesmart Nikola Parapunov address ambiguity | Search `Никола Парапунов`, `Карпош 4`, Telesmart, PeeringDB, AEK, municipal boundary. |
| Veles | Net.Bit official datacenter lead | Search Net.Bit, `Никола Оровчанец`, Veles permits/procurement/EVN. |
| Stip | Neotel/neoCloud Stip data center lead; Telekabel HQ/telecom context | Search Neotel, neoCloud, Telekabel, Stip municipality, AEK, EVN. |
| Makedonska Kamenica | Data Center DTS project lead | Search Data Center DTS, CompuNet, municipal planning, power connection. |
| Prilep | Government Business Continuity and Disaster Recovery Data Centre | Search EU projects, Ministry of Interior/Finance, `Васко Карангелески`, Prilep permits/procurement. |
| Kavadarci | Earlier BCDR candidate/rejected scenario | Search only as historical candidate unless new procurement/permit appears. |
| Kriva Palanka / Deve Bair | DataCenterMap and job-ad lead for "Deve Bair"; weak | Require operator, permit, AEK, customs/border or power evidence before counting. |
| Ilinden / Petrovec / Kumanovo / Tetovo / Gostivar / Bitola / Ohrid / Struga / Gevgelija | Industrial/logistics/telecom/airport/border-city plausibility but no strong public confirmed lead in checked results | Run universal workflow plus industrial-zone, SEZ/TIDZ, telecom POP, municipal procurement, and power-substation terms. |

High-priority templates:

```text
"Перо Наков" "data center" OR "дата центар"
"Киро Глигоров" Telesmart "colocation"
"Никола Парапунов" Telesmart "Skopje"
"Јане Сандански" Interspace "data center"
"Кузман Јосифовски Питу" neoDC OR Neotel
"Никола Оровчанец" Net.Bit Veles
"Makedonska Kamenica" "Data Center DTS"
"Васко Карангелески" "data centre" Prilep
"Deve Bair" "data center" Macedonia
```

### 7.3 Lower-probability municipality sweep

For the remaining municipalities, expect mostly negative results or small public-sector server rooms. Use:

- municipal site + `дата центар`, `центар за податоци`, `серверска сала`, `јавна набавка`;
- AEK/operator terms for local telecom POPs;
- EVN/MEPSO terms for large industrial-load or substation clues;
- TIDZ/industrial-zone terms where relevant;
- local press terms only after official and operator searches.

Do not count:

- generic "data" portals, GIS databases, digitalization projects, or software systems;
- telecom base stations or fibre routes without a hosting/compute facility;
- public procurement for servers unless it identifies a server room/data-centre facility;
- cloud services resold from foreign regions;
- investment-promotion language saying the country is suitable for data centers without a named site.

