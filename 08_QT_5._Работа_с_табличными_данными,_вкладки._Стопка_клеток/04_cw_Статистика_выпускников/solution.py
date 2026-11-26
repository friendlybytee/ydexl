import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QTableWidget,
                             QVBoxLayout, QWidget, QHeaderView, QPushButton,
                             QFileDialog, QMessageBox, QTableWidgetItem)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Статистика выпускников")
        self.setGeometry(100, 100, 1000, 600)

        self.headers = []
        self.rows = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.open_button = QPushButton("Открыть файл")
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        self.create_empty_tabs()

    def create_empty_tabs(self):
        data_widget = QWidget()
        data_layout = QVBoxLayout(data_widget)
        self.data_table = QTableWidget()
        data_layout.addWidget(self.data_table)
        self.tab_widget.addTab(data_widget, "Данные")

        count_widget = QWidget()
        count_layout = QVBoxLayout(count_widget)
        self.count_table = QTableWidget()
        count_layout.addWidget(self.count_table)
        self.tab_widget.addTab(count_widget, "Численность выпускников")

        match_widget = QWidget()
        match_layout = QVBoxLayout(match_widget)
        self.match_table = QTableWidget()
        match_layout.addWidget(self.match_table)
        self.tab_widget.addTab(match_widget, "Соответствует")

        no_match_widget = QWidget()
        no_match_layout = QVBoxLayout(no_match_widget)
        self.no_match_table = QTableWidget()
        no_match_layout.addWidget(self.no_match_table)
        self.tab_widget.addTab(no_match_widget, "Не соответствует")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "CSV (*.csv);;Все файлы (*)"
        )

        if file_path:
            try:
                self.load_csv_data(file_path)
                self.update_tables()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def load_csv_data(self, filename):
        self.headers = []
        self.rows = []

        with open(filename, encoding="utf-8-sig") as f:
            data = list(csv.reader(f, delimiter=";"))
        self.headers = data[0]
        self.rows = [r for r in data[1:] if r]

    def update_tables(self):
        self.update_data_table()
        self.update_count_table()
        self.update_match_table()
        self.update_no_match_table()

    def fill(self, table, cols, head):
        table.setSortingEnabled(False)
        table.setColumnCount(len(cols))
        table.setHorizontalHeaderLabels(head)
        table.setRowCount(len(self.rows))
        for i, r in enumerate(self.rows):
            for j, c in enumerate(cols):
                table.setItem(i, j, QTableWidgetItem(r[c]))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setSortingEnabled(True)

    def update_data_table(self):
        self.fill(self.data_table, range(len(self.headers)), self.headers)

    def update_count_table(self):
        self.fill(self.count_table, [0, 1], ["Специальность", "Численность выпускников, тыс. чел."])

    def update_match_table(self):
        self.fill(self.match_table, [0, 2, 4], ["Специальность", "Соответствует, тыс. чел.", "Соответствует, %"])

    def update_no_match_table(self):
        self.fill(self.no_match_table, [0, 3, 5], ["Специальность", "Не соответствует, тыс. чел.", "Не соответствует, %"])


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
