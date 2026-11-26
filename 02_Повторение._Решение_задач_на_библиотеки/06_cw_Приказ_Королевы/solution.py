from docxtpl import DocxTemplate

a, b, c = input().split('/')
t = DocxTemplate('decree_template.docx')
t.render({'ruler': a, 'item': b, 'palace': c})
t.save('order.docx')
