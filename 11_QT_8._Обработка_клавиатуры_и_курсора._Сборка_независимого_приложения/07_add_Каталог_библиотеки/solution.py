import sys
import os
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox,
                             QTableWidget, QTableWidgetItem, QLabel)

DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(DIR, "library.sqlite")


def create_db():
    if os.path.exists(DB):
        return
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, genre TEXT, image TEXT)")
    con.executemany("INSERT INTO books (title, author, year, genre, image) VALUES (?, ?, ?, ?, ?)", [
        ("Война и мир", "Лев Толстой", 1869, "Роман", "images/war_and_peace.png"),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", "images/anna_karenina.png"),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", ""),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "images/master.png"),
        ("Евгений Онегин", "Александр Пушкин", 1833, "Поэма", ""),
    ])
    con.commit()
    con.close()


class Library(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каталог библиотеки")
        self.resize(800, 450)
        self.mode = QComboBox()
        self.mode.addItems(["По названию", "По автору"])
        self.search = QLineEdit()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Название", "Автор", "Год", "Жанр"])
        self.info = QLabel()
        self.picture = QLabel()
        self.picture.setFixedSize(200, 280)

        top = QHBoxLayout()
        top.addWidget(self.mode)
        top.addWidget(self.search)
        side = QVBoxLayout()
        side.addWidget(self.picture)
        side.addWidget(self.info)
        mid = QHBoxLayout()
        mid.addWidget(self.table, 1)
        mid.addLayout(side)
        lay = QVBoxLayout(self)
        lay.addLayout(top)
        lay.addLayout(mid)

        self.search.textChanged.connect(self.load)
        self.mode.currentIndexChanged.connect(self.load)
        self.table.currentCellChanged.connect(self.show_info)
        self.load()

    def load(self):
        con = sqlite3.connect(DB)
        data = con.execute("SELECT title, author, year, genre, image FROM books").fetchall()
        con.close()
        k = self.mode.currentIndex()
        t = self.search.text().lower()
        self.rows = [r for r in data if t in r[k].lower()]
        self.table.setRowCount(len(self.rows))
        for i, r in enumerate(self.rows):
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(r[j])))
        self.table.resizeColumnsToContents()
        self.show_info(self.table.currentRow())

    def show_info(self, i, *args):
        if not 0 <= i < len(self.rows):
            self.info.setText("")
            self.picture.clear()
            return
        title, author, year, genre, image = self.rows[i]
        self.info.setText(f"{title}\n{author}\n{year}, {genre}")
        pix = QPixmap(os.path.join(DIR, image)) if image else QPixmap()
        if pix.isNull():
            pix = QPixmap(200, 280)
            pix.fill(QColor("lightgray"))
        self.picture.setPixmap(pix.scaled(200, 280, Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == "__main__":
    create_db()
    app = QApplication(sys.argv)
    w = Library()
    w.show()
    sys.exit(app.exec())
