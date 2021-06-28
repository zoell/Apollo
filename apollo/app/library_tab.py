import sys
from typing import Any, Callable

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt

from apollo.app.dataproviders import SQLTableModel


class LibraryTab:
    """
    Library tab Functions
    """
    def __init__(self, UI: Any):
        """
        Class Constructor
        """
        # Development code not production code will cause bugs if not removed -
        if UI != None:
            self.UI = UI
        else:
            from apollo.app.mainapp_ux import ApolloMain
            self.UI = ApolloMain()
        # ---------------------------------------------------------------------

        self.DataProvider = self.UI.DataProvider
        self.Init_DataModels()
        self.FunctionBindidngs()

    def FunctionBindidngs(self):
        """
        Function Bindings
        """
        self.UI.LDT_TBV_maintable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.UI.LDT_TBV_maintable.customContextMenuRequested.connect(self.MainTable_ContextMenu)

        self.UI.LBT_LSV_grouping.setContextMenuPolicy(Qt.CustomContextMenu)
        self.UI.LBT_LSV_grouping.customContextMenuRequested.connect(self.GroupTable_ContextMenu)

    def Init_DataModels(self):
        """
        Inits and Gets all te Data Models form the Data Provider
        """
        self.MainView = self.UI.LDT_TBV_maintable
        self.MainModel = SQLTableModel(self.UI.DBManager)
        self.MainModel.LoadTable("library", self.MainModel.DB_FIELDS)
        self.DataProvider.AddModel(self.MainModel, "library_model")

        self.NowPlayingQueue = self.DataProvider.GetModel("nowplaying_model")
        self.MainView.setModel(self.MainModel)
        self.UI.LBT_LSV_grouping.setModel(self.MainModel)

    def MainTable_ContextMenu(self):
        """
        Call the Custom Context Menu for the Main Table
        """
        def BindMenuActions(Element: QtGui.QAction, Name: str, Method: Callable = lambda: print("NotImplemented")):
            Element.addAction(f"{Name}").triggered.connect(Method)

        # Main Menu
        MainMenu = QtWidgets.QMenu()

        BindMenuActions(MainMenu, "Play Now",
                        lambda: self.NowPlayingQueue.PlayNow(self.MainView.selectedIndexes())
                        )

        BindMenuActions(MainMenu, "Queue Next",
                        lambda: self.NowPlayingQueue.QueueNext(self.MainView.selectedIndexes())
                        )

        BindMenuActions(MainMenu, "Queue Last",
                        lambda: self.NowPlayingQueue.QueueLast(self.MainView.selectedIndexes())
                        )

        # Play More Menu
        lv_1_1 = MainMenu.addMenu("Play More")
        BindMenuActions(lv_1_1, "Try On Auto-DJ")
        lv_1_1.addSeparator()

        lv_1_1.addMenu("Output To")
        lv_1_1.addSeparator()

        BindMenuActions(lv_1_1, "Play Shuffled",
                        lambda: self.NowPlayingQueue.PlayShuffled(self.MainView.selectedIndexes())
                        )

        lv_1_1.addSeparator()

        BindMenuActions(lv_1_1, "Play Artist",
                        lambda: self.NowPlayingQueue.PlayArtist(self.MainView.selectedIndexes())
                        )
        lv_1_1.addSeparator()

        BindMenuActions(lv_1_1, "Play Album Now",
                        lambda: self.NowPlayingQueue.PlayAlbum(self.MainView.selectedIndexes())
                        )

        BindMenuActions(lv_1_1, "Queue Album Next",
                        lambda: self.NowPlayingQueue.QueueAlbumNext(self.MainView.selectedIndexes())
                        )

        BindMenuActions(lv_1_1, "Queue Album Last",
                        lambda: self.NowPlayingQueue.QueueAlbumLast(self.MainView.selectedIndexes())
                        )

        lv_1_1.addSeparator()

        BindMenuActions(lv_1_1, "Play Genre",
                        lambda: self.NowPlayingQueue.PlayGenre(self.MainView.selectedIndexes())
                        )

        MainMenu.addSeparator()

        # Edit Action
        BindMenuActions(MainMenu, "Edit @")

        # Ratings Menu
        lv_1_2 = MainMenu.addMenu("Rating")
        BindMenuActions(lv_1_2, "0   star")
        BindMenuActions(lv_1_2, "1   star")
        BindMenuActions(lv_1_2, "1/5 stars")
        BindMenuActions(lv_1_2, "2   stars")
        BindMenuActions(lv_1_2, "2/5 stars")
        BindMenuActions(lv_1_2, "3   stars")
        BindMenuActions(lv_1_2, "3/5 stars")
        BindMenuActions(lv_1_2, "4   stars")
        BindMenuActions(lv_1_2, "4/5 stars")
        BindMenuActions(lv_1_2, "5   stars")

        # Add To Playlist Menu
        lv_1_3 = MainMenu.addMenu("Add To Playlist")

        # Send To Menu
        lv_1_4 = MainMenu.addMenu("Send To")

        # Delete Action
        BindMenuActions(MainMenu, "Delete")
        BindMenuActions(MainMenu, "Remove")
        MainMenu.addSeparator()

        # Search Menu
        lv_1_5 = MainMenu.addMenu("Search")
        BindMenuActions(lv_1_5, "Search Similar Artist")
        BindMenuActions(lv_1_5, "Search Similar Album")
        BindMenuActions(lv_1_5, "Search Similar Genre")
        lv_1_5.addSeparator()
        BindMenuActions(lv_1_5, "Open In Browser")
        BindMenuActions(lv_1_5, "Locate In Explorer")

        # Execution
        cursor = QtGui.QCursor()
        MainMenu.exec(cursor.pos())

    def GroupTable_ContextMenu(self):
        """
        Call the Custom Context Menu for the Grouping Table
        """
        MainMenu = QtWidgets.QMenu()

        Cursor = QtGui.QCursor()
        MainMenu.exec(Cursor.pos())


if __name__ == "__main__":
    from apollo.app.mainapp import ApolloExecute

    app = ApolloExecute()
    app.Execute()
