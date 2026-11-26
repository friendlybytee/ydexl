"""
Задача: Калькулятор
Категория: Дополнительные задачи
Ограничение времени: 1 секунда
Ограничение памяти: 64Mb

Условие:
Каждый из нас пользовался калькулятором: физические формулы, средний балл, площадь комнаты, взнос каждого при сборе на подарок - для всего этого требуется калькулятор. Давайте выразим дань уважения к этому чудесному устройству и сами создадим *компьютерный* калькулятор!

Каждый калькулятор умеет четыре базовые функции:

* сложение
* вычитание
* умножение
* деление

Калькулятор также умеет работать с отрицательными и вещественными числами.

Помимо этого, у калькулятора имеются две примечательные кнопки:

* `С (от англ. clear - очистить)` полностью очищает поле ввода
* `CE (от англ. clear entry - очистить ввод)` стирает вводимое число, однако первый операнд (число) и оператор (знак), еcли они есть, остаются. Например, если ввести только `5`, то обе кнопки одинаково очистят поле ввода, если же ввести `5 + 5`, то кнопка `C` сотрет все, а `CE` только последную пятерку, оставив при этом введенные `5 +`.

Также, калькулятор достаточно умен, чтобы не выходить из строя при делении на ноль. В таком случае калькулятор сообщает об ошибке и не выполняет операцию.

![calculator.gif](./upload.gif)

Наименования классов и атрибутов следующие:

* `Calculator` класс приложения
* `main_label` основное поле ввода (нижнее)
* `secondary_label` дополнительное поле ввода (верхнее)
* `number_buttons` список кнопок по возрастанию их значений, где первый элемент кнопка **ноль**, а последний **девять**
* `clear_button` и `clear_entry_button` кнопки `C` и `CE` соответственно
* `divide_button`, `multiply_button`, `substract_button`, `add_button` кнопки `/`, `*`, `-` и `+` соответственно
* `float_point_button` кнопка точки (`.`)
* `plus_minus_button` кнопка смены знака числа (`±`)
* `equals_button` кнопка выполнения выражения (`=`)

Приложение назовите `Калькулятор`. Можете расположить элементы как в примере, а можете по-своему - вдруг ваше расположение удобнее?

Калькуляторы умеют работать с большими числами, очень большими, а экран у них маленький. Рассмотрим такой пример:

`123456789123456789123456789...`

Очевидно, что это число слишком длинное. Как же нам уместить такое число на экране?

Мы с вами будем использовать [экспоненциальную запись](https://ru.wikipedia.org/wiki/Экспоненциальная_запись). Существуют разные форматы записи: `123E+26`, `123E26`, `123e+26`, `123e26`. В записи `1.23E+26`, `E+26` обозначает, что число `1.23` умножается на `10``26`. В Python существует готовый [модуль](https://docs.python.org/3/library/decimal.html), который позволяет отображать числа в нужном формате. О том, как это сделать, читайте [здесь](https://stackoverflow.com/a/48986482).

Основное поле ввода должно умещать 11 символов, а при переполнении - использовать экспоненциальную запись. Дополнительное поле должно использовать экспоненциальную запись, если число (без знака и пробелов) длиннее 30 символов.

Оговорим некоторые моменты:

* при делении на ноль в основном поле должно отображаться сообщение `ОШИБКА`, а дополнительное поле должно быть пустым; после этого, при нажатии на любое число, должно появляться это число, а при нажатии на иные кнопки - отображаться `0`
* основное поле не должно быть пустым: после очистки в нем должен отображаться `0`
* в дополнительном поле число и знак арифметической операции должны разделяться пробелом
* кнопка смены знака не должна менять знак, если введенное число равно нулю (т.е. при `0`, `0.00` и прочих формах записи нуля кнопка не должна добавлять знак "минус")
* если вводимое число уже содержит точку, кнопка `float_point_button` должна игнорироваться
* если после деления у числа имеется ненужный `.0` (число поделилось нацело), следует выводить только целую часть
* следует ориентироваться на **gif-пример**

"""

import sys
from decimal import Decimal, getcontext

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QGridLayout, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget,
)

getcontext().prec = 60


def exp_text(n):
    m, e = ("%.2e" % n).split("e")
    return m + "e" + str(int(e))


def num_text(n):
    if n == n.to_integral_value():
        return str(int(n))
    return format(n.normalize(), "f")


def calc(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if b == 0:
        return None
    return a / b


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.resize(240, 370)

        self.secondary_label = QLabel()
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_label = QLabel()
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.main_label.setFont(QFont("Arial", 32))

        self.number_buttons = [self.make_button(str(i)) for i in range(10)]
        self.divide_button = self.make_button("/")
        self.multiply_button = self.make_button("*")
        self.substract_button = self.make_button("-")
        self.add_button = self.make_button("+")
        self.clear_button = self.make_button("C")
        self.clear_entry_button = self.make_button("CE")
        self.float_point_button = self.make_button(".")
        self.plus_minus_button = self.make_button("±")
        self.equals_button = self.make_button("=")

        for b in self.number_buttons:
            b.clicked.connect(self.on_digit)
        for b in (self.divide_button, self.multiply_button,
                  self.substract_button, self.add_button):
            b.clicked.connect(self.on_op)
        self.clear_button.clicked.connect(self.reset)
        self.clear_entry_button.clicked.connect(self.on_ce)
        self.float_point_button.clicked.connect(self.on_point)
        self.plus_minus_button.clicked.connect(self.on_sign)
        self.equals_button.clicked.connect(self.on_equals)

        d = self.number_buttons
        rows = [
            [d[7], d[8], d[9], self.divide_button],
            [d[4], d[5], d[6], self.multiply_button],
            [d[1], d[2], d[3], self.substract_button],
            [self.clear_button, d[0], self.clear_entry_button, self.add_button],
        ]
        grid = QGridLayout()
        grid.setSpacing(2)
        for i, row in enumerate(rows):
            for j, b in enumerate(row):
                grid.addWidget(b, i, j)
        grid.addWidget(self.float_point_button, 4, 0)
        grid.addWidget(self.plus_minus_button, 4, 1)
        grid.addWidget(self.equals_button, 4, 2, 1, 2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.secondary_label)
        layout.addWidget(self.main_label)
        layout.addLayout(grid, stretch=1)

        self.reset()

    def make_button(self, text):
        b = QPushButton(text, self)
        b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return b

    def reset(self):
        self.first = None
        self.op = None
        self.cur = "0"
        self.new = True
        self.err = False
        self.show_labels()

    def show_labels(self):
        if self.err:
            self.main_label.setText("ОШИБКА")
            self.secondary_label.setText("")
            return
        if len(self.cur) > 11:
            self.main_label.setText(exp_text(Decimal(self.cur)))
        else:
            self.main_label.setText(self.cur)
        if self.op is None:
            self.secondary_label.setText("")
            return
        s = num_text(self.first)
        if len(s.lstrip("-")) > 30:
            s = exp_text(self.first)
        self.secondary_label.setText(s + " " + self.op)

    def fail(self):
        self.reset()
        self.err = True
        self.show_labels()

    def skip_error(self):
        if self.err:
            self.reset()
            return True
        return False

    def on_digit(self):
        if self.err:
            self.reset()
        d = self.sender().text()
        if self.new or self.cur == "0":
            self.cur = d
        else:
            self.cur += d
        self.new = False
        self.show_labels()

    def on_point(self):
        if self.skip_error():
            return
        if self.new:
            self.cur = "0."
        elif "." not in self.cur:
            self.cur += "."
        self.new = False
        self.show_labels()

    def on_sign(self):
        if self.skip_error():
            return
        if Decimal(self.cur) == 0:
            return
        if self.cur.startswith("-"):
            self.cur = self.cur[1:]
        else:
            self.cur = "-" + self.cur
        self.new = False
        self.show_labels()

    def on_op(self):
        if self.skip_error():
            return
        if self.op is None:
            self.first = Decimal(self.cur)
        elif not self.new:
            res = calc(self.first, self.op, Decimal(self.cur))
            if res is None:
                self.fail()
                return
            self.first = res
        self.op = self.sender().text()
        self.cur = num_text(self.first)
        self.new = True
        self.show_labels()

    def on_equals(self):
        if self.skip_error():
            return
        if self.op is not None:
            res = calc(self.first, self.op, Decimal(self.cur))
            if res is None:
                self.fail()
                return
            self.cur = num_text(res)
            self.first = None
            self.op = None
        self.new = True
        self.show_labels()

    def on_ce(self):
        if self.skip_error():
            return
        self.cur = "0"
        self.new = True
        self.show_labels()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
