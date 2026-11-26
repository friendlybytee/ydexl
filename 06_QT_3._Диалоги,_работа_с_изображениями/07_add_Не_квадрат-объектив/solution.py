import math
import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter, QPolygonF
from PyQt6.QtWidgets import (
    QApplication, QColorDialog, QLabel, QLineEdit, QPushButton, QWidget,
)


class NoTSquare(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Не квадрат-объектив")
        self.start_point = [350.0, 250.0]
        self.draw_flag = False
        self.color = QColor(0, 0, 0)

        QLabel("k", self).setGeometry(10, 10, 20, 25)
        QLabel("n", self).setGeometry(120, 10, 20, 25)
        QLabel("m", self).setGeometry(230, 10, 20, 25)
        self.k = QLineEdit("0.8", self)
        self.k.setGeometry(30, 10, 80, 25)
        self.n = QLineEdit("5", self)
        self.n.setGeometry(140, 10, 80, 25)
        self.m = QLineEdit("20", self)
        self.m.setGeometry(250, 10, 80, 25)
        self.draw = QPushButton("Рисовать", self)
        self.draw.setGeometry(350, 10, 100, 25)
        self.draw.clicked.connect(self.start)

    def start(self):
        self.color = QColorDialog().getColor()
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if not self.draw_flag:
            return
        k = float(self.k.text())
        n = int(self.n.text())
        m = int(self.m.text())
        pts = []
        for i in range(n):
            angle = 2 * math.pi * i / n
            pts.append((250 + 100 * math.cos(angle), 250 + 100 * math.sin(angle)))
        qp = QPainter(self)
        qp.setPen(self.color)
        for _ in range(m):
            poly = QPolygonF()
            for x, y in pts:
                poly.append(QPointF(x, y))
            qp.drawPolygon(poly)
            new = []
            for i in range(n):
                x1, y1 = pts[i]
                x2, y2 = pts[(i + 1) % n]
                new.append((x1 + (x2 - x1) * (1 - k), y1 + (y2 - y1) * (1 - k)))
            pts = new
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = NoTSquare()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
