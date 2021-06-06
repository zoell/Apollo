# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library_manager_uivZynzS.ui'
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
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.LBM_WDG_centeral = QWidget(MainWindow)
        self.LBM_WDG_centeral.setObjectName(u"LBM_WDG_centeral")
        self.LBM_WDG_centeral.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.LBM_WDG_centeral)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.LBM_TABWG_main = QTabWidget(self.LBM_WDG_centeral)
        self.LBM_TABWG_main.setObjectName(u"LBM_TABWG_main")
        self.LBM_TABWG_main.setTabShape(QTabWidget.Rounded)
        self.LBM_TABWG_main.setIconSize(QSize(16, 16))
        self.LBM_TABWG_main.setDocumentMode(False)
        self.LBM_WDG_LBT = QWidget()
        self.LBM_WDG_LBT.setObjectName(u"LBM_WDG_LBT")
        self.gridLayout_2 = QGridLayout(self.LBM_WDG_LBT)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LBT_PSB_libprev = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_libprev.setObjectName(u"LBT_PSB_libprev")
        self.LBT_PSB_libprev.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_libprev.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.LBT_PSB_libprev)

        self.LBT_CMBX_libname = QComboBox(self.LBM_WDG_LBT)
        self.LBT_CMBX_libname.setObjectName(u"LBT_CMBX_libname")
        self.LBT_CMBX_libname.setMinimumSize(QSize(24, 24))
        self.LBT_CMBX_libname.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout.addWidget(self.LBT_CMBX_libname)

        self.LBT_PSB_libnext = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_libnext.setObjectName(u"LBT_PSB_libnext")
        self.LBT_PSB_libnext.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_libnext.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.LBT_PSB_libnext)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.LBT_SCAR_main = QScrollArea(self.LBM_WDG_LBT)
        self.LBT_SCAR_main.setObjectName(u"LBT_SCAR_main")
        self.LBT_SCAR_main.setFrameShape(QFrame.StyledPanel)
        self.LBT_SCAR_main.setWidgetResizable(True)
        self.LBT_WDG_SCARmain = QWidget()
        self.LBT_WDG_SCARmain.setObjectName(u"LBT_WDG_SCARmain")
        self.LBT_WDG_SCARmain.setGeometry(QRect(0, 0, 767, 534))
        self.gridLayout_3 = QGridLayout(self.LBT_WDG_SCARmain)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(4)
        self.gridLayout_3.setContentsMargins(0, 4, 0, 4)
        self.frame_4 = QFrame(self.LBT_WDG_SCARmain)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(4, 0, 4, 0)
        self.LBT_GBX_libstat = QGroupBox(self.frame_4)
        self.LBT_GBX_libstat.setObjectName(u"LBT_GBX_libstat")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.LBT_GBX_libstat.sizePolicy().hasHeightForWidth())
        self.LBT_GBX_libstat.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.LBT_GBX_libstat)
        self.gridLayout_15.setSpacing(4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 4, 0, 4)
        self.frame_13 = QFrame(self.LBT_GBX_libstat)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(4, 0, 4, 0)
        self.label_24 = QLabel(self.frame_13)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(75, 24))
        self.label_24.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_15.addWidget(self.label_24)

        self.LBT_LEDT_totartist = QLineEdit(self.frame_13)
        self.LBT_LEDT_totartist.setObjectName(u"LBT_LEDT_totartist")
        self.LBT_LEDT_totartist.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_totartist.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_totartist.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.LBT_LEDT_totartist)


        self.gridLayout_15.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.LBT_GBX_libstat)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(4, 0, 4, 0)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMinimumSize(QSize(75, 24))
        self.label_16.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_11.addWidget(self.label_16)

        self.LBT_LEDT_topartist = QLineEdit(self.frame_10)
        self.LBT_LEDT_topartist.setObjectName(u"LBT_LEDT_topartist")
        self.LBT_LEDT_topartist.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_topartist.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_topartist.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.LBT_LEDT_topartist)


        self.gridLayout_15.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_9 = QFrame(self.LBT_GBX_libstat)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(4, 0, 4, 0)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(75, 24))
        self.label_21.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_12.addWidget(self.label_21)

        self.LBT_LEDT_totalbum = QLineEdit(self.frame_9)
        self.LBT_LEDT_totalbum.setObjectName(u"LBT_LEDT_totalbum")
        self.LBT_LEDT_totalbum.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_totalbum.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_totalbum.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.LBT_LEDT_totalbum)


        self.gridLayout_15.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame_8 = QFrame(self.LBT_GBX_libstat)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(4, 0, 4, 0)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setMinimumSize(QSize(75, 24))
        self.label_18.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_9.addWidget(self.label_18)

        self.LBT_LEDT_toptrack = QLineEdit(self.frame_8)
        self.LBT_LEDT_toptrack.setObjectName(u"LBT_LEDT_toptrack")
        self.LBT_LEDT_toptrack.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_toptrack.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_toptrack.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.LBT_LEDT_toptrack)


        self.gridLayout_15.addWidget(self.frame_8, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.LBT_GBX_libstat)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(4, 0, 4, 0)
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(75, 24))
        self.label_19.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_8.addWidget(self.label_19)

        self.LBT_LEDT_tottrack = QLineEdit(self.frame_6)
        self.LBT_LEDT_tottrack.setObjectName(u"LBT_LEDT_tottrack")
        self.LBT_LEDT_tottrack.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_tottrack.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_tottrack.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.LBT_LEDT_tottrack)


        self.gridLayout_15.addWidget(self.frame_6, 2, 0, 1, 1)

        self.frame_11 = QFrame(self.LBT_GBX_libstat)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(4, 0, 4, 0)
        self.label_22 = QLabel(self.frame_11)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setMinimumSize(QSize(75, 24))
        self.label_22.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_13.addWidget(self.label_22)

        self.LBT_LEDT_topalbum = QLineEdit(self.frame_11)
        self.LBT_LEDT_topalbum.setObjectName(u"LBT_LEDT_topalbum")
        self.LBT_LEDT_topalbum.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_topalbum.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_topalbum.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.LBT_LEDT_topalbum)


        self.gridLayout_15.addWidget(self.frame_11, 2, 1, 1, 1)

        self.frame_5 = QFrame(self.LBT_GBX_libstat)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, 0, 4, 0)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(75, 24))
        self.label_17.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_7.addWidget(self.label_17)

        self.LBT_LEDT_totplaytime = QLineEdit(self.frame_5)
        self.LBT_LEDT_totplaytime.setObjectName(u"LBT_LEDT_totplaytime")
        self.LBT_LEDT_totplaytime.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_totplaytime.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_totplaytime.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.LBT_LEDT_totplaytime)


        self.gridLayout_15.addWidget(self.frame_5, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.LBT_GBX_libstat)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(4, 0, 4, 0)
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setMinimumSize(QSize(75, 24))
        self.label_20.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_10.addWidget(self.label_20)

        self.LBT_LEDT_topgenre = QLineEdit(self.frame_7)
        self.LBT_LEDT_topgenre.setObjectName(u"LBT_LEDT_topgenre")
        self.LBT_LEDT_topgenre.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_topgenre.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_topgenre.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.LBT_LEDT_topgenre)


        self.gridLayout_15.addWidget(self.frame_7, 3, 1, 1, 1)

        self.frame_12 = QFrame(self.LBT_GBX_libstat)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(4, 0, 4, 0)
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(75, 24))
        self.label_23.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_14.addWidget(self.label_23)

        self.LBT_LEDT_totsize = QLineEdit(self.frame_12)
        self.LBT_LEDT_totsize.setObjectName(u"LBT_LEDT_totsize")
        self.LBT_LEDT_totsize.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_totsize.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_totsize.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.LBT_LEDT_totsize)


        self.gridLayout_15.addWidget(self.frame_12, 4, 0, 1, 1)

        self.frame_14 = QFrame(self.LBT_GBX_libstat)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(4, 0, 4, 0)
        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
        self.label_25.setMinimumSize(QSize(75, 24))
        self.label_25.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_16.addWidget(self.label_25)

        self.LBT_LEDT_totplay = QLineEdit(self.frame_14)
        self.LBT_LEDT_totplay.setObjectName(u"LBT_LEDT_totplay")
        self.LBT_LEDT_totplay.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_totplay.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_totplay.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.LBT_LEDT_totplay)


        self.gridLayout_15.addWidget(self.frame_14, 4, 1, 1, 1)


        self.gridLayout_4.addWidget(self.LBT_GBX_libstat, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 3, 0, 1, 1)

        self.frame_2 = QFrame(self.LBT_WDG_SCARmain)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 24))
        self.label_2.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.LBT_LEDT_dbpath = QLineEdit(self.frame_2)
        self.LBT_LEDT_dbpath.setObjectName(u"LBT_LEDT_dbpath")
        self.LBT_LEDT_dbpath.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_dbpath.setMaximumSize(QSize(16777215, 24))
        self.LBT_LEDT_dbpath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.LBT_LEDT_dbpath)

        self.LBT_PSB_libpathedit = QPushButton(self.frame_2)
        self.LBT_PSB_libpathedit.setObjectName(u"LBT_PSB_libpathedit")
        self.LBT_PSB_libpathedit.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_libpathedit.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.LBT_PSB_libpathedit)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.LBT_WDG_SCARmain)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setSpacing(4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 0, 4, 4)
        self.LBT_GBX_filemon = QGroupBox(self.frame_3)
        self.LBT_GBX_filemon.setObjectName(u"LBT_GBX_filemon")
        sizePolicy.setHeightForWidth(self.LBT_GBX_filemon.sizePolicy().hasHeightForWidth())
        self.LBT_GBX_filemon.setSizePolicy(sizePolicy)
        self.LBT_GBX_filemon.setMinimumSize(QSize(0, 300))
        self.gridLayout_6 = QGridLayout(self.LBT_GBX_filemon)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 4)
        self.LBT_LSV_filesmon = QListView(self.LBT_GBX_filemon)
        self.LBT_LSV_filesmon.setObjectName(u"LBT_LSV_filesmon")
        self.LBT_LSV_filesmon.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout_6.addWidget(self.LBT_LSV_filesmon, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, -1, 4, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.LBT_PSB_fileadd = QPushButton(self.LBT_GBX_filemon)
        self.LBT_PSB_fileadd.setObjectName(u"LBT_PSB_fileadd")
        self.LBT_PSB_fileadd.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_fileadd.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_4.addWidget(self.LBT_PSB_fileadd)

        self.LBT_PSB_fileremove = QPushButton(self.LBT_GBX_filemon)
        self.LBT_PSB_fileremove.setObjectName(u"LBT_PSB_fileremove")
        self.LBT_PSB_fileremove.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_fileremove.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_4.addWidget(self.LBT_PSB_fileremove)

        self.LBT_PSB_filerescan = QPushButton(self.LBT_GBX_filemon)
        self.LBT_PSB_filerescan.setObjectName(u"LBT_PSB_filerescan")
        self.LBT_PSB_filerescan.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_filerescan.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_4.addWidget(self.LBT_PSB_filerescan)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.LBT_GBX_filemon, 0, 0, 2, 1)

        self.LBT_GBX_filefilter = QGroupBox(self.frame_3)
        self.LBT_GBX_filefilter.setObjectName(u"LBT_GBX_filefilter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LBT_GBX_filefilter.sizePolicy().hasHeightForWidth())
        self.LBT_GBX_filefilter.setSizePolicy(sizePolicy4)
        self.LBT_GBX_filefilter.setMinimumSize(QSize(0, 300))
        self.gridLayout_7 = QGridLayout(self.LBT_GBX_filefilter)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.LBT_LSV_filters = QListView(self.LBT_GBX_filefilter)
        self.LBT_LSV_filters.setObjectName(u"LBT_LSV_filters")
        self.LBT_LSV_filters.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.LBT_LSV_filters.setProperty("showDropIndicator", False)
        self.LBT_LSV_filters.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.LBT_LSV_filters.setUniformItemSizes(True)

        self.gridLayout_7.addWidget(self.LBT_LSV_filters, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.LBT_GBX_filefilter, 0, 1, 2, 1)


        self.gridLayout_3.addWidget(self.frame_3, 2, 0, 1, 1)

        self.frame = QFrame(self.LBT_WDG_SCARmain)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 24))
        self.label.setMaximumSize(QSize(50, 24))

        self.horizontalLayout_2.addWidget(self.label)

        self.LBT_LEDT_dbname = QLineEdit(self.frame)
        self.LBT_LEDT_dbname.setObjectName(u"LBT_LEDT_dbname")
        self.LBT_LEDT_dbname.setMinimumSize(QSize(0, 24))
        self.LBT_LEDT_dbname.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_2.addWidget(self.LBT_LEDT_dbname)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.LBT_SCAR_main.setWidget(self.LBT_WDG_SCARmain)

        self.gridLayout_2.addWidget(self.LBT_SCAR_main, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.LBT_PSB_import = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_import.setObjectName(u"LBT_PSB_import")
        self.LBT_PSB_import.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_import.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_import)

        self.LBT_PSB_export = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_export.setObjectName(u"LBT_PSB_export")
        self.LBT_PSB_export.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_export.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_export)

        self.LBT_PSB_active = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_active.setObjectName(u"LBT_PSB_active")
        self.LBT_PSB_active.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_active.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_active)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.LBT_PSB_libadd = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_libadd.setObjectName(u"LBT_PSB_libadd")
        self.LBT_PSB_libadd.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_libadd.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_libadd)

        self.LBT_PSB_libremove = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_libremove.setObjectName(u"LBT_PSB_libremove")
        self.LBT_PSB_libremove.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_libremove.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_libremove)

        self.LBT_PSB_librescan = QPushButton(self.LBM_WDG_LBT)
        self.LBT_PSB_librescan.setObjectName(u"LBT_PSB_librescan")
        self.LBT_PSB_librescan.setMinimumSize(QSize(24, 24))
        self.LBT_PSB_librescan.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_5.addWidget(self.LBT_PSB_librescan)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.LBM_TABWG_main.addTab(self.LBM_WDG_LBT, "")
        self.LBM_WDG_MDE = QWidget()
        self.LBM_WDG_MDE.setObjectName(u"LBM_WDG_MDE")
        self.gridLayout_8 = QGridLayout(self.LBM_WDG_MDE)
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(4)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.MDE_PSB_filename_prev = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_filename_prev.setObjectName(u"MDE_PSB_filename_prev")
        self.MDE_PSB_filename_prev.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_filename_prev.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.MDE_PSB_filename_prev)

        self.MDE_LEDT_filename = QLineEdit(self.LBM_WDG_MDE)
        self.MDE_LEDT_filename.setObjectName(u"MDE_LEDT_filename")
        self.MDE_LEDT_filename.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_filename.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_filename.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.MDE_LEDT_filename)

        self.MDE_PSB_filename_next = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_filename_next.setObjectName(u"MDE_PSB_filename_next")
        self.MDE_PSB_filename_next.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_filename_next.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.MDE_PSB_filename_next)


        self.gridLayout_8.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)

        self.splitter = QSplitter(self.LBM_WDG_MDE)
        self.splitter.setObjectName(u"splitter")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy5)
        self.splitter.setOrientation(Qt.Horizontal)
        self.MDE_SCAR_main = QScrollArea(self.splitter)
        self.MDE_SCAR_main.setObjectName(u"MDE_SCAR_main")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.MDE_SCAR_main.sizePolicy().hasHeightForWidth())
        self.MDE_SCAR_main.setSizePolicy(sizePolicy6)
        self.MDE_SCAR_main.setMinimumSize(QSize(523, 0))
        self.MDE_SCAR_main.setWidgetResizable(True)
        self.MDE_WDG_SCARmain = QWidget()
        self.MDE_WDG_SCARmain.setObjectName(u"MDE_WDG_SCARmain")
        self.MDE_WDG_SCARmain.setGeometry(QRect(0, -1159, 506, 1622))
        self.gridLayout_10 = QGridLayout(self.MDE_WDG_SCARmain)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(4)
        self.gridLayout_10.setContentsMargins(4, 4, 4, 4)
        self.verticalSpacer = QSpacerItem(20, 27, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.MDE_GBX_mediainfo = QGroupBox(self.MDE_WDG_SCARmain)
        self.MDE_GBX_mediainfo.setObjectName(u"MDE_GBX_mediainfo")
        self.gridLayout_9 = QGridLayout(self.MDE_GBX_mediainfo)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 4, 4, 4)
        self.frame_17 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_17)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(75, 24))
        self.label_28.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_20.addWidget(self.label_28)

        self.MDE_LEDT_minfo_type = QLineEdit(self.frame_17)
        self.MDE_LEDT_minfo_type.setObjectName(u"MDE_LEDT_minfo_type")
        self.MDE_LEDT_minfo_type.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_type.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_type.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.MDE_LEDT_minfo_type)


        self.gridLayout_9.addWidget(self.frame_17, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy1.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy1)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_29.setSpacing(4)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(75, 24))
        self.label_38.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_29.addWidget(self.label_38)

        self.MDE_LEDT_minfo_tagversion = QLineEdit(self.frame_26)
        self.MDE_LEDT_minfo_tagversion.setObjectName(u"MDE_LEDT_minfo_tagversion")
        self.MDE_LEDT_minfo_tagversion.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_tagversion.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_tagversion.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.MDE_LEDT_minfo_tagversion)


        self.gridLayout_9.addWidget(self.frame_26, 0, 1, 1, 1)

        self.frame_18 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_21.setSpacing(4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_18)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(75, 24))
        self.label_29.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_21.addWidget(self.label_29)

        self.MDE_LEDT_minfo_size = QLineEdit(self.frame_18)
        self.MDE_LEDT_minfo_size.setObjectName(u"MDE_LEDT_minfo_size")
        self.MDE_LEDT_minfo_size.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_size.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_size.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.MDE_LEDT_minfo_size)


        self.gridLayout_9.addWidget(self.frame_18, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_28.setSpacing(4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_25)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(75, 24))
        self.label_37.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_28.addWidget(self.label_37)

        self.MDE_LEDT_minfo_length = QLineEdit(self.frame_25)
        self.MDE_LEDT_minfo_length.setObjectName(u"MDE_LEDT_minfo_length")
        self.MDE_LEDT_minfo_length.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_length.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_length.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.MDE_LEDT_minfo_length)


        self.gridLayout_9.addWidget(self.frame_25, 1, 1, 1, 1)

        self.frame_19 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setSpacing(4)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(75, 24))
        self.label_30.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_22.addWidget(self.label_30)

        self.MDE_LEDT_minfo_dateAdded = QLineEdit(self.frame_19)
        self.MDE_LEDT_minfo_dateAdded.setObjectName(u"MDE_LEDT_minfo_dateAdded")
        self.MDE_LEDT_minfo_dateAdded.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_dateAdded.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_dateAdded.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.MDE_LEDT_minfo_dateAdded)


        self.gridLayout_9.addWidget(self.frame_19, 2, 0, 1, 1)

        self.frame_27 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_30.setSpacing(4)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_27)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(75, 24))
        self.label_39.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_30.addWidget(self.label_39)

        self.MDE_LEDT_minfo_dateModified = QLineEdit(self.frame_27)
        self.MDE_LEDT_minfo_dateModified.setObjectName(u"MDE_LEDT_minfo_dateModified")
        self.MDE_LEDT_minfo_dateModified.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_dateModified.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_dateModified.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.MDE_LEDT_minfo_dateModified)


        self.gridLayout_9.addWidget(self.frame_27, 2, 1, 1, 1)

        self.frame_20 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_20)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(75, 24))
        self.label_31.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_23.addWidget(self.label_31)

        self.MDE_LEDT_minfo_lastPlayed = QLineEdit(self.frame_20)
        self.MDE_LEDT_minfo_lastPlayed.setObjectName(u"MDE_LEDT_minfo_lastPlayed")
        self.MDE_LEDT_minfo_lastPlayed.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_lastPlayed.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_lastPlayed.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.MDE_LEDT_minfo_lastPlayed)


        self.gridLayout_9.addWidget(self.frame_20, 3, 0, 1, 1)

        self.frame_24 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_27.setSpacing(4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_24)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(75, 24))
        self.label_36.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_27.addWidget(self.label_36)

        self.MDE_LEDT_minfo_playCount = QLineEdit(self.frame_24)
        self.MDE_LEDT_minfo_playCount.setObjectName(u"MDE_LEDT_minfo_playCount")
        self.MDE_LEDT_minfo_playCount.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_playCount.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_playCount.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.MDE_LEDT_minfo_playCount)


        self.gridLayout_9.addWidget(self.frame_24, 3, 1, 1, 1)

        self.frame_21 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_21)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(75, 24))
        self.label_32.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_24.addWidget(self.label_32)

        self.MDE_LEDT_minfo_bitrate = QLineEdit(self.frame_21)
        self.MDE_LEDT_minfo_bitrate.setObjectName(u"MDE_LEDT_minfo_bitrate")
        self.MDE_LEDT_minfo_bitrate.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_bitrate.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_bitrate.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.MDE_LEDT_minfo_bitrate)


        self.gridLayout_9.addWidget(self.frame_21, 4, 0, 1, 1)

        self.frame_28 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_31.setSpacing(4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_28)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(75, 24))
        self.label_40.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_31.addWidget(self.label_40)

        self.MDE_LEDT_minfo_bitrateMode = QLineEdit(self.frame_28)
        self.MDE_LEDT_minfo_bitrateMode.setObjectName(u"MDE_LEDT_minfo_bitrateMode")
        self.MDE_LEDT_minfo_bitrateMode.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_bitrateMode.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_bitrateMode.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.MDE_LEDT_minfo_bitrateMode)


        self.gridLayout_9.addWidget(self.frame_28, 4, 1, 1, 1)

        self.frame_22 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_22)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(75, 24))
        self.label_33.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_25.addWidget(self.label_33)

        self.MDE_LEDT_minfo_channels = QLineEdit(self.frame_22)
        self.MDE_LEDT_minfo_channels.setObjectName(u"MDE_LEDT_minfo_channels")
        self.MDE_LEDT_minfo_channels.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_channels.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_channels.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.MDE_LEDT_minfo_channels)


        self.gridLayout_9.addWidget(self.frame_22, 5, 0, 1, 1)

        self.frame_31 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy1.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy1)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_34.setSpacing(4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_31)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(75, 24))
        self.label_35.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_34.addWidget(self.label_35)

        self.MDE_LEDT_minfo_sampleRate = QLineEdit(self.frame_31)
        self.MDE_LEDT_minfo_sampleRate.setObjectName(u"MDE_LEDT_minfo_sampleRate")
        self.MDE_LEDT_minfo_sampleRate.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_sampleRate.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_sampleRate.setReadOnly(True)

        self.horizontalLayout_34.addWidget(self.MDE_LEDT_minfo_sampleRate)


        self.gridLayout_9.addWidget(self.frame_31, 5, 1, 1, 1)

        self.frame_23 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_23)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(75, 24))
        self.label_34.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_26.addWidget(self.label_34)

        self.MDE_LEDT_minfo_encoderInfo = QLineEdit(self.frame_23)
        self.MDE_LEDT_minfo_encoderInfo.setObjectName(u"MDE_LEDT_minfo_encoderInfo")
        self.MDE_LEDT_minfo_encoderInfo.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_encoderInfo.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_encoderInfo.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.MDE_LEDT_minfo_encoderInfo)


        self.gridLayout_9.addWidget(self.frame_23, 6, 0, 1, 1)

        self.frame_30 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_33.setSpacing(4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_30)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(75, 24))
        self.label_42.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_33.addWidget(self.label_42)

        self.MDE_LEDT_minfo_encoderSettings = QLineEdit(self.frame_30)
        self.MDE_LEDT_minfo_encoderSettings.setObjectName(u"MDE_LEDT_minfo_encoderSettings")
        self.MDE_LEDT_minfo_encoderSettings.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_encoderSettings.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_encoderSettings.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.MDE_LEDT_minfo_encoderSettings)


        self.gridLayout_9.addWidget(self.frame_30, 6, 1, 1, 1)

        self.frame_29 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy1.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy1)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_29)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(75, 24))
        self.label_41.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_32.addWidget(self.label_41)

        self.MDE_LEDT_minfo_alumGain = QLineEdit(self.frame_29)
        self.MDE_LEDT_minfo_alumGain.setObjectName(u"MDE_LEDT_minfo_alumGain")
        self.MDE_LEDT_minfo_alumGain.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_alumGain.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_alumGain.setReadOnly(True)

        self.horizontalLayout_32.addWidget(self.MDE_LEDT_minfo_alumGain)


        self.gridLayout_9.addWidget(self.frame_29, 7, 0, 1, 1)

        self.frame_32 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_35.setSpacing(4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_32)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(75, 24))
        self.label_43.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_35.addWidget(self.label_43)

        self.MDE_LEDT_minfo_trackGain = QLineEdit(self.frame_32)
        self.MDE_LEDT_minfo_trackGain.setObjectName(u"MDE_LEDT_minfo_trackGain")
        self.MDE_LEDT_minfo_trackGain.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_trackGain.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_trackGain.setReadOnly(True)

        self.horizontalLayout_35.addWidget(self.MDE_LEDT_minfo_trackGain)


        self.gridLayout_9.addWidget(self.frame_32, 7, 1, 1, 1)

        self.frame_16 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(75, 24))
        self.label_27.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_19.addWidget(self.label_27)

        self.MDE_LEDT_minfo_Fname = QLineEdit(self.frame_16)
        self.MDE_LEDT_minfo_Fname.setObjectName(u"MDE_LEDT_minfo_Fname")
        self.MDE_LEDT_minfo_Fname.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_Fname.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_Fname.setReadOnly(False)

        self.horizontalLayout_19.addWidget(self.MDE_LEDT_minfo_Fname)


        self.gridLayout_9.addWidget(self.frame_16, 8, 0, 1, 2)

        self.frame_15 = QFrame(self.MDE_GBX_mediainfo)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(75, 24))
        self.label_26.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_17.addWidget(self.label_26)

        self.MDE_LEDT_minfo_Fpath = QLineEdit(self.frame_15)
        self.MDE_LEDT_minfo_Fpath.setObjectName(u"MDE_LEDT_minfo_Fpath")
        self.MDE_LEDT_minfo_Fpath.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_minfo_Fpath.setMaximumSize(QSize(16777215, 24))
        self.MDE_LEDT_minfo_Fpath.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.MDE_LEDT_minfo_Fpath)


        self.gridLayout_9.addWidget(self.frame_15, 9, 0, 1, 2)


        self.gridLayout_10.addWidget(self.MDE_GBX_mediainfo, 0, 0, 1, 1)

        self.MDE_GBX_coverart = QGroupBox(self.MDE_WDG_SCARmain)
        self.MDE_GBX_coverart.setObjectName(u"MDE_GBX_coverart")
        self.gridLayout_11 = QGridLayout(self.MDE_GBX_coverart)
        self.gridLayout_11.setSpacing(4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MDE_PIXLB_cover1 = QLabel(self.MDE_GBX_coverart)
        self.MDE_PIXLB_cover1.setObjectName(u"MDE_PIXLB_cover1")
        sizePolicy3.setHeightForWidth(self.MDE_PIXLB_cover1.sizePolicy().hasHeightForWidth())
        self.MDE_PIXLB_cover1.setSizePolicy(sizePolicy3)
        self.MDE_PIXLB_cover1.setMinimumSize(QSize(240, 240))
        self.MDE_PIXLB_cover1.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout.addWidget(self.MDE_PIXLB_cover1)

        self.MDE_CMBX_cover1 = QComboBox(self.MDE_GBX_coverart)
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.addItem("")
        self.MDE_CMBX_cover1.setObjectName(u"MDE_CMBX_cover1")
        self.MDE_CMBX_cover1.setMinimumSize(QSize(24, 24))
        self.MDE_CMBX_cover1.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout.addWidget(self.MDE_CMBX_cover1)


        self.gridLayout_11.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MDE_PIXLB_cover2 = QLabel(self.MDE_GBX_coverart)
        self.MDE_PIXLB_cover2.setObjectName(u"MDE_PIXLB_cover2")
        sizePolicy3.setHeightForWidth(self.MDE_PIXLB_cover2.sizePolicy().hasHeightForWidth())
        self.MDE_PIXLB_cover2.setSizePolicy(sizePolicy3)
        self.MDE_PIXLB_cover2.setMinimumSize(QSize(240, 240))
        self.MDE_PIXLB_cover2.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout_2.addWidget(self.MDE_PIXLB_cover2)

        self.MDE_CMBX_cover2 = QComboBox(self.MDE_GBX_coverart)
        self.MDE_CMBX_cover2.setObjectName(u"MDE_CMBX_cover2")
        self.MDE_CMBX_cover2.setMinimumSize(QSize(24, 24))
        self.MDE_CMBX_cover2.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_2.addWidget(self.MDE_CMBX_cover2)


        self.gridLayout_11.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.MDE_GBX_coverart, 1, 0, 1, 1)

        self.MDE_GBX_mediatags = QGroupBox(self.MDE_WDG_SCARmain)
        self.MDE_GBX_mediatags.setObjectName(u"MDE_GBX_mediatags")
        self.verticalLayout_3 = QVBoxLayout(self.MDE_GBX_mediatags)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.frame_33 = QFrame(self.MDE_GBX_mediatags)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_36.setSpacing(4)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_33)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(75, 24))
        self.label_44.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_36.addWidget(self.label_44)

        self.MDE_LEDT_mtags_title = QLineEdit(self.frame_33)
        self.MDE_LEDT_mtags_title.setObjectName(u"MDE_LEDT_mtags_title")
        self.MDE_LEDT_mtags_title.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_title.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_36.addWidget(self.MDE_LEDT_mtags_title)


        self.verticalLayout_3.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.MDE_GBX_mediatags)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy1.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy1)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_37.setSpacing(4)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_34)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(75, 24))
        self.label_45.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_37.addWidget(self.label_45)

        self.MDE_LEDT_mtags_artist = QLineEdit(self.frame_34)
        self.MDE_LEDT_mtags_artist.setObjectName(u"MDE_LEDT_mtags_artist")
        self.MDE_LEDT_mtags_artist.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_artist.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_37.addWidget(self.MDE_LEDT_mtags_artist)


        self.verticalLayout_3.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.MDE_GBX_mediatags)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy1.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy1)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_35)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(75, 24))
        self.label_46.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_38.addWidget(self.label_46)

        self.MDE_LEDT_mtags_album = QLineEdit(self.frame_35)
        self.MDE_LEDT_mtags_album.setObjectName(u"MDE_LEDT_mtags_album")
        self.MDE_LEDT_mtags_album.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_album.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_38.addWidget(self.MDE_LEDT_mtags_album)


        self.verticalLayout_3.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.MDE_GBX_mediatags)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy1.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy1)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_39.setSpacing(4)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_36)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(75, 24))
        self.label_47.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_39.addWidget(self.label_47)

        self.MDE_LEDT_mtags_albumArtist = QLineEdit(self.frame_36)
        self.MDE_LEDT_mtags_albumArtist.setObjectName(u"MDE_LEDT_mtags_albumArtist")
        self.MDE_LEDT_mtags_albumArtist.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_albumArtist.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_39.addWidget(self.MDE_LEDT_mtags_albumArtist)


        self.verticalLayout_3.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.MDE_GBX_mediatags)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy1.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy1)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_40.setSpacing(4)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_37)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(75, 24))
        self.label_48.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_40.addWidget(self.label_48)

        self.MDE_LEDT_mtags_author = QLineEdit(self.frame_37)
        self.MDE_LEDT_mtags_author.setObjectName(u"MDE_LEDT_mtags_author")
        self.MDE_LEDT_mtags_author.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_author.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_40.addWidget(self.MDE_LEDT_mtags_author)


        self.verticalLayout_3.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.MDE_GBX_mediatags)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_41.setSpacing(4)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_38)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(75, 24))
        self.label_49.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_41.addWidget(self.label_49)

        self.MDE_LEDT_mtags_composer = QLineEdit(self.frame_38)
        self.MDE_LEDT_mtags_composer.setObjectName(u"MDE_LEDT_mtags_composer")
        self.MDE_LEDT_mtags_composer.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_composer.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_41.addWidget(self.MDE_LEDT_mtags_composer)


        self.verticalLayout_3.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.MDE_GBX_mediatags)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy1.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy1)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_42.setSpacing(4)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_39)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(75, 24))
        self.label_50.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_42.addWidget(self.label_50)

        self.MDE_LEDT_mtags_conductor = QLineEdit(self.frame_39)
        self.MDE_LEDT_mtags_conductor.setObjectName(u"MDE_LEDT_mtags_conductor")
        self.MDE_LEDT_mtags_conductor.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_conductor.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_42.addWidget(self.MDE_LEDT_mtags_conductor)


        self.verticalLayout_3.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.MDE_GBX_mediatags)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_43.setSpacing(4)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_40)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(75, 24))
        self.label_51.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_43.addWidget(self.label_51)

        self.MDE_LEDT_mtags_date = QLineEdit(self.frame_40)
        self.MDE_LEDT_mtags_date.setObjectName(u"MDE_LEDT_mtags_date")
        self.MDE_LEDT_mtags_date.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_date.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_43.addWidget(self.MDE_LEDT_mtags_date)


        self.verticalLayout_3.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.MDE_GBX_mediatags)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_44.setSpacing(4)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_41)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(75, 24))
        self.label_52.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_44.addWidget(self.label_52)

        self.MDE_LEDT_mtags_orgDate = QLineEdit(self.frame_41)
        self.MDE_LEDT_mtags_orgDate.setObjectName(u"MDE_LEDT_mtags_orgDate")
        self.MDE_LEDT_mtags_orgDate.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_orgDate.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_44.addWidget(self.MDE_LEDT_mtags_orgDate)


        self.verticalLayout_3.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.MDE_GBX_mediatags)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy1.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy1)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_46.setSpacing(4)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_43)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(75, 24))
        self.label_54.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_46.addWidget(self.label_54)

        self.MDE_LEDT_mtags_discSub = QLineEdit(self.frame_43)
        self.MDE_LEDT_mtags_discSub.setObjectName(u"MDE_LEDT_mtags_discSub")
        self.MDE_LEDT_mtags_discSub.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_discSub.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_46.addWidget(self.MDE_LEDT_mtags_discSub)


        self.verticalLayout_3.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.MDE_GBX_mediatags)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy1.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy1)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_45.setSpacing(4)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_42)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(75, 24))
        self.label_53.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_45.addWidget(self.label_53)

        self.MDE_LEDT_mtags_discNum = QLineEdit(self.frame_42)
        self.MDE_LEDT_mtags_discNum.setObjectName(u"MDE_LEDT_mtags_discNum")
        self.MDE_LEDT_mtags_discNum.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_discNum.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_45.addWidget(self.MDE_LEDT_mtags_discNum)


        self.verticalLayout_3.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.MDE_GBX_mediatags)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy1.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy1)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_47.setSpacing(4)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_44)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(75, 24))
        self.label_55.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_47.addWidget(self.label_55)

        self.MDE_LEDT_mtags_trackNo = QLineEdit(self.frame_44)
        self.MDE_LEDT_mtags_trackNo.setObjectName(u"MDE_LEDT_mtags_trackNo")
        self.MDE_LEDT_mtags_trackNo.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_trackNo.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_47.addWidget(self.MDE_LEDT_mtags_trackNo)


        self.verticalLayout_3.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.MDE_GBX_mediatags)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy1.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy1)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_48.setSpacing(4)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_45)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(75, 24))
        self.label_56.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_48.addWidget(self.label_56)

        self.MDE_LEDT_mtags_lyricist = QLineEdit(self.frame_45)
        self.MDE_LEDT_mtags_lyricist.setObjectName(u"MDE_LEDT_mtags_lyricist")
        self.MDE_LEDT_mtags_lyricist.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_lyricist.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_48.addWidget(self.MDE_LEDT_mtags_lyricist)


        self.verticalLayout_3.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.MDE_GBX_mediatags)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy1.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy1)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_49.setSpacing(4)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.frame_46)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(75, 24))
        self.label_57.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_49.addWidget(self.label_57)

        self.MDE_LEDT_mtags_media = QLineEdit(self.frame_46)
        self.MDE_LEDT_mtags_media.setObjectName(u"MDE_LEDT_mtags_media")
        self.MDE_LEDT_mtags_media.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_media.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_49.addWidget(self.MDE_LEDT_mtags_media)


        self.verticalLayout_3.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.MDE_GBX_mediatags)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy1.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy1)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_50.setSpacing(4)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_47)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(75, 24))
        self.label_58.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_50.addWidget(self.label_58)

        self.MDE_LEDT_mtags_encodedBy = QLineEdit(self.frame_47)
        self.MDE_LEDT_mtags_encodedBy.setObjectName(u"MDE_LEDT_mtags_encodedBy")
        self.MDE_LEDT_mtags_encodedBy.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_encodedBy.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_50.addWidget(self.MDE_LEDT_mtags_encodedBy)


        self.verticalLayout_3.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.MDE_GBX_mediatags)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy1.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy1)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_51.setSpacing(4)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.frame_48)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(75, 24))
        self.label_59.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_51.addWidget(self.label_59)

        self.MDE_LEDT_mtags_mood = QLineEdit(self.frame_48)
        self.MDE_LEDT_mtags_mood.setObjectName(u"MDE_LEDT_mtags_mood")
        self.MDE_LEDT_mtags_mood.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_mood.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_51.addWidget(self.MDE_LEDT_mtags_mood)


        self.verticalLayout_3.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.MDE_GBX_mediatags)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy1.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy1)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_52.setSpacing(4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.frame_49)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(75, 24))
        self.label_60.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_52.addWidget(self.label_60)

        self.MDE_LEDT_mtags_version = QLineEdit(self.frame_49)
        self.MDE_LEDT_mtags_version.setObjectName(u"MDE_LEDT_mtags_version")
        self.MDE_LEDT_mtags_version.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_version.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_52.addWidget(self.MDE_LEDT_mtags_version)


        self.verticalLayout_3.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.MDE_GBX_mediatags)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy1.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy1)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_53.setSpacing(4)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.frame_50)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(75, 24))
        self.label_61.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_53.addWidget(self.label_61)

        self.MDE_LEDT_mtags_lang = QLineEdit(self.frame_50)
        self.MDE_LEDT_mtags_lang.setObjectName(u"MDE_LEDT_mtags_lang")
        self.MDE_LEDT_mtags_lang.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_lang.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_53.addWidget(self.MDE_LEDT_mtags_lang)


        self.verticalLayout_3.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.MDE_GBX_mediatags)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy1.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy1)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_54.setSpacing(4)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_51)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(75, 24))
        self.label_62.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_54.addWidget(self.label_62)

        self.MDE_LEDT_mtags_performer = QLineEdit(self.frame_51)
        self.MDE_LEDT_mtags_performer.setObjectName(u"MDE_LEDT_mtags_performer")
        self.MDE_LEDT_mtags_performer.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_performer.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_54.addWidget(self.MDE_LEDT_mtags_performer)


        self.verticalLayout_3.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.MDE_GBX_mediatags)
        self.frame_52.setObjectName(u"frame_52")
        sizePolicy1.setHeightForWidth(self.frame_52.sizePolicy().hasHeightForWidth())
        self.frame_52.setSizePolicy(sizePolicy1)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_55.setSpacing(4)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.frame_52)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(75, 24))
        self.label_63.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_55.addWidget(self.label_63)

        self.MDE_LEDT_mtags_releaseCount = QLineEdit(self.frame_52)
        self.MDE_LEDT_mtags_releaseCount.setObjectName(u"MDE_LEDT_mtags_releaseCount")
        self.MDE_LEDT_mtags_releaseCount.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_releaseCount.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_55.addWidget(self.MDE_LEDT_mtags_releaseCount)


        self.verticalLayout_3.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.MDE_GBX_mediatags)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy1.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy1)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_56.setSpacing(4)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.frame_53)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(75, 24))
        self.label_64.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_56.addWidget(self.label_64)

        self.MDE_LEDT_mtags_Org = QLineEdit(self.frame_53)
        self.MDE_LEDT_mtags_Org.setObjectName(u"MDE_LEDT_mtags_Org")
        self.MDE_LEDT_mtags_Org.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_Org.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_56.addWidget(self.MDE_LEDT_mtags_Org)


        self.verticalLayout_3.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.MDE_GBX_mediatags)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy1.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy1)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_57.setSpacing(4)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_54)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(75, 24))
        self.label_65.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_57.addWidget(self.label_65)

        self.MDE_LEDT_mtags_genre = QLineEdit(self.frame_54)
        self.MDE_LEDT_mtags_genre.setObjectName(u"MDE_LEDT_mtags_genre")
        self.MDE_LEDT_mtags_genre.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_genre.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_57.addWidget(self.MDE_LEDT_mtags_genre)


        self.verticalLayout_3.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.MDE_GBX_mediatags)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy1.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy1)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_58.setSpacing(4)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_55)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(75, 24))
        self.label_66.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_58.addWidget(self.label_66)

        self.MDE_LEDT_mtags_Web = QLineEdit(self.frame_55)
        self.MDE_LEDT_mtags_Web.setObjectName(u"MDE_LEDT_mtags_Web")
        self.MDE_LEDT_mtags_Web.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_mtags_Web.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_58.addWidget(self.MDE_LEDT_mtags_Web)


        self.verticalLayout_3.addWidget(self.frame_55)


        self.gridLayout_10.addWidget(self.MDE_GBX_mediatags, 3, 0, 1, 1)

        self.MDE_GBX_lyrics = QGroupBox(self.MDE_WDG_SCARmain)
        self.MDE_GBX_lyrics.setObjectName(u"MDE_GBX_lyrics")
        self.gridLayout_12 = QGridLayout(self.MDE_GBX_lyrics)
        self.gridLayout_12.setSpacing(4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(4, 4, 4, 4)
        self.frame_57 = QFrame(self.MDE_GBX_lyrics)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy1.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy1)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_60.setSpacing(4)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.frame_57)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(75, 24))
        self.label_67.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_60.addWidget(self.label_67)

        self.MDE_LEDT_lyricistedit = QLineEdit(self.frame_57)
        self.MDE_LEDT_lyricistedit.setObjectName(u"MDE_LEDT_lyricistedit")
        self.MDE_LEDT_lyricistedit.setMinimumSize(QSize(0, 24))
        self.MDE_LEDT_lyricistedit.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_60.addWidget(self.MDE_LEDT_lyricistedit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_4)

        self.MDE_RDB_synclyrics = QRadioButton(self.frame_57)
        self.MDE_RDB_synclyrics.setObjectName(u"MDE_RDB_synclyrics")
        self.MDE_RDB_synclyrics.setChecked(True)

        self.horizontalLayout_60.addWidget(self.MDE_RDB_synclyrics)

        self.MDE_RDB_unsynclyrics = QRadioButton(self.frame_57)
        self.MDE_RDB_unsynclyrics.setObjectName(u"MDE_RDB_unsynclyrics")

        self.horizontalLayout_60.addWidget(self.MDE_RDB_unsynclyrics)


        self.gridLayout_12.addWidget(self.frame_57, 0, 0, 1, 1)

        self.MDE_TXBRW_lyrics = QTextBrowser(self.MDE_GBX_lyrics)
        self.MDE_TXBRW_lyrics.setObjectName(u"MDE_TXBRW_lyrics")
        self.MDE_TXBRW_lyrics.setMinimumSize(QSize(0, 250))
        self.MDE_TXBRW_lyrics.setReadOnly(False)

        self.gridLayout_12.addWidget(self.MDE_TXBRW_lyrics, 1, 0, 1, 1)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.MDE_CKB_nolyrics = QCheckBox(self.MDE_GBX_lyrics)
        self.MDE_CKB_nolyrics.setObjectName(u"MDE_CKB_nolyrics")
        self.MDE_CKB_nolyrics.setTristate(True)

        self.horizontalLayout_61.addWidget(self.MDE_CKB_nolyrics)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_5)

        self.MDE_PSB_searchweb = QPushButton(self.MDE_GBX_lyrics)
        self.MDE_PSB_searchweb.setObjectName(u"MDE_PSB_searchweb")
        self.MDE_PSB_searchweb.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_searchweb.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_61.addWidget(self.MDE_PSB_searchweb)


        self.gridLayout_12.addLayout(self.horizontalLayout_61, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.MDE_GBX_lyrics, 4, 0, 1, 1)

        self.MDE_SCAR_main.setWidget(self.MDE_WDG_SCARmain)
        self.splitter.addWidget(self.MDE_SCAR_main)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.widget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(75, 24))
        self.label_68.setMaximumSize(QSize(16777215, 24))
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_68)

        self.MDE_LSV_filelist = QListView(self.widget)
        self.MDE_LSV_filelist.setObjectName(u"MDE_LSV_filelist")

        self.verticalLayout_4.addWidget(self.MDE_LSV_filelist)

        self.splitter.addWidget(self.widget)

        self.gridLayout_8.addWidget(self.splitter, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.MDE_PSB_undo = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_undo.setObjectName(u"MDE_PSB_undo")
        self.MDE_PSB_undo.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_undo.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_6.addWidget(self.MDE_PSB_undo)

        self.MDE_PSB_inspect = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_inspect.setObjectName(u"MDE_PSB_inspect")
        self.MDE_PSB_inspect.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_inspect.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_6.addWidget(self.MDE_PSB_inspect)

        self.MDE_TLB_autotag = QToolButton(self.LBM_WDG_MDE)
        self.MDE_TLB_autotag.setObjectName(u"MDE_TLB_autotag")
        self.MDE_TLB_autotag.setMinimumSize(QSize(24, 24))
        self.MDE_TLB_autotag.setMaximumSize(QSize(16777215, 24))
        self.MDE_TLB_autotag.setPopupMode(QToolButton.MenuButtonPopup)
        self.MDE_TLB_autotag.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.MDE_TLB_autotag)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.MDE_PSB_rename = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_rename.setObjectName(u"MDE_PSB_rename")
        self.MDE_PSB_rename.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_rename.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_6.addWidget(self.MDE_PSB_rename)

        self.MDE_PSB_save = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_save.setObjectName(u"MDE_PSB_save")
        self.MDE_PSB_save.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_save.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_6.addWidget(self.MDE_PSB_save)

        self.MDE_PSB_cancel = QPushButton(self.LBM_WDG_MDE)
        self.MDE_PSB_cancel.setObjectName(u"MDE_PSB_cancel")
        self.MDE_PSB_cancel.setMinimumSize(QSize(24, 24))
        self.MDE_PSB_cancel.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_6.addWidget(self.MDE_PSB_cancel)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.LBM_TABWG_main.addTab(self.LBM_WDG_MDE, "")
        self.LBM_WDG_FLM = QWidget()
        self.LBM_WDG_FLM.setObjectName(u"LBM_WDG_FLM")
        self.LBM_TABWG_main.addTab(self.LBM_WDG_FLM, "")

        self.gridLayout.addWidget(self.LBM_TABWG_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.LBM_WDG_centeral)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.LBM_TABWG_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library Manager", None))
        self.LBT_PSB_libprev.setText("")
        self.LBT_PSB_libnext.setText("")
        self.LBT_GBX_libstat.setTitle(QCoreApplication.translate("MainWindow", u"Library Statistics", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Total Artists", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Top Artist", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total Alums", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Top Track", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Total Tracks", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Top Album", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Play Time", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Top Genre", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Library Size", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Total Playcount", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DB Path", None))
        self.LBT_PSB_libpathedit.setText("")
        self.LBT_GBX_filemon.setTitle(QCoreApplication.translate("MainWindow", u"Files Monitored", None))
        self.LBT_PSB_fileadd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.LBT_PSB_fileremove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.LBT_PSB_filerescan.setText(QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.LBT_GBX_filefilter.setTitle(QCoreApplication.translate("MainWindow", u"File Extension FIlters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DB Name", None))
        self.LBT_PSB_import.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.LBT_PSB_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.LBT_PSB_active.setText(QCoreApplication.translate("MainWindow", u"Set as Active", None))
        self.LBT_PSB_libadd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.LBT_PSB_libremove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.LBT_PSB_librescan.setText(QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.LBM_TABWG_main.setTabText(self.LBM_TABWG_main.indexOf(self.LBM_WDG_LBT), QCoreApplication.translate("MainWindow", u"Library ", None))
        self.MDE_PSB_filename_prev.setText("")
        self.MDE_PSB_filename_next.setText("")
        self.MDE_GBX_mediainfo.setTitle(QCoreApplication.translate("MainWindow", u"Media Information", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Tag Version", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Date Added", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Date Modified", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Last Played", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Play Count", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"BitRate", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"BitRate Mode", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Channels", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Sample Rate", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Encoder Info", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Encoder Settings", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Album Gain", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Track Gain", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"File Path", None))
        self.MDE_GBX_coverart.setTitle(QCoreApplication.translate("MainWindow", u"Track Artwork ", None))
        self.MDE_PIXLB_cover1.setText("")
        self.MDE_CMBX_cover1.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(7, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.MDE_CMBX_cover1.setItemText(8, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.MDE_PIXLB_cover2.setText("")
        self.MDE_GBX_mediatags.setTitle(QCoreApplication.translate("MainWindow", u"Metadata Tags", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Album Artist", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Composer", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Conductor", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Original Date ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Disc Subtitle", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Disc Number", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Track No", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Lyricist", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Media", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Encoded By", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Mood ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Performer", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Release Country", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Orginization ", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.MDE_GBX_lyrics.setTitle(QCoreApplication.translate("MainWindow", u"Lyrics", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Lyricist", None))
        self.MDE_RDB_synclyrics.setText(QCoreApplication.translate("MainWindow", u"Synchronized", None))
        self.MDE_RDB_unsynclyrics.setText(QCoreApplication.translate("MainWindow", u"Unsynchronized", None))
        self.MDE_CKB_nolyrics.setText(QCoreApplication.translate("MainWindow", u"No Lyrics", None))
        self.MDE_PSB_searchweb.setText(QCoreApplication.translate("MainWindow", u"Search Internet", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Tracks List", None))
        self.MDE_PSB_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.MDE_PSB_inspect.setText(QCoreApplication.translate("MainWindow", u"Inspect", None))
        self.MDE_TLB_autotag.setText(QCoreApplication.translate("MainWindow", u"AutoTag", None))
        self.MDE_PSB_rename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.MDE_PSB_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.MDE_PSB_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.LBM_TABWG_main.setTabText(self.LBM_TABWG_main.indexOf(self.LBM_WDG_MDE), QCoreApplication.translate("MainWindow", u"Metadata Edit", None))
        self.LBM_TABWG_main.setTabText(self.LBM_TABWG_main.indexOf(self.LBM_WDG_FLM), QCoreApplication.translate("MainWindow", u"File Manager", None))
    # retranslateUi

