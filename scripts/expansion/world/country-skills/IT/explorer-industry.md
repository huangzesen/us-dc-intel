# IT Explorer Industry - colocation providers, cloud regions, trade press, and regional query patterns

Date: 2026-08-12. Scope: Italy datacenter enumeration methodology focused on industry/vendor sources, cloud regions, trade press, associations, and region-level search patterns. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/market source, **C** = directory, aggregator, local promo, weak secondary, or unverified lead.

---

## 0. Italy-specific frame

- Italy has no complete public national datacenter registry. Build the facility census by triangulating **operator pages**, **cloud-region pages**, **Italian Datacenter Association / market sources**, **DCD and Italian trade press**, **regional/municipal permitting**, and **grid/environmental authorization notices**.
- The practical enumeration center of gravity is **Lombardy / Greater Milan**: Milan, Settala, Peschiera Borromeo/San Bovio, Melegnano, Siziano, Vellezzo Bellini, Cornaredo, Vittuone, Pavia/Bornasco/Certosa di Pavia, Bergamo/Ponte San Pietro, and the wider Milan west/south logistics-power corridor. Treat Lombardy as its own deep workflow.
- Second-order clusters: **Lazio/Rome** (Aruba Rome, PSN/government cloud, enterprise/edge sites), **Piedmont/Turin** (Oracle Turin, TIM/Noovle, AI/sovereign-cloud narrative), **Tuscany/Arezzo-Pisa-Florence** (Aruba Arezzo and regional colo), **Sicily/Palermo** (Open Hub Med/subsea), and regional edge nodes around Bologna, Padua/Verona, Naples/Bari/Cagliari/Genoa.
- Italian official filings use mixed vocabulary. Search both English and Italian: `data center`, `datacenter`, `centro dati`, `centri dati`, `CED`, `centro elaborazione dati`, `cloud region`, `polo strategico nazionale`, `infrastruttura digitale`, `impianto di calcolo`, `colocation`, `hyperscale`.
- 2026 permitting context matters. Italy introduced a simplified/single authorization framework for datacenter development, while Lombardy created a regional datacenter guidance/law surface and a `Sportello regionale per i centri dati`. For large projects, search national **MIMIT** strategic-interest notices plus regional **VIA/AIA/AUA** and municipal planning records.

---

## 1. Source grades and URLs

### 1.1 Association, events, and market context

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Italian Datacenter Association (IDA) | https://italiandatacenter.com/ and English page https://italiandatacenter.com/en/ | Best sector association seed. Founded by Microsoft, Equinix Italy, Rai Way, DATA4, STACK Infrastructure, Digital Realty, Vantage Data Centers, and CBRE Data Centers; use member/news pages to identify current ecosystem actors. Not a facility registry. | B |
| IDA press page | https://italiandatacenter.com/press/ | Italian-language media roundup and association policy reactions; good for tracking regulation and investment narratives. | B |
| German Datacenter Association partner profile for IDA | https://www.germandatacenters.com/en/partner/ida-italian-datacenter-association/ | Independent association profile confirming founding members and creation date. | B |
| Data Center Nation Milan | https://datacenternation.com/dcn-milan/ and agenda pages | Current Italian operator/investor/supplier attendee list; useful for names to pivot into project searches. | B/C |
| Osservatori Digital Innovation / Politecnico di Milano | https://www.osservatori.net/ ; query `site:osservatori.net data center Italia` | Market/investment sizing and cluster commentary. Good context, not facility-level truth. | B |
| A2A / Ambrosetti datacenter report material | Example A2A release: https://www.gruppoa2a.it/it/media/comunicati-stampa/italia-data-center-ambrosetti | Useful national count/power distribution context; A2A is also a potential Lombardy operator/energy counterparty. | B |

### 1.2 Trade press and directories

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics Italy tag | https://www.datacenterdynamics.com/en/tags/italy/ and filtered news such as https://www.datacenterdynamics.com/en/news/?tag=italy&term=colocation-wholesale | Best English-language deal/construction feed for Italy. Recent leads include Rai Way Rome approval, CyrusOne Milan groundbreaking, Digital Realty Milan land, Retelit financing/sale reports, Aruba acquisitions, Open Hub Med, Certosa di Pavia, Redelfi, and Khazna/Eni. | B |
| Data Center Magazine / DCNN / Capacity / Telecoms.com / Telecompaper | Query by operator + Italy/Milan/Rome | Good for vendor PR syndication and cloud-region launches. Verify capacity/status elsewhere. | B-/C+ |
| Agenda Digitale | https://www.agendadigitale.eu/ ; query `site:agendadigitale.eu data center Italia normativa` | Strong Italian policy/regulatory commentary. Use for law/policy pointers, then verify in official gazettes/regional pages. | B |
| Italian local press | `la Provincia Pavese`, `Il Giorno`, `MilanoToday`, `RomaToday`, `Corriere Milano`, `La Repubblica`, `TorinoToday`, regional newspapers | Often first to expose municipal plans, protests, council votes, land purchases, and construction starts. Useful leads; verify against municipal albo/pretorio or regional VIA/AIA. | C+/B- |
| DataCenterMap | https://www.datacentermap.com/italy/ and city pages such as https://www.datacentermap.com/italy/milan/ | Fast facility/address/operator seed. Current Milan pages surface many active and pipeline aliases; never final source alone. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/italy | Commercial facility directory; good for provider/facility names and rough addresses. Verify via operator or permit. | C+ |
| Baxtel | https://baxtel.com/data-centers/italy | Strong for hyperscale campus leads and neighboring-facility graph; useful for Microsoft/Vantage/CyrusOne/CloudHQ-style projects. | C+ |
| Datacenterplatform / DC Atlas | https://datacenterplatform.com/data-centers/ , https://dcatlas.io/ | Helpful for operator address lists and MW hints; verify. | C |

### 1.3 Official/public records to pair with industry leads

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| MIMIT data-center strategic-interest notices | https://www.mimit.gov.it/ ; query `site:mimit.gov.it "Data Center" "interesse strategico nazionale"` | A-grade national lead for major foreign/strategic investments. Example: 2026 notices for large programs in Lombardy/Piedmont and other strategic-interest declarations under the Decreto Asset framework. | A |
| Regional VIA/VAS/AIA portals | Each region has an environment-assessment page; query `site:regione.{region}.it "data center" VIA AIA` | Best public path for generator plants, grid works, environmental screening, water/cooling, and project documents. | A |
| Municipal planning and building portals | Comune `Sportello Unico Edilizia (SUE)`, `Sportello Unico Attivita Produttive (SUAP)`, `Albo Pretorio`, `Delibere`, `Urbanistica`, `Permesso di costruire` | Project-level evidence: planning variant, building permit, council resolution, convention, public consultation. | A-/B |
| Business registry / company identity | Registro Imprese / Telemaco, company official pages, investor releases | Use to resolve SPVs and operator parentage. Many projects use property SPVs or real-estate developers before operator handoff. | A/B |
| Terna and local DSO grid filings/news | https://www.terna.it/ ; local utilities A2A, Unareti, E-Distribuzione, Iren, Hera, Acea | Grid connection, substations, HV/MV works, and waste-heat tie-ins often reveal scale before press. | A/B |
| Lombardy dedicated datacenter regulation page | https://www.regione.lombardia.it/ambiente-e-territorio/red-procedimenti-autorizzatori-progetti-data-center | Core Lombardy source. Regione Lombardia issued 2024 guidelines for datacenter physical infrastructure authorization and assessment; later regional law establishes a datacenter counter/authorization surface. | A |

---

## 2. Italian and English query templates

### 2.1 Facility/project discovery

```text
"{comune}" ("data center" OR datacenter OR "centro dati" OR "centri dati" OR "centro elaborazione dati" OR CED) ("permesso di costruire" OR "variante urbanistica" OR "conferenza dei servizi" OR VIA OR AIA OR AUA OR "autorizzazione unica")
"{provincia}" ("data center" OR "centro dati") (MW OR MVA OR "cabina primaria" OR "stazione elettrica" OR "gruppi elettrogeni")
site:{comune_domain} ("data center" OR "centro dati" OR datacenter) ("delibera" OR "permesso di costruire" OR "albo pretorio" OR "urbanistica")
site:{regional_domain} ("data center" OR "centro dati" OR datacenter) (VIA OR AIA OR AUA OR "verifica di assoggettabilita" OR "valutazione impatto ambientale")
site:mimit.gov.it "data center" ("interesse strategico nazionale" OR "preminente interesse strategico")
```

### 2.2 Vendor/trade triangulation

```text
site:datacenterdynamics.com/en/ Italy "data center" {operator OR comune OR provincia}
site:italiandatacenter.com {operator OR comune OR "data center"}
"{operator}" Italy ("data center" OR datacenter OR colocation OR cloud) (Milan OR Milano OR Rome OR Roma OR Turin OR Torino)
"{operator}" "{comune}" (MW OR MVA OR sqm OR "metri quadrati" OR "IT load" OR "critical IT load")
"{operator}" "{comune}" ("inizio lavori" OR "inaugura" OR "apre" OR "acquisisce" OR "approvato" OR "autorizzato")
```

### 2.3 Italian permitting vocabulary

Use these variants because municipal and environmental files rarely use one standard label:

```text
"centro dati"
"centri dati"
"centro elaborazione dati"
"CED"
"data center"
datacenter
"infrastruttura digitale"
"polo cloud"
"cloud region"
"polo strategico nazionale"
"permesso di costruire"
"permesso di costruire convenzionato"
"piano attuativo"
"variante urbanistica"
"sportello unico edilizia"
"sportello unico attivita produttive"
"conferenza dei servizi"
"verifica di assoggettabilita a VIA"
"valutazione di impatto ambientale"
"autorizzazione integrata ambientale"
"autorizzazione unica ambientale"
"gruppi elettrogeni"
"cabina primaria"
"stazione elettrica"
"teleriscaldamento"
"recupero calore"
```

### 2.4 Lifecycle/status words

- **Intent/land only**: `accordo`, `protocollo`, `memorandum`, `opzione su terreno`, `manifestazione di interesse`, `proposta`, `studio di fattibilita`, `pipeline`, `programma di investimento`.
- **Permit evidence**: `permesso di costruire`, `istanza`, `conferenza dei servizi`, `autorizzazione unica`, `VIA`, `AIA`, `AUA`, `provvedimento autorizzatorio`, `delibera`, `determinazione`, `albo pretorio`.
- **Construction**: `inizio lavori`, `cantierizzazione`, `bonifica`, `demolizione`, `posa della prima pietra`, `cantiere`, `realizzazione`.
- **Operational**: `inaugurato`, `attivo`, `aperto`, `messo in esercizio`, `operativo`, operator official facility page, cloud-region live docs, PeeringDB active facility.

---

## 3. Operator and vendor seed list

Operator official pages are **A- for current existence/location** and **B for capacity** unless capacity is in formal filings or detailed technical specs.

| Operator | Official / strong source | Italy search pivots and notes |
|---|---|---|
| Aruba / Aruba Cloud | https://www.datacenter.it/en/ ; https://www.arubacloud.com/why-choose-aruba/datacenter | Italian incumbent. Official pages list Ponte San Pietro/Bergamo and Rome; Aruba Cloud also lists IT1/IT2 Arezzo, IT3 Bergamo, IT4 Rome. Search Arezzo, Ponte San Pietro, Bergamo, Tecnopolo Tiburtino/Rome, and acquisitions. |
| Retelit / Irideos | https://www.retelit.it/en/housing | Milan/Corsico/Avalon and national colo/network sites; DCD has financing/sale/waste-heat leads. Search `Retelit Avalon`, `Irideos`, `Corsico`, `Milano Viviani`, `A2A Calore`. |
| Equinix Italy | https://www.equinix.com/data-centers/europe-colocation/italy-colocation | Milan ML sites, xScale/AI-ready positioning. Search `Equinix ML`, `Settimo Milanese`, `Italy colocation`. |
| DATA4 | https://www.data4group.com/en/data-center-in-milan-italy/ | Milan-Cornaredo MIL01 and Vittuone/MIL2 expansion. Search Cornaredo, Vittuone, Settimo Milanese, Monzoro, `Data4 MIL2`. |
| STACK Infrastructure | https://www.stackinfra.com/locations/emea/milan/ | Siziano/Milan campus, former Supernap Italia, expansions around Pavia/Milan south. Search Siziano, Vellezzo Bellini, Milan MIL01/MIL02/MIL04. |
| Noovle / TIM Enterprise | https://www.noovle.com/en/datacenter/ ; TIM Noovle launch release https://www.gruppotim.it/en/press-archive/corporate/2021/PR-Noovle-DEF-EN.html | TIM datacenter estate, Google partnership, PSN/government cloud, Turin OCI host partner. Search Santo Stefano Ticino, Pomezia, Turin/Torino, PSN, TIM Enterprise. |
| Vantage Data Centers | https://vantage-dc.com/data-center-locations/emea/milan-italy/ and second Italy campus release https://vantage-dc.com/news/vantage-data-centers-expands-european-footprint-with-second-italian-campus/ | Milan I/Melegnano 64 MW official, Castelletto second campus 32 MW. Search Melegnano, Castelletto, MXP1, MXP2, Pavia/Milan south. |
| Digital Realty | https://www.digitalrealty.com/data-centers/emea | Historically via Milan/Interxion ecosystem; DCD reports land outside Milan for future development. Search `Digital Realty Milan`, `Interxion Milan`, `Caldera`, land/development filings. |
| Rai Way | https://www.raiway.it/ ; IDA founder article https://www.raiway.it/en/media/news/news-servizi-e-innovazione/rai-way-among-the-founders-of-ida-italian-data-center-association | Broadcast-infrastructure operator entering hyperscale/edge. DCD reported approval for a large Rome-area project. Search `Rai Way data center Roma`, `Santa Palomba`, `Pomezia`, `Milan`. |
| Microsoft | Azure official region list plus Microsoft Local project pages such as https://local.microsoft.com/blog/bornasco-datacenter-construction-update/ | Italy North/Milan cloud region and Lombardy campus pipeline. Search Settala, Peschiera Borromeo/San Bovio, Bornasco, `Microsoft Local Italy`. |
| AWS | https://aws.amazon.com/local/italy/milan/ ; launch blog https://aws.amazon.com/blogs/aws/now-open-aws-europe-milan-region/ | Europe (Milan) region. Search only for official region evidence and local permitting under AWS/Amazon Web Services/Amazon Data Services Italy. |
| Google Cloud / Google / Telecom Italia | Google locations https://cloud.google.com/about/locations and Compute regions docs https://docs.cloud.google.com/compute/docs/regions-zones | Milan `europe-west8` is live; Turin `europe-west12` has been announced/appears in region listings depending source freshness. TIM/Noovle partnership is key for mapping. |
| Oracle Cloud / TIM | OCI regions docs https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm ; Turin launch https://www.oracle.com/news/announcement/oracle-opens-second-public-cloud-region-in-italy-2025-11-19/ | OCI has Italy Northwest/Milan `eu-milan-1` and Italy North/Turin `eu-turin-1`; Turin is hosted with TIM Enterprise. |
| CyrusOne | https://www.cyrusone.com/ ; DCD Italy news | First Italian facility outside Milan broke ground in 2026 per DCD. Search Segrate/Via Reggio Emilia, MIL1/MIL2, Peschiera/Segrate permits. |
| CloudHQ | https://www.cloudhq.com/ ; DCD/Baxtel leads | Milan/MXP pipeline. Search MXP4/MXP5, Milan west/south municipalities, SPVs. |
| Khazna / Eni | Khazna official plus DCD leads | Announced AI campus concept around Ferrera Erbognone / Pavia area with Eni. Treat as B until official Italian permits/MIMIT notices are found. |
| EdgeConneX | EdgeConneX official plus MIMIT/DCD/market reports | 2026 strategic-interest investment leads in Lombardy; search `EdgeConneX Campus Italia`, `Lombardia`, MIMIT notices, municipal locations. |
| A2A / Redelfi / Magnora / Solaria | Company releases, DCD, Borsa Italiana filings | Energy developers entering datacenter development. Treat as pipeline leads until operator/permit evidence exists. |
| Open Hub Med | https://www.openhubmed.it/ and DCD acquisition news | Sicily/Palermo-area subsea/colo facility. Search Palermo, Carini, Sicily, Mediterra, Open Hub Med. |

Other names to pivot: NTT Global Data Centers, Colt DCS / NorthC / AtlasEdge legacy edge assets, Templus, Utility Line Italia, Seeweb, Keliweb, Ehiweb, IRIDEOS aliases, Fastweb, Vodafone, Wind Tre, INPS/Sogei public-sector DCs, university/HPC centers (CINECA Bologna/Casalecchio, INFN CNAF Bologna).

---

## 4. Hyperscaler/cloud official pages

Cloud pages prove a logical cloud region/metro; they do not prove exact street addresses. Use as seed signals and map to facilities only with official operator/project documents, local permitting, incidents, PeeringDB, or credible trade reporting.

| Provider | Italy region signal | URL | Grade |
|---|---|---|---|
| AWS | Europe (Milan), `eu-south-1`, opened 2020, three AZs; AWS local Milan page describes AWS Europe (Milan) Region. | https://aws.amazon.com/local/italy/milan/ , https://aws.amazon.com/blogs/aws/now-open-aws-europe-milan-region/ | A region / C facility |
| Microsoft Azure | Italy North, physical location Milan, `italynorth`, availability zones supported in Azure public-cloud region list. | https://learn.microsoft.com/en-us/azure/reliability/regions-list | A region / C facility |
| Google Cloud | Milan `europe-west8` in official location/Compute docs; check docs for Turin `europe-west12` status before counting as live. | https://cloud.google.com/about/locations , https://docs.cloud.google.com/compute/docs/regions-zones | A region / C facility |
| Oracle Cloud Infrastructure | Italy Northwest (Milan) `eu-milan-1`; Italy North (Turin) `eu-turin-1`; OCI docs list both, and Oracle announced Turin in 2025 with TIM Enterprise as host partner. | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm , https://www.oracle.com/news/announcement/oracle-opens-second-public-cloud-region-in-italy-2025-11-19/ | A region / B host-partner / C facility |
| Google/Oracle/Microsoft multicloud | Oracle Database@Azure / Oracle Database@Google Cloud may reference Italy North/Milan support. | Use provider docs only. | A service-region / C facility |
| PSN / sovereign public-sector cloud | Polo Strategico Nazionale, TIM/Leonardo/CDP/Sogei ecosystem, Oracle Alloy/OCI references in trade press | Use PSN and government procurement/press documents to map Italian public-sector cloud facilities; avoid assuming all PSN workloads equal new datacenters. | A/B |

Cloud pivot queries:

```text
"AWS" "Milan Region" "data center" Italy
"Azure" "Italy North" Milan datacenter Settala Bornasco
"Google Cloud" "europe-west8" Milan TIM Noovle data center
"Oracle" "eu-milan-1" "eu-turin-1" TIM Enterprise data center
"Polo Strategico Nazionale" "data center" TIM Leonardo Sogei
```

---

## 5. Region-level enumeration method

For each Italian region, run four passes:

1. **Vendor/trade pass (B/C -> A/B)**: use the regional operator seeds below plus DCD/IDA/DataCenterMap/Baxtel. Extract operator, project alias, municipality, power/MW, status verb, and cited source.
2. **Regional environment pass (A)**: query the region portal for `VIA`, `verifica di assoggettabilita`, `AIA`, `AUA`, `VAS`, `gruppi elettrogeni`, `stazione elettrica`, and project/operator names.
3. **Municipal pass (A-/B)**: query `comune.{city}.it`, `albo pretorio`, `delibere`, SUE/SUAP, `permesso di costruire`, `piano attuativo`, `variante urbanistica`, and `conferenza dei servizi`.
4. **Grid/heat pass (A/B)**: search Terna, DSO/utility pages, district-heating operators, and energy-company releases for grid connection, substations, `teleriscaldamento`, or `recupero calore`.

Generic regional template:

```text
site:regione.{region_domain} ("data center" OR datacenter OR "centro dati" OR CED) (VIA OR AIA OR AUA OR "autorizzazione unica" OR "verifica di assoggettabilita")
site:comune.{city_domain} ("data center" OR datacenter OR "centro dati") ("permesso di costruire" OR "variante urbanistica" OR "delibera" OR "albo pretorio")
"{region}" "{city}" ("data center" OR datacenter OR "centro dati") (MW OR MVA OR "gruppi elettrogeni" OR "cabina primaria")
```

### 5.1 Region seeds and query patterns

| Region | Priority cities/provinces and operator pivots | Copy-paste query seeds |
|---|---|---|
| Lombardia | Milan metro, Settala, Peschiera Borromeo/San Bovio, Melegnano, Siziano, Vellezzo Bellini, Cornaredo, Vittuone, Corsico, Pavia/Bornasco/Certosa, Bergamo/Ponte San Pietro. Operators: Microsoft, AWS/Azure ecosystem, Equinix, DATA4, STACK, Vantage, Digital Realty, Retelit, Aruba, CyrusOne, CloudHQ, EdgeConneX, A2A, Khazna/Eni, Rai Way Milan. | `site:regione.lombardia.it "data center" VIA AIA`; `site:regione.lombardia.it "centri dati"`; `site:comune.milano.it datacenter "permesso di costruire"`; `"Settala" "data center" Microsoft`; `"Bornasco" "data center" Microsoft`; `"Certosa di Pavia" "data center" 50MW`; `"Ponte San Pietro" Aruba "data center"` |
| Lazio | Rome/Tecnopolo Tiburtino, Pomezia, Santa Palomba, public-sector/PSN sites. Operators: Aruba, Rai Way, Noovle/TIM, PSN, Sogei, Oracle/sovereign cloud ecosystem. | `site:regione.lazio.it "data center" VIA AIA`; `site:comune.roma.it "data center" Aruba`; `"Tecnopolo Tiburtino" "data center"`; `"Rai Way" "data center" Roma`; `"Pomezia" "data center" Noovle OR Rai Way` |
| Piemonte | Turin/Torino, Novara, Alessandria logistics-power corridors. Operators: Oracle/TIM Enterprise, Noovle/TIM, possible MIMIT strategic-interest projects. | `site:regione.piemonte.it "data center" VIA AIA`; `"Oracle" "Torino" "cloud region"`; `"TIM Enterprise" Torino "data center"`; `site:mimit.gov.it "data center" Piemonte`; `"Novara" "data center" MW` |
| Toscana | Arezzo, Florence, Pisa, Prato. Operators: Aruba IT1/IT2 Arezzo, regional hosting, research/HPC. | `site:regione.toscana.it "data center" VIA AIA`; `"Arezzo" Aruba "data center"`; `"Toscana" "centro dati" "permesso di costruire"`; `"Pisa" "data center" CED` |
| Emilia-Romagna | Bologna/Casalecchio, Modena, Parma, Reggio Emilia, Piacenza, Rimini. Operators: CINECA/Leonardo HPC, INFN CNAF, regional colo/edge, possible logistics corridor sites. | `site:regione.emilia-romagna.it "data center" VIA AIA`; `"Bologna" "data center" CINECA`; `"Casalecchio" "data center"`; `"INFN CNAF" "data center"`; `"Piacenza" datacenter MW` |
| Veneto | Padua/Padova, Verona, Vicenza, Venice/Mestre, Treviso. Operators: regional edge/colo, telcos, enterprise DCs. | `site:regione.veneto.it "data center" VIA AIA`; `"Padova" "data center" colocation`; `"Verona" datacenter "permesso di costruire"`; `"Mestre" "centro dati"` |
| Liguria | Genoa/Genova, Savona, La Spezia; subsea/port and edge angle. | `site:regione.liguria.it "data center" VIA AIA`; `"Genova" "data center" porto`; `"Liguria" "centro dati" "gruppi elettrogeni"` |
| Trentino-Alto Adige/Suedtirol | Trento, Bolzano/Bozen, hydropower/green DC angle, public-sector and research sites. | `site:provincia.tn.it "data center"`; `site:provincia.bz.it "data center" OR "Rechenzentrum"`; `"Trento" "data center" cloud`; `"Bolzano" Rechenzentrum OR "centro dati"` |
| Friuli-Venezia Giulia | Trieste, Udine, Pordenone; port/subsea/research angle. | `site:regione.fvg.it "data center" VIA AIA`; `"Trieste" "data center" porto`; `"Udine" "centro dati"` |
| Marche | Ancona, Pesaro, Jesi; regional edge/public-sector. | `site:regione.marche.it "data center" VIA AIA`; `"Ancona" "centro dati"`; `"Pesaro" datacenter` |
| Umbria | Perugia, Terni; low-density regional edge/public-sector. | `site:regione.umbria.it "data center" VIA AIA`; `"Perugia" "centro dati"`; `"Terni" datacenter` |
| Abruzzo | L'Aquila, Pescara, Chieti; disaster-recovery/public-sector angle. | `site:regione.abruzzo.it "data center" VIA AIA`; `"L'Aquila" "data center"`; `"Pescara" "centro dati"` |
| Molise | Campobasso, Termoli; low density. | `site:regione.molise.it "data center"`; `"Campobasso" "centro dati"`; `"Termoli" datacenter` |
| Campania | Naples/Napoli, Caserta, Salerno, Nola/Marcianise logistics corridor. Operators: telco/edge, public-sector, potential AI/enterprise sites. | `site:regione.campania.it "data center" VIA AIA`; `"Napoli" "data center" colocation`; `"Caserta" datacenter MW`; `"Nola" "centro dati"` |
| Puglia | Bari, Lecce, Brindisi, Taranto; subsea/eastern-Med and public-sector edge angle. | `site:regione.puglia.it "data center" VIA AIA`; `"Bari" "data center" cloud`; `"Lecce" "centro dati"`; `"Brindisi" datacenter` |
| Basilicata | Potenza, Matera; low-density public-sector/edge. | `site:regione.basilicata.it "data center"`; `"Potenza" "centro dati"`; `"Matera" datacenter` |
| Calabria | Cosenza, Catanzaro, Lamezia Terme, Reggio Calabria; regional edge and subsea south angle. | `site:regione.calabria.it "data center" VIA`; `"Lamezia Terme" datacenter`; `"Reggio Calabria" "centro dati"` |
| Sicilia | Palermo/Carini, Catania, Messina; Open Hub Med and subsea/Med gateway angle. | `site:regione.sicilia.it "data center" VIA AIA`; `"Open Hub Med" Palermo "data center"`; `"Carini" "data center"`; `"Catania" datacenter`; `"Sicilia" "centro dati" "gruppi elettrogeni"` |
| Sardegna | Cagliari, Sassari, Olbia; AWS engineering presence is not a facility signal; search edge/public-sector and submarine cable landings. | `site:regione.sardegna.it "data center" VIA`; `"Cagliari" "data center" colocation`; `"Sassari" "centro dati"`; `"Olbia" datacenter` |
| Valle d'Aosta | Aosta; low-density, hydropower/edge/research. | `site:regione.vda.it "data center" OR "centro dati"`; `"Aosta" datacenter`; `"Valle d'Aosta" "centro elaborazione dati"` |

### 5.2 Province/municipality workflow for Lombardy

Because Lombardy concentrates most hyperscale growth, do not rely on a single regional search. Run municipality-specific searches for each suspected campus:

```text
"{comune}" "{operator}" "data center"
site:comune.{comune}.it "{operator}" OR "data center" OR "centro dati"
site:albo-pretorio.{comune_domain} "data center"
"{comune}" "permesso di costruire" "data center"
"{comune}" "conferenza dei servizi" "data center"
"{comune}" "gruppi elettrogeni" "data center"
"{comune}" "cabina primaria" "data center"
"{comune}" "teleriscaldamento" "data center"
```

Priority Lombardy municipalities to sweep repeatedly: Milan/Milano, Settala, Peschiera Borromeo, Segrate, Melegnano, Siziano, Vellezzo Bellini, Bornasco, Certosa di Pavia, Ferrera Erbognone, Corsico, Cornaredo, Vittuone, Settimo Milanese, Ponte San Pietro, Bergamo, Zibido San Giacomo, Lodi, Binasco, Lacchiarella, Landriano, Rozzano, Pero, Rho.

---

## 6. Verification rules

- **Do not count market report totals as facilities.** Reports can say Italy has dozens/hundreds of datacenters or GW pipeline, but facility records need operator, municipality/address, status, and evidence.
- **Separate cloud region from building.** AWS/Azure/GCP/OCI region pages are A-grade for logical region existence; exact facilities are usually hidden and must be inferred only from official local project pages, operator relationship, permits, or credible incident/trade evidence.
- **Resolve aliases.** Same site may appear under brand, SPV, landowner, campus name, and municipality: e.g., `Supernap Italia` -> `STACK`, `Irideos` -> `Retelit`, `Avalon`, `MXP1`, `MIL01`, `Santo Stefano Ticino`, `Tecnopolo Tiburtino`.
- **Treat MW carefully.** Italian trade articles may quote full buildout or backup-generator MW. Prefer `critical IT load`, `potenza IT`, `MVA grid connection`, and environmental files with generator counts. Label design/full-buildout separately from operational power.
- **Status discipline:** `strategic interest`, land secured, and investment announced are not construction. Count as planned unless a permit, construction update, or operator opening page exists. `inaugurato/aperto/operativo` plus operator page is operational evidence.
- **Grid and water are strong sanity checks.** Large AI/hyperscale campuses leave traces in substations, HV/MV connections, AIA/VIA files, water/cooling limits, and waste-heat/district-heating agreements.

Recommended discovery order:

1. Seed from IDA founders/members and major operators: Aruba, Retelit, Equinix, DATA4, STACK, Noovle/TIM, Vantage, Digital Realty, Rai Way, Microsoft, AWS, Google, Oracle, CyrusOne, CloudHQ, EdgeConneX, Khazna/Eni, A2A.
2. Sweep DCD Italy tag and IDA press for 2024-2026 projects and M&A.
3. Build a Lombardy municipality queue from Milan/Pavia/Bergamo project aliases; verify with Regione Lombardia datacenter/VIA pages and municipal SUE/SUAP/albo.
4. Add cloud regions: AWS Milan, Azure Italy North, Google Milan/Turin status, OCI Milan/Turin, PSN/Noovle/TIM.
5. Sweep non-Lombardy regional anchors: Rome/Lazio, Turin/Piedmont, Arezzo/Tuscany, Bologna/Emilia-Romagna, Palermo/Sicily, then all remaining regions using the region table.
6. Assign evidence grade per data point and keep pipeline/permit/operational status separate.
