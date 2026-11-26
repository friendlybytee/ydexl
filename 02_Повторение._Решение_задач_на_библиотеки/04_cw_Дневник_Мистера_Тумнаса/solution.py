from datetime import datetime

with open('tumnus_diary.txt', encoding='utf-8') as f:
    s = f.readline().split()[-1]
a = datetime.strptime(input().strip(), '%d.%m.%Y')
b = datetime.strptime(s, '%d.%m.%Y')
print(f'До встречи осталось {(b - a).days} дней')
