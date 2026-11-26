"""
Задача: Знакомство с L-системами
Категория: Дополнительные задачи
Ограничение времени: 10 секунд
Ограничение памяти: 64Mb

Условие:
Напишите программу с графическим пользовательским интерфейсом на PyQT, которая умеет по заданному определению строить L-системы. Определение L-системы задается в текстовом файле, который необходимо открыть с помощью диалога открытия файла при запуске программы. Структура файла следующая:

Первая строка — название системы (строка); Вторая строка — целое число, говорящее о том, на сколько углов делится плоскость. Этот параметр необходим для организации поворотов; Третья строка — аксиома; Остальное — теоремы.  
Пример:

Кривая Коха

5  
F  
F F-F++F-F

![lsys.gif](./upload.gif)

Первый шаг эволюции строится автоматически, затем возможно перемещение между шагами эволюции с помощью слайдера.

Первую линию начинайте строить из точки с координатами (250, 400)

Также, установите длину линий равной 20 пикселям

Класс, реализующий окно приложения, назовите **LSystem**.

Цвет, которым будете рисовать сохраните в атрибут **color** объекта приложения при инициализации.

Слайдеру установите минимальное число равное 1, а максимальное 5. Назовите его **slider**. Размер окна приложения сделайте строго 1000 пикселей по обоим измерениям. Слайдер расположите горизонтально внизу окна начиная с точки (25, 980).

Все вычисления производите в вещественных числах, вещественные результаты вычислений передавайте конструктору класса [**QPointF**](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QPointF.html#PySide6.QtCore.QPointF) - это точки, по которым будут строится линии. Для построения линий используйте синтаксис:

```
QtGui.QPainter.drawLine(p1, p2)
```

Где **p1** и **p2** - объекты класса **QPointF**.

Пример:
--- Пример 1 ---
Ввод:
Ограничение времени
Вывод:
10 секунд

--- Пример 2 ---
Ввод:
Ограничение памяти
Вывод:
64Mb

"""

import math
import sys

from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QFileDialog, QSlider, QWidget


class LSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1000)
        self.color = QColor(0, 0, 0)
        name, _ = QFileDialog.getOpenFileName(
            self, "Открыть L-систему", "", "Text (*.txt);;All (*)"
        )
        with open(name, encoding="utf-8") as f:
            lines = f.read().split("\n")
        self.setWindowTitle(lines[0].strip())
        self.parts = int(lines[1])
        self.axiom = lines[2].strip()
        self.rules = {}
        for line in lines[3:]:
            a = line.split()
            if len(a) == 2:
                self.rules[a[0]] = a[1]

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setGeometry(25, 980, 950, 15)
        self.slider.setMinimum(1)
        self.slider.setMaximum(5)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.update)

    def evolve(self, steps):
        s = self.axiom
        for _ in range(steps):
            res = ""
            for c in s:
                res += self.rules.get(c, c)
            s = res
        return s

    def paintEvent(self, event):
        s = self.evolve(self.slider.value())
        qp = QPainter(self)
        qp.setPen(self.color)
        x, y = 250.0, 400.0
        angle = 0
        stack = []
        for c in s:
            if c == "+":
                angle += 1
            elif c == "-":
                angle -= 1
            elif c == "[":
                stack.append((x, y, angle))
            elif c == "]":
                if stack:
                    x, y, angle = stack.pop()
            elif c.isalpha():
                rad = math.pi / 2 + 2 * math.pi * angle / self.parts
                nx = x + 20 * math.cos(rad)
                ny = y - 20 * math.sin(rad)
                qp.drawLine(QPointF(x, y), QPointF(nx, ny))
                x, y = nx, ny
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = LSystem()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
