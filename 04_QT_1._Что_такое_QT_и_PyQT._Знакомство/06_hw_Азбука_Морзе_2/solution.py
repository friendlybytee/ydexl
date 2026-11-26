import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget

CODES = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
         "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Азбука Морзе 2")
        lay = QGridLayout(self)
        self.alphabet_buttons = {}
        for i in range(26):
            c = chr(ord("a") + i)
            b = QPushButton(c)
            b.clicked.connect(self.add)
            self.alphabet_buttons[c] = b
            lay.addWidget(b, i // 15, i % 15)
        self.result = QLineEdit()
        lay.addWidget(self.result, 2, 0, 1, 15)

    def add(self):
        c = self.sender().text()
        self.result.setText(self.result.text() + CODES[ord(c) - ord("a")])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MorseCode()
    w.show()
    sys.exit(app.exec())
