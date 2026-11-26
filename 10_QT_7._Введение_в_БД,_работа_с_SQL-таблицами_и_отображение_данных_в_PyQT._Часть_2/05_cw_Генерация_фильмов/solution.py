import sqlite3
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton, QStatusBar, QTableWidget,
                             QTableWidgetItem, QTextEdit, QWidget)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Генерация фильмов")
        w = QWidget(self)
        self.setCentralWidget(w)
        self.textEdit = QTextEdit(w)
        self.textEdit.setGeometry(10, 10, 200, 30)
        self.pushButton = QPushButton("Запуск", w)
        self.pushButton.setGeometry(220, 10, 100, 30)
        self.saveButton = QPushButton("Изменить", w)
        self.saveButton.setGeometry(330, 10, 100, 30)
        self.tableWidget = QTableWidget(w)
        self.tableWidget.setGeometry(10, 50, 580, 300)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.con = sqlite3.connect("films_db.sqlite")
        self.rows = []
        self.pushButton.clicked.connect(self.run)
        self.saveButton.clicked.connect(self.save)

    def run(self):
        try:
            self.rows = self.con.execute("SELECT * FROM films WHERE " + self.textEdit.toPlainText()).fetchall()
        except sqlite3.Error:
            self.rows = []
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["id", "title", "year", "genre", "duration"])
        for i, r in enumerate(self.rows):
            for j, v in enumerate(r):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))
        self.statusbar.showMessage("" if self.rows else "По этому запросу ничего не найдено")

    def save(self):
        if not self.rows:
            return
        if QMessageBox.question(self, "", "Действительно заменить элементы?") != QMessageBox.StandardButton.Yes:
            return
        for r in self.rows:
            self.con.execute("DELETE FROM films WHERE id = ?", (r[0],))
            self.con.execute("INSERT INTO films (id, title, year, genre, duration) VALUES (?, ?, ?, ?, ?)",
                             (r[0], r[1][::-1], r[2] + 1000, r[3], r[4] * 2))
        self.con.commit()
        self.run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
