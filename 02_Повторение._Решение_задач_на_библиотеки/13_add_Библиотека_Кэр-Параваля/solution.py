import csv

from docx import Document
from docxtpl import DocxTemplate


res = None
with open('books.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, delimiter=';'):
        if int(row['Copies']) <= 1:
            continue
        t = DocxTemplate('book_card.docx')
        t.render(row)
        if res is None:
            res = t.docx
            continue
        res.add_page_break()
        end = res.element.body[-1]
        for e in list(t.docx.element.body)[:-1]:
            end.addprevious(e)
if res is None:
    res = Document()
res.save('library.docx')
