"""
Задача: Геральдический щит
Категория: Дополнительные задачи

Условие:
В замке Кэр-Параваль решили создать геральдический щит, объединяющий символы разных народов Нарнии. Описание герба хранится в JSON-файле.

Напишите программу, которая:

* Читает файл **coat\_of\_arms.json** с описанием герба.
* Создаёт изображение герба размером 800×800 пикселей с белым фоном.
* Рисует все элементы согласно описанию.
* Сохраняет результат в файл **narnia\_shield.png**.

Для рисования звезды и креста предложены схемы, `position` — центр фигуры, `size` — сторона квадрата, в который они вписаны.  
По ключу `"emblem"` варианты: `"circle"` (тогда даётся радиус `radius`), `"square"` (тогда даётся сторона квадрата `side`).

#### Пример входного файла

```
{
    "background": "gold",
    "border": {
        "color": "maroon",
        "width": 20
    },
    "emblem": {
        "shape": "circle",
        "color": "red",
        "position": [400, 300],
        "radius": 120
    },
    "symbols": [
        {
            "shape": "star",
            "color": "white",
            "position": [150, 150],
            "size": 120
        },
        {
            "shape": "star",
            "color": "white",
            "position": [650, 150],
            "size": 120
        },
        {
            "shape": "cross",
            "color": "silver",
            "position": [400, 600],
            "size": 200
        }
    ]
}
```

**Результат:**

![result](./statement-file.png)

Схема звезды:  
![result](./statement-file.png)

Схема креста:  
![result](./statement-file.png)

"""

import json
from PIL import Image, ImageDraw

with open("coat_of_arms.json", encoding="utf-8") as f:
    a = json.load(f)

img = Image.new("RGB", (800, 800), "white")
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 799, 799), fill=a["background"], outline=a["border"]["color"], width=a["border"]["width"])

e = a["emblem"]
x, y = e["position"]
if e["shape"] == "circle":
    r = e["radius"]
    d.ellipse((x - r, y - r, x + r, y + r), fill=e["color"])
else:
    s = e["side"] / 2
    d.rectangle((x - s, y - s, x + s, y + s), fill=e["color"])

for b in a["symbols"]:
    x, y = b["position"]
    s = b["size"]
    if b["shape"] == "star":
        r = s / 2
        w = s / 10
        p = [(x, y - r), (x + w, y - w), (x + r, y), (x + w, y + w),
             (x, y + r), (x - w, y + w), (x - r, y), (x - w, y - w)]
        d.polygon(p, fill=b["color"])
    else:
        w = s / 10
        d.rectangle((x - w, y - s / 2, x + w, y + s / 2), fill=b["color"])
        d.rectangle((x - s / 2, y - w, x + s / 2, y + w), fill=b["color"])

img.save("narnia_shield.png")
