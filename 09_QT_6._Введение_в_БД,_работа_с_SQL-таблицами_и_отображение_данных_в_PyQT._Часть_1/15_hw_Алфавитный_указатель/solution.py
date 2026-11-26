import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow, QPushButton, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget,
)

LETTERS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Алфавитный указатель")
        self.con = sqlite3.connect("films_db.sqlite")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        grid = QGridLayout()
        layout.addLayout(grid)

        self.buttons = []
        for i, letter in enumerate(LETTERS):
            b = QPushButton(letter)
            b.clicked.connect(lambda checked, l=letter: self.show_films(l))
            grid.addWidget(b, i // 11, i % 11)
            self.buttons.append(b)

        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Название", "Год", "Жанр", "Продолжительность"])
        layout.addWidget(self.tableWidget)

    def show_films(self, letter):
        query = (
            "SELECT f.id, f.title, f.year, g.title, f.duration "
            "FROM Films f JOIN genres g ON g.id = f.genre "
            "WHERE f.title LIKE ? ORDER BY f.id"
        )
        rows = self.con.execute(query, (letter + "%",)).fetchall()
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))
        if rows:
            self.statusBar().showMessage(f"Нашлось {len(rows)} записей")
        else:
            self.statusBar().showMessage("К сожалению, ничего не нашлось")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
