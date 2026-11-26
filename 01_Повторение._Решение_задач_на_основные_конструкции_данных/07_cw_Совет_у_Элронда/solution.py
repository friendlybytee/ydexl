import csv
import json

g = {}
with open('members.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        g.setdefault(r['race'], []).append(r['name'])
with open('council.jsonlines', 'w', encoding='utf-8') as f:
    for k in sorted(g):
        d = {'race': k, 'members': sorted(g[k], key=lambda x: (-len(x), x))}
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
