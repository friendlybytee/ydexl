import random
from itertools import combinations

a = input().split()
w = {}
with open('tournament.txt', 'w', encoding='utf-8') as f:
    for x, y in combinations(a, 2):
        z = random.choice([x, y])
        w[z] = w.get(z, 0) + 1
        print(f'{x} vs {y}: победил {z}.', file=f)
    for k in w:
        print(f'{k} - {w[k]}', file=f)
