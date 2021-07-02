import os.path
import sys, re

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt

from apollo.db.library_manager import DataBaseManager
from apollo import exe_time


class SQLTableModel(QtGui.QStandardItemModel):
    """
    Extends the Standard Item Model
    """
    def __init__(self, Driver: DataBaseManager, ParentView: QtWidgets.QAbstractItemView):
        """
        Class Constructor
        """
        super().__init__()
        self.DBManager = Driver
        self.ParentView = ParentView
        self.DB_NAME = Driver.DB_NAME
        self.DB_FIELDS = self.DBManager.db_fields
        self.DB_TABLE = None

    def OrderTable(self, Keys):
        """
        Info: Orders table rows accroding to the keys
        Args:
        Keys: list[String, String]
            -> Kesy to use to sort rows
        Returns: None
        Errors: None
        """
        def FilterData(Row):
            return [QtGui.QStandardItem(str(V)) for V in ResultSet_dict.get(Row)]

        self.removeRows(0, self.rowCount())
        ResultSet = self.DBManager.exec_query(f"SELECT * FROM {self.DB_TABLE}")

        if len(ResultSet) > 0:
            ResultSet_dict = {Value[0]: Value for Value in ResultSet}
            for Row in Keys:
                self.appendRow(FilterData(Row))

    def Data_atIndex(self, Indexes: list = [], Rows: list = [], Columns: list = []):
        """
        Info: returns all the data at selected Positions in a TBV
        Args:
        TBV: TableView
            Table to get data from
        cols: List[int, int]
        Return: List[[Column, Column, ...]]
        Errors:
        """
        Table = {}

        if Columns == []:
            Columns = list(range(len(self.DB_FIELDS)))

        if Indexes != []:
            for index in Indexes:
                Row = index.row()
                Col = index.column()
                if Col in Columns:
                    if Table.get(Row):
                        Table[Row].append(index.data())
                    elif len(Columns) >= 2:
                        Table[Row] = [index.data()]
                    else:
                        Table[Row] = index.data()

        if Rows != []:
            for Row in Rows:
                for Col in Columns:
                    if Table.get(Row):
                        Table[Row].append(self.index(Row, Col).data())
                    elif len(Columns) >= 2:
                        Table[Row] = [self.index(Row, Col).data()]
                    else:
                        Table[Row] = self.index(Row, Col).data()

        return list(Table.values())

    def RefreshData(self):
        """
        Info: Refreshing the Tablemodel
        Args: None
        Returns: None
        Errors: None
        """
        self.removeRows(0, self.rowCount())
        self.LoadData(self.DB_TABLE)

    def LoadTable(self, TableName, Header = None):
        """
        Info: Loads the table model with DB values
        Args:
        TableName: string
            -> DB tablename to get data from
        Header: list(string, string)
            -> header names of the table
        Orientation: Qt.Horizontal | Qt.vertical
            -> Orientation of header data
        Returns: None
        Errors: None
        """
        self.DB_TABLE = TableName
        self.LoadData(TableName)
        if Header != None:
            self.LoadHeaderData(Header, Qt.Horizontal)
        else:
            self.LoadHeaderData(self.DB_FIELDS, Qt.Horizontal)

    def LoadData(self, TableName):
        """
        Info: Loads the table model with DB values
        Args:
        TableName: string
            -> DB tablename to get data from
        Returns: None
        Errors: None
        """
        ResultSet = self.DBManager.exec_query(f"SELECT * FROM {TableName}")
        for Row in ResultSet:
            self.appendRow(list(map(lambda x: QtGui.QStandardItem(str(x)), Row)))

    def LoadHeaderData(self, Header, Orientation = Qt.Horizontal):
        """
        Info: Loads the table model with DB values
        Args:
        Header: list(string, string)
            -> header names of the table
        Orientation: Qt.Horizontal | Qt.vertical
            -> Orientation of header data
        Returns: None
        Errors: None
        """
        for col, data in enumerate(Header):
            self.setHeaderData(col, Orientation, str(data).replace("_", " ").title())

    def RemoveItem(self, SelectedIndexes: [QtCore.QModelIndex], Delete: bool):
        """
        Info: Removes Item From Model
        Args:
        View: QtTableView
            -> View to delete data from
        Returns: None
        Errors:
        1. Rows are not deleted when deleting more than 5000 rows
        """

        if self.DB_TABLE == "library":
            selectedID = self.Data_atIndex(Indexes = SelectedIndexes, Columns = [0])
            selectedID = ", ".join([f"'{v}'"for v in selectedID])
            self.DBManager.exec_query(f"DELETE FROM {self.DB_TABLE} WHERE file_id IN ({selectedID})")
            self.RefreshData()
            Paths = self.Data_atIndex(SelectedIndexes, [self.DB_FIELDS.index("file_path")])
            #TODO: ENABLE IN PRODUCTION
            # if Delete:
            #     for path in Paths:
            #         if os.path.isfile(path):
            #             os.remove(path)
        else:
            selectedID = set([index.row() for index in SelectedIndexes.selectedIndexes()])
            if len(selectedID) == self.rowCount():
                self.removeRows(0, self.rowCount())
            else:
                OFFSET = 0
                for R in selectedID:
                    self.removeRow(R - OFFSET)
                    OFFSET += 1


    def UpdateTrack_Rating(self, Indexes: [QtCore.QModelIndex], rating: float):
        """
        Updates of the selected index and Refreshes data

        Parameters
        ----------
        Indexes: [QtCore.QModelIndex]
            index of rows to be updated
        rating: float
            rating to update to
        """
        Indexes = ", ".join([f"'{v}'" for v in self.Data_atIndex(Indexes = Indexes, Columns = [0])])
        self.DBManager.exec_query(f"""
        UPDATE {self.DB_TABLE}
        SET rating = {rating}
        WHERE
            file_id IN ({Indexes})
        """)
        self.RefreshData()

    def SearchModel(self, query: str, View: QtWidgets.QTableView):
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
                View.showRow(Row)
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
                View.showRow(Row)
            else:
                View.hideRow(Row)

    def SearchBrowser(self, Indexes: [QtCore.QModelIndex]):
        """
        Queries a browser

        Parameters
        ----------
        Indexes: [QtCore.QModelIndex]
            data to use
        """
        for index in Indexes:
            if index.column() == self.DB_FIELDS.index("file_name"):
                query = index.data()
                break

    def SearchFileSystem(self, Indexes: [QtCore.QModelIndex]):
        """
        Searches File system for the given Path

        Parameters
        ----------
         Indexes: [QtCore.QModelIndex]
            Data to use to run the query
        """
        for index in Indexes:
            if index.column() == self.DB_FIELDS.index("file_path"):
                query = index.data()

    def SearchSimilarField(self, Indexes: [QtCore.QModelIndex], Filed: str):
        """
        Searches the parent VIew for the Similar Fields

        Parameters
        ----------
        Indexes: [QtCore.QModelIndex]
            data to search for matches
        Filed: str
            Field to search in
        """
        for index in Indexes:
            if index.column() == self.DB_FIELDS.index(Filed):
                query = index.data()
                break
        if query not in ["", None, " "]:
            self.SearchModel(query, self.ParentView)

class GroupItems_Model(QtGui.QStandardItemModel):
    """
    Model to set all the data about grouping a given DB table and applies a mask on a view
    """
    def __init__(self, Driver: DataBaseManager, ParentView: QtWidgets.QTableView, Table: str, Field: str):
        """
        Class Constructor

        Parameters
        ----------
        Driver: DataBaseManager
            driver to use internally to run queries
        ParentView: QtWidgets.QTableView
            parent view that this Model masks
        Table: str
            Table name of the table to monitor
        Field: str
            grouping field
        """
        super().__init__()
        self.Driver = Driver
        self.ParentView = ParentView
        self.DB_FIELDS = self.Driver.db_fields
        self.DB_TABLE = Table
        self.Group_Field = Field
        self.LoadData(Field)

    def ApplyGroup(self, Index: QtCore.QModelIndex):
        """
        Applies a mask using the field selected

        Parameters
        ----------
        Index: item index double clicked
        """
        query = Index.data()
        if query in ["", None]:
            return None

        if self.Group_Field == "folder":
            Col = self.DB_FIELDS.index("file_path")
            Model = self.ParentView.model()
            for Row in range(Model.rowCount()):
                data = Model.index(Row, Col).data()
                if data.find(query) != -1:
                    self.ParentView.showRow(Row)
                else:
                    self.ParentView.hideRow(Row)

        elif self.Group_Field in ["rating", "genre", "date", "artist", "album"]:
            Col = self.DB_FIELDS.index(self.Group_Field)
            Model = self.ParentView.model()
            for Row in range(Model.rowCount()):
                data = Model.index(Row, Col).data()
                if data == query:
                    self.ParentView.showRow(Row)
                else:
                    self.ParentView.hideRow(Row)
        else:
            return None

    def LoadData(self, Group: str):
        self.Group_Field = Group
        if Group == "folder":
            ResultSet = self.Driver.exec_query(r"""
            SELECT DISTINCT REPLACE(file_path, '\'||file_name, '')
            FROM library
            WHERE  (file_path NOT IN ("", " "))
            ORDER BY file_path
            """)
        else:
            ResultSet = self.Driver.exec_query(f"""
            SELECT DISTINCT {Group}
            FROM {self.DB_TABLE}
            WHERE  ({Group} NOT IN ("", " "))
            ORDER BY {Group}
            """)
        self.removeRows(0, self.rowCount())
        for Row in ResultSet:
            self.appendRow(QtGui.QStandardItem(str(Row)))


class ApolloDataProvider:
    """
    Data and Model Provider for all classes
    """
    def __init__(self):
        """Constructor"""
        self.DataModels = {}

    def AddModel(self, DataModel, Key):
        self.DataModels[Key] = DataModel

    def GetModel(self, Key):
        if (Key in self.DataModels.keys()):
            return self.DataModels.get(Key)
        else:
            raise NotImplementedError()
