import sys

from PyQt6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout,
                             QMainWindow, QPlainTextEdit, QPushButton,
                             QVBoxLayout, QWidget)


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Антиплагиат")
        self.alert_value = QDoubleSpinBox()
        self.alert_value.setRange(0, 100)
        self.alert_value.setValue(50)
        self.text1 = QPlainTextEdit()
        self.text2 = QPlainTextEdit()
        self.checkBtn = QPushButton("Проверить")
        self.checkBtn.clicked.connect(self.check)
        texts = QHBoxLayout()
        texts.addWidget(self.text1)
        texts.addWidget(self.text2)
        main = QVBoxLayout()
        main.addWidget(self.alert_value)
        main.addLayout(texts)
        main.addWidget(self.checkBtn)
        central = QWidget()
        central.setLayout(main)
        self.setCentralWidget(central)

    def check(self):
        a = set(self.text1.toPlainText().split("\n"))
        b = set(self.text2.toPlainText().split("\n"))
        total = len(a | b)
        p = len(a & b) / total * 100
        if p >= self.alert_value.value():
            msg = f"Тексты похожи на {p:.2f}%, плагиат"
        else:
            msg = f"Тексты похожи на {p:.2f}%, не плагиат"
        self.statusBar().showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AntiPlagiarism()
    w.show()
    sys.exit(app.exec())
