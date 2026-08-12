# NO Explorer Industry - Norway Datacenter Enumeration

Date: 2026-08-12. Scope: Norway data-center discovery from operators, industry association pages, cloud-region pages, trade press, construction announcements, and market directories. Always reconcile with the official methodology in `explorer-official.md`.

Reliability grades:

- Grade A: operator-owned facility page, official cloud-region page, Nkom registration, municipal record, environmental permit, NVE/Statnett document.
- Grade B: credible trade press, stock-exchange/company press release, construction contractor announcement, or association profile with named site and date.
- Grade C: directory, market report, unsourced social post, or inferred cloud/metro location.

Key correction from the draft: Google has no public Google Cloud region in Norway, but Google/WS Computing is building a physical data center at Gromstul in Skien. Do not confuse "cloud region exists" with "physical data center exists"; both must be represented separately.

## 0. Industry structure and source priorities

### 0.1 Start with Nkom, then enrich

Nkom is now the public commercial-operator backbone:

- https://nkom.no/datasenter/oversikt
- CSV: https://stenonicprdnoea01.blob.core.windows.net/enonicpubliccontainer/prd/tildeling/datasenter/datasenter-operatorer.csv

Verified on 2026-08-12: Nkom page updated 11.08.2026, 115 registered data centres including internal sites, 61 commercial operators listed. The public Nkom list names commercial operators but not every site location, so enrich it with operator pages and permits.

Nkom-listed commercial operators worth prioritizing for facility pivots include:

```text
GREEN MOUNTAIN AS
GREEN MOUNTAIN INNLANDET AS
BULK DATA CENTERS OS-IX AS
BULK DATA CENTERS N01 AS
BULK DATA CENTERS N01 DCM101 AS
BULK DATA CENTERS N01 DCM102 AS
SI OSL 01 AS
SI OSL 02 AS
SI OSL 03.1 AS
SI OSL 03.2 AS
SI OSL 04 AS
NSCALE DRIFT AS
LEFDAL MINE DATACENTER AS
ASP DATA CENTER AS
STORESPEED AS
GLOBALCONNECT AS
DATAFJELLET AS
TUSSA IKT AS
TAFJORD CONNECT AS
NEAS IT AS
TROLLFJORD IKT SENTER AS
TYDAL DATA CENTER AS
EXANORTH AS
NTE TELEKOM AS
REN ROROS DIGITAL AS
POLARDC DRA AS
EVINY FIBER AS
TELIA NORGE AS
ATEA AS
BLIX SOLUTIONS AS
ORANGE BUSINESS DIGITAL NORWAY AS
```

### 0.2 Association and market sources

- Norsk Datasenterindustri / Norwegian Datacenter Industry: https://www.datasenterindustrien.no/ - Grade B+ for membership/operator universe; not a facility census.
- Business Norway: https://businessnorway.com/ - Grade B for investment-promotion case studies; use as a lead.
- Doffin / public procurement entry point: https://www.anskaffelser.no/ - Grade A for procurement notices, not proof of a private facility.
- Data Center Dynamics: https://www.datacenterdynamics.com/ - Grade B.
- Datacenter Forum: https://www.datacenter-forum.com/ - Grade B.
- Baxtel: https://baxtel.com/ - Grade B-/C+ depending on source links.
- DataCenterMap: https://www.datacentermap.com/norway/ - Grade C+; useful for addresses and lead discovery, not final proof.

## 1. Search templates

### 1.1 Operator and facility discovery

```text
"{operator}" Norge datasenter
"{operator}" Norway data center
"{operator}" "{municipality}" datasenter
"{operator}" "{site}" MW
"{operator}" "{site}" "PUE"
"{operator}" "{site}" "heat reuse"
"{operator}" "{site}" "nødstrøm"
"{operator}" "{site}" "forurensningsloven"
site:{operator-domain} datasenter
site:{operator-domain} "data center" Norway
site:datasenterindustrien.no "{operator}"
```

### 1.2 Status and construction

```text
"{site}" "under construction" Norway
"{site}" "byggestart" datasenter
"{site}" "ferdigstilt" datasenter
"{site}" "overlevert" datasenter
"{site}" "i drift" datasenter
"{site}" "rammetillatelse"
"{site}" "igangsettingstillatelse"
"{site}" "utslippstillatelse"
"{site}" "nettilknytning"
"{site}" "transformatorstasjon"
```

### 1.3 Cloud and hyperscale

```text
site:learn.microsoft.com azure "Norway East" "Norway West"
site:datacenters.microsoft.com "Norway East"
site:docs.aws.amazon.com "Norway" "Region"
site:cloud.google.com/about/locations Norway
site:datacenters.google Norway Skien
site:oracle.com/cloud "Norway" "region"
"WS Computing" Google Skien Gromstul
"Google" "600 million euro" Skien data center
```

## 2. Operator and platform map

Treat official operator pages as Grade A for existence, marketed location, and current operating status stated by that operator. Treat future full-build MW as Grade B unless a permit/grid record independently supports it.

| Operator/platform | Source URLs | Facility notes and grading |
|---|---|---|
| Green Mountain | https://greenmountain.no/data-centers/ | A for operator portfolio. Norwegian sites: SVG-Rennesoy, TEL-Rjukan, OSL-Enebakk, OSL-Hamar. |
| Green Mountain OSL-Enebakk | https://greenmountain.no/data-center/osl-enebakk/ | A for Enebakk location, 75,000 m2, three buildings, 93 MW line-of-sight/site capacity as marketed. Verify permits in Enebakk. |
| Green Mountain OSL-Hamar | https://greenmountain.no/data-center/osl-hamar/ | A for Hamar/Innlandet campus, TikTok tenant, first three buildings complete/in operation, 90 MW used/committed and 150 MW planned capacity as operator-stated. Verify Hamar/Loten/NVE details. |
| Green Mountain TEL-Rjukan | https://greenmountain.no/data-center/tel-rjukan/ | A for Tinn/Rjukan operating campus, 29,000 m2 and 50 MW site capacity as operator-stated. |
| Green Mountain SVG-Rennesoy | https://greenmountain.no/data-center/svg-rennesoy/ | A for Stavanger/Rennesoy operating mountain-hall site, 22,600 m2 and 25 MW site capacity as operator-stated. Environment permit evidence available via Norske utslipp/Statsforvalteren. |
| Bulk OS-IX | https://bulkinfrastructure.com/data-centers/locations/os-ix | A for Oslo Internet Exchange facility. Verify current expansion/power in Oslo records; directory claims vary. |
| Bulk N01 | https://bulkinfrastructure.com/data-centers/locations/n01 | A for Bulk's marketed Agder/Southern Norway campus, 3 km2 zoned for data centers, up to 1 GW marketed capacity. Confirm exact municipality and permits before facility rows. |
| STACK Infrastructure / DigiPlex legacy | https://www.stackinfra.com/ | A/B for operator ownership; use Nkom SPVs `SI OSL * AS` and municipal records for Oslo/Fetsund/Ringerike assets. |
| Lefdal Mine Datacenter | https://www.lefdalmine.com/ | A for Vestland underground campus. Confirm AI/HPC use with Sigma2/HPE: https://www.sigma2.no/our-data-centre and https://www.sigma2.no/procurement-project-hpc-a2 |
| Nscale Glomfjord | https://www.nscale.com/product/glomfjord | A for operator-stated Nordland/Glomfjord AI data center, 30 MW operational and expandable to 60 MW. Nkom lists NSCALE DRIFT AS. Verify Meloy/NVE/Statsforvalteren. |
| atNorth NOR01 Haugaland | https://www.atnorth.com/nordic-data-centers/norway-data-centers/haugaland-nor01/ | A for operator-stated planned site at Haugaland Business Park, 36 ha, 120 MW initial phases, 350 MW site capacity. Verify Tysvaer and grid records before treating as permitted/under construction. |
| WS Computing / Google Skien | municipal and environmental URLs below | A for Skien/Gromstul project from municipality and Statsforvalteren. Operator/public branding should be recorded as Google/WS Computing carefully because permits are under WS Computing AS. |
| PolarDC | https://www.polardc.com/ and https://www.polardc.com/current-locations | A for operator existence and claimed Norway locations; C/B for exact DRA/HER01/MW until municipal records confirm. Nkom lists POLARDC DRA AS. |
| Magnora Data Center / Storespeed | https://magnoradc.com/ and https://magnoraasa.com/company-portfolio/magnora-data-center-norway/ | A/B for Magnora's own project portfolio; Storespeed is Nkom-listed. Averoya 100 MW is development, not operational unless permits prove it. |
| Datafjellet | https://www.datafjellet.no/ | A for Bergen mountain-hall operator-marketed facility; verify through Bergen records. |
| Tussa IKT | https://www.tussa.no/bedrift/it/tussa-datasenter | A for operator-stated data-center services on Sunnmore; verify Orsta/Hovdebygda records. |
| Tafjord Connect | https://www.tafjord.no/bedrift/fiber/produkt-tjenester/colocation/ | A for operator-stated colocation; verify Alesund facility specifics. |
| NEAS IT | https://neas.no/bedrift/it/neas-datasenter/ | A for operator-stated local data centers in Kristiansund and Oppdal; verify municipality records. |
| GlobalConnect | https://globalconnectcarrier.com/services/data-center-and-colocation/ | A for Nordic colocation offering; Norwegian facility details often directory-derived, so verify Oslo/Trondheim addresses. |
| Tydal Data Center / Bitdeer | Nkom plus trade/Bitdeer/DCI leads | Nkom lists Tydal Data Center AS. Large 180 MW AI claims are B until Tydal/NVE/Statsforvalteren records are captured. |
| Exanorth | Nkom plus Norwegian press | Nkom lists Exanorth as crypto-mining. Namsskogan/Tunnsjodalen location is B until municipal/grid records are captured. |

## 3. Cloud-region facts

Cloud pages are Grade A for region availability and geography, not for physical building address.

| Platform | Official source | Norway treatment |
|---|---|---|
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/blog/microsoft-cloud-in-norway-opens-with-availability-of-microsoft-azure/ | Norway East and Norway West are live Azure regions. Use as metro anchors only; physical sites are not public. |
| Microsoft data-center region pages | https://datacenters.microsoft.com/gl_regions/norwayeast/ | A for Microsoft public regional description; not a facility address. |
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No AWS Norway region in the official region list as of this methodology date. Treat 2022 Oslo-region announcements as stale leads unless AWS official list changes. |
| Google Cloud | https://cloud.google.com/about/locations/ | No public Google Cloud Norway region in official locations. Separately, Google/WS Computing has a physical Skien/Gromstul data-center project. |
| Google data centers | https://datacenters.google/ | Use for Google corporate data-center program; local proof for Norway currently comes from Skien municipality and WS Computing permits. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No public Norway cloud region in official list. |
| Sigma2 | https://www.sigma2.no/ | National research-compute operator. Sigma2 confirms national HPC/AI infrastructure at Lefdal Mine. |

## 4. Per-division industry leads

### Oslo

Confirmed/strong leads:

- Bulk OS-IX, Oslo - Grade A operator page; verify PBE permits for expansions.
- STACK/DigiPlex Oslo SPVs (`SI OSL * AS`) - Grade A Nkom for operator registration; Grade B/C until each facility address is tied to municipal/operator page.
- GlobalConnect Oslo/Nydalen, Telia/Telenor/Blix/Orange/Atea colocation - Grade A/B for operator universe; verify addresses in Oslo PBE/Nkom/operator pages.

Search:

```text
"Hans Møller Gasmanns vei 9" datasenter
site:innsyn.pbe.oslo.kommune.no "datasenter"
"SI OSL" Oslo datasenter
"DigiPlex" Ulven Oslo datasenter
"GlobalConnect" Nydalen datasenter
```

### Rogaland

Confirmed/strong leads:

- Green Mountain SVG-Rennesoy - Grade A.
- atNorth NOR01 Haugaland/Gismarvik/Tysvaer - Grade A for announced operator site, B for development status until permits.
- Green Mountain Sandnes/Vagle, Time/Undheim, Haugaland options - B/C until municipal records.
- Asp Data Center AS/Suldal - Nkom Grade A operator row; facility details need municipal confirmation.
- Azure Norway West - Grade A cloud-region fact, C for physical address unless a permit confirms it.

Search:

```text
site:stavanger.kommune.no "Green Mountain" "Rennesøy"
site:sandnes.kommune.no datasenter Vagle
site:time.kommune.no datasenter Undheim
site:tysver.kommune.no OR site:tysvaer.kommune.no datasenter Gismarvik
"Asp Data Center" Suldal
"Microsoft" Sandnes Kvålkroken datasenter
```

### More and Romsdal

Confirmed/strong leads:

- Tussa IKT, Sunnmore/Orsta - Grade A operator page; Nkom-listed.
- Tafjord Connect, Alesund - Grade A operator page; Nkom-listed.
- NEAS IT, Kristiansund/Oppdal - Grade A operator page; Nkom-listed.
- Magnora Scale Averoya, near Kristiansund/Averoy - Grade A/B development from Magnora, not operational proof.

Search:

```text
site:kristiansund.kommune.no datasenter NEAS
site:averoy.kommune.no datasenter Magnora
site:alesund.kommune.no datasenter Tafjord
site:orsta.kommune.no datasenter Tussa
"Magnora Scale Averøya" datasenter
```

### Northland

Confirmed/strong leads:

- Nscale Glomfjord, Meloy - Grade A operator page; Nkom-listed as NSCALE DRIFT AS.
- Trollfjord IKT Senter, Stokmarknes/Hadsel - Grade A Nkom operator row, B/C facility detail until local proof.
- Kolos Ballangen - dormant historic lead; do not count as active without new official evidence.

Search:

```text
site:meloy.kommune.no Nscale Glomfjord datasenter
site:hadsel.kommune.no Trollfjord IKT datasenter
site:nve.no Glomfjord datasenter
"Kolos" Ballangen datasenter status
"Svartisen" "5 MW" Statnett
```

### Svalbard

No confirmed commercial data-center operator from reviewed sources. Keep separate from mainland Arctic marketing. Search local/ground-station sources only to document exclusions.

### Jan Mayen

No confirmed commercial data-center operator. Treat as negative unless a defense/meteorological telecom facility is explicitly in scope; do not classify such rooms as commercial colocation.

### Viken: Akershus, Buskerud, Ostfold

Confirmed/strong leads:

- Green Mountain OSL-Enebakk - Grade A.
- STACK/DigiPlex Fetsund/Lillestrom - Grade A Nkom SPV, B/C until address/permit confirmation.
- Storespeed Halden/Fredrikstad - Nkom-listed; Magnora says Storespeed operates a data center in Halden. Verify operator page and Halden records.
- Ringerike/Treklyngen - B/C development/land lead.

Search:

```text
site:enebakk.kommune.no "Green Mountain" datasenter
site:lillestrom.kommune.no "DigiPlex" OR "STACK" OR "Heiaveien"
site:ringerike.kommune.no datasenter Treklyngen
site:halden.kommune.no Storespeed datasenter
site:fredrikstad.kommune.no Storespeed
```

### Inland

Confirmed/strong leads:

- Green Mountain OSL-Hamar/Heggvin - Grade A operator page and Nkom operator rows.
- Eidsiva Digital AS - Nkom-listed; verify facility role.
- Elverum/Arcem-type leads - C/B until local records.

Search:

```text
site:hamar.kommune.no Heggvin datasenter
site:loten.kommune.no Heggvin datasenter
site:nve.no Heggvin transformatorstasjon
"Green Mountain Innlandet" datasenter
"Eidsiva Digital" datasenter
site:elverum.kommune.no datasenter
```

### Vestfold and Telemark

Confirmed/strong leads:

- Green Mountain TEL-Rjukan/Tinn - Grade A.
- WS Computing/Google Gromstul/Skien - Grade A from Skien municipality and Statsforvalteren.
- PolarDC DRA/Tordal/Heroya/Porsgrunn - Nkom-listed operator; exact sites are B/C until municipal records.

Verified URLs:

- Skien municipality Google/Gromstul timeline: https://www.skien.kommune.no/by-og-naeringsutvikling/google-etablering-i-skien-kommune/tidslinje-hva-har-skjedd-fram-til-naa/
- Statsforvalteren Datasenter 1 permit: https://www.statsforvalteren.no/vestfold-og-telemark/miljo-og-klima/forurensning/tillatelse-til-ws-computing-as-for-datalagringssenter-pa-gromstul-i-skien/
- Statsforvalteren Datasenter 2 hearing: https://www.statsforvalteren.no/vestfold-og-telemark/horinger/2026/06/soknad-om-tillatelse-etter-forurensningsloven---ws-computing-as---datasenter-2-gromstul/

Search:

```text
site:skien.kommune.no "WS Computing"
site:skien.kommune.no Gromstul datasenter
site:tinn.kommune.no "Green Mountain" Rjukan
site:porsgrunn.kommune.no PolarDC Herøya datasenter
site:drangedal.kommune.no Tordal datasenter
```

### Agder

Confirmed/strong leads:

- Bulk N01 Southern Norway/Agder - Grade A operator page; verify exact municipality/permits.
- Bulk Kristiansand references in directories/trade press - B/C unless tied to N01 or municipal records.
- Tonstad/Sirdal and former industrial power sites - watch-list.

Search:

```text
site:kristiansand.kommune.no Bulk N01 datasenter
site:vennesla.kommune.no Bulk N01 datasenter
site:sirdal.kommune.no Tonstad datasenter
site:nve.no Bulk N01
"Bulk" "N01" "Agder" "1GW"
```

### Westland

Confirmed/strong leads:

- Lefdal Mine Datacenter - Grade A.
- Sigma2/HPE Olivia at Lefdal - Grade A/B depending on source; use Sigma2 as primary.
- Datafjellet Bergen - Grade A operator page; verify Bergen permits.
- Eviny Fiber AS - Nkom-listed; verify if it operates customer-facing data-center facilities.
- Bergen/Husnes Arcem/Polar market leads - B/C until official records.

Search:

```text
site:stad.kommune.no Lefdal datasenter
site:stryn.kommune.no Lefdal datasenter
site:bergen.kommune.no Datafjellet datasenter
site:kvinnherad.kommune.no Husnes datasenter
"Eviny Fiber" datasenter
"Lefdal Mine" Sigma2 Olivia
```

### Trondelag

Confirmed/strong leads:

- Tydal Data Center AS - Nkom-listed; Bitdeer/DCI large AI data-center claims are B until local/grid/environment records are found.
- Exanorth AS - Nkom-listed crypto-mining; Namsskogan/Tunnsjodalen claims need local confirmation.
- NTE Telekom AS - Nkom-listed; search Moholt/Steinkjer/Trondheim public-sector data-center material.
- Ren Roros Digital AS - Nkom-listed; local data-center/cloud-service lead.
- GlobalConnect Trondheim - directory/operator-colocation lead; verify address and Nkom/operator linkage.

Search:

```text
site:tydal.kommune.no "Tydal Data Center"
site:nve.no "Tydal Data Center"
site:namsskogan.kommune.no Exanorth datasenter
site:roros.kommune.no "Ren Røros Digital" datasenter
site:trondheim.kommune.no "Moholt Datasenter"
"GlobalConnect" Trondheim "Prinsens gate 39"
```

### Troms and Finnmark

Confirmed/strong leads:

- No large commercial campus confirmed from the reviewed source set.
- Use Nkom operator names with possible northern operations as seeds, but require municipality/NVE/Statsforvalteren confirmation.
- Grid constraints north of Svartisen make capacity/date validation especially important.

Search:

```text
site:tromso.kommune.no datasenter
site:harstad.kommune.no datasenter
site:alta.kommune.no datasenter
site:hammerfest.kommune.no datasenter
site:sor-varanger.kommune.no datasenter
site:nve.no Troms datasenter
site:nve.no Finnmark datasenter
```

## 5. Workflow

1. Pull Nkom CSV and normalize legal names, org numbers, and crypto-mining flags.
2. Join obvious operator names to official operator pages.
3. For each named site, assign repo division and current county using the mapping in `explorer-official.md`.
4. Search municipal planning/building portals for permit/case IDs.
5. Search Statsforvalteren/Miljodirektoratet/Norske utslipp for pollution permits and hearings.
6. Search NVE/Statnett and local grid-company pages for substations, connection capacity, and restrictions.
7. Assign grade per field, not per facility. A facility can be Grade A for existence and Grade C for a marketed future capacity number.
8. Keep negative results for Svalbard, Jan Mayen, Troms/Finnmark, and quiet counties so coverage is auditable.

Facility confidence rule: mark a facility real when at least two independent signals agree, one of which should be Grade A when available. For newly regulated commercial operators, Nkom plus an operator page may be enough for existence, but status, address, and MW still need separate source grades.
