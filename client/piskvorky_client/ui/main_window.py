from .generated import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Main application window"""

    ui: Ui_MainWindow

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
