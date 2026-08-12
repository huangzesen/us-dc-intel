# IS Explorer Official - Iceland Datacenter Enumeration

Date: 2026-08-12. Scope: Iceland (IS). Division model: **region**; repo divisions (8): Capital Region; Southern Peninsula; West; Westfjords; Northwest; Northeast; East; South.

Purpose: enumerate Icelandic datacenter projects from official and primary sources: planning/EIA records, municipal permits, grid and power announcements, company registers, public procurement, telecom/regulator pages, operator facility pages, and cable/IXP operator pages. Use `explorer-industry.md` to discover names, then confirm here before treating a site as present.

## 0. Iceland-specific structure facts

### 0.1 Administrative division model

Iceland has national government and municipalities as the operative planning/building authorities. The 8 regions are statistical/regional groupings used by Statistics Iceland and common official reporting, not provinces with separate datacenter permitting authority. Municipality counts change through mergers; Statistics Iceland's municipality/region tables are the refresh source: https://www.statice.is/statistics/population/inhabitants/municipalities-and-urban-nuclei/

Use the repo division names exactly:

| Repo division | Icelandic name | Key municipalities / localities to search |
|---|---|---|
| Capital Region | Höfuðborgarsvæðið | Reykjavík, Kópavogur, Hafnarfjörður, Garðabær, Mosfellsbær, Seltjarnarnes, Kjósarhreppur |
| Southern Peninsula | Suðurnes | Reykjanesbær, Keflavík, Njarðvík, Ásbrú, Grindavíkurbær, Suðurnesjabær, Vogar |
| West | Vesturland | Akranes, Borgarbyggð, Hvalfjarðarsveit, Snæfellsbær, Stykkishólmur, Grundarfjarðarbær, Dalabyggð, Skorradalshreppur |
| Westfjords | Vestfirðir | Ísafjarðarbær, Vesturbyggð, Strandabyggð, Súðavíkurhreppur, Bolungarvík, Reykhólahreppur, Kaldrananeshreppur, Árneshreppur |
| Northwest | Norðurland vestra | Húnabyggð, Blönduós, Húnaþing vestra, Skagafjörður, Skagabyggð, Skagaströnd |
| Northeast | Norðurland eystra | Akureyri, Norðurþing, Fjallabyggð, Dalvíkurbyggð, Eyjafjarðarsveit, Þingeyjarsveit, Langanesbyggð, Svalbarðsstrandarhreppur |
| East | Austurland | Múlaþing, Seyðisfjörður, Egilsstaðir, Fjarðabyggð, Vopnafjarðarhreppur |
| South | Suðurland | Árborg/Selfoss, Ölfus, Hveragerði, Rangárþing ytra, Rangárþing eystra, Vestmannaeyjabær, Mýrdalshreppur, Skaftárhreppur, Sveitarfélagið Hornafjörður, Flóahreppur |

### 0.2 National registries and absence of a DC register

- **Fyrirtækjaskrá / company registry**: https://www.skatturinn.is/fyrirtaekjaskra/ . Use for legal entity names, kennitala, registered office, and activity codes. Grade A for registry facts. The registry does not by itself prove a datacenter facility location.
- **No national datacenter register found**. Fjarskiptastofa regulates electronic communications networks/services, but Iceland does not appear to maintain a datacenter-specific registration list comparable to Norway's Nkom datacenter register. Treat this as an absence, not a negative proof: census work must combine planning, grid/power, operator, and local-government evidence.
- **Statistics/energy context**: Statistics Iceland (https://www.statice.is/) and Orkustofnun (https://os.is/) are context sources, not facility lists.

### 0.3 Legal/regulatory basis

- **Electronic communications**: Act No. 70/2022, current consolidated law at https://www.althingi.is/lagas/nuna/2022070.html . Older Act No. 81/2003 is repealed under Act No. 70/2022, art. 109: https://www.althingi.is/altext/lagasofn/nuna/2003081.html . Regulator: Fjarskiptastofa/ECOI, https://www.fjarskiptastofa.is/ . A datacenter operator is not automatically an electronic communications provider unless it operates public communications networks/services.
- **Fjarskiptastofa statute**: Act No. 75/2021, https://www.althingi.is/lagas/nuna/2021075.html .
- **Electricity**: Act No. 65/2003, https://www.althingi.is/lagas/nuna/2003065.html . Main official energy actors for DC discovery are Landsvirkjun (power seller, https://www.landsvirkjun.com/ and https://www.landsvirkjun.is/), Landsnet (TSO, https://www.landsnet.is/), Orkustofnun (https://os.is/), and distribution utilities.
- **Planning**: Act No. 123/2010, https://www.althingi.is/lagas/nuna/2010123.html . Municipalities process local plans and construction permits; HMS/Skipulagsstofnun provides national oversight and portals.
- **Environmental assessment**: Act No. 111/2021, current consolidated law at https://www.althingi.is/lagas/nuna/2021111.html . HMS has the current environmental-assessment service page: https://island.is/en/o/hms/environmental-impact-assessment-of-projects .
- **Data protection**: Act No. 90/2018, https://www.althingi.is/lagas/nuna/2018090.html ; authority Persónuvernd, https://www.personuvernd.is/ .
- **Public procurement**: Act No. 120/2016, https://www.althingi.is/lagas/nuna/2016120.html . From 2024-08-01, Fjársýslan / Financial Management Authority assumed Ríkiskaup's central procurement tasks: https://island.is/en/o/central-public-procurement/about-rikiskaup . Tender publicity portal: https://island.is/en/tender-website and https://utbodsvefur.is/ .

## 1. Search vocabulary

Use Icelandic and English terms. Icelandic accents matter; also run accent-free variants where practical.

```text
gagnaver
gagnaversrekstur
gagnavarsla
netþjónastofa / netthjonastofa
netþjónn / netthjonn
vefhýsing / vefhysing
vistun
skýþjónusta / skyþjonusta / sky thjonusta
gagnaský / gagnasky
stafræn innviði / stafraen innvidi
sæstrengur / saestrengur / sjávarstrengur
ljósleiðari / ljosleidari
raforkufrekur iðnaður / raforkufrekar iðnaður
forgangsorka
raforkusamningur
tenging við flutningskerfi
framkvæmdaleyfi
byggingarleyfi
matsskylda / ákvörðun um matsskyldu
umhverfismat framkvæmda
skipulagsbreyting / deiliskipulag / aðalskipulag
iðnaðarsvæði
útboð / innkaup
dulmálamynt / rafmyntagröftur / grafarvinnsla
```

English: data center, data centre, colocation, colo, HPC, AI infrastructure, server farm, hosting, cloud, submarine cable, cable landing station, internet exchange, grid connection, power purchase agreement, firm power.

## 2. Official/regulatory pipeline

### 2.1 Planning and EIA

- **Skipulagsgátt**: https://skipulagsgatt.is/ . This is the national consultation portal for planning matters, environmental assessment, and construction/execution permits. The portal is JavaScript-heavy; use web search snippets plus direct portal search in a browser when needed. The page itself states it is a consultation portal for planning, EIA, and execution permits. Grade A for case metadata/documents retrieved from it.
- **HMS/island.is environmental-assessment database**: search `site:island.is/s/hms/gagnagrunnur-umhverfismats gagnaver`. Example verified case: "Nýtt gagnaver Verne við Valhallarbraut, Reykjanesbæ" decision/screening page, 2026-06-02: https://island.is/s/hms/gagnagrunnur-umhverfismats/nytt-gagnaver-verne-vid-valhallarbraut-reykjanesbae-2-6-2026 . Grade A for the screened project's existence/status.
- **Skipulagsstofnun/HMS**: https://www.skipulag.is/ and HMS planning pages at https://hms.is/ . Use when old cases predate Skipulagsgátt or are mirrored in legacy Skipulagsstofnun pages.
- **Municipality sites**: needed for building permits, minutes, land allocations, local plans, and consultation notices. Example official local evidence: Húnabyggð/Blönduós 2021 Borealis expansion notice, https://www.hunabyggd.is/is/mannlif/frettir-og-vidburdir/frettir-og-auglysingar/tilkynningar-og-frettir/framkvaemdir-hafnar-vid-staekkun-gagnavers-etix-everywhere-borealis-a-blonduosi .

### 2.2 Energy/grid

- **Landsvirkjun**: primary power-sales source. Its Icelandic datacenter page says it has datacenter customers and identifies Verne Global, atNorth (formerly Advania Data Centers), and Borealis as datacenter customers: https://www.landsvirkjun.is/gagnaver . Recent primary PPA examples:
  - Borealis Blönduós additional 12 MW firm power, 2026-06-23: https://www.landsvirkjun.com/news/borealis-and-landsvirkjun-sign-a-12-mw-power-purchasing-agreement .
  - atNorth Akureyri up to 12 MW green firm power, 2025-09: https://www.landsvirkjun.com/news/landsvirkjun-and-atnorth-akureyri-sign-new-green-firm-ppa .
- **Landsnet**: TSO and grid-connection lead source, https://www.landsnet.is/ . Verne and Landsnet announced a Keflavík high-capacity substation in 2026 via Verne's source page: https://www.verne.co/news/news-verne-and-landsnet-launch-high-capacity-substation . Prefer Landsnet documents if a matching Landsnet page is found; otherwise grade the operator announcement A for operator fact and B for TSO-side fact unless Landsnet co-publication is confirmed.
- **Orkustofnun**: https://os.is/ . Use for energy statistics/licensing context, not as a DC permit register.
- **Distribution utilities**: Veitur, RARIK, HS Orka, ON and local utilities can reveal smaller colo or municipal hosting sites. Grade A only when the utility document states the specific facility/client/project.

### 2.3 Telecom, IXP, and cables

- **Fjarskiptastofa/ECOI**: https://www.fjarskiptastofa.is/ . Relevant for communications networks/services, not a facility census.
- **RIX**: https://www.rix.is/en/ . RIX states POPs at Tæknigarður/Dunhagi 5, ISNIC HQ/Katrínartún 2, and Múlastöð/Ármúla 25 in Reykjavík. PeeringDB RIX record: https://www.peeringdb.com/ix/228 . Grade A for RIX's own location statements; PeeringDB is self-reported (C/B depending on owner-maintained evidence).
- **Múli IXP**: Internet Society Pulse/PeeringDB list Múli IXP as an active Reykjavik IXP with small membership: https://pulse.internetsociety.org/en/ixp-tracker/country/IS/ . Treat as C until confirmed by an operator-owned page.
- **Farice**: https://farice.is/network/ . Farice is primary for FARICE-1, DANICE, and IRIS and states its network serves international data center customers. Use Farice for cable facts; cable landing stations are connectivity infrastructure, not datacenters unless a colo/DC facility is separately evidenced.
- **Farice 2026 AUÐUR cable plan**: Farice announced preparations for a new southern Iceland-Scotland cable in 2026 on its English feed: https://farice.is/embed/ . Track as a connectivity trigger, not a DC project.

### 2.4 Investment promotion and policy

- U.S. International Trade Administration Iceland Data Centers guide, last published 2026-04-01: https://www.trade.gov/country-commercial-guides/iceland-data-centers . Grade B/A for government-market context; not a facility census.
- Invest in Iceland: https://invest.is/ ; Business Iceland: https://islandsstofa.is/ ; Data Centers by Iceland: https://www.datacentersbyiceland.com/ . Use as lead/promotion sources, not final proof of facility status.
- Digital Iceland: https://island.is/ and Stafrænt Ísland content under island.is. The old `stafraent.is` domain should not be relied on without checking redirect/status.

### 2.5 Hyperscaler official-region check

As of this review, no AWS, Azure, Google Cloud, or Oracle Cloud public cloud region in Iceland was found on official region pages. Re-check every review cycle:

```text
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
https://cloud.google.com/about/locations
https://www.oracle.com/cloud/public-cloud-regions/
```

## 3. Query templates

```text
# National planning / EIA
site:skipulagsgatt.is gagnaver
site:skipulagsgatt.is "gagnaver" "framkvæmdaleyfi"
site:skipulagsgatt.is "gagnaver" "matsskylda"
site:island.is/s/hms/gagnagrunnur-umhverfismats gagnaver
site:skipulag.is gagnaver
"Nýtt gagnaver" "ákvörðun um matsskyldu"

# Municipal planning / permits
site:reykjanesbaer.is gagnaver
site:akureyri.is gagnaver
site:hunabyggd.is gagnaver OR "Borealis"
site:reykjavik.is gagnaver OR "byggingarleyfi"
site:hafnarfjordur.is gagnaver OR "Steinhella"
site:{municipality-domain} "gagnaver" "deiliskipulag"
site:{municipality-domain} "gagnaver" "byggingarleyfi"

# Energy/grid
site:landsvirkjun.is gagnaver
site:landsvirkjun.com "data center" Iceland
site:landsvirkjun.com "MW" "data centre" "Iceland"
site:landsnet.is gagnaver
site:landsnet.is "data center" OR "data centre"
site:os.is gagnaver
"gagnaver" "forgangsorka"
"gagnaver" "raforkusamningur"

# Company/registry
site:skatturinn.is/fyrirtaekjaskra "Verne"
site:skatturinn.is/fyrirtaekjaskra "atNorth"
site:skatturinn.is/fyrirtaekjaskra "Borealis Data Center"
"{operator legal name}" kennitala

# Procurement and government cloud
site:utbodsvefur.is gagnaver OR "skýþjónusta" OR "vistun"
site:island.is/en/tender-website data center OR cloud OR hosting
site:ted.europa.eu Iceland "data center" OR "cloud" OR "hosting"

# Telecom/cable
site:fjarskiptastofa.is gagnaver OR "data center"
site:rix.is "RIX" "Reykjavík"
site:farice.is "data center" OR "landing" OR IRIS OR DANICE OR FARICE-1
```

## 4. Per-division enumeration approach

Expectation scale: **hub** (multiple commercial DCs) > **light** (1-2 known commercial/telecom DCs) > **none/watch** (no confirmed commercial DC; document negative sweeps and monitor triggers).

| Division | Current expectation | Official enumeration approach |
|---|---|---|
| Capital Region | Light | Confirm atNorth ICE01 in Hafnarfjörður via atNorth + Landsvirkjun lineage; Borealis Reykjavík via Borealis acquisition/site pages; telecom/IXP rooms through RIX, Míla/Síminn, Sýn/Vodafone, Nova, and municipal permits. Search Reykjavík, Hafnarfjörður, Kópavogur, Garðabær. |
| Southern Peninsula | HUB | Core targets: Verne Keflavík/Ásbrú, atNorth ICE02 Keflavík, Borealis Fitjar. Use Reykjanesbær planning, HMS EIA database, Landsvirkjun/Landsnet, and operator pages. Monitor Verne 2026 120 MW expansion study and Valhallarbraut EIA screening. |
| West | None/watch | No verified commercial DC this pass. Search Akranes, Borgarbyggð, Hvalfjarðarsveit, Skorradalur plus Landsvirkjun/grid news. Promote only on planning, PPA, or operator evidence. |
| Westfjords | None/watch | No verified commercial DC this pass. Grid remoteness lowers expectation. Search Ísafjarðarbær and Westfjords regional portals annually unless a cable/grid/project trigger appears. |
| Northwest | Light | Borealis Blönduós is confirmed. Search Húnabyggð/Blönduós planning, Landsvirkjun PPAs, Borealis site pages, and local press. |
| Northeast | Light | atNorth ICE03 Akureyri is confirmed; Opin Kerfi/telecom rooms are leads unless primary facility evidence is found. Search Akureyri planning, Landsvirkjun atNorth PPA, atNorth pages, and local Akureyri media. |
| East | None/watch | FARICE-1 landing at Seyðisfjörður is connectivity only. Search Múlaþing/Fjarðabyggð planning and Farice cable news; do not count cable landing stations as DCs. |
| South | None/watch | DANICE/Greenland Connect and IRIS/AUÐUR southern landing context is connectivity only. Search Rangárþing ytra, Ölfus, Árborg, Hveragerði, and Farice. Do not count landing stations without separate colo/DC evidence. |

Division coverage is complete when each of the eight repo divisions has either a confirmed facility table entry or a dated negative/watch note with the searched municipalities and triggers.

## 5. Reliability grades

- **A** - primary/official source proving the specific fact: Skipulagsgátt/HMS/Skipulagsstofnun case document, municipal permit/minutes, Landsvirkjun/Landsnet/Orkustofnun document, Fyrirtækjaskrá record, Althingi law text, operator-owned facility page, RIX/Farice page for their own assets.
- **B** - reliable secondary/trade source with named operator, place, date, and status: DCD, Data Center Knowledge, Capacity, RÚV, Vísir, mbl, Viðskiptablaðið, Iceland Review, BusinessWire/PRNewswire for corporate announcements, trade.gov for government-market context.
- **C** - aggregator/weak/self-reported source: DataCenterMap, Baxtel, Ocolo, DataCenters.com, DataCenterHawk, Cloudscene-style counts, Wikipedia, LinkedIn/social posts, market-report teasers, PeeringDB when not corroborated by the listed operator.
- **U** - do not use in final facility rows. If a fact is unverified, omit it or label it as a lead in the industry file only.

A grade covers only the fact attached to it. Example: atNorth's own page can grade ICE02 existence/location as A; a third-party Tier claim remains C unless confirmed by atNorth or Uptime Institute.

## 6. Confirmed facilities/projects and official evidence

| Facility / project | Division | Status | Evidence / grade |
|---|---|---|---|
| Verne Iceland / Keflavík campus, Ásbrú/Valhallarbraut, Reykjanesbær | Southern Peninsula | Operational; active expansion pipeline | A: operator facility page states Iceland campus, 100% renewable power, over 140 MW campus capacity, connectivity: https://www.verne.co/iceland . A: Verne 2026 substation/expansion facts on operator page, including 240 MW installed-capacity substation and 120 MW proposed extension: https://www.verne.co/news/news-verne-and-landsnet-launch-high-capacity-substation and https://www.verne.co/news/news-verne-to-host-supplier-information-day-for-major-keflavik-campus-expansion . A: HMS EIA database case "Nýtt gagnaver Verne við Valhallarbraut, Reykjanesbæ", 2026-06-02: https://island.is/s/hms/gagnagrunnur-umhverfismats/nytt-gagnaver-verne-vid-valhallarbraut-reykjanesbae-2-6-2026 . A: 2010 special act authorizing government agreements for Verne datacenter in Reykjanesbær: https://www.althingi.is/lagas/150a/2010057.html . |
| atNorth ICE02 Keflavík | Southern Peninsula | Operational; expansion underway/announced | A: atNorth Iceland page lists ICE02 Keflavík; ICE02 page describes Tier 3 campus near Keflavík airport on 9 ha: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/ and https://www.atnorth.com/nordic-data-centers/iceland-data-centers/keflavik-mega-site/ . B: Icelandic press/operator announcement for 2024 expansions at ICE02/ICE03: https://www.visir.is/g/20242646476d/staekka-gagnaverin-a-akureyri-og-i-reykjanesbae . |
| Borealis Fitjar Campus, Reykjanesbær | Southern Peninsula | Operational | A: Borealis site page lists location Reykjanesbær, built-out capacity 10 MW, ISO 27001: https://bdc.is/sites/fitjar-campus . |
| atNorth ICE01 Reykjavík metro site, Steinhella 10, Hafnarfjörður | Capital Region | Operational | A: atNorth ICE01 page states Reykjavík metro site and >2,700 sqm white technical space: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/reykjavik-metro-site/ . A: Landsvirkjun identifies atNorth as formerly Advania Data Centers and a datacenter customer: https://www.landsvirkjun.is/gagnaver . |
| Borealis Reykjavík Campus / Reykjavík DC | Capital Region | Operational | A: Borealis "Our sites" lists Reykjavík Campus: https://bdc.is/sites . A: Borealis acquisition notice says it acquired Reykjavik DC from Íslandsbanki and describes up to 7,000 sqm when fully developed: https://bdc.is/insights/borealis-acquires-reykjavik-data-center . |
| RIX POPs, Reykjavík | Capital Region | Network/IXP colocation, not a commercial DC campus | A: RIX states POPs at Tæknigarður, ISNIC HQ/Katrínartún 2, and Múlastöð/Ármúla 25: https://www.rix.is/en/ . C: PeeringDB RIX record lists three Reykjavík facilities and capacity: https://www.peeringdb.com/ix/228 . Count as interconnection infrastructure, not a separate datacenter unless facility-level colo is in scope. |
| Borealis Blönduós Campus | Northwest | Operational; expanding | A: Borealis site page states Blönduós campus, 100+ MW expansion capacity, ISO 27001: https://bdc.is/sites/bl%C3%B6ndu%C3%B3s-campus . A: Landsvirkjun 2026-06-23 PPA provides additional 12 MW firm power for growth in Blönduós: https://www.landsvirkjun.com/news/borealis-and-landsvirkjun-sign-a-12-mw-power-purchasing-agreement . A/B: Húnabyggð local notice documented 2021 expansion construction: https://www.hunabyggd.is/is/mannlif/frettir-og-vidburdir/frettir-og-auglysingar/tilkynningar-og-frettir/framkvaemdir-hafnar-vid-staekkun-gagnavers-etix-everywhere-borealis-a-blonduosi . |
| atNorth ICE03 Akureyri | Northeast | Operational; expanding | A: atNorth ICE03 page states Tier 3 campus in Akureyri on 4.3 ha: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/akureyri-mega-site/ . A: Landsvirkjun 2025 PPA supplies up to 12 MW to the Akureyri datacenter: https://www.landsvirkjun.com/news/landsvirkjun-and-atnorth-akureyri-sign-new-green-firm-ppa . B/A local: Akureyri.net reported official opening of first phase at Hlíðarvellir in June 2023: https://www.akureyri.net/is/frettir/nytt-gagnaver-atnorth-vigt-a-akureyri . |
| FARICE-1 landing, Seyðisfjörður | East | Cable landing station; not counted as DC | A: Farice network page for FARICE-1/DANICE/IRIS: https://farice.is/network/ . Use as connectivity context only. |
| DANICE / Greenland Connect / IRIS / planned AUÐUR southern landing context | South | Cable landing/connectivity; not counted as DC | A: Farice network page: https://farice.is/network/ . A: Farice English feed for 2026 AUÐUR southern Iceland-Scotland cable plan: https://farice.is/embed/ . Verify exact landing-point details before assigning municipality. |

## 7. Negative/watch coverage by division

- **West**: No commercial datacenter confirmed from operator pages, Landsvirkjun customer pages, or broad planning/EIA searches in this review. Re-run Akranes, Borgarbyggð, Hvalfjarðarsveit, and Skipulagsgátt searches annually.
- **Westfjords**: No commercial datacenter confirmed. Treat as low probability unless a new cable, grid, or municipal industrial-plan trigger appears.
- **East**: No commercial datacenter confirmed. FARICE-1 at Seyðisfjörður is a cable landing station only.
- **South**: No commercial datacenter confirmed. Farice cable infrastructure and landing stations are connectivity only.

## 8. Update / re-check cadence

- **Monthly**: Skipulagsgátt/HMS searches for `gagnaver`; operator news pages for Verne, atNorth, Borealis; Landsvirkjun and Landsnet news; Icelandic press `gagnaver`.
- **Quarterly**: municipality sweeps for Reykjanesbær, Akureyri, Húnabyggð, Reykjavík, Hafnarfjörður; RIX/PeeringDB/Pulse IXP changes; Farice cable announcements.
- **Semi-annual**: hyperscaler official region pages; Uptime Institute/certification databases; company registry details for operators and project entities.
- **Annual**: full eight-division negative sweep, including West, Westfjords, East, and South, and reconciliation against `explorer-industry.md`.

Event triggers: EIA screening, building permit, PPA, grid-connection/substation document, cable RFS/new landing point, acquisition/brand change, or new operator facility page.
