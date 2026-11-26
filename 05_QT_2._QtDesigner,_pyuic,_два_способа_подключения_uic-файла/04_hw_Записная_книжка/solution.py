"""
Задача: Записная книжка
Категория: Домашняя работа
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb

Условие:
Напишите программу «Записная книжка» с графическим пользовательским интерфейсом на PyQT, используя необходимые виджеты.

Класс, реализующий это приложение назовите **MyNotes**.

Виджеты ввода имени и телефона должны являться **QLineEdit** и называться **contactName** и **contactNumber** соответственно.

Кнопку добавления контакта назовите **addContactBtn**.

Список контактов реализуйте через **QListWidget** и назовите **contactList**.

![mynotes.gif](./upload.gif)

Пользователь должен иметь возможность ввести имя контакта и его номер. После добавление данные должны отображаться в списке.

"""

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
