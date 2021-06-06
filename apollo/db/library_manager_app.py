import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt

from apollo.gui.ui_library_manager_ui import Ui_MainWindow as LibraryManager_UI

class LibraryManager_App(QtWidgets.QMainWindow, LibraryManager_UI):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
