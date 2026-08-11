# GRIDWATCH — Design Proposal for the US Data Center Intelligence Site

**Redesign of `xhelio.ai/datacenters/`** · Proposal + working mockup (`design-mockup.html`)
**Date:** 2026-08-11 · **Data basis:** 2,731 unified centers, 8,019 source URLs, 544.2 GW tracked capacity, 3,222 counties explored (100%)

---

## 1. Art Direction Statement

**Concept: "The National Grid Operations Room" （国家电网作战室）**

The current page is a project-tracking kanban. The data has outgrown it: what the corpus actually documents is **the largest industrial buildout in modern American history** — a 544-gigawatt compute pipeline racing across 1,175 counties. The redesign reframes the site from *"our exploration progress board"* to *"a national situational-awareness instrument"* — something between a power-grid SCADA console, a Bloomberg terminal, and a NORAD wall display.

Design principles:

- **The number is the hero.** One enormous animated figure — 544.2 GW — anchors the page. Everything else is evidence supporting it.
- **Instrument, not brochure.** Monospace numerals, hairline rules, engineering-drawing grid texture, uppercase letterspaced kickers. Dense but never cluttered.
- **Dark-first.** A control room is dark. Light mode is the "print/daylight" variant, not the default.
- **Color is data.** Chrome is nearly monochrome (steel blue-black + one amber signal accent). Saturated color appears **only** where it encodes status or magnitude — so every colored pixel means something.
- **Motion = power flowing.** Counters count up, bars energize left-to-right, a faint scanline sweeps the hero. One well-orchestrated load sequence; no gratuitous wiggle.

The memorable thing: **opening the page feels like switching on a wall of instruments that are watching the entire country.**

---

## 2. Color Palette

All chart colors are taken from a CVD-validated palette and were **re-validated with a colorblind-simulation validator against the actual page surfaces** (dark `#11161F`, light `#FCFCFA`). The pipeline-status ordering (violet→magenta→blue→orange→aqua) passes adjacent-pair checks in both modes.

### Chrome (UI) tokens

| Role | Dark (default) | Light |
|---|---|---|
| Page plane | `#0A0D12` | `#F5F5F1` |
| Card / chart surface | `#11161F` | `#FCFCFA` |
| Hairline / border | `#1E2734` | `#E3E2DA` |
| Primary ink | `#E8EDF6` | `#14181F` |
| Secondary ink | `#A7B2C5` | `#4C5566` |
| Muted (axis, captions) | `#66748C` | `#7C8698` |
| **Signal accent (amber)** — chrome only | `#F5A83C` | fill `#E09A2D`, text-safe `#8A5A00` |

Amber is the "power/energization" brand signal: active tabs, focus rings, the live-pulse dot, hero underline. It is **never** used as a chart series color (it would collide with the construction orange).

### Status palette (the core encoding — used identically in chips, funnel, stacked chart)

| Status | 中文 | Light | Dark |
|---|---|---|---|
| Announced 已公告 | violet | `#4A3AA7` | `#9085E9` |
| Planned 规划中 | magenta | `#E87BA4` | `#D55181` |
| Approved 已批准 | blue | `#2A78D6` | `#3987E5` |
| Construction 在建 | orange | `#EB6834` | `#D95926` |
| Operational 运营中 | aqua | `#1BAF7A` | `#199E70` |
| Rejected 已否决 | red | `#E34948` | `#E66767` |
| Unknown 未知 | gray | `#898781` | `#898781` |

Validator result: dark mode **all checks pass** (worst adjacent CVD ΔE 9.4); light mode passes CVD + normal-vision floors, with two fills below 3:1 surface contrast — mitigated per the relief rule (every colored mark carries a **visible text label**, and the registry table is a full table view).

### Sequential ramp (choropleth / magnitude only) — blue, one hue

Light mode (low→high): `#CDE2FB → #9EC5F4 → #5598E7 → #256ABF → #0D366B`
Dark mode (low→high, brightest = most): `#0D366B → #184F95 → #2A78D6 → #5598E7 → #86B6EF`

---

## 3. Typography

No webfont downloads (self-contained, GitHub Pages friendly). Character comes from *how* system faces are used, not which:

- **Data face (display + numerals + labels):** `ui-monospace, 'SF Mono', Menlo, Consolas, monospace`. All numbers are monospaced — they align, they tick, they read as instrumentation. The hero figure is mono at ~96px with tight tracking.
- **Prose face:** `system-ui, -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif` — also covers Chinese cleanly.
- **Kickers/section labels:** mono, uppercase, `letter-spacing: 0.18em`, muted ink, prefixed with an index (`01 · NATIONAL MAP`) — the engineering-document register that gives the page its voice.
- Tabular alignment everywhere numbers stack (mono gives this for free).

---

## 4. Layout System

- **12-col fluid grid, max-width 1240px**, 24px gutters; cards sit on the page plane with 1px hairlines and 14px radius. Background carries a **faint blueprint grid texture** (pure CSS `repeating-linear-gradient`, ~2% opacity) + a soft radial glow behind the hero.
- **Narrative order (top → bottom):** Headline instrument → geography → pipeline physics → time → actors → receipts.
  1. **Topbar** — wordmark + EN/中文 + Dark/Light (sticky).
  2. **Hero** — animated 544.2 GW counter + 4 stat tiles (facilities / sources / counties with projects / counties explored 100%).
  3. **01 · National map** — US tile-grid cartogram choropleth, metric toggle (GW ↔ facility count), click-to-filter.
  4. **02 · Pipeline funnel** — announced → planned → approved → construction → operational, by GW.
  5. **03 · Buildout wave** — stacked columns 2018–2030 by year signal.
  6. **04 · Operators** — top-developer leaderboard, tabbed by capacity / by facility count.
  7. **05 · Registry** — sortable, filterable table of real projects with status chips and inline capacity bars.
  8. **Footer** — evidence-grade distribution (official/news/tracker/social), corpus timestamp, method note.

---

## 5. Key Components & Data-Visualization Ideas

### 5.1 Hero counter (the wow moment)
`544.2 GW` counts up from 0 over ~1.8s (ease-out `requestAnimationFrame`), amber underline draws in, a scanline sweeps once. Sub-line: *"tracked across 2,731 facilities · 8,019 sources"*, each also counting up. A pulsing "LIVE CORPUS" dot ties it to the pipeline that regenerates the page.

### 5.2 US tile-grid cartogram (replaces "wall of batch cards")
- 11×8 CSS-grid of state tiles (50 states + DC + PR) in the standard tile-map arrangement — **no image, no GeoJSON, no CDN**; it's ~50 divs.
- Choropleth fill = sequential blue ramp binned on capacity (＜1 / 1–5 / 5–15 / 15–45 / 45+ GW); toggle re-bins by facility count.
- Hover → tooltip (state, facilities, GW). **Click → filters the registry table** and pins a state chip in the filter bar. This one interaction turns the page from report into instrument.
- Why tile grid over true choropleth: zero dependencies, mobile-legible, equal visual weight per state (TX/VA don't win by land area — they win by color, which is the honest encoding).

### 5.3 Pipeline funnel
Five horizontal bars, width ∝ GW, in the validated status colors with direct labels (GW + project count). Reads the buildout's physics at a glance: **212.6 GW planned vs 27.7 GW operational — a 7.7× wave still to land.**

### 5.4 Buildout wave (stacked columns, 2018–2030)
Yearly project signals stacked as Pipeline / Construction / Operational (3 validated series, 2px segment gaps, 4px rounded tops). The hockey stick — 19 signals in 2018 → 781 in 2026 — *is* the story; a linear axis keeps it honest. Hover gives per-year breakdown; legend always visible.

### 5.5 Operator leaderboard
Top-10 horizontal bars, single-hue (no legend needed), direct-labeled. Tab toggle: **by GW** (Tract 17.9, Fermi America 17.0, Meta 10.3 …) vs **by facilities** (Microsoft 65, Google 62, AWS 38 …) — two very different stories, one component.

### 5.6 Registry table
~55 real flagship projects (from the DB) with: mono capacity column + inline magnitude bar, colored status chips (always labeled), county/state, year signal, evidence grade tag. Sortable headers (GW, year), status + state filter selects, wired to the map. This is also the accessibility "table view" for every chart above.

### 5.7 Evidence strip (footer)
One stacked bar: official 1,608 / news 642 / tracker 440 / social 36 — the "receipts" that make the corpus credible.

*(Not in mockup, worth doing later: county-level heatmap drill-in per state; capacity-weighted funnel conversion rates; per-operator sparklines; "new this week" diff badges.)*

---

## 6. Dark / Light Theming

- CSS custom properties on `:root[data-theme=…]`; **every** color in the page (chrome *and* chart) is a token — zero raw hex in component CSS.
- Dark is default (control-room stance); toggle persists in `localStorage`, respects `prefers-color-scheme` on first visit.
- Chart colors are **re-stepped per mode, not auto-inverted** — the dark sequential ramp runs brightest-= -highest, both mode sets validated separately.

## 7. Bilingual EN / 中文

- Keep the proven `<span class="en">/<span class="zh">` pattern, but drive it from `html[data-lang]` with CSS (`[data-lang="en"] .zh { display:none }`) — no JS walking the DOM.
- JS-generated strings (tooltips, chips, counts) go through a tiny `L(key)` dictionary keyed off `data-lang`.
- Numbers, state codes, and operator names stay Latin in both languages (correct convention for zh data dashboards).

## 8. Responsive / Mobile

- Stat tiles: 4-up → 2-up → 1-up. Map tiles shrink to abbr-only (value labels hide < 720px); tooltips switch to tap.
- Funnel and leaderboard are horizontal bars — they survive narrow screens natively.
- Registry becomes an edge-swipe horizontal-scroll table with sticky first column; filters wrap.
- All charts are HTML/CSS boxes (no canvas), so they reflow for free.

## 9. Interaction & Motion Details

- **Load sequence (staggered, once):** hero counter → stat tiles fade-rise (60ms stagger) → bars energize on scroll into view (`IntersectionObserver`, width/height transition with per-index delay).
- Hover: tiles lift 1px + hairline brightens; table rows wash; every chart mark has a tooltip with hit-target ≥ the mark.
- Map click = cross-filter; active filters render as dismissible chips ("TX ✕").
- Sort headers show ▲▼ carets; re-sort animates nothing (tables should be instant).
- `prefers-reduced-motion`: counters render final values, transitions collapse to 0 — one media query.

## 10. Implementation Plan (changes to `render_kanban.py`)

Keep the architecture exactly as-is: **Python renders one static self-contained HTML** from the SQLite DB. No build step, no framework, no CDN.

1. **Split the template out.** Move HTML/CSS/JS into `kanban_template.html` with `%%TOKEN%%` slots; `render_kanban.py` becomes: query → aggregate → `json.dumps` → substitute. (Keeps diffs reviewable as the page grows.)
2. **New aggregation queries** (all shown in this proposal exist in the current schema):
   - totals: `COUNT(*)`, `SUM(capacity_mw)`, source count, distinct county count;
   - per-state: count + MW (feeds map);
   - status funnel: count + MW for the 5 canonical statuses (fold long-tail `status` strings into the nearest canonical bucket with a small mapping table — the DB has ~20 verbose one-off statuses);
   - year × status-group matrix (2018–2030);
   - top operators by count and by MW (consider a `owner_canonical` normalization pass later — "Amazon Web Services"/"Amazon Data Services"/"Amazon" currently split);
   - registry rows: top ~200 by MW + all operational ≥100 MW, as a JSON array (client-side filter/sort handles the rest);
   - evidence-grade counts.
3. **Embed data as one `const DATA = {...}` JSON blob**; all rendering is client-side from that blob (map, funnel, wave, leaderboard, table). Page stays a single file; payload for ~200 registry rows is ~40 KB, well under GitHub Pages comfort.
4. **Keep the old kanban content** (batch board, county tables) behind a collapsed "Exploration ops" section or a second page (`/datacenters/ops.html`) — the exploration-progress view still matters to you, it just shouldn't be the front door. 100%-complete batch cards are history, not news.
5. **Ship order:** tokens + hero + map (day 1) → funnel + wave + leaderboard (day 2) → registry + cross-filter + i18n/theming polish (day 3). Each stage is shippable.

## 11. Success Criteria

- First-screen comprehension: a stranger understands "US is building ~544 GW of data centers, here's where" in **< 10 seconds**.
- Zero external requests; single HTML file; < 300 KB.
- Both themes and both languages fully covered; charts pass CVD validation; every color-encoded mark carries a text label.

---

*Companion artifact: `design-mockup.html` — a fully working, self-contained demonstration built on real database values (55+ real projects, real per-state totals, real funnel/wave/operator numbers).*
