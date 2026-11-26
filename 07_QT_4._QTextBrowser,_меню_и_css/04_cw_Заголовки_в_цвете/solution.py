"""
Задача: Заголовки в цвете
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Напишите приложение на PyQT для вывода введённых пользователем строк с заданным им оформлением html.

Класс, реализующий окно приложения, назовите `HeadersInColor` (он наследуется от `QMainWindow`).

Окно приложения должно содержать:

* `lineEdit` (`QLineEdit`) для ввода строки;
* `comboBox` (`QComboBox`) — выпадающий список — уровень заголовка (от h1 до h6 или p, по умолчанию — просто абзац p);
* `lineEdit_2` (`QLineEdit`) для ввода цвета текста (по умолчанию чёрный);
* `pushButton` — кнопку Вывести для вывода отформатированного текста в окне `QTextBrowser`, каждая следующая строка добавляется к общему тексту;
* `pushButton_2` — кнопку Очистить, чтобы очистить поле вывода, все введённые строки стираются из памяти;
* `textBrowser` (`QTextBrowser`) — для вывода текста.

Класс должен реализовывать методы `write_text` и `clear_text`. А так же иметь дополнительные атрибут - `text`, список заголовков.

![headers_colored.gif](./statement-file.gif)

"""

import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit,
                             QComboBox, QPushButton, QTextBrowser)


class HeadersInColor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = []
        self.lineEdit = QLineEdit()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["h1", "h2", "h3", "h4", "h5", "h6", "p"])
        self.comboBox.setCurrentText("p")
        self.lineEdit_2 = QLineEdit("black")
        self.pushButton = QPushButton("Вывести")
        self.pushButton_2 = QPushButton("Очистить")
        self.textBrowser = QTextBrowser()
        central = QWidget()
        lay = QVBoxLayout(central)
        for w in (self.lineEdit, self.comboBox, self.lineEdit_2, self.pushButton,
                  self.pushButton_2, self.textBrowser):
            lay.addWidget(w)
        self.setCentralWidget(central)
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)

    def write_text(self):
        tag = self.comboBox.currentText()
        color = self.lineEdit_2.text().strip() or "black"
        self.text.append(f'<{tag} style="color:{color}">{self.lineEdit.text()}</{tag}>')
        self.textBrowser.setHtml("".join(self.text))

    def clear_text(self):
        self.text = []
        self.textBrowser.setHtml("")


def main():
    app = QApplication(sys.argv)
    w = HeadersInColor()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
