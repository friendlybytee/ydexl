import sys

from PyQt6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLineEdit, QPlainTextEdit,
                             QPushButton, QWidget)

MENU = {"Чизбургер": 10, "Гамбургер": 20, "Кока-кола": 15, "Наггетсы": 30}


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заказ в Макдональдсе 2")
        lay = QGridLayout(self)
        self.checkboxes = []
        self.inputs = []
        for i, s in enumerate(MENU):
            cb = QCheckBox(s)
            cb.toggled.connect(self.toggle)
            e = QLineEdit("0")
            self.checkboxes.append(cb)
            self.inputs.append(e)
            lay.addWidget(cb, i, 0)
            lay.addWidget(e, i, 1)
        self.orderButton = QPushButton("Заказать")
        self.orderButton.clicked.connect(self.make_order)
        lay.addWidget(self.orderButton, 4, 0)
        self.order = QPlainTextEdit()
        lay.addWidget(self.order, 5, 0, 1, 2)

    def toggle(self, on):
        i = self.checkboxes.index(self.sender())
        self.inputs[i].setText("1" if on else "0")

    def make_order(self):
        lst = ["Ваш заказ", ""]
        s = 0
        for i in range(4):
            if self.checkboxes[i].isChecked():
                name = self.checkboxes[i].text()
                n = int(self.inputs[i].text())
                p = n * MENU[name]
                s += p
                lst.append(f"{name}-----{n}-----{p}")
        lst.append("")
        lst.append(f"Итого: {s}")
        self.order.setPlainText("\n".join(lst))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
