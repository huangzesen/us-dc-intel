import json, re
p = '/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-277.jsonl'
lines = open(p).read().splitlines()
out = []
fixed = 0
for line in lines:
    if not line.strip():
        continue
    try:
        json.loads(line)
        out.append(line)
        continue
    except Exception:
        pass
    # insert missing ']' closing source_urls before ', "evidence_date"'
    new = re.sub(r'/", "evidence_date"', '/"], "evidence_date"', line)
    try:
        json.loads(new)
        out.append(new)
        fixed += 1
    except Exception as e:
        print('STILL BAD:', str(e)[:100])
        out.append(line)
open(p, 'w').write('\n'.join(out) + '\n')
print('fixed lines:', fixed)
ok = bad = 0
for line in open(p):
    line = line.strip()
    if not line:
        continue
    try:
        json.loads(line)
        ok += 1
    except Exception as e:
        bad += 1
        print('BAD:', str(e)[:100])
print('OK', ok, 'BAD', bad)
