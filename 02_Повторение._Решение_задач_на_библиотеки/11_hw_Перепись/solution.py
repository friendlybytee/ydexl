from collections import Counter
from openpyxl import load_workbook

wb = load_workbook('census.xlsx')
rows = list(wb['Жители'].iter_rows(min_row=2, values_only=True))
age = [r[3] for r in rows]
hgt = [r[4] for r in rows]
k, c = Counter(r[2] for r in rows).most_common(1)[0]
ws = wb.create_sheet('Статистика')
ws.append(['Максимальный возраст', max(age)])
ws.append(['Средний возраст', round(sum(age) / len(age), 2)])
ws.append(['Максимальный рост', max(hgt)])
ws.append(['Средний рост', round(sum(hgt) / len(hgt), 2)])
ws.append(['Титульная раса (код)', k])
ws.append(['Процент титульной расы', round(c / len(rows) * 100, 2)])
wb.save('statistics.xlsx')
