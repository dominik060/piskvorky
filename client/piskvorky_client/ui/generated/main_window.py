# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionDelete_account = QAction(MainWindow)
        self.actionDelete_account.setObjectName(u"actionDelete_account")
        self.actionxd = QAction(MainWindow)
        self.actionxd.setObjectName(u"actionxd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuAccount = QMenu(self.menubar)
        self.menuAccount.setObjectName(u"menuAccount")
        self.menuxd = QMenu(self.menubar)
        self.menuxd.setObjectName(u"menuxd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuxd.menuAction())
        self.menuAccount.addAction(self.actionDelete_account)
        self.menuxd.addAction(self.actionxd)

        self.retranslateUi(MainWindow)
        self.actionDelete_account.triggered.connect(MainWindow.deleteAccount)
        self.actionxd.triggered.connect(MainWindow.xd)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDelete_account.setText(QCoreApplication.translate("MainWindow", u"Delete account", None))
        self.actionxd.setText(QCoreApplication.translate("MainWindow", u"xd", None))
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuxd.setTitle(QCoreApplication.translate("MainWindow", u"xd", None))
    # retranslateUi

