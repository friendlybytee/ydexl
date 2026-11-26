r"""
Задача: Сокровища Бильбо
Категория: Дополнительные задачи
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Бильбо — хоббит запасливый и подозрительный. Он хочет защитить доступ к своим сокровищам с помощью секретного ключа. Ключ — это число, которое должно совпадать с общим количеством предметов в кладовой (сумма всех Количество). Только тогда Бильбо разрешит группировать и выгружать данные.

Напишите функцию для проверки доступа и работы с секретным файлом.

Файл `CSV` содержит данные с заголовками (разделители — точки):  
`Предмет,Количество,Цена_в_золотых,Где_найдено`  
`Item.Quantity.Price_in_gold.Found_in`

Функция **process\_treasures(csv\_filename, json\_filename, secret\_key, grouping)** принимает аргументы:

* `csv_filename` — имя исходного CSV-файла.
* `json_filename` — имя выходного JSON-файла.
* `secret_key` — число (ключ доступа).
* `grouping` — строка, название поля для группировки (может быть одно из полей файла, например, 'Где\_найдено' или 'Цена\_в\_золотых').

Функция:

* читает данные из CSV-файла.
* проверяет ключ: если `secret_key` не совпадает с общей суммой количества предметов — сохраняет в JSON-файл сообщение об ошибке `{"error": "access denied"}`.  
  Если ключ верный:
* группирует сокровища по указанному полю group\_by.
* для каждой группы подсчитывает:
  1. Количество предметов в группе (сумма Количество).
  2. Общую стоимость группы (сумма Количество \* Цена\_в\_золотых).
  3. Список названий предметов в группе в обратном алфавитном порядке.
* записывает результат в JSON-файл в формате:

```
{
  "group1": {
    "total_items": 10,
    "total_value": 1500,
    "items": ["предмет1", "предмет2"]
  },
  "group2": {
    ...
  }
}
```

В названии группы после group записывается значение параметра группировки, по которому она произведена. В примере это 1, 2 или 4 — количества предметов.

Пример:
--- Пример 1 ---
Ввод:
#  Содержимое файла treasure.csv

Item.Quantity.Price_in_gold.Found_in

The One Ring.1.1000.Misty Mountains

Golden Cup.4.50.Lonely Mountain

Mithril Coat.1.5000.Smaug's Lair

Elven Blade.2.300.Mirkwood

Arkenstone.1.10000.Lonely Mountain

Elven Rope.2.150.Lothlórien

River Pearl.1.800.Esgaroth

Silver Necklace.1.250.Rivendell

Golden Goblet.2.120.The Shire

Precious Gem.4.75.Moria



# Вызов функции

process_treasures('treasure.csv', 'result.json', 19, 'Quantity')
Вывод:
{

  "group1": {

    "total_items": 5,

    "total_value": 17050,

    "items": [

      "The One Ring",

      "Silver Necklace",

      "River Pearl",

      "Mithril Coat",

      "Arkenstone"

    ]

  },

  "group2": {

    "total_items": 6,

    "total_value": 1140,

    "items": [

      "Golden Goblet",

      "Elven Rope",

      "Elven Blade"

    ]

  },

  "group4": {

    "total_items": 8,

    "total_value": 500,

    "items": [

      "Precious Gem",

      "Golden Cup"

    ]

  }

}

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()

import csv
import json


def process_treasures(csv_filename, json_filename, secret_key, grouping):
    names = {'Предмет': 'Item', 'Количество': 'Quantity',
             'Цена_в_золотых': 'Price_in_gold', 'Где_найдено': 'Found_in'}
    grouping = names.get(grouping, grouping)
    with open(csv_filename, encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='.'))
    if sum(int(r['Quantity']) for r in rows) != int(secret_key):
        res = {'error': 'access denied'}
    else:
        g = {}
        for r in rows:
            k = r[grouping]
            if k not in g:
                g[k] = {'total_items': 0, 'total_value': 0, 'items': []}
            q = int(r['Quantity'])
            g[k]['total_items'] += q
            g[k]['total_value'] += q * int(r['Price_in_gold'])
            g[k]['items'].append(r['Item'])
        keys = sorted(g, key=lambda k: (0, int(k), '') if k.isdigit() else (1, 0, k))
        res = {}
        for k in keys:
            g[k]['items'].sort(reverse=True)
            res['group' + k] = g[k]
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
