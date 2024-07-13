# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(520, 452)
        self.gridLayoutWidget = QWidget(LoginDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 481, 429))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Ubuntu Condensed"])
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.addrEdit = QLineEdit(self.gridLayoutWidget)
        self.addrEdit.setObjectName(u"addrEdit")
        font1 = QFont()
        font1.setPointSize(11)
        self.addrEdit.setFont(font1)

        self.verticalLayout.addWidget(self.addrEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.username = QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName(u"username")

        self.verticalLayout.addWidget(self.username)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.password = QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName(u"password")

        self.verticalLayout.addWidget(self.password)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.loginButton = QPushButton(self.gridLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        font2 = QFont()
        font2.setPointSize(14)
        self.loginButton.setFont(font2)

        self.verticalLayout.addWidget(self.loginButton)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.registerButton = QPushButton(self.gridLayoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setFont(font2)

        self.verticalLayout.addWidget(self.registerButton)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.retranslateUi(LoginDialog)
        self.loginButton.clicked.connect(LoginDialog.login)
        self.registerButton.clicked.connect(LoginDialog.register)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"Log in", None))
        self.addrEdit.setText(QCoreApplication.translate("LoginDialog", u"localhost:5000", None))
        self.addrEdit.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Server adress", None))
        self.username.setInputMask("")
        self.username.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginDialog", u"Log in", None))
        self.registerButton.setText(QCoreApplication.translate("LoginDialog", u"Register", None))
    # retranslateUi

