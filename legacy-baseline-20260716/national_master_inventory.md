# Phase 4 national integration and deduplication

Cutoff: 2026-07-16.

- **208 unique master projects**: 185 detailed Phase3 physical records plus 23 unmatched seed-only records.
- Seed dispositions: 48 merged, 23 retained seed-only, 6 excluded.
- Phase3↔regional stable-ID coverage: 186/186; orphan IDs: 0 regional, 0 Phase3.
- Ledger mappings: 447/447; duplicate input keys: 0.
- Phase3 action records: 513 input, 512 retained in included raw Phase3 records, 512 retained in master raw action records.
- Unique source URLs retained in master or exclusion ledger: 667/667.
- State counts: AK: 2, AL: 3, AR: 1, AZ: 7, CA: 4, CO: 2, GA: 8, HI: 1, IA: 4, ID: 2, IL: 6, IN: 10, KS: 2, KY: 2, LA: 1, MA: 2, MD: 3, ME: 4, MI: 2, MN: 7, MO: 4, MS: 6, MT: 1, NC: 5, ND: 4, NH: 2, NJ: 4, NM: 1, NV: 5, NY: 4, OH: 11, OK: 8, OR: 4, PA: 6, RI: 1, SC: 5, SD: 3, TN: 2, TX: 23, UT: 11, VA: 7, WA: 5, WI: 6, WV: 3, WY: 4

Phase3 is authoritative. Regional records merge by exact stable ID. Seed rows merge only on explicit evidence; uncertain candidates remain separate and flagged. Raw detailed records are embedded to preserve aliases, roles, locations, capacities, milestones, actions, status, pending evidence, sources, contradictions, and provenance. Government and company evidence retain their supplied classifications.

SHA-256:
- national_master_inventory.json: 2113de4b0a3455288dc010fcf731fca2aa127d7faa02cfd7418950716b1d1b9a
- dedupe_ledger.json: 9484ab2dc20d8b02ecd48ce9919919ee22be9e91fef2da5cd33927a8c5d7f95c
