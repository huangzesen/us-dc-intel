#!/usr/bin/env python3
import json, sys

def fix(path):
    raw = open(path, encoding='utf-8').read()
    dec = json.JSONDecoder()
    idx = 0
    objs = []
    while True:
        while idx < len(raw) and raw[idx] in ' \t\r\n':
            idx += 1
        if idx >= len(raw):
            break
        obj, end = dec.raw_decode(raw, idx)
        objs.append(obj)
        idx = end
    with open(path, 'w', encoding='utf-8') as f:
        for o in objs:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    print(f'{path}: {len(objs)} records rewritten')

for p in sys.argv[1:]:
    fix(p)
