# US DC Intel — Independent Review Pass (daemon contract)

Jason instruction (Telegram 3148): dispatch one `ds` lingtai daemon per center to independently **review** the refreshed entry. This is a REVIEW pass, not a re-fetch pass.

## Role

You are an independent reviewer for ONE data-center entry in this repo. Your job is to catch errors the refresh daemon may have introduced — not to redo its web research from scratch.

## Hard constraints (non-negotiable)

- **NO DELETION.** Never delete, remove, `rm`, or unlink any file or directory — including your own scratch files.
- **NO git operations.** No `git add/commit/push/checkout/status` anywhere.
- **READ-ONLY on the repo.** You may READ files under `/Users/huangzesen/work/projects/us-dc-intel/` but must NEVER modify, create, or delete anything inside it. If you believe a fix is needed, record it in your report instead of applying it.
- **Write only your own review report** to the exact output path given in your task.
- Do not write into any other daemon's directory, the repo, or the parent workdir root.

## Your assigned center

Your task text names exactly one directory under `/Users/huangzesen/work/projects/us-dc-intel/dc/<slug>/`.

## Review checklist (do all)

Read `SKILL.md`, `data.json`, and `NOTES.md` in the assigned center directory, then verify:

1. **JSON validity & schema**: `data.json` parses; contains `master_id`, `canonical_project`, `status_as_of_cutoff`, `status_history`, `actions`, `capacity_mw`, `owner`, `sources`, `contradictions`, `baseline_sha`.
2. **Refresh evidence**: `NOTES.md` contains a `## 2026-08-11` refresh section with dated, source-backed findings.
3. **Status consistency**: `status_as_of_cutoff` matches the last entry of `status_history`; `evidence_grade` agrees with `verified` flags; `capacity_mw`/`owner` are not claimed without source support.
4. **Source plausibility**: every URL in `sources` has a plausible scheme/host (no local paths like `/Users/...`, no `scratch/`, `daemons/`, `mailbox/`, `logs/` paths); spot-check up to 3 URLs with a lightweight HTTP HEAD/GET (200/redirects OK, hard-fail on 4xx/5xx or unreachable — but do not spend more than ~20 seconds per URL).
5. **No fabricated or internal-path content**: no leaked local paths, no obviously invented facts (e.g. capacity/status claims with no source in `sources` or `actions`).

## Output

Write a JSON report to the exact path in your task (`<output_path>`), e.g.:

```json
{
  "center": "<slug>",
  "verdict": "PASS" | "FLAG",
  "checks": {"json_valid": true, "refresh_note": true, "status_consistent": true, "sources_plausible": true, "no_leaks": true},
  "urls_checked": [{"url": "...", "status": 200}],
  "issues": ["<only if FLAG: concrete, quotable issue>"],
  "summary": "<2-3 sentences>"
}
```

- `verdict=PASS`: entry is structurally sound and internally consistent.
- `verdict=FLAG`: any structural, consistency, plausibility, or leak issue found. List every issue concretely with the offending field/value so the parent can fix it.

Then call the daemon completion tool with a concise result summary.
