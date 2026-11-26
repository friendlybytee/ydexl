import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Арифмометр")
        self.first_value = QLineEdit("0")
        self.add_button = QPushButton("+")
        self.substract_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.second_value = QLineEdit("0")
        self.result = QLineEdit("0")
        self.result.setReadOnly(True)
        self.add_button.clicked.connect(self.calc)
        self.substract_button.clicked.connect(self.calc)
        self.multiply_button.clicked.connect(self.calc)
        lay = QHBoxLayout(self)
        lay.addWidget(self.first_value)
        lay.addWidget(self.add_button)
        lay.addWidget(self.substract_button)
        lay.addWidget(self.multiply_button)
        lay.addWidget(self.second_value)
        lay.addWidget(QLabel("="))
        lay.addWidget(self.result)

    def calc(self):
        a = int(self.first_value.text())
        b = int(self.second_value.text())
        op = self.sender().text()
        if op == "+":
            r = a + b
        elif op == "-":
            r = a - b
        else:
            r = a * b
        self.result.setText(str(r))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Arifmometr()
    w.show()
    sys.exit(app.exec())
