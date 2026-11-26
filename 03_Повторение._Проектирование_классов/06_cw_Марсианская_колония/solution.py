"""
Задача: Марсианская колония
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
На Марсе строится колония. Для работы используются роботы разных специализаций. Вам нужно реализовать систему классов, которая моделирует взаимодействие добытчиков, перевозчиков и строителей.

#### Базовые классы

**Robot**

* Атрибуты: `name` (строка), `battery` (целое число, по умолчанию 100).
* Метод `status()` возвращает список: `[name, battery, "idle"]`
* Метод `info()` возвращает: `"Robot {name} ready for work"`

**Miner** — наследуется от **Robot**

* Добавляется атрибут: `resource` (строка, по умолчанию `"stone"`).
* Метод `mine()` возвращает: `"{name} mined {resource}"`
* Переопределяет `status()`: возвращает `[name, battery, "mining", resource]`

**Transporter** — наследуется от **Robot**

* Добавляется атрибут: `cargo` (целое число, по умолчанию 0).
* Метод `transport()` возвращает: `"{name} transported {cargo} kg"`
* Переопределяет `status()`: возвращает `[name, battery, "transporting", cargo]`

**Builder** — наследуется от **Robot**.

* Добавляется атрибут: `material` (строка, по умолчанию `"brick"`).
* Метод `build()` возвращает: `"{name} built a wall from {material}"`
* Переопределяет `status()`: возвращает `[name, battery, "building", material]`

#### Специализированные роботы

1. **MinerTransporter** — наследуется от **Miner** и **Transporter** в указанном порядке.

* Конструктор принимает: `name, battery` (по умолчанию 100), `resource, cargo`.
* Метод `work()` вызывает `mine()`, затем `transport()` и возвращает объединённый результат через перенос строки.
* Не переопределяет `status()` — наследует его от первого родителя (`Miner`).

2. **TransporterBuilder** — наследуется от **Transporter** и **Builder** в указанном порядке.

* Конструктор принимает: `name, battery` (по умолчанию 100), `cargo, material`.
* Метод `work()` вызывает `transport()`, затем `build()` и возвращает объединённый результат через перенос строки.
* Не переопределяет `status()` — наследует его от первого родителя (`Transporter`).

3. **SuperRobot** — наследуется от **Builder** и **MinerTransporter** в указанном порядке.

* Конструктор принимает: `name, battery` (по умолчанию 100), `resource, cargo, material`.
* Метод `work()` вызывает `mine()`, затем `transport()`, затем `build()` и возвращает объединённый результат через перенос строки.
* Не переопределяет `status()` — наследует его от первого родителя (`Builder`).

Пример:
--- Пример 1 ---
Ввод:
mt = MinerTransporter("Truck", 80, "ore", 500)
name, battery, mode, spec = mt.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(mt.work())
print()
tb = TransporterBuilder("Crane", 90, 300, "concrete")
name, battery, mode, spec = tb.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(tb.work())
print()
sr = SuperRobot("Megatron", 75, "titanium", 1000, "steel")
name, battery, mode, spec = sr.status()
print(f'Robot {name} has charge {battery}% and stay in {mode} mode with {spec}')
print(sr.work())
Вывод:
Robot Truck has charge 80% and stay in mining mode with ore
Truck mined ore
Truck transported 500 kg

Robot Crane has charge 90% and stay in transporting mode with 300
Crane transported 300 kg
Crane built a wall from concrete

Robot Megatron has charge 75% and stay in building mode with steel
Megatron mined titanium
Megatron transported 1000 kg
Megatron built a wall from steel

"""

import sys


def main():
    # TODO: вайбкодинг решения начинается здесь
    pass


if __name__ == "__main__":
    main()
