#!/usr/bin/env python3
"""Generate Americas exploration batches from americas-manifest.jsonl.

Method (same as US county exploration): chunk each country's second-level
admin divisions into groups of ~10 divisions; tiny territories (<=5 divisions)
stay as one whole-territory batch. US is skipped (already explored at county
level, deeper than second level).

Outputs:
  scripts/expansion/americas/batches/<batch>.jsonl  — one JSON object per batch
"""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(BASE, "americas-manifest.jsonl")
BATCH_DIR = os.path.join(BASE, "batches")
os.makedirs(BATCH_DIR, exist_ok=True)

SKIP_COUNTRIES = {"US"}  # US done at county granularity
CHUNK = 10

rows = [json.loads(l) for l in open(MANIFEST) if l.strip()]
batches = []
for r in sorted(rows, key=lambda x: x["country_code"]):
    cc = r["country_code"]
    if cc in SKIP_COUNTRIES:
        continue
    divs = r["divisions"]
    if len(divs) <= 5:
        batches.append({"country_code": cc, "country_name": r["country_name"], "divisions": divs})
    else:
        for i in range(0, len(divs), CHUNK):
            batches.append({"country_code": cc, "country_name": r["country_name"], "divisions": divs[i:i+CHUNK]})

for i, b in enumerate(batches):
    with open(os.path.join(BATCH_DIR, f"batch-{i:03d}.jsonl"), "w") as f:
        f.write(json.dumps(b, ensure_ascii=False) + "\n")

print(f"batches: {len(batches)}")
print(f"divisions covered: {sum(len(b['divisions']) for b in batches)}")
print(f"batch dir: {BATCH_DIR}")
