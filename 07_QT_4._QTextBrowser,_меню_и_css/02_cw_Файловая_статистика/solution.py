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
