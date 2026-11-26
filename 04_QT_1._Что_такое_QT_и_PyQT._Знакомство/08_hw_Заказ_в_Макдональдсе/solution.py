import sys

from PyQt6.QtWidgets import QApplication, QCheckBox, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заказ в Макдональдсе")
        lay = QVBoxLayout(self)
        self.menu_checkboxes = []
        for s in ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]:
            cb = QCheckBox(s)
            self.menu_checkboxes.append(cb)
            lay.addWidget(cb)
        self.order_btn = QPushButton("Заказать")
        self.order_btn.clicked.connect(self.order)
        lay.addWidget(self.order_btn)
        self.result = QPlainTextEdit()
        lay.addWidget(self.result)

    def order(self):
        lst = ["Ваш заказ:", ""]
        for cb in self.menu_checkboxes:
            if cb.isChecked():
                lst.append(cb.text())
        self.result.setPlainText("\n".join(lst))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MacOrder()
    w.show()
    sys.exit(app.exec())
