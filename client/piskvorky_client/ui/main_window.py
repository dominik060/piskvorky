from .overview_view import OverviewView
from .generated import Ui_MainWindow
from .game_view import GameView
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Slot





class MainWindow(QMainWindow):
    """Main application window"""

    ui: Ui_MainWindow
    

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.overview_view()

        
    def overview_view(self):
        view = OverviewView()
        view.new_game.connect(self.new_game)
        self.setCentralWidget(view)

    @Slot()
    def end_game(self): 
        self.setCentralWidget(OverviewView())

    @Slot()
    def new_game(self): 
        view = GameView()
        view.end_game.connect(self.end_game)
        self.setCentralWidget(view)
