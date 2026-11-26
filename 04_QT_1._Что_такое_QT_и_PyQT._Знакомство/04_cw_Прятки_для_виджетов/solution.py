import sys

from PyQt6.QtWidgets import QApplication, QCheckBox, QGridLayout, QLineEdit, QWidget


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Прятки для виджетов")
        lay = QGridLayout(self)
        for i in range(1, 5):
            cb = QCheckBox(f"edit{i}")
            cb.setChecked(True)
            cb.toggled.connect(self.toggle)
            e = QLineEdit()
            setattr(self, f"checkbox{i}", cb)
            setattr(self, f"edit{i}", e)
            lay.addWidget(cb, i, 0)
            lay.addWidget(e, i, 1)

    def toggle(self, on):
        e = getattr(self, self.sender().text())
        e.setVisible(on)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WidgetsHideNSeek()
    w.show()
    sys.exit(app.exec())
