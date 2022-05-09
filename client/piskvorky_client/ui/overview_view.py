from .generated import Ui_OverviewView
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

class OverviewView(QWidget):
    """Widget to display match statistic"""

    ui: Ui_OverviewView
    new_game = Signal()

    def __init__(self):
        super(OverviewView, self).__init__()
        self.ui = Ui_OverviewView()
        self.ui.setupUi(self)

    
    def newGameClicked(self):
        self.new_game.emit()
        