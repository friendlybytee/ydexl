import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычисление выражений")
        self.first_value = QLineEdit()
        self.trick_button = QPushButton("->")
        self.second_value = QLineEdit()
        self.trick_button.clicked.connect(self.run)
        lay = QGridLayout(self)
        lay.addWidget(QLabel("Выражение:"), 0, 0)
        lay.addWidget(QLabel("Результат:"), 0, 2)
        lay.addWidget(self.first_value, 1, 0)
        lay.addWidget(self.trick_button, 1, 1)
        lay.addWidget(self.second_value, 1, 2)

    def run(self):
        self.second_value.setText(str(eval(self.first_value.text())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Evaluator()
    w.show()
    sys.exit(app.exec())
