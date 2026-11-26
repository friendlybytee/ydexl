"""
Задача: Псевдоним. Возвращение
Категория: Домашняя работа
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb

Условие:
Добавьте к программе «Псевдоним» графический пользовательский интерфейс на PyQT.

Напоминаем правила. Игра заключается в следующем: в одной куче лежит N камней, каждому из двух игроков разрешается по очереди брать не более 3 камней. Выигрывает тот, кто возьмёт последний. Количество камней должно задаваться перед началом новой игры.

Класс, реализующий окно приложения назовите **Pseudonym**.

![pseudonym.gif](./upload.gif)

Оставшееся количество камней на столе должно отображаться на экране в виджете **QLCDNumber**, который называется **remainLcd**. Для ввода количества камней в игре используйте **QSpinBox**, назовите этот виджет **stones**, кнопку для начала новой игры **startButton**. Поле ввода количества камней которое хочет взять пользователь назовите **takeInput**, кнопку для взятия камней из кучи **takeButton**. Отображение истории игры реализуйте с помощью **QListWidget**, назовите этот виджет **listWidget**.

В случае победы игрока выводите "Победа пользователя!" в виджет с названием **resultLabel**. При победе компьютера выводите "Победа компьютера!".

Ходы вашего ИИ не должны противоречить правилам игры.

"""

import sys

from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLCDNumber,
                             QLineEdit, QListWidget, QPushButton, QSpinBox,
                             QVBoxLayout, QWidget)


class Pseudonym(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Псевдоним")
        self.remain = 0
        self.stones = QSpinBox()
        self.stones.setRange(1, 1000)
        self.stones.setValue(20)
        self.startButton = QPushButton("Новая игра")
        self.remainLcd = QLCDNumber()
        self.takeInput = QLineEdit()
        self.takeButton = QPushButton("Взять")
        self.listWidget = QListWidget()
        self.resultLabel = QLabel("")
        self.startButton.clicked.connect(self.start)
        self.takeButton.clicked.connect(self.take)
        top = QHBoxLayout()
        top.addWidget(self.stones)
        top.addWidget(self.startButton)
        mid = QHBoxLayout()
        mid.addWidget(self.takeInput)
        mid.addWidget(self.takeButton)
        main = QVBoxLayout(self)
        main.addLayout(top)
        main.addWidget(self.remainLcd)
        main.addLayout(mid)
        main.addWidget(self.listWidget)
        main.addWidget(self.resultLabel)

    def start(self):
        self.remain = self.stones.value()
        self.remainLcd.display(self.remain)
        self.listWidget.clear()
        self.resultLabel.setText("")

    def take(self):
        if self.remain == 0:
            return
        text = self.takeInput.text()
        if not text.isdigit():
            return
        n = int(text)
        if n < 1 or n > 3 or n > self.remain:
            return
        self.takeInput.clear()
        self.remain -= n
        self.listWidget.addItem(f"Пользователь взял {n}, осталось {self.remain}")
        if self.remain == 0:
            self.finish("Победа пользователя!")
            return
        c = self.remain % 4
        if c == 0:
            c = 1
        self.remain -= c
        self.listWidget.addItem(f"Компьютер взял {c}, осталось {self.remain}")
        if self.remain == 0:
            self.finish("Победа компьютера!")
        self.remainLcd.display(self.remain)

    def finish(self, msg):
        self.remainLcd.display(0)
        self.resultLabel.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Pseudonym()
    w.show()
    sys.exit(app.exec())
