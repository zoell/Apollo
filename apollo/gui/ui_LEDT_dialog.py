# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LEDT_dialogbZJdsy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"LEDT_Dialog_MainWindow")
        MainWindow.resize(360, 120)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"LEDT_Dialog_centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"LEDT_Dialog_gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"LEDT_Dialog_lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"LEDT_Dialog_buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1, Qt.AlignBottom)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LEDT_Dialog_MainWindow", None))
    # retranslateUi


class LEDT_Dialog(Ui_MainWindow, QMainWindow): # Untested
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.setupUi(self)
