"""
Задача: Аисты
Категория: Дополнительные задачи
Ограничение времени: 20 секунд
Ограничение памяти: 512 Мб

Условие:
Это просто рисунок аистов из графических примитивов.

Характерный размер клеточки записан в аргументе `part`, который передаётся конструктору класса. Цвет заливки окна BABY\_BLUE\_EYES. Толщина контура фигур с контуром — 1/10, а линий — 1/5 от характерного размера.

![alt-text](./statement-file)

[ссылка на детальное изображение](https://assets.contest.yandex.net/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..fBo5vawV7TimsfAB.X-4qZtqvPicYqpvBM3kNGrkCk7RcW-ngV2N0kqZ7ISvQSgDBqx3F8LFj2tdTZZY_P2pLcjt4UIBAzvC_I0dc8-b_lOuFVPT61KxpXA6xku5DCXCdtb5JzF1w-m7UR6bjQSdadlMP.-in7WkEKtIjTfMiE-qFEsA)  
 Для рисования нужно использовать такие методы: `arcade.draw_circle_filled()`, `arcade.draw_circle_outline()`, `arcade.draw_triangle_filled()`, `arcade.draw_line()`, `arcade.draw_arc_filled()`, `arcade.draw_arc_outline()`.

Используйте шаблон кода ниже (вместо `...` впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные аргументы.

 **Шаблон кода решения**

```
import arcade

PART = 20
SCREEN_WIDTH = PART * 20
SCREEN_HEIGHT = PART * 20
SCREEN_TITLE = "Storks"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, part):
        super().__init__(width, height, title)
        ...

    def on_draw(self):
        self.clear()
        ...

def setup_game(width=400, height=400, title="Storks", part=20):
    game = MyGame(width, height, title, part)
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, PART)
    arcade.run()

if __name__ == "__main__":
    main()
```

### Результат

![gif result](./statement-file)

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()
