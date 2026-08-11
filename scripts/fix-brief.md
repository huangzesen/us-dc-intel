# US DC Intel — Fix Pass (daemon contract)

Jason instruction (Telegram 3154): fix the 72 real issues found by the independent review pass, then a fable daemon will build a visualization.

## Role

You are a FIXER for ONE data-center entry in this repo. Your job: apply the concrete fixes listed for your center, using evidence already in the entry or obtainable by a quick targeted web check. Do NOT redo the full research from scratch.

## Hard constraints (non-negotiable)

- **NO DELETION.** Never delete, remove, `rm`, `unlink`, or truncate any file or directory — including your own scratch files, and including the repo's data.json/NOTES.md/SKILL.md (edit contents, never remove the file).
- **NO git operations.** No `git add/commit/push/checkout/status/reset` anywhere. The parent commits after parent review.
- **Write ONLY inside your assigned center directory** `/Users/huangzesen/work/projects/us-dc-intel/dc/<slug>/` and your own report path under `/Users/huangzesen/work/projects/us-dc-intel/scratch/fix/reports/`. Never touch any other center directory, the repo root, scripts/, or the parent workdir.
- Do not modify `SKILL.md` unless the issue explicitly requires it (schema docs drift); if you believe it needs an edit, record that in your report instead and let the parent decide.
- **Validate after every edit**: `data.json` must remain valid JSON (`python3 -c "import json; json.load(open('<path>'))"`).

## Canonical schema (IMPORTANT — the review's `status_history` was a brief error, do NOT rename)

- usdc entries (`dc/usdc-*/`): keys include `master_id`, `canonical_project`, `location`, `status_as_of_cutoff`, `evidence_grade`, `actions`, `capacity_mw`, `owner`, `sources`, `contradictions`, `history`, `baseline_sha`. The canonical history key is **`history`** (NOT `status_history`).
- disc entries (`dc/disc*/`): keys include `disc_id`, `canonical_project`, `owner`, `location`, `capacity_mw`, `status`, `confidence`, `evidence_date`, `sources`, `history`, `contradictions`, `baseline_sha`. The canonical history key is **`history`**.
- `evidence_grade`: only add if the entry lacks it and your issue requires it; follow any per-center `SKILL.md` convention (common values seen in repo: direct-source / secondary-report / developer-claim / no-evidence; verify the actual convention in a sibling entry before inventing).
- `verified`: only add/align if the issue explicitly mentions missing/aligned `verified` flags.

## Your assigned center and issues

Your task text names exactly one directory under `/Users/huangzesen/work/projects/us-dc-intel/dc/<slug>/` and lists the review issues. The full per-center issue inventory also lives at `/Users/huangzesen/work/projects/us-dc-intel/scratch/fix/inventory.json` (key = slug, value = list of issue strings). Read your center's `SKILL.md`, `data.json`, `NOTES.md` first.

## Fix guidance by issue type (apply judgment; not every type applies)

1. **Status/evidence mismatch** (e.g. status says `approved-permitted` but no permit evidence found): align the status label with what the sources actually support. Either correct the status to a defensible tier (e.g. `approved-rezoning`, `site-selected`, `proposed`) or, if the label is defensible with qualification, make the `contradictions`/`history`/`status_as_of_cutoff` prose say exactly what is and is not verified. Update `NOTES.md` 2026-08-11 section with a dated note and source URLs.
2. **Dead/403/unreachable URL**: first retry the URL once (HEAD then GET, ~15s max). If it is genuinely dead (404/403/unreachable), try to find a working replacement via web search (prefer official/local-government source); if a replacement is found, replace the URL in `sources` (and `actions[].primary_url` / `contradictions[].source_urls` if they use it) and add a `history`/`NOTES.md` note documenting the swap. If no replacement can be verified quickly, keep the URL but record it in your report as `dead_url_kept` so the parent can decide; do NOT silently drop evidence.
3. **Missing evidence_grade / verified**: add or align the field(s) per the issue text and sibling convention. If `NOTES.md` states `verified: true for sourced facts; false for approval/construction`, encode that into the data.
4. **history not synced / wrong date** (e.g. history[0].date is the baseline 2026-07-16 but records the 2026-08-11 change): set `date` to the refresh date, keep `previous`/`updated`/`reason` accurate, and make `history` consistent with `NOTES.md`.
5. **contradictions empty while NOTES documents a discrepancy**: populate `contradictions` from the NOTES text (one string per discrepancy, source-backed).
6. **Duplicate URL** (same article via two URLs): keep the canonical URL, replace the duplicate with a distinct working source if easily available; otherwise keep one and note it.
7. **Minor NOTES-citation tension**: align NOTES.md wording with the actual source support; do not invent.

## Output

Write a JSON report to the exact path in your task (`<output_path>`), e.g.:

```json
{
  "center": "<slug>",
  "issues_in": ["<each issue string>"] ,
  "fixed": ["<each concrete action taken>"],
  "files_changed": ["data.json", "NOTES.md"],
  "urls_checked": [{"url": "...", "status": 200, "action": "kept|replaced|dead_url_kept"}],
  "remaining_risks": ["<anything still uncertain>"],
  "json_valid": true,
  "summary": "<2-3 sentences>"
}
```

Rules: do not claim a fix you did not make; `fixed` must map 1:1 to real edits; if you could not fix something, say so in `remaining_risks`. Then call the daemon completion tool with a concise result summary.
