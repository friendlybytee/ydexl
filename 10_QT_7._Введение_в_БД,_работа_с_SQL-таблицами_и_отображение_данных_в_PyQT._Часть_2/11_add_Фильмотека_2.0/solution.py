import sqlite3
import sys
from datetime import date
from PyQt6.QtWidgets import (QApplication, QComboBox, QMainWindow, QMessageBox, QPlainTextEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QTabWidget, QWidget)


def fill(table, head, rows):
    table.setColumnCount(len(head))
    table.setHorizontalHeaderLabels(head)
    table.setRowCount(len(rows))
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            table.setItem(i, j, QTableWidgetItem(str(v)))


def ids(table):
    return sorted({int(table.item(x.row(), 0).text()) for x in table.selectedItems()})


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 500)
        self.setWindowTitle("Фильмотека 2.0")
        self.con = sqlite3.connect("films_db.sqlite")
        self.tabWidget = QTabWidget(self)
        self.setCentralWidget(self.tabWidget)
        self.filmsTab = QWidget()
        self.genresTab = QWidget()
        self.tabWidget.addTab(self.filmsTab, "Фильмы")
        self.tabWidget.addTab(self.genresTab, "Жанры")

        self.filmsTable = QTableWidget(self.filmsTab)
        self.filmsTable.setGeometry(10, 50, 660, 380)
        self.addFilmButton = QPushButton("Добавить", self.filmsTab)
        self.addFilmButton.setGeometry(10, 10, 120, 30)
        self.editFilmButton = QPushButton("Изменить", self.filmsTab)
        self.editFilmButton.setGeometry(140, 10, 120, 30)
        self.deleteFilmButton = QPushButton("Удалить", self.filmsTab)
        self.deleteFilmButton.setGeometry(270, 10, 120, 30)

        self.genresTable = QTableWidget(self.genresTab)
        self.genresTable.setGeometry(10, 50, 660, 380)
        self.addGenreButton = QPushButton("Добавить", self.genresTab)
        self.addGenreButton.setGeometry(10, 10, 120, 30)
        self.editGenreButton = QPushButton("Изменить", self.genresTab)
        self.editGenreButton.setGeometry(140, 10, 120, 30)
        self.deleteGenreButton = QPushButton("Удалить", self.genresTab)
        self.deleteGenreButton.setGeometry(270, 10, 120, 30)

        self.add_film_widget = None
        self.edit_film_widget = None
        self.add_genre_widget = None
        self.edit_genre_widget = None

        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton.clicked.connect(self.delete_film)
        self.addGenreButton.clicked.connect(self.add_genre)
        self.editGenreButton.clicked.connect(self.edit_genre)
        self.deleteGenreButton.clicked.connect(self.delete_genre)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.update_films()
        self.update_genres()

    def tab_changed(self, index):
        if index == 0:
            self.update_films()
        else:
            self.update_genres()

    def update_films(self):
        rows = self.con.execute("SELECT films.id, films.title, films.year, ifnull(genres.title, films.genre), "
                                "films.duration FROM films LEFT JOIN genres ON films.genre = genres.id "
                                "ORDER BY films.id DESC").fetchall()
        fill(self.filmsTable, ["ИД", "Название", "Год", "Жанр", "Длительность"], rows)

    def update_genres(self):
        rows = self.con.execute("SELECT id, title FROM genres ORDER BY id").fetchall()
        fill(self.genresTable, ["ИД", "Название"], rows)

    def add_film(self):
        self.add_film_widget = AddFilmWidget(self)
        self.add_film_widget.show()

    def edit_film(self):
        a = ids(self.filmsTable)
        if not a:
            self.statusBar().showMessage("Ничего не выбрано")
            return
        self.statusBar().showMessage("")
        self.edit_film_widget = AddFilmWidget(self, a[0])
        self.edit_film_widget.show()

    def delete_film(self):
        a = ids(self.filmsTable)
        if not a:
            self.statusBar().showMessage("Ничего не выбрано")
            return
        self.statusBar().showMessage("")
        s = ", ".join(map(str, a))
        if QMessageBox.question(self, "", f"Действительно удалить элементы с id {s}?") == QMessageBox.StandardButton.Yes:
            self.con.execute(f"DELETE FROM films WHERE id IN ({s})")
            self.con.commit()
            self.update_films()

    def add_genre(self):
        self.add_genre_widget = AddGenreWidget(self)
        self.add_genre_widget.show()

    def edit_genre(self):
        a = ids(self.genresTable)
        if not a:
            self.statusBar().showMessage("Ничего не выбрано")
            return
        self.statusBar().showMessage("")
        self.edit_genre_widget = AddGenreWidget(self, a[0])
        self.edit_genre_widget.show()

    def delete_genre(self):
        a = ids(self.genresTable)
        if not a:
            self.statusBar().showMessage("Ничего не выбрано")
            return
        self.statusBar().showMessage("")
        s = ", ".join(map(str, a))
        if QMessageBox.question(self, "", f"Действительно удалить элементы с id {s}?") == QMessageBox.StandardButton.Yes:
            self.con.execute(f"DELETE FROM genres WHERE id IN ({s})")
            self.con.commit()
            self.update_genres()


class AddFilmWidget(QMainWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.resize(300, 250)
        self.setWindowTitle("Добавление записи")
        w = QWidget(self)
        self.setCentralWidget(w)
        self.title = QPlainTextEdit(w)
        self.title.setGeometry(10, 10, 280, 30)
        self.year = QPlainTextEdit(w)
        self.year.setGeometry(10, 50, 280, 30)
        self.duration = QPlainTextEdit(w)
        self.duration.setGeometry(10, 90, 280, 30)
        self.comboBox = QComboBox(w)
        self.comboBox.setGeometry(10, 130, 280, 30)
        self.pushButton = QPushButton("Добавить", w)
        self.pushButton.setGeometry(10, 170, 280, 30)
        self.con = sqlite3.connect("films_db.sqlite")
        self.params = dict(self.con.execute("SELECT title, id FROM genres").fetchall())
        self.comboBox.addItems(self.params)
        self.film_id = film_id
        self.genre = None
        if film_id is None:
            self.pushButton.clicked.connect(self.get_adding_verdict)
        else:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText("Отредактировать")
            self.setWindowTitle("Редактирование записи")
            self.get_elem()

    def get_elem(self):
        t, y, g, d = self.con.execute("SELECT title, year, genre, duration FROM films WHERE id = ?",
                                      (self.film_id,)).fetchone()
        self.title.setPlainText(str(t))
        self.year.setPlainText(str(y))
        self.duration.setPlainText(str(d))
        names = [k for k in self.params if self.params[k] == g]
        if names:
            self.comboBox.setCurrentText(names[0])
        else:
            self.genre = g
            self.comboBox.addItem(str(g))
            self.comboBox.setCurrentText(str(g))

    def read(self):
        t = self.title.toPlainText().strip()
        y = self.year.toPlainText().strip()
        d = self.duration.toPlainText().strip()
        if not t or not y.isdigit() or not d.isdigit() or int(y) > date.today().year or int(d) <= 0 \
                or self.comboBox.currentIndex() < 0:
            self.statusBar().showMessage("Неверно заполнена форма")
            return None
        return t, int(y), self.params.get(self.comboBox.currentText(), self.genre), int(d)

    def get_adding_verdict(self):
        a = self.read()
        if a is None:
            return False
        self.con.execute("INSERT INTO films (title, year, genre, duration) VALUES (?, ?, ?, ?)", a)
        self.con.commit()
        self.parent().update_films()
        self.close()
        return True

    def get_editing_verdict(self):
        a = self.read()
        if a is None:
            return False
        self.con.execute("UPDATE films SET title = ?, year = ?, genre = ?, duration = ? WHERE id = ?",
                         a + (self.film_id,))
        self.con.commit()
        self.parent().update_films()
        self.close()
        return True


class AddGenreWidget(QMainWindow):
    def __init__(self, parent=None, genre_id=None):
        super().__init__(parent)
        self.resize(300, 120)
        self.setWindowTitle("Добавление жанра")
        w = QWidget(self)
        self.setCentralWidget(w)
        self.title = QPlainTextEdit(w)
        self.title.setGeometry(10, 10, 280, 30)
        self.pushButton = QPushButton("Добавить", w)
        self.pushButton.setGeometry(10, 50, 280, 30)
        self.con = sqlite3.connect("films_db.sqlite")
        self.genre_id = genre_id
        if genre_id is None:
            self.pushButton.clicked.connect(self.get_adding_verdict)
        else:
            self.pushButton.clicked.connect(self.get_editing_verdict)
            self.pushButton.setText("Отредактировать")
            self.setWindowTitle("Редактирование жанра")
            t = self.con.execute("SELECT title FROM genres WHERE id = ?", (genre_id,)).fetchone()[0]
            self.title.setPlainText(str(t))

    def get_adding_verdict(self):
        t = self.title.toPlainText().strip()
        if not t:
            self.statusBar().showMessage("Неверно заполнена форма")
            return False
        self.con.execute("INSERT INTO genres (title) VALUES (?)", (t,))
        self.con.commit()
        self.parent().update_genres()
        self.close()
        return True

    def get_editing_verdict(self):
        t = self.title.toPlainText().strip()
        if not t:
            self.statusBar().showMessage("Неверно заполнена форма")
            return False
        self.con.execute("UPDATE genres SET title = ? WHERE id = ?", (t, self.genre_id))
        self.con.commit()
        self.parent().update_genres()
        self.close()
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
