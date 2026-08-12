# BA Explorer Official - Bosnia and Herzegovina Datacenter Enumeration via Construction Permits, Regulators, Energy, Procurement, and Cloud Sources

Date: 2026-08-12. Scope: Bosnia and Herzegovina (BA), division-level enumeration across the 3 world-manifest.jsonl divisions: **Federation of Bosnia and Herzegovina (FBiH)**, **Republika Srpska (RS)**, and **Brcko District (BD)**. Angle: **official/regulatory/cloud-first methodology** for finding operational, planned, and proposed datacenter facilities. Reliability grades: **A** = official/primary source (permit authority, regulator, government, public procurement, operator official page, cloud-provider official region page), **B** = strong trade press or named-party business press, **C** = directory/aggregate/marketing-only lead.

> Final review note: key official, operator, procurement, energy-regulator, and cloud-region URLs were re-checked in August 2026. Some BiH portals are dynamic, redirecting, or intermittently unreachable from automated checks; where that was observed, this methodology treats the URL as a search surface and names the live fallback. Grade every record honestly; do not promote a lead to a facility without a primary record.

---

## 0. Bosnia and Herzegovina-specific frame

- **There is no national datacenter registry and no unified national building-permit database in BiH.** The census must be assembled by joining three largely separate regulatory stacks: (1) state-level (BiH) telecom/energy/procurement institutions, (2) entity-level and canton-level planning/permitting authorities, and (3) municipal/district permit offices. This is the single most important structural fact for enumeration: a building permit for a datacenter is issued at **cantonal (FBiH), municipal (RS), or District (BD) level**, while **telecom licensing is state-level (RAK)** and **electricity licensing is split between DERK (state), FERK (FBiH) and RERS (RS)**.
- **FBiH** is further split into **10 cantons**, each with its own spatial-planning law, ministry and permit practice, plus ~79 municipalities/"grad" units. There is no unified FBiH e-permit portal; you must poll cantonal ministries and municipal services. Key cantons for datacenters: **Sarajevo Canton** (capital; BH Telecom DC, federal institutions), **Herzegovina-Neretva** (Mostar; HT Eronet DC), **Central Bosnia** (Novi Travnik; Globalhost), **Tuzla Canton** (University of Tuzla datacenter concept), and **Zenica-Doboj** (old steelworks datacenter proposal).
- **RS** has one spatial-planning ministry (Ministarstvo za prostorno uređenje, građevinarstvo i ekologiju) and issues most permits through municipal/city "Odjeljenje za prostorno uređenje" offices; the older government host `vladars.net` redirects to the current `vladars.rs` portal. RS has pursued electronic permits, but `edozvola.vladars.net` was not a live search endpoint in this review; locate any current eDozvola/eUprava service from `vladars.rs` or municipal pages at enumeration time. Highest-yield RS cities: **Banja Luka** (m:tel/Telekom Srpske HQ, Integra Data Centar, Lanaco, RS government, ministry), Bijeljina, Doboj, Prijedor, Istočno Sarajevo, Trebinje.
- **Brcko District (BD)** is a single self-governing unit (208 km², one city). Permits come from the District government's Department for Spatial Planning and Property Affairs; the district runs its own laws, budget and procurement; the district utility **JP "Komunalno Brčko"** appears in DERK's electricity-trader register. Expect at most small telecom/municipal server rooms and any public-sector e-government hosting, not commercial colo.
- **Language matters**: use Bosnian/Croatian/Serbian (BCS) local terms, not just English: `data centar`, `data centri`, `centar podataka`, `podatkovni centar`, `kolokacija`, `telehousing`, `server sala`/`serverska sala`, `građevinska dozvola`, `urbanistička saglasnost`, `lokacijska informacija`, `lokacijski uslovi`, `upotrebna dozvola`, `ekološka dozvola`, `lokalna ekološka dozvola` (LEK), `studija uticaja na okoliš/životnu sredinu`, `trafostanica`, `agregat`, `UPS`, `rashladni sistem`, `hlađenje`, `protivpožarni sistem`. In RS also run **Cyrillic** variants (e.g., `центар података`, `грађевинска дозвола`, `употребна дозвола`).
- **Current high-confidence physical leads are small-market and telecom/government/utility focused, not hyperscale**: BH Telecom Data Centar (Sarajevo; colocation + DR site), HT Eronet Data Centar (Mostar; georedundant), LANACO Technology Center/Data Center (Banja Luka; operator/technology-center evidence), and Globalhost Data Center (Novi Travnik per current operator/directory pages). Integra Data Centar (Banja Luka) and m:tel Virtual Data Center are useful leads but need address/permit/operator confirmation before being counted as physical facilities. Planned/proposed leads include the RS state datacenter reported by BIRN/Detektor, University of Tuzla concept, Zenica old-steelworks proposal, BH Telecom modular datacenter tender, and BH Telecom-AWS "sovereign cloud" MoU. Directory-only leads require primary confirmation before counting.
- **No AWS/Azure/GCP/OCI public cloud region exists in BiH** in the official region lists checked in this pass. Treat local `cloud`, `Virtual Data Center`, `VPS` and "sovereign cloud" offerings as hosted/colo/cloud-service products unless a hyperscaler official page names BiH.

Lifecycle vocabulary (three regimes, keep separate fields):

```text
FBiH:  prostorni plan (kantonalni/općinski) < urbanistička saglasnost / lokacijska informacija < građevinska dozvola (općina/grad; federalno ministarstvo za objekte od značaja za FBiH) < upotrebna dozvola
RS:    prostorni plan < lokacijski uslovi < građevinska dozvola (jedinica lokalne samouprave; ministarstvo za objekte od republičkog značaja) < upotrebna dozvola
BD:    prostorni plan Distrikta < građevinska dozvola (Odjeljenje za prostorno planiranje i imovinsko-pravne poslove) < upotrebna dozvola
```

Promote a candidate to facility evidence only with: a building/use permit naming the site, an official operator opening/tender, an official government decision, an official energy-company project note, an official regulator record, or a named-site official operator page.

---

## 1. Core query vocabulary

### 1.1 Local-language (BCS) terms

```text
"data centar" +"Bosna i Hercegovina"
"data centri" +"BiH"
"centar podataka" OR "centri podataka"
"podatkovni centar"
"kolokacija" "data centar"
"telehousing"
"server sala" OR "serverska sala"
"građevinska dozvola" "data centar"
"urbanistička saglasnost" "data centar"
"lokacijska informacija" "data centar"
"lokacijski uslovi" "data centar"
"upotrebna dozvola" "data centar"
"ekološka dozvola" "data centar"
"lokalna ekološka dozvola" "data centar"
"studija uticaja na okoliš" "data centar"
"elaborat uticaja na životnu sredinu" "data centar"
"trafostanica" "data centar"
"agregat" "UPS" "data centar"
"hlađenje" OR "rashladni" "data centar"
"protivpožarni sistem" "server sala"
"digitalizacija" "data centar" "institucija"
"Vlada RS" "data centar"
"Vlada FBiH" "data centar"
"Brčko distrikt" "data centar"
"центар података" OR "грађевинска дозвола" "Република Српска"
```

### 1.2 English terms

```text
"Bosnia" "data center"
"Bosnia" "data centre"
"Bosnia and Herzegovina" "colocation"
"Sarajevo" "data center"
"Banja Luka" "data center"
"Mostar" "data center"
"Tuzla" "data center"
"Zenica" "data center"
"Brcko" "data center"
"Bosnia" "data center" "building permit"
"Bosnia" "data center" "grid connection"
"Bosnia" "cloud region" AWS Azure Google Oracle
```

### 1.3 Official-source query templates

Substitute `{entity}`, `{canton}`, `{municipality}`, `{operator}`, `{site}`, `{gazette}`.

```text
site:rak.ba ("registar operatora" OR "data centar")
site:derk.ba ("data centar" OR "registar")
site:javnenabavke.gov.ba "data centar"
site:ejn.gov.ba ("data centar" OR "server sala" OR "kolokacija")
site:ecjn.gov.ba "data centar"
site:fbihvlada.gov.ba "data centar"
site:fmpu.gov.ba "urbanistička saglasnost" "{entity}"
site:fmpu.gov.ba "data centar"
site:vladars.rs ("data centar" OR "центар података")
site:vladars.rs "грађевинска дозвола" "{entity}"
site:vlada.bdcentral.net ("data centar" OR "informaciona tehnologija")
site:ppipo.bdcentral.net ("građevinska dozvola" OR "ekološka dozvola" OR "lokacijski uslovi")
site:sluzbenilist.ba "data centar"
site:{canton-ministry-domain} "građevinska dozvola" "{entity}"
site:{municipal-domain} "građevinska dozvola" "data centar"
site:{municipal-domain} "upotrebna dozvola" "{operator}"
site:{municipal-domain} "urbanistička saglasnost" "{operator}"
site:bhtelecom.ba ("Data Centar" OR "kolokacija")
site:hteronet.ba ("data centar" OR "kolokacija")
site:mtel.ba ("Virtual Data Center" OR "data centar")
site:integradc.net ("data centar" OR "kolokacija")
site:lanaco.com ("data centar" OR "kolokacija" OR "cloud i data infrastruktura")
site:lanacocloud.com ("kolokacija" OR "data centar")
site:tehnoloskicentar.ba ("LANACO Data centar" OR "Tier 4")
site:tehnoloskicentar.com ("LANACO Data centar" OR "Tier 4")
site:global.ba "data centar"
site:bhix.net participants
```

---

## 2. Grade A official/regulatory backbone

### 2.1 State-level (BiH) institutions

Primary sources:

- **RAK - Regulatorna agencija za komunikacije BiH**: https://www.rak.ba/ . Grade A for electronic-communications regulation: operator registration, licensing decisions, market analysis, numbering, and public consultations. The site is indexed as the official RAK portal but may time out or return gateway errors to automated fetches; use browser search, cached snippets, and RAK document search when needed. Use it to build the telecom-operator universe (BH Telecom, HT Eronet / JP Hrvatske telekomunikacije d.d. Mostar, Telekom Srpske / m:tel, Telemach d.o.o. Sarajevo, plus ISPs) and then pivot each name to official pages, tenders, and permits. RAK publishes operator/market reports; it does not publish a datacenter registry.
- **Vijeće ministara BiH** (Council of Ministers): state digitalization and e-government decisions, budget items for state IT infrastructure; search `vijeceministara.gov.ba` (verify current domain) and state-gazette decisions.
- **IDDEEA - Agencija za identifikacione dokumente, evidenciju i razmjenu podataka BiH**: https://iddeea.gov.ba/ . Grade A/B lead for state-level critical IT infrastructure (CIPS/identity systems, data-exchange platform). IDDEEA runs major state databases; its hosting/DR arrangements are a legitimate internal-datacenter lead even though it does not publish a facility list.
- **Službeni glasnik BiH**: https://www.sluzbenilist.ba/ . Grade A for state laws/decisions and public-notice tenders. Also search the FBiH gazette (Službene novine FBiH) and RS gazette (Službeni glasnik RS) for entity-level acts; verify gazette URLs at enumeration time.
- Other state bodies with material IT estates to probe via procurement only: Central Bank of BiH (cbbh.ba), Indirect Taxation Authority (UIO), Pension/Health funds, and the Ministry of Communications and Transport of BiH (`mkt.gov.ba`, which returned a server error in this review, so use search and procurement fallbacks). These run internal server rooms/DR, not commercial colo.

Extraction fields for state records: authority, document type, decision number, date, subject, budget/investment value, procuring entity, location references.

### 2.2 Federation of BiH (FBiH) - federal and cantonal planning/permitting

Primary sources:

- **Federalno ministarstvo prostornog uređenja (FMPU)**: https://fmpu.gov.ba/ and urbanistička dozvola process page https://fmpu.gov.ba/urbanisticka-dozvola/ . Grade A for `urbanistička saglasnost`/`lokacijska informacija` for objects of Federation-wide significance (per Uredba 32/14 and successors). In FBiH, urbanistička saglasnost is issued at cantonal level on the basis of the opinion of the municipal service; the federal ministry handles objects of significance for the Federation.
- **Vlada FBiH portal**: https://fbihvlada.gov.ba/ . Grade A for government decisions, ministry competences, and budget items (search `data centar`, `digitalizacija`, `informaciona infrastruktura`).
- **Cantonal ministries of spatial planning** (10 cantons). Each canton has its own law (e.g., Zakon o prostornom uređenju Kantona Sarajevo, text at https://www.paragraf.ba/propisi/kantona-sarajevo/zakon-o-prostornom-uredjenju-kantona-sarajevo.html ) and ministry. Municipal offices then issue the actual building/use permits; example guide: Novo Sarajevo municipality urbanistička saglasnost process PDF at https://novosarajevo.ba/userfiles/doc/Pribavljanje%20urbanisti%C4%8Dke%20saglasnosti.pdf .
- **Municipal permit services**: every FBiH municipality/grad publishes (to varying degrees) permit decisions, plans, and urbanističko-tehnički uslovi. Sarajevo city municipalities (Centar, Stari Grad, Novo Sarajevo, Novi Grad, Ilidža), Mostar, Tuzla, Zenica and Bihać are the highest-yield targets.

Cantons and focus (10):

| Canton (seat) | Datacenter relevance | Official-first route |
|---|---|---|
| Sarajevo (Sarajevo) | Capital; BH Telecom DC + colocation, federal institutions, universities, banks | KS Ministry of Spatial Planning, Sarajevo municipal services, BH Telecom official pages, FMPU, FBiH gov, e-Nabavke |
| Tuzla (Tuzla) | University of Tuzla datacenter concept (2025, presented to TK Government) | TK Government/ministry pages, Univerzitet u Tuzli procurement, klix.ba coverage, municipal permits |
| Zenica-Doboj (Zenica) | Political proposal for datacenter at Stara Željezara (2026); steelworks/industrial-park energy context | ZDK ministry/municipal permits, zenicablog/press, EPBiH grid connection records |
| Herzegovina-Neretva (Mostar) | HT Eronet DC (Mostar) | HT Eronet official pages, Mostar municipal permits, EPHZHB grid records |
| Central Bosnia (Travnik/Novi Travnik) | Globalhost current operator/directory evidence points to Novi Travnik; also institutional server rooms | Globalhost official pages, Travnik/Novi Travnik municipal permits, SBK ministry, e-Nabavke |
| Una-Sana (Bihać), Posavina (Orašje), Bosnian Podrinje (Goražde), West Herzegovina (Široki Brijeg), Canton 10 (Livno) | Low yield; telecom nodes and municipal e-gov only | Compact municipal-permit sweep + procurement + RAK operators |

Municipal query template:

```text
site:{municipal-domain} "{operator}" "građevinska dozvola"
site:{municipal-domain} "{operator}" "upotrebna dozvola"
site:{municipal-domain} "{operator}" "urbanistička saglasnost"
site:{municipal-domain} "data centar"
site:{municipal-domain} "server sala"
site:{municipal-domain} "agregat" "UPS"
site:{municipal-domain} "trafostanica" "{operator}"
site:{municipal-domain} "{industrial_zone}" "data centar"
"{municipality}" "građevinska dozvola" "data centar"
"{municipality}" "urbanistička saglasnost" "data centar"
```

### 2.3 Republika Srpska (RS) - ministry, municipalities, e-permitting

Primary sources:

- **Ministarstvo za prostorno uređenje, građevinarstvo i ekologiju RS**: RS government portal https://vladars.rs/ (the older `https://www.vladars.net/` redirects here; ministry pages remain under `Vlada/Ministarstva` paths). Grade A for entity-level spatial-planning law, building regulations, environmental (`ekološka`) dozvole, and supervision of municipal permitting.
- **Municipal/city "Odjeljenje za prostorno uređenje" offices**: issue most RS building permits. Public guides exist, e.g., Grad Prnjavor permit guide PDF https://gradprnjavor.com/wp-content/uploads/2024/08/Gradjevinska-dozvola-latinica-2024.pdf and Grad Zvornik investor guide https://gradzvornik.org/wp-content/uploads/2024/12/v_gradjevinske_dozvole_srb_int.pdf (Grade A/B for procedure, useful for discovering how permit records are published in RS municipalities). Grad Banja Luka is the highest-yield municipality (m:tel HQ, Integra DC, Lanaco, RS government district).
- **RS e-permitting (eDozvola/eUprava RS)**: RS has promoted electronic building permits; the older address `edozvola.vladars.net` failed DNS resolution in this review, so locate the live system from `vladars.rs`, `euprava`, or municipal pages at enumeration time. If a working e-permit portal exists, use it to search `data centar`, `server sala`, `trafostanica`; otherwise poll municipal pages and e-Nabavke.
- **RS digitalization ministry**: Ministarstvo za naučnotehnološki razvoj, visoko obrazovanje i informaciono društvo on `vladars.rs` - Grade A for RS e-government, the planned RS state datacenter, and ICT strategy documents (search `data centar`, `digitalizacija`, `eUprava`).
- **RERS - Regulatorna komisija za energetiku RS**: https://reers.ba/ . Grade A for RS electricity licensing.

RS query templates:

```text
site:vladars.rs "data centar"
site:vladars.rs "центар података"
site:vladars.rs "грађевинска дозвола" "{entity}"
site:vladars.rs "lokacijski uslovi" "{entity}"
site:vladars.rs "ekološka dozvola" "{entity}"
site:{rs-municipal-domain} "građevinska dozvola" "data centar"
site:{rs-municipal-domain} "upotrebna dozvola" "{operator}"
"Banja Luka" "data centar" "građevinska dozvola"
"Bijeljina" OR "Doboj" OR "Prijedor" OR "Trebinje" "data centar"
```

### 2.4 Brcko District (BD)

Primary sources:

- **Vlada Brčko distrikta BiH**: https://vlada.bdcentral.net/ and https://www.vlada.bdcentral.net/ are the government publication surfaces, though automated checks may time out. Grade A for District government decisions, departments, and e-government when the page/document is retrieved. The Department for Spatial Planning and Property Affairs uses the `ppipo.bdcentral.net` publication surface and issues BD building/environment permits.
- **District e-government/procurement**: BD is a contracting authority on e-Nabavke (ejn.gov.ba); search `Brčko distrikt` + `data centar`, `server sala`, `UPS`, `agregat`, `informacioni sistem`.
- **JP "Komunalno Brčko" d.o.o. Brčko distrikt**: appears in DERK's trader register; use for district utility/energy context (Grade A/B for district grid identity, not a datacenter).

BD query templates:

```text
site:vlada.bdcentral.net ("data centar" OR "informaciona tehnologija")
site:vlada.bdcentral.net "građevinska dozvola" "{entity}"
site:ppipo.bdcentral.net ("građevinska dozvola" OR "ekološka dozvola" OR "lokacijski uslovi") "{entity}"
"Brčko distrikt" "data centar"
"Brcko district" "data center"
"Brčko" "server sala" OR "kolokacija"
```

### 2.5 Energy and grid pipeline

Primary sources:

- **DERK - Državna regulatorna komisija za električnu energiju (SERC)**: https://www.derk.ba/ . Grade A for state-level electricity regulation, license registries (including a public `Registar trgovaca` PDF under DocumentsPDFs), tariffs, and cross-entity issues. DERK licenses transmission; generation/supply/distribution are licensed by FERK and RERS.
- **FERK (FBiH)**: https://www.ferk.ba/ (verify domain at enumeration time). Grade A for FBiH electricity licenses, decisions and public hearings.
- **RERS (RS)**: entity regulator; see 2.3.
- **Elektroprenos BiH** (transmission company; current reachable site `https://www.elprenos.ba/Naslovna.html`) and **NOSBiH** (`https://www.nosbih.ba/`, independent system operator). Grade A for transmission development plans and substation projects - context, not datacenter proof.
- **DSOs per entity**: Elektroprivreda BiH (FBiH), Elektroprivreda HZHB (FBiH/HN canton), ERS group with Elektrokrajina/Elektro Doboj/Elektro Bijeljina (RS). Grade A for grid-connection context, closed distribution systems (zatvoreni distributivni sistem) in industrial parks, and any utility datacenter/DR projects (e.g., EPBiH ICT infrastructure announcements).
- Grid-connection evidence terms: `elektroenergetska saglasnost`, `priključak na mrežu`, `trafostanica`, `priključna snaga`, `MW`, `MVA`, `kV`.

Energy query templates:

```text
site:derk.ba "licenca" "{entity}"
site:derk.ba "zatvoreni distributivni sistem"
site:ferk.ba "licenca" "{entity}"
site:reers.ba "licenca" "{entity}"
"data centar" "trafostanica" "BiH"
"data centar" "MW" "Bosna i Hercegovina"
"data centar" "priključna snaga" "BiH"
"Elektroprenos" ("data centar" OR "DR centar")
"Elektroprivreda BiH" "data centar"
"Elektroprivreda RS" "data centar"
```

Use energy records for siting/capacity context only. Do not infer a datacenter from a substation or a license alone; promote only when a record names a datacenter project, owner, or facility.

### 2.6 Environmental permitting

Primary sources:

- **FBiH**: integrated environmental permits (`okolišna dozvola`) from Federalno ministarstvo okoliša i turizma (`https://fmoit.gov.ba/`); small installations need `lokalna ekološka dozvola` (LEK) from cantonal environment ministries. EIA studies (`studija uticaja na okoliš`) may be triggered by generator/fuel/cooling installations.
- **RS**: `ekološka dozvola` and EIA (studija uticaja na životnu sredinu) from the Ministry for Spatial Planning, Construction and Ecology; public guides exist (see rars-msp.org permit-guide PDF from 2020 in this pass).
- **BD**: District environment department under the District government.

Search terms:

```text
"lokalna ekološka dozvola" "data centar"
"okolišna dozvola" "server sala" OR "data centar"
"ekološka dozvola" "data centar"
"studija uticaja na okoliš" "{operator}"
"elaborat uticaja na životnu sredinu" "{operator}"
"agregat" "dizel" "server sala" "BiH"
"rashladni" "data centar" "BiH"
```

What to extract: applicant/owner, project location, parcels, authority, decision date, generator count/fuel, UPS/battery, cooling system, transformer/substation, noise/emission conditions, EIA required vs not.

### 2.7 Public procurement (e-Nabavke)

Primary sources:

- **Agencija za javne nabavke BiH**: https://javnenabavke.gov.ba/ . Grade A for procurement law and portal ownership.
- **Portal e-Nabavke**: https://www.ejn.gov.ba/ (search interface). Grade A for all BiH public tenders: ministries, cantons, municipalities, public companies (telcos are partially subject to procurement rules), universities, hospitals, utilities. Search terms: `data centar`, `server sala`, `kolokacija`, `DR lokacija`, `UPS`, `agregat`, `klimatizacija`, `hlađenje`, `protivpožarni`, `informacioni sistem`, `hardver`, `virtualizacija`.
- **Centralized procurement system (ISCN)**: https://ecjn.gov.ba/bs-latn-ba/about . Grade A for framework agreements and centralized buys that often bundle IT infrastructure.

Procurement query templates:

```text
site:ejn.gov.ba "data centar"
site:ejn.gov.ba "server sala"
site:ejn.gov.ba "kolokacija"
site:ejn.gov.ba "UPS" "agregat"
site:ejn.gov.ba "trafostanica" "{entity}"
site:ejn.gov.ba "digitalizacija" "{ministry}"
site:ecjn.gov.ba "data centar"
"javna nabavka" "data centar" "BiH"
```

Procurement is Grade A for intent/scope and a strong facility lead when it names a physical site or building works (`radovi`, `izgradnja`, `adaptacija prostora za servere`); distinguish equipment-only buys from construction.

### 2.8 RAK operator universe and IXP evidence

- Use RAK to enumerate licensed operators: BH Telecom d.d. Sarajevo, JP Hrvatske telekomunikacije d.d. Mostar (HT Eronet), Telekom Srpske a.d. Banja Luka (m:tel brand), Telemach d.o.o. Sarajevo, plus fixed ISPs and hosting firms (e.g., Blicnet, Logosoft, Lanaco, Mikroelektronika, Globalnet - verify current names/status via RAK register). Pivot each to official pages, tenders and permits.
- **BHIX - Bosnian Internet Exchange**: https://bhix.net/ . Grade A for the IXP itself (Sarajevo-area; participants list is public); peering participants are a useful operator/colo discovery surface. Check PeeringDB for additional BiH facilities and exchanges.

---

## 3. Cloud region and operator pipeline

### 3.1 Official cloud-region checks

| Provider | Official page | BiH signal |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No BiH public region found in this pass. BH Telecom-AWS "sovereign cloud" MoU (2025) is a local hosting/edge arrangement, not an AWS region. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No BiH public region found in this pass. |
| Google Cloud | https://cloud.google.com/about/locations | No BiH public region found in this pass. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No BiH public region found in this pass. |

Rule: a local `cloud`, `VPS`, `Virtual Data Center`, or reseller page is not hyperscale-region evidence unless the provider's official region page names BiH.

### 3.2 Operator and colo leads (official pages)

| Lead | URL / source surface | Municipality | Evidence use |
|---|---|---|---|
| BH Telecom Data Centar (colo + DR) | https://www.bhtelecom.ba/usluge-za-poslovne-korisnike/2019/09/nova-cloud-usluga-kolokacija-u-data-centru-bh-telecoma/ | Sarajevo | Grade A operator page: Data Centar described as primary DR site in BiH, colocation incl. racks, cooling, UPS, managed services. |
| BH Telecom modular datacenter tender | https://seenews.com/news/bosnias-bh-telecom-opens-tender-for-works-on-modular-data-centre-1235646 | Sarajevo | Grade B (SeeNews, Sep 2023) for tender on modular DC construction; seek BH Telecom tender page/contract award for Grade A. |
| BH Telecom-AWS sovereign cloud MoU | https://btw.media/en/bh-telecom-and-aws-launch-sovereign-cloud ; https://www.telecomrevieweurope.com/articles/telecom-operators/bh-telecom-aws-to-power-bosnias-digital-future/ ; https://connectingregion.com/news/bosnias-digital-future-with-amazon/ ; https://capacityglobal.com/news/bh-telecom-aws-bosnia/ | Sarajevo | Grade B (Jun 2025) MoU for sovereign cloud for public sector; service-level lead, not a new facility by itself. |
| HT Eronet Data Centar | https://www.hteronet.ba/digitalna-rjesenja/ht-eronet-data-centar-pg368 | Mostar | Grade A operator/service page: georedundant HT Eronet data center service; use permits/procurement for site-specific construction proof. |
| HT Eronet kolokacija poslužitelja | https://www.hteronet.ba/poslovni-korisnici/kolokacija-posluzitelja-pg64 (also indexed at `/digitalna-rjesenja/kolokacija-posluzitelja-s116`) | Mostar | Grade A operator/service page: server colocation with redundant cooling/power; use permits/procurement for site-specific construction proof. |
| m:tel Virtual Data Center (service) | https://mtel.ba/Poslovni/ICT/Cloud-infrastruktura/Virtual-Data-Center ; press note https://mtel.ba/Press-centar/a14296-Prezentacija-usluga-u-m-tel-Biznis-centru.html | Banja Luka | Grade B/C service lead only until a physical m:tel/Telekom Srpske facility with address appears. |
| Integra Data Centar (Integra Inženjering d.o.o. Banja Luka) | https://integradc.net/ ("Poslovni centar Integra DC") | Banja Luka | Grade B/C company-site colo lead; seek building permit/address via Grad Banja Luka permits and e-Nabavke. |
| LANACO Technology Center / Data Center | https://www.tehnoloskicentar.ba/ (also `https://tehnoloskicentar.com/`); https://www.lanaco.com/bs/cloud-i-data-infrastruktura ; https://lanacocloud.com/cloud.php | Banja Luka | Grade B operator/company evidence for a named LANACO data center and cloud/colo offers; promote to Grade A only with permit, procurement, official opening, or audited certification/source document. |
| Globalhost Data Center | https://www.global.ba/dc.php ; https://www.global.ba/kolokacija.php ; https://www.global.ba/en/kolokacija.php | Novi Travnik / Central Bosnia Canton | Grade B company-site evidence: current Globalhost pages describe a data center/colocation in Novi Travnik. Confirm address and permits before Grade A. |

### 3.3 State and public-sector planned projects

- **RS state datacenter (planned)**: BIRN/Detektor reporting "Republika Srpska planira data centar po uzoru na Srbiju" https://detektor.ba/2026/05/14/republika-srpska-planira-izgadnju-data-centra-po-uzoru-na-srbiju/ and earlier/regional mirrors such as BIRN/N1. Grade B for intent; keep status `planned` until site/permits/tender appear. Pivot to `vladars.rs` (MNTRI) and e-Nabavke for tenders.
- **University of Tuzla datacenter (concept)**: Klix https://www.klix.ba/vijesti/bih/pogledajte-kako-bi-trebao-izgledati-data-centar-u-tuzli-za-digitalno-umrezavanje-svih-institucija/250403114 (Apr 2025) - concept design presented to Tuzla Canton Government; Grade B/C intent; track TK government and university procurement.
- **Zenica old steelworks datacenter (political proposal)**: https://www.zenicablog.com/sdp-zenica-stara-zeljezara-zenica-nova-sansa/ (Jan 2026) - Grade C political proposal; do not count without government/planning action.
- **State institutional IT estates**: IDDEEA (https://iddeea.gov.ba/), Central Bank of BiH, UIO - probe via e-Nabavke and gazette decisions for server-room/DR projects (Grade A when procurement names them).

### 3.4 Trade and business press (Grade B leads)

- Klix (https://www.klix.ba/), Avaz (https://avaz.ba/), Oslobođenje (oslobodjenje.ba), FENA (fena.ba), Nezavisne novine (https://www.nezavisne.com/), Glas Srpske (glassrpske.com), Capital.ba, Akta.ba, SEEbiz (seeebiz.eu), SeeNews (seenews.com), BIRN (birn.rs), btw.media, telecomrevieweurope.com, capacityglobal.com, Data Center Dynamics, US trade.gov country guide (https://www.trade.gov/country-commercial-guides/bosnia-and-herzegovina-telecommunications-industry). Verify every claim against official pages.

---

## 4. Division enumeration workflow (world-manifest.jsonl divisions)

For every division and municipality:

1. **FBiH**: poll FMPU (urbanistička saglasnost/lokacijska informacija) -> cantonal ministry of spatial planning -> municipal permit office (građevinska/upotrebna dozvola, urbanističko-tehnički uslovi). Search by operator legal entity AND by `data centar`/`server sala`/`trafostanica` terms AND by address/parcel.
2. **RS**: poll RS ministry (`vladars.rs`) -> municipal Odjeljenje za prostorno uređenje (građevinska/upotrebna dozvola, lokacijski uslovi); use e-permitting portal if live (verify).
3. **BD**: poll District government (`vlada.bdcentral.net`) -> Department for Spatial Planning and Property Affairs (`ppipo.bdcentral.net`).
4. For all divisions: search e-Nabavke (ejn.gov.ba) + ecjn.gov.ba for tenders naming `data centar`, `server sala`, `kolokacija`, `UPS`, `agregat`, `izgradnja`; search DERK/FERK/RERS for licenses/closed distribution systems; search environmental authorities for EIA/LEK/ekološka dozvola; search RAK for operators; search state/entity digitalization strategies and budgets.
5. Promote a candidate only after a primary record confirms facility/project. Keep separate fields for physical site, administrative owner, operator/service brand, stage, and evidence grade.

Division priority table:

| Division | High-yield places | Approach and expected yield |
|---|---|---|
| Federation of BiH (FBiH) | Sarajevo (BH Telecom DC, federal institutions), Mostar (HT Eronet DC), Novi Travnik (Globalhost), Tuzla (Univerzitet u Tuzli concept), Zenica (steelworks proposal) | Cantonal+municipal permit sweep, operator pages, e-Nabavke. Highest yield of the three divisions: expect ~5-8 verifiable leads (operator DCs, hosting colo, public-sector server rooms). |
| Republika Srpska (RS) | Banja Luka (m:tel/Telekom Srpske, Integra DC, LANACO, RS gov), Bijeljina, Doboj, Prijedor, Istočno Sarajevo, Trebinje | RS ministry + municipal permits + eDozvola/eUprava if live + `vladars.rs` digitalization + e-Nabavke + RERS. Expect ~4-6 leads (telco/cloud services, Integra/LANACO, planned RS state DC). |
| Brcko District (BD) | Brčko city | District government + Department permits + e-Nabavke + JP Komunalno Brčko. Low yield: expect 0-2 internal/municipal server-room leads. |

Generic municipality query pattern:

```text
("{municipality}" OR "{municipal-local-name}") "data centar"
("{municipality}" OR "{municipal-local-name}") "server sala"
("{municipality}" OR "{municipal-local-name}") "kolokacija"
("{municipality}" OR "{municipal-local-name}") "građevinska dozvola" "data centar"
("{municipality}" OR "{municipal-local-name}") "urbanistička saglasnost" "data centar"
("{municipality}" OR "{municipal-local-name}") "upotrebna dozvola" "data centar"
("{municipality}" OR "{municipal-local-name}") "trafostanica" "data centar"
("{municipality}" OR "{municipal-local-name}") "agregat" "data centar"
site:{municipal-domain} "data centar"
site:{municipal-domain} "server sala"
site:{municipal-domain} "UPS"
site:{municipal-domain} "{operator}"
```

---

## 5. Reliability rules and pitfalls

Reliability:

- **Grade A**: issued permit (građevinska/upotrebna/urbanistička saglasnost) from cantonal/municipal/District authority or FMPU; RS ministry decision; DERK/FERK/RERS license or decision; RAK record; official operator datacenter/tender page; government session material or official procurement document (e-Nabavke); official hyperscaler region page.
- **Grade B**: SeeNews, BIRN, Klix, Avaz, Nezavisne, Glas Srpske, Capital, Akta, SEEbiz, btw.media, telecomrevieweurope, capacityglobal, Bloomberg Adria, company statements reported by named press.
- **Grade C**: DataCenterMap, Datacenters.com, Cloudscene, PeeringDB (as directory), LinkedIn, SEO/hosting pages, reseller `cloud`/`Virtual Data Center` offers, political proposals without government action.

Pitfalls:

- **Three legal regimes**: a permit in FBiH does not imply RS/BD coverage and vice versa; record the issuing division/canton/municipality.
- `Data centar` can mean a retail computer shop, an institutional server room, a telecom network facility, a cloud-service product, or a true colocation facility. Capture facility type; do not merge.
- Telecom colocation (RAK reference offers, exchange colo) can mean regulated access to exchanges/MDFs, not commercial datacenter colo.
- m:tel's `Virtual Data Center` is a cloud service (VPS/NaaS), not proof of a physical facility; Globalhost/LANACO/Integra pages are company-site evidence - confirm addresses/permits before Grade A enumeration.
- Government feasibility studies, MoUs (e.g., BH Telecom-AWS) and political proposals (Zenica) are Grade A/B for intent but not for operational status. Require permit, tender, construction, handover, or opening evidence.
- **Fragmented portals**: FBiH has no unified e-permit database; many municipal sites publish scanned PDFs (use OCR), year indexes, or nothing at all. Budget time per canton.
- Cyrillic/Latin and diacritic variants are all needed: `data centar`/`центар података`, `građevinska dozvola`/`грађевинска дозвола`, `Brčko`/`Brcko`, `Široki Brijeg`/`Siroki Brijeg`.
- Old and new construction procedures coexist; legacy records may say `odobrenje za građenje` or reference pre-2010s laws - do not discard.
- `edozvola.vladars.net` failed DNS in this review; always re-verify RS e-permit URLs from `vladars.rs`, eUprava pages, and municipal permit pages at enumeration time.
