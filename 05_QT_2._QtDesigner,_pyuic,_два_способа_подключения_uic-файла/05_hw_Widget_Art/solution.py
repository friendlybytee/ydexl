import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


class WidgetArt(QWidget):
    def __init__(self, matrix):
        super().__init__()
        self.setWindowTitle("Widget Art")
        self.widgetArt = QGridLayout(self)
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                btn = QPushButton("*" if v == 1 else "")
                btn.setFixedSize(40, 40)
                self.widgetArt.addWidget(btn, i, j)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    ex = WidgetArt(matrix)
    ex.show()
    sys.exit(app.exec())
