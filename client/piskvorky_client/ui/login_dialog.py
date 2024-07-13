from ..api_client import ApiClient
from .generated import Ui_LoginDialog
from PySide6.QtWidgets import QDialog
from typing import Tuple, Optional


class LoginDialog(QDialog):
    """Dialog to login"""

    ui: Ui_LoginDialog
    api_client: Optional[ApiClient] = None

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

    def reject(self):
        exit(1)
    
    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        addr = self.ui.addrEdit.text()
        self.api_client = ApiClient(addr, username, password)
        if self.api_client.validate_credentials():
           self.accept()
        else:
            self.reject()
            


    def register(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        addr = self.ui.addrEdit.text()
        self.api_client = ApiClient.register(addr, username, password)
        self.accept()



    def exec(self) -> ApiClient:
        super().exec()
        return self.api_client
