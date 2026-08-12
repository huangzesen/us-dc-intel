# IS Explorer Industry - Iceland Datacenter Discovery

Date: 2026-08-12. Scope: Iceland (IS). Division model: **region**; repo divisions (8): Capital Region; Southern Peninsula; West; Westfjords; Northwest; Northeast; East; South.

Purpose: discover Icelandic datacenter candidates from operators, trade press, industry promotion, connectivity records, certification databases, and aggregators. Facility rows from this file are leads until confirmed against official/primary evidence in `explorer-official.md`.

## 0. Industry-side structure facts

- Iceland's commercial datacenter market is small and concentrated around three primary operators: Verne, atNorth, and Borealis Data Center. Official power/customer evidence from Landsvirkjun names Verne Global, atNorth (formerly Advania Data Centers), and Borealis as datacenter customers: https://www.landsvirkjun.is/gagnaver .
- Power availability is the gating issue. Trade and Icelandic press reported reduced electricity sales to datacenters/crypto mining in 2024, while Landsvirkjun's 2026 PPA pages show targeted firm-power additions where the grid can support them.
- Connectivity is a major sales argument. Farice operates the international cable network used by datacenter customers; RIX and Múli IXP provide domestic exchange/peering context in Reykjavík.
- No AWS, Azure, Google Cloud, or Oracle Cloud public cloud region in Iceland was found on official region pages in this review. Re-check via the official URLs in `explorer-official.md`.
- Aggregator counts vary and are not reliable census counts. Treat DataCenterMap, Baxtel, Ocolo, DataCenters.com, Cloudscene-style country counts, and market-report teasers as lead sources only.

## 1. Industry search vocabulary

Use the Icelandic and English vocabulary in `explorer-official.md`, plus:

```text
colo / colocation
HPC / high performance computing
AI infrastructure / gervigreind
OCP Ready
Tier III / EN 50600 / ISO 27001
PUE
liquid cooling / vökvakæling
bitcoin mining / crypto mining / rafmyntagröftur
Verne / Verne Global
atNorth / Advania Data Centers
Borealis Data Center / Etix Everywhere Borealis
Fitjar / Blönduós / Hlíðarvellir / Steinhella / Ásbrú / Valhallarbraut
RIX / Múli IXP
Farice / FARICE-1 / DANICE / IRIS / AUÐUR / Far North Fiber
```

## 2. Reliability grades

- **A** - operator-owned/primary source for the specific fact: operator facility page, operator press release, RIX/Farice official page, Landsvirkjun/Landsnet page, municipal page, or company registry.
- **B** - reliable secondary or trade source with named operator/place/date/status: DCD, Data Center Knowledge, Capacity, RÚV, Vísir, mbl, Viðskiptablaðið, Iceland Review, BusinessWire/PRNewswire, trade.gov.
- **C** - aggregator/weak/self-reported: DataCenterMap, Baxtel, Ocolo, DataCenters.com, DataCenterHawk, market-report teasers, Wikipedia, LinkedIn/social posts, PeeringDB/Pulse for facts not independently confirmed by the asset owner.
- **Lead only** - a weak or ambiguous item that should not be added to the official facility table until confirmed.

Grades attach only to the fact stated. Example: Borealis can be A for site existence and ISO 27001 on its own page; a capacity value from an aggregator remains C unless also shown by Borealis or a power/grid source.

## 3. Operator/source backbone

### 3.1 Commercial datacenter operators

- **Verne**: https://www.verne.co/ ; Iceland campus: https://www.verne.co/iceland ; news: https://www.verne.co/news . A for Verne facility/capacity/connectivity/expansion statements. Key 2026 items: high-capacity substation with Landsnet, https://www.verne.co/news/news-verne-and-landsnet-launch-high-capacity-substation ; supplier day for potential 120 MW Keflavík extension, https://www.verne.co/news/news-verne-to-host-supplier-information-day-for-major-keflavik-campus-expansion . Verne media center says Verne is backed by Ardian since 2024: https://www.verne.co/media-center .
- **atNorth**: https://www.atnorth.com/ ; Iceland overview: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/ . Facility pages:
  - ICE01 Reykjavík metro/Hafnarfjörður: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/reykjavik-metro-site/
  - ICE02 Keflavík: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/keflavik-mega-site/
  - ICE03 Akureyri: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/akureyri-mega-site/
  A for operator facility facts. Landsvirkjun atNorth Akureyri PPA is primary power evidence: https://www.landsvirkjun.com/news/landsvirkjun-and-atnorth-akureyri-sign-new-green-firm-ppa .
- **Borealis Data Center**: https://bdc.is/ ; sites: https://bdc.is/sites . Facility pages:
  - Blönduós Campus: https://bdc.is/sites/bl%C3%B6ndu%C3%B3s-campus
  - Fitjar Campus: https://bdc.is/sites/fitjar-campus
  - Reykjavík Campus is listed from the sites page; acquisition of Reykjavik DC: https://bdc.is/insights/borealis-acquires-reykjavik-data-center
  A for Borealis facility facts. Landsvirkjun Borealis 12 MW Blönduós PPA is primary: https://www.landsvirkjun.com/news/borealis-and-landsvirkjun-sign-a-12-mw-power-purchasing-agreement . Borealis financing page confirms three Iceland campuses plus Kajaani, Finland, and $148m financing: https://bdc.is/insights/borealis-data-center-secures-c-135-million-usd-term-loan-and-13-million-usd-revolving-facilities-to-fund-ambitious-expansion-in-iceland-and-finland .

### 3.2 Telecom, hosting, and smaller colocations

- **RIX / Internet á Íslandi hf.**: https://www.rix.is/en/ ; connected members: https://www.rix.is/en/connected ; PeeringDB: https://www.peeringdb.com/ix/228 . RIX POPs are in Reykjavík; count as interconnection/colo rooms, not commercial datacenter campuses unless the facility itself is in scope.
- **Múli IXP**: Internet Society Pulse lists Múli IXP in Reykjavík with one physical location and small member count: https://pulse.internetsociety.org/en/ixp-tracker/country/IS/ . Use as a lead until an operator-owned page is found.
- **Síminn/Míla, Sýn/Vodafone, Nova, Sensa/Origo, Opin Kerfi, smaller hosting firms**: use as leads for telecom/server rooms and managed hosting. Do not count as standalone commercial datacenters without a primary facility page, permit/minutes, RIX/PeeringDB facility record, or operator document.
- **Advania**: relevant historically because Landsvirkjun identifies atNorth as formerly Advania Data Centers. Do not infer current Advania-owned datacenter campuses without current primary evidence.

### 3.3 Connectivity sources

- **Farice**: network page, https://farice.is/network/ . A for Farice's own cable/network facts and for the statement that its network serves international datacenter customers.
- **Farice English feed**: https://farice.is/embed/ . A for Farice 2026 AUÐUR cable plan between southern Iceland and Scotland.
- **Far North Fiber**: https://www.farnorthfiber.com/ . Use for Arctic cable project status. Farice's older press-feed item covers Japan-Iceland connectivity through IRIS/Far North Fiber: https://farice.is/category/press-releases/ . Cable projects are triggers for future DC interest, not facility evidence.

### 3.4 Trade press and local press

Use these for leads, dates, ownership changes, financing, customer deployments, and local reaction:

```text
site:datacenterdynamics.com Iceland data center
site:datacenterknowledge.com Iceland data center
site:capacitymedia.com Iceland data center
site:thetechcapital.com Iceland data center
site:ruv.is gagnaver
site:visir.is gagnaver
site:mbl.is gagnaver
site:vb.is gagnaver
site:akureyri.net gagnaver atNorth
site:icelandreview.com data center Iceland
site:grapevine.is "data center" Iceland
```

Verified useful examples:

- Vísir 2024 atNorth ICE02/ICE03 expansion report: https://www.visir.is/g/20242646476d/staekka-gagnaverin-a-akureyri-og-i-reykjanesbae .
- Akureyri.net 2023 opening of atNorth first phase at Hlíðarvellir: https://www.akureyri.net/is/frettir/nytt-gagnaver-atnorth-vigt-a-akureyri .
- Vísir tag page documents 2024 electricity/crypto-mining contraction context: https://www.visir.is/t/3950 .
- Nordic Labour Journal interview says Landsvirkjun decided in 2022 not to make or renew crypto-mining deals: https://www.nordiclabourjournal.org/iceland-ditches-crypto-mining-for-ai-a-great-opportunity-for-nordic-data-centres/ . Grade B for interview/context; prefer Landsvirkjun primary when available.

### 3.5 Aggregators and databases

Use only to discover names/addresses to confirm elsewhere:

```text
https://www.datacentermap.com/iceland/
https://baxtel.com/data-center/iceland
https://www.ocolo.io/data-centers/iceland/
https://www.datacenters.com/locations/iceland
https://www.arizton.com/market-reports/iceland-data-center-market
https://www.peeringdb.com/advanced_search?country=IS
https://pulse.internetsociety.org/en/ixp-tracker/country/IS/
```

Aggregator rows for old crypto sites, small hosting rooms, or telecom rooms are not enough to add a confirmed facility.

### 3.6 Certifications

- Borealis pages state ISO 27001 for Blönduós and Fitjar; Borealis also states Blönduós data halls B5.2 and B6.2 were OCP Ready: https://bdc.is/insights/borealis-data-center-becomes-the-first-ocp-ready-facility-in-iceland .
- Verne states EN 50600 certification for one Iceland data hall: https://www.verne.co/blog/blog-verne-achieves-en-50600-certification-in-iceland-for-reliability-and-resilience .
- atNorth facility pages state Tier 3 for ICE01/ICE02/ICE03. Treat this as A for atNorth's own Tier 3 marketing claim, not as Uptime Institute certification unless verified in Uptime's certification database.
- Re-check Uptime Institute certification search separately before stating "Uptime Tier Certified."

## 4. Query templates

```text
# Operators
site:verne.co Iceland Keflavik data center
site:verne.co "Valhallarbraut" OR "Ásbrú" OR "Landsnet"
site:atnorth.com ICE01 OR ICE02 OR ICE03
site:atnorth.com Akureyri Keflavik Reykjavik "data center"
site:bdc.is Blönduós OR Blonduos OR Fitjar OR Reykjavík
site:bdc.is "Landsvirkjun" OR "12 MW" OR "OCP Ready"

# Ownership / financing / acquisitions
"Verne" "Ardian" "Iceland"
"atNorth" "CPP Investments" "Equinix" acquisition
"Borealis Data Center" Vauban Infranity Arion
"Borealis Data Center" "Reykjavik DC" "Íslandsbanki"

# Telecom / IXP / hosting
site:rix.is Reykjavík "POP" OR "connected"
site:peeringdb.com "Iceland" "Reykjavik" facility
"Múli IXP" OR "Muli IXP"
site:mila.is gagnaver OR hýsing OR colocation
site:siminn.is gagnaver OR hýsing
site:syn.is gagnaver OR hýsing
site:nova.is gagnaver OR hýsing
site:opinkerfi.is gagnaver OR Akureyri

# Trade/local press
site:ruv.is gagnaver
site:visir.is gagnaver
site:mbl.is gagnaver
site:vb.is gagnaver
site:akureyri.net gagnaver atNorth
site:datacenterdynamics.com Iceland Borealis OR Verne OR atNorth

# Cable/connectivity
site:farice.is network IRIS DANICE FARICE-1 AUÐUR
site:farnorthfiber.com Iceland
site:submarinenetworks.com Iceland cable data center

# Aggregator leads
site:datacentermap.com/iceland Verne OR Borealis OR atNorth
site:baxtel.com Iceland "data center"
site:ocolo.io Iceland "data center"
```

## 5. Per-division industry approach

| Division | Expected activity | Industry discovery approach |
|---|---|---|
| Capital Region | Light | atNorth ICE01, Borealis Reykjavík, RIX POPs, telecom/hosting rooms. Confirm with operator pages and RIX; avoid counting normal hosting/CDN resellers as physical DCs. |
| Southern Peninsula | HUB | Verne Keflavík, atNorth ICE02, Borealis Fitjar, and related Reykjanesbær/Ásbrú expansion news. Monitor Verne, atNorth, Borealis, Landsvirkjun, Landsnet, Reykjanesbær, and cable landing/connectivity announcements. |
| West | None/watch | Search aggregators and press for Akranes/Borgarbyggð/Hvalfjörður leads. No confirmed commercial DC this review. |
| Westfjords | None/watch | Search annual negative sweep only unless a grid/cable trigger appears. No confirmed commercial DC this review. |
| Northwest | Light | Borealis Blönduós is the key site. Track Borealis, Landsvirkjun, Húnabyggð, local press, OCP/ISO/capacity updates. |
| Northeast | Light | atNorth ICE03 Akureyri is the key site. Search atNorth, Landsvirkjun, Akureyri municipality/local press, and Opin Kerfi leads. |
| East | None/watch | FARICE-1/Seyðisfjörður is cable infrastructure only. Search Múlaþing/Fjarðabyggð press and Farice; do not count cable stations as DCs. |
| South | None/watch | DANICE/Greenland Connect/IRIS/AUÐUR landing context is cable infrastructure only. Search Farice, Ölfus, Árborg, Hveragerði, Rangárþing ytra. |

## 6. Confirmed industry facility/source table

| Facility / project | Division | Industry evidence |
|---|---|---|
| Verne Iceland / Keflavík campus | Southern Peninsula | A: Verne Iceland page, https://www.verne.co/iceland . A: 2026 high-capacity substation with Landsnet, https://www.verne.co/news/news-verne-and-landsnet-launch-high-capacity-substation . A: 2026 potential 120 MW extension supplier day, https://www.verne.co/news/news-verne-to-host-supplier-information-day-for-major-keflavik-campus-expansion . A: Verne media center says backed by Ardian since 2024, https://www.verne.co/media-center . |
| atNorth ICE01 Reykjavík metro / Hafnarfjörður | Capital Region | A: atNorth Iceland overview and ICE01 page: https://www.atnorth.com/nordic-data-centers/iceland-data-centers/ and https://www.atnorth.com/nordic-data-centers/iceland-data-centers/reykjavik-metro-site/ . |
| atNorth ICE02 Keflavík | Southern Peninsula | A: atNorth ICE02 page, https://www.atnorth.com/nordic-data-centers/iceland-data-centers/keflavik-mega-site/ . B: Vísir 2024 expansion report, https://www.visir.is/g/20242646476d/staekka-gagnaverin-a-akureyri-og-i-reykjanesbae . |
| atNorth ICE03 Akureyri | Northeast | A: atNorth ICE03 page, https://www.atnorth.com/nordic-data-centers/iceland-data-centers/akureyri-mega-site/ . A: Landsvirkjun PPA, https://www.landsvirkjun.com/news/landsvirkjun-and-atnorth-akureyri-sign-new-green-firm-ppa . B: Akureyri.net opening report, https://www.akureyri.net/is/frettir/nytt-gagnaver-atnorth-vigt-a-akureyri . |
| Borealis Blönduós Campus | Northwest | A: Borealis site page, https://bdc.is/sites/bl%C3%B6ndu%C3%B3s-campus . A: Landsvirkjun 12 MW PPA, https://www.landsvirkjun.com/news/borealis-and-landsvirkjun-sign-a-12-mw-power-purchasing-agreement . A: Borealis OCP Ready statement for data halls B5.2/B6.2, https://bdc.is/insights/borealis-data-center-becomes-the-first-ocp-ready-facility-in-iceland . |
| Borealis Fitjar Campus | Southern Peninsula | A: Borealis site page, https://bdc.is/sites/fitjar-campus . |
| Borealis Reykjavík Campus / Reykjavik DC | Capital Region | A: Borealis sites page lists Reykjavík Campus, https://bdc.is/sites . A: Borealis acquisition of Reykjavik DC, https://bdc.is/insights/borealis-acquires-reykjavik-data-center . |
| RIX POPs | Capital Region | A: RIX operator page, https://www.rix.is/en/ . C: PeeringDB RIX record, https://www.peeringdb.com/ix/228 . Interconnection infrastructure only unless the local facility is being counted as a colo room. |
| Múli IXP | Capital Region | C: Internet Society Pulse lists Múli IXP as active in Reykjavík, https://pulse.internetsociety.org/en/ixp-tracker/country/IS/ . Lead only pending operator-owned confirmation. |
| Farice cable network: FARICE-1, DANICE, IRIS | East / South / national connectivity | A: Farice network page, https://farice.is/network/ . Connectivity only, not DC facility evidence. |
| Farice AUÐUR planned Iceland-Scotland cable | South / national connectivity | A: Farice English feed, https://farice.is/embed/ . Monitor as a future connectivity trigger. |
| Far North Fiber Japan-Europe Arctic system | n/a | A/B: Far North Fiber project page, https://www.farnorthfiber.com/ ; Farice press-feed item, https://farice.is/category/press-releases/ . Connectivity trigger only. |

## 7. Leads requiring caution

- **Advania current facilities**: historically relevant to atNorth lineage; Landsvirkjun states atNorth was formerly Advania Data Centers. Do not list current Advania-owned DCs without current primary facility evidence.
- **Opin Kerfi Akureyri**: remains a lead for managed IT/hosting near Akureyri. Confirm via operator facility page, municipal permit, or other primary source before adding.
- **Telecom rooms (Síminn/Míla, Sýn/Vodafone, Nova)**: likely present for network operations, but facility addresses/capacity need primary evidence before adding as datacenters.
- **Legacy crypto-mining sites**: treat as historical/lead only. Current state must be proven by operator, permit, power contract, or local reporting.
- **Aggregator-only "Iceland datacenter" rows**: do not import directly. Many duplicate operator rooms, old names, or hosting/CDN resellers.

## 8. Update / re-check cadence

- **Monthly**: Verne, atNorth, Borealis news; Landsvirkjun/Landsnet announcements; Icelandic press searches for `gagnaver`; HMS/Skipulagsgátt searches for new EIA/planning cases.
- **Quarterly**: PeeringDB/Pulse country=IS IXPs/facilities; RIX members/locations; Farice cable announcements; aggregator diff for new names only.
- **Semi-annual**: Uptime Institute and certification checks; ownership/acquisition status for Verne, atNorth, Borealis; telecom/hosting operator pages.
- **Annual**: full eight-division sweep, with explicit negative searches for West, Westfjords, East, and South; reconcile against `explorer-official.md`.
