"""
Задача: Квадрат-объектив — 1
Категория: Классная работа
Ограничение времени: 10 секунд
Ограничение памяти: 64Mb

Условие:
Напишите программу «Квадрат-объектив — 1» с графическим пользовательским интерфейсом. На экране нарисован квадрат. Пользователем в соответствующие поля вводятся три параметра:

Целое число **a** — размер стороны самого большого квадрата в пикселях (по умолчанию равен 300)  
Вещественное число **k** — коэффициент масштабирования (<1, по умолчанию равен 0.9)  
Целое число **n** — количество повторений (по умолчанию равно 10) Программа строит n квадратов, сторона каждого следующего квадрата определяется по формуле: **ai = ai-1\*k**.  
Все квадраты имеют общий центр.

![square1.gif](./upload.gif)

Класс, реализующий окно приложения, назовите **Square1**. Размер окна приложения сделайте строго 800 на 900 пикселей. Кнопку, которая будет рисовать квадраты, назовите **btn**. Поле ввода размера стороны квадрата **lineEdit**. Поля для ввода коэффициента и количества квадратов назовите **lineEdit\_2** и **lineEdit\_3** соответственно.

Цвет, которым вы будете рисовать квадраты должен отличаться от фонового и должен быть сохранён в атрибут **color** объекта класса приложения в виде **QColor**. Для изображения квадрата воспользуйтесь методом [**drawRect**](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPainter.html#PySide6.QtGui.QPainter.drawRect) класса [**QPainter**](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QPainter.html#PySide6.QtGui.QPainter). Для создания объекта прямоугольника, который передается методу **drawRect**, используйте класс [**QRectF**](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QRectF.html#PySide6.QtCore.QRectF). Все вычисления производите в вещественных числах, вещественные результаты вычислений передавайте конструктору класса **QRectF** Левая верхняя точка самого большого квадрата должна иметь координаты (50, 130). Все элементы управления (поля для ввода данных и кнопки) расположите выше этих координат.

"""

import sys

from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 900)
        self.setWindowTitle("Квадрат-объектив — 1")
        self.color = QColor(200, 0, 0)
        self.draw_flag = False

        QLabel("a", self).setGeometry(10, 10, 30, 25)
        QLabel("k", self).setGeometry(210, 10, 30, 25)
        QLabel("n", self).setGeometry(410, 10, 30, 25)
        self.lineEdit = QLineEdit("300", self)
        self.lineEdit.setGeometry(40, 10, 150, 25)
        self.lineEdit_2 = QLineEdit("0.9", self)
        self.lineEdit_2.setGeometry(240, 10, 150, 25)
        self.lineEdit_3 = QLineEdit("10", self)
        self.lineEdit_3.setGeometry(440, 10, 150, 25)
        self.btn = QPushButton("Рисовать", self)
        self.btn.setGeometry(620, 10, 150, 25)
        self.btn.clicked.connect(self.start)

    def start(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        if not self.draw_flag:
            return
        a = float(self.lineEdit.text())
        k = float(self.lineEdit_2.text())
        n = int(self.lineEdit_3.text())
        qp = QPainter(self)
        qp.setPen(self.color)
        cx = 50 + a / 2
        cy = 130 + a / 2
        for _ in range(n):
            qp.drawRect(QRectF(cx - a / 2, cy - a / 2, a, a))
            a *= k
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = Square1()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
