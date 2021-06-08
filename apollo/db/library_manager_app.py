from apollo.utils import AppConfig
import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt

from apollo.gui.ui_library_manager_ui import Ui_MainWindow as LibraryManager_UI
from apollo.db import LibraryManager

class LibraryManager_App(QtWidgets.QMainWindow, LibraryManager_UI):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LibManager = LibraryManager()
        self.Config = AppConfig()
        self.BindingFunctions()
        self.fillData(DB_name = self.Config["CURRENT_DB"])

    def fillData(self, _type = None, **kwargs):
        if _type == "DB" or _type == None:
            for Key in self.Config["MONITERED_DB"].keys():
                self.LBT_CMBX_libname.addItem(Key)

        if _type == "DB_STATS" or _type == None:
            self.LibManager.connect(self.Config[f"MONITERED_DB/{kwargs.get('DB_name')}/db_loc"])
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
            self.LibManager.close_connection()

    def BindingFunctions(self):
        self.LBT_CMBX_libname.currentTextChanged.connect(lambda name: (self.fillData(_type = "DB_STATS", DB_name = name)))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        print(1)
        self.LibManager.close_connection()
        return super().closeEvent(event)

if __name__ == "__main__":
    from apollo.plugins.app_theme import Theme

    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    UI = LibraryManager_App()
    Theme_obj = Theme(App=app)
    UI.LBT_PSB_active.pressed.connect(lambda: (app.setStyleSheet((Theme_obj.GenStyleSheet(Theme_obj.pallete)))))
    UI.MDE_PSB_save.pressed.connect(lambda: (app.setStyleSheet((Theme_obj.GenStyleSheet(Theme_obj.pallete)))))
    UI.show()
    app.exec()
