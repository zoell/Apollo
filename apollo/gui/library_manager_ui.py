# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Ommar/AppData/Local/Temp/library_manager_uimPdUus.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 578))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LBM_GBX_library = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.LBM_GBX_library.setMinimumSize(QtCore.QSize(0, 300))
        self.LBM_GBX_library.setObjectName("LBM_GBX_library")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.LBM_GBX_library)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 4)
        self.gridLayout_3.setSpacing(4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 4, 1, 1)
        self.LBM_PSB_libadd = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_libadd.setObjectName("LBM_PSB_libadd")
        self.gridLayout_3.addWidget(self.LBM_PSB_libadd, 2, 5, 1, 1)
        self.LBM_PSB_libremove = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_libremove.setObjectName("LBM_PSB_libremove")
        self.gridLayout_3.addWidget(self.LBM_PSB_libremove, 2, 6, 1, 1)
        self.LBM_PSB_libexport = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_libexport.setObjectName("LBM_PSB_libexport")
        self.gridLayout_3.addWidget(self.LBM_PSB_libexport, 2, 3, 1, 1)
        self.LBM_CMBX_dbname = QtWidgets.QComboBox(self.LBM_GBX_library)
        self.LBM_CMBX_dbname.setMinimumSize(QtCore.QSize(0, 24))
        self.LBM_CMBX_dbname.setMaximumSize(QtCore.QSize(16777215, 24))
        self.LBM_CMBX_dbname.setObjectName("LBM_CMBX_dbname")
        self.gridLayout_3.addWidget(self.LBM_CMBX_dbname, 0, 1, 1, 7)
        self.LBM_PSB_back = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_back.setMinimumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_back.setMaximumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_back.setObjectName("LBM_PSB_back")
        self.gridLayout_3.addWidget(self.LBM_PSB_back, 0, 0, 1, 1)
        self.LBM_PSB_fowd = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_fowd.setMinimumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fowd.setMaximumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fowd.setObjectName("LBM_PSB_fowd")
        self.gridLayout_3.addWidget(self.LBM_PSB_fowd, 0, 8, 1, 1)
        self.LBM_FR_library = QtWidgets.QFrame(self.LBM_GBX_library)
        self.LBM_FR_library.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LBM_FR_library.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LBM_FR_library.setObjectName("LBM_FR_library")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.LBM_FR_library)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(2)
        self.gridLayout_6.setVerticalSpacing(4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.LBM_LEDT_path = QtWidgets.QLineEdit(self.LBM_FR_library)
        self.LBM_LEDT_path.setMinimumSize(QtCore.QSize(0, 24))
        self.LBM_LEDT_path.setObjectName("LBM_LEDT_path")
        self.gridLayout_6.addWidget(self.LBM_LEDT_path, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.LBM_FR_library)
        self.label_2.setMinimumSize(QtCore.QSize(0, 24))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.LBM_FR_library)
        self.label.setMinimumSize(QtCore.QSize(0, 24))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.LBM_LEDT_name = QtWidgets.QLineEdit(self.LBM_FR_library)
        self.LBM_LEDT_name.setMinimumSize(QtCore.QSize(0, 24))
        self.LBM_LEDT_name.setObjectName("LBM_LEDT_name")
        self.gridLayout_6.addWidget(self.LBM_LEDT_name, 0, 1, 1, 2)
        self.LBM_PSB_fileexp = QtWidgets.QPushButton(self.LBM_FR_library)
        self.LBM_PSB_fileexp.setMinimumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fileexp.setMaximumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fileexp.setObjectName("LBM_PSB_fileexp")
        self.gridLayout_6.addWidget(self.LBM_PSB_fileexp, 1, 2, 1, 1)
        self.LBM_LSV_filters = QtWidgets.QListView(self.LBM_FR_library)
        self.LBM_LSV_filters.setObjectName("LBM_LSV_filters")
        self.gridLayout_6.addWidget(self.LBM_LSV_filters, 5, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.LBM_FR_library)
        self.label_4.setMinimumSize(QtCore.QSize(0, 24))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 4, 0, 1, 3)
        self.LBM_LSV_filesmon = QtWidgets.QListView(self.LBM_FR_library)
        self.LBM_LSV_filesmon.setObjectName("LBM_LSV_filesmon")
        self.gridLayout_6.addWidget(self.LBM_LSV_filesmon, 3, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.LBM_FR_library)
        self.label_3.setMinimumSize(QtCore.QSize(0, 24))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 2)
        self.LBM_PSB_fileexp_2 = QtWidgets.QPushButton(self.LBM_FR_library)
        self.LBM_PSB_fileexp_2.setMinimumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fileexp_2.setMaximumSize(QtCore.QSize(24, 24))
        self.LBM_PSB_fileexp_2.setObjectName("LBM_PSB_fileexp_2")
        self.gridLayout_6.addWidget(self.LBM_PSB_fileexp_2, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.LBM_FR_library, 1, 0, 1, 9)
        self.LBM_PSB_libimport = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_libimport.setObjectName("LBM_PSB_libimport")
        self.gridLayout_3.addWidget(self.LBM_PSB_libimport, 2, 0, 1, 3)
        self.LBM_PSB_librescan = QtWidgets.QPushButton(self.LBM_GBX_library)
        self.LBM_PSB_librescan.setObjectName("LBM_PSB_librescan")
        self.gridLayout_3.addWidget(self.LBM_PSB_librescan, 2, 7, 1, 2)
        self.gridLayout_2.addWidget(self.LBM_GBX_library, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LBM_GBX_library.setTitle(_translate("MainWindow", "Library Manager"))
        self.LBM_PSB_libadd.setText(_translate("MainWindow", "Add"))
        self.LBM_PSB_libremove.setText(_translate("MainWindow", "Remove"))
        self.LBM_PSB_libexport.setText(_translate("MainWindow", "Export"))
        self.LBM_PSB_back.setText(_translate("MainWindow", "<<"))
        self.LBM_PSB_fowd.setText(_translate("MainWindow", ">>"))
        self.label_2.setText(_translate("MainWindow", "DB Filepath"))
        self.label.setText(_translate("MainWindow", "DB Name"))
        self.LBM_PSB_fileexp.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Filters"))
        self.label_3.setText(_translate("MainWindow", "Files Monitored"))
        self.LBM_PSB_fileexp_2.setText(_translate("MainWindow", "..."))
        self.LBM_PSB_libimport.setText(_translate("MainWindow", "Import"))
        self.LBM_PSB_librescan.setText(_translate("MainWindow", "Rescan"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File Manager"))
        self.groupBox_3.setTitle(_translate("MainWindow", "File Metadata Editor"))
