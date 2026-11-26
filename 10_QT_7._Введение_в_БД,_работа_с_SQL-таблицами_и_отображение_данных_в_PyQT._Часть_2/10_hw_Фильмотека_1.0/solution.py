import sqlite3
import sys
from datetime import date
from PyQt6.QtWidgets import (QApplication, QComboBox, QMainWindow, QPlainTextEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QWidget)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 450)
        self.setWindowTitle("Фильмотека")
        w = QWidget(self)
        self.setCentralWidget(w)
        self.addButton = QPushButton("Добавить", w)
        self.addButton.setGeometry(10, 10, 120, 30)
        self.tableWidget = QTableWidget(w)
        self.tableWidget.setGeometry(10, 50, 680, 380)
        self.con = sqlite3.connect("films_db.sqlite")
        self.add_form = None
        self.addButton.clicked.connect(self.adding)
        self.update_result()

    def update_result(self):
        rows = self.con.execute("SELECT films.id, films.title, films.year, genres.title, films.duration FROM films "
                                "LEFT JOIN genres ON films.genre = genres.id ORDER BY films.id DESC").fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ИД", "Название", "Год", "Жанр", "Длительность"])
        self.tableWidget.setRowCount(len(rows))
        for i, r in enumerate(rows):
            for j, v in enumerate(r):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()


class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 250)
        self.setWindowTitle("Добавление фильма")
        w = QWidget(self)
        self.setCentralWidget(w)
        self.title = QPlainTextEdit(w)
        self.title.setGeometry(10, 10, 280, 30)
        self.year = QPlainTextEdit(w)
        self.year.setGeometry(10, 50, 280, 30)
        self.duration = QPlainTextEdit(w)
        self.duration.setGeometry(10, 90, 280, 30)
        self.comboBox = QComboBox(w)
        self.comboBox.setGeometry(10, 130, 280, 30)
        self.pushButton = QPushButton("Добавить", w)
        self.pushButton.setGeometry(10, 170, 280, 30)
        self.con = sqlite3.connect("films_db.sqlite")
        self.params = dict(self.con.execute("SELECT title, id FROM genres").fetchall())
        self.comboBox.addItems(self.params)
        self.pushButton.clicked.connect(self.get_adding_verdict)

    def get_adding_verdict(self):
        t = self.title.toPlainText().strip()
        y = self.year.toPlainText().strip()
        d = self.duration.toPlainText().strip()
        if not t or not y.isdigit() or not d.isdigit() or int(y) > date.today().year or int(d) <= 0:
            self.statusBar().showMessage("Неверно заполнена форма")
            return False
        self.con.execute("INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)",
                         (t, int(y), self.params[self.comboBox.currentText()], int(d)))
        self.con.commit()
        self.parent().update_result()
        self.close()
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
