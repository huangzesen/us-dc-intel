# Tracker / Commercial Source Research Summary

Scope: Tracker commercial/free data sources for US data center super-list expansion. I only wrote `source-research-trackers.jsonl` and this summary.

## Curl tests performed

- Cleanview `https://www.cleanview.co/data-centers/us`: HTTP 200, 719080 bytes.
- Baxtel corrected URL `https://baxtel.com/data-center/united-states`: HTTP 200, 286414 bytes. Initial guessed `/data-centers/united-states` returned 404.
- datacenterHawk home: HTTP 200, 520270 bytes, but only marketing/aggregate data.
- Data Center Map home, `/usa/`, and Dallas city page: HTTP 429 to plain curl.
- DC Byte home and Search Data Centers page: HTTP 200, but product/login/trial page only.
- JLL North America report: HTTP 200; CBRE report pages returned HTTP 403 to plain curl.
- FracTracker tracker/article, dcmap.us, trackdatacenters.com, and a Cloudscene facility page: HTTP 200. dcmap.us `/api/map` returned HTTP 403.

## Best direct sources

1. **Cleanview**: highest-value public tracker for planned projects. The US page exposes project-level URLs, top operating/planned cards, capacity, status, expected year, developer/location, and totals: 3,049 total, 1,214 operating, 1,788 planned, 369,928 MW planned. Next step is to inspect Next chunks/state pages for a complete list API.
2. **Baxtel**: strong for broad facility coverage and operating/under-construction validation. Country page reports 5,115 US facilities and embeds stage/year MW chart data. Needs sitemap/search crawling to enumerate all facility pages.
3. **FracTracker National Data Centers Tracker**: strong open-access proposal/AI buildout source. Article states facility-level dataset is downloadable/non-commercial and includes address, coordinates, operator/tenant, MW, square footage, acreage, power sourcing, cooling, and status.
4. **dcmap.us**: promising free map with 4,800 tracked facilities, 317 GW tracked, operational/construction/planned counts, and state/market pages. API returned 403 to curl, so use browser/session workflow or crawl static state/market pages first.

## Partial / supplemental sources

- **Data Center Map**: valuable free directory, but plain curl got 429. Use only with browser-like rate limiting, search-cache seeding, or manual endpoint discovery.
- **Cloudscene**: useful operating colocation facility validation for address, operator, carriers, square feet, and MW. Less useful for planned hyperscale projects.
- **US Data Center Proposal Tracker**: public shell is accessible, but data is hidden behind client app/Turnstile. Worth a short browser/devtools pass, not first priority.
- **JLL/CBRE broker reports**: good for market-level capacity/pipeline sanity checks, not project-level rows. JLL page curls; CBRE blocks curl with 403.

## Commercial / not directly scrapeable

- **datacenterHawk**: public site only exposes aggregate claims such as 10,500+ verified data centers and 344 GW tracked. Full data/API appears app/login/commercial.
- **DC Byte**: public pages advertise 8,300+ facilities and facility-level fields, but project data is in Market Analytics/login/free trial.

## Recommended crawl priority

1. Cleanview project/state pages.
2. Baxtel sitemap, country/region/provider/facility pages.
3. FracTracker dashboard/download/layer endpoint.
4. dcmap.us static state/market pages, then browser-backed `/api/map`.
5. Data Center Map only after rate-limit strategy.
6. Cloudscene for operating facility enrichment.
7. Broker reports for aggregate QA, not row creation.
8. datacenterHawk/DC Byte only if paid/API access is procured.
