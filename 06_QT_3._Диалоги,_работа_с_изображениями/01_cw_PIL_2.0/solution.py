"""
Задача: PIL 2.0
Категория: Классная работа
Ограничение времени: 20 секунд
Ограничение памяти: 64Mb

Условие:
Вспомним PIL. Напишите программу с графическим пользовательским интерфейсом на PyQT. При старте приложения должен открываться диалог выбора изображения. В программу загружается квадратная картинка. Необходимо реализовать следующие возможности:

Оставить один из цветовых каналов Повернуть картинку на 90 градусов влево/вправо Все изменения должны быть видны в реальном времени.

![pil.gif](./upload.gif)

Класс, реализующий окно приложения, назовите **MyPillow**.

Для диалога выбора изображений используйте класс **QFileDialog**.

Надписи на всех кнопках должны быть идентичны надписям из примера (с учётом регистра).

Кнопки, отвечающие за изменение цвета, объединить в группу с названием **channelButtons**.

Кнопки, отвечающие за повороты, объединить в группу с названием **rotateButtons**.

Обработчики нажатия на кнопки, следует привязать к каждой кнопке индивидуально.

Текущее изображение нужно хранить в поле объекта класса **MyPillow**, поле назовите **curr_image** его тип - **QImage**.

Изучите подробнее документацию к классам **[QImage](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QImage.html)**, **[QTransform](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTransform.html)** и **[QPixmap](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QPixmap.html)**. При решении этой задачи не используйте библиотеку **Pillow**.

"""

import sys

from PyQt6.QtGui import QImage, QPixmap, QTransform, QColor
from PyQt6.QtWidgets import (
    QApplication, QButtonGroup, QFileDialog, QLabel, QPushButton, QWidget,
)


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PIL 2.0")
        self.setFixedSize(400, 420)
        result = QFileDialog.getOpenFileName(
            self, "Выбрать картинку", "",
            "Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)"
        )
        name = result[0] if isinstance(result, (tuple, list)) else result
        self.curr_image = QImage(name)
        self.orig_image = QImage(self.curr_image)  # без фильтра каналов
        self.shown_image = self.curr_image

        self.label = QLabel(self)
        self.label.setGeometry(140, 10, 250, 250)
        self.label.setScaledContents(True)

        self.channelButtons = QButtonGroup(self)
        self.rotateButtons = QButtonGroup(self)
        self.btn_r = QPushButton("R", self)
        self.btn_g = QPushButton("G", self)
        self.btn_b = QPushButton("B", self)
        self.btn_all = QPushButton("ALL", self)
        self.btn_left = QPushButton("Против часовой стрелки", self)
        self.btn_right = QPushButton("По часовой стрелке", self)

        y = 10
        for btn in (self.btn_r, self.btn_g, self.btn_b, self.btn_all):
            btn.setGeometry(10, y, 120, 30)
            self.channelButtons.addButton(btn)
            y += 60
        self.btn_left.setGeometry(10, 340, 190, 30)
        self.btn_right.setGeometry(210, 340, 180, 30)
        self.rotateButtons.addButton(self.btn_left)
        self.rotateButtons.addButton(self.btn_right)

        self.btn_r.clicked.connect(self.red)
        self.btn_g.clicked.connect(self.green)
        self.btn_b.clicked.connect(self.blue)
        self.btn_all.clicked.connect(self.all_channels)
        self.btn_left.clicked.connect(self.rotate_left)
        self.btn_right.clicked.connect(self.rotate_right)
        self.show_image()

    def sync(self):
        # если curr_image подменили снаружи, считаем его новым оригиналом
        if self.curr_image is not self.shown_image:
            self.orig_image = QImage(self.curr_image)

    def show_image(self):
        self.shown_image = self.curr_image
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def keep_channel(self, channel):
        self.sync()
        img = QImage(self.orig_image)
        for x in range(img.width()):
            for y in range(img.height()):
                c = img.pixelColor(x, y)
                rgb = [c.red(), c.green(), c.blue()]
                for i in range(3):
                    if i != channel:
                        rgb[i] = 0
                img.setPixelColor(x, y, QColor(rgb[0], rgb[1], rgb[2], c.alpha()))
        self.curr_image = img
        self.show_image()

    def red(self):
        self.keep_channel(0)

    def green(self):
        self.keep_channel(1)

    def blue(self):
        self.keep_channel(2)

    def all_channels(self):
        self.sync()
        self.curr_image = QImage(self.orig_image)
        self.show_image()

    def rotate(self, angle):
        self.sync()
        t = QTransform().rotate(angle)
        self.orig_image = self.orig_image.transformed(t)
        self.curr_image = self.curr_image.transformed(t)
        self.show_image()

    def rotate_left(self):
        self.rotate(-90)

    def rotate_right(self):
        self.rotate(90)


def main():
    app = QApplication(sys.argv)
    w = MyPillow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
