import csv
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem, QLineEdit)
from PyQt6.QtCore import Qt


class InteractiveReceipt(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Интерактивный чек")
        layout = QVBoxLayout(self)
        self.tableWidget = QTableWidget()
        self.total = QLineEdit()
        self.total.setReadOnly(True)
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.total)
        self.load()
        self.tableWidget.itemChanged.connect(self.recount)
        self.recount()

    def load(self):
        with open("price.csv", encoding="utf-8") as f:
            rows = list(csv.reader(f, delimiter=";"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Цена", "Количество"])
        self.tableWidget.setRowCount(len(rows) - 1)
        for i, r in enumerate(rows[1:]):
            for j in range(2):
                item = QTableWidgetItem(r[j])
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(i, j, item)
            self.tableWidget.setItem(i, 2, QTableWidgetItem("0"))

    def recount(self):
        s = 0
        for i in range(self.tableWidget.rowCount()):
            price = float(self.tableWidget.item(i, 1).text())
            try:
                count = int(self.tableWidget.item(i, 2).text())
            except ValueError:
                count = 0
            s += price * count
        self.total.setText(str(int(s)) if s == int(s) else str(s))


def main():
    app = QApplication(sys.argv)
    w = InteractiveReceipt()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
