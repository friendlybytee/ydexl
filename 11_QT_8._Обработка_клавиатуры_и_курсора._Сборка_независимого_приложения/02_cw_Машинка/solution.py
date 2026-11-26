import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

DIR = os.path.dirname(os.path.abspath(__file__))
NAMES = ["car1.png", "car2.png", "car3.png"]


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Машинка")
        self.setMouseTracking(True)
        self.n = 0
        self.pixmap = QPixmap(os.path.join(DIR, NAMES[0]))
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.resize(self.pixmap.size())
        self.lbl.setMouseTracking(True)
        self.lbl.move(0, 0)

    def mouseMoveEvent(self, event):
        x = int(event.position().x())
        y = int(event.position().y())
        if x <= 250 and y <= 250:
            self.lbl.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.n = (self.n + 1) % 3
            self.pixmap = QPixmap(os.path.join(DIR, NAMES[self.n]))
            self.lbl.setPixmap(self.pixmap)
            self.lbl.resize(self.pixmap.size())


def main():
    app = QApplication(sys.argv)
    w = Car()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
