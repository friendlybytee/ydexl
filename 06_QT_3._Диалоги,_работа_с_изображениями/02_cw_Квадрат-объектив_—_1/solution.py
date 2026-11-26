import sys

from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 900)
        self.setWindowTitle("Квадрат-объектив — 1")
        self.color = QColor(200, 0, 0)
        self.draw_flag = False

        QLabel("a", self).setGeometry(10, 10, 30, 25)
        QLabel("k", self).setGeometry(210, 10, 30, 25)
        QLabel("n", self).setGeometry(410, 10, 30, 25)
        self.lineEdit = QLineEdit("300", self)
        self.lineEdit.setGeometry(40, 10, 150, 25)
        self.lineEdit_2 = QLineEdit("0.9", self)
        self.lineEdit_2.setGeometry(240, 10, 150, 25)
        self.lineEdit_3 = QLineEdit("10", self)
        self.lineEdit_3.setGeometry(440, 10, 150, 25)
        self.btn = QPushButton("Рисовать", self)
        self.btn.setGeometry(620, 10, 150, 25)
        self.btn.clicked.connect(self.start)

    def start(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if not self.draw_flag:
            return
        a = float(self.lineEdit.text())
        k = float(self.lineEdit_2.text())
        n = int(self.lineEdit_3.text())
        qp = QPainter(self)
        qp.setPen(self.color)
        cx = 50 + a / 2
        cy = 130 + a / 2
        for _ in range(n):
            qp.drawRect(QRectF(cx - a / 2, cy - a / 2, a, a))
            a *= k
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = Square1()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
