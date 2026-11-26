"""
Задача: Минипланировщик
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Используя виджеты календаря, выбора времени, отображения списка и другие, напишите программу-ежедневник с графическим пользовательским интерфейсом на PyQT. Класс, реализующий это приложение назовите **SimplePlanner**

Виджет выбора времени должен называться **timeEdit** и иметь тип **QTimeEdit**.

Календарь реализуйте через **QCalendarWidget** и назовите этот виджет **calendarWidget**. Кнопку добавления события назовите **addEventBtn**.  
Поле для ввода описания события назовите **lineEdit**.

Для отображения списка событий используйте **QListWidget**, назовите этот виджет **eventList**.

Пользователь должен иметь возможность ввести название события, выбирать дату и время. После нажатия на кнопку «Добавить» событие должно добавляться в в список событий. События должны быть отсортированы по возрастанию даты.

![miniplanner.gif](./statement-file.gif)  
Для размещения виджетов используйте различные layout.  
Дату/время следует преобразовывать в текст в такой формат "2020-03-04 12:34:00"

"""

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
