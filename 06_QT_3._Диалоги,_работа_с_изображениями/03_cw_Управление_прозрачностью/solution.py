import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QSlider, QWidget


class AlphaManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Управление прозрачностью")
        self.orig = QPixmap("orig.jpg")
        self.pixmap = QPixmap(self.orig)
        w = self.orig.width()
        h = self.orig.height()
        self.setFixedSize(w + 55, h + 20)

        self.label = QLabel(self)
        self.label.setGeometry(45, 10, w, h)
        self.alpha = QSlider(Qt.Orientation.Vertical, self)
        self.alpha.setGeometry(10, 10, 25, h)
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)
        self.alpha.valueChanged.connect(self.change)
        self.change()

    def change(self):
        image = QImage("orig.jpg").convertToFormat(QImage.Format.Format_ARGB32)
        v = self.alpha.value()
        for x in range(image.width()):
            for y in range(image.height()):
                c = image.pixelColor(x, y)
                c.setAlpha(v)
                image.setPixelColor(x, y, c)
        image.save("new.png")
        self.pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(self.pixmap)


def main():
    app = QApplication(sys.argv)
    w = AlphaManagement()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
