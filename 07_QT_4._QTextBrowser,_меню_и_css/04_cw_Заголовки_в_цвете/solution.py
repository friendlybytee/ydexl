import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit,
                             QComboBox, QPushButton, QTextBrowser)


class HeadersInColor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = []
        self.lineEdit = QLineEdit()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["h1", "h2", "h3", "h4", "h5", "h6", "p"])
        self.comboBox.setCurrentText("p")
        self.lineEdit_2 = QLineEdit("black")
        self.pushButton = QPushButton("Вывести")
        self.pushButton_2 = QPushButton("Очистить")
        self.textBrowser = QTextBrowser()
        central = QWidget()
        lay = QVBoxLayout(central)
        for w in (self.lineEdit, self.comboBox, self.lineEdit_2, self.pushButton,
                  self.pushButton_2, self.textBrowser):
            lay.addWidget(w)
        self.setCentralWidget(central)
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)

    def write_text(self):
        tag = self.comboBox.currentText()
        color = self.lineEdit_2.text().strip() or "black"
        self.text.append(f'<{tag} style="color:{color}">{self.lineEdit.text()}</{tag}>')
        self.textBrowser.setHtml("".join(self.text))

    def clear_text(self):
        self.text = []
        self.textBrowser.setHtml("")


def main():
    app = QApplication(sys.argv)
    w = HeadersInColor()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
