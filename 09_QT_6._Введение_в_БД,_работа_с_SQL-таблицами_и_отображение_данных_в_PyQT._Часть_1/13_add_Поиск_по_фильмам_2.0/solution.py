import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QFormLayout, QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget,
)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск по фильмам 2.0")
        self.con = sqlite3.connect("films_db.sqlite")

        self.year = QLineEdit()
        self.year.setObjectName("year")
        self.title = QLineEdit()
        self.title.setObjectName("title")
        self.duration = QLineEdit()
        self.duration.setObjectName("duration")
        self.queryButton = QPushButton("Найти")
        self.queryButton.setObjectName("queryButton")
        self.errorLabel = QLabel()
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName("tableWidget")

        form = QFormLayout()
        form.addRow("Год", self.year)
        form.addRow("Название", self.title)
        form.addRow("Продолжительность", self.duration)
        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.queryButton)
        layout.addWidget(self.errorLabel)
        layout.addWidget(self.tableWidget)

        self.queryButton.clicked.connect(self.search)

    def condition(self, field, text):
        text = text.strip()
        if text.isdigit():
            return f"{field} = {text}"
        return f"{field} {text}"

    def search(self):
        self.errorLabel.setText("")
        parts = []
        for field, edit in (("year", self.year), ("title", self.title), ("duration", self.duration)):
            if edit.text().strip():
                parts.append(self.condition(field, edit.text()))
        query = "SELECT * FROM Films"
        if parts:
            query += " WHERE " + " AND ".join(parts)
        try:
            cur = self.con.execute(query)
            rows = cur.fetchall()
        except sqlite3.Error:
            self.errorLabel.setText("Неправильный запрос")
            return
        self.tableWidget.setColumnCount(len(cur.description))
        self.tableWidget.setHorizontalHeaderLabels([d[0] for d in cur.description])
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(v)))
        if not rows:
            self.errorLabel.setText("Ничего не найдено")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
