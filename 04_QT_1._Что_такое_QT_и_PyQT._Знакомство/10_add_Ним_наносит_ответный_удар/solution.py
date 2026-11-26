import sys
from random import randint

from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLCDNumber, QPushButton, QWidget


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ним наносит ответный удар")
        lay = QGridLayout(self)
        self.result_label = QLabel()
        lay.addWidget(self.result_label, 0, 0, 1, 2)
        self.btnp = QPushButton()
        self.btnm = QPushButton()
        self.btnp.clicked.connect(self.plus)
        self.btnm.clicked.connect(self.minus)
        lay.addWidget(self.btnp, 1, 0)
        lay.addWidget(self.btnm, 1, 1)
        self.moves_lcd = QLCDNumber()
        self.x_lcd = QLCDNumber()
        lay.addWidget(QLabel("Осталось ходов"), 2, 0)
        lay.addWidget(self.moves_lcd, 2, 1)
        lay.addWidget(QLabel("Текущее число"), 3, 0)
        lay.addWidget(self.x_lcd, 3, 1)
        self.new_game()

    def new_game(self):
        self.X = randint(1, 50)
        self.Y = randint(1, 10)
        self.Z = randint(1, 10)
        self.moves = 10
        self.btnp.setText(f"+{self.Y}")
        self.btnm.setText(f"-{self.Z}")
        self.show_state()

    def show_state(self):
        self.moves_lcd.display(self.moves)
        self.x_lcd.display(self.X)

    def plus(self):
        self.step(self.Y)

    def minus(self):
        self.step(-self.Z)

    def step(self, d):
        self.X += d
        self.moves -= 1
        self.result_label.setText("")
        if self.X == 0:
            self.result_label.setText("Вы победили, начинаем новую игру")
            self.new_game()
        elif self.moves == 0:
            self.result_label.setText("Вы проиграли, начинаем новую игру")
            self.new_game()
        else:
            self.show_state()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NimStrikesBack()
    w.show()
    sys.exit(app.exec())
