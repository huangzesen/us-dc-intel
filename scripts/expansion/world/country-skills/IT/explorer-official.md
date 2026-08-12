# IT Explorer Official - Italy Datacenter Enumeration via Permits, Energy/Grid, Cloud Regions, Colo, and Regulators

Date: 2026-08-12. Scope: Italy (IT), with region/province/municipality routing. Focus angle: official/regulatory/cloud pipeline for enumerating datacenter facilities, expansions, and project pipeline. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak aggregate/unverified source.

---

## 0. Structural facts that shape Italy enumeration

- Italy now has a national datacenter authorization signal. **Decreto-legge 20 febbraio 2026, n. 21**, converted by **Legge 10 aprile 2026, n. 49**, introduced a **procedimento unico** for authorization of construction, expansion, operation, and grid-connection works for `centri dati / data center`. Official law source: https://www.gazzettaufficiale.it/eli/id/2026/02/20/26G00041/SG. Grade A.
- MASE published operational materials for the new data-center authorization route in July 2026, including application forms, the list of required authorizations/assents, public notice model, and digital submission specs. Source: https://va.mite.gov.it/it-IT/Comunicazione/DettaglioDirezione/6306 and MASE news https://www.mase.gov.it/portale/-/data-center-pubblicate-le-prime-indicazioni-operative-sul-procedimento-unico-per-le-autorizzazioni. Grade A.
- Before and alongside the 2026 single procedure, projects surface in a fragmented chain: municipal **SUE/SUAP** building/productive-activity portals, municipal planning variants, regional/national **VIA/VAS/AIA** files, fire-prevention files, grid-connection requests, and operator announcements.
- The best national public project repository is the MASE **Valutazioni e Autorizzazioni Ambientali - VAS/VIA/AIA** portal: https://va.mite.gov.it/. Search `Ricerca Progetti - VIA`, `Ricerca Installazioni - AIA`, and communications. Grade A. It already exposes many named datacenter projects in Lombardy, including Data4, Amazon Data Services Italy, STACK/Supernap, and Noviglio/Siziano/Rho/Pero/Settimo Milanese cases.
- Datacenters are often categorized in environmental files as **Centrali** because the trigger is emergency generator thermal capacity, not the server halls themselves. MASE adopted specific guidelines for datacenters with emergency generator capacity above 50 MWt by D.D. VA n. 257 del 02/08/2024: https://va.mite.gov.it/it-IT/Comunicazione/DettaglioDirezione/4755. Grade A.
- Grid is the strongest forward-looking signal but is noisy. Terna is competent for high and extra-high voltage connections, especially loads at or above 10 MW, and says the connection request is the first step of the route. Source: https://www.terna.it/it/sistema-elettrico/programmazione-territoriale-efficiente. Grade A for process. Terna/Lightbox and trade press report very large speculative data-center connection requests; treat aggregate GW as pipeline pressure, not real projects.
- Lombardy is the primary cluster and the only region with a mature data-center-specific regulatory frame as of this file. Regione Lombardia DGR XII/2629 of 24/06/2024 adopted guidelines for municipalities, and L.R. 3 giugno 2026 n. 11 created a regional siting regime. Official regional page: https://www.regione.lombardia.it/ambiente-e-territorio/red-procedimenti-autorizzatori-progetti-data-center. Grade A.
- Geography: Milan metro/Lombardy dominates; Piedmont/Turin is now a cloud-region seed; Veneto, Emilia-Romagna, Tuscany, Lazio/Rome, Campania/Naples, Sicily/Palermo-Catania, Liguria/Genoa, Puglia/Bari, and Sardinia have secondary signals from cloud edge, IXPs, telco, public-sector cloud, subsea cables, industrial land, and energy capacity.

Key lifecycle vocabulary:

`studio di fattibilita` < `istanza` < `procedimento unico` / `conferenza di servizi` < `verifica di assoggettabilita a VIA` < `VIA` / `AIA` < `provvedimento autorizzatorio` < `permesso di costruire` / `SCIA` / `DIA` < `inizio lavori` < `cantiere` < `collaudo` / `CPI` < `agibilita` < `messa in esercizio`

Count `provvedimento autorizzatorio`, `permesso di costruire`, `inizio lavori`, `CPI`, `agibilita`, or operator-verified launch as strong project evidence. Treat `richiesta di connessione`, `annuncio investimento`, or `manifestazione interesse` as planned/pipeline evidence only.

---

## 1. Italian and English query patterns

### 1.1 Core Italian terms

Use Italian first. English finds cloud/colo pages and international trade press.

```text
data center
datacenter
centro dati
centri dati
centro elaborazione dati
CED
server farm
cloud region
colocation OR co-location
housing
hyperscale OR hyperscaler
campus data center
procedimento unico data center
autorizzazione unica data center
permesso di costruire data center
SCIA data center
DIA centro elaborazione dati
SUAP data center
SUE data center
variante urbanistica data center
piano attuativo data center
piano regolatore data center
PGT data center
PRG data center
PUC data center
PAT PI data center
PUG data center
VIA data center
verifica di assoggettabilita data center
AIA data center
gruppi elettrogeni data center
potenza termica nominale data center
cabina primaria data center
stazione elettrica data center
connessione alla rete data center
allacciamento Terna data center
teleriscaldamento data center
recupero calore data center
acqua raffreddamento data center
certificato prevenzione incendi data center
agibilita data center
```

### 1.2 Official discovery queries

Substitute `{regione}`, `{provincia}`, `{comune}`, `{operator}`, `{site}`, `{legal_entity}`.

Planning and permits:

```text
"{comune}" "data center" "permesso di costruire"
"{comune}" "centro dati" "permesso di costruire"
"{comune}" "centro elaborazione dati" SCIA
"{comune}" "data center" "variante urbanistica"
"{comune}" "data center" "piano attuativo"
"{comune}" "data center" "delibera"
"{comune}" "data center" "conferenza di servizi"
site:{comune-domain} "data center" "permesso di costruire"
site:{comune-domain} "centro elaborazione dati" OR "centro dati"
site:{comune-domain} "data center" "SUAP"
site:{comune-domain} "data center" "albo pretorio"
site:{comune-domain} "data center" "determinazione"
filetype:pdf "data center" "permesso di costruire" "{comune}"
filetype:pdf "centro elaborazione dati" "agibilita" "{comune}"
```

MASE and environmental:

```text
site:va.mite.gov.it "data center" "{regione}"
site:va.mite.gov.it "centro dati" "{comune}"
site:va.mite.gov.it "centro elaborazione dati"
site:va.mite.gov.it "{operator}" "data center"
site:va.mite.gov.it "{legal_entity}" "VIA"
site:mase.gov.it "data center" "procedimento unico"
site:mase.gov.it "centri dati" "procedimento unico"
site:{regione-domain} "VIA" "data center"
site:{regione-domain} "AIA" "data center"
site:{provincia-domain} "data center" "VIA"
"{operator}" "{comune}" "gruppi elettrogeni"
"{project}" "potenza termica nominale" "data center"
```

Energy and grid:

```text
site:terna.it "data center" "connessione"
site:terna.it "data center" "rete di trasmissione"
site:terna.it "centri dati" "rete"
site:arera.it "data center" "connessione"
"{comune}" "data center" "stazione elettrica"
"{comune}" "data center" "cabina primaria"
"{comune}" "data center" "alta tensione"
"{comune}" "data center" "Terna"
"{comune}" "data center" "e-distribuzione"
"{comune}" "data center" "Areti" OR "Unareti" OR "A2A" OR "IRETI"
"{operator}" "{site}" "MW" "Italy"
"{operator}" "{site}" "MVA" "Italy"
```

Operator/cloud pivot:

```text
"AWS" "eu-south-1" "Milan"
"Amazon Data Services Italy" "data center" "VIA"
"Microsoft" "Italy North" "data center"
"Google Cloud" "europe-west8" "Milan"
"Google Cloud" "europe-west12" "Turin"
"Oracle Cloud" "eu-milan-1" OR "eu-turin-1"
"DATA4" "Milan" "VIA"
"STACK Infrastructure" "Siziano" OR "Milan"
"Equinix" "Milan" "ML"
"Aruba" "Ponte San Pietro" "data center"
"Retelit" "34 data centers" Italy
"Noovle" "data center" "Italy"
```

### 1.3 English queries

```text
"Italy" "data center" "single authorization"
"Italy" "data center" "building permit"
"Italy" "data center" "environmental impact assessment"
"Milan" "data center" "VIA"
"Milan" "data center" "grid connection"
"Turin" "cloud region" "data center"
"Rome" "data center" "permit"
"Italy" "hyperscale campus" "MW"
"Italy" "data center" "Terna" "connection requests"
```

---

## 2. Grade A official/regulatory backbone

### 2.1 MASE procedural and environmental portal

Primary URLs:

- MASE VIA/VAS/AIA portal: https://va.mite.gov.it/. Grade A.
- MASE operational notice for the data-center single procedure: https://va.mite.gov.it/it-IT/Comunicazione/DettaglioDirezione/6306. Grade A.
- MASE datacenter VIA guidelines, D.D. VA n. 257 del 02/08/2024: https://va.mite.gov.it/it-IT/Comunicazione/DettaglioDirezione/4755. Grade A.
- Example project pages:
  - Amazon Data Services Italy, `Progetto Datacenter edificio A e edificio B Rho/Pero (MI)`: https://va.mite.gov.it/it-IT/Oggetti/Info/11344. Grade A.
  - DATA4, `Progetto D4 Data Center MIL1 - Masterplan campus`, Settimo Milanese/Cornaredo: https://va.mite.gov.it/it-IT/Oggetti/Info/11512. Grade A.
  - STACK/Supernap expansion, Siziano: https://va.mite.gov.it/it-IT/Oggetti/Documentazione/7938/15674. Grade A.
  - Noviglio datacenter: https://va.mite.gov.it/it-IT/Oggetti/Info/9499. Grade A.

What to extract:

- project name, proponent legal entity, municipality/province/region;
- procedure type: `VIA`, `Verifica di Assoggettabilita a VIA`, `Verifica di Ottemperanza`, `AIA`, `procedimento unico`;
- dates: presentation, public consultation, integration requests, decision;
- emergency generators: count, thermal MW, electrical MW, fuel storage;
- grid works: substations, cable routes, voltage level, network operator;
- building evidence embedded in appendices: `DIA`, `SCIA`, `permesso di costruire`, fire-prevention certificate (`CPI`), `agibilita`;
- parcel/site details, campus phases, IT load if disclosed, water/cooling design, heat reuse.

Portal workflow:

1. Use the portal search for `data center`, `datacenter`, `centro dati`, `CED`, known operator names, and municipalities.
2. Open both `Info` and `Documentazione`; project PDFs may contain older municipal files that are not indexed by search engines.
3. Record public-observation deadlines and current status. Do not treat `istruttoria tecnica` as approval.
4. Use MASE IDs (`ID_VIP/ID_MATTM`, `Codice procedura`, `Codice istanza online`) as stable keys for deduplication.

### 2.2 2026 procedimento unico / legal route

- Legal basis: DL 21/2026 converted by Law 49/2026, Gazzetta Ufficiale source https://www.gazzettaufficiale.it/eli/id/2026/02/20/26G00041/SG. Grade A.
- MASE submission package: https://va.mite.gov.it/it-IT/Comunicazione/DettaglioDirezione/6306. Grade A.

Use this route for new projects from mid-2026 onward. Search for:

```text
"procedimento unico" "data center" "{comune}"
"procedimento unico" "centri dati" "{operator}"
"autorizzazione" "centro dati" "articolo 8" "DL 21/2026"
"avviso al pubblico" "centro dati" "{comune}"
site:va.mite.gov.it "procedimento unico" "data center"
site:mase.gov.it "procedimento unico" "centri dati"
```

Important caution: the procedure is new. There may be a transition period where old municipal/regional VIA/SUAP records coexist with national single-procedure files.

### 2.3 Municipal SUE/SUAP and planning

Italy has no national open building-permit register comparable to a single LPA database. The operating unit is the **Comune**, with routing through:

- **SUE** (`Sportello Unico per l'Edilizia`) for building applications.
- **SUAP** (`Sportello Unico per le Attivita Produttive`) for productive activity, siting, construction, expansion, and operation.
- **impresainungiorno.gov.it** national SUAP portal: https://www.impresainungiorno.gov.it/. Grade A for routing/process, but submitted files are often not public.
- Municipal `albo pretorio`, `amministrazione trasparente`, council deliberations, and planning portals.
- Official municipal land-use plans, whose names vary by region: `PGT` in Lombardy, `PRG/PRGC` in Piedmont and many regions, `PAT/PI` in Veneto, `PUG` in Emilia-Romagna/Puglia, `PUC` in Campania and parts of the south, `Piano Operativo` in Tuscany.

Municipal evidence to capture:

- `permesso di costruire`, `SCIA`, `DIA`, `CILA` only if relevant to actual works;
- `variante urbanistica`, `piano attuativo`, `accordo di programma`, `convenzione urbanistica`;
- `delibera di consiglio/giunta`, `determinazione dirigenziale`, `conferenza di servizi`;
- land sale/lease in industrial areas;
- fire-prevention and occupancy: `CPI`, `SCIA antincendio`, `agibilita`;
- district heating/waste heat agreements.

### 2.4 Regional VIA/VAS/AIA portals

For projects below national thresholds or handled regionally, search each region's environmental portal. Common patterns:

```text
site:{regione-domain} "Valutazione Impatto Ambientale" "data center"
site:{regione-domain} "Verifica di assoggettabilita" "data center"
site:{regione-domain} "Autorizzazione Integrata Ambientale" "data center"
site:{regione-domain} "VIA" "centro elaborazione dati"
```

Use regional portals as Grade A when hosted by the region/province/metropolitan city. Cross-check with MASE if emergency-generator capacity or national single-procedure status implies a MASE-level record.

### 2.5 Grid and energy

Primary official sources:

- Terna territorial programming/connection process: https://www.terna.it/it/sistema-elettrico/programmazione-territoriale-efficiente. Grade A.
- Terna 2025 Development Plan page: https://www.terna.it/en/media/press-releases/detail/2025-development-plan and report page https://www.terna-reports.it/2024/2025-development-plan. Grade A for grid-investment context.
- Terna Lightbox data-center analysis: https://lightbox.terna.it/it/insight/data-center-rete-trasmissione and https://lightbox.terna.it/it/sfide/data-center-green. Grade A-/B+ because it is Terna-owned editorial, useful for aggregate request counts and trends.
- ARERA planning/network materials may mention data-center connection pressure; example search result: https://www.arera.it/. Grade A for regulation, not facility census.

Grid search priorities:

1. Search Terna for `data center`, `centri dati`, `connessione`, `stazione elettrica`, `cabina primaria`.
2. Search regional DSOs by area:
   - Lombardy/Milan: Unareti, A2A, e-distribuzione, Terna.
   - Piedmont/Turin: IRETI, e-distribuzione, Terna.
   - Veneto: e-distribuzione, AGSM AIM, Terna.
   - Emilia-Romagna: e-distribuzione, Hera, IRETI, Terna.
   - Tuscany: e-distribuzione, Terna.
   - Lazio/Rome: Areti, e-distribuzione, Terna.
   - Campania: e-distribuzione, Terna.
   - Sicily: e-distribuzione, Terna.
3. Search municipal council files for substations and cable corridors.

Never equate a Terna connection request with a buildable project. Record separately: `requested grid capacity`, `connection quote accepted`, `authorized network works`, `building/environmental permit`, `construction`, and `operational IT load`.

### 2.6 Cloud/PA regulator sources: AGCOM, ACN, AgID, DTD

- **AGCOM**: https://www.agcom.it/. Grade A for communications-market regulation. AGCOM is not currently a facility-level datacenter permit registry. It is useful for telecom/CDN/cloud regulatory context and operator identity, especially where datacenters support electronic communications networks.
- **ACN cloud qualification**: https://www.acn.gov.it/portale/cloud/qualificazione-e-adeguamento and catalog page https://www.acn.gov.it/portale/catalogo-delle-infrastrutture-digitali-e-dei-servizi-cloud. Grade A for qualified PA cloud/infrastructure providers; not a complete physical facility list.
- **Strategia Cloud Italia / Dipartimento per la trasformazione digitale**: https://innovazione.gov.it/dipartimento/focus/strategia-cloud-italia/. Grade A for public-sector cloud strategy and data classification.
- **AgID PA cloud page**: https://www.agid.gov.it/en/infrastructures/pa-cloud. Grade A policy background.
- **Polo Strategico Nazionale (PSN)**: https://www.polostrategiconazionale.it/. Grade A/B for official PSN operator pages and PA cloud migration context; verify physical facility claims through operator/permit files.

Use ACN catalog/provider qualification as an operator seed list, then pivot to permits, MASE, municipal files, and official facility pages.

---

## 3. Official cloud and operator seed lists

### 3.1 Hyperscale cloud regions - official pages

Cloud-region pages prove country/metro region existence but not exact buildings.

| Provider | Official source | Italy signal | Enumeration use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/local/italy/milan/ | `eu-south-1`, Europe (Milan), 3 AZs | Search `Amazon Data Services Italy S.r.l.`, `Rho/Pero`, `Milan`, MASE VIA, Lombardy/Milan municipal files. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Italy North / Milan geography | Search `Microsoft`, `Noovle`, `PSN`, `Italy North`, and Milan metro permits. |
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/about/locations | `europe-west8` Milan; also Turin region signal on Google/partner pages where available | Search `Google Cloud`, `TIM`, `Noovle`, Milan/Turin, ACN qualification, MASE files. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | `eu-milan-1` Italy Northwest (Milan); `eu-turin-1` Italy North (Turin) | Pivot to Milan/Turin, TIM Enterprise host-partner announcements, ACN qualification, and municipal/environmental files. |

### 3.2 Colocation / carrier-neutral / Italian cloud operators

Use official pages first, then MASE/municipal evidence.

| Operator | Official source | Italy seed |
|---|---|---|
| Equinix | https://www.equinix.com/data-centers/europe-colocation/italy-colocation/milan-data-centers | Milan metro ML facilities; search `Equinix ML`, `Settimo Milanese`, `Milan`, `CPI`, `SCIA`. |
| DATA4 | https://www.data4group.com/en/data-center-in-milan-italy/ | Milan campus; MASE project `D4 Data Center MIL1` at Settimo Milanese/Cornaredo. |
| STACK Infrastructure | https://www.stackinfra.com/locations/emea/milan/ | Milan/Siziano/Supernap lineage; search MASE `Supernap`, `Infrastructure Italia Land`, `Siziano`. |
| Aruba | https://www.aruba.it/ and Aruba datacenter/cloud pages | Ponte San Pietro/Bergamo, Arezzo, Rome/IT3 style facilities; search municipal and fire/environmental files. |
| Retelit / Retelit Data Center | https://www.retelit.it/en/housing | Official page states a network of 34 Italian data centers plus Innsbruck; use as seed, verify addresses and permits locally. |
| TIM Enterprise / Noovle | https://www.noovle.com/ and TIM Enterprise pages | Cloud/Google/PSN partner, Italy cloud regions and telco DC estate. Search `Noovle data center`, `TIM data center`, `PSN`, Milan/Turin/Rome. |
| Digital Realty | https://www.digitalrealty.com/ | IDA founding/operator seed for Italy; search Milan area projects and official announcements. |
| Vantage Data Centers | https://vantage-dc.com/ | IDA founding/operator seed and hyperscale pipeline lead; verify through MASE/municipal records before counting. |
| Rai Way Edge / Rai Way | https://www.raiway.it/ | Edge/datacenter infrastructure seed; likely smaller or broadcast/telco-linked facilities. |
| Seeweb, Serverplan, Deda Cloud, Register.it, Irideos legacy, Fastweb, WindTre, Vodafone, Lepida, CSI Piemonte | official operator/ACN pages | Regional/PA/telco cloud and edge facilities. Count only when physical facility evidence exists. |

Association/trade seed:

- IDA - Italian Datacenter Association: https://italiandatacenter.com/en/ and member page https://italiandatacenter.com/en/members/. Grade B for market/operator discovery, A-/B when directly describing the association itself. Founding/member names are useful seeds but not facility proof.
- Data Center Dynamics Italy articles: https://www.datacenterdynamics.com/. Grade B; use to find operators, investment announcements, and then follow primary links.
- CorCom, Agenda Digitale, Key4biz, QualEnergia, Il Sole 24 Ore, Industria Italiana. Grade B for sourced investment/grid/regulatory news; verify with MASE, Terna, region, or operator pages.

---

## 4. Per-division enumeration workflow

Italy should be enumerated as a funnel:

1. **National official sweep**: MASE VIA/VAS/AIA search for `data center`, `centro dati`, `CED`, and operator names. Add all records with MASE IDs and procedure statuses.
2. **New single-procedure sweep**: MASE communications and `procedimento unico` public notices. New applications after July 2026 should increasingly appear here.
3. **Cloud/colo seed sweep**: AWS/Azure/GCP/OCI region pages, Equinix, DATA4, STACK, Aruba, Retelit, TIM/Noovle, IDA members.
4. **Grid sweep**: Terna process/context, Terna/DSO substations, municipal `cabina primaria` and `stazione elettrica` documents. Keep request capacity separate from permitted/operating capacity.
5. **Regional environmental sweep**: regional VIA/VAS/AIA portals and regional guidelines, especially Lombardy and any region with active `centro dati` files.
6. **Comune sweep**: for every candidate municipality, search SUE/SUAP, planning plan names, `albo pretorio`, `delibere`, `determine`, and council minutes.
7. **Legal-entity pivot**: search exact proponent/SPV names found in MASE or permits through Registro Imprese/REA references, operator pages, and local filings. Do not rely on generic brand names alone.

### 4.1 Priority regions and query routing

| Region | Priority | Main official route | Target places/operators | Query notes |
|---|---:|---|---|---|
| Lombardia | Very high | MASE VIA/VAS/AIA; Regione Lombardia datacenter page; municipal PGT/SUE/SUAP; Citta Metropolitana Milano; Terna/Unareti/A2A/e-distribuzione | Milan, Rho, Pero, Settimo Milanese, Cornaredo, Siziano, Noviglio, Lacchiarella, Liscate, Bergamo/Ponte San Pietro, Brescia | Search MASE first. Use `PGT`, `DGR XII/2629`, `L.R. 11/2026`, `AIA`, `gruppi elettrogeni`, `teleriscaldamento`. |
| Piemonte | High | Regione Piemonte VIA; municipal PRG/PRGC/SUAP; Torino geoportal; Terna/IRETI | Turin, Novara, Alessandria, Vercelli, industrial/logistics corridors | Oracle `eu-turin-1`, Google/TIM/Noovle Turin signals. Queries: `Torino data center PRG`, `Piemonte centro dati VIA`, `IRETI data center`. |
| Veneto | Medium/high | Regione Veneto VIA; municipal PAT/PI and SUAP; Terna/e-distribuzione/AGSM AIM | Padua, Verona, Venice/Mestre, Vicenza, Treviso | Search `PAT`, `PI`, `variante urbanistica`, `data center Veneto VIA`, `cabina primaria data center`. |
| Emilia-Romagna | Medium/high | Regione Emilia-Romagna VIA; municipal PUG/SUAP; Lepida/PA cloud; Terna/Hera/IRETI | Bologna, Modena, Parma, Reggio Emilia, Piacenza, Ravenna | Include public research/HPC: CINECA/INFN are not commercial colo unless facility-grade; search `PUG data center`, `Lepida data center`, `centro elaborazione dati`. |
| Toscana | Medium | Regione Toscana VIA; municipal Piano Operativo/PRG/SUAP; Terna/e-distribuzione | Arezzo, Florence, Pisa, Prato, Livorno | Aruba/Arezzo and telco/cloud seeds. Search `Piano Operativo data center`, `Arezzo data center permesso`. |
| Lazio | High | Regione Lazio VIA; Roma Capitale SUE/SUAP/PRG; Citta Metropolitana Roma; Areti/e-distribuzione/Terna | Rome, Pomezia, Fiumicino, Guidonia, Tecnopolo/PSN-related leads | Search `Roma data center permesso`, `Areti cabina primaria data center`, `Namex`, `PSN`, `Noovle`, `Aruba`. |
| Campania | Medium | Regione Campania VIA; municipal PUC/SUAP; e-distribuzione/Terna; port/subsea and IXP leads | Naples, Caserta, Salerno, Nola logistics belt | Search `PUC data center`, `Napoli data center SUAP`, `Namex Napoli`, `centro elaborazione dati Campania`. |
| Sicilia | Medium | Regione Siciliana VIA/VAS; municipal PRG/SUAP; Terna/e-distribuzione; subsea/edge leads | Palermo, Catania, Carini, Termini Imerese, Messina | AWS edge Palermo is a seed, not facility proof. Search `Sicilia data center VIA`, `Palermo data center`, `cavi sottomarini data center`. |
| Liguria | Medium | Regione Liguria VIA; Genova municipal planning/SUAP; Terna/e-distribuzione; port/subsea | Genoa, Savona | Search `Genova data center`, `Liguria centro dati VIA`, subsea/IXP terms. |
| Puglia | Medium | Regione Puglia VIA; municipal PUG/SUAP; Terna/e-distribuzione | Bari, Brindisi, Taranto, Lecce | Namex Bari/edge and public cloud seeds; search `PUG data center Bari`, `centro dati Puglia`. |
| Sardegna | Medium/low | Regione Sardegna VIA; municipal PUC/SUAP; Terna/e-distribuzione | Cagliari, Sassari, industrial/renewable zones | Watch energy-rich sites and submarine cable claims; verify permits. |
| Friuli-Venezia Giulia | Medium/low | regional VIA; municipal PRGC/SUAP; Terna/e-distribuzione | Trieste, Udine, Pordenone | Search for port/subsea/HPC/industrial leads. |
| Trentino-Alto Adige/Sudtirol | Medium/low | Province of Trento/Bolzano environmental/building portals; municipal PRG | Trento, Bolzano, Brennercom/Retelit leads | Search Italian and German: `Rechenzentrum Bozen`, `Datacenter Bolzano`, `centro dati Trento`. |
| Marche, Umbria, Abruzzo, Molise, Basilicata, Calabria, Valle d'Aosta | Low baseline | regional VIA + municipal PRG/SUAP + telco/PA clouds | regional capitals and industrial parks | Search all terms once per region and pivot from ACN/operator lists. |

### 4.2 Municipality/province drill-down pattern

For each hit, derive these searches:

```text
site:{comune-domain} "{project}" OR "{operator}"
site:{comune-domain} "data center" "delibera"
site:{comune-domain} "data center" "determinazione"
site:{comune-domain} "data center" "albo pretorio"
site:{comune-domain} "data center" "permesso di costruire"
site:{comune-domain} "data center" "agibilita"
site:{comune-domain} "data center" "CPI"
site:{provincia-domain} "data center" "VIA" OR "AIA"
site:{citta-metropolitana-domain} "data center" "conferenza di servizi"
```

If the municipality uses a third-party portal, search the portal name plus the municipality:

```text
"{comune}" "SUE" "data center"
"{comune}" "SUAP" "data center"
"{comune}" "impresainungiorno" "data center"
"{comune}" "Geoportale" "data center"
"{comune}" "albo pretorio" "{operator}"
```

---

## 5. Reliability and deduplication rules

### 5.1 Reliability grades

- **A**: MASE VIA/VAS/AIA or procedimento unico records; Gazzetta Ufficiale laws; regional/municipal permits and planning acts; Terna/DSO official connection or network-work documents; operator official facility pages for live facilities; ACN catalog for PA cloud qualification.
- **B**: IDA, operator association pages, trade press, legal client alerts, market reports, conference pages, and sourced news that name operators/sites/MW but do not include the primary permit.
- **C**: generic datacenter maps, broker listings, scraped directories, social posts, unsourced investment claims, and SEO pages.

### 5.2 Deduplication keys

Use a facility/project key based on:

```text
operator/proponent legal entity + municipality + site/campus name + MASE ID/procedure code + parcel/address if available
```

Common duplicate traps:

- brand vs SPV: `STACK` vs `Supernap Italia` vs `Infrastructure Italia Land ...`;
- `DATA4 Milan campus` vs individual MIL buildings/phases;
- hyperscale cloud region vs underlying colo/host partner;
- municipal building files embedded as appendices inside MASE documentation;
- grid connection request vs actual building/environmental permit;
- old `CED` in offices/telco exchanges vs facility-grade datacenter.

### 5.3 Capacity fields

Track separate fields:

- `IT load MW`;
- `gross electrical capacity / utility import MW or MVA`;
- `emergency generator electrical MW`;
- `emergency generator thermal MWt`;
- `Terna/DSO requested connection capacity`;
- `authorized grid works`;
- `operational consumption` if reported.

Italian environmental files often disclose generator thermal capacity more clearly than IT load. Do not convert or compare without noting assumptions.

---

## 6. Fast-start source checklist

Start every Italy refresh with these exact URLs and queries:

```text
https://va.mite.gov.it/
site:va.mite.gov.it "data center"
site:va.mite.gov.it "centro dati"
site:va.mite.gov.it "centro elaborazione dati"
site:mase.gov.it "procedimento unico" "data center"
site:regione.lombardia.it "data center"
site:terna.it "data center" "connessione"
site:acn.gov.it "Catalogo delle Infrastrutture digitali e dei Servizi cloud"
site:agcom.it "cloud" "data center"
site:italiandatacenter.com "members"
```

Then seed operators:

```text
"Amazon Data Services Italy" "data center" "VIA"
"DATA 4 MILAN" "data center" "VIA"
"Supernap Italia" "Siziano" "data center"
"Infrastructure Italia Land" "data center"
"Noviglio datacenters" "data center"
"Equinix" "Milan" "data center"
"Aruba" "Ponte San Pietro" "data center"
"Retelit" "housing" "34 data centers"
"Noovle" "data center" "Italy"
```

Recommended first pass by region:

1. Lombardy/Milan metro: MASE plus Lombardy regional page and municipal PGT/SUE files.
2. Piedmont/Turin: OCI/Google/TIM cloud seeds plus regional/municipal PRG/VIA files.
3. Lazio/Rome: PA cloud/PSN/Namex/Areti plus Roma Capitale and regional VIA.
4. Veneto/Emilia-Romagna/Tuscany: regional VIA plus municipal planning and operator seeds.
5. Campania/Sicily/Puglia/Liguria/Sardinia: subsea/edge/IXP leads plus regional VIA and municipal SUAP/PRG.

---

## 7. Notes on current known official examples

These examples are not a complete census; they prove where the official paper trail appears:

- Rho/Pero (MI): `Progetto Datacenter edificio A e edificio B Rho/Pero (MI)`, proponent Amazon Data Services Italy S.r.l., MASE page https://va.mite.gov.it/it-IT/Oggetti/Info/11344. Grade A.
- Settimo Milanese/Cornaredo (MI): `Progetto D4 Data Center MIL1 - Masterplan campus`, proponent DATA 4 MILAN S.p.A., MASE page https://va.mite.gov.it/it-IT/Oggetti/Info/11512. Grade A.
- Siziano (PV): `Progetto di ampliamento del Data Center Supernap sito in via Marche 8 a Siziano`, MASE documentation https://va.mite.gov.it/it-IT/Oggetti/Documentazione/7938/15674. Grade A.
- Noviglio/Lacchiarella (MI): `Nuovo Data Center da realizzarsi in Frazione Santa Corinna`, proponent Noviglio datacenters Mxp I S.r.l., MASE page https://va.mite.gov.it/it-IT/Oggetti/Info/9499. Grade A.
- Milan cloud region: AWS `eu-south-1`, Google `europe-west8`, Azure Italy North, OCI `eu-milan-1`; official cloud pages are Grade A for regional service availability, not physical address.
- Turin cloud region: OCI `eu-turin-1` is listed in Oracle regions; use as a Piedmont seed, not proof of a specific building address.

