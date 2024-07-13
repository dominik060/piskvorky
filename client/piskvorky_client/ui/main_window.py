from email.message import Message
from .overview_view import OverviewView
from .generated import Ui_MainWindow
from .game_view import GameView
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
from PySide6.QtCore import Slot
from .. import api_client
import webbrowser





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

    def deleteAccount(self):
        msg_box = QMessageBox()
        msg_box.setText("Do you want to delete your account?")
        msg_box.setInformativeText("Your account will be forever lost.")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        if msg_box.exec() == QMessageBox.Yes:
            api_client.API_CLIENT.delete_account()
            exit(0)

    def xd(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        exit(1)


    @Slot()
    def end_game(self): 
        self.setCentralWidget(OverviewView())

    @Slot()
    def new_game(self): 
        view = GameView()
        view.end_game.connect(self.end_game)
        self.setCentralWidget(view)
