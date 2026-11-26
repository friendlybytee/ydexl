import random
from itertools import combinations

a = ['Джил', 'Люси', 'Питер', 'Сьюзен', 'Эдмунд', 'Юстэс']
n = int(input())
for c in random.sample(list(combinations(a, 4)), n):
    print(', '.join(c))
