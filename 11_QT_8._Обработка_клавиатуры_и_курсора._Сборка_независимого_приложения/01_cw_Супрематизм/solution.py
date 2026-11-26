import sys
from random import randint
from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("Супрематизм")
        self.setMouseTracking(True)
        self.cur = QPointF(0, 0)
        self.shape = None

    def draw(self, shape, p):
        self.shape = shape
        self.c = p
        self.r = randint(20, 100)
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.update()

    def mouseMoveEvent(self, event):
        self.cur = event.position()

    def mousePressEvent(self, event):
        self.cur = event.position()
        if event.button() == Qt.MouseButton.LeftButton:
            self.draw("circle", self.cur)
        elif event.button() == Qt.MouseButton.RightButton:
            self.draw("square", self.cur)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.draw("triangle", self.cur)

    def paintEvent(self, event):
        if self.shape is None:
            return
        p = QPainter(self)
        p.setBrush(self.color)
        p.setPen(self.color)
        x, y, r = self.c.x(), self.c.y(), self.r
        if self.shape == "circle":
            p.drawEllipse(self.c, float(r), float(r))
        elif self.shape == "square":
            p.drawRect(QRectF(x - r / 2, y - r / 2, float(r), float(r)))
        else:
            d = r * 3 ** 0.5 / 2
            p.drawPolygon(QPolygonF([QPointF(x, y - r), QPointF(x + d, y + r / 2), QPointF(x - d, y + r / 2)]))
        p.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Suprematism()
    w.show()
    sys.exit(app.exec())
