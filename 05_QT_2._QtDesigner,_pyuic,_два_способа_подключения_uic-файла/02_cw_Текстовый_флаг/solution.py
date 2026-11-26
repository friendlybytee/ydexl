import sys

from PyQt6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
                             QPushButton, QRadioButton, QVBoxLayout, QWidget)

COLORS = ["Синий", "Красный", "Зелёный"]


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 250)
        self.setWindowTitle("Текстовый флаг")
        self.groups = []
        main = QVBoxLayout(self)
        row = QHBoxLayout()
        for i in range(3):
            group = QButtonGroup(self)
            setattr(self, f"color_group_{i + 1}", group)
            self.groups.append(group)
            col = QVBoxLayout()
            for name in COLORS:
                btn = QRadioButton(name)
                group.addButton(btn)
                col.addWidget(btn)
            group.buttons()[0].setChecked(True)
            row.addLayout(col)
        main.addLayout(row)
        self.make_flag = QPushButton("Сделать флаг")
        self.make_flag.clicked.connect(self.make)
        main.addWidget(self.make_flag)
        self.result = QLabel("")
        main.addWidget(self.result)

    def make(self):
        names = [g.checkedButton().text() for g in self.groups]
        self.result.setText(", ".join(names))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FlagMaker()
    w.show()
    sys.exit(app.exec())
