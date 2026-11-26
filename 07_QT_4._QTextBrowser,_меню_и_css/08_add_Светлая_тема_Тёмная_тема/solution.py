"""
Задача: Светлая тема/Тёмная тема
Категория: Дополнительные задачи
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Напишите приложение на PyQT6, содержащее текстовый браузер (`textBrowser`), поле для ввода текста (`lineEdit`) и две кнопки (`pushButton` и `pushButton1`), оформление которого можно изменять по нажатию на вторую кнопку.

При загрузке окна тема тёмная, на второй кнопке написано **Светлая тема**. Если на неё нажать, то тема становится светлой, а надпись меняется на **Тёмная тема**.

Первая кнопка служит для отправки сообщений, написанных в поле ввода, в окно текстового браузера. Каждое сообщение предваряется текстом `Message: <введённый текст>` (Сообщение также можно отправить, нажав клавишу Enter на клавиатуре).

Класс, реализующий окно приложения, называется `MainWindow` и наследуется от `QMainWindow`, а так же должен содержать методы `send_message` и `change_theme`.

Задайте две глобальных константы со стилями для оформления тем:

* Тёмная тема: `dark_style`
* Светлая тема: `light_style`

Оформление светлой и тёмной темы вы можете выбрать самостоятельно, важно, чтобы оно находилось в глобальных константах, описанных выше.

![theme.gif](./statement-file.gif)

"""

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QTextBrowser)

dark_style = """
QMainWindow, QWidget { background-color: #2b2b2b; color: #ffffff; }
QTextBrowser, QLineEdit { background-color: #3c3f41; color: #ffffff; }
QPushButton { background-color: #4b4b4b; color: #ffffff; }
"""

light_style = """
QMainWindow, QWidget { background-color: #ffffff; color: #000000; }
QTextBrowser, QLineEdit { background-color: #f5f5f5; color: #000000; }
QPushButton { background-color: #e0e0e0; color: #000000; }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textBrowser = QTextBrowser()
        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("Отправить")
        self.pushButton1 = QPushButton("Светлая тема")
        central = QWidget()
        lay = QVBoxLayout(central)
        lay.addWidget(self.textBrowser)
        row = QHBoxLayout()
        row.addWidget(self.lineEdit)
        row.addWidget(self.pushButton)
        lay.addLayout(row)
        lay.addWidget(self.pushButton1)
        self.setCentralWidget(central)
        self.dark = True
        self.setStyleSheet(dark_style)
        self.pushButton.clicked.connect(self.send_message)
        self.lineEdit.returnPressed.connect(self.send_message)
        self.pushButton1.clicked.connect(self.change_theme)

    def send_message(self):
        self.textBrowser.append(f"Message: {self.lineEdit.text()}")
        self.lineEdit.clear()

    def change_theme(self):
        self.dark = not self.dark
        if self.dark:
            self.setStyleSheet(dark_style)
            self.pushButton1.setText("Светлая тема")
        else:
            self.setStyleSheet(light_style)
            self.pushButton1.setText("Тёмная тема")


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
