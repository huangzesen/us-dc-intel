import json, re, sys
p = '/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-277.jsonl'
lines = open(p).read().splitlines()
for i, line in enumerate(lines, 1):
    try:
        json.loads(line)
        continue
    except Exception:
        pass
    print('BAD line', i)
    for m in re.finditer(r'\]"', line):
        print('   seg:', repr(line[max(0, m.start()-50):m.end()+30]))
