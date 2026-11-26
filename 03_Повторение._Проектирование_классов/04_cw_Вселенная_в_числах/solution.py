"""
Задача: Вселенная в числах
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Создайте класс **VogonNumber**, который принимает число. Перегрузите для него:

* `__add__, __sub__, __mul__, __truediv__` — все операции должны возвращать новый экземпляр класса `VogonNumber` с числом, которое равно соответственно сумме, разности, произведению или частному исходного числа и аргумента оператора. В случае деления значение округляется до целого по правилам [банковского округления](https://www.google.com/search?q=%D0%B1%D0%B0%D0%BD%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B5+%D0%BE%D0%BA%D1%80%D1%83%D0%B3%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5&rlz=1C5GCEA_enRU1107RU1107&oq=%D0%B1%D0%B0%D0%BD%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B5+%D0%BE%D0%BA%D1%80%D1%83&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBggCEEUYOTIHCAMQABiABDIHCAQQABiABDIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yCAgJEAAYFhge0gEIMzA3OWowajeoAgCwAgA&sourceid=chrome&source=chrome.ob&ie=UTF-8) (функция `round`).
* `__iadd__` (для +=) — изменяет текущий объект и возвращает его.
* `__floordiv__` — если результат деления меньше 42, то возбуждает исключение `ZeroDivisionError` с сообщением:  
  `"Это худшее стихотворение в моей жизни!"`, иначе возвращает новый `VogonNumber` — результат деления нацело значения атрибута класса на аргумент оператора.
* `__str__` — возвращает строку  
  `"Число Вселенной: <число>"`

Пример:
--- Пример 1 ---
Ввод:
vn = VogonNumber(42)
vn1 = vn + 3
vn2 = vn1 * 17
vn3 = vn2 / 7
vn4 = vn3 // 2
print(vn, vn1, vn2, vn3, vn4, sep='\n')
Вывод:
Число Вселенной: 42
Число Вселенной: 45
Число Вселенной: 765
Число Вселенной: 109
Число Вселенной: 54

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()
