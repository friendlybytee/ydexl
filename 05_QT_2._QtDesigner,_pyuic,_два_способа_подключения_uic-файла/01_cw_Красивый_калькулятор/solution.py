"""
Задача: Красивый калькулятор
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64.0 Мб

Условие:
Вам дан файл [calc.ui](./calc.ui), в котором реализован интерфейс красивого калькулятора. Изучите его, подключите к своей программе любым из способов и реализуйте все его функции. (Загружать этот файл вместе с решением не надо, изменять интерфейс тоже)

Класс, реализующий окно приложения, назовите **Calculator**

![prettycalc.gif](./markdown-image.gif)

Если какое-то выражение вычислить не получается (например, квадратный корень для отрицательного числа), должно выводиться соответствующее сообщение.

"""

import sys
from math import factorial, sqrt

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)
        self.text = ""
        self.a = None
        self.op = None
        for i in range(10):
            getattr(self, f"btn{i}").clicked.connect(self.add_char)
        self.btn_dot.clicked.connect(self.add_char)
        self.btn_plus.clicked.connect(self.set_op)
        self.btn_minus.clicked.connect(self.set_op)
        self.btn_mult.clicked.connect(self.set_op)
        self.btn_div.clicked.connect(self.set_op)
        self.btn_pow.clicked.connect(self.set_op)
        self.btn_eq.clicked.connect(self.equals)
        self.btn_sqrt.clicked.connect(self.unary)
        self.btn_fact.clicked.connect(self.unary)
        self.btn_clear.clicked.connect(self.clear)

    def show_text(self, s):
        self.text = s
        self.table.display(s)

    def add_char(self):
        ch = self.sender().text()
        if ch == "." and "." in self.text:
            return
        self.show_text(self.text + ch)

    def number(self):
        return float(self.text)

    def fmt(self, x):
        if x == int(x) and abs(x) < 1e15:
            return str(int(x))
        return str(x)

    def set_op(self):
        if self.text == "":
            return
        self.a = self.number()
        self.op = self.sender().text()
        self.text = ""
        self.table.display(0)

    def equals(self):
        if self.op is None or self.text == "":
            return
        b = self.number()
        try:
            if self.op == "+":
                r = self.a + b
            elif self.op == "-":
                r = self.a - b
            elif self.op == "*":
                r = self.a * b
            elif self.op == "/":
                r = self.a / b
            else:
                r = self.a ** b
            if isinstance(r, complex):
                raise ValueError
            self.show_text(self.fmt(r))
        except (ZeroDivisionError, ValueError, OverflowError):
            self.text = ""
            self.table.display("Error")
        self.op = None

    def unary(self):
        if self.text == "":
            return
        x = self.number()
        try:
            if self.sender() is self.btn_sqrt:
                r = sqrt(x)
            else:
                r = factorial(int(x)) if x == int(x) else 1 / 0
            self.show_text(self.fmt(r))
        except (ZeroDivisionError, ValueError, OverflowError):
            self.text = ""
            self.table.display("Error")

    def clear(self):
        self.a = None
        self.op = None
        self.show_text("")
        self.table.display(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    sys.exit(app.exec())
