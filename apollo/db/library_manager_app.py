import os, sys, time
from threading import Thread
from threading import Event as ThreadEvent
from typing import Callable

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QModelIndex, Qt

from apollo.utils import PathUtils as PU
from apollo.utils import AppConfig
from apollo.gui.ui_library_manager_ui import Ui_MainWindow as LibraryManager_UI
from apollo.gui.ui_LEDT_dialog import LEDT_Dialog as LineEdit_Dialog
from apollo.app import FileExplorer
from apollo.db import LibraryManager, Connection


LBT_FILE_FILTERS = ("MP3", "AAC", "M4A", "MPC", "OGG", "FLAC",
                    "ALAC", "APE", "Opus", "TAK", "WavPack",
                    "WMA", "WAV", "MIDI", "MOD", "UMX", "XM")


class FileScanner_Thread(Thread):  # untested
    FILE_FILTERS = LBT_FILE_FILTERS

    def __init__(self, FileQueue: list, Ext: list, DB_name: str, Slot: Callable = lambda x: ''):
        super().__init__()
        self.daemon = False
        self.name = "FileScanner_Thread"
        self.FileQueue = FileQueue
        self.Slot = Slot
        self.Extension = [K for K, V in zip(FileScanner_Thread.FILE_FILTERS, Ext) if V == 1]
        self.Manager = LibraryManager(DB_name)
        self.DeclareEvents()

    def finished(self):
        """
        Interface function to call at the end of the thread
        """
        pass

    def run(self) -> None:
        while self.Running.is_set():
            if self.Pause.is_set():
                time.sleep(0.1)
                continue
            if self.Scanning.is_set():
                for Dir in self.FileQueue:
                    self.Manager.ScanDirectory(Dir, self.Extension, self.Slot)
                self.Scanning.clear()
                self.exit()

    def exit(self):
        self.Running.clear()
        self.finished()

    def DeclareEvents(self):
        self.Running = ThreadEvent()
        self.Scanning = ThreadEvent()
        self.Pause = ThreadEvent()
        self.Pause.clear()

    def start(self):
        self.Running.set()
        self.Scanning.set()
        super().start()
        return self


class LibraryManager_App(QtWidgets.QMainWindow, LibraryManager_UI):
    LBT_FILE_FILTERS = LBT_FILE_FILTERS

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.setupUi(self)
        self.LibManager = LibraryManager()
        self.Config = AppConfig()
        self.CheckDB_config()

        self.DB_ManagerTab = DBManager_Tab(self)
        self.Metadata_ManagerTab = MetadataManager_Tab(self)

    def CheckDB_config(self):
        """
        Checks for all te files that are declared in the config if the exist
        """
        for indx in self.Config["MONITERED_DB"].keys():
            if not os.path.isfile(self.Config[f"MONITERED_DB/{indx}/db_loc"]):
                del self.Config[f"MONITERED_DB/{indx}"]
            for f_indx, file in enumerate(self.Config[f"MONITERED_DB/{indx}/file_mon"]):
                if not os.path.isdir(file):
                    del self.Config[f"MONITERED_DB/{indx}/file_mon"][f_indx]
        self.Config.Manager.DumpConfig()

    def closeEvent(self, event: QtGui.QCloseEvent):
        """
        CLoses the UI and related sub windows

        Parameters
        ----------
        event : QtGui.QCloseEvent
            CLose event of main window
        """
        self.CheckDB_config()
        self.DB_ManagerTab.close()
        return super().closeEvent(event)


class FilesMonitored_Exp(FileExplorer):

    def __init__(self, ParentView: QtWidgets.QListView):
        super().__init__(_type="checkbox")
        self.ParentView = ParentView

        # Function Bindings
        self.buttonBox.accepted.connect(lambda: self.FillModel())

    def FillModel(self):
        Items = self.get_FilePath()
        Model = QtGui.QStandardItemModel()
        for R, file_path in enumerate(Items):
            itm = QtGui.QStandardItem(str(file_path))
            itm.setCheckable(True)
            itm.setCheckState(Qt.Checked)
            Model.insertRow(R, itm)
        self.ParentView.setModel(Model)
        self.close()

    def show(self) -> None:
        # is done to clear old references for all old checked files and adds new file refrences
        self.FilePathModel.checkStates = {}
        model = self.ParentView.model()
        for item in range(model.rowCount()):
            path = model.index(item, 0).data()
            if os.path.isdir(path):
                self.FilePathModel.checkStates[path] = QtCore.Qt.Checked

        super().raise_()
        return super().show()


class DBnameFileExp(FileExplorer):

    def __init__(self, NameEdit: QtWidgets.QLineEdit, PathEdit: QtWidgets.QLineEdit):
        super().__init__()
        self.NameEdit = NameEdit
        self.PathEdit = PathEdit
        self.Config = AppConfig()
        self.UI_Bindings()

    def UI_Bindings(self):
        self.buttonBox.accepted.connect(self.AcceptPath)
        self.buttonBox.rejected.connect(self.close)

        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.RequestContextMenu)

    def RequestContextMenu(self, Point):
        MainMenu = QtWidgets.QMenu()
        MainMenu.addAction("Add New Folder").triggered.connect(self.Add_New_Folder)
        MainMenu.addAction("Select Folder").triggered.connect(self.SelectedPath)
        MainMenu.addAction("Rename Folder").triggered.connect(self.Rename_Folder)
        MainMenu.addAction("Delete Folder").triggered.connect(self.Delete_Folder)
        MainMenu.addAction("Create DataBase").triggered.connect(self.Create_DataBase)

        Cursor = QtGui.QCursor()
        MainMenu.exec(Cursor.pos())

    def Create_DataBase(self):
        def CreateDB():
            Index = self.treeView.selectedIndexes()
            if len(Index) != 0:
                NAME = self.LEDT_widget.lineEdit.text()
                OG_path = self.FilePathModel.filePath(Index[0])
                NEW_path = PU.PathJoin(OG_path, f"{NAME}.db".replace(" ", "_").lower())
                self.PathEdit.setText(NEW_path)
                self.Config[f"MONITERED_DB/{NAME}"] = {
                    "name": NAME,
                    "db_loc": NEW_path,
                    "file_mon": [],
                    "filters": [1 for _ in LBT_FILE_FILTERS]
                }
                if not os.path.isfile(NEW_path):
                    with Connection.connect(NEW_path) as con:
                        pass
            self.LEDT_widget.buttonBox.accepted.connect(lambda: None)
            self.LEDT_widget.close()

        if not hasattr(self, "LEDT_widget"):
            self.LEDT_widget = LineEdit_Dialog()

        self.LEDT_widget.buttonBox.accepted.connect(CreateDB)
        self.LEDT_widget.setWindowTitle("Add New DB")
        self.LEDT_widget.lineEdit.clear()
        self.LEDT_widget.show()
        self.LEDT_widget.raise_()

    def Delete_Folder(self):
        Index = list(map(lambda x: self.FilePathModel.filePath(x), self.treeView.selectedIndexes()))
        if len(Index) != 0:
            src = Index[0]
            if not os.path.ismount(src):
                PU.PurgeDirectory(src)

    def Add_New_Folder(self):

        def CreateDirectory():
            Index = list(map(lambda x: self.FilePathModel.filePath(x), self.treeView.selectedIndexes()))
            if len(Index) != 0 and PU.WinFileValidator(self.LEDT_widget.lineEdit.text()):
                path = os.path.normpath(os.path.join(Index[0], self.LEDT_widget.lineEdit.text()))
                os.mkdir(path)
            self.LEDT_widget.buttonBox.accepted.connect(lambda: None)
            self.LEDT_widget.close()

        if not hasattr(self, "LEDT_widget"):
            self.LEDT_widget = LineEdit_Dialog()

        self.LEDT_widget.buttonBox.accepted.connect(CreateDirectory)
        self.LEDT_widget.setWindowTitle("Add New Folder")
        self.LEDT_widget.lineEdit.clear()
        self.LEDT_widget.show()
        self.LEDT_widget.raise_()

    def Rename_Folder(self):

        def RenameDirectory():
            Index = list(map(lambda x: self.FilePathModel.filePath(x), self.treeView.selectedIndexes()))
            if len(Index) != 0 and PU.WinFileValidator(self.LEDT_widget.lineEdit.text()):
                if os.path.ismount(Index[0]):
                    self.label.setText("Tried to rename A Drive")
                    self.LEDT_widget.close()
                    return 0
                path = os.path.normpath(os.path.join(os.path.split(Index[0])[0], self.LEDT_widget.lineEdit.text()))
                os.rename(Index[0], path)
            self.LEDT_widget.buttonBox.accepted.connect(lambda: None)
            self.LEDT_widget.close()

        if not hasattr(self, "LEDT_widget"):
            self.LEDT_widget = LineEdit_Dialog()

        self.LEDT_widget.buttonBox.accepted.connect(RenameDirectory)
        self.LEDT_widget.setWindowTitle("Rename Folder")
        self.LEDT_widget.lineEdit.clear()
        self.LEDT_widget.show()
        self.LEDT_widget.raise_()

    def SelectedPath(self):
        Index = self.treeView.selectedIndexes()
        if len(Index) != 0:
            NAME = self.NameEdit.text()
            OG_path = self.FilePathModel.filePath(Index[0])
            NEW_path = PU.PathJoin(OG_path, f"{NAME}.db".replace(" ", "_").lower())
            self.PathEdit.setText(NEW_path)

    def AcceptPath(self):
        self.OGPATH = self.PathEdit.text()
        self.close()

    def show(self):
        self.OGPATH = self.PathEdit.text()
        super().raise_()
        return super().show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if hasattr(self, "LEDT_widget"): self.LEDT_widget.close()
        self.PathEdit.setText(self.OGPATH)
        return super().closeEvent(event)


class DBManager_Tab:

    def __init__(self, UI: LibraryManager_App):
        """
        Class Constructor

        Parameters
        ----------
        UI: LibraryManager_App
            injected UI
        """
        self.UI = UI
        self.InternalState_Flags()
        self.fillData(self.UI.Config["CURRENT_DB"])
        self.UpdateComboBox()
        self.FunctionBindings()

    def InternalState_Flags(self):
        """
        Inits all the class flags
        """
        self.FileScannerRunning = 0
        self.LBT_CURRENT_LOADED_DB = ""

    def FunctionBindings(self):
        """
        Binds all the functions with the UI
        """
        self.UI.LBT_PSB_libnext.pressed.connect(lambda: self.DB_LEDT_TextChange(1))
        self.UI.LBT_PSB_libprev.pressed.connect(lambda: self.DB_LEDT_TextChange(-1))
        self.UI.LBT_CMBX_libname.currentTextChanged.connect(self.fillData)
        self.UI.LBT_LEDT_dbname.returnPressed.connect(self.Rename_DB)
        self.UI.LBT_PSB_libadd.pressed.connect(self.SaveNew_DB)
        self.UI.LBT_PSB_libremove.pressed.connect(self.Remove_DB)
        self.UI.LBT_PSB_librescan.pressed.connect(self.RescanFolders)
        self.UI.LBT_PSB_active.pressed.connect(self.SetAs_Active)
        self.UI.LBT_PSB_fileadd.pressed.connect(self.FileExp_MonitoredFiles_launch)
        self.UI.LBT_PSB_fileremove.pressed.connect(self.Remove_Folder)
        self.UI.LBT_PSB_libpathedit.pressed.connect(self.FileExp_DBDir_launch)

        # not implemented
        self.UI.LBT_PSB_import.pressed.connect(self.Import_DB)
        self.UI.LBT_PSB_export.pressed.connect(self.Export_DB)

    def Import_DB(self): ...

    def Export_DB(self): ...

    def SetAs_Active(self):
        self.UI.Config["CURRENT_DB"] = self.LBT_CURRENT_LOADED_DB

    def FileExp_MonitoredFiles_launch(self):
        """
        Launches a file Explorer for the monitored file listview to add directories
        """
        if not hasattr(self, "FileExp_mon"):
            self.FileExp_mon = FilesMonitored_Exp(self.UI.LBT_LSV_filesmon)
        self.FileExp_mon.show()

    def FileExp_DBDir_launch(self):
        """
        Launches a FileExplorer for the DB path to add a directory path that the DB will be placed
        """
        if not hasattr(self, "FileExp_db"):
            self.FileExp_db = DBnameFileExp(self.UI.LBT_LEDT_dbname, self.UI.LBT_LEDT_dbpath)
        self.FileExp_db.show()

    def UpdateComboBox(self):
        """
        Updates the Combobox with all the DBs that are loaded in config
        """
        Model = self.UI.LBT_CMBX_libname.model()
        Model.removeRows(0, self.UI.LBT_CMBX_libname.count())
        for indx, Key in enumerate(self.UI.Config["MONITERED_DB"].keys()):
            Model.insertRow(indx, QtGui.QStandardItem(str(Key)))

        # sets the current Loaded item in CMBX
        for idx in range(self.UI.LBT_CMBX_libname.count()):
            if self.LBT_CURRENT_LOADED_DB == "":
                self.LBT_CURRENT_LOADED_DB = self.UI.Config["CURRENT_DB"]
            if self.UI.LBT_CMBX_libname.itemText(idx) == self.LBT_CURRENT_LOADED_DB:
                self.UI.LBT_CMBX_libname.setCurrentIndex(idx)

    def Remove_Folder(self):
        """
        removes all the unchecked files from the DB
        """
        # get the file filters for the DB
        Model = self.UI.LBT_LSV_filesmon.model()
        FILE_MON = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Unchecked:
                Model.removeRow(R)
        self.Updated_DB()

    def Remove_DB(self):
        """
        Removes the DB and its config
        """
        if not os.path.isfile(self.UI.LBT_LEDT_dbpath.text()):
            return None
        OG_NAME = self.UI.LBT_CMBX_libname.currentText()
        os.remove(self.UI.Config[f"MONITERED_DB/{OG_NAME}/db_loc"])
        del self.UI.Config[f"MONITERED_DB/{OG_NAME}"]
        self.UI.Config[f"CURRENT_DB"] = self.UI.Config[f"MONITERED_DB"].keys()[0]
        self.UpdateComboBox()

    def Rename_DB(self):
        """
        Renames the current loaded DB
        """
        if not PU.WinPathValidator(self.UI.LBT_LEDT_dbname.text()):
            return None

        OG_NAME = self.UI.LBT_CMBX_libname.currentText()
        NEW_NAME = self.UI.LBT_LEDT_dbname.text().strip()
        OG_path = self.UI.LBT_LEDT_dbpath.text()
        NEW_path = PU.PathJoin(os.path.split(OG_path)[0], f"{NEW_NAME}.db".replace(" ", "_").lower())

        self.UI.LBT_LEDT_dbpath.setText(NEW_path)
        os.rename(src=OG_path, dst=NEW_path)

        # writes new config and deletes the old config
        self.UI.Config[f"MONITERED_DB/{NEW_NAME}"] = {
            "name": NEW_NAME,
            "db_loc": NEW_path,
            "file_mon": (self.UI.Config[f"MONITERED_DB/{OG_NAME}/file_mon"]),
            "filters": (self.UI.Config[f"MONITERED_DB/{OG_NAME}/filters"])
        }
        del self.UI.Config[f"MONITERED_DB/{OG_NAME}"]

        if self.UI.Config[f"CURRENT_DB"] == OG_NAME:
            self.UI.Config[f"CURRENT_DB"] = NEW_NAME

        self.LBT_CURRENT_LOADED_DB = NEW_NAME
        self.UpdateComboBox()

    def SaveNew_DB(self):
        """
        Saves the Data and creates a New DB
        """
        if not PU.WinPathValidator(self.UI.LBT_LEDT_dbname.text()):
            return None

        OG_NAME = self.UI.LBT_CMBX_libname.currentText()
        NEW_NAME = self.UI.LBT_LEDT_dbname.text().strip()
        OG_path = self.UI.LBT_LEDT_dbpath.text()
        NEW_path = PU.PathJoin(os.path.split(OG_path)[0], f"{NEW_NAME}.db".replace(" ", "_").lower())

        # gets the files that are currently scanned and loaded data for
        Model = self.UI.LBT_LSV_filters.model()
        FILTERS = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                FILTERS.append(1)
            else:
                FILTERS.append(0)

        # get the file filters for the DB
        Model = self.UI.LBT_LSV_filesmon.model()
        FILE_MON = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                FILE_MON.append(Data.data())

        if not os.path.isfile(NEW_path):
            with Connection(NEW_path) as con:
                pass

        # adds the new DB info to the config
        self.UI.Config[f"MONITERED_DB/{NEW_NAME}"] = {
            "name": NEW_NAME,
            "db_loc": NEW_path,
            "file_mon": FILE_MON,
            "filters": FILTERS
        }

        self.LBT_CURRENT_LOADED_DB = NEW_NAME
        self.UpdateComboBox()

    def Updated_DB(self):
        """
        Updates the currently loaded db with new info
        """

        if not PU.WinPathValidator(self.UI.LBT_LEDT_dbname.text()):
            return None

        NEW_NAME = self.UI.LBT_LEDT_dbname.text().strip()
        OG_path = self.UI.LBT_LEDT_dbpath.text()

        # gets the files that are currently scanned and loaded data for
        Model = self.UI.LBT_LSV_filters.model()
        FILTERS = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                FILTERS.append(1)
            else:
                FILTERS.append(0)

        # get the file filters for the DB
        Model = self.UI.LBT_LSV_filesmon.model()
        FILE_MON = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                FILE_MON.append(Data.data())

        # adds the new DB info to the config
        self.UI.Config[f"MONITERED_DB/{NEW_NAME}"] = {
            "name": NEW_NAME,
            "db_loc": OG_path,
            "file_mon": FILE_MON,
            "filters": FILTERS
        }

        self.LBT_CURRENT_LOADED_DB = NEW_NAME
        self.UpdateComboBox()

    def fillData(self, DB_name):
        """
        FIll ths UI with Data Corresponding to the DB file open

        Parameters
        ----------
        DB_name: str, optional
            DB name to load data for, bu default None
        """
        if DB_name != "":
            self.LBT_CURRENT_LOADED_DB = DB_name

            path = (self.UI.Config[f"MONITERED_DB/{DB_name}/db_loc"])
            self.UI.LBT_LEDT_dbname.setText(str(DB_name))
            self.UI.LBT_LEDT_dbpath.setText(str(path))

            # Updates DB stats
            self.UI.LibManager.connect(path, check=True)
            self.UI.LBT_LEDT_totartist.setText(f"{str(self.UI.LibManager.TableArtistcount())} Artists")
            self.UI.LBT_LEDT_totalbum.setText(f"{str(self.UI.LibManager.TableAlbumcount())} Albums")
            self.UI.LBT_LEDT_tottrack.setText(f"{str(self.UI.LibManager.TableTrackcount())} Tracks")
            self.UI.LBT_LEDT_totplaytime.setText(f"{str(self.UI.LibManager.TablePlaytime())}")
            self.UI.LBT_LEDT_totsize.setText(f"{str(self.UI.LibManager.TableSize())} GB")
            self.UI.LBT_LEDT_topartist.setText(f"{str(self.UI.LibManager.Topartist())}")
            self.UI.LBT_LEDT_toptrack.setText(f"{str(self.UI.LibManager.Toptrack())}")
            self.UI.LBT_LEDT_topalbum.setText(f"{str(self.UI.LibManager.TopAlbum())}")
            self.UI.LBT_LEDT_topgenre.setText(f"{str(self.UI.LibManager.Topgenre())}")
            self.UI.LBT_LEDT_totplay.setText(f"{str(self.UI.LibManager.TablePlaycount())} Plays")

            # Updates DB files
            paths = (self.UI.Config[f"MONITERED_DB/{DB_name}/file_mon"])
            Model = QtGui.QStandardItemModel()
            for R, file_path in enumerate(paths):
                itm = QtGui.QStandardItem(str(file_path))
                itm.setCheckable(True)
                itm.setCheckState(Qt.Checked)
                Model.insertRow(R, itm)
            self.UI.LBT_LSV_filesmon.setModel(Model)

            # Updates DB ext Filters
            filters = (self.UI.Config[f"MONITERED_DB/{DB_name}/filters"])
            Model = QtGui.QStandardItemModel()
            for (R, state), filt in zip(enumerate(filters), LibraryManager_App.LBT_FILE_FILTERS):
                itm = QtGui.QStandardItem(str(filt))
                itm.setCheckable(True)
                if state == 1:
                    itm.setCheckState(Qt.Checked)
                else:
                    itm.setCheckState(Qt.Unchecked)
                Model.insertRow(R, itm)
            self.UI.LBT_LSV_filters.setModel(Model)

    def DB_LEDT_TextChange(self, offset: int = 1):
        """
        Cycles through all the DB that are added to the config

        Parameters
        ----------
        offset : int, optional
            goes forward or backward according to offset, by default 1
        """
        # resets for pointer at end
        if self.UI.LBT_CMBX_libname.count() <= (self.UI.LBT_CMBX_libname.currentIndex() + offset):
            self.UI.LBT_CMBX_libname.setCurrentIndex(0)

        # resets for pointer at 0
        elif 0 > (self.UI.LBT_CMBX_libname.currentIndex() + offset):
            self.UI.LBT_CMBX_libname.setCurrentIndex(self.UI.LBT_CMBX_libname.count() - 1)

        # back or forward
        else:
            self.UI.LBT_CMBX_libname.setCurrentIndex(self.UI.LBT_CMBX_libname.currentIndex() + offset)

    def RescanFolders(self):
        """
        Launches a thread to scan all the folders monitored
        """
        def started():
            self.FileScannerRunning = 1

        def finished():
            self.FileScannerRunning = 0

        if not self.FileScannerRunning:
            self.UI.statusBar.showMessage("Scanning For Files! This Might Take A While")

            # gets the selected File
            Model = self.UI.LBT_LSV_filesmon.model()
            FILE_MON = []
            for R in range(Model.rowCount()):
                Data = Model.index(R, 0)
                if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                    FILE_MON.append(Data.data())

            # gets the selected FileExt
            Model = self.UI.LBT_LSV_filters.model()
            FILTERS = []
            for R in range(Model.rowCount()):
                Data = Model.index(R, 0)
                if Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked:
                    FILTERS.append(1)
                else:
                    FILTERS.append(0)

            DB = (self.UI.Config[f"MONITERED_DB/{self.UI.LBT_CMBX_libname.currentText()}/db_loc"])
            if FILTERS != [] and FILE_MON != []:
                started()
                ScannerThread = FileScanner_Thread(FILE_MON, FILTERS, DB, self.UI.statusBar.showMessage)
                ScannerThread.start()
                ScannerThread.finished = finished
                self.Updated_DB()
            else:
                self.UI.statusBar.showMessage("Scanning For Files! No directory Selected")
        else:
            self.UI.statusBar.showMessage("Scanning For Files!")

    def close(self):
        """
        UI destructor for all the objects initialized and open
        """
        if hasattr(self, "FileExp_db"):
            self.FileExp_db.close()
        if hasattr(self, "FileExp_mon"):
            self.FileExp_mon.close()


class MetadataManager_Tab:

    def __init__(self, UI: LibraryManager_App):
        self.UI = UI


if __name__ == "__main__":
    from apollo.plugins.app_theme import Theme


    def themeUpdate(Theme_obj):
        STYLESHEET = (Theme_obj.GenStyleSheet(Theme.THEME))
        Theme.STYLESHEET = STYLESHEET
        return STYLESHEET


    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    Theme_obj = Theme(App = app)

    UI = LibraryManager_App()
    UI.Theme = Theme_obj

    UI.LBT_PSB_import.pressed.connect(lambda: app.setStyleSheet(themeUpdate(Theme_obj)))

    UI.show()
    app.exec()
