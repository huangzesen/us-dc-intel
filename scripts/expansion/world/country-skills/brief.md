# Country Methodology Pipeline — Daemon Task Brief（Jason 3455）

Each daemon receives ONE country (country_code + name + divisions) and researches how to efficiently and correctly enumerate datacenter projects for that country, then writes its findings to the country's methodology folder.

## Input
- Country code + name + divisions list (from world-manifest.jsonl).
- Read the template/sibling files under `country-skills/CN/` for the expected depth/style (explorer-1-web.md, explorer-2-*.md, explorer-3-*.md, SKILL.md).

## Output
- Folder: `scripts/expansion/world/country-skills/<CODE>/`
- File: `explorer-<your-angle>.md` — ONE new file. DO NOT overwrite the partner's file or SKILL.md.
- SKILL.md is written later by the parent from the explorer set (parent owns merge).

## Method (per country)
1. Web-search authoritative sources for that country: official regulator/licensing filings, planning-permit databases, grid/energy approvals, national DC association listings, hyperscale/colo vendor official region/zone pages, trade press.
2. For non-Chinese countries also note: English + local-language search patterns, government e-permitting portals (e.g. India's CPPP/state portals, Germany's BaFin/regulators + Bauantrag, UK planning portals, Australia state planning), cloud region official pages (AWS/Azure/GCP/OCI region list), major colo players.
3. Identify per-division enumeration approach: how to query each province/state/region for DC projects (e.g. state planning portal, local press, cluster/industrial park lists).
4. Reliability grades: A (official/primary), B (strong secondary/trade press), C (weak/aggregate).
5. Be concrete: URLs, query templates, portal names, key vendor/operator names.

## Hard constraints
- **NO-DELETION**: never delete/rm any file. Only create your own explorer file.
- No git writes, no repo modification beyond your explorer file.
- Use real public sources; no fabricated data; mark confidence honestly.

## Completion
- Reply with: output path, country, what the file covers, key findings (3-5 bullets).
