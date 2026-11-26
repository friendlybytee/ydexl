"""
Задача: Перемешивание
Категория: Домашняя работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
В папке с вашей программой лежит текстовый файл `lines.txt`. Ваша задача — написать приложение на PyQT6 для вывода строк из этого файла в поле `QTextBrowser` по нажатию на кнопку: сначала выводятся все чётные строки, а потом — все нечётные. Первая строка считается нечётной.

![shuffle.gif](./statement-file.gif)

Класс, реализующий окно приложения, назовите `Shuffle` и унаследуйте от `QWidget`, кнопку назовите `button`, текстовое поле — `text_field`, а так же метод открытия файла `load_strings`.

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser


class Shuffle(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Перемешать")
        self.text_field = QTextBrowser()
        lay = QVBoxLayout(self)
        lay.addWidget(self.button)
        lay.addWidget(self.text_field)
        self.button.clicked.connect(self.load_strings)

    def load_strings(self):
        try:
            with open("lines.txt", encoding="utf-8") as f:
                lst = f.read().splitlines()
        except OSError:
            lst = []
        res = lst[1::2] + lst[0::2]
        self.text_field.setPlainText("\n".join(res))


def main():
    app = QApplication(sys.argv)
    w = Shuffle()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
