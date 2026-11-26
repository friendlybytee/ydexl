"""
Задача: Рост хорошего настроения
Категория: Домашняя работа
Ограничение времени: 10 секунд
Ограничение памяти: 64Mb

Условие:
Напишите программу с графическим пользовательским интерфейсом на PyQT. При запуске программы средствами QPainter должен рисоваться смайлик. С помощью слайдера можно управлять масштабом смайлика.

![goodmoodrising.gif](./upload.gif)

Класс, реализующий окно приложения, назовите **GoodMoodRising**.

На слайдере установите 0 минимальным значением, а 100 максимальным. Изначальное 50. Слайдер назовите **slider**. Также, он обязательно должен быть вертикальным, выходить из точки (970, 40) (левый верхний угол), быть шириной в 20 пикселей и высотой в 500

пусть size - значение на слайдере. Тогда, большой круг должен быть вписан в квадрат, начинающийся из (0, 0) и стороной 10 \* size. Левый глаз должен быть вписан в квадрат из точки (2 \* size, 2 \* size) и иметь радиус 2 \* size. Правый глаз должен быть симметричен

Улыбку нарисуйте из точки (2 \* size, 6 \* size). Она должна иметь длинну 6 \* size, высоту 2 \* size. Для улыбки используйте функцию **drawArc**. Оставшиеся 2 параметра (a, alen) должны равняться (-480, -1920)

Цвет, которым будете рисовать, сохраните в классе, назвав **color** (тип данных **QColor**). Размер окна приложения сделайте строго 1000 по каждому измерению.

"""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QSlider, QWidget


class GoodMoodRising(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1000)
        self.setWindowTitle("Рост хорошего настроения")
        self.color = QColor(255, 200, 0)
        self.slider = QSlider(Qt.Orientation.Vertical, self)
        self.slider.setGeometry(970, 40, 20, 500)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        s = self.slider.value()
        qp = QPainter(self)
        qp.setPen(self.color)
        qp.drawEllipse(0, 0, 10 * s, 10 * s)
        qp.drawEllipse(2 * s, 2 * s, 2 * s, 2 * s)
        qp.drawEllipse(6 * s, 2 * s, 2 * s, 2 * s)
        qp.drawArc(2 * s, 6 * s, 6 * s, 2 * s, -480, -1920)
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = GoodMoodRising()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
