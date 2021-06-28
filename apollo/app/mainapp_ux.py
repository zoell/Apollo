import sys, datetime

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
    Initilizes Apollo and all related functions
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

    def closeSubTabs(self):
        """
        Closes all te subtabs declared
        """
        if hasattr(self, "LibraryManagerApp"):
            self.LibraryManagerApp.close()

    def InitTabs(self):
        """
        Initilizes all the tabs for apollo
        """
        self.NowPlayingTab = NowPlayingTab(self)
        self.LibraryTab = LibraryTab(self)

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
