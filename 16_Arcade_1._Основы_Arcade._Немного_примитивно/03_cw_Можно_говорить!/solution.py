"""
Задача: Можно говорить!
Категория: Классная работа
Ограничение времени: 20 секунд
Ограничение памяти: 256 Мб

Условие:
Дорисуйте смайлу рот — это дуга в 180 градусов, расположение которой показано на схеме. Толщина линии — 1/20 от радиуса смайла. Цвет чёрный. Используйте метод `draw_arc_outline`. Положение глаз показано на схеме (их центры находятся на половине радиуса по горизонтали и по вертикали). Размер глаза — 15 пикселей. Ширина и высота эллипса, частью которого является улыбка, равна 3/2 (три вторых) радиуса. Вычисления производить в целых числах.

![alt-text](./statement-file)

Используйте шаблон кода ниже (вместо `...` впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные аргументы.

 **Шаблон кода решения**

```
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smile Silence"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.radius = radius

    def on_draw(self):
        '''Этот метод отвечает за отрисовку содержимого окна'''
        self.clear()
        ...

def setup_game(width=800, height=600, title="Smile Silence", radius=200):
    game = MyGame(width, height, title, radius)
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

### Результат (800x600) с радиусом 200

![alt-text](./statement-file)

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()
