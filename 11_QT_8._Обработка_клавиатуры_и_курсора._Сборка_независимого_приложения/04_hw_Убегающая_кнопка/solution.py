import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle("Убегающая кнопка")
        self.setMouseTracking(True)
        self.button = QPushButton("Нажми", self)
        self.button.setMouseTracking(True)
        self.button.move(150, 120)

    def mouseMoveEvent(self, event):
        x = event.position().x()
        y = event.position().y()
        b = self.button
        if b.x() - 30 <= x <= b.x() + b.width() + 30 and b.y() - 30 <= y <= b.y() + b.height() + 30:
            for _ in range(100):
                nx = randint(0, self.width() - b.width())
                ny = randint(0, self.height() - b.height())
                if nx - 30 > x or nx + b.width() + 30 < x or ny - 30 > y or ny + b.height() + 30 < y:
                    break
            b.move(nx, ny)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
