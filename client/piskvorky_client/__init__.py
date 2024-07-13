from .ui import MainWindow, LoginDialog
from PySide6.QtWidgets import QApplication
import sys

from . import api_client 

def main():
    app = QApplication(sys.argv)

    # Open login dialog
    api_client.API_CLIENT = LoginDialog().exec()

    # Create and show main window
    window = MainWindow()
    window.show()

    
    sys.exit(app.exec())
