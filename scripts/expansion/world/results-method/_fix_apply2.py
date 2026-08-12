import json
p = '/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-277.jsonl'
lines = open(p).read().splitlines()
out = []
for line in lines:
    if not line.strip():
        continue
    try:
        json.loads(line)
        out.append(line)
        continue
    except Exception:
        pass
    # insert missing ']' closing source_urls at the unique boundary
    marker = '", "evidence_date"'
    idx = line.find(marker)
    if idx == -1:
        print('NO MARKER - manual needed')
        out.append(line)
        continue
    new = line[:idx] + '"]' + line[idx+1:]
    try:
        json.loads(new)
        out.append(new)
    except Exception as e:
        print('STILL BAD:', str(e)[:120])
        out.append(line)
open(p, 'w').write('\n'.join(out) + '\n')
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
