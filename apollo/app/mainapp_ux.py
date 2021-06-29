import sys, datetime
from typing import Callable

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt

from apollo.gui.ui_mainwindow_apollo import Ui_MainWindow as MainWindow
from apollo.utils import AppConfig
from apollo.plugins.app_theme import Theme
from apollo.db import LibraryManager
from apollo.db.library_manager_app import LibraryManager_App
from apollo.app.dataproviders import ApolloDataProvider
from apollo.app.library_tab import LibraryTab
from apollo.app.nowplaying_tab import NowPlayingTab


class ApolloUX(QtWidgets.QMainWindow, MainWindow):
    """
    Initializes Apollo and all related functions
    """
    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.setupUi(self)
        self.setupUx()

        # Init
        self.AppConfig = AppConfig()
        self.Theme = Theme()
        self.DBManager = LibraryManager(self.AppConfig["current_db_path"])
        self.DataProvider = ApolloDataProvider()

    def setupUx(self):
        self.MW_HSP_subwindows.setCollapsible(0, False)


class ApolloMain(ApolloUX):
    """
    Initializes Apollo and all related functions
    """
    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.InitTabs()
        self.FunctionBindings()

    def FunctionBindings(self):
        """
        Binds all the functions and actions
        """
        self.actionDataBase_Manager.triggered.connect(lambda: self.Launch_LibraryManagerApp(0))
        self.actionMetadata_Edit.triggered.connect(lambda: self.Launch_LibraryManagerApp(1))
        self.actionFile_Orginizer.triggered.connect(lambda: self.Launch_LibraryManagerApp(2))

    def InitTabs(self):
        """
        Initilizes all the tabs for apollo
        """
        self.NowPlayingTab = NowPlayingTab(self)
        self.LibraryTab = LibraryTab(self)

    def Launch_LibraryManagerApp(self, TabOpen: int = 0):
        """
        Launches the Library Manager app

        Parameters
        ----------
        TabOpen: int
            Tab to point to when the app is launced
        """
        self.LibraryManagerApp = LibraryManager_App()
        self.LibraryManagerApp.LBM_TABWG_main.setCurrentIndex(TabOpen)
        self.LibraryManagerApp.raise_()
        self.LibraryManagerApp.show()

    def HeaderActionsBinding(self, Index: int, Model: QtGui.QStandardItemModel, Header: QtWidgets.QHeaderView):
        """
        Creates all the actions and checkboxes for the related header section at given index

        Parameters
        ----------
        Index: Int
            index of rhe given header section
        Model: QStandardItemModel
            Model of the given table
        Header: QHeaderView
            header view of the given table

        Return
        ------
            QAction
        """
        def HeaderHide(Index: int, Action: QtGui.QAction, Header: QtWidgets.QHeaderView): # works
            """
            Binds all the actions with the hiding and showing functions

            Parameters
            ----------
            Index: Int
                index of rhe given header section
            Action: QAction
                Action to set check and uncheck state
            Header: QHeaderView
                header view of the given table
            """
            if not (Header.isSectionHidden(Index)):
                Action.setChecked(False)
                Header.hideSection(Index)
            else:
                Action.setChecked(True)
                Header.showSection(Index)

        Action = QtGui.QAction(Model.headerData(Index, QtCore.Qt.Horizontal))
        Action.setCheckable(True)
        if Header.isSectionHidden(Index):
            Action.setChecked(False)
        else:
            Action.setChecked(True)
        Action.triggered.connect(lambda: HeaderHide(Index, Action, Header))
        return Action

    def CreateRating_Action(self, Menu: QtWidgets.QMenu, rating: float, method: Callable):
        """
        Create a action with the rating stars

        Parameters
        ----------
        Menu: QtWidgets.QMenu
            Main menu to add actions to
        rating: float
            rating in float
        method: Callable
            method to add to the action
        """
        # Painter
        pixmap = QtGui.QPixmap(24*5, 24)
        painter = QtGui.QPainter(pixmap)
        painter.save()
        point = QtCore.QPoint(4, 4)
        painter.fillRect(pixmap.rect(), QtGui.QColor(self.Theme.get("ui-01")))
        for star in range(int(rating)):
            Image = QtGui.QImage(":/icon_pack/png/16/star_icon-01.png")
            Image.smoothScaled(24, 24)
            painter.drawImage(point, Image)
            point.setX(point.x() + 24)

        if (rating - int(rating)) == 0.5:
            Image = QtGui.QImage(":/icon_pack/png/16/star-half_icon-01.png")
            Image.smoothScaled(24, 24)
            painter.drawImage(point, Image)
        painter.setPen(QtGui.QColor(self.Theme.get("ui-background")))
        painter.drawLine(0, 23, 24*5, 23)

        painter.restore()
        painter.end()
        # Painter

        Action = QtWidgets.QWidgetAction(Menu)
        Label = QtWidgets.QLabel(Menu)
        Label.setPixmap(pixmap)
        Label.setFixedHeight(24)
        Action.setDefaultWidget(Label)

        Action.triggered.connect(method)
        Menu.addAction(Action)

    def closeSubTabs(self):
        """
        Closes all te subtabs declared
        """
        if hasattr(self, "LibraryManagerApp"):
            self.LibraryManagerApp.close()

    def closeEvent(self, event:QtGui.QCloseEvent):
        """
        Close Event for the Main App

        Parameters
        ----------
        event: QtGui.QCloseEvent
            Close Event when the tab is closed
        """
        self.closeSubTabs()


if __name__ == "__main__":
    from apollo.app.mainapp import ApolloExecute

    app = ApolloExecute()
    app.Execute()
