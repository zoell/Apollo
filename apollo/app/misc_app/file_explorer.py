from PySide6 import QtCore, QtWidgets, QtGui

from apollo.gui.ui_file_exp_ui import Ui_MainWindow
from apollo import PathUtils as PU

import os

class CheckableFileSystemModel(QtWidgets.QFileSystemModel): # Untested
    """
    Subclassing hte Filesystem model to add checkboxes
    """
    checkStateChanged = QtCore.Signal(str, bool)

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.checkStates = {}
        self.rowsInserted.connect(self.checkAdded) #type: ignore
        self.rowsRemoved.connect(self.checkParent) #type: ignore
        self.rowsAboutToBeRemoved.connect(self.checkRemoved) #type: ignore

    def checkState(self, index):
        """
        Gets the state of the path items and returns it

        :Args:
            index: QModelIdnex
                index of the item to get path form

        :Return:
            returs the state of the path item if checked or unchecked
        """
        return self.checkStates.get(self.filePath(index), QtCore.Qt.Unchecked)

    def setCheckState(self, index, state, emitStateChange=True):
        """
        Gets the file path of the index object and Emits a signal on state change.

        :Args:
            index: QModelIdnex
                index of the item in the model
            state: Qt.Unchecked
                state of the item (Checked/Unchecked)
            emitStateChange: bool
                sets if the signal should be emitted
        """
        path = self.filePath(index)
        if self.checkStates.get(path) == state:
            return
        self.checkStates[path] = state
        if emitStateChange:
            self.checkStateChanged.emit(path, bool(state))

    def checkAdded(self, parent, first, last):
        """
        if a file/directory is added, ensure it follows the parent state as long
        as the parent is already tracked; note that this happens also when
        expanding a directory that has not been previously loaded

        :Args:
            parent: QModelIdnex
            first: Int
            last: Int
        """
        if not parent.isValid():
            return
        if self.filePath(parent) in self.checkStates:
            state = self.checkState(parent)
            for row in range(first, last + 1):
                index = self.index(row, 0, parent)
                path = self.filePath(index)
                if path not in self.checkStates:
                    self.checkStates[path] = state
        self.checkParent(parent)

    def checkRemoved(self, parent, first, last):
        """
        remove items from the internal dictionary when a file is deleted;
        note that this *has* to happen *before* the model actually updates,
        that's the reason this function is connected to rowsAboutToBeRemoved

        :Args:
            parent: QModelIdnex
            first: Int
            last: Int
        """
        for row in range(first, last + 1):
            path = self.filePath(self.index(row, 0, parent))
            if path in self.checkStates:
                self.checkStates.pop(path)

    def checkParent(self, parent):
        """
        verify the state of the parent according to the children states
        :Args:
            parent: QModelIdnex
                index of the parent object passed in
        """
        if not parent.isValid():
            return
        childStates = [self.checkState(self.index(r, 0, parent)) for r in range(self.rowCount(parent))]
        newState = QtCore.Qt.Checked if all(childStates) else QtCore.Qt.Unchecked
        oldState = self.checkState(parent)
        if newState != oldState:
            self.setCheckState(parent, newState)
            self.dataChanged.emit(parent, parent)
        self.checkParent(parent.parent())

    def flags(self, index):
        """
        :Args:
            index: QModelIdnex
                index of the object passed in
        :Return:
            calls the flag method of the parent class and returns the flags of the index obj
        """
        return super().flags(index) | QtCore.Qt.ItemIsUserCheckable

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
        :Args:
            index: QModelIdnex
                index of the parent object passed in
            role: Qt.DisplayRole

        :Return:
            calls the data method of the parent class and returns the data
        """
        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            return self.checkState(index)
        return super().data(index, role)

    def setData(self, index: QtCore.QModelIndex, value, role, checkParent=True, emitStateChange=True):
        """
        set the data for the children, but do not emit the state change,
        and don't check the parent state (to avoid recursion)

        :Args:
            index: QModelIdnex
                index of the model
            value: Any
                value to set at the index
            role: Qt.DisplayRole
                role of ht index object
            checkParent: bool
                checks th4e parent
            emitStateChange: bool
                enable/disables the signal
        """
        if role == QtCore.Qt.CheckStateRole and index.column() == 0:
            self.setCheckState(index, value, emitStateChange)
            for row in range(self.rowCount(index)):
                self.setData(self.index(row, 0, index), value, QtCore.Qt.CheckStateRole,
                            checkParent=False, emitStateChange=False)
            self.dataChanged.emit(index, index)
            if checkParent:
                self.checkParent(index.parent())
            return True

        return super().setData(index, value, role)


class FileExplorer(Ui_MainWindow, QtWidgets.QMainWindow): # Untested
    """
    File Explore that Apollo will reimplement adn exted for each UI elemet that needs and exlorer
    """
    def __init__(self, _filter: str = "dir", _type: str = "nocheckbox"):
        """Constructor"""
        super().__init__()
        self.setupUi(self)
        self.fill_FilePathTree(self.treeView, _type)
        self.applyFilter(_filter)

        self.SelectedFiles = []
        self.buttonBox.rejected.connect(self.close)

    def applyFilter(self, _filter):
        if _filter == "dir":
            self.FilePathModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        if _filter == "files":
            self.FilePathModel.setFilter(QtCore.QDir.AllEntries | QtCore.QDir.NoDotAndDotDot)

    def disableCheckbox(self):
        self.FilePathModel = QtWidgets.QFileSystemModel()
        self.FilePathModel.setRootPath("")
        self.FilePathModel.setReadOnly(True)
        self.FilePathModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.treeView.setModel(self.FilePathModel)

    def enableCheckbox(self):
        self.FilePathModel = CheckableFileSystemModel()
        self.FilePathModel.setRootPath("")
        self.FilePathModel.setReadOnly(True)
        self.FilePathModel.setFilter(QtCore.QDir.AllDirs | QtCore.QDir.NoDotAndDotDot)
        self.treeView.setModel(self.FilePathModel)

    def fill_FilePathTree(self, TreeView: QtWidgets.QTreeView, _type: str):
        """
        Fills the tree model for the file dir struct

        :Args:
            TreeView: the treeview to set data to
        """
        if _type == "checkbox":
            self.enableCheckbox()
        else:
            self.disableCheckbox()

        TreeView.setModel(self.FilePathModel)
        TreeView.resizeColumnToContents(1)
        TreeView.hideColumn(1)
        TreeView.hideColumn(2)
        TreeView.hideColumn(3)

    def get_FilePath(self):
        """
        gets all the file paths that have been selected
        """
        SelectedPaths = [K for K, V in self.FilePathModel.checkStates.items() if V == 2]
        SelectedPaths.sort()

        for Item in SelectedPaths:
            # handles error for secured system files
            try:
                # filters out mount related issues
                if os.path.ismount(Item):
                    subdirs = os.listdir(Item)
                    Item = Item.replace("/", "")
                else:
                    subdirs = os.listdir(Item)
                # compress the directory tree if all the file in the parent are selected
                for subdir in subdirs:
                    if ("/".join([Item, subdir])) in SelectedPaths:
                        SelectedPaths.pop(SelectedPaths.index("/".join([Item, subdir])))
            # deals with persission error and removes those files
            except PermissionError:
                if len(SelectedPaths) > 0:
                    SelectedPaths.pop(SelectedPaths.index(Item))
                continue
        return SelectedPaths

    def get_Path(self, index):
        return self.FilePathModel.filePath(index)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    UI = FileExplorer(_type="checkbox")
    UI.show()
    app.exec()
