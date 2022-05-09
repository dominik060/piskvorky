# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overview_view.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_OverviewView(object):
    def setupUi(self, OverviewView):
        if not OverviewView.objectName():
            OverviewView.setObjectName(u"OverviewView")
        OverviewView.resize(965, 775)
        self.verticalLayout_2 = QVBoxLayout(OverviewView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(OverviewView)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)

        self.verticalLayout.addWidget(self.tableView)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.pushButton = QPushButton(OverviewView)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 40))
        palette = QPalette()
        brush = QBrush(QColor(36, 31, 49, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(98, 160, 234, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        brush2 = QBrush(QColor(190, 190, 190, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.pushButton.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setIconSize(QSize(16, 20))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.retranslateUi(OverviewView)
        self.pushButton.clicked.connect(OverviewView.newGameClicked)

        QMetaObject.connectSlotsByName(OverviewView)
    # setupUi

    def retranslateUi(self, OverviewView):
        OverviewView.setWindowTitle(QCoreApplication.translate("OverviewView", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("OverviewView", u"Odehran\u00e9 hry", None))
        self.label.setText(QCoreApplication.translate("OverviewView", u"Losses", None))
        self.label_2.setText(QCoreApplication.translate("OverviewView", u"Wins", None))
        self.label_3.setText(QCoreApplication.translate("OverviewView", u"Ties", None))
        self.label_4.setText(QCoreApplication.translate("OverviewView", u"0", None))
        self.label_5.setText(QCoreApplication.translate("OverviewView", u"0", None))
        self.label_6.setText(QCoreApplication.translate("OverviewView", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("OverviewView", u"New game", None))
    # retranslateUi

