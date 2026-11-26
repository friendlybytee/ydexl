"""
Задача: Текстовый флаг
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb

Условие:
Напишите приложение «Текстовый флаг» с графическим пользовательским интерфейсом на PyQT.

Пользователь должен иметь возможность выбрать цвет для каждой из трёх полос флага с помощью Radio Button из трех вариантов. После выбора и нажатия на кнопку «Сделать флаг» программа должна выводить сообщение, соответствующее выбранным цветам. Например: «Красный, Зелёный, Белый».

Класс, реализующий окно приложения, назовите **FlagMaker**.

Группы кнопок для выбора цветов должны быть типа **QButtonGroup**.

Кнопки каждого цвета должны быть типа **QRadioButton**. Кнопки выбора цветов должны быть добавлены в группы кнопок в порядке, изображенном на анимации (Синий, Красный, Зелёный).

Кнопка для генерации флага должна называться **make\_flag**. Элемент итогового текстового флага должен иметь тип **QLabel** и называться **result**.

Группы кнопок для выбора первого, второго, третьего цвета назовите **color\_group\_1**, **color\_group\_2**, **color\_group\_3** соответственно. Кнопки надо добавлять в группы в следующем порядке цветов: "Синий", "Красный", "Зелёный". Создание виджетов **QButtonGroup** и добавление в них кнопок лучше делать не с использованием **QtDesigner**, а в коде своей программы.

Сделайте так, чтобы размер окна нельзя было изменять. Выберите размер на свое усмотрение. Как это сделать можно посмотреть в [документации](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QWidget.setFixedSize)

![textflag.gif](./upload.gif)

"""

import sys

from PyQt6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
                             QPushButton, QRadioButton, QVBoxLayout, QWidget)

COLORS = ["Синий", "Красный", "Зелёный"]


class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 250)
        self.setWindowTitle("Текстовый флаг")
        self.groups = []
        main = QVBoxLayout(self)
        row = QHBoxLayout()
        for i in range(3):
            group = QButtonGroup(self)
            setattr(self, f"color_group_{i + 1}", group)
            self.groups.append(group)
            col = QVBoxLayout()
            for name in COLORS:
                btn = QRadioButton(name)
                group.addButton(btn)
                col.addWidget(btn)
            group.buttons()[0].setChecked(True)
            row.addLayout(col)
        main.addLayout(row)
        self.make_flag = QPushButton("Сделать флаг")
        self.make_flag.clicked.connect(self.make)
        main.addWidget(self.make_flag)
        self.result = QLabel("")
        main.addWidget(self.result)

    def make(self):
        names = [g.checkedButton().text() for g in self.groups]
        self.result.setText(", ".join(names))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FlagMaker()
    w.show()
    sys.exit(app.exec())
