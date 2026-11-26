import json

best = None
with open('rings.txt', encoding='utf-8') as f:
    for s in f:
        a = s.split()
        if a and (best is None or int(a[3]) >= int(best[3])):
            best = a
t, m, k, p = best[0], best[1], best[2], int(best[3])
d = {'title': t, 'material': m, 'keeper': k, 'power': p,
     'visibility': 'visible' if (len(t) + len(k) + p) % 2 == 0 else 'invisible'}
with open('powerful.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
