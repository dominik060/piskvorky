from PySide6.QtWidgets import QPushButton

class XoBox(QPushButton):
    """X or O box in the board"""

    x: int
    y: int

    def __init__(self, x:int, y:int):
        super(XoBox, self).__init__()
        self.x = x
        self.y = y
    