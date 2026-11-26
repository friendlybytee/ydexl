"""
Задача: Файловая статистика
Категория: Классная работа
Ограничение времени: 1 секунда
Ограничение памяти: 64 Мб

Условие:
Напишите приложение с графическим пользовательским интерфейсом на PyQT, которое позволяет пользователю задать имя текстового файла, в котором содержатся через пробельные символы (пробел, табуляция, перевод строки и т. д.) целые числа. По нажатию на кнопку необходимо вывести в соответствующие виджеты максимальное, минимальное и среднее значение из этого файла. Эту же информацию необходимо сохранить в файл `out.txt`.

По нажатию на кнопку необходимо в поле `QTextBrowser` вывести максимальное, минимальное и среднее значение из этого файла в формате:

```
Максимальное значение = [целое число]
Минимальное значение = [целое число]
Среднее значение = [число с двумя знаками после запятой (при выводе использовать форматированный вывод)]
```

Для этого класс должен реализовывать метод `min_med_max`, который считает и выводит эти значения в статус-бар.

Рассмотрим крайние случаи:

* В случае, если файл не существует, следует выводить текст «Указанный файл не существует» в статусбар. Этот виджет QStatusBar уже есть в классе QMainWindow, он называется statusBar. Для получения доступа к этому виджету испольльзуйте метод statusBar класса QMainWindow.
* Если файл пуст или состоит только из пробельных символов (пробелов, символов табуляции и переноса строки и т. д.), в статусбаре отображать сообщение «Указанный файл пуст».
* Пользователь приложения может случайно указать файл с некорректным содержимым: вещественными числами или текстовыми данными. Если программа не может корректно считать целые числа из файла, в статусбаре необходимо отобразить «Файл содержит некорректные данные».

Во всех трех случаях следует обнулить поле вывода.

Класс, реализующий окно приложения и наследующийся от `QMainWindow`, назовите `FileStat`. Поле ввода названия файла — `filenameEdit`, кнопку — `button`. Поле для вывода назовите `textBrowser`.

![file_stat.gif](./statement-file.gif)

"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextBrowser


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filenameEdit = QLineEdit()
        self.button = QPushButton("Считать")
        self.textBrowser = QTextBrowser()
        central = QWidget()
        lay = QVBoxLayout(central)
        lay.addWidget(self.filenameEdit)
        lay.addWidget(self.button)
        lay.addWidget(self.textBrowser)
        self.setCentralWidget(central)
        self.button.clicked.connect(self.min_med_max)

    def min_med_max(self):
        self.textBrowser.setPlainText("")
        try:
            with open(self.filenameEdit.text(), encoding="utf-8") as f:
                parts = f.read().split()
        except OSError:
            self.statusBar().showMessage("Указанный файл не существует")
            return
        if not parts:
            self.statusBar().showMessage("Указанный файл пуст")
            return
        try:
            lst = [int(x) for x in parts]
        except ValueError:
            self.statusBar().showMessage("Файл содержит некорректные данные")
            return
        res = (
            f"Максимальное значение = {max(lst)}\n"
            f"Минимальное значение = {min(lst)}\n"
            f"Среднее значение = {sum(lst) / len(lst):.2f}"
        )
        self.textBrowser.setPlainText(res)
        self.statusBar().showMessage(res.replace("\n", "; "))
        with open("out.txt", "w", encoding="utf-8") as f:
            f.write(res)


def main():
    app = QApplication(sys.argv)
    w = FileStat()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
