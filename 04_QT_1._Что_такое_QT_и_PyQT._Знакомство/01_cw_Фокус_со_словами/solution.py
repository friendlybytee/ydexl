import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QWidget


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Фокус со словами")
        self.first_value = QLineEdit()
        self.trick_button = QPushButton("->")
        self.second_value = QLineEdit()
        self.trick_button.clicked.connect(self.trick)
        lay = QHBoxLayout(self)
        lay.addWidget(self.first_value)
        lay.addWidget(self.trick_button)
        lay.addWidget(self.second_value)

    def trick(self):
        if self.trick_button.text() == "->":
            self.second_value.setText(self.first_value.text())
            self.first_value.setText("")
            self.trick_button.setText("<-")
        else:
            self.first_value.setText(self.second_value.text())
            self.second_value.setText("")
            self.trick_button.setText("->")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WordTrick()
    w.show()
    sys.exit(app.exec())
