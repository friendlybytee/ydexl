import sys

from PyQt6.QtWidgets import (QApplication, QGridLayout, QLabel, QLCDNumber, QLineEdit,
                             QPushButton, QWidget)


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Миникалькулятор")
        self.number_1 = QLineEdit()
        self.number_2 = QLineEdit()
        self.calculate_button = QPushButton("->")
        self.calculate_button.clicked.connect(self.calc)
        self.result_sum = QLCDNumber()
        self.result_sub = QLCDNumber()
        self.result_mul = QLCDNumber()
        self.result_div = QLCDNumber()
        lay = QGridLayout(self)
        lay.addWidget(QLabel("Первое число(целое):"), 0, 0)
        lay.addWidget(self.number_1, 1, 0)
        lay.addWidget(QLabel("Второе число(целое):"), 2, 0)
        lay.addWidget(self.number_2, 3, 0)
        lay.addWidget(self.calculate_button, 1, 1)
        names = ["Сумма:", "Разность:", "Произведение:", "Частное:"]
        lcds = [self.result_sum, self.result_sub, self.result_mul, self.result_div]
        for i in range(4):
            lay.addWidget(QLabel(names[i]), i, 2)
            lay.addWidget(lcds[i], i, 3)

    def calc(self):
        a = int(self.number_1.text())
        b = int(self.number_2.text())
        self.result_sum.display(a + b)
        self.result_sub.display(a - b)
        self.result_mul.display(a * b)
        if b == 0:
            self.result_div.display("Error")
        else:
            self.result_div.display(str(round(a / b, 3)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiniCalculator()
    w.show()
    sys.exit(app.exec())
