a = b = 0
for x in input().split():
    x = int(x)
    if x % 2:
        a += x
    else:
        b += x
print(f'Тёмного мёда: {a}.')
print(f'Светлого мёда: {b}.')
