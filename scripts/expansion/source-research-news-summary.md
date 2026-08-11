# Source Research - News / Announcements / State / Federal

Scope: items #11-14 in the brief plus free project-level sources found during testing. I used direct `curl` checks and web search. Tested sources include Wikipedia API, Utility Dive RSS/articles/trendline, DCD, VEDP, IEDC, WEDC, Permitting Council, TrackDataCenters, and Data Center Knowledge.

## Best Direct-Crawl Sources

1. State economic development press-release portals, especially VEDP, IEDC, and WEDC.
   These are authoritative, free, stable, and project-level. They usually include company, county/city, investment, jobs, announcement date, incentives, and status. Capacity MW is inconsistent, but Virginia sometimes gives capacity or square footage. Build a CMS-aware crawler seeded by state + `data center`, `datacenter`, `cloud`, `AI infrastructure`.

2. Data Center Knowledge monthly `New Data Center Developments`.
   Free pages are crawlable and often aggregate multiple named projects with capacity/status. This is the best news-style recurring project feed I found. Parse monthly article URLs from search/RSS, then extract project bullets from article body.

3. Utility Dive RSS/search/trendline.
   Directly crawlable and useful for power/interconnection context, named loads, utility deals, and early grid-side signals. It is not a clean project table, so treat as discovery leads and enrich with primary operator/state/RTO sources.

4. Permitting Council FAST-41 portfolio and press releases.
   Very high-quality federal signal for projects requiring federal coordination. Current data-center coverage is small, with QTS Richmond Technology Park Data Center 5 as the key sample, but this should be watched because policy now explicitly routes data-center infrastructure into FAST-41.

## Partial Or Fragile Sources

- Wikipedia has a working API but no complete US data-center list. Use only as seed/de-dupe for notable facilities and operator pages.
- Data Center Dynamics has strong project-level articles, but direct `curl` returned Cloudflare challenge/403. Use web search/browser-assisted discovery or a licensed feed.
- TrackDataCenters is highly relevant but not curl-friendly: the app exposes a `/api/data/` path in the bundle, but direct API access returns an error and the site uses Turnstile. Use only with permission or browser-based collection.

## Recommended Priority

1. Implement state EDO crawler for VA, TX, GA, IN, WI, OH, AZ, IA, NC, SC, LA, MS, PA, NY, MI.
2. Add Data Center Knowledge monthly roundup parser.
3. Add Utility Dive RSS/search lead collector for grid-linked project discovery.
4. Add Permitting Council FAST-41 watcher for `Data Storage and Data Management`.
5. Keep DCD and TrackDataCenters as manual/browser-assisted enrichment, not unattended primary feeds.

Validation notes: direct tests confirmed successful reads for Wikipedia category API, Utility Dive feed/article/trendline, VEDP article/list, IEDC article, WEDC article/search, Data Center Knowledge article/search, and permitting.gov FAST-41 portfolio. Direct tests confirmed access problems for DCD via Cloudflare, old `permits.performance.gov` via Akamai Access Denied, and TrackDataCenters `/api/data/` via direct-access denial.
