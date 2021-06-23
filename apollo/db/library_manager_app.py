# type: ignore
import os, sys, time
from threading import Thread
from threading import Event as ThreadEvent
from typing import Callable

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QModelIndex, Qt

from apollo.gui.ui_library_manager_ui import Ui_MainWindow as LibraryManager_UI
from apollo.utils import AppConfig
from apollo.db import LibraryManager, FileManager
from apollo import PathUtils as PU
from apollo.app import FileExplorer


class FilesMonitored_Exp(FileExplorer):

    def __init__(self, ParentView: QtWidgets.QListView):
        super().__init__(_type = "checkbox")
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
            Model.insertRow(R,itm)
        self.ParentView.setModel(Model)
        self.close()

    def show(self) -> None:
        # is done to clear old refrences for all old checked files and adds new file refrences
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
        self.UI_Bindings()

    def UI_Bindings(self):
        self.buttonBox.accepted.connect(self.AcceptPath)
        self.buttonBox.rejected.connect(self.close)

        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.RequestContextMenu)

    def RequestContextMenu(self, Point):
        MainMenu = QtWidgets.QMenu()
        MainMenu.addAction("Add New Folder")
        MainMenu.addAction("Select Folder").triggered.connect(self.SelectedPath)
        MainMenu.addAction("Rename Folder")
        MainMenu.addAction("Delete Folder")
        MainMenu.addAction("Create DataBase")

        Cursor = QtGui.QCursor()
        MainMenu.exec(Cursor.pos())

    def SelectedPath(self):
        Index = self.treeView.selectedIndexes()
        if len(Index) != 0:
            NAME = self.NameEdit.text()
            OG_path = self.FilePathModel.filePath(Index[0])
            NEW_path = PU.PathJoin(OG_path, f"{NAME}.db".replace(" ","_").lower())
            self.PathEdit.setText(NEW_path)

    def AcceptPath(self):
        self.OGPATH = self.PathEdit.text()
        self.close()

    def show(self):
        self.OGPATH = self.PathEdit.text()
        super().raise_()
        return super().show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.PathEdit.setText(self.OGPATH)
        return super().closeEvent(event)


class FileScanner_Thread(Thread): # untested
    FILE_FILTERS = ["MP3", "AAC", "M4A", "MPC", "OGG", "FLAC",
                    "ALAC", "APE", "Opus", "TAK", "WavPack",
                    "WMA", "WAV", "MIDI", "MOD", "UMX", "XM"]

    def __init__(self, FileQueue: list, Ext: list, DB_name: str, Slot: Callable = lambda x: ''):
        super().__init__()
        self.daemon = False
        self.name = "FileScanner_Thread"
        self.FileQueue = FileQueue
        self.Slot = Slot
        self.Extension = [K for K, V in zip(FileScanner_Thread.FILE_FILTERS, Ext) if V == 1]
        self.Manager = LibraryManager(DB_name)
        self.DeclareEvents()

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

    LBT_CURRENT_LOADED_DB = ""
    LBT_FILE_FILTERS = ["MP3", "AAC", "M4A", "MPC", "OGG", "FLAC",
                        "ALAC", "APE", "Opus", "TAK", "WavPack",
                        "WMA", "WAV", "MIDI", "MOD", "UMX", "XM"]

    def __init__(self):
        """
        Class Constructor
        """
        super().__init__()
        self.setupUi(self)
        self.Theme = None
        self.LibManager = LibraryManager()
        self.Config = AppConfig()
        self.InternalState_Flags()

        self.BindingFunctions()
        self.UpadateComboBox()
        self.fillData(self.Config["CURRENT_DB"])

    def InternalState_Flags(self):
        self.FileScannerRunning = 1

    def BindingFunctions(self):
        """
        Connects all the function to all the buttons
        """
        self.LBT_CMBX_libname.currentTextChanged.connect(lambda name: (
            self.fillData(DB_name = name)
            )
        )
        self.LBT_LEDT_dbname.returnPressed.connect(self.DBName_Changed)
        self.LBT_PSB_fileadd.clicked.connect(self.FileExp_MonitoredFiles_launch)
        self.LBT_PSB_libpathedit.clicked.connect(self.FileExp_DBDir_launch)
        self.LBT_PSB_filerescan.clicked.connect(self.RescanFolders)

        self.LBT_PSB_libadd.clicked.connect(lambda: self.DBName_Changed("SAVE_NEW"))
        self.LBT_PSB_libnext.clicked.connect(lambda: (self.DB_LEDT_TextChange()))
        self.LBT_PSB_libprev.clicked.connect(lambda: (self.DB_LEDT_TextChange(-1)))


    def UpadateComboBox(self):
        Model = self.LBT_CMBX_libname.model()
        Model.removeRows(0, self.LBT_CMBX_libname.count())
        for indx, Key in enumerate(self.Config["MONITERED_DB"].keys()):
            Model.insertRow(indx, QtGui.QStandardItem(str(Key)))

        # sets the current Loaded item in CMBX
        for idx in range(self.LBT_CMBX_libname.count()):
            if self.LBT_CMBX_libname.itemText(idx) == self.Config["CURRENT_DB"]:
                self.LBT_CMBX_libname.setCurrentIndex(idx)

    def RescanFolders(self):
        self.statusBar.showMessage("Scanning For Files! This Might Take A While")

        # gets the selected File
        Model = self.LBT_LSV_filesmon.model()
        FILE_MON = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if (Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked):
                FILE_MON.append(Data.data())

        # gets the selected FileExt
        Model = self.LBT_LSV_filters.model()
        FILTERS = []
        for R in range(Model.rowCount()):
            Data = Model.index(R, 0)
            if (Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked):
                FILTERS.append(1)
            else:
                FILTERS.append(0)

        DB = (self.Config[f"MONITERED_DB/{self.LBT_CMBX_libname.currentText()}/db_loc"])
        ScannerThread = FileScanner_Thread(FILE_MON, FILTERS, DB, lambda m: self.statusBar.showMessage(m))
        ScannerThread.start()

    def fillData(self, DB_name):
        """
        FIll ths UI with Data Corresponding to the DB file open

        Parameters
        ----------
        _type : str, optional
            Type of data to be refreshed, by default ""
        DB_name: str, optional
            DB name to load data for, bu default None
        """
        if DB_name == "":
            return None
        LibraryManager_App.LBT_CURRENT_LOADED_DB = DB_name

        path = (self.Config[f"MONITERED_DB/{DB_name}/db_loc"])
        self.LBT_LEDT_dbname.setText(str(DB_name))
        self.LBT_LEDT_dbpath.setText(str(path))

        # Updates DB stats
        self.LibManager.connect(path, Check = True)
        self.LBT_LEDT_totartist.setText(f"{str(self.LibManager.TableArtistcount())} Artists")
        self.LBT_LEDT_totalbum.setText(f"{str(self.LibManager.TableAlbumcount())} Albums")
        self.LBT_LEDT_tottrack.setText(f"{str(self.LibManager.TableTrackcount())} Tracks")
        self.LBT_LEDT_totplaytime.setText(f"{str(self.LibManager.TablePlaytime())}")
        self.LBT_LEDT_totsize.setText(f"{str(self.LibManager.TableSize())} GB")
        self.LBT_LEDT_topartist.setText(f"{str(self.LibManager.Topartist())}")
        self.LBT_LEDT_toptrack.setText(f"{str(self.LibManager.Toptrack())}")
        self.LBT_LEDT_topalbum.setText(f"{str(self.LibManager.TopAlbum())}")
        self.LBT_LEDT_topgenre.setText(f"{str(self.LibManager.Topgenre())}")
        self.LBT_LEDT_totplay.setText(f"{str(self.LibManager.TablePlaycount())} Plays")

        # Updates DB files
        paths = (self.Config[f"MONITERED_DB/{DB_name}/file_mon"])
        Model = QtGui.QStandardItemModel()
        for R, file_path in enumerate(paths):
            itm = QtGui.QStandardItem(str(file_path))
            itm.setCheckable(True)
            itm.setCheckState(Qt.Checked)
            Model.insertRow(R,itm)
        self.LBT_LSV_filesmon.setModel(Model)

        #Updates DB ext Filters
        filters = (self.Config[f"MONITERED_DB/{DB_name}/filters"])
        Model = QtGui.QStandardItemModel()
        for (R, state), filt in zip(enumerate(filters), LibraryManager_App.LBT_FILE_FILTERS):
            itm = QtGui.QStandardItem(str(filt))
            itm.setCheckable(True)
            if state == 1:
                itm.setCheckState(Qt.Checked)
            else:
                itm.setCheckState(Qt.Unchecked)
            Model.insertRow(R,itm)
        self.LBT_LSV_filters.setModel(Model)

    def DBName_Changed(self, _type: str = "RENAME"):
        """
        Reacts to the change of teh DB name in the input LineEdit

        Parameters
        ----------
        _type : str, optional
            Type of operation to perform, by default "RENAME"

        Returns
        -------
        None
            If the DB name is not valid
        """
        if not PU.WinPathValidator(self.LBT_LEDT_dbname.text()):
            return None

        if self.LBT_CMBX_libname.currentText() == self.LBT_LEDT_dbname.text():
            return None

        OG_NAME = self.LBT_CMBX_libname.currentText()
        NEW_NAME = self.LBT_LEDT_dbname.text()
        OG_path = self.LBT_LEDT_dbpath.text()
        NEW_path = PU.PathJoin(os.path.split(OG_path)[0], f"{NEW_NAME}.db".replace(" ","_").lower())

        if _type == "RENAME": # renames the DB and the file too
            self.LBT_LEDT_dbpath.setText(NEW_path)
            os.rename(src = OG_path, dst = NEW_path)

            # writes new config and deletes the old config
            self.Config[f"MONITERED_DB/{NEW_NAME}"] = {
                "name": NEW_NAME,
                "db_loc": NEW_path,
                "file_mon": (self.Config[f"MONITERED_DB/{OG_NAME}/file_mon"]),
                "filters": (self.Config[f"MONITERED_DB/{OG_NAME}/filters"])
            }
            del self.Config[f"MONITERED_DB/{OG_NAME}"]

        if _type == "SAVE_NEW": # saves a new DB file
            # gets the files that are currently scanned and loaded data for
            Model = self.LBT_LSV_filters.model()
            FILTERS = []
            for R in range(Model.rowCount()):
                Data = Model.index(R, 0)
                if (Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked):
                    FILTERS.append(1)
                else:
                    FILTERS.append(0)

            # get the file filters for the DB
            Model = self.LBT_LSV_filesmon.model()
            FILE_MON = []
            for R in range(Model.rowCount()):
                Data = Model.index(R, 0)
                if (Data.data(QtCore.Qt.CheckStateRole) == QtCore.Qt.Checked):
                    FILE_MON.append(Data.data())

            # adds the new DB info to the config
            self.Config[f"MONITERED_DB/{NEW_NAME}"] = {
                "name": NEW_NAME,
                "db_loc": NEW_path,
                "file_mon": FILE_MON,
                "filters": FILTERS
            }
        self.Config["CURRENT_DB"] = NEW_NAME
        self.UpadateComboBox()

    def FileExp_MonitoredFiles_launch(self):
        """
        Launces a file Explorer for the moonitored file listview to add directories
        """
        if not hasattr(self, "FileExp_mon"):
            self.FileExp_mon = FilesMonitored_Exp(self.LBT_LSV_filesmon)
            self.Theme.SetSheet(self.FileExp_mon)

        self.FileExp_mon.show()

    def FileExp_DBDir_launch(self):
        """
        Launches a FileExplorer for the DB path to add a directory path that the DB will be placed
        """
        if not hasattr(self, "FileExp_db"):
            self.FileExp_db = DBnameFileExp(self.LBT_LEDT_dbname, self.LBT_LEDT_dbpath)
            self.Theme.SetSheet(self.FileExp_db)

        self.FileExp_db.show()

    def DB_LEDT_TextChange(self, offset: int = 1):
        """
        Cycles through all the DB that are added to the config

        Parameters
        ----------
        offset : int, optional
            goes forward or backward accordint to offset, by default 1
        """
        # resets for pointer at end
        if (self.LBT_CMBX_libname.count() <= (self.LBT_CMBX_libname.currentIndex() + offset)):
            self.LBT_CMBX_libname.setCurrentIndex(0)
        # resets for pointer at 0
        elif (0 > (self.LBT_CMBX_libname.currentIndex() + offset)):
            self.LBT_CMBX_libname.setCurrentIndex(self.LBT_CMBX_libname.count() - 1)
        # back or forward
        else:
            self.LBT_CMBX_libname.setCurrentIndex(self.LBT_CMBX_libname.currentIndex() + offset)

    def closeEvent(self, event: QtGui.QCloseEvent):
        """
        CLoses the UI and realted sub windows

        Parameters
        ----------
        event : QtGui.QCloseEvent
            CLose event of main window
        """
        if hasattr(self, "FileExp_db"): self.FileExp_db.close()
        if hasattr(self, "FileExp_mon"): self.FileExp_mon.close()
        return super().closeEvent(event)


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
