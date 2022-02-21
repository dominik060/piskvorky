from curses import window
from .ui.main_window import MainWindow
from PySide2.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
