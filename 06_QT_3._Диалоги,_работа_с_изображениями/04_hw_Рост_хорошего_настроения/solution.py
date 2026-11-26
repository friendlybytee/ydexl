import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QSlider, QWidget


class GoodMoodRising(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("Рост хорошего настроения")
        self.color = QColor(255, 200, 0)
        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setGeometry(970, 40, 20, 500)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        s = self.slider.value()
        qp = QPainter(self)
        qp.setPen(self.color)
        qp.drawEllipse(0, 0, 10 * s, 10 * s)
        qp.drawEllipse(2 * s, 2 * s, 2 * s, 2 * s)
        qp.drawEllipse(6 * s, 2 * s, 2 * s, 2 * s)
        qp.drawArc(2 * s, 6 * s, 6 * s, 2 * s, -480, -1920)
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = GoodMoodRising()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
