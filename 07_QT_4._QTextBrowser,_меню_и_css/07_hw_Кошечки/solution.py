"""
Задача: Кошечки
Категория: Домашняя работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
В файле `cat_breeds.csv` (для отладки можно скачать [пример](https://assets.contest.yandex.net/testsys/statement-file.gif?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..HkG93vRbQBIbkIFP.w_EA9T9VmygunKBPO35lmX2UaEsdKm-PjCSORVPh1GpXgB5e9XlpU1mnalhGvVmAxGf-Hw876_q0ASIOAcNml0PmZzS-nsh-jsziznUI.OSQoHGMkg68BTdw2qdFf-g)) записана информация о породах кошек и некоторые дополнительные сведения о каждой из них с заголовками (разделители — ;):

```
Breed; Location of origin; Type; Body type; Coat type and length; Coat pattern
```

Напишите приложение на PyQT6, которое помогает найти породу по вводимой в поле `QLineEdit` подстроке. Все строки, в породе которых есть подстрока в любом регистре, выводятся в поле QTextBrowser со значениями полей через запятую и пробел. Порода (breed) выделена полужирным начертанием (bold), остальное — обычным. Заливка под текстом чередуется из цветов по порядку в цикле:

```
Cornsilk
BlanchedAlmond
Bisque
NavajoWhite
Wheat
BurlyWood
Tan
```

Цвет под строкой можно изменить так: `<тег style="background:имя цвета">...</тег>`

Класс, реализующий окно приложения, называется `CatBreeds` и наследуется от `QMainWindow`, должен быть метод `write`.

Окно содержит строку для ввода породы `QLineEdit` с именем `lineEdit` (вывод появляется сразу после ввода символа) и поле вывода `QTextBrowser` с именем `textBrowser`.

![cat_breeds.gif](./statement-file.gif)

"""

import csv
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextBrowser

COLORS = ["Cornsilk", "BlanchedAlmond", "Bisque", "NavajoWhite", "Wheat", "BurlyWood", "Tan"]


class CatBreeds(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lineEdit = QLineEdit()
        self.textBrowser = QTextBrowser()
        central = QWidget()
        lay = QVBoxLayout(central)
        lay.addWidget(self.lineEdit)
        lay.addWidget(self.textBrowser)
        self.setCentralWidget(central)
        try:
            with open("cat_breeds.csv", encoding="utf-8") as f:
                self.rows = list(csv.reader(f, delimiter=";"))[1:]
        except OSError:
            self.rows = []
        self.lineEdit.textChanged.connect(self.write)

    def write(self):
        sub = self.lineEdit.text().lower()
        res = []
        for row in self.rows:
            row = [x.strip() for x in row]
            if not row or sub not in row[0].lower():
                continue
            color = COLORS[len(res) % len(COLORS)]
            rest = "".join(", " + x for x in row[1:])
            res.append(f'<p style="background:{color}"><b>{row[0]}</b>{rest}</p>')
        self.textBrowser.setHtml("".join(res))


def main():
    app = QApplication(sys.argv)
    w = CatBreeds()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
