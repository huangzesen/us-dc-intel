---
name: method-explore
location: scripts/expansion/world/method-tasks/method-explore/SKILL.md
description: "Method-driven datacenter exploration contract - read a batch file and the country methodology, web-search every division, write results JSONL. Read before every method-driven exploration task."
---

# Method-Driven Exploration Brief

You are a deepseek-flash explorer in the method-driven datacenter discovery pipeline. Work dir: /Users/huangzesen/work/projects/us-dc-intel

## Input
- Batch file: `scripts/expansion/world/method-batches/<batch>.jsonl` — one JSON object: `{country_code, country_name, divisions: [...], part, total_parts}`
- Methodology: `scripts/expansion/world/country-skills/<CODE>/SKILL.md` plus `explorer-official.md` and `explorer-industry.md` in the same directory. READ the methodology first: it holds the division model, verified query templates, official/regulatory and industry/vendor discovery pipelines, source-reliability grades (A/B/C/U), and per-division search notes for this exact country.

## Method (per division in the batch)
1. Follow the country methodology: use its search vocabulary / query templates, its verified official/regulator/cloud-region sources and industry/press/operator/interconnection sources.
2. Web-search each division for real datacenter projects: `<division> <country> data center OR datacenter OR server farm OR colocation` plus the methodology's vendor/operator names (AWS, Google, Microsoft, Meta, Equinix, Digital Realty, NTT, STT GDC, AirTrunk, Colt DCS, Vantage, GDS, Chindata, Yondr, etc. + division).
3. For each hit record a project with source URL + evidence date + grade.
4. Cover every division in the batch. If a division genuinely has no datacenter activity, write `{"country_code": ..., "country_name": ..., "division": "<name>", "no_projects": true}` so coverage is complete.
5. Aim for completeness over precision. Major hubs should yield more; tiny territories 0-5 is fine. Reuse results already in `results/` (first-round codex discovery) as leads but RE-VERIFY against the methodology; the point of this round is method-driven depth, so prefer newly verified evidence.

## Output
- File: `scripts/expansion/world/results-method/<batch>.jsonl` — one JSON line per discovered project/center:
  `{country_code, country_name, division, name, status, capacity_mw, developer, source_urls: [...], evidence_date, evidence_grade, notes}`
  - `status` in announced|planned|approved|construction|operational|rejected|unknown
  - `capacity_mw`: number or null
  - `evidence_date`: ISO date when the source was published/checked
  - `evidence_grade`: A (official/primary), B (reliable trade press), C (weak/aggregate), U (unverified)
- If your batch was partially completed by a previous run, read the existing output and only append missing divisions.

## Hard constraints
- **NO-DELETION**: never delete/rm any file. Only create your output file (mkdir -p the results-method dir first).
- No git writes, no repo modification beyond your output file.
- Use real public sources. No fabricated data; mark confidence honestly (U when unverified).
- Do not read or touch other agents' private data.

## Completion
- Reply with: output path, projects found count, divisions covered, per-division quick summary (one line each), any division with no projects found.
