import csv
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QComboBox, QPushButton)


class OlympResult(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Результаты олимпиады")
        layout = QVBoxLayout(self)
        top = QHBoxLayout()
        self.schools = QComboBox()
        self.classes = QComboBox()
        self.resultButton = QPushButton("Показать")
        top.addWidget(self.schools)
        top.addWidget(self.classes)
        top.addWidget(self.resultButton)
        self.tableWidget = QTableWidget()
        layout.addLayout(top)
        layout.addWidget(self.tableWidget)

        with open("rez.csv", encoding="utf-8") as f:
            data = list(csv.reader(f))
        self.rows = data[1:]
        self.schools.addItem("Все")
        self.schools.addItems(sorted({r[2].split("-")[2] for r in self.rows}, key=int))
        self.schools.currentIndexChanged.connect(self.fill_classes)
        self.fill_classes()
        self.resultButton.clicked.connect(self.show_rows)

    def fill_classes(self):
        s = self.schools.currentText()
        self.classes.clear()
        self.classes.addItem("Все")
        self.classes.addItems(sorted({r[2].split("-")[3] for r in self.rows if s in ("Все", r[2].split("-")[2])}, key=int))

    def show_rows(self):
        school = self.schools.currentText()
        cls = self.classes.currentText()
        rows = []
        for r in self.rows:
            p = r[2].split("-")
            if school != "Все" and p[2] != school:
                continue
            if cls != "Все" and p[3] != cls:
                continue
            rows.append((r[1].split()[3], r[7]))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Результат"])
        self.tableWidget.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j, v in enumerate(r):
                self.tableWidget.setItem(i, j, QTableWidgetItem(v))


def main():
    app = QApplication(sys.argv)
    w = OlympResult()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
