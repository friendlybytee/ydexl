import csv
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextBrowser

COLORS = ["Cornsilk", "BlanchedAlmond", "Bisque", "NavajoWhite", "Wheat", "BurlyWood", "Tan"]


class CatBreeds(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lineEdit = QLineEdit()
        self.textBrowser = QTextBrowser()
        central = QWidget()
        lay = QVBoxLayout(central)
        lay.addWidget(self.lineEdit)
        lay.addWidget(self.textBrowser)
        self.setCentralWidget(central)
        try:
            with open("cat_breeds.csv", encoding="utf-8") as f:
                self.rows = list(csv.reader(f, delimiter=";"))[1:]
        except OSError:
            self.rows = []
        self.lineEdit.textChanged.connect(self.write)

    def write(self):
        sub = self.lineEdit.text().lower()
        res = []
        for row in self.rows:
            row = [x.strip() for x in row]
            if not row or sub not in row[0].lower():
                continue
            color = COLORS[len(res) % len(COLORS)]
            rest = "".join(", " + x for x in row[1:])
            res.append(f'<p style="background:{color}"><b>{row[0]}</b>{rest}</p>')
        self.textBrowser.setHtml("".join(res))


def main():
    app = QApplication(sys.argv)
    w = CatBreeds()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
