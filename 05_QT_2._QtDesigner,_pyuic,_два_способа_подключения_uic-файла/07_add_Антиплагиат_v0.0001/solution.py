"""
Задача: Антиплагиат v0.0001
Категория: Дополнительные задачи
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb

Условие:
Напишите программу с графическим интерфейсом на PyQT с использованием Layout, которая реализует простейшую проверку на антиплагиат. На форме приложения должно содержаться:

Виджет **QDoubleSpinBox** для задания порога срабатывания антиплагиата, назовите его **alert\_value**. Два **QPlainTextEdit** для ввода текста. Назовите их **text1** и **text2**. Кнопка для расчета результата, которая должна называться **checkBtn**. Для вывода результата сравнения используйте виджет **QStatusBar**, который уже есть в классе **QMainWindow**, он называется **statusbar**. Для получения доступа к этому виджету используйте метод **statusBar** класса **QMainWindow**. Класс, реализующий окно приложения назовите **AntiPlagiarism**, унаследуйте его от класса **QMainWindow**.

![antiplagiarism.gif](./upload.gif)

В качестве значения похожести текстов используйте отношения количества уникальных строк, встречающихся в обоих текстах, к общему количеству уникальных строк (в процентах, с точностью до 2 знаков после запятой).

Примеры сообщений, которые должны выводится в результате проверки на плагиат:

"Тексты похожи на 50.01%, плагиат"  
"Тексты похожи на 1.01%, не плагиат"

"""

import sys

from PyQt6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout,
                             QMainWindow, QPlainTextEdit, QPushButton,
                             QVBoxLayout, QWidget)


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Антиплагиат")
        self.alert_value = QDoubleSpinBox()
        self.alert_value.setRange(0, 100)
        self.alert_value.setValue(50)
        self.text1 = QPlainTextEdit()
        self.text2 = QPlainTextEdit()
        self.checkBtn = QPushButton("Проверить")
        self.checkBtn.clicked.connect(self.check)
        texts = QHBoxLayout()
        texts.addWidget(self.text1)
        texts.addWidget(self.text2)
        main = QVBoxLayout()
        main.addWidget(self.alert_value)
        main.addLayout(texts)
        main.addWidget(self.checkBtn)
        central = QWidget()
        central.setLayout(main)
        self.setCentralWidget(central)

    def check(self):
        a = set(self.text1.toPlainText().split("\n"))
        b = set(self.text2.toPlainText().split("\n"))
        total = len(a | b)
        p = len(a & b) / total * 100
        if p >= self.alert_value.value():
            msg = f"Тексты похожи на {p:.2f}%, плагиат"
        else:
            msg = f"Тексты похожи на {p:.2f}%, не плагиат"
        self.statusBar().showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AntiPlagiarism()
    w.show()
    sys.exit(app.exec())
