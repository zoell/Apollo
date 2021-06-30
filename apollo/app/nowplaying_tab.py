import sys

from PySide6 import QtWidgets, QtGui, QtCore, QtSql
from PySide6.QtCore import QPoint, QRect, QSize, Qt

from apollo.utils import PlayingQueue, exe_time
from apollo.app.dataproviders import SQLTableModel
from apollo.db import DBFIELDS


class NowPlayingQueue(SQLTableModel):
    """
    Utilities for data and communication between tabs
    """
    def __init__(self, Driver: QtSql.QSqlDriver, ParentView: QtWidgets.QAbstractItemView):
        """
        Class Constructor
        """
        super().__init__(Driver, ParentView)
        self.PlayingQueue = PlayingQueue()

    def Get_columnData(self, Column: int):
        """
        Gets Data from the model

        Parameters
        ----------
        Column: int
            index of the column to get data from

        Returns
        -------
        List:
            Column Data
        """
        return self.Data_atIndex(Rows = list(range(self.rowCount())), Columns = [Column])

    def PlayNow(self, Indexes: [QtCore.QModelIndex]):
        """"""
        Indexes = self.Data_atIndex(Indexes = Indexes, Columns = [0])
        self.DBManager.CreateView("nowplaying", Indexes)
        self.RefreshData()
        self.PlayingQueue.RemoveElements()
        self.PlayingQueue.AddElements(self.Get_columnData(0))

    def PlayShuffled(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected indexes from View and adds Shuffled Data to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        Indexes = self.Data_atIndex(Indexes = Indexes, Columns = [0])
        self.DBManager.CreateView("nowplaying", Indexes, Shuffled = True)
        self.RefreshData()
        self.PlayingQueue.RemoveElements()
        self.PlayingQueue.AddElements(self.Get_columnData(0))

    def PlayArtist(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected Artists from View and adds to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        Indexes = self.Data_atIndex(Indexes = Indexes,Columns = [self.DB_FIELDS.index('artist')])
        self.DBManager.CreateView("nowplaying", Indexes, FilterField  = 'artist', Filter = True)
        self.RefreshData()
        self.PlayingQueue.RemoveElements()
        self.PlayingQueue.AddElements(self.Get_columnData(0))

    def PlayAlbum(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected Album from View and adds to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        Indexes = self.Data_atIndex(Indexes = Indexes, Columns = [self.DB_FIELDS.index('album')])
        self.DBManager.CreateView("nowplaying", Indexes, FilterField = 'album', Filter = True)
        self.RefreshData()
        self.PlayingQueue.RemoveElements()
        self.PlayingQueue.AddElements(self.Get_columnData(0))

    def PlayGenre(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected genre from View and adds to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        Indexes = self.Data_atIndex(Indexes = Indexes, Columns = [self.DB_FIELDS.index('genre')])
        self.DBManager.CreateView("nowplaying", Indexes, FilterField = 'genre', Filter = True)
        self.RefreshData()
        self.PlayingQueue.RemoveElements()
        self.PlayingQueue.AddElements(self.Get_columnData(0))

    def QueueNext(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected indexes from View and queues to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        NewIndexes = self.Data_atIndex(Indexes = Indexes, Columns = [0])
        self.PlayingQueue.AddNext(NewIndexes)
        Indexes = self.PlayingQueue.GetQueue()
        self.DBManager.CreateView("nowplaying", Indexes)
        self.OrderTable(Indexes)

    def QueueLast(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected indexes from View and queues to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        NewIndexes = self.Data_atIndex(Indexes = Indexes, Columns = [0])
        self.PlayingQueue.AddElements(NewIndexes)
        Indexes = self.PlayingQueue.GetQueue()
        self.DBManager.CreateView("nowplaying", Indexes)
        self.OrderTable(Indexes)

    def QueueAlbumNext(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected indexes from View and queues to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        NewIndexes = self.Data_atIndex(Indexes = Indexes, Columns = [self.DB_FIELDS.index('album')])
        NewIndexes = ", ".join([f"'{v}'" for v in NewIndexes])
        NewIndexes = self.DBManager.exec_query(f"""
        SELECT file_id
        FROM library
        WHERE album IN ({NewIndexes})
        OR lower(album) IN ({NewIndexes})
        """)
        self.PlayingQueue.AddNext(NewIndexes)
        Indexes = self.PlayingQueue.GetQueue()
        self.DBManager.CreateView("nowplaying", Indexes)
        self.OrderTable(Indexes)

    def QueueAlbumLast(self, Indexes: [QtCore.QModelIndex]):
        """
        Info: Gets selected indexes from View and queues to model
        Args:
        View: QtTableView
            -> view to get data from

        Returns: None
        Errors: None
        """
        NewIndexes = self.Data_atIndex(Indexes = Indexes, Columns = [self.DB_FIELDS.index('album')])
        NewIndexes = ", ".join([f"'{v}'" for v in NewIndexes])
        NewIndexes = self.DBManager.exec_query(f"""
        SELECT file_id
        FROM library
        WHERE album IN ({NewIndexes})
        OR lower(album) IN ({NewIndexes})
        """)
        self.PlayingQueue.AddElements(NewIndexes)
        Indexes = self.PlayingQueue.GetQueue()
        self.DBManager.CreateView("nowplaying", Indexes)
        self.OrderTable(Indexes)

    def SearchModel(self, query: str, View: QtWidgets.QListView):
        """
        Queries the tables and displays the matched rows

        Parameters
        ----------
        query: str
            Query string to search for
        View: QtWidgets.QTableView
            View to apply mask to
        """
        if query == "":
            for Row in range(self.rowCount()):
                View.setRowHidden(Row, False)
            return None

        for Row in range(self.rowCount()):
            Query = []
            for Col in ["album", "albumartist", "artist", "title"]:
                Col = self.DB_FIELDS.index(Col)
                data = self.index(Row, Col).data()
                Query.append(data.find(query) != -1)
                Query.append(data.find(query.upper()) != -1)
                Query.append(data.find(query.lower()) != -1)
                Query.append(data.find(query.title()) != -1)

            if any(Query):
                View.setRowHidden(Row, False)
            else:
                View.setRowHidden(Row, True)

class NowPlaying_ItemDelegate(QtWidgets.QStyledItemDelegate):
    """
    Delegate calss for the NPQ which interfaces with the model
    """
    def __init__(self, Model):
        """
        Class Constructor

        Parameters
        ----------
        Model : QtGui.QStandardItemModel
            Modle to load data from
        """
        super().__init__()
        self._model = Model
        self._style = QtWidgets.QApplication.style()
        self._theme = {}
        self._option = None
        self._painter = None

    def setDataModel(self, Value):
        """
        Setter for the DataModel

        Parameters
        ----------
        Value : QtGui.QStandardItemModel
            DataModel
        """
        self._model = Value

    def setFields(self, T, M, B1, B2, B3):
        self.Fields = [DBFIELDS.index(F) for F in [T, M, B1, B2, B3]]

    def getData(self, index):
        Row = index.row()
        return [self._model.index(Row, Col).data() for Col in self.Fields]

    def paint(self, painter, option, index):
        painter.save()
        self.DrawWidget(painter, QtWidgets.QStyleOptionViewItem(option), index)
        painter.restore()

    def sizeHint(self, option, index):
        return QSize(option.rect.width(), 64)

    def DrawWidget(self, Painter: QtGui.QPainter, Option, Index):
        state = Option.state

        if state & self._style.State_Enabled and state & self._style.State_Selected:
            # Selected
            color = QtGui.QColor(self._theme.get("ui-02"))
            border = QtGui.QColor(self._theme.get("ui-01"))

        elif state & self._style.State_Enabled and state & self._style.State_Active:
            # Normal
            color = QtGui.QColor(self._theme.get("ui-01"))
            border = QtGui.QColor(self._theme.get("ui-02"))

        elif state & self._style.State_Enabled:
            # Inactive
            color = QtGui.QColor(self._theme.get("ui-01"))
            border = QtGui.QColor(self._theme.get("ui-02"))

        else:
            # Disabled
            color = QtGui.QColor(self._theme.get("disabled-02"))
            border = QtGui.QColor(self._theme.get("disabled-02"))

        Painter.setPen(color)
        self._style.drawPrimitive(self._style.PE_PanelItemViewItem, Option, Painter, Option.widget)
        Painter.fillRect(Option.rect, (color))

        Painter.setPen(QtGui.QColor(self._theme.get("text-02")))
        items = self.getData(Index)
        self.DrawCover(Painter, Option)
        self.DrawTop(Painter, Option, items[0])
        self.DrawMid(Painter, Option, items[1])
        self.DrawBottom(Painter, Option, [items[2], items[3], items[4]])

        Painter.setPen(border)
        Painter.drawLine(QPoint(0, Option.rect.y() + 63), QPoint(Option.rect.width(), Option.rect.y() + 63))

    def DrawCover(self, Painter, Options):
        self._style.subElementRect(self._style.SE_ItemViewItemDecoration, Options, Options.widget)
        Rect = Options.rect
        TempRec = QRect(Rect.x() + 4, Rect.y() + 4, 56, 56)
        if False:
            pass
        else:
            Painter.drawImage(TempRec, QtGui.QImage(':/icon_pack/png/64/music_icon-02.png'))

    def DrawTop(self, Painter, Options, item):
        Rect = Options.rect
        TempRec = QRect(Rect.x() + 64, Rect.y() + 4, Rect.width() - 68, 16)
        Painter.drawText(TempRec, item)

    def DrawMid(self, Painter, Options, item):
        Rect = Options.rect
        TempRec = QRect(Rect.x() + 64, Rect.y() + 24, Rect.width() - 68, 16)
        Painter.drawText(TempRec, item)

    def DrawBottom(self, Painter, Options, items):
        Rect = Options.rect
        Width = round((Rect.width() - 72) / 3)
        # 1
        TempRec = QRect(Rect.x() + 64, Rect.y() + 44, Width, 16)
        Painter.drawText(TempRec, items[0])
        # 2
        TempRec = QRect(Rect.x() + (64 + Width + 4), Rect.y() + 44, Width, 16)
        Painter.drawText(TempRec, items[1])
        # 3
        TempRec = QRect(Rect.x() + (64 + Width + 4 + Width + 4), Rect.y() + 44, Width - 4, 16)
        Painter.drawText(TempRec, items[2])


class NowPlayingTab:
    """
    Now PLaying Tab
    """
    def __init__(self, UI):
        """
        Class constructor
        """
        # Development code not production code will cause bugs if not remove
        if UI != None:
            self.UI = UI
        else:
            from apollo.app.mainapp_ux import ApolloMain
            self.UI = ApolloMain()
        ###
        self.DataProvider = self.UI.DataProvider
        self.Init_DataModels()
        self.Function_Bindings()

    def Init_DataModels(self):
        """
        Inits all the Data Model
        """
        self.MainView = self.UI.NPQ_LSV_mainqueue
        self.MainModel = NowPlayingQueue(self.UI.DBManager, self.MainView)
        self.MainModel.LoadTable("nowplaying", self.MainModel.DB_FIELDS)
        self.DataProvider.AddModel(self.MainModel, "nowplaying_model")
        self.MainView.setModel(self.MainModel)

        self.Delegate = NowPlaying_ItemDelegate(self.MainModel)
        self.Delegate._theme = self.UI.Theme
        self.Delegate.setFields("artist", "title", "length", "filesize", "bitrate")

        self.UI.NPQ_LSV_mainqueue.setItemDelegate(self.Delegate)

    def Function_Bindings(self):
        self.UI.NPQ_LEDT_search.textChanged.connect(lambda q: self.MainModel.SearchModel(q, self.MainView))


if __name__ == "__main__":
    from apollo.app.mainapp import ApolloExecute

    app = ApolloExecute()
    app.Execute()
