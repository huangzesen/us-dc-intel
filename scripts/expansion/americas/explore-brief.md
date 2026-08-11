# Americas Datacenter Exploration — Daemon Task Brief

Each daemon receives ONE batch file and searches for datacenter projects in every division of that batch.

## Input
- Batch: `scripts/expansion/americas/batches/<batch>.jsonl` — one JSON object: `{country_code, country_name, divisions: [...]}`

## Output
- File: `scripts/expansion/americas/results/<batch>.jsonl` — one JSON line per discovered project/center
- Line schema: `{country_code, country_name, division, name, status, capacity_mw, developer, source_urls: [...], evidence_date, evidence_grade, notes}`
  - `status` ∈ announced|planned|approved|construction|operational|rejected|unknown
  - `capacity_mw`: number or null
  - `evidence_date`: ISO date when the source was published/checked
  - `evidence_grade`: A (official/primary), B (reliable trade press), C (weak/aggregate), U (unverified)

## Method (per division)
1. Web-search: `<division> <country> data center OR datacenter OR server farm project` (also try hyperscale/colocation names: AWS, Google, Microsoft, Meta, Equinix, Digital Realty, Vertiv, etc. + division)
2. For each hit: record a project with source URL + evidence date + grade
3. Cover every division in the batch. If a division genuinely has no datacenter activity, write `{"country_code": ..., "country_name": ..., "division": "<name>", "no_projects": true}` so coverage is complete
4. Aim for completeness over precision (宁多勿漏). 0-5 projects for tiny territories is fine; big divisions (São Paulo, Ontario, Quebec, Mexico City, etc.) should yield 5-30+

## Hard constraints
- **NO-DELETION**: never delete/rm any file. Only create your output file (mkdir -p the results dir first).
- No git writes, no repo modification beyond your results file.
- Use real public sources (official announcements, news, trade press). No fabricated data; mark confidence honestly.
- If a division is huge and time-limited, prioritize major cities/hubs in that division.

## Completion
- Reply with: output path, projects found count, divisions covered, per-division quick summary (one line each), any division with no projects found.
