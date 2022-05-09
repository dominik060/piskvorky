from .generated import Ui_LoginDialog
from PySide6.QtWidgets import QDialog
from typing import Tuple


class LoginDialog(QDialog):
    """Dialog to login"""

    ui: Ui_LoginDialog

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)


    def reject(self):
        exit(1)
    
    def exec_(self) -> Tuple[str, str]:
        super().exec_()
        username = self.ui.username.text()
        password = self.ui.password.text()

        return username, password
