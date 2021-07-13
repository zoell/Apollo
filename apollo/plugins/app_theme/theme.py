import sys, re, importlib, subprocess, json, os
from posixpath import ismount
from typing import Any

from PySide6 import QtWidgets, QtGui, QtCore

from apollo import PARENT_DIR
from apollo.utils import PathUtils as PU
from apollo.utils import AppConfig

class ThemeLoadFailed(Exception): __module__ = "Theme"


class Theme:
    """
    Theme class for application
    """
    ROOTPATH = PU.PathJoin(PARENT_DIR, "plugins", "app_theme", "theme_packs")
    STYLESHEET = ""
    THEME = ""

    def __init__(self, App: QtWidgets.QWidget = None, Name: str = ""):
        """
        Class Constructor
        """
        self.ThemeConfig = AppConfig()

        if not os.path.isdir(Theme.ROOTPATH): # pragma: no cover
            os.mkdir(Theme.ROOTPATH)
            if not os.path.isfile(PU.PathJoin(Theme.ROOTPATH, "__init__.py")):
                # Creates an Import
                with open(PU.PathJoin(Theme.ROOTPATH, "__init__.py"), "w") as FH:
                    FH.write("from . import *")
            if not os.path.isdir(PU.PathJoin(Theme.ROOTPATH, "GRAY_100")):
                self.CreateThemePack(Theme.ROOTPATH, "GRAY_100", self.DefaultPallete())

        if Name == "":
            self.LoadTheme(self.ThemeConfig["ACTIVETHEME"], App)
        else:
            self.LoadTheme(Name, App)

    def get(self, key: Any):
        """
        returns a given colour form the pallete

        Parameters
        ----------
        key : Any
            colour name

        Returns
        -------
        str
            colour value
        """
        return Theme.THEME.get(key)

    def LoadTheme(self, name: str = "", app: QtWidgets.QApplication = None): # pragma: no cover
        """
        Loads the theme for the given Application

        Parameters
        ----------
        app : QApplication
            Application to load theme for
        name : str, optional
            Name of the theme, by default ""
        """
        if name == "":
            name = self.ThemeConfig["ACTIVETHEME"]

        if name in os.listdir(Theme.ROOTPATH):
            Theme.STYLESHEET = self.GetStyleSheet(name)
            Theme.THEME = self.GetPallete(name)
            self.LoadAppIcons(name)
            if app:
                app.setStyleSheet(Theme.STYLESHEET)

    def GetStyleSheet(self, Name: str = ""):
        """
        Get the style sheet for the theme

        Parameters
        ----------
        Name : str, optional
            theme name, by default ""

        Returns
        -------
        str
            Stylesheet fot the given theme

        Raises
        ------
        ThemeLoadFailed
            raised if the stylesheet doesnt exist
        """
        if os.path.isfile(PU.PathJoin(Theme.ROOTPATH, Name, "stylesheet.css")):
            with open(PU.PathJoin(Theme.ROOTPATH, Name, "stylesheet.css")) as FH:
                Stylesheet = FH.read()
            return Stylesheet
        else:
            raise ThemeLoadFailed("Stylesheet Not avaliable")

    def GetPallete(self, Name: str = ""):
        """
        Get the style sheet for the theme

        Parameters
        ----------
        Name : str, optional
            theme name, by default ""

        Returns
        -------
        dict
            pallete for the loaded theme

        Raises
        ------
        ThemeLoadFailed
            raised if the json pallete doest exist
        """
        if os.path.isfile(PU.PathJoin(Theme.ROOTPATH, Name, "theme.json")):
            with open(PU.PathJoin(Theme.ROOTPATH, Name, "theme.json")) as FH:
                Pallete = json.load(FH)
            return Pallete
        else:
            raise ThemeLoadFailed("Pallete Not avaliable")

    def LoadAppIcons(self, Name: str = "", PKG: str = None):
        """
        Loads the style sheet for the theme

        Parameters
        ----------
        Name : str, optional
            theme name, by default ""
        PKG : str, optional
            Package name, by default None

        Raises
        ------
        ThemeLoadFailed
            is raised when the theme icon pack doesnt exist
        """
        if os.path.isfile(PU.PathJoin(Theme.ROOTPATH, Name, "app_icons.py")):
            if PKG != None:
                importlib.import_module(f".{Name}", PKG)
            else:
                importlib.import_module(f".{Name}", "apollo.plugins.app_theme.theme_packs")
        else:
            raise ThemeLoadFailed("Resource Not avaliable")

    def CreateThemePack(self, Dest: str, Name: str, pallete: dict): #tested
        """
        Creates a theme pack using the given theme pallete

        Parameters
        ----------
        Dest : str
            Dest Directory
        Name : str
            Name of the theme Pallete
        pallete : dict
            Pallete of colors
        """
        # Creates a theme pack directory
        if PU.WinFileValidator(Name) and not os.path.isdir(PU.PathJoin(Dest, Name)):
            ThemePath = (PU.PathJoin(Dest, Name))
            if os.makedirs(ThemePath):
                self.ThemeConfig[Name] = ThemePath
        else: return None

        # Creates an app theme json
        if not os.path.isfile(PU.PathJoin(ThemePath, "theme.json")):
            with open(PU.PathJoin(ThemePath, "theme.json"), "w") as FH:
                json.dump(pallete, FH)
        else: return None

        # Creates an app Stylesheet
        if not os.path.isfile(PU.PathJoin(ThemePath, "stylesheet.css")):
            with open(PU.PathJoin(ThemePath, "stylesheet.css"), "w") as FH:
                Stylesheet = self.GenStyleSheet(pallete)
                FH.write(Stylesheet)
        else: return None

        # Creates an Import
        if not os.path.isfile(PU.PathJoin(ThemePath, "__init__.py")):
            with open(PU.PathJoin(ThemePath, "__init__.py"), "w") as FH:
                FH.write("from . import app_icons")
        else: return None

        # Creates an app icons
        if not os.path.isfile(PU.PathJoin(ThemePath, "app_icons.qrc")):
            with open(PU.PathJoin(ThemePath, "app_icons.qrc"), "w") as FH:
                resource = self.GenAppIcons(pallete, ThemePath)
                FH.write(resource)
            # processes resource file for icons
            IN = PU.PathJoin(ThemePath, "app_icons.qrc")
            OUT = PU.PathJoin(ThemePath, "app_icons.py")
            if self.CompileResource(IN, OUT):
                # cleanup
                PU.PurgeDirectory(PU.PathJoin(ThemePath, "png"))
                PU.PurgeFile(IN)
        else: return None

        self.ThemeConfig[f"APPTHEMES/{Name}"] = ThemePath

    def GenStyleSheet(self, pallete: dict, stylesheet: str = None): # Tested
        """
        Generates stylesheet using a UI colour pallete

        Parameters
        ----------
        pallete : dict
            Dict of the color pallete
        stylesheet : str, optional
            stylesheet to use, by default None

        Returns
        -------
        String
            stylesheet Generated
        """
        if stylesheet == None:
            with open(PU.PathJoin(os.path.split(Theme.ROOTPATH)[0], "mainwindow_apollo.css")) as style:
                stylesheet = style.read()
        for element, value in pallete.items():
            stylesheet = re.sub(f"[($)]{element}(?!-)", value, stylesheet)
        return stylesheet

    def GenAppIcons(self, pallete: dict, Dest: str): # Tested
        """
        Generates the theme icons for the app using SVG

        Parameters
        ----------
        pallete : dict
            Theme dict
        Dest : str
            Destination Path

        Returns
        -------
        String
            Returns the app.qrc resource file
        """
        # create the root directory named as "png"
        if not os.path.isdir(PU.PathJoin(Dest, "png")):
            # Dest is <BaseDir//png>
            os.mkdir(PU.PathJoin(Dest, "png"))
            Dest = PU.PathJoin(Dest, "png")

            # creates extra sub dirs for each image size
            for size in [16, 24, 32, 48, 64]:
                if not os.path.isdir(PU.PathJoin(Dest, f"{size}")):
                    os.mkdir(PU.PathJoin(Dest, f"{size}"))

        self.GenPNG(pallete, Dest)

        ImgPath = []
        for Dir, SDir, files in os.walk(Dest):
            ImgPath.extend([PU.PathJoin(Dir, file) for file in files])

        return self.GenIconResource(ImgPath)

    def GenPNG(self, pallete:dict , Dest: str): # Tested
        """
        Generate an PNG using te SVG

        Parameters
        ----------
        pallete : dict
            Pallet of colors
        Dest : str
            Dest directory for all image
        """
        # works for only for SVG files present in root directory
        SVGS = os.listdir(PU.PathJoin(os.path.split(Theme.ROOTPATH)[0], "svg"))

        # Scans all the SVG file to generate theme images
        for Image in SVGS:
            # SVG image Abs Path
            Image = PU.PathJoin(PU.PathJoin(os.path.split(Theme.ROOTPATH)[0], "svg"), Image)
            for ThemeName in ["icon-01", "icon-02", "icon-03", "inverse-01", "disabled-02", "disabled-03"]:
                Colour = QtGui.QColor(pallete.get(ThemeName))
                for size in [16, 24, 32, 48, 64]:
                   self.ImageOverlay(Image, ThemeName, PU.PathJoin(Dest, f"{size}"), Colour, size)

    def ImageOverlay(self, Image: str, Theme: str, Dest: str, Color: QtGui.QColor, size: int = 64): # tested
        """
        Overlays and creates a PNG from an SVG

        Parameters
        ----------
        Image : String
            SVG image path
        Theme : String
            Theme name
        Dest : String
            Destination path
        Color : QtGui.QColor
            theme colour
        size : int, optional
            image size, by default 64

        Returns
        -------
        String
            Image Path
        """
        Icon = QtGui.QIcon(Image).pixmap(QtCore.QSize(size, size))
        Painter = QtGui.QPainter(Icon)
        Painter.setBrush(Color)
        Painter.setPen(Color)
        Painter.setCompositionMode(Painter.CompositionMode_SourceIn)
        Painter.drawRect(Icon.rect())
        Painter.end()
        if not Icon.isNull():
            name = os.path.splitext(os.path.split(Image)[1])[0]
            path = PU.PathJoin(Dest, f"{name}_{Theme}.png")
            Icon.save(path)
        return path

    def GenIconResource(self, Files: list): # Tested
        """
        Generates a resource file for all icons

        Parameters
        ----------
        Files: List[String]
            paths of all file to ad to resource file

        Returns
        -------
        String:
            resource info
        """
        HEADER = """<RCC>\n    <qresource prefix="icon_pack">"""
        Prep = lambda x: "\\".join(x.rsplit("\\", 2)[-2:])
        BODY = "\n".join([f"{' '*8}<file>png\\{Prep(File)}</file>" for File in Files])
        FOOTER = f"""    </qresource>\n</RCC>"""
        String = "\n".join([HEADER, BODY, FOOTER])
        return String

    def CompileResource(self, IN: str, OUT: str): # Tested
        """
        Resource Compiler, Compiles all the images to a single file to immport on runtime

        Parameters
        ----------
        IN : Str
           IN file Path
        OUT : Str
           OUT file Path

        Returns
        -------
        Boolean
            if compiler ran successful

        """
        from PySide6 import __path__ as PYS_path

        exe = [PU.PathJoin(PYS_path[0], "rcc.exe"), '-g', 'python', "-o", OUT, IN]
        with subprocess.Popen(exe, stderr=subprocess.PIPE) as proc:
            out, err = proc.communicate()
            if err: # pragma: no cover
                msg = err.decode("utf-8")
                command = ' '.join(exe)
                print(f"Error: {msg}\nwhile executing '{command}'")
                return False
        return True

    @staticmethod
    def SetSheet(widget: QtWidgets.QWidget, sheet: str = ""):
        """
        Sets the Loaded Stylesheet for the Widget

        Parameters
        ----------
        widget : QtWidgets.QWidget
            QWidget to add stylesheet to
        sheet : str, optional
            Stylesheet, by default ""
        """
        if sheet == "":
            sheet = Theme.STYLESHEET
        widget.setStyleSheet(sheet)

    @staticmethod
    def getThemeNames():
        """
        Gets all the theme file present in the directory

        Returns
        -------
        dict
            dict of all the themes
        """
        themes = {}
        for F in os.listdir(PU.PathJoin(PARENT_DIR, "plugins", "app_theme", "theme_packs")):
            if F not in ['__init__.py', '__pycache__']:
                themes[F] = (PU.PathJoin(PARENT_DIR, "plugins", "app_theme", "theme_packs", F))

        return themes

    @classmethod
    def DefaultPallete(cls):
        """
        Default colour pallete for apollo

        Returns
        -------
        Dict
            Color Pallete
        """
        JSON = {"ui-background" : "#161616",
                "interactive-01" : "#0f62fe",
                "interactive-02" : "#6f6f6f",
                "interactive-03" : "#ffffff",
                "interactive-04" : "#4589ff",
                "danger" : "#da1e28",
                "ui-01" : "#262626",
                "ui-02" : "#393939",
                "ui-02-alt" : "#525252",
                "ui-03" : "#393939",
                "ui-04" : "#6f6f6f",
                "ui-05" : "#f4f4f4",
                "button-separator" : "#161616",
                "decorative-01" : "#525252",
                "text-01" : "#f4f4f4",
                "text-02" : "#c6c6c6",
                "text-03" : "#6f6f6f",
                "text-04" : "#ffffff",
                "text-05" : "#8d8d8d",
                "text-error" : "#ff8389",
                "link-01" : "#78a9ff",
                "inverse-link" : "#0f62fe",
                "icon-01" : "#f4f4f4",
                "icon-02" : "#c6c6c6",
                "icon-03" : "#ffffff",
                "field-01" : "#262626",
                "field-02" : "#393939",
                "inverse-01" : "#161616",
                "inverse-02" : "#f4f4f4",
                "support-01" : "#fa4d56",
                "support-02" : "#42be65",
                "support-03" : "#f1c21b",
                "support-04" : "#4589ff",
                "inverse-support-01" : "#da1e28",
                "inverse-support-02" : "#24a148",
                "inverse-support-03" : "#f1c21b",
                "inverse-support-04" : "#0043ce",
                "focus" : "#ffffff",
                "inverse-focus-ui" : "#0f62fe",
                "hover-primary" : "#0353e9",
                "hover-primary-text" : "#a6c8ff",
                "hover-secondary" : "#606060",
                "hover-tertiary" : "#f4f4f4",
                "hover-ui" : "#353535",
                "hover-ui-light" : "#525252",
                "hover-selected-ui" : "#4c4c4c",
                "hover-danger" : "#ba1b23",
                "hover-row" : "#353535",
                "inverse-hover-ui" : "#e5e5e5",
                "active-primary" : "#002d9c",
                "active-secondary" : "#393939",
                "active-tertiary" : "#c6c6c6",
                "active-ui" : "#525252",
                "active-danger" : "#750e13",
                "selected-ui" : "#393939",
                "highlight" : "#001d6c",
                "skeleton-01" : "#353535",
                "skeleton-02" : "#393939",
                "visited-link" : "#be95ff",
                "disabled-01" : "#262626",
                "disabled-02" : "#525252",
                "disabled-03" : "#6f6f6f"
            }
        return JSON


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    inst = Theme()
    inst.GenAppIcons(Theme.DefaultPallete(), r"D:\dev\Apollo-dev\apollo\plugins\app_theme\theme_packs\new")
    app.exec()
