import sys

from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QColor, QPainter, QPolygonF
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class Square2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Квадрат-объектив — 2")
        self.color = QColor(255, 0, 0)
        self.draw_flag = False

        QLabel("k", self).setGeometry(10, 10, 20, 25)
        QLabel("n", self).setGeometry(150, 10, 20, 25)
        self.k = QLineEdit("0.8", self)
        self.k.setGeometry(30, 10, 100, 25)
        self.n = QLineEdit("20", self)
        self.n.setGeometry(170, 10, 100, 25)
        self.draw = QPushButton("Рисовать", self)
        self.draw.setGeometry(300, 10, 100, 25)
        self.draw.clicked.connect(self.start)

    def start(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if not self.draw_flag:
            return
        k = float(self.k.text())
        n = int(self.n.text())
        pts = [(150.0, 150.0), (350.0, 150.0), (350.0, 350.0), (150.0, 350.0)]
        qp = QPainter(self)
        qp.setPen(self.color)
        for _ in range(n):
            poly = QPolygonF()
            for x, y in pts:
                poly.append(QPointF(x, y))
            qp.drawPolygon(poly)
            new = []
            for i in range(4):
                x1, y1 = pts[i]
                x2, y2 = pts[(i + 1) % 4]
                new.append((x1 + (x2 - x1) * (1 - k), y1 + (y2 - y1) * (1 - k)))
            pts = new
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = Square2()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
