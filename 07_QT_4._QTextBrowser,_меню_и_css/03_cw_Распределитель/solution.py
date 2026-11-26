import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QFileDialog


class Distributor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_browser = QTextBrowser()
        self.setCentralWidget(self.text_browser)
        self.names = []
        file_menu = self.menuBar().addMenu("Файл")
        a = QAction("Открыть", self)
        a.triggered.connect(self.load_file)
        file_menu.addAction(a)
        a = QAction("Сохранить", self)
        a.triggered.connect(self.save_file)
        file_menu.addAction(a)
        spread_menu = self.menuBar().addMenu("Распределить")
        for title, ext in [("TXT", "txt"), ("CSV", "csv"), ("PNG", "png"), ("PY", "py"), ("Другие", "")]:
            a = QAction(title, self)
            a.triggered.connect(lambda checked, e=ext: self.spread(e))
            spread_menu.addAction(a)

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, "Открыть", "")[0]
        if not fname:
            return
        with open(fname, encoding="utf-8") as f:
            text = f.read()
        self.names = text.split()
        self.text_browser.setPlainText(text)

    def save_file(self):
        fname = QFileDialog.getSaveFileName(self, "Сохранить", "")[0]
        if not fname:
            return
        with open(fname, "w", encoding="utf-8") as f:
            f.write(self.text_browser.toPlainText())

    def spread(self, ext):
        if not self.names:
            return
        known = (".txt", ".csv", ".png", ".py")
        if ext:
            lst = [n for n in self.names if n.lower().endswith("." + ext)]
        else:
            lst = [n for n in self.names if not n.lower().endswith(known)]
        self.text_browser.setPlainText("\n".join(sorted(lst)))


def main():
    app = QApplication(sys.argv)
    w = Distributor()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
