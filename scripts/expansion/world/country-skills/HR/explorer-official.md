# HR Explorer Official - Croatia Datacenter Enumeration Methodology

Date: 2026-08-12. Scope: official/regulatory/cloud-first methodology for enumerating datacenter, colocation, cloud-edge, AI/HPC, and large ICT infrastructure projects in Croatia. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade source, **C** = weak aggregate or promotional claim.

Croatian-language search terms matter: **podatkovni centar**, **data centar**, **računalni centar**, **kolokacija**, **cloud**, **oblak**, **ICT infrastruktura**, **informacijska infrastruktura**, **umjetna inteligencija**, **AI data centar**, **visokoučinkovito računarstvo / HPC**, **građevinska dozvola**, **lokacijska dozvola**, **uporabna dozvola**, **zahvat u prostoru**, **procjena utjecaja na okoliš / PUO**, **ocjena o potrebi procjene / OPUO**, **priključenje na mrežu**, **trafostanica**, **prijenosna mreža**.

---

## 0. Structural Facts

- Croatia is small and Zagreb-centric for commercial colocation, but the official paper trail is national and searchable. Start nationally, then pivot to **Zagreb City**, **Zagreb County**, **Varazdin/Medimurje**, coastal metro counties, and any project-specific municipality.
- The strongest facility evidence is not a telecom license. It is the built-environment trail: **location permit, building permit, occupancy permit, spatial-plan act, public-notice board item, environmental screening/EIA, and grid connection evidence**.
- The national planning stack is **ISPU / eDozvola** under the Ministry of Physical Planning, Construction and State Assets. The Ministry says eDozvola supports electronic filing and status tracking for building and occupancy permits, and its **Oglasna ploča** publishes issued permits and public calls: https://edozvola.gov.hr/notice-board and https://mpgi.gov.hr/oglasna-ploca-13818/13818. **Grade A**.
- County/city administrative departments still matter because construction and spatial-planning authority is local by location. The Ministry publishes addresses for competent county/city bodies, e.g. Split-Dalmatia and City Split offices: https://mpgi.gov.hr/o-ministarstvu/djelokrug/graditeljstvo-98/adrese-upravnih-tijela-koji-obavljaju-poslove-prostornog-uredjenja-i-gradnje/splitsko-dalmatinska-zupanija-8598/8598. **Grade A**.
- HAKOM is useful for an operator universe and telecom pivots, not a complete datacenter registry. Its **e-Operator** is the central database of electronic communications network/service operators in Croatia: https://eoperator.hakom.hr/eop/pub/en/eoperator and https://www.hakom.hr/en/e-operator-211/210. **Grade A**.
- Electricity is a gating check. Large projects may require transmission or distribution connection work. Use **HOPS** transmission development plans, **HEP ODS** distribution connection pages, and **HERA** consultations/approvals. HOPS publishes ten-year transmission network plans: https://www.hops.hr/92136ad3-dfa8-4674-b6aa-3c7a0d41654c. HEP ODS describes digital network-connection filings via **Moja mreza**: https://www.hep.hr/ods/ostalo/obrasci-i-dokumenti/obrasci-i-dokumenti-vezani-uz-prikljucenje-na-mrezu/700. HERA regulates energy activities: https://www.hera.hr/en/html/index.html. **Grade A**.

---

## 1. Official Source Pipeline

### 1.1 Planning and Construction Permits - Core Facility Evidence

Primary portals:

- **ISPU - Informacijski sustav prostornog uredjenja**: https://ispu.mgipu.hr/ and https://portal-ispu.gov.hr/. Use for spatial plans, geoportal layers, and location context. **Grade A**.
- **eDozvola**: https://edozvola.gov.hr/. Use for active/issued permits and public notice searches. **Grade A**.
- **eDozvola Oglasna ploca**: https://edozvola.gov.hr/notice-board. The Ministry states all information on issued permits is published through this notice board. Search by place, investor, act type, and project term. **Grade A**.
- **gov.hr building permit guide**: https://gov.hr/hr/gradjevinska-dozvola/1250. Confirms applications are filed electronically through eDozvola or competent administrative body based on construction location. **Grade A**.
- **Occupancy permit guide**: https://gov.hr/hr/uporabna-dozvola/1260. Use **uporabna dozvola** as the operational-status trigger; it is stronger than opening ceremony news. **Grade A**.

High-value Croatian queries:

```text
site:edozvola.gov.hr/notice-board "podatkovni centar"
site:edozvola.gov.hr/notice-board "data centar"
site:edozvola.gov.hr/notice-board "računalni centar"
site:edozvola.gov.hr/notice-board "građevinska dozvola" "data centar"
site:edozvola.gov.hr/notice-board "uporabna dozvola" "podatkovni centar"
site:mpgi.gov.hr "podatkovni centar" "građevinska dozvola"
site:mpgi.gov.hr "data centar" "lokacijska dozvola"
site:portal-ispu.gov.hr "podatkovni centar"
```

Project-lifecycle interpretation:

- **lokacijska dozvola** = strong siting/planning evidence, pre-build.
- **građevinska dozvola** = approved construction; treat as high-confidence planned/under-construction depending on issue date and news.
- **izmjena i dopuna građevinske dozvole** = phase expansion, design change, or capacity/power change.
- **uporabna dozvola** = strongest public sign that the facility/phase may be operational.
- **javni poziv / uvid u spis predmeta** = pending permit; useful early lead, not proof of approval.

### 1.2 Environmental Screening and EIA

Primary portals:

- Ministry EIA/SEA pages for **PUO, SPUO, OPUO**: https://mzozt.gov.hr/o-ministarstvu-1065/djelokrug/procjena-utjecaja-na-okolis-puo-spuo/7370 and active PUO listings such as https://mzozt.gov.hr/o-ministarstvu-1065/djelokrug/procjena-utjecaja-na-okolis-puo-spuo/procjena-utjecaja-zahvata-na-okolis-puo-4014/procjena-utjecaja-zahvata-na-okolis-puo-4021/4021. **Grade A**.
- The Ministry defines PUO as an assessment before a location permit or other approval where a location permit is not mandatory. Use it to catch large campuses, generators, substations, energy plants, and behind-the-meter projects before construction permits. **Grade A**.

Queries:

```text
site:mzozt.gov.hr "podatkovni centar" (PUO OR OPUO OR "procjena utjecaja")
site:mzozt.gov.hr "data centar" "zahvat"
site:mzozt.gov.hr "računalni centar" "elaborat zaštite okoliša"
site:mzozt.gov.hr "trafostanica" "podatkovni centar"
site:mzozt.gov.hr "{municipality}" "data centar"
```

Extraction targets: investor, cadastral municipality, parcel, generator count, cooling system, transformer/substation capacity, water use, backup fuel, gross floor area, phased buildout.

### 1.3 Energy and Grid

Primary entities:

- **HOPS** - transmission system operator, planning and transmission grid development: https://www.hops.hr/en/ and plan archive https://www.hops.hr/92136ad3-dfa8-4674-b6aa-3c7a0d41654c. **Grade A**.
- **HEP ODS** - distribution connections and regional distribution areas; connection applications use Moja mreza or local distribution office: https://www.hep.hr/ods/pristup-mrezi/postupci-prikljucenja-na-mrezu/28 and https://www.hep.hr/ods/ostalo/obrasci-i-dokumenti/obrasci-i-dokumenti-vezani-uz-prikljucenje-na-mrezu/700. **Grade A**.
- **HERA** - regulator approving/consulting on network plans and energy rules: https://www.hera.hr/hr/html/savjetovanje-2025-03.html and https://www.hera.hr/en/html/index.html. **Grade A**.

Queries:

```text
site:hops.hr "podatkovni centar"
site:hops.hr "data centar"
site:hops.hr "{county_or_city}" "trafostanica" "priključenje"
site:hep.hr/ods "data centar" OR "podatkovni centar"
site:hera.hr "podatkovni centar" OR "data centar"
"priključenje na mrežu" "data centar" Hrvatska
"trafostanica" "data centar" Zagreb
```

Method: for any project over roughly 1-2 MW, search for a matching substation or grid-connection notice. For very large AI-campus claims, require HOPS/HEP/HERA evidence or an environmental/permit file that names dedicated generation, transmission connection, or a transformer station.

### 1.4 Telecom Regulator and Network Infrastructure

Use HAKOM to enumerate operators and connectivity pivots:

- **e-Operator**: https://eoperator.hakom.hr/eop/pub/en/eoperator. Search company names from colo/cloud claims: Digital Realty/Altus, DataBox, A1 Hrvatska, Hrvatski Telekom, Telemach, CRATIS/DC North, Akton, Comping/Data Target, CARNET/SRCE. **Grade A for operator status; not facility capacity**.
- HAKOM portal: https://www.hakom.hr/en/. Search news, decisions, market data, approvals, and e-Agency tools. **Grade A**.

Queries:

```text
site:hakom.hr "data centar"
site:hakom.hr "podatkovni centar"
site:hakom.hr "{operator}" "elektroničke komunikacije"
site:eoperator.hakom.hr "{operator}"
```

HAKOM is especially useful for confirming whether a claimed colocation/hosting entity is an electronic-communications operator or network provider. Do not treat HAKOM absence as proof that a private enterprise datacenter does not exist.

### 1.5 Public Procurement

Primary portals:

- **EOJN RH** - Croatian public procurement platform: https://eojn.hr/. **Grade A for tenders/awards**.
- Legacy/public notices in **Narodne novine EOJN**: https://eojn.nn.hr/. **Grade A**.
- EU TED / Publications Office can mirror Croatian large procurements: https://op.europa.eu/en/web/public-procurement. **Grade A**.

Queries:

```text
site:eojn.hr "data centar"
site:eojn.hr "podatkovni centar"
site:eojn.hr "računalni centar"
site:eojn.hr "kolokacija"
site:eojn.nn.hr "data centar"
site:eojn.nn.hr "podatkovni centar"
site:op.europa.eu Croatia Zagreb "data-centre infrastructure"
```

Use procurement for government/university/HPC projects and for expansion signals: turnkey AI/HPC infrastructure, data-center construction works, UPS/generator/cooling contracts, and colocation service awards.

---

## 2. Cloud and Carrier-Neutral Sources

### 2.1 Hyperscaler Official Pages

Croatia has no official public cloud region from AWS, Azure, Google Cloud, or OCI in the official region lists checked; it has edge/network presence and nearby EU regions.

- **AWS Global Infrastructure**: https://aws.amazon.com/about-aws/global-infrastructure/ and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/. AWS public-sector blog says AWS opened a data-centre design facility in Croatia and launched an AWS Edge location in Zagreb in February 2021: https://aws.amazon.com/blogs/publicsector/aws-opens-data-centre-design-facility-croatia/. **Grade A for AWS statements; design facility is not a cloud region**.
- **Microsoft Azure regions list**: https://learn.microsoft.com/en-us/azure/reliability/regions-list and geography page https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies. No Croatia region in the official region list; nearby regions include Austria, Italy North, Poland Central, Germany, Switzerland, etc. **Grade A**.
- **Google Cloud locations**: https://cloud.google.com/about/locations and data-center location list https://datacenters.google/locations. No Croatia region/datacenter listed; nearest relevant official Europe locations include Milan, Frankfurt, Austria development site, etc. **Grade A**.
- **Oracle Cloud regions**: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and region page https://www.oracle.com/cloud/public-cloud-regions/. No Croatia public OCI region in official lists checked. **Grade A**.

Cloud query patterns:

```text
site:aws.amazon.com Croatia Zagreb "Edge location"
site:aws.amazon.com Croatia "data centre design facility"
site:learn.microsoft.com/azure Croatia "region"
site:cloud.google.com Croatia "region"
site:oracle.com/cloud Croatia "region"
"Zagreb" "edge location" (AWS OR CloudFront OR Akamai OR Google OR Microsoft)
```

### 2.2 Croatian Colo and Datacenter Operators

Start with official operator pages, then verify via permits/HAKOM/CIX/trade press.

| Operator / facility | Geography | Official or strong source | Grade | Notes |
|---|---|---|---|---|
| Digital Realty / former Altus IT ZAG1 | Zagreb City | Digital Realty Zagreb page: https://www.digitalrealty.com/data-centers/emea/zagreb; CIX FAQ confirms CIX2 at Digital Realty, Selska cesta 93: https://www.cix.hr/en/faq | A-/B | Official operator page for market; CIX confirms facility role. Use eDozvola for address-specific permit history. |
| DataBox | Zagreb City | Official facility page: https://databox.hr/en/data-centar_/ | A- | Search DataBox, Savica, Zitnjak, and Croatian terms. Capacity claims need permit or operator-doc confirmation. |
| A1 Hrvatska | Zagreb City | DCD report on 2021 Zagreb facility: https://www.datacenterdynamics.com/en/news/a1-croatia-opens-zagreb-data-center/; A1 official business pages should be checked per service | B, A if official A1 page found | Telco-owned; pivot through HAKOM and building permits around Neziceva/Veleslav Holjevac. |
| Hrvatski Telekom | Zagreb City | HT business ICT/cloud page: https://www.hrvatskitelekom.hr/poslovni/ict/wholesale; Siemens/HT cooling-upgrade article confirms HT Zagreb datacenter activity: https://blog.siemens.com/en/2026/02/ai-controls-the-cooling-of-croatias-telekom-data-center/ | A-/B | Telco-owned; likely multiple network/technical sites. Avoid counting exchanges as datacenters unless marketed/leased as DC. |
| DC North / CRATIS | Varazdin | Official DC North site: https://dcnorth.hr/; CRATIS opening and strategic-project posts: https://www.cratis.hr/en/blog/grand-opening-data-center-dc-north-55/ and https://www.cratis.hr/en/blog/data-center-dc-north-has-been-included-in-the-list-of-strategic-projects-republic-croatia-54/ | A-/B | Strong non-Zagreb facility. CIX says third CIX location was put into operation at DC North in May 2025: https://www.cix.hr/en/news/srce-marked-25-years-of-croatian-internet-exchange-cix/295. |
| SRCE / CIX / CARNET | Zagreb and Varazdin CIX nodes | CIX official: https://www.cix.hr/en and SRCE CIX page: https://www.srce.unizg.hr/en/cix | A | National IXP and academic infrastructure; count facility only if a datacenter service/site is explicitly in scope. |
| Croatian Web Hosting, Akton, Comping/Data Target, PCK/DataCross, local hosts | Zagreb County / Zagreb metro | Aggregators such as Baxtel/DataCenterMap/Datacenters.com | C/B depending source | Use as leads only; verify against operator official pages, HAKOM, permits, and procurement. |

Trade/aggregate sources:

- **Data Center Dynamics** for Croatian facility news and investment announcements: https://www.datacenterdynamics.com/. **Grade B**.
- **Baxtel**, **DataCenterMap**, **Datacenters.com**, **Cloudscene**, **PeeringDB**: useful seed lists; capacity may be stale or submitted by provider. **Grade C/B**.
- **CIX official member/location news** is stronger than generic aggregators for peering-enabled sites. **Grade A for CIX facts**.
- Croatian business press: Lider, Poslovni dnevnik, ICTbusiness.info, Netokracija, Bug.hr, SEEbiz, tportal, HINA releases. Use as B/C unless they quote official permits or operator filings.
- Regional energy/infrastructure press: Balkan Green Energy News for grid policy context. **Grade B**; confirm rules on HERA/HOPS/HEP.

---

## 3. Search Workflow

### 3.1 National Sweep

1. Search eDozvola/Oglasna ploca for Croatian and English datacenter terms.
2. Search ISPU/MPGI for spatial plans and permit notices by project/operator name.
3. Search MZOZT/MINGO environmental pages for PUO/OPUO and backup-power/generation evidence.
4. Search HOPS/HEP/HERA for connection, substation, and network-plan evidence.
5. Search HAKOM e-Operator for all named operators and telecom pivots.
6. Search cloud official region/edge pages for hyperscaler evidence.
7. Search EOJN/TED for public-sector HPC, AI, colocation, and datacenter construction awards.
8. Only then use trade/aggregator lists to fill likely missed small colo sites.

### 3.2 Generic Query Templates

Discovery:

```text
"{county_or_city}" ("podatkovni centar" OR "data centar" OR "računalni centar") (gradnja OR izgradnja OR otvoren OR otvorenje OR investicija OR kampus)
"{county_or_city}" ("AI data centar" OR "umjetna inteligencija" OR "HPC" OR "visokoučinkovito računarstvo") (infrastruktura OR centar OR nabava)
"{municipality}" "{operator}" "data centar"
```

Permit:

```text
"{county_or_city}" ("data centar" OR "podatkovni centar") ("građevinska dozvola" OR "lokacijska dozvola" OR "uporabna dozvola")
site:edozvola.gov.hr/notice-board "{municipality}" "data centar"
site:mpgi.gov.hr "{county}" "podatkovni centar"
"{operator}" ("građevinska dozvola" OR "uporabna dozvola" OR "lokacijska dozvola")
```

Energy/capacity:

```text
"{project}" (MW OR MVA OR kW OR "priključna snaga" OR "IT snaga")
"{project}" ("trafostanica" OR "TS" OR "priključenje na mrežu")
"{project}" ("agregat" OR "UPS" OR "hlađenje" OR "PUE")
```

Procurement:

```text
"{county_or_city}" ("data centar" OR "podatkovni centar") site:eojn.hr
"kolokacija" "Zagreb" site:eojn.hr
"računalni centar" "nabava" "Hrvatska"
"data-centre infrastructure" "Croatia" site:op.europa.eu
```

Status words:

- planned/early: **planirano**, **najavljeno**, **namjeravani zahvat**, **investicija**, **uvršten u strateške projekte**.
- permitting: **zahtjev**, **javni uvid**, **lokacijska dozvola**, **građevinska dozvola**, **rješenje**.
- construction: **početak radova**, **gradnja**, **izgradnja**, **dovršetak radova**.
- operational: **otvoren**, **pušten u rad**, **u funkciji**, **uporabna dozvola**, **komercijalni rad**.

---

## 4. County-by-County Enumeration Approach

Use the official Croatia division list: Zagreb County, Krapina-Zagorje, Sisak-Moslavina, Karlovac, Varazdin, Koprivnica-Krizevci, Bjelovar-Bilogora, Primorje-Gorski Kotar, Lika-Senj, Virovitica-Podravina, Pozega-Slavonia, Brod-Posavina, Zadar, Osijek-Baranja, Sibenik-Knin, Vukovar-Srijem, Split-Dalmatia, Istria, Dubrovnik-Neretva, Medimurje, Zagreb City.

### 4.1 High-Priority Counties

**Zagreb City**

- Highest density of live colo/network sites: Digital Realty/Altus ZAG1, DataBox, A1, Hrvatski Telekom, CIX/SRCE, local hosting providers.
- Query both **Grad Zagreb** and district/address terms: **Selska cesta**, **Savica**, **Zitnjak**, **Buzin**, **Sesvete**, **Neziceva**, **Veleslav Holjevac**, **Jankomir**.

```text
"Grad Zagreb" ("podatkovni centar" OR "data centar") ("građevinska dozvola" OR "uporabna dozvola")
site:edozvola.gov.hr/notice-board "Grad Zagreb" "data centar"
"Selska cesta" "data centar" Zagreb
"Savica" "DataBox" "data centar"
"Nežićeva" "A1" "data centar"
"Zagreb" "CIX2" "Digital Realty"
```

**Zagreb County**

- Search airport/logistics belt and satellite towns: **Velika Gorica**, **Buzin** (often administratively Zagreb/Velika Gorica depending site), **Samobor**, **Sveta Nedelja**, **Jastrebarsko**, **Kriz**, **Dugo Selo**, **Rugvica**. Aggregators mention Zagreb metro sites outside city; verify with eDozvola and county/city offices.

```text
"Zagrebačka županija" "data centar"
"Velika Gorica" ("data centar" OR "podatkovni centar") "građevinska dozvola"
"Jastrebarsko" "data centar"
"Križ" "DataCross" OR "PCK" "data centar"
```

**Varazdin**

- Strong non-Zagreb target: **DC North / CRATIS** in Varazdin, plus CIX third location. Verify operator official page, strategic-project news, local permits, and HOPS/HEP connection if capacity is material.

```text
"Varaždin" "DC North" "građevinska dozvola"
"Varaždinska županija" ("podatkovni centar" OR "data centar")
"CRATIS" "DC North" "uporabna dozvola"
"Varaždin" "CIX" "data centar"
```

**Medimurje**

- Border/interconnection logic near Hungary/Slovenia; search **Cakovec**, **Nedelišće**, **Prelog**, and energy/interconnector terms. No known major commercial DC seed found in initial sweep; treat as low-density but adjacent to Varazdin.

```text
"Međimurska županija" ("data centar" OR "podatkovni centar")
"Čakovec" "data centar"
"Prelog" "podatkovni centar"
```

**Sisak-Moslavina**

- Important because of 2026 trade-press claims around **Topusko / Pantheon** AI campus. Treat as **C/B lead until official permit, strategic-project, energy, or environmental documents are found**. Search Topusko, Petrinja, Sisak, Glina, Novska.

```text
"Topusko" ("Pantheon" OR "AI data centar" OR "data centar")
"Sisačko-moslavačka županija" "podatkovni centar"
site:edozvola.gov.hr/notice-board "Topusko" "data centar"
site:mzozt.gov.hr "Topusko" ("data centar" OR "umjetna inteligencija" OR "zahvat")
site:hops.hr "Topusko" "priključenje"
```

**Primorje-Gorski Kotar**

- Rijeka/Krk port, submarine/fiber, logistics, and university/HPC angle. Search **Rijeka**, **Kostrena**, **Omisalj**, **Krk**, **Matulji**, **Bakar**.

```text
"Primorsko-goranska županija" ("data centar" OR "podatkovni centar")
"Rijeka" ("data centar" OR "računalni centar") ("CARNET" OR "Sveučilište" OR "kolokacija")
"Krk" "data centar" "priključenje"
"Rijeka" "trafostanica" "data centar"
```

**Split-Dalmatia**

- Second-largest metro, university/public-sector IT, port/subsea/fiber. Search **Split**, **Solin**, **Kastela**, **Dugopolje**, **Trogir**, **Makarska**. Use local administrative bodies from MPGI list.

```text
"Splitsko-dalmatinska županija" ("data centar" OR "podatkovni centar")
"Split" ("data centar" OR "računalni centar") ("građevinska dozvola" OR "kolokacija")
"Dugopolje" "data centar"
site:eojn.hr "Split" "data centar"
```

**Osijek-Baranja**

- Eastern university/industrial/logistics target. Search **Osijek**, **Cepin**, **Antunovac**, **Beli Manastir**, **Darda**, **Nemetin**; include public-sector HPC/procurement terms.

```text
"Osječko-baranjska županija" ("data centar" OR "podatkovni centar")
"Osijek" ("računalni centar" OR "HPC" OR "kolokacija")
"Osijek" "građevinska dozvola" "data centar"
site:eojn.hr "Osijek" ("data centar" OR "računalni centar")
```

**Istria**

- Tourism, fiber/coastal, industrial parks; search **Pula**, **Rovinj**, **Porec**, **Umag**, **Labin**, **Pazin**.

```text
"Istarska županija" ("data centar" OR "podatkovni centar")
"Pula" "data centar"
"Pazin" "podatkovni centar"
```

**Zadar / Sibenik-Knin / Dubrovnik-Neretva**

- Coastal public-sector, tourism/edge, submarine/fiber, disaster recovery. Search city names plus **otok**, **luka**, **CARNET**, **kolokacija**, **ICT infrastruktura**.

```text
"Zadarska županija" ("data centar" OR "podatkovni centar")
"Šibensko-kninska županija" ("data centar" OR "podatkovni centar")
"Dubrovačko-neretvanska županija" ("data centar" OR "podatkovni centar")
"Dubrovnik" "računalni centar" "nabava"
```

### 4.2 Medium/Low-Density Counties

For Krapina-Zagorje, Karlovac, Koprivnica-Krizevci, Bjelovar-Bilogora, Lika-Senj, Virovitica-Podravina, Pozega-Slavonia, Brod-Posavina, Vukovar-Srijem:

- Search county Croatian adjective/name plus county seat and industrial-zone names.
- Add **poduzetnička zona**, **gospodarska zona**, **industrijska zona**, **brownfield**, **strateški projekt**, and **trafostanica** to catch campus proposals.
- Use eDozvola first; local business-park/news claims are often promotional.

Templates:

```text
"{county_hr}" ("data centar" OR "podatkovni centar" OR "računalni centar")
"{county_seat}" ("data centar" OR "podatkovni centar") ("građevinska dozvola" OR "lokacijska dozvola")
"{county_seat}" ("ICT infrastruktura" OR "HPC" OR "umjetna inteligencija") "nabava"
"{industrial_zone}" ("data centar" OR "podatkovni centar" OR "cloud")
site:edozvola.gov.hr/notice-board "{county_seat}" "data centar"
site:mzozt.gov.hr "{county_seat}" "data centar"
site:eojn.hr "{county_seat}" "računalni centar"
```

Croatian county names to use in queries:

| Manifest division | Croatian query form |
|---|---|
| Zagreb County | Zagrebačka županija |
| Krapina-Zagorje | Krapinsko-zagorska županija |
| Sisak-Moslavina | Sisačko-moslavačka županija |
| Karlovac | Karlovačka županija |
| Varazdin | Varaždinska županija |
| Koprivnica-Krizevci | Koprivničko-križevačka županija |
| Bjelovar-Bilogora | Bjelovarsko-bilogorska županija |
| Primorje-Gorski Kotar | Primorsko-goranska županija |
| Lika-Senj | Ličko-senjska županija |
| Virovitica-Podravina | Virovitičko-podravska županija |
| Pozega-Slavonia | Požeško-slavonska županija |
| Brod-Posavina | Brodsko-posavska županija |
| Zadar | Zadarska županija |
| Osijek-Baranja | Osječko-baranjska županija |
| Sibenik-Knin | Šibensko-kninska županija |
| Vukovar-Srijem | Vukovarsko-srijemska županija |
| Split-Dalmatia | Splitsko-dalmatinska županija |
| Istria | Istarska županija |
| Dubrovnik-Neretva | Dubrovačko-neretvanska županija |
| Medimurje | Međimurska županija |
| Zagreb City | Grad Zagreb |

---

## 5. Evidence Grading and Verification

### 5.1 Grade by Data Point

| Evidence | Grade | Use |
|---|---|---|
| eDozvola/MPGI issued location/building/occupancy permit | A | Facility existence, lifecycle, legal location |
| MZOZT/MINGO PUO/OPUO/EIA documents | A | Early project lead, environmental and technical detail |
| HOPS/HEP/HERA grid documents | A | Power feasibility, substations, connection constraints |
| HAKOM e-Operator | A | Operator/network-provider status |
| EOJN/TED procurement notices and awards | A | Public-sector projects, ICT/HPC/data-center works |
| Operator official facility page | A- for existence, B for capacity unless technical certificate or filing supports it | Live-site seed |
| CIX/SRCE official IXP location notice | A for CIX location, B for facility capacity | Interconnection evidence |
| DCD / strong trade press | B | Discovery and event confirmation |
| Baxtel/DataCenterMap/Datacenters.com/Cloudscene | C/B | Lead generation, never final capacity without verification |
| Local-government investment/promo article | C unless it links to a permit or official decision | Intent only |

### 5.2 Validation Recipe

For every candidate record:

1. Normalize project identity: operator ultimate parent, facility brand, legal entity, address/municipality, county, and phase.
2. Search Croatian and English names. Example: **Digital Realty Zagreb**, **Altus IT**, **ZAG1**, **Selska cesta 93**.
3. Require one A-grade source for location/status if possible: eDozvola permit, occupancy permit, environmental decision, HOPS/HEP connection, or official operator page.
4. Capacity is separate from existence. Prefer permit/EIA/grid/operator technical documents over aggregator MW. Mark marketing design capacity as **planned/design**.
5. Do not count:
   - AWS Croatia design facility as a cloud region or datacenter region.
   - Cloud/hosting service pages with no Croatian facility evidence.
   - CIX node by itself as a commercial datacenter unless the host facility is named.
   - Announced AI mega-campus claims unless permits, strategic-project decision, EIA, or power evidence exists.
6. Operational status: **uporabna dozvola**, official opening plus service availability, active CIX/PeeringDB presence at the facility, or operator service page are stronger than construction-start news.

### 5.3 Output Notes

Recommended record fields:

```json
{
  "country_code": "HR",
  "country_name": "Croatia",
  "division": "Zagreb City",
  "name": "Digital Realty ZAG1 / former Altus IT",
  "status": "operational",
  "capacity_mw": null,
  "developer": "Digital Realty",
  "source_urls": ["https://www.digitalrealty.com/data-centers/emea/zagreb", "https://www.cix.hr/en/faq"],
  "evidence_date": "2026-08-12",
  "evidence_grade": "A-/B",
  "notes": "Verify permit/occupancy record in eDozvola before assigning capacity."
}
```

For counties with no validated project, write `no_projects: true` only after eDozvola, MZOZT, HAKOM/operator, EOJN, and trade/aggregate sweeps are all negative.

---

## 6. Starter Seed List for Follow-Up Enumeration

Use these only as leads; each must be rechecked against official/primary evidence before becoming a final facility record.

- **Zagreb City**: Digital Realty ZAG1 / former Altus IT; DataBox; A1 Zagreb data center; Hrvatski Telekom Zagreb data center(s); SRCE/CIX host locations; smaller hosters.
- **Zagreb County**: Zagreb metro airport/logistics and satellite facilities reported by aggregators, including Buzin/Velika Gorica/Jastrebarsko/Kriz leads.
- **Varazdin**: DC North / CRATIS; CIX third location at DC North.
- **Sisak-Moslavina**: Topusko/Pantheon AI campus claim. Treat as unverified lead until official Croatian permit, strategic-project, EIA, or grid evidence is found.
- **Split-Dalmatia, Primorje-Gorski Kotar, Osijek-Baranja, Istria, Zadar, Dubrovnik-Neretva**: likely public-sector, university, edge, or DR-scale sites rather than hyperscale. Use procurement + permits.

Best first-pass order: **Zagreb City -> Zagreb County -> Varazdin -> Sisak-Moslavina/Topusko lead -> Split-Dalmatia -> Primorje-Gorski Kotar -> Osijek-Baranja -> Istria -> coastal counties -> remaining inland counties**.
