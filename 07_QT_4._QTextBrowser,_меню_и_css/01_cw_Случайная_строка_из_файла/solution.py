import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser
import random


class RandomString(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Показать")
        self.textBrowser = QTextBrowser()
        lay = QVBoxLayout(self)
        lay.addWidget(self.button)
        lay.addWidget(self.textBrowser)
        self.button.clicked.connect(self.load_random_string)

    def load_random_string(self):
        try:
            with open("lines.txt", encoding="utf-8") as f:
                lst = f.read().splitlines()
        except OSError:
            lst = []
        if lst:
            self.textBrowser.setHtml(f"<h1>{random.choice(lst)}</h1>")
        else:
            self.textBrowser.setHtml("")


def main():
    app = QApplication(sys.argv)
    w = RandomString()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
