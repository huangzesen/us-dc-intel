# US Data Center Intelligence

Self-maintaining, regularly-updated intelligence repo for U.S. under-construction / planned data centers.

- **Route**: read `SKILL.md` first (top-level progressive disclosure)
- **Baseline**: `legacy-baseline-20260716/` — frozen 2026-07-16 national master inventory (208 masters; SHA `2113de4b…`)
- **Per-center dirs**: `dc/<slug>/` each with `SKILL.md` (maintenance contract), `data.json` (structured baseline fields), `NOTES.md` (update log)
- **Scripts**: `scripts/generate_skeleton.py` (idempotent skeleton generator)
- **Ownership**: built by dev4bot per Jason (Telegram 3089/3093/3097/3107/3109); baseline origin 衡枢(codex)/算枢(datacenter-tracker)

## Status

- [x] repo init + baseline freeze (byte-identical, SHA verified)
- [x] 208 per-center skeleton generated
- [x] top-level SKILL.md + generator script
- [ ] codex daemon discovery of DCs NOT in baseline (Jason 3107)
- [ ] 208-center batch refresh + evidence-gap fill
- [ ] weekly self-maintenance loop
