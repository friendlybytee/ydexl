n, m = map(int, input().split())
t = 0
while n < m:
    t += 1
    n += 2 * t - 1
print(f'Время - {t}.')
print(f'Количество дозорных - {n}.')
