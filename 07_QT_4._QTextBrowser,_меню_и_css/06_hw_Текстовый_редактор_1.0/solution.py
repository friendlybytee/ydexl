"""
Задача: Текстовый редактор 1.0
Категория: Домашняя работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Реализуйте на PyQT простой тестовый редактор, обладающий следующими функциями: открыть файл, создать новый файл, сохранить измененный файл.

* Кнопка **Создать новый** очищает виджеты, отображающие название файла и его содержимое.
* Кнопка **Сохранить файл** создает файл с указанным названием и записывает в него содержимое текстового поля. В случае, если такой файл уже существует, его содержимое перезаписывается на новое. Если название файла не указано, создавать файл не нужно.
* Кнопка **Открыть файл** проверяет, что указанный файл существует, и выводит его содержимое в текстовое поле, в противном случае ничего не происходит.

Класс `Notebook` должен определять методы `new_file`, `save_file`, `open_file`.

![notebook.gif](./statement-file.gif)

Класс, реализующий окно приложения, назовите `Notebook` и унаследуйте его от `QWidget`.  
 Кнопки назовите `new_button`, `save_button` и `open_button`.  
 Поле ввода названия файла назовите `filename_edit`, при этом используйте `QLineEdit`.  
 Поле ввода текста назовите `text_edit`, при этом используйте `QPlainTextEdit`.

"""

import os
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPlainTextEdit, QPushButton)


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        self.new_button = QPushButton("Создать новый")
        self.save_button = QPushButton("Сохранить файл")
        self.open_button = QPushButton("Открыть файл")
        self.filename_edit = QLineEdit()
        self.text_edit = QPlainTextEdit()
        lay = QVBoxLayout(self)
        row = QHBoxLayout()
        row.addWidget(self.new_button)
        row.addWidget(self.save_button)
        row.addWidget(self.open_button)
        lay.addLayout(row)
        lay.addWidget(self.filename_edit)
        lay.addWidget(self.text_edit)
        self.new_button.clicked.connect(self.new_file)
        self.save_button.clicked.connect(self.save_file)
        self.open_button.clicked.connect(self.open_file)

    def new_file(self):
        self.filename_edit.setText("")
        self.text_edit.setPlainText("")

    def save_file(self):
        name = self.filename_edit.text()
        if not name:
            return
        with open(name, "w", encoding="utf-8") as f:
            f.write(self.text_edit.toPlainText())

    def open_file(self):
        name = self.filename_edit.text()
        if not os.path.isfile(name):
            return
        with open(name, encoding="utf-8") as f:
            self.text_edit.setPlainText(f.read())


def main():
    app = QApplication(sys.argv)
    w = Notebook()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
