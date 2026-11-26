import csv
import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QFileDialog

CLASSES = "OBAFGKM"
DISTANCES = [("до 10", -1, 10), ("до 20", 10, 20), ("до 30", 20, 30), ("свыше 30", 30, 10 ** 9)]


class ClosestStars(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.text_browser = QTextBrowser()
        self.setCentralWidget(self.text_browser)
        file_menu = self.menuBar().addMenu("Файл")
        a = QAction("Открыть", self)
        a.triggered.connect(self.load_file)
        file_menu.addAction(a)
        a = QAction("Сохранить", self)
        a.triggered.connect(self.save_file)
        file_menu.addAction(a)
        select_menu = self.menuBar().addMenu("Выбор")
        class_menu = select_menu.addMenu("Спектральный класс")
        for c in CLASSES:
            a = QAction(c, self)
            a.triggered.connect(lambda checked, c=c: self.by_class(c))
            class_menu.addAction(a)
        dist_menu = select_menu.addMenu("Расстояние")
        for title, lo, hi in DISTANCES:
            a = QAction(title, self)
            a.triggered.connect(lambda checked, t=title, lo=lo, hi=hi: self.by_distance(t, lo, hi))
            dist_menu.addAction(a)

    def load_file(self):
        fname = QFileDialog.getOpenFileName(self, "Открыть", "", "CSV (*.csv);;Все файлы (*)")[0]
        if not fname:
            return
        with open(fname, encoding="utf-8") as f:
            self.text = f.read()

    def save_file(self):
        fname = QFileDialog.getSaveFileName(self, "Сохранить", "")[0]
        if not fname:
            return
        with open(fname, "w", encoding="utf-8") as f:
            f.write(self.text_browser.toPlainText())

    def rows(self):
        return list(csv.reader(self.text.splitlines(), delimiter=";"))[1:]

    def show_stars(self, title, names):
        res = f"<h3>{title}</h3>"
        for n in sorted(names):
            res += f"<p>{n}</p>"
        self.text_browser.setHtml(res)

    def name(self, row):
        return f"{row[0]} {row[1]}" if row[1] else row[0]

    def by_class(self, c):
        names = [self.name(r) for r in self.rows() if r[2].startswith(c)]
        self.show_stars(f"Спектральный класс {c}", names)

    def by_distance(self, title, lo, hi):
        names = [self.name(r) for r in self.rows() if lo < float(r[7]) <= hi]
        self.show_stars(f"Расстояние {title}", names)


def main():
    app = QApplication(sys.argv)
    w = ClosestStars()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
