import os
import pathvalidate
import shutil
import json
import time
import threading

from apollo import PARENT_DIR


def exe_time(method):
    def timed(*args, **kw):
        """
        Calculates the method execution time. exe_time is used as an Method decorator

        Returns
        -------
        callback
            wrapped callback
        """
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r %2.4f s' % (method.__name__, (te - ts)))
        return result
    return timed

def tryit(method):
    def exe(*args, **kwargs):
        """
        Wraps the method execution in exception block, is used as an Method decorator

        Returns
        -------
        callback
            wrapped callback
        """
        try:
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            if 'log_time' in kwargs:
                name = kwargs.get('log_name', method.__name__.upper())
                kwargs['log_time'][name] = int((te - ts) * 1000)
            else:
                print ('%r %2.4f s' % (method.__name__, (te - ts)))
            return result
        except Exception as e:
                print (f"{method.__name__}: {e}")
    return exe

def ThreadIt(method):
    def Exe(*args, **kw):
        """
        Thread executes any given function, is used as an Method decorator

        Returns
        -------
        callback
            wrapped callback
        """
        Thread = threading.Thread(target = method, args = args, kwargs = kw, name = method.__name__)
        Thread.start()
    return Exe

def dedenter(string = '', indent_size = 4):
    """
    Dedents the string according to the given indent

    Parameters
    ----------
    string : str, optional
        String to dedent, by default ''
    indent_size : int, optional
        indent size to reduce, by default 4

    Returns
    -------
    str
        output string that is dedented
    """
    string = string.expandtabs().splitlines()
    string = ("\n".join([line[(indent_size):] for line in string]))
    return (string.strip("\n"))


class PlayingQueue:
    """
    PlayingQueue is used as a track queue to manage track Playback.
    Base datatype used as the queue is an List and related operations of lists.
    """
    # management of index scaling when indexes are modified
    def __init__(self, circ = False):
        self.PlayingQueue = []
        self.CurrentIndex = 0
        self.IsCircular = circ
        self.index_pos = []

    def __len__(self):
        return len(self.PlayingQueue)

    def __repr__(self):
        return str(self.PlayingQueue)

    def AddElements(self, element: list, Index = None):
        """
        Adds Elements to the playing Queue according to the index

        Parameters
        ----------
        element : list
            A list of a single or multiple elements to add
        Index : int, optional
            Index to add elements to, by default None
        """
        #element insertion to an empty queue
        if Index == None:
            self.PlayingQueue.extend(element)

        # element insertion at an index
        else:
            if Index > len(self.PlayingQueue):
                self.PlayingQueue.extend(element)
            else:
                for offset, item in enumerate(element):
                    self.PlayingQueue.insert((Index + offset), item)
                # index scaling when elements are added
                if self.CurrentIndex >= Index:
                    self.CurrentIndex += len(element)


    def AddNext(self, element):
        """
        Adds Elements to the playing Queue after currest position

        Parameters
        ----------
        element : List
            A list of a single or multiple elements to add
        """
        self.AddElements(element, Index = self.GetPointer() + 1)


    def RemoveElements(self, Index = None, Start = None, End = None):
        """
        Removes a single element Or Elements between an Range Of indexes

        Parameters
        ----------
        Index : Int, optional
            index of the element to pop, by default None
        Start : Int, optional
            Start position of the slice, by default None
        End : Int, optional
            End Position of the slice, by default None
        """
        # removing single element from an index
        if Index != None and (Start == None or End == None):
            self.PlayingQueue.pop(Index)
            if  self.CurrentIndex > Index:
                self.CurrentIndex -= 1
            elif self.CurrentIndex == Index:
                self.JumpPos(0)
            else:
                pass

        # slice removal
        if Start != None and End != None:
            if End >= len(self.PlayingQueue):
                del self.PlayingQueue[Start:]
                if Start <= self.CurrentIndex:
                    self.JumpPos(0)
            else:
                del self.PlayingQueue[Start: End]
                if Start == self.CurrentIndex or self.CurrentIndex == End:
                    self.JumpPos(0)
                elif Start < self.CurrentIndex < End:
                    self.JumpPos(0)
                elif End < self.CurrentIndex:
                    offset = (End - Start)
                    self.CurrentIndex -= offset

        # Only start Args given
        if Start != None and End == None:
            del self.PlayingQueue[Start:]
            if Start <= self.CurrentIndex:
                self.JumpPos(0)

        # Complete dump of queue
        if Index == None and Start == None and End == None:
            self.PlayingQueue = []
            self.CurrentIndex = 0

        # index scaling when elements are removed


    def IncrementPointer(self, by = 1):
        """
        Increments the index with an given offset

        Parameters
        ----------
        by : int, optional
            offset to incerment index, by default 1

        Returns
        -------
        int
            current index

        Raises
        ------
        IndexError
        """
        if (self.CurrentIndex + by) < len(self.PlayingQueue):
            self.CurrentIndex += by
        else:
            # Circular Indexing of queue
            if self.IsCircular:
                self.CurrentIndex = 0
            # Normal Indexing of queue
            else:
                self.CurrentIndex = 0
                raise IndexError()
        return self.CurrentIndex



    def DecrementPointer(self, by = 1):
        """
        Decrements the index with an given offset

        Parameters
        ----------
        by : int, optional
            offset to Decerment index, by default 1

        Returns
        -------
        int
            current index

        Raises
        ------
        IndexError
        """

        if (self.CurrentIndex - by) >= 0:
            self.CurrentIndex -= by
        else:
            # Circular Indexing of queue
            if self.IsCircular:
                self.CurrentIndex = len(self.PlayingQueue) - 1
            # Normal Indexing of queue
            else:
                self.CurrentIndex = 0
                raise IndexError()

        return self.CurrentIndex


    def JumpPos(self, Pos):
        """
        Random access of queue

        Parameters
        ----------
        Pos : Int
            index to jump to
        """
        if Pos in range(len(self.PlayingQueue)):
            self.CurrentIndex = Pos


    def SetCircular(self, bool_):
        """
        Enables and disables endpoint Circling of a list

        Parameters
        ----------
        bool_ : bool
            sets if the queue wraps around itself
        """
        self.IsCircular = bool_


    def GetPointer(self):
        """
        gets the current index where the pointer is at

        Returns
        -------
        int
            current index of the pointer
        """
        return self.CurrentIndex


    def GetCurrent(self):
        """
        Gets the current value at index

        Returns
        -------
        any
            item at given index
        """
        if self.CurrentIndex != None:
            return self.PlayingQueue[self.CurrentIndex]


    def GetNext(self):
        """
        gets the next value

        Returns
        -------
        int
            gets the next index
        """
        self.IncrementPointer()
        return self.GetCurrent()


    def GetPrevious(self):
        """
        gets the previous index

        Returns
        -------
        index
            gets the previous
        """
        self.DecrementPointer()
        return self.GetCurrent()


    def GetQueue(self):
        """
        Returns the complete queue

        Returns
        -------
        list
            gets the complete queue
        """
        return self.PlayingQueue


class PathUtils:
    """
    Path related Utility functions
    """
    def __init__(self): ...

    @staticmethod
    def PurgeDirectory(path):
        """
        Purges directory tree

        Parameters
        ----------
        path : String
            string of directory or file path
        """
        shutil.rmtree(path)

    @staticmethod
    def PurgeFile(path):
        """
        Purges a single file

        Parameters
        ----------
        path : String
            string of directory or file path
        """
        os.remove(path)

    @staticmethod
    def WinPathValidator(path):
        """
        Path validator function that checks for OS appropiate paths

        Parameters
        ----------
        path : String
            string of directory or file path

        Returns
        -------
        Boolean
            returns if a path is valid or not
        """
        return pathvalidate.is_valid_filepath(path)

    @staticmethod
    def WinFileValidator(file):
        """
        file name validator function that checks for OS appropiate paths

        Parameters
        ----------
        path : String
            string of directory or file path

        Returns
        -------
        Boolean
            returns if a file name is valid or not
        """
        return pathvalidate.is_valid_filepath(file)

    @staticmethod
    def PathJoin(*args):
        """
        Path Join function

        Parameters
        ----------
        path : List(string, string)
            string of directory or file path

        Returns
        -------
        String
            a normalized path according to OS
        """
        return os.path.normpath(os.path.join(*args))

    @staticmethod
    def isFileExt(file, ext):
        return (os.path.splitext(file)[1] == ext)


class ConfigManager:
    """
    Manages the Configuration Parameters of Apollo

    >>> inst = ConfigManager()
    >>> inst.Getvariable("ROOT/SUB/SUB1")
    >>> inst.Setvariable(["VALUE"], "ROOT/SUB/SUB1")
    """
    def __init__(self, config_dict = None):
        self.config_dict = config_dict

    @staticmethod
    def default_settings():
        """
        Initializes the default launch config

        Returns
        -------
        dict
            returns the default config
        """
        config = {
            "APPTHEMES": {},
            "LIBRARY_GROUPORDER": "file_path",
            "ACTIVETHEME": "GRAY_100",
            "CURRENT_DB": "Default",
            "MONITERED_DB": {
                "Default": {
                    "name": "Default",
                    "db_loc": os.path.join(PARENT_DIR, 'db', 'default.db'),
                    "file_mon": [],
                    "filters": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                }
            }
        }
        return config

    def LoadConfig(self, file):
        """
        Opens the config file and loads the settings JSON

        Parameters
        ----------
        file : String, optional
            Config File path, by default None

        Returns
        -------
        dict
            reads a JSON and returns the config
        """
        self.file = file
        self.config_dict = {}
        if not os.path.isfile(file):
            with open(file, "w") as FP:
                json.dump(self.default_settings(), FP, indent = 4)
                self.config_dict = self.default_settings()
        else:
            try:
                with open(file) as FP:
                    self.config_dict = json.load(FP)
            except json.JSONDecodeError as e:
                print(e)
                with open(file, "w") as FP:
                    json.dump({}, FP, indent = 4)
        return self

    def DumpConfig(self):
        """
        Writes Data to the Config File

        Parameters
        ----------
        file : str, optional
            File Name To write Into, by default None

        Returns
        -------
        Boolean
            returns if the write was succesful
        """
        if self.file == None:
            return False
        with open(self.file, "w") as FP:
            json.dump(self.config_dict, FP, indent = 4)
            return True

    def Getvalue(self, path = "", config = None):
        """
        Recursively Traverses the path and gets the value

        Parameters
        ----------
        path : str, list, optional
            Path used to traverse the dict, by default ""
        config : dict, optional
            dict to traverse, by default None

        Returns
        -------
        any
            returns value stored at a given path in the config
        """
        if config == None:
            config = self.config_dict

        if isinstance(path, str):
            if path.find(r"//") != -1: raise IndexError(path)
            path = path.split("/")

        if len(path) >= 1 and not("" in path):
            index = path.pop(0)
            data = config.get(index, False)

            if isinstance(data, dict):
                return self.Getvalue(path, data)
            else:
                return data
        else:
            return config

    def Setvalue(self, value, path = '', config = None):
        """
        Recursively Traverses the path and Sets the value
        >>> self.Config_manager.Setvalue(["VALUE"], "ROOT/SUB/SUB1")

        Parameters
        ----------
        value : Any
            Value to replace or set
        path : str, optional
            dict to traverse, by default ''
        config : Dict, optional
            Path used to traverse the dict, by default None

        Returns
        -------
        Boolean
            returns if operation was succesful
        """
        if config == None:
            config = self.config_dict

        if isinstance(path, str):
            if path.find(r"//") != -1: raise IndexError(path)
            path = path.split("/")

        if len(path) >= 1 and not("" in path):
            index = path.pop(0)
            if index in config.keys():
                data = config.get(index, False)

                if isinstance(data, dict):
                    if len(path) == 0:
                        config[index] = value
                    else:
                        return self.Setvalue(value, path, data)

                if isinstance(data, str):
                    config[index] = value

                if isinstance(data, list) and isinstance(value, list):
                    config[index].extend(value)
                elif isinstance(data, list) and not isinstance(value, list):
                    config[index].append(value)
                else:
                    config[index] = value
            else:
                config[index] = value
        else:
            return None

    def DropKey(self, path = '', config = None):
        if config == None:
            config = self.config_dict

        if isinstance(path, str):
            path = path.split("/")

        if len(path) >= 1 and not("" in path):
            index = path.pop(0)
            if index in config.keys() and len(path) == 0:
                del config[index]
                return None
            else:
                data = config.get(index, False)
                return self.DropKey(path, data)


class AppConfig(dict):

    def __init__(self, Config = "DEFAULT"):
        """
        Manages all the app config loading and writing config manager that manages the config.cfg file
        """
        self.Manager = ConfigManager()
        if Config == "DEFAULT":
            self.Manager.file = (os.path.join(PARENT_DIR,"config.cfg"))
            self.Manager.LoadConfig(os.path.join(PARENT_DIR,"config.cfg"))
        if isinstance(Config, dict):
            self.Manager.config_dict = Config
            self.Manager.file = None
        if isinstance(Config, str) and Config != "DEFAULT":
            self.Manager.LoadConfig(Config)

    def __repr__(self):
        return json.dumps(self.Manager.config_dict, indent = 2)

    def __str__(self):
        return json.dumps(self.Manager.config_dict, indent = 2)

    def __getitem__(self, key):
        """
        Gets the item at index

        Parameters
        ----------
        key : any
            key to look for
        """
        if key == "current_db_path":
            return self.current_db_path
        else:
            return self.Manager.Getvalue(key)

    def __delitem__(self, v) -> None:
        self.Manager.DropKey(v)
        self.Manager.DumpConfig()

    def __setitem__(self, key, value):
        """
        Gets the item at index

        Parameters
        ----------
        key : any
            key to look for
        """
        if key == "current_db_path":
            self.current_db_path = value
        else:
            self.Manager.Setvalue(value, key)
        self.Manager.DumpConfig()

    # current_db_path #########################################################
    @property
    def current_db_path(self):
        name = self.Manager.Getvalue("CURRENT_DB")
        return self.Manager.Getvalue(f"MONITERED_DB/{name}/db_loc")

    @current_db_path.setter
    def current_db_path(self, value):
        name = self.Manager.Getvalue("CURRENT_DB")
        self.Manager.Setvalue([value], f"MONITERED_DB/{name}/db_loc")
