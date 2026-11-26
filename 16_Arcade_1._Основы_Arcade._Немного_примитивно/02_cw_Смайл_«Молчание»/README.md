# Смайл «Молчание»

| Характеристика | Значение |
| --- | --- |
| **Категория** | Классная работа |
| **Макс. балл** | 16 |
| **Ограничение времени** | 20 секунд |
| **Ограничение памяти** | 256 Мб |
| **Ввод** | стандартный ввод |
| **Вывод** | стандартный вывод |
| **ID задачи** | `88948` |

---

## Условие

В окне размером `900х600`, залитом белым цветом, нарисуйте жёлтый (255, 192, 0) смайлик с двумя чёрными глазами. Смайл должен располагаться по центру окна. Положение глаз показано на схеме (их центры находятся на половине радиуса по горизонтали и по вертикали). Размер глаза — `15` пикселей. Для отрисовки кругов используйте метод `draw_circle_filled`.

![alt-text](./statement-file)

Используйте шаблон кода ниже (вместо `...` впишите свой код). Атрибуты класса должны иметь такие же имена, как и переданные аргументы.

 **Шаблон кода решения**

```
import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smile Silence"

class MyGame(arcade.Window):
    def __init__(self, width, height, title, radius):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.radius = radius

    def on_draw(self):
        """Этот метод отвечает за отрисовку содержимого окна"""
        self.clear()
        ...

def setup_game(width=900, height=600, title="Smile Silence", radius=200):
    game = MyGame(width, height, title, radius)
    return game

def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
```

### Результат (900x600) с радиусом 200

![alt-text](./statement-file)

## Примечания

Для успешного выполнения ваше решение должно содержать функцию `setup_game` и другие методы и функции, предоставленные в шаблоне.
