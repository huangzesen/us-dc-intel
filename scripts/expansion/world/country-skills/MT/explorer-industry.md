# MT Explorer Industry - Malta Datacentre Enumeration via Operators, Trade Press, Directories, and Locality Query Patterns

Date: 2026-08-12. Scope: Malta (MT), 68 local-council divisions. Angle: **industry/operator-led discovery**. Reliability grades: **A** = operator official page, public-sector page, regulatory/permit source, stock-exchange/company filing; **B** = trade press or reputable local business press; **C** = directory/marketplace/SEO hosting page or unverified aggregate.

---

## 0. Market shape

- Malta's datacentre market is small and service-provider led. The best first pass is an **operator sweep**, then a **locality/permit verification pass** in PA/Gazette/ERA records.
- Confirmed public leads cluster around Birkirkara, Qormi/Handaq/Mriehel, Santa Venera, Kalkara/SmartCity, Swieqi/Madliena, Marsa, Gzira, Żejtun/Bulebel, Msida, and Rabat Gozo/Victoria.
- Industry pages often say `Malta data centre` without a street address. Assign locality only after the operator page, ERA permit, PA record, or a consistent address directory confirms it.
- Malta has strong demand from iGaming, fintech, telecom, government, and disaster recovery. These sectors generate many cloud/VPS/hosting pages that do **not** prove a physical facility.

---

## 1. Operator and vendor sweep

### 1.1 Priority operators/facilities

| Operator / facility lead | Official / useful URL | Localities to check | Evidence use |
|---|---|---|---|
| MITA Data Centre | https://mita.gov.mt/ and https://mita.gov.mt/portfolio/facilities-at-data-centre/ | Santa Venera; also Gozo/Victoria procurement leads | Grade A public-sector hosting facility; capacity usually undisclosed. |
| BMIT Technologies | https://www.bmit.com.mt/datacentre/ | Qormi/Handaq, Kalkara/SmartCity, Żejtun/Bulebel | Grade A for BMIT's Malta datacentre platform and Handaq/SmartCity labels. Pair with PA/Gazette and investor/stock-exchange docs for site details. |
| BMIT Żejtun | https://www.bmit.com.mt/blog/bmit-announces-new-e10m-data-centre-facility/ | Żejtun / Bulebel Industrial Estate | Official announcement: purpose-built Tier III-target facility, more than 400 racks, under construction in 2019; verify operational/current details separately. |
| Melita Business | https://www.melitabusiness.com/hosting-cloud/melita-data-centre/ and https://www.melitabusiness.com/hosting-cloud/secure-facilities/ | Swieqi/Madliena; Qormi/Mriehel secondary site | Grade A for Melita's own facility claims; ERA EP1255/22 confirms generators at Madliena/Swieqi. |
| GO plc | https://www.go.com.mt/wholesale/data/ and https://www.go.com.mt/business/solutions/hosting-services/ | Birkirkara and Marsa leads | Grade A for GO official hosting/colo service; directory evidence often supplies Marsa address, so verify locality in PA/operator documents where possible. |
| Epic Malta | https://www.epic.com.mt/business/solutions/data-centre/ | Santa Venera directory lead; Luqa is mainly head office | Epic official service page confirms datacentre/colo/DR offering; facility address is usually directory-level unless primary evidence is found. |
| Continent 8 Malta | https://www.continent8.com/locations/emea/malta/ | Santa Venera and second Malta facility leads | Official page says access to two diverse co-location facilities in Malta; use directories/PA for locality but grade address as C unless primary. |
| CSL Data Centre Services | https://www.csl.com.mt/ and https://www.csl.com.mt/contact-us/ | Birkirkara / Central Business District | Official page describes its own Tier 3-rated carrier-neutral datacentre facilities and 2,000 sqm rack-space capacity. |
| Malta Internet Exchange (MIX) | https://www.mix.net.mt/ and https://www.nic.org.mt/about/ | Msida / University of Malta | Interconnection lead, not a colo facility by itself. Use for Msida network-infrastructure context. |
| University of Malta / Msida directory lead | University and MIX sources; directories such as Cloudscene/DataCenterMap | Msida | Treat as C until an official University/MITA/PA source confirms a physical datacentre service. |
| Heritage Malta data centre | https://heritagemalta.mt/news/new-data-centre-at-heritage-malta-headquarters/ | Kalkara / Bighi | Official 2025 public-sector operational lead; likely internal/archive facility, not commercial colo. |
| Enemalta / Streamcast underground DC | https://enemalta.com.mt/2018/04/12/collaboration-streamcast-enemalta-moves-ahead-rapidly/ | Marsa | Official project-launch evidence but later reporting says the project failed; status should be `rejected`/`abandoned` unless fresh primary evidence shows operation. |

Operator search templates:
```
"{operator}" "Malta" "data centre"
"{operator}" "Malta" "data center"
"{operator}" "Malta" datacentre
"{operator}" "{locality}" "data centre"
"{operator}" "{locality}" "colocation"
"{operator}" "{locality}" "rack"
"{operator}" "{locality}" "Tier III"
"{operator}" "{locality}" "ISO 27001"
"{operator}" "{locality}" "PCI DSS"
"{operator}" "{locality}" "generator"
```

Targeted operator/locality strings:
```
"BMIT" "Handaq" "data centre"
"BMIT" "SmartCity" "data centre"
"BMIT" "Zejtun" "data centre"
"BMIT" "Bulebel" "data centre"
"Melita" "Madliena" "data centre"
"Melita" "Mriehel" "data centre"
"GO" "Birkirkara" "data centre"
"GO" "Marsa" "data centre"
"Epic" "Canon Road" "data centre"
"Continent 8" "Malta DC2"
"CSL" "Dun Karm Street" "data centre"
"MIDI" "Gzira" "DC1"
"SIS" "North Shore" "Gzira" "data centre"
"Gozo Data Centre" "Victoria"
```

### 1.2 IXOne and Aria handling

The brief requested attention to `Malta Ixone` and `Aria`. Targeted searches for `IXOne Malta data centre`, `Ixone Malta colocation`, `Aria Malta data centre`, and `Aria Malta colocation` did not produce a verifiable Malta datacentre operator or facility in this pass. Treat these as **name-disambiguation traps** unless a future source gives a company registration number, facility address, or operator page. Keep them in the negative-query log so later enumerators do not promote false positives from unrelated people, music/ARIA terms, or generic web noise.

Negative-control queries:
```
"IXOne" "Malta" "data centre"
"IXOne" "Malta" colocation
"Ixone" "data center" "Malta"
"Aria" "Malta" "data centre"
"Aria" "Malta" colocation
"Aria" "BMIT" "Malta"
```

---

## 2. Trade press and secondary sources

Use these to discover project names, historical status, rack counts, investment value, and locality. Verify in PA/ERA/operator/MBR before final enumeration.

| Source | URL | Malta use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Strongest international trade source for BMIT Żejtun and Enemalta/Streamcast Marsa project history. | B |
| Times of Malta | https://timesofmalta.com/ | Good for MITA launch history, BMIT announcements, Streamcast/Marsa reporting, and local planning/business context. | B |
| MaltaToday | https://www.maltatoday.com.mt/ | Useful for BMIT SmartCity, Streamcast abandoned-project/court reporting, and PA/environment issues. | B |
| TVM News / PBS | https://tvmnews.mt/ | Useful local public broadcaster source for BMIT Żejtun and government-linked technology projects. | B |
| The Malta Independent | https://www.independent.com.mt/ | Useful for local project announcements and Streamcast/Enemalta history. | B |
| Malta Stock Exchange announcements / Borza Malta | https://borzamalta.com.mt/ | Grade A/B for listed-company disclosures such as BMIT/Malta Properties transactions and property details. | A/B |
| DataCenterMap | https://www.datacentermap.com/malta/ | Best open directory for small Malta facilities and addresses; current listing showed 12 facilities across 8 markets during this pass. | C unless matched to primary |
| Datacenters.com | https://www.datacenters.com/locations/malta | Facility/provider directory; useful for provider universe. | C |
| Cloudscene | https://cloudscene.com/market/data-centers-in-malta/all | Useful for IXP/carrier/facility cross-checks; verify elsewhere. | C |
| Data Center Platform / Catalog / Colomap / Upstack | Various directory pages | Helpful for legacy addresses such as GO Marsa, BMIT Qormi/SmartCity, Epic St Venera. | C |

Trade-query examples:
```
site:datacenterdynamics.com/en/news/ "Malta" "data center"
site:datacenterdynamics.com/en/news/ "BMIT" "Malta"
site:datacenterdynamics.com/en/news/ "Enemalta" "Streamcast"
site:timesofmalta.com "data centre" "MITA"
site:timesofmalta.com "BMIT" "data centre" "Zejtun"
site:maltatoday.com.mt "data centre" "SmartCity"
site:maltatoday.com.mt "Streamcast" "Enemalta" "data centre"
site:tvmnews.mt "data centre" "BMIT"
site:independent.com.mt "Streamcast" "data centre" "Malta"
```

---

## 3. Directory-to-primary verification workflow

1. Start with DataCenterMap/Cloudscene/Datacenters.com only to seed facility names and addresses.
2. Search exact name + locality + operator official domain.
3. Search exact address in PA/eApplications/Gazette.
4. Search the operator in ERA MCP records for backup generators.
5. Search the legal entity in MBR and, for listed entities, Malta Stock Exchange announcements.
6. Record a directory-only site as Grade C and add a note naming what primary evidence is missing.

Directory query templates:
```
site:datacentermap.com/malta/ "Malta Data Centers"
site:datacentermap.com/malta/ "{locality}" "{operator}"
site:datacenters.com "Malta" "{operator}" "data centre"
site:cloudscene.com "Malta" "{operator}" "data center"
site:datacenterplatform.com "Malta" "{operator}"
site:colomap.com "Malta" "{operator}"
```

---

## 4. Locality search recipes

Use English first; then add Maltese spellings/diacritics and neighborhood/industrial-estate names.

Universal locality sweep:
```
"{division}" "Malta" "data centre"
"{division}" "Malta" "data center"
"{division}" "Malta" datacentre
"{division}" "Malta" "server farm"
"{division}" "Malta" colocation
"{division}" "Malta" "cloud hosting"
"{division}" "Malta" "backup generator" "data centre"
"{division}" "Malta" "substation" "data centre"
site:pa.org.mt "{division}" "data centre"
site:gov.mt "Planning Authority" "{division}" "data centre"
site:era.org.mt "{division}" "data centre"
```

High-yield variants:
```
"Santa Venera" OR "St Venera" "data centre"
"Birkirkara" OR "B'Kara" "data centre"
"Qormi" OR "Handaq" OR "Tal-Handaq" "data centre"
"Mriehel" OR "Mrieħel" "data centre"
"Kalkara" OR "SmartCity Malta" OR "Ricasoli" "data centre"
"Swieqi" OR "Madliena" "data centre"
"Zejtun" OR "Żejtun" OR "Bulebel" "data centre"
"Marsa" "underground" "data centre"
"Gzira" OR "Gżira" "SIS DC1" OR "MIDI DC1"
"Msida" "Malta Internet Exchange" OR "University of Malta" "data centre"
"Victoria" "Gozo Data Centre" OR "Rabat Gozo" "data centre"
```

Locality pitfalls to log:
- `amrun` in the manifest is Ħamrun/Hamrun; MITA head office is near Blata l-Bajda/Hamrun, but MITA's listed Data Centre is Santa Venera.
- `Melliea` in the manifest is Mellieħa/Mellieha.
- `Gajnsielem`, `Gargur`, `Gasri`, `Gaxaq`, and `Xagra` should also be searched as Ghajnsielem, Gharghur, Ghasri, Ghaxaq, Xaghra.
- `Saint John` is San Gwann/San Ġwann; cloud-hosting companies there should not be counted unless a physical datacentre is confirmed.
- `Saint Lucia's` is Santa Lucija; likely low yield.

---

## 5. Known facility/project seed list for validation

This is a methodology seed list, not a final census. Re-check every item during enumeration.

| Seed | Locality assignment | Status tendency | Best evidence path |
|---|---|---|---|
| MITA Data Centre | Santa Venera | Operational | MITA official page; PA/ERA if needed |
| MITA / Gozo Data Centre | Rabat Gozo / Victoria | Operational or public-sector internal lead | MITA procurement and government docs |
| BMIT Handaq | Qormi / Tal-Handaq | Operational | BMIT official + investor/stock-exchange docs + directory address |
| BMIT SmartCity | Kalkara | Operational | BMIT official + MaltaToday/PA SmartCity |
| BMIT Żejtun | Żejtun / Bulebel | Operational or post-2019 purpose-built facility | BMIT official announcement + PA/Gazette |
| Melita Primary Data Centre | Swieqi / Madliena | Operational | Melita official + ERA EP1255/22 |
| Melita Mriehel secondary site | Qormi or Birkirkara/CBD boundary | Operational lead | Melita official; directory locality needs primary confirmation |
| GO Birkirkara Data Centre | Birkirkara | Operational | GO official wholesale page |
| GO Marsa Data Centre | Marsa | Operational lead | GO official service + directory address; seek PA/ERA confirmation |
| Epic Malta data centre | Santa Venera lead | Operational lead | Epic official service; directory address needs primary confirmation |
| Continent 8 Malta facilities | Santa Venera and second undisclosed Malta site leads | Operational lead | Continent 8 official + directory cross-check |
| CSL Data Centre Services | Birkirkara/CBD | Operational | CSL official page/contact page |
| MIDI/SIS DC1 | Gzira | Operational lead | Directory-only unless operator/PA evidence found |
| University of Malta / MIX | Msida | IXP/data-centre lead | MIX/NIC official; avoid counting as commercial colo without confirmation |
| Heritage Malta data centre | Kalkara / Bighi | Operational internal/public-sector | Heritage Malta official 2025 news |
| Enemalta/Streamcast underground DC | Marsa | Abandoned/rejected unless revalidated | Enemalta official launch + MaltaToday/DCD later status |

---

## 6. Capacity extraction guidance

Malta capacity evidence is often non-MW:

- rack count: BMIT Żejtun announced more than 400 racks; BMIT Handaq directory claims about 300 racks; use primary documents where possible;
- floor area: BMIT official page gives 1,200 sqm usable floor across its Malta datacentres; CSL official page states 2,000 sqm rack-space capacity;
- generators: ERA MCP records give rated thermal-input bands and coordinates, useful for resilience/emissions but not IT load;
- power/rack: BMIT Handaq page gives customer power per rack; do not multiply by all racks unless the source explicitly supports that;
- investment value: BMIT Żejtun EUR 10m, BMIT SmartCity EUR 3.5m, Streamcast/Enemalta EUR 5m pilot / EUR 75m proposed are project-size signals, not MW.

Capacity query templates:
```
"{facility}" "rack" OR "racks"
"{facility}" "sqm" OR "m2" OR "square metres"
"{facility}" "MW" OR "MVA" OR "kW per rack"
"{facility}" "generator" OR "UPS" OR "2N"
"{facility}" "Tier III" OR "ISO 27001" OR "PCI DSS"
"{facility}" "investment" "€"
```

When capacity is not public, set `capacity_mw: null` and record the disclosed proxy in notes rather than deriving a false MW figure.
