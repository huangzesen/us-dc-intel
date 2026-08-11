# Independent Review Pass — 2026-08-11 (Jason Telegram 3148)

240 centers reviewed by one `ds` lingtai daemon each (5 concurrent groups, backend=lingtai/deepseek).

## Results
- **PASS: 108** · **FLAG: 132**

## FLAG categories (overlapping)
- `status_history` key naming: 125 — review-brief wording artifact. Repo canonical change-log key is `history` (refresh-brief.md, generate_skeleton.py, 176/240 entries). Not a data defect; no mass rename.
- status consistency: 119 — includes 125 key-naming cascades (cross-check impossible without key) + real tier/evidence mismatches.
- evidence_grade missing: 38 — real schema gaps in some refreshed entries.
- capacity consistency: 26.

## Real issues needing fix (72 unique)
Top clusters:
- **Status tier vs evidence mismatch** (approved-permitted claimed but no permit evidence found): disc029, usdc-0025, usdc-0029, etc.
- **Dead/unreachable source URLs** (404 / connection refused / bot-block 403): disc011, usdc-0021, usdc-0026, usdc-0094, etc.
- **Missing evidence_grade / verified flags**: usdc-0047, usdc-0104, usdc-0105, etc.
- **history not updated on refresh** (data.json stale vs NOTES.md): usdc-0084, usdc-0011, usdc-0015.
- **SKILL.md vs data.json drift** (location/address not synced): usdc-0113, usdc-0035, usdc-0074.
- **Minor/cosmetic**: duplicate URLs, non-chronological actions, truncated sentences.

Full per-center issues: `reports/review-2026-08-11-summary.json`.
Raw per-center reports: dev4bot scratch/us-dc-review/*.json (parent workdir).
