import csv
import random
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem, QPushButton)
from PyQt6.QtGui import QColor


class Expensive(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Осторожно: дорого")
        layout = QVBoxLayout(self)
        self.tableWidget = QTableWidget()
        self.updateButton = QPushButton("Обновить цвета")
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.updateButton)
        self.load()
        self.paint()
        self.updateButton.clicked.connect(self.paint)

    def load(self):
        with open("price.csv", encoding="utf-8") as f:
            rows = list(csv.reader(f, delimiter=";"))
        data = [(r[0], r[1]) for r in rows[1:]]
        data.sort(key=lambda r: float(r[1]), reverse=True)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Цена"])
        self.tableWidget.setRowCount(len(data))
        for i, r in enumerate(data):
            for j in range(2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(r[j]))

    def paint(self):
        n = self.tableWidget.rowCount()
        top = sorted({float(self.tableWidget.item(i, 1).text()) for i in range(n)}, reverse=True)[:5]
        for i in range(n):
            if float(self.tableWidget.item(i, 1).text()) in top:
                color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                for j in range(2):
                    self.tableWidget.item(i, j).setBackground(color)


def main():
    app = QApplication(sys.argv)
    w = Expensive()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
