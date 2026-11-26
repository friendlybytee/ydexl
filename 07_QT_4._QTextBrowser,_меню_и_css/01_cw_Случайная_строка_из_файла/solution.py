"""
Задача: Случайная строка из файла
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Напишите интерфейс на PyQT — форма, наследник `QWidget` — для вывода случайной строки из файла `lines.txt` в `QTextBrowser`. Строку выводите заголовком первого уровня (тег h1).

Файл может быть пустым, тогда и выводить ничего не надо.

Класс, реализующий окно приложения, назовите `RandomString`. Кнопку — `button`, поле для вывода строки — `textBrowser`. Класс `RandomString` должен иметь определение метода `load_random_string`, который открывает файл и выводит содержимое в окно. В случае отсутствия файла нужно выводить пустую строку.

![random_string.gif](./statement-file.gif)

"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
import random


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Показать")
        self.textBrowser = QTextBrowser()
        lay = QVBoxLayout(self)
        lay.addWidget(self.button)
        lay.addWidget(self.textBrowser)
        self.button.clicked.connect(self.load_random_string)

    def load_random_string(self):
        try:
            with open("lines.txt", encoding="utf-8") as f:
                lst = f.read().splitlines()
        except OSError:
            lst = []
        if lst:
            self.textBrowser.setHtml(f"<h1>{random.choice(lst)}</h1>")
        else:
            self.textBrowser.setHtml("")


def main():
    app = QApplication(sys.argv)
    w = RandomString()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
