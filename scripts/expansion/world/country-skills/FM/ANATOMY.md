# FM · Country Anatomy

Datacenter-country knowledge layer for the Federated States of Micronesia (FM/FSM).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | Present — merged from the two explorers |
| Official / regulatory / cloud pipeline | `explorer-official.md` | Present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | Present |
| State division layer | `divisions/` | To be added later |

## Division layer (future)

The manifest (`world-manifest.jsonl`) requires state coverage of **4 states**: **Kosrae, Pohnpei, Chuuk, Yap**. A future `divisions/` layer will carry per-state discovery/audit skills; searches must stay anchored to "Federated States of Micronesia", "FSM", and the state names because "Micronesia" alone is regionally ambiguous, and states without a verified facility beyond telecom connectivity should be recorded as `no_projects: true` with the search trail preserved.
