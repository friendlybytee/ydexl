import sys

from PyQt6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout,
                             QLineEdit, QListWidget, QPushButton,
                             QTimeEdit, QVBoxLayout, QWidget)


class SimplePlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Минипланировщик")
        self.events = []
        self.calendarWidget = QCalendarWidget()
        self.timeEdit = QTimeEdit()
        self.lineEdit = QLineEdit()
        self.addEventBtn = QPushButton("Добавить")
        self.eventList = QListWidget()
        self.addEventBtn.clicked.connect(self.add_event)
        left = QVBoxLayout()
        left.addWidget(self.calendarWidget)
        left.addWidget(self.timeEdit)
        left.addWidget(self.lineEdit)
        left.addWidget(self.addEventBtn)
        main = QHBoxLayout(self)
        main.addLayout(left)
        main.addWidget(self.eventList)

    def add_event(self):
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        time = self.timeEdit.time().toString("HH:mm:ss")
        self.events.append(f"{date} {time} {self.lineEdit.text()}")
        self.events.sort()
        self.eventList.clear()
        self.eventList.addItems(self.events)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SimplePlanner()
    w.show()
    sys.exit(app.exec())
