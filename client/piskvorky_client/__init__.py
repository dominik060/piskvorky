from .ui import MainWindow, LoginDialog
from PySide6.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)

    # Create and show main window
    window = MainWindow()
    window.show()

    # Open login dialog
    username, password = LoginDialog().exec_()
    print(username, password)
    
    sys.exit(app.exec_())
