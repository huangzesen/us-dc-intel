# CZ Explorer Official — Czechia Datacenter Enumeration from Permits, EIA, Grid, Telecom, and Public Records

Date: 2026-08-12. Scope: Czechia (CZ), all 14 manifest divisions: Prague; Central Bohemia; South Bohemia; Plzen; Karlovy Vary; Usti nad Labem; Liberec; Hradec Kralove; Pardubice; Vysocina; South Moravia; Olomouc; Zlin; Moravia-Silesia. This file is the official-source methodology. Use `explorer-industry.md` for operator, cloud, association, and trade-press pivots.

Reliability grades used here:

- **A**: primary public authority or official operator/cloud record: municipal/regional notice board, building-office decision, CENIA EIA/SEA record, IPPC record, CUZK cadastre, ARES/justice.cz entity record, ČEPS/ERÚ/DSO document, ČTÚ/NEN record, official operator page.
- **B**: strong secondary lead: established Czech or international trade press, operator blog without permit evidence, investment-agency/news release that does not itself contain the permit or facility record.
- **C**: weak lead only: directories, maps, marketplace listings, social posts, SEO pages, unsourced capacity claims.

Do not upgrade evidence because multiple C-grade directories repeat the same entry. A facility becomes countable only when an A-grade source confirms the site, or when a B-grade operator/press lead is paired with official permit/EIA/grid/cadastre evidence.

---

## 1. Verified Official Source Backbone

These URLs were checked during review. A `403` or timeout from command-line curl is noted where the site is still a real official source but resists automated crawling.

| Source | URL | Grade | Use | Notes |
|---|---|---:|---|---|
| CENIA EIA projects in Czechia | `https://portal.cenia.cz/eiasea/view/eia100_cr` | A | Search project names, investor IČO, municipality, EIA status, generator/cooling/power descriptions | Quick search covers code, name, classification, status, and competent authority. |
| CENIA EIA/SEA info page | `https://cenia.gov.cz/odborna-podpora/eiasea/informacni-systemy-eia-a-sea/` | A | Process source and portal pivot | Confirms EIA/SEA systems publish EIA documents. |
| ERÚ transmission-development plan page | `https://eru.gov.cz/plan-rozvoje-ps-cr-2025-2034` | A | Ten-year transmission planning, large-load context, consultation documents | Grid signal only; not a building permit. |
| ERÚ connection decree page | `https://eru.gov.cz/vyhlaska-o-podminkach-pripojeni-k-elektrizacni-soustave` | A | Connection rules and terms under vyhláška č. 16/2016 Sb. | Regulatory context, not facility evidence. |
| ČEPS | `https://www.ceps.cz` | A | Transmission development plans, adequacy reports, connection/load clues | Large-load evidence; not proof of construction. |
| ČEZ Distribuce | `https://www.cezdistribuce.cz` | A | DSO for most north/west/central/east Czech divisions | Search site plus municipality/operator. |
| EG.D | `https://www.egd.cz` | A | DSO for South Bohemia, South Moravia, Vysočina areas | Real official DSO; curl returned `403`, so use browser/manual search. |
| PREdistribuce | `https://www.predistribuce.cz` | A | Prague DSO | Key for Prague DC load/110 kV pivots. |
| ČTÚ | `https://www.ctu.cz` | A | Telecom operator registration, decisions, fiber/context | Not a datacenter registry. |
| NEN public procurement | `https://nen.nipez.cz` | A | State/university/server-room/DC procurements | Real official procurement route; curl timeout observed. |
| CUZK cadastre viewer | `https://nahlizenidokn.cuzk.cz` | A | Parcel, building, ownership, easement pivots | Use after an address/parcel is known. |
| ARES | `https://ares.gov.cz` | A | Legal name, IČO, address | Use for exact entity searches. |
| Justice.cz | `https://justice.cz` | A | Commercial register filings | Use for operator legal entities and filings. |
| UUR planning portal | `https://portal.uur.cz` | A | Planning-law and planning-system gateway | Process and planning links, not a permit database. |
| Builder's Portal / DIA | `https://portal.stavebnisprava.gov.cz` and `https://dia.gov.cz` | A | Official e-channel for building proceedings under the new Building Act | Do not assume it is a complete public search registry. |
| IPPC system | `https://ippc.mzp.cz/` | A | Integrated-permit leads for fuel storage, backup generation, emissions/noise | Search together with kraj and operator terms. |

Important structural fact: Czechia does **not** have a single public national building-permit registry comparable to some other European jurisdictions. Building-office evidence normally appears on municipal or city-district `úřední deska` pages, with regional authorities used for EIA, planning, appeals, and selected notices.

---

## 2. Core Czech Search Vocabulary

Search Czech first, with and without diacritics. Many older PDFs are OCR-poor or indexed without accents.

```text
datové centrum / datove centrum
datacentrum / datacentra
data centrum / datová centra
serverovna / serverovny
kolokace / housing / serverhousing
cloudové služby / privátní cloud
hyperscale / hyperskalní datové centrum
AI datové centrum / datové centrum pro umělou inteligenci
stavba datového centra / výstavba datacentra
úřední deska / verejna vyhlaska / veřejná vyhláška
stavební povolení / stavebni povoleni
územní rozhodnutí / rozhodnutí o umístění stavby
společné povolení / společné územní a stavební řízení
kolaudační souhlas / kolaudační rozhodnutí / zkušební provoz
EIA / posouzení vlivů na životní prostředí / oznámení záměru
integrované povolení / IPPC
připojení k distribuční soustavě / připojení k přenosové soustavě
sjednaný příkon / rezervovaný příkon / požadovaný příkon
rozvodna / trafostanice / transformátor / 110 kV / 400 kV
náhradní zdroj / dieselagregát / záložní zdroj / UPS
chlazení / chladicí jednotky / free cooling / akumulace chladu
průmyslová zóna / technologický park / brownfield
```

Facility documents often avoid `datové centrum`; they may describe a generic `technologická budova`, `administrativní objekt`, `serverovna`, `trafostanice`, `strojovna chlazení`, or `náhradní zdroj`.

---

## 3. Official Query Templates

Substitute `{division}`, `{kraj}`, `{okres}`, `{municipality}`, `{městská část}`, `{operator}`, `{legal_entity}`, `{IČO}`, `{address}`, `{parcel}`, and `{substation}`.

### 3.1 Building Office / Notice Board

```text
"{municipality}" "datové centrum" "stavební povolení"
"{municipality}" "datacentrum" "územní rozhodnutí"
"{municipality}" "serverovna" "kolaudační souhlas"
"{operator}" "{municipality}" "úřední deska"
"{legal_entity}" "stavební povolení"
"{legal_entity}" "kolaudační souhlas"
site:{municipality-domain} "datové centrum" "veřejná vyhláška"
site:{municipality-domain} "datacentrum" "stavební povolení"
site:{municipality-domain} "serverovna" "kolaudační"
site:{municipality-domain} "náhradní zdroj" "dieselagregát"
filetype:pdf "datové centrum" "stavební povolení" "{municipality}"
filetype:pdf "datacentrum" "oznámení o zahájení" "{municipality}"
filetype:pdf "{address}" "stavební povolení"
```

For Prague, search both the city and the relevant city district: `Praha 10`, `Praha 15`, `Praha 4`, `Praha 9`, etc. For Brno, search the magistrate and relevant city parts where notices are split.

### 3.2 EIA / IPPC

```text
site:portal.cenia.cz/eiasea "datové centrum"
site:portal.cenia.cz/eiasea "datacentrum"
site:portal.cenia.cz/eiasea "serverovna"
site:portal.cenia.cz/eiasea "{operator}"
site:portal.cenia.cz/eiasea "{municipality}" "datové centrum"
"{municipality}" "datacentrum" "EIA"
"{operator}" "integrované povolení"
site:ippc.cz "{operator}" OR "{municipality}" "náhradní zdroj"
site:mzp.cz "datové centrum" "integrované povolení"
site:{kraj-domain} "datové centrum" "EIA"
```

Extract: investor, IČO, parcels, building description, IT load or transformer size, backup generator capacity, fuel storage, cooling system, water consumption, phase schedule, competent authority, and decision/status date.

### 3.3 Energy / Grid

```text
site:ceps.cz "datové centrum"
site:ceps.cz "připojení" "přenosová soustava"
site:eru.gov.cz "Plán rozvoje PS" "datové centrum"
site:eru.gov.cz "datová centra" "příkon"
site:cezdistribuce.cz "datové centrum" "připojení"
site:egd.cz "datové centrum" "připojení"
site:predistribuce.cz "datové centrum" "připojení"
"{municipality}" "datové centrum" "rozvodna"
"{municipality}" "datové centrum" "trafostanice"
"{operator}" "sjednaný příkon" OR "rezervovaný příkon"
"{substation}" "datové centrum" "MW" OR "MVA"
```

Keep grid facts separate from facility status: `requested_connection_MW_or_MVA`, `connection_point`, `connection_status`, `permit_status`, `construction_status`, and `operational_status`. A grid request is not a datacenter.

### 3.4 Telecom / Public Procurement / Entity

```text
site:ctu.cz "{operator}" "datové centrum"
site:ctu.cz "optická síť" "{municipality}"
site:nen.nipez.cz "datové centrum"
site:nen.nipez.cz "serverovna"
site:nen.nipez.cz "kolokace"
site:nen.nipez.cz "vládní cloud"
site:ares.gov.cz "{legal_entity}" "{IČO}"
site:justice.cz "{legal_entity}" "datové centrum"
```

Public procurement is especially useful for government, university, hospital, and HPC/server-room projects that never appear in industry directories.

---

## 4. Counting and Status Rules

Use these classifications consistently:

- **Operational**: official operator facility page, public institution page, `kolaudační souhlas`, or current service page tied to a Czech address.
- **Under construction**: building permit or official construction-start notice plus project identity.
- **Planned**: official announcement plus EIA, planning, or grid/land evidence.
- **Lead**: press, association, directory, procurement-intent, zoning, grid application, or investment-agency mention without enough official project evidence.
- **Do not count**: CDN/edge PoPs, cloud sales offices, network PoPs, peering-only presence, general `market presence`, speculative grid demand, or any AWS/Azure/GCP/OCI Czech region claim not present in the provider's official region list.

Recommended facility fields:

```text
country_code, division, kraj_name, okres, municipality, city_district,
facility_name, operator, operator_legal_entity, IČO,
address, parcel_ids, facility_type,
status, status_date, evidence_grade,
permit_case_id, eia_code, ippc_case_id,
requested_connection_MW_or_MVA, transformer_or_generator_capacity,
connection_point_or_DSO, cooling_notes, source_urls, notes
```

---

## 5. Per-Division Official Strategy

All 14 divisions are covered below. Region rows are routing guides, not facility counts.

| Manifest division | Czech region | Regional official URL | Relevant DSO | Priority municipalities / districts | Official-first strategy | Known official or semi-official pivots |
|---|---|---|---|---|---|---|
| Prague | Hlavní město Praha | `https://www.praha.eu` | PREdistribuce | Praha 4, 9, 10, 13, 15, Vysočany, Malešice, Hostivař, Chodov, Stodůlky, Českomoravská | Search Prague magistrate plus city-district notice boards; then PREdistribuce and CENIA/IPPC for generators/cooling. | T-Mobile DC7, TTC TELEPORT, SafeDX, CE Colo, OVHcloud Prague, VSHosting, O2/CETIN seeds. |
| Central Bohemia | Středočeský kraj | `https://stredoceskykraj.cz/web/urad` | ČEZ Distribuce | Mladá Boleslav, Kladno, Kolín, Říčany, Nymburk, D1/D11 logistics corridors | Start with known enterprise/industrial names, then municipal notice boards and CUZK parcels. | Škoda Auto Mladá Boleslav corporate DC lead; watch Prague-periphery industrial parks. |
| South Bohemia | Jihočeský kraj | `https://www.kraj-jihocesky.cz` | EG.D | České Budějovice, Tábor, Písek | Sweep CENIA, regional notice board, EG.D, city notice boards; expect public-sector/server-room evidence more than colo. | Low-density division; count only official institutional/operator records. |
| Plzen | Plzeňský kraj | `https://www.plzensky-kraj.cz` | ČEZ Distribuce | Plzeň, Nýřany, Rokycany, D5 industrial areas | Search Plzeň electronic notice board and regional EIA/planning; use ČEZ Distribuce for 110 kV clues. | Regional colo/enterprise leads; no confirmed hyperscale campus. |
| Karlovy Vary | Karlovarský kraj | `https://www.kr-karlovarsky.cz` | ČEZ Distribuce | Karlovy Vary, Sokolov, Cheb | Low-density sweep: CENIA, kraj/municipal notice boards, public procurement, industrial-zone terms. | Treat all discovered items as leads until A-grade permit/operator evidence. |
| Usti nad Labem | Ústecký kraj | `https://www.kr-ustecky.cz` | ČEZ Distribuce | Ústí nad Labem, Chomutov, Most, Kadaň, Žatec industrial zones | High-priority sweep for large-load and brownfield projects: CENIA, ČEZ Distribuce, municipal boards, CzechInvest/news leads. | Chomutov datacenter/data-hub is a B-grade lead until permit/EIA/operator evidence confirms status. |
| Liberec | Liberecký kraj | `https://kraj-lbc.cz` | ČEZ Distribuce | Liberec, Jablonec nad Nisou, Turnov | Search regional/municipal notice boards with `serverovna`, `technologická budova`, and enterprise names; then CUZK. | Low-mid density; likely enterprise/server-room facilities. |
| Hradec Kralove | Královéhradecký kraj | `https://www.khk.cz` | ČEZ Distribuce | Hradec Králové, Trutnov, Náchod | Search public-sector procurement, municipal notice boards, CENIA/IPPC for backup generators. | Low-density; beware hospital/university server rooms counted as separate asset class. |
| Pardubice | Pardubický kraj | `https://www.pardubickykraj.cz` | ČEZ Distribuce | Pardubice, Chrudim, industrial/electronics parks | Sweep municipal boards, CENIA, NEN; search industrial park operators and `trafostanice`. | Low-mid density enterprise leads. |
| Vysocina | Kraj Vysočina | `https://www.kr-vysocina.cz/` | EG.D / ČEZ Distribuce edges | Jihlava, Třebíč, Žďár nad Sázavou, Dukovany energy area | Search kraj notice board (`/uredni-deska/1`), CENIA, EG.D, NEN; use energy terms carefully. | No countable hyperscale lead from official sources; energy context alone is not a site. |
| South Moravia | Jihomoravský kraj | `https://www.jmk.cz` | EG.D | Brno, Brno-Černovice, Brno-střed, Kanice u Brna, Modřice | Search Brno magistrate/city parts, Kanice municipal board, JMK EIA, EG.D; pair operator blogs with permits. | MasterDC Brno/Kanice lead, O2 Brno, Coolhousing private Brno, CESNET/CERIT research infrastructure. |
| Olomouc | Olomoucký kraj | `https://www.olkraj.cz` | ČEZ Distribuce | Olomouc, Prostějov, Přerov | Sweep CENIA, municipal boards, NEN and enterprise terms; expect small/server-room records. | Low-mid density. |
| Zlin | Zlínský kraj | `https://zlinskykraj.cz` | EG.D / ČEZ Distribuce edges | Zlín, Uherské Hradiště, Otrokovice | Search SYNOT/Monaco legal entities, municipal boards, CENIA/IPPC, CUZK parcels. | Datové centrum Monaco/SYNOT is an industry seed; require official/operator page or permit for A-grade. |
| Moravia-Silesia | Moravskoslezský kraj | `https://www.msk.cz` | ČEZ Distribuce | Ostrava, Ostrava-Poruba, Ostrava-Vítkovice, Karviná, Frýdek-Místek | Strong official/HPC route: IT4Innovations, EuroHPC, VŠB-TUO, CENIA, MSK notice board; distinguish public HPC from commercial colo. | IT4Innovations/VLQ/Czech AI Factory are A-grade public/HPC facility pivots. |

---

## 6. Official Cloud / Operator Pivots for Permit Searches

Use these only as seeds; final facility status still depends on the counting rules.

| Operator / provider | Official URL | Grade | CZ signal | Official-method action |
|---|---|---:|---|---|
| AWS global infrastructure | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` and `https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/` | A | No Czech Region or Local Zone found in official pages reviewed; third-party mentions of Prague edge/local-zone-like nodes are not facility evidence. | Do not count cloud region/local zone unless AWS page says so. |
| Microsoft Azure regions | `https://learn.microsoft.com/en-us/azure/reliability/regions-list` | A | No Czech public-cloud region in official region list reviewed. | Do not count a Czech Azure region. |
| Google Cloud locations | `https://cloud.google.com/about/locations` and `https://datacenters.google/locations` | A | No Czech Google Cloud region or Google-owned datacenter location in official pages reviewed. | Treat Chomutov/Google rumors as unconfirmed leads. |
| Oracle OCI regions | `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm` and `https://www.oracle.com/cloud/public-cloud-regions/` | A | No official Prague/Czech OCI public region confirmed in reviewed pages. | Re-check `eu-prague-1` claims against Oracle docs before counting. |
| OVHcloud Prague | `https://www.ovhcloud.com/en/datacenter/europe/czech-republic/prague/` | A | Official Prague datacentre page exists. | Search Prague permits/address/legal entity and PREdistribuce. |
| T-Mobile Czech Republic | `https://www.t-mobile.cz` | A | Official operator seed; DC7 details require official PDF/page or press pairing. | Search `DC7`, `K Pérovně`, `Praha 10/15`, T-Mobile legal entity. |
| O2 Czech Republic | `https://www.o2.cz/firmy-a-organizace/it-reseni/datove-centrum` | A | Official datacenter services page. | Resolve current O2 DC locations, then search Prague/Brno permits. |
| CETIN collocation | `https://www.cetin.cz/products-and-services/collocation` | A | Official nationwide collocation service in CETIN buildings. | Treat as network collocation; count only site-specific facilities. |
| IT4Innovations VLQ | `https://www.it4i.cz/en/infrastructure/vlq-quantum-computer` | A | Official Ostrava quantum/HPC infrastructure; installation/commissioning in 2025. | Count as public/HPC asset, not commercial colo. |

---

## 7. Known Trapdoors and Quality Controls

- **Equinix Prague**: third-party directories list Prague facilities, but reviewed searches did not surface an official Equinix Prague location page. Keep as C-grade/B-grade lead until Equinix official confirmation or local permit/address evidence exists.
- **OVHcloud Prague**: official page exists; still resolve whether it is a full datacentre, Local Zone, or specific product location before comparing with hyperscale cloud regions.
- **Chomutov**: keep as B-grade lead unless EIA/permit/operator documents confirm the actual project, site, and status.
- **Kanice u Brna MasterDC**: official MasterDC blog is a B-grade project announcement until municipal/JMK/EG.D/permit evidence confirms construction or operation.
- **HPC/public facilities**: IT4Innovations, CESNET, CERIT, government-cloud and hospital server rooms are valid infrastructure records, but mark `facility_type=HPC/public/research/government` and do not mix with commercial colo counts.
- **Capacity claims**: separate IT load, gross electrical capacity, requested grid capacity, generator capacity, and rack count. Never convert between them without source support.
- **Date discipline**: every status must carry the source date or retrieval date. A 2025 target opening is not operational in 2026 unless a launch/current-service source confirms it.

---

## 8. Minimal Official Workflow

1. Pull ARES/justice.cz legal entity names and IČO for each operator/lead.
2. Search CENIA EIA by `datové centrum`, `datacentrum`, `serverovna`, operator, municipality, and IČO.
3. Search region and municipality notice boards for permit lifecycle terms and address/parcel pivots.
4. Use CUZK to normalize address, parcel, ownership, and easements.
5. Check ČEPS/ERÚ and the relevant DSO for connection/load context.
6. Search ČTÚ and NEN for telecom/public-sector records.
7. Assign status and grade using §4; keep unsupported leads in a separate lead queue.
