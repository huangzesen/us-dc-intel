# GH Explorer Official - Ghana Datacenter Enumeration via Regulators, Permits, Power, ICT Government and Investment Records

Date: 2026-08-12. Country: **GH Ghana**. Division model: **16 regions** (`subnational_type = region`): Ahafo, Ashanti, Bono, Bono East, Central, Eastern, Greater Accra, North East, Northern, Oti, Savannah, Upper East, Upper West, Volta, Western, Western North. Angle: **official and regulatory evidence** for commercial, telecom, government, enterprise and hyperscale/pipeline data-centre facilities.

Reliability grades:
- **A** = primary/official evidence: NCA licence/service pages and consultations, Energy Commission licence/permit registers, EPA permit/EIA records, MMDA development/building permits, NITA or ministry records, Data Protection Commission registrations, GIPC/GFZA registrations, official cloud-region pages, Uptime Institute award pages.
- **A-** = official operator page or official press release proving a named site, location or status, but not a regulator filing; use cautiously for design capacity.
- **B** = strong secondary evidence: established trade press, investor/developer announcements, peering/subsea industry bodies, reputable Ghanaian business press.
- **C** = lead only: market reports, directories, social posts, unsourced capacity tables, SEO pages, or claims that cannot be tied to a permit, official register or operator page.

Use the grade on the *specific claim*. A facility can be **A** for existence, **B** for announced MW, and **C** for commissioning status if those facts come from different evidence chains.

---

## 0. Ghana-specific structure facts

- Ghana has **no national data-centre register** and no unified public database for local development/building permits. Build the official chain from: operator/SPV name -> MMDA planning/building permit -> EPA environmental permit/EIA -> Energy Commission power permit/register -> NCA telecom/submarine/managed-services licence where relevant -> DPC registration -> NITA/ministry or operator official confirmation.
- Ghana is administratively divided into **16 regions**. Treat region coverage as complete only when every region in the table below has been searched or explicitly marked `no_projects: true` with date and query notes.
- The market is **commercially Greater Accra-led**: Accra, Ring Road/CBD, Airport/Ridge, Amrahia, Appolonia City and Tema are the main targets. **Ashanti is not blank**: Uptime Institute records a NITA **Ghana E-Gov Cloud Data Center** in Kumasi. Other regions are usually negative for commercial colocation but can contain government, telco, bank, mining, oil/gas, university or disaster-recovery rooms.
- English is the practical search language. Use both spellings and aliases: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `colocation`, `co-location`, `cloud data center`, `ICT hub`, `Tier III`, `Tier IV`, `MW`, `MVA`, `bulk customer`, `substation`, `generator`, `EIA`, `environmental permit`.
- Ghana has **no confirmed AWS, Azure, Google Cloud or Oracle public cloud region** as of this methodology date. Cloud/edge/CDN presence is not a facility record unless the provider's official region/location page names Ghana as a cloud region or a Ghana facility.
- Press-release MW is common. Do not convert announced design capacity into operational IT load without a commissioning source, permit, Uptime constructed-facility award, utility connection, or operator status page.

---

## 1. Regulator - National Communications Authority (NCA)

Official site: https://nca.org.gh/. Regulatory framework page: https://nca.org.gh/regulatory-framework/. Licensing/authorisation area: https://nca.org.gh/licencing-and-authorisation/.

Verified points:
- NCA is Ghana's electronic-communications regulator under the **National Communications Authority Act, 2008 (Act 769)** and **Electronic Communications Act, 2008 (Act 775)**.
- NCA is **not a general data-centre-permit authority**. Use it for connectivity-adjacent evidence: submarine cable landing licences, public data/internet service authorisations, satellite/VSAT, infrastructure/tower licensing, spectrum, managed-services consultations and licensed service-provider pivots.
- NCA's submarine cable landing page states that a submarine cable licence authorises landing and operation of optical-fibre submarine cable systems and associated **cable landing stations** in Ghana. This is a strong Grade-A lead source for DC-adjacent assets.
- NCA's public submarine-cable page lists legacy providers **SAT-3, MainOne, WACS, Glo and ACE**. Because newer 2Africa/Bayobab landings post-date some NCA web copy, verify 2Africa through Bayobab/MTN official releases and then check NCA for licence/consultation evidence.
- NCA type approval/conformance is equipment-level evidence only; it does not prove a facility.

What to extract: licensee/SPV, licence class, authorisation scope, station/site wording, district/address, effective/expiry dates, consultation notice dates, and related operator names.

NCA query templates:
```text
site:nca.org.gh "Submarine Cable Landing" Ghana
site:nca.org.gh "data centre" OR "data center" OR datacentre
site:nca.org.gh "landing station" Ghana "{operator}"
site:nca.org.gh "public data service" "{operator}"
site:nca.org.gh "managed service" "{operator}"
site:nca.org.gh "Next-Gen Infraco" OR NGIC Ghana licence
"National Communications Authority" "submarine cable" "Ghana" "{operator}"
```

Grade guidance: **A** for NCA pages, notices and official downloads; **B** for trade press quoting an NCA action; **C** for generic lists of licensees without an NCA page.

---

## 2. Power and energy evidence

### 2.1 Energy Commission

Official site: https://energycom.gov.gh/. Licence/permit register examples: https://energycom.gov.gh/regnew/index.php/Energy/loadRegister/Bulk%20Customer%20Register and licensing pages under https://www.energycom.gov.gh/index.php/licensing/. Online portal: https://licences.energycom.gov.gh/.

Verified points:
- Energy Commission regulates electricity and natural gas under the **Energy Commission Act, 1997 (Act 541)**.
- Its electricity licensing manual identifies **Bulk Customer Permit**, **Siting Permit** and **Construction Permit** as relevant permit types. The Bulk Customer Register exposes permit holder, address, business nature, permit number, issue date and expiry date.
- A data centre may surface as a bulk electricity customer, self-generation/captive-generation project, renewable-energy project, or through siting/construction permits for generation or supply infrastructure. Backup diesel generation and solar supply are the most likely official hooks.

Energy Commission templates:
```text
site:energycom.gov.gh "{operator}" "Bulk Customer"
site:energycom.gov.gh "{operator}" "EC_BCP"
site:energycom.gov.gh "{operator}" "Siting Permit" OR "Construction Permit"
site:energycom.gov.gh "data centre" OR "data center" OR datacentre
"Energy Commission" Ghana "{company}" generator OR diesel OR solar OR "self-generation"
"Bulk Customer Register" Ghana "{company}"
```

### 2.2 Utilities and grid operators

Use official utility pages to corroborate grid connection, substations, power reliability and large-load status:
- ECG - Electricity Company of Ghana: https://www.ecggh.com/ (southern distribution area including Greater Accra, Ashanti, Central, Eastern, Volta, Western and related southern regions).
- NEDCo - Northern Electricity Distribution Company: https://nedco.com.gh/ (northern distribution areas including Northern, Upper East, Upper West, Savannah, North East and nearby northern service areas).
- GRIDCo - Ghana Grid Company: https://www.gridcogh.com/ (transmission/substations).
- PURC: https://purc.com.gh/ (tariffs and regulatory context, not a facility census).
- VRA: https://www.vra.com/ (generation context and industrial power leads).

Utility templates:
```text
site:ecggh.com "{site}" "data centre" OR substation OR "power supply" OR "load"
site:gridcogh.com "{site}" substation OR transmission OR MVA
site:nedco.com.gh "{region}" "data centre" OR "server room"
"{operator}" Ghana "power" "substation" "data centre"
"{town}" Ghana "MVA" "data centre" OR "ICT"
```

Grade guidance: **A** for Energy Commission registers and official utility documents; **B** for utility or project press releases that do not show permit records; **C** for reported MW without a permit/register.

---

## 3. Environment - EPA Ghana

Official site: https://epa.gov.gh/. Public permitting/ERP portal: https://www.client.epa.gov.gh/ and https://www.client.epa.gov.gh/public/permits when reachable. Ghana.GOV EPA services: https://www.ghana.gov.gh/mdas/.

Verified points:
- Ghana's environmental permitting has historically operated under the **Environmental Protection Agency Act, 1994 (Act 490)** and **Environmental Assessment Regulations, 1999 (LI 1652)**, with amendments. Check each batch for current successor instruments because Ghana has been updating environmental legislation.
- LI 1652-style procedure requires undertakings with likely significant environmental impacts to register and obtain environmental permit/EIA clearance before construction/operation. Data centres are relevant because of standby generators, fuel storage, cooling, water use, noise, batteries and e-waste.
- EPA permit/EIA records are the best official source for technical capacity clues: generator count/MW, fuel storage, cooling system, water demand, site plan, phase description and proponent/SPV.

EPA templates:
```text
site:epa.gov.gh "data centre" OR "data center" OR datacentre
site:client.epa.gov.gh "{operator}" OR "{SPV}"
site:client.epa.gov.gh "data centre" Ghana
"EPA Ghana" "environmental permit" "data centre"
"{operator}" Ghana "environmental impact" OR EIA OR "environmental permit"
filetype:pdf Ghana "data centre" "environmental permit"
filetype:pdf Ghana "{operator}" generator "EIA"
```

Grade guidance: **A** for permit/EIA numbers and EPA registry pages; **B** for official project press saying an EPA permit was granted but not showing the permit; **C** for claimed environmental compliance with no document.

---

## 4. Planning and building permits - MMDAs

Development/building permits are handled by Metropolitan, Municipal and District Assemblies (MMDAs), not by one national data-centre portal. Use assembly sites, planning notices, assembly minutes, procurement pages and Ghana.GOV service listings.

High-priority assemblies:
- Accra Metropolitan Assembly: https://ama.gov.gh/
- Tema Metropolitan Assembly: https://tma.gov.gh/
- Kumasi Metropolitan Assembly: https://www.kma.gov.gh/
- La Dade-Kotopon, Adentan, La Nkwantanang-Madina, Ga East, Ga West and Kpone-Katamanso municipal assemblies for Airport/Ridge/Ring Road, Amrahia, Appolonia City, Spintex and Tema-area sites.
- Tamale Metropolitan Assembly: https://tamalemetro.gov.gh/ for Northern-region checks.

Planning templates:
```text
site:{assembly-domain} "data centre" OR "data center" OR datacentre
site:{assembly-domain} "building permit" "{operator}"
site:{assembly-domain} "development permit" "{site}" OR "{operator}"
"{district}" Ghana "data centre" "permit" OR "development permit"
"{town}" Ghana "data centre" construction permit
"{operator}" "plot" OR "parcel" "Accra" "data centre"
```

Extract: MMDA, plot/parcel/LR/GR number, applicant/SPV, use description, permit decision/date, floor area, generators/mechanical plant references, and district/region assignment. **A** only when the assembly document or official permit notice is found.

---

## 5. Data protection, ICT government and public-sector DCs

### Data Protection Commission (DPC)

Official site: https://dataprotection.org.gh/. Ghana's Data Protection Act, 2012 (**Act 843**) requires data controllers/processors to register with the Commission. DPC is company-level evidence, not facility-level evidence.

Templates:
```text
site:dataprotection.org.gh "{operator}"
"Data Protection Commission" Ghana "{operator}" registered
"Act 843" Ghana "{operator}" "data controller"
```

### NITA and ministry sources

NITA: https://nita.gov.gh/. Data Centre project page: https://nita.gov.gh/projects/datacentre/. Uptime Institute client page for NITA lists two Ghana awards: **Primary Ghana National Data Center Accra** and **Ghana E-Gov Cloud Data Center, Kumasi**: https://uptimeinstitute.com/uptime-institute-awards/client/national-information-technology-agency-nita/1008.

Ministry of Communication, Digital Technology and Innovations: https://moc.gov.gh/. Ghana Digital Centres Ltd / Accra Digital Centre: https://gdcl.gov.gh/ and https://adc.gov.gh/.

Templates:
```text
site:nita.gov.gh "data centre" OR "data center" OR datacentre
site:nita.gov.gh "Kumasi" "data centre" OR "cloud"
site:moc.gov.gh "data centre" OR "digital centre" OR NITA
site:gdcl.gov.gh "data centre" OR "regional digital centre"
site:adc.gov.gh "data centre" OR colocation OR "server room"
site:uptimeinstitute.com Ghana NITA "Data Center"
```

Grade guidance: **A** for NITA/ministry official pages and Uptime award records; **B** for government press; **C** for directories that infer NITA site counts.

---

## 6. Investment, free zones and company/SPV pivots

- GIPC - Ghana Investment Promotion Centre: https://gipcghana.com/ and https://gipc.gov.gh/. Use for foreign-investor registration and ICT/data-centre investment announcements.
- Ghana Free Zones Authority (GFZA): https://gfza.gov.gh/. Use for free-zone enterprise licences around Tema Free Zone, Appolonia, Dawa and other industrial parks.
- Registrar-General's Department: https://rgd.gov.gh/. Use to resolve SPV names and ownership.
- Ghana Revenue Authority: https://gra.gov.gh/. Use only as tax/company corroboration.

Templates:
```text
site:gipcghana.com "data centre" OR "data center" OR datacentre
site:gipc.gov.gh "data centre" OR ICT "Accra"
site:gfza.gov.gh "data centre" OR "ICT" "enterprise"
"Ghana Free Zones" "{operator}" licence
"Registrar-General" Ghana "{SPV}" "data centre"
"{operator}" Ghana "GIPC" OR "GFZA" OR "free zone"
```

Grade guidance: **A** for official registration/licence; **B** for project capacity in investment-promotion material; **C** for investor decks or directories without filings.

---

## 7. Official cloud-region check

Run on every batch. The absence of Ghana on an official cloud region list means no Ghana cloud-region facility should be created.

Official pages:
- AWS Global Infrastructure / Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure geographies and region list: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Templates:
```text
site:aws.amazon.com Ghana "Region" "Availability Zone"
site:learn.microsoft.com/azure Ghana "Azure region"
site:cloud.google.com/about/locations Ghana "region"
site:oracle.com/cloud Ghana "cloud region"
```

Grade guidance: **A** only for official provider region/location pages. Cloud offices, partner nodes, caches, CDN PoPs and edge nodes are ecosystem notes, not DC facility records.

---

## 8. Per-region official coverage map

| Region | Capitals / hubs and official bodies | Expected official outcome | Core official queries |
|---|---|---|---|
| **Greater Accra** | Accra, Ridge, Ring Road, Airport, Dzorwulu, East Legon, Spintex, Amrahia, Appolonia City, Tema; AMA, TMA, Ga East, Adentan, La Nkwantanang-Madina, La Dade-Kotopon, Kpone-Katamanso | Main commercial and government cluster: Equinix AC1/MDXi, Onix, PAIX, Africa Data Centres/Onix pipeline, NITA Accra, telco DCs, cable landings, IXPs | `site:ama.gov.gh "data centre"`, `site:tma.gov.gh "data centre"`, `"Appolonia" "data centre" Ghana`, `"Amrahia" "data centre" Ghana`, `"Ring Road Central" "data centre"`, `site:nca.org.gh "landing station" Accra` |
| **Ashanti** | Kumasi, KMA, KNUST, NITA Kumasi | Government DC exists: Uptime lists NITA **Ghana E-Gov Cloud Data Center, Kumasi**. Commercial colo not confirmed. | `site:kma.gov.gh "data centre" OR server`, `site:nita.gov.gh Kumasi "data centre"`, `site:uptimeinstitute.com Ghana Kumasi "Data Center"`, `"Kumasi" "colocation" Ghana` |
| **Bono** | Sunyani | Negative for commercial colo unless government/telco DR appears | `"Sunyani" "data centre" Ghana`, `site:energycom.gov.gh Sunyani "data centre"`, `site:{assembly} "server room"` |
| **Bono East** | Techiman | Negative for commercial colo | `"Techiman" "data centre" Ghana`, `"Bono East" "ICT" "data centre"` |
| **Ahafo** | Goaso, Kenyasi mining belt | Check mining/enterprise rooms; no commercial colo expected | `"Ahafo" "data centre" Ghana`, `"Kenyasi" server room data Ghana` |
| **Central** | Cape Coast, Winneba | University/government ICT only; negative commercial colo | `"Cape Coast" "data centre" Ghana`, `"University of Cape Coast" "data centre"` |
| **Eastern** | Koforidua | Government/telco rooms; negative commercial colo | `"Koforidua" "data centre" Ghana`, `"Eastern Region" Ghana "server room"` |
| **North East** | Nalerigu | Negative; telco/government facilities only | `"Nalerigu" "data centre" Ghana`, `"North East Region" Ghana "ICT" "server"` |
| **Northern** | Tamale, Yendi | Government/UN/telco rooms; negative commercial colo | `site:tamalemetro.gov.gh "data centre" OR server`, `"Tamale" "data centre" Ghana` |
| **Oti** | Dambai | Negative | `"Oti Region" "data centre" Ghana`, `"Dambai" "server room" Ghana` |
| **Savannah** | Damongo | Negative | `"Savannah Region" Ghana "data centre"`, `"Damongo" "server room" Ghana` |
| **Upper East** | Bolgatanga | Negative | `"Bolgatanga" "data centre" Ghana`, `"Upper East" Ghana "server room"` |
| **Upper West** | Wa | Negative | `"Wa" "data centre" Ghana`, `"Upper West" Ghana "server room"` |
| **Volta** | Ho, Hohoe | Telco/government rooms; negative commercial colo | `"Ho" "data centre" Ghana`, `"Volta Region" Ghana "data centre"` |
| **Western** | Sekondi-Takoradi, Takoradi port/oil/gas | Enterprise rooms possible; negative commercial colo | `"Takoradi" "data centre" Ghana`, `"Sekondi" "server room"`, `"Western Region" Ghana "data centre"` |
| **Western North** | Sefwi Wiawso | Negative | `"Western North" Ghana "data centre"`, `"Sefwi Wiawso" "server room" Ghana` |

Generic sweep for every region:
```text
"{region}" Ghana "data centre" OR "data center" OR datacentre OR "server room"
"{capital}" Ghana "colocation" OR "co-location" OR "cloud data center"
site:*.gov.gh "{region}" "data centre" OR "server room" OR ICT
"{region}" Ghana "environmental permit" "data centre"
"{region}" Ghana "bulk customer" "data centre"
```

---

## 9. Verification recipe

1. Start with named facilities from operator/NITA/Uptime records: Equinix AC1/MDXi Appolonia, Onix Accra #1, PAIX Accra, NITA Accra, NITA Kumasi, Africa Data Centres/Onix Accra pipeline, MTN/Telecel/AT/NGIC enterprise leads.
2. Resolve aliases and SPVs: Equinix AC1 = MainOne/MDXi Appolonia; Onix Accra #1 = Ngoya Etix DC (Ghana) Ltd / Onix Data Centres Ghana; PAIX Accra = RackAfrica legacy; NITA sites may appear as Ghana National Data Center, Primary Ghana National Data Center Accra, Ghana E-Gov Cloud Data Center Kumasi.
3. For each named facility, seek permit evidence in this order: EPA/EIA -> MMDA development/building permit -> Energy Commission bulk customer/self-generation/siting/construction permit -> NCA telecom/landing-station evidence -> DPC/company registration -> official operator/NITA page -> Uptime.
4. Separate facts: `status`, `capacity_mw`, `racks`, `tier`, `address`, `region`, `operator`, `SPV`, `evidence_date`, `source_urls`, `evidence_grade`.
5. For capacity, prefer permit/genset/power-connection records over press. Record announced design capacity separately from commissioned or operational capacity.
6. Use `no_projects: true` only after running region templates and checking official/national sources for the relevant capital/towns.
7. Re-run official cloud-region check every batch.

Status ladder: rumour < MoU < announced < land acquired < permit applied < permit granted < construction started < commissioned/inaugurated < operational. Do not skip ladder stages without evidence.

---

## 10. Pitfalls and corrections from draft verification

- **NCA licence does not equal data-centre facility**. It is a Grade-A connectivity/regulatory lead, especially for submarine cable landing stations and public data/network services.
- **Ashanti is not fully negative**: Uptime Institute lists NITA's Ghana E-Gov Cloud Data Center in **Kumasi**. Mark Ashanti as government DC present, commercial colo unconfirmed.
- **2Africa is real for Ghana**, but NCA's public submarine page may still list only older providers. Use Bayobab/MTN official evidence and then look for NCA licence traces.
- **Equiano does not land in Ghana** based on Google/Equiano route evidence; do not create a Ghana record for it.
- **No hyperscaler public cloud region in Ghana** as of 2026-08-12 after checking official AWS/Azure/GCP/Oracle region pages.
- **Africa Data Centres Accra** should remain pipeline/construction/partnered unless a current official source confirms operational commissioning.
- Directories are lead sources only. They often merge aliases or list inferred capacity; dedupe before ingesting.

## Grade-A backbone URLs

| Source | URL | Use |
|---|---|---|
| NCA | https://nca.org.gh/ | Telecom licences, landing-station authority, consultations |
| NCA submarine cable landing | https://nca.org.gh/submarine-cable-landing/ | Cable landing station licence scope and legacy providers |
| NCA regulatory framework | https://nca.org.gh/regulatory-framework/ | Acts 769/775 and related rules |
| Energy Commission | https://energycom.gov.gh/ | Electricity/gas licensing |
| Bulk Customer Register | https://energycom.gov.gh/regnew/index.php/Energy/loadRegister/Bulk%20Customer%20Register | Large-load permit holder checks |
| ECG / NEDCo / GRIDCo | https://www.ecggh.com/ ; https://nedco.com.gh/ ; https://www.gridcogh.com/ | Distribution/transmission evidence |
| EPA Ghana / ERP | https://epa.gov.gh/ ; https://www.client.epa.gov.gh/public/permits | Environmental permits and EIA records |
| NITA data centre | https://nita.gov.gh/projects/datacentre/ | Government DC evidence |
| Uptime NITA | https://uptimeinstitute.com/uptime-institute-awards/client/national-information-technology-agency-nita/1008 | Accra and Kumasi government DC awards |
| DPC | https://dataprotection.org.gh/ | Controller/processor registration |
| GDCL / Accra Digital Centre | https://gdcl.gov.gh/ ; https://adc.gov.gh/ | Government digital-centre and ICT-campus evidence |
| GIPC / GFZA / RGD | https://gipcghana.com/ ; https://gfza.gov.gh/ ; https://rgd.gov.gh/ | Investment, free-zone and SPV pivots |
| Cloud region pages | AWS/Azure/GCP/Oracle URLs in section 7 | Ghana cloud-region exclusion check |
