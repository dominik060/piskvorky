# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_view.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_GameView(object):
    def setupUi(self, GameView):
        if not GameView.objectName():
            GameView.setObjectName(u"GameView")
        GameView.resize(600, 800)
        GameView.setMaximumSize(QSize(100000, 100000))
        self.verticalLayout = QVBoxLayout(GameView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameField = QGridLayout()
        self.gameField.setObjectName(u"gameField")

        self.verticalLayout.addLayout(self.gameField)

        self.pushButton = QPushButton(GameView)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(GameView)
        self.pushButton.clicked.connect(GameView.giveUpClicked)

        QMetaObject.connectSlotsByName(GameView)
    # setupUi

    def retranslateUi(self, GameView):
        GameView.setWindowTitle(QCoreApplication.translate("GameView", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("GameView", u"Vzd\u00e1t se", None))
    # retranslateUi

