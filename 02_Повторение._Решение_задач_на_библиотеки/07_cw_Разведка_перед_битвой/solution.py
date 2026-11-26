import random
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = 'Разведка'
ws.append(['Тип войск', 'Количество', 'Опасность'])
s = 0
for t in input().split(', '):
    k = random.randint(50, 500)
    s += k
    ws.append([t, k, random.randint(1, 10)])
ws.append(['ИТОГО', s])
wb.save('enemies.xlsx')
