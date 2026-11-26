import sqlite3
import sys

from PyQt6.QtWidgets import (
    QApplication, QComboBox, QLabel, QLineEdit, QPushButton, QWidget,
    QFormLayout,
)

FIELDS = {"Год выпуска": ("year", True), "Название": ("title", False), "Продолжительность": ("duration", True)}


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск по фильмам")
        self.con = sqlite3.connect("films_db.sqlite")

        self.parameterSelection = QComboBox()
        self.parameterSelection.setObjectName("parameterSelection")
        self.parameterSelection.addItems(["Год выпуска", "Название", "Продолжительность"])
        self.queryLine = QLineEdit()
        self.queryLine.setObjectName("queryLine")
        self.queryButton = QPushButton("Найти")
        self.queryButton.setObjectName("queryButton")
        self.errorLabel = QLabel()
        self.errorLabel.setObjectName("errorLabel")

        self.idEdit = QLineEdit()
        self.idEdit.setObjectName("idEdit")
        self.titleEdit = QLineEdit()
        self.titleEdit.setObjectName("titleEdit")
        self.yearEdit = QLineEdit()
        self.yearEdit.setObjectName("yearEdit")
        self.genreEdit = QLineEdit()
        self.genreEdit.setObjectName("genreEdit")
        self.durationEdit = QLineEdit()
        self.durationEdit.setObjectName("durationEdit")
        self.edits = [self.idEdit, self.titleEdit, self.yearEdit,
                      self.genreEdit, self.durationEdit]

        layout = QFormLayout(self)
        layout.addRow("Параметр", self.parameterSelection)
        layout.addRow("Значение", self.queryLine)
        layout.addRow(self.queryButton)
        layout.addRow(self.errorLabel)
        layout.addRow("ID", self.idEdit)
        layout.addRow("Название", self.titleEdit)
        layout.addRow("Год", self.yearEdit)
        layout.addRow("Жанр", self.genreEdit)
        layout.addRow("Продолжительность", self.durationEdit)

        self.queryButton.clicked.connect(self.search)

    def search(self):
        for e in self.edits:
            e.setText("")
        self.errorLabel.setText("")
        field, is_number = FIELDS[self.parameterSelection.currentText()]
        value = self.queryLine.text()
        if is_number:
            if not value.strip().isdigit():
                self.errorLabel.setText("Неправильный запрос")
                return
            value = int(value)
        row = self.con.execute(f"SELECT * FROM Films WHERE {field} = ? ORDER BY id LIMIT 1", (value,)).fetchone()
        if row is None:
            self.errorLabel.setText("Ничего не найдено")
            return
        for e, v in zip(self.edits, row):
            e.setText(str(v))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
