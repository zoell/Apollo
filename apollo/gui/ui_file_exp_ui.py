# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_exp_uiBqrqfY.ui'
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
            MainWindow.setObjectName(u"FileExp_MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QSize(500, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"FileExp_centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"FileExp_gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"FileExp_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"FileExp_buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1, Qt.AlignBottom)

        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"FileExp_treeView")

        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("FileExp_MainWindow", u"File Explorer", None))
        self.label.setText(QCoreApplication.translate("FileExp_MainWindow", u"TextLabel", None))
    # retranslateUi

