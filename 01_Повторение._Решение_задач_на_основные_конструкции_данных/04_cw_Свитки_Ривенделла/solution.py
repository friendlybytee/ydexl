"""
Задача: Свитки Ривенделла
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
В библиотеке Ривенделла хранятся древние свитки. Элронд хочет отобрать только эльфийские свитки для перевода.

Напишите функцию, которая их выберет.

Функция **scrolls()** принимает произвольное количество кортежей *(название свитка, его тип)*.  
Функция возвращает список свитков, в типе которых присутствует *elves* в любом регистре, отсортированный в обратном алфавитном порядке.

Пример:
--- Пример 1 ---
Ввод:
data = [('Quenta Silmarillion', 'elves chronicles'),
        ('The Mines of Moria', 'dwarven engineering'),
        ('The Old Forest', 'huorns and elves'),
        ('The Trees of Valinor', 'elvish botany'),
        ('The Ruin of Doriath', 'elves tragedy')]
print(*scrolls(*data), sep='\n')
Вывод:
The Ruin of Doriath
The Old Forest
Quenta Silmarillion

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()
