import sys

from PyQt6.QtWidgets import (QApplication, QLineEdit, QListWidget,
                             QPushButton, QVBoxLayout, QWidget)


class MyNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Записная книжка")
        self.contactName = QLineEdit()
        self.contactName.setPlaceholderText("Имя")
        self.contactNumber = QLineEdit()
        self.contactNumber.setPlaceholderText("Телефон")
        self.addContactBtn = QPushButton("Добавить")
        self.contactList = QListWidget()
        self.addContactBtn.clicked.connect(self.add_contact)
        lay = QVBoxLayout(self)
        lay.addWidget(self.contactName)
        lay.addWidget(self.contactNumber)
        lay.addWidget(self.addContactBtn)
        lay.addWidget(self.contactList)

    def add_contact(self):
        name = self.contactName.text()
        number = self.contactNumber.text()
        self.contactList.addItem(f"{name}: {number}")
        self.contactName.clear()
        self.contactNumber.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyNotes()
    w.show()
    sys.exit(app.exec())
