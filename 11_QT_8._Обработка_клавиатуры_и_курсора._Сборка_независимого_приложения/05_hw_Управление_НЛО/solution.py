import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

DIR = os.path.dirname(os.path.abspath(__file__))


class UfoControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Управление НЛО")
        self.ufo = QLabel(self)
        pix = QPixmap(os.path.join(DIR, "ufo.png"))
        self.ufo.setPixmap(pix)
        self.ufo.resize(pix.size())
        self.ufo.move(0, 0)

    def keyPressEvent(self, event):
        x = self.ufo.x()
        y = self.ufo.y()
        key = event.key()
        if key == Qt.Key.Key_Left:
            x -= 10
        elif key == Qt.Key.Key_Right:
            x += 10
        elif key == Qt.Key.Key_Up:
            y -= 10
        elif key == Qt.Key.Key_Down:
            y += 10
        else:
            return
        if x < 0:
            x = 250
        if x > 250:
            x = 0
        if y < 0:
            y = 250
        if y > 250:
            y = 0
        self.ufo.move(x, y)


def main():
    app = QApplication(sys.argv)
    w = UfoControl()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
