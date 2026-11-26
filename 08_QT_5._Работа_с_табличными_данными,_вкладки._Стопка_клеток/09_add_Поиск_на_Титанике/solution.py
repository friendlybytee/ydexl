import csv
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableWidget,
                             QTableWidgetItem, QLineEdit)
from PyQt6.QtGui import QColor


class TitanicSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск на Титанике")
        layout = QVBoxLayout(self)
        self.searchEdit = QLineEdit()
        self.resultTable = QTableWidget()
        layout.addWidget(self.searchEdit)
        layout.addWidget(self.resultTable)

        with open("titanic.csv", encoding="utf-8") as f:
            data = list(csv.reader(f))
        self.headers = data[0]
        self.rows = data[1:]
        self.searchEdit.textChanged.connect(self.show_rows)
        self.show_rows()

    def show_rows(self):
        text = self.searchEdit.text().lower()
        rows = self.rows
        if len(text) >= 3:
            rows = [r for r in rows if text in r[1].lower()]
        self.resultTable.setColumnCount(len(self.headers))
        self.resultTable.setHorizontalHeaderLabels(self.headers)
        self.resultTable.setRowCount(len(rows))
        for i, r in enumerate(rows):
            color = QColor("#00FF00") if r[5] == "1" else QColor("#FF0000")
            for j, v in enumerate(r):
                item = QTableWidgetItem(v)
                item.setBackground(color)
                self.resultTable.setItem(i, j, item)


def main():
    app = QApplication(sys.argv)
    w = TitanicSearch()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
