import sys
from decimal import Decimal, getcontext

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget,
)

getcontext().prec = 60


def exp_text(n):
    m, e = ("%.2e" % n).split("e")
    return m + "e" + str(int(e))


def num_text(n):
    if n == n.to_integral_value():
        return str(int(n))
    return format(n.normalize(), "f")


def calc(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if b == 0:
        return None
    return a / b


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.resize(240, 370)

        self.secondary_label = QLabel()
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_label = QLabel()
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_label.setFont(QFont("Arial", 32))

        self.number_buttons = [self.make_button(str(i)) for i in range(10)]
        self.divide_button = self.make_button("/")
        self.multiply_button = self.make_button("*")
        self.substract_button = self.make_button("-")
        self.add_button = self.make_button("+")
        self.clear_button = self.make_button("C")
        self.clear_entry_button = self.make_button("CE")
        self.float_point_button = self.make_button(".")
        self.plus_minus_button = self.make_button("±")
        self.equals_button = self.make_button("=")

        for b in self.number_buttons:
            b.clicked.connect(self.on_digit)
        for b in (self.divide_button, self.multiply_button,
                  self.substract_button, self.add_button):
            b.clicked.connect(self.on_op)
        self.clear_button.clicked.connect(self.reset)
        self.clear_entry_button.clicked.connect(self.on_ce)
        self.float_point_button.clicked.connect(self.on_point)
        self.plus_minus_button.clicked.connect(self.on_sign)
        self.equals_button.clicked.connect(self.on_equals)

        d = self.number_buttons
        rows = [
            [d[7], d[8], d[9], self.divide_button],
            [d[4], d[5], d[6], self.multiply_button],
            [d[1], d[2], d[3], self.substract_button],
            [self.clear_button, d[0], self.clear_entry_button, self.add_button],
        ]
        grid = QGridLayout()
        grid.setSpacing(2)
        for i, row in enumerate(rows):
            for j, b in enumerate(row):
                grid.addWidget(b, i, j)
        grid.addWidget(self.float_point_button, 4, 0)
        grid.addWidget(self.plus_minus_button, 4, 1)
        grid.addWidget(self.equals_button, 4, 2, 1, 2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.secondary_label)
        layout.addWidget(self.main_label)
        layout.addLayout(grid, stretch=1)

        self.reset()

    def make_button(self, text):
        b = QPushButton(text, self)
        b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return b

    def reset(self):
        self.first = None
        self.op = None
        self.cur = "0"
        self.new = True
        self.err = False
        self.show_labels()

    def show_labels(self):
        if self.err:
            self.main_label.setText("ОШИБКА")
            self.secondary_label.setText("")
            return
        if len(self.cur) > 11:
            self.main_label.setText(exp_text(Decimal(self.cur)))
        else:
            self.main_label.setText(self.cur)
        if self.op is None:
            self.secondary_label.setText("")
            return
        s = num_text(self.first)
        if len(s.lstrip("-")) > 30:
            s = exp_text(self.first)
        self.secondary_label.setText(s + " " + self.op)

    def fail(self):
        self.reset()
        self.err = True
        self.show_labels()

    def skip_error(self):
        if self.err:
            self.reset()
            return True
        return False

    def on_digit(self):
        if self.err:
            self.reset()
        d = self.sender().text()
        if self.new or self.cur == "0":
            self.cur = d
        else:
            self.cur += d
        self.new = False
        self.show_labels()

    def on_point(self):
        if self.skip_error():
            return
        if self.new:
            self.cur = "0."
        elif "." not in self.cur:
            self.cur += "."
        self.new = False
        self.show_labels()

    def on_sign(self):
        if self.skip_error():
            return
        if Decimal(self.cur) == 0:
            return
        if self.cur.startswith("-"):
            self.cur = self.cur[1:]
        else:
            self.cur = "-" + self.cur
        self.new = False
        self.show_labels()

    def on_op(self):
        if self.skip_error():
            return
        if self.op is None:
            self.first = Decimal(self.cur)
        elif not self.new:
            res = calc(self.first, self.op, Decimal(self.cur))
            if res is None:
                self.fail()
                return
            self.first = res
        self.op = self.sender().text()
        self.cur = num_text(self.first)
        self.new = True
        self.show_labels()

    def on_equals(self):
        if self.skip_error():
            return
        if self.op is not None:
            res = calc(self.first, self.op, Decimal(self.cur))
            if res is None:
                self.fail()
                return
            self.cur = num_text(res)
            self.first = None
            self.op = None
        self.new = True
        self.show_labels()

    def on_ce(self):
        if self.skip_error():
            return
        self.cur = "0"
        self.new = True
        self.show_labels()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
