import sys

from PyQt6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton, QRadioButton,
                             QWidget)


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики-нолики")
        lay = QGridLayout(self)
        self.x_radio = QRadioButton("X")
        self.o_radio = QRadioButton("O")
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.new_game)
        lay.addWidget(self.x_radio, 0, 0)
        lay.addWidget(self.o_radio, 0, 1)
        self.button_grid = []
        for i in range(3):
            row = []
            for j in range(3):
                b = QPushButton()
                b.setFixedSize(50, 50)
                b.clicked.connect(lambda _, i=i, j=j: self.move(i, j))
                lay.addWidget(b, i + 1, j)
                row.append(b)
            self.button_grid.append(row)
        self.result = QLabel()
        lay.addWidget(self.result, 4, 0, 1, 3)
        self.new_game_button = QPushButton("Новая игра")
        self.new_game_button.clicked.connect(self.new_game)
        lay.addWidget(self.new_game_button, 5, 0, 1, 3)
        self.new_game()

    def new_game(self):
        self.turn = "X" if self.x_radio.isChecked() else "O"
        for row in self.button_grid:
            for b in row:
                b.setText("")
                b.setEnabled(True)
        self.result.setText("")

    def move(self, i, j):
        b = self.button_grid[i][j]
        if b.text():
            return
        b.setText(self.turn)
        g = [[x.text() for x in row] for row in self.button_grid]
        lines = g + [list(c) for c in zip(*g)]
        lines.append([g[k][k] for k in range(3)])
        lines.append([g[k][2 - k] for k in range(3)])
        if [self.turn] * 3 in lines:
            self.result.setText(f"Выиграл {self.turn}!")
            for row in self.button_grid:
                for x in row:
                    x.setEnabled(False)
        elif all(all(row) for row in g):
            self.result.setText("Ничья!")
        self.turn = "O" if self.turn == "X" else "X"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TicTacToe()
    w.show()
    sys.exit(app.exec())
