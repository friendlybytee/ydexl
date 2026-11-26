import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фильтрация по жанрам")
        self.con = sqlite3.connect("films_db.sqlite")

        self.parameterSelection = QComboBox()
        self.parameterSelection.setObjectName("parameterSelection")
        for title, in self.con.execute("SELECT title FROM genres ORDER BY id"):
            self.parameterSelection.addItem(title)
        self.queryButton = QPushButton("Показать")
        self.queryButton.setObjectName("queryButton")
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Жанр", "Год выпуска"])

        layout = QVBoxLayout(self)
        layout.addWidget(self.parameterSelection)
        layout.addWidget(self.queryButton)
        layout.addWidget(self.tableWidget)

        self.queryButton.clicked.connect(self.show_films)
        self.fill(self.con.execute("SELECT title, genre, year FROM Films ORDER BY id").fetchall())

    def show_films(self):
        self.fill(self.con.execute("SELECT title, genre, year FROM Films WHERE genre = "
                                   "(SELECT id FROM genres WHERE title = ?) ORDER BY id",
                                   (self.parameterSelection.currentText(),)).fetchall())

    def fill(self, rows):
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
