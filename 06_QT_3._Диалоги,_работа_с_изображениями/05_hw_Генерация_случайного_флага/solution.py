import random
import sys

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QInputDialog, QPushButton, QWidget


class RandomFlag(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 400)
        self.setWindowTitle("Случайный флаг")
        self.base = [80, 80, 120, 30]
        self.colors = []
        self.button = QPushButton("Создать флаг", self)
        self.button.setGeometry(20, 20, 260, 30)
        self.button.clicked.connect(self.make_flag)

    def make_flag(self):
        n, ok = QInputDialog.getInt(self, "Флаг", "Количество цветов", 3, 1, 10, 1)
        if not ok:
            return
        self.colors = []
        for _ in range(n):
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            self.colors.append(QColor(r, g, b))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        x, y, w, h = self.base
        for c in self.colors:
            qp.setBrush(c)
            qp.drawRect(x, y, w, h)
            y += h
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = RandomFlag()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
