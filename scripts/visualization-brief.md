# US DC Intel — Visualization (fable/claude daemon contract)

Jason instruction (Telegram 3154 + 3158): after the fix pass, build a **visualization** of the US data-center intelligence repo, **including the total planned power (功耗) of planned data centers over the next few years**.

## Role

You are a VISUALIZATION ENGINEER. Build one self-contained, human-facing HTML dashboard from the repo's canonical data. Do NOT re-research the centers; the data has already been refreshed and reviewed.

## Hard constraints (non-negotiable)

- **NO DELETION.** Never delete, remove, `rm`, `unlink`, or truncate any file.
- **NO git operations.** No `git add/commit/push/checkout/reset` anywhere. The parent commits after review.
- **Write ONLY** to the output file(s) you are assigned: `/Users/huangzesen/work/projects/us-dc-intel/visualization/dc-dashboard.html` (create the dir if needed) and, if helpful, `/Users/huangzesen/work/projects/us-dc-intel/scratch/fix/viz-notes.md`. Do NOT touch any `dc/*/` center directory, `data.json`, `NOTES.md`, `SKILL.md`, or `reports/`.
- **NO secret-shaped content**: no `/Users/`, `scratch/`, `daemons/`, `logs/`, `em-*` local paths or file names in the HTML. The HTML must be publishable.

## Inputs

- `/Users/huangzesen/work/projects/us-dc-intel/scratch/fix/centers-summary.json` — 240 centers with: slug, name, state, capacity_mw (126 have values), status (long prose), evidence_grade, owner, completion_year (155 have values), verified.
- `/Users/huangzesen/work/projects/us-dc-intel/dc/*/data.json` — per-center canonical records (read only when you need details, e.g. status tier, sources count).

## Deliverable

One **standalone, self-contained HTML file** (`visualization/dc-dashboard.html`), conclusion-first, source-labeled, no external CDN required (inline CSS/JS only, or vanilla). Language: **中文** with English terms where natural. It must include:

1. **头部概览 (summary hero)**: total centers (240), centers with capacity data, total planned capacity in MW/GW, coverage notes, data as-of 2026-08-11.
2. **总功耗逐年图 (TOTAL PLANNED POWER BY YEAR — Jason's explicit request)**: bar/line chart of total planned capacity_mw (in GW) by completion_year (2025–2031+, plus an 'unassigned/unknown' bucket for centers with capacity but no year). This is the centerpiece.
3. **状态分布 (status distribution)**: classify status prose into coarse tiers (operational/live, construction/site work, approved/permitted, proposed/planned, unknown) with counts and a chart; include a method note that classification is derived from prose.
4. **地理分布 (geographic map)**: US state-level count and capacity aggregation (table or simple SVG/choropleth bars).
5. **所有者/运营商 (owner breakdown)**: top owners by count and by total capacity (e.g. Google, Microsoft, Meta, Amazon/AWS, xAI, CoreWeave, etc.).
6. **证据等级 (evidence grade)**: distribution of evidence_grade values and verified flags.
7. **明细表 (searchable table)**: all 240 centers — slug/name, state, capacity MW, completion_year, status tier, evidence_grade, verified. Client-side filter/sort.

Rules:
- Numbers must come from the data, not invented. Where capacity is missing, show it as missing and count it; do not impute.
- Include a short methodology/footnote: data as-of 2026-08-11 refresh + independent review; completion_year is derived from text signals (completion/target/energization phrases), so treat as directional.
- Make it visually clean and informative for a human scanning on a laptop: strong typography, consistent palette, no clutter.

## Output

After writing the HTML, verify it opens (file size > 50KB is fine; check no obvious broken template placeholders), then call the daemon completion tool with a concise summary: file path, approximate size, main sections, and any data caveats.
