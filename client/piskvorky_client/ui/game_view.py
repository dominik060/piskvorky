from .xobox import XoBox
from .generated import Ui_GameView
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal


class GameView(QWidget):
    """Game board"""

    ui: Ui_GameView
    end_game = Signal()

    def __init__(self):
        super(GameView, self).__init__()
        self.ui = Ui_GameView()
        self.ui.setupUi(self)
        self.generate_board()
        

    def generate_board(self):
        for y in range(5):
            for x in range(5):
                xobox = XoBox(x, y)
                xobox.clicked.connect(self.xobox_clicked)
                self.ui.gameField.addWidget(xobox, y, x)

    @Slot()
    def xobox_clicked(self): 
        sender = self.sender()
        sender.setText("X")
        sender.setDisabled(True)
        print(f"x = {sender.x}, y ={sender.y}")


    def giveUpClicked(self):
        self.end_game.emit()