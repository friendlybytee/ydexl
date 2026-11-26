"""
Задача: Генерация случайного флага
Категория: Домашняя работа
Ограничение времени: 10 секунд
Ограничение памяти: 64Mb

Условие:
Напишите программу с графическим пользовательским интерфейсом на PyQt, которая создаёт изображение разноцветного (полосатого) флага. Количество цветов необходимо получить от пользователя с помощью диалогового окна.

Цвета генерируются случайно.

![randomflag.gif](./upload.gif)

Минимальное число, которое разрешено вводить пользователю должно быть 1, а максимальное 10. По умолчанию поставьте число 3 и сделайте, чтобы шаг был равен 1

Генерировать цвета обязательно с помощью **random.randrange**. Для получения одного случайного цвета обязательно сгенерировать три числа, отвечающие за r, g и b каналы (для каждого канала от 0 до 256, не включая 256). Цвета нужно генерировать для прямоугольников сверху вниз.

Класс, реализующий окно приложения, назовите **RandomFlag**.

При инициализации приложения необходимо сохранить параметры прямоугольника (одной полосы флага) в атрибут **base** объекта класса приложения в виде списка, первые 2 значения в котором - это x и y координата левой верхней точки верхней полосы флага, а следующие два - величины сторон (длина и ширина)

Кнопку назовите **button**. Размер окна приложения сделайте строго 300 на 400 пикселей.

"""

import random
import sys

from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QInputDialog, QPushButton, QWidget


class RandomFlag(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 400)
        self.setWindowTitle("Случайный флаг")
        self.base = [80, 80, 120, 30]
        self.colors = []
        self.button = QPushButton("Создать флаг", self)
        self.button.setGeometry(20, 20, 260, 30)
        self.button.clicked.connect(self.make_flag)

    def make_flag(self):
        n, ok = QInputDialog.getInt(self, "Флаг", "Количество цветов", 3, 1, 10, 1)
        if not ok:
            return
        self.colors = []
        for _ in range(n):
            r = random.randrange(0, 256)
            g = random.randrange(0, 256)
            b = random.randrange(0, 256)
            self.colors.append(QColor(r, g, b))
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        x, y, w, h = self.base
        for c in self.colors:
            qp.setBrush(c)
            qp.drawRect(x, y, w, h)
            y += h
        qp.end()


def main():
    app = QApplication(sys.argv)
    w = RandomFlag()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
