from datetime import datetime

a = datetime.strptime(input().strip(), '%d/%m/%Y')
b = datetime.strptime(input().strip(), '%d/%m/%Y')
d = (b - a).days
with open('worlds.txt', 'w', encoding='utf-8') as f:
    print(d, file=f)
    print(d * 24, file=f)
    print('Ты стал героем!' if d > 7 else 'Это было короткое приключение', file=f)
