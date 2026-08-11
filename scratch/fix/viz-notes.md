# Visualization notes — dc-dashboard.html (2026-08-11)

Built `visualization/dc-dashboard.html` (64.7 KB, standalone, inline CSS/JS, no CDN, 中文 + English terms, light + dark mode with toggle) from `scratch/fix/centers-summary.json` (240 rows embedded as a compact JSON array; all displayed numbers computed client-side from that single embedded source).

## Headline numbers (as rendered)

- 240 centers; **126 with capacity_mw**, total **107,566 MW ≈ 107.6 GW** (floor estimate — 114 centers have no disclosed MW and are NOT imputed).
- By target completion year (capacity-weighted, GW): 2025: 10.6 · **2026: 49.0** · 2027: 1.7 · 2028: 7.8 · 2029: 0.3 · 2030: 0 · 2031+: 2.7 · **year unknown: 35.5**. 155 centers have a completion_year (41/106/3/3/1/1 across 2025/2026/2027/2028/2029/2031).
- Status tiers (keyword classification of status prose): operational 95 (23.0 GW), construction 67 (31.2 GW), approved/permitted 37 (25.7 GW), proposed/planned 40 (27.7 GW), unknown 1 ("not verified - likely seed conflation").
- States: 45 after normalization; TX 33 centers / 28.8 GW leads, then UT 14.3, OH 12.8, PA 10.9. Top-3 states = 52% of disclosed capacity.
- Owners (keyword canonicalization): "Other" bucket 107 centers / 54.7 GW; named leaders by capacity Amazon/AWS 11.2, Meta 8.6, Microsoft 5.7, PowerHouse/AREP 4.1, Google 3.8 GW; by count Google 26, AWS 19, Microsoft 18, Meta 15, QTS 11.
- Evidence grade (leading letter extracted): B 91, A- 61, A 19, B+ 8, B- 1, prose-only 26, null 34. Verified: true 14, false 7, null 219.

## Derivation choices (all done at build time, embedded per-row)

- **State normalization**: summary mixes 2-letter codes and full names ("Texas", "West Virginia") — mapped full names to codes before aggregating.
- **Status tier**: regex priority operational > construction(-underway signals only, so "pre-construction"/"construction expected" don't count) > approved > proposed; "local process" → proposed. Method note shown in the dashboard.
- **completion_year 2026 concentration** (106/155) likely partly an extraction artifact; dashboard flags it as directional next to the centerpiece chart.
- **Owner field types**: 7 dicts + 1 list in the summary — flattened values (URLs dropped) before canonical keyword matching; JVs count under first matched operator.
- **Evidence grade**: `^[ABCD][+-]?` prefix extracted; long free-text grades shown as 长文本.

## Verification done

- JS syntax check of the embedded script (node `new Function`) — OK; no placeholder remains.
- Rendered via headless Chrome in light and dark modes and visually inspected — layout, labels, both palettes OK.
- Grepped the HTML for local-path-shaped strings — none (only font-stack false positive).
- Palette: dataviz reference palette; ordinal blue ramps validated with the skill's validator in both modes (ALL CHECKS PASS).
