import datetime
import hashlib
import os
import random
from typing import Callable, Union

from PySide6.QtSql import QSqlDatabase, QSqlQuery

from apollo import exe_time, dedenter, PathUtils
from apollo.plugins.audio_player import MediaFile

DBFIELDS = ("file_id", "path_id", "file_name", "file_path", "album",
            "albumartist", "artist", "author", "bpm", "compilation",
            "composer", "conductor", "date", "discnumber", "discsubtitle",
            "encodedby", "genre", "language", "length", "filesize",
            "lyricist", "media", "mood", "organization", "originaldate",
            "performer", "releasecountry", "replaygain_gain", "replaygain_peak",
            "title", "tracknumber", "version", "website", "album_gain",
            "bitrate", "bitrate_mode", "channels", "encoder_info", "encoder_settings",
            "frame_offset", "layer", "mode", "padding", "protected", "sample_rate",
            "track_gain", "track_peak", "rating", "playcount")


class DBStructureError(Exception):
    __module__ = "LibraryManager"


class QueryBuildFailed(Exception):
    __module__ = "LibraryManager"


class QueryExecutionFailed(Exception):
    __module__ = "LibraryManager"


class Connection:
    """
    class that manages all the connections to a DB and executes queries in a context manager
    """

    def __init__(self, db_name: str, commit: bool = True):
        """
        Class Constructor

        Parameters
        ----------
        db_name: str
            path/name of the db to connect to
        """
        super().__init__()
        self.DB = self.connect(db_name)
        self.autocommit = commit

    def __enter__(self):
        self.db_driver = QSqlDatabase.addDatabase("QSQLITE", str(random.random()))
        self.db_driver.setDatabaseName(self.DB)
        if self.db_driver.open() and self.db_driver.isValid() and self.db_driver.isOpen():
            return self.db_driver
        else:
            raise ConnectionError(self.DB)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if hasattr(self, "db_driver"):
            self.db_driver.commit()
            del self.db_driver
        if any([exc_type, exc_value, exc_traceback]):
            print(f"exc_type: {exc_type}\nexc_value: {exc_value}\nexc_traceback: {exc_traceback}")
        QSqlDatabase.removeDatabase(str(random.random()))

    @staticmethod
    def connect(db_name: str):  # Tested
        """
        connects to a DB
        Parameters
        ----------
        db_name: str
            path/name of the db to connect to

        Returns
        -------
        str
            DB name if that DB exists on te file system
        """
        if (db_name == ":memory:") or PathUtils.isFileExt(db_name, ".db"):
            return db_name
        else:
            raise ConnectionError()


class DataBaseManager:
    """
    Base class for all th sql related function and queries
    """
    DB_NAME: str

    def __init__(self):
        """
        Initializes the Database Driver and connects to DB and Initializes the
        fields for the Database Tables
        """
        self.db_fields = DBFIELDS

    def connect(self, db_name: str, check: bool = True):  # Tested
        """
        Uses the Database Driver to create a connection with a local
        database.If Db not avaliable will create new Db

        >>> DataBaseManager.connect("default.db")

        Parameters
        ----------
        db_name: String
            path of a Valid Database or a Database name in order to create a blank one
        check: bool
            flag to set in order to perform the structural integrity checks

        Returns
        -------
        Boolean
            returns true if connection was succesful

        Raises
        ------
        ConnectionError
            if database fails to connect or fails checks
        """
        self.DB_NAME = db_name
        if check:
            if not self.db_startup_checks():
                raise DBStructureError("Startup Checks Failed")
            else:
                return True
        # only executes when connection fails and app closes
        else:  # pragma: no cover
            return True

    def db_startup_checks(self):  # Tested
        """
        Performs validation test for Table availability and structure.
        Creates the table or the view if it doesnt exist.

        Returns
        -------
        Boolean
            Returns true if all checks are passed
        """

        # checks for existences of library table
        [[TABLE, COLUMNS]] = self.exec_query("""
            SELECT
            (
                SELECT
                IIF(name = 'library', TRUE, FALSE)
                FROM sqlite_master
                WHERE type = 'table'
            ) AS TABLE_CHECK,
            (
                SELECT
                min(
                    IIF( name IN(
                        'file_id', 'path_id','file_name','file_path','album',
                        'albumartist','artist','author','bpm','compilation',
                        'composer','conductor','date','discnumber','discsubtitle',
                        'encodedby','genre','language','length','filesize',
                        'lyricist','media','mood','organization','originaldate',
                        'performer','releasecountry','replaygain_gain','replaygain_peak',
                        'title','tracknumber','version','website','album_gain',
                        'bitrate','bitrate_mode','channels','encoder_info','encoder_settings',
                        'frame_offset','layer','mode','padding','protected','sample_rate',
                        'track_gain','track_peak', 'rating', 'playcount'), TRUE, FALSE
                    )
                )
                FROM pragma_table_info('library')
            ) AS COLUMN_CHECK;
        """)
        if not bool(TABLE) or not bool(COLUMNS):
            self.Create_LibraryTable()

        # checks for existences of nowplaying view
        [[TABLE, COLUMNS]] = self.exec_query("""
            SELECT
            (
                SELECT
                IIF(name = 'nowplaying', TRUE, FALSE)
                FROM sqlite_master
                WHERE type = 'view'
            ) AS TABLE_CHECK,
            (
                SELECT
                min(
                    IIF( name IN(
                        'file_id', 'path_id','file_name','file_path','album',
                        'albumartist','artist','author','bpm','compilation',
                        'composer','conductor','date','discnumber','discsubtitle',
                        'encodedby','genre','language','length','filesize',
                        'lyricist','media','mood','organization','originaldate',
                        'performer','releasecountry','replaygain_gain','replaygain_peak',
                        'title','tracknumber','version','website','album_gain',
                        'bitrate','bitrate_mode','channels','encoder_info','encoder_settings',
                        'frame_offset','layer','mode','padding','protected','sample_rate',
                        'track_gain','track_peak', 'rating', 'playcount'), TRUE, FALSE
                    )
                )
                FROM pragma_table_info('nowplaying')
            ) AS COLUMN_CHECK
        """)
        if not bool(TABLE) or not bool(COLUMNS):
            self.Create_EmptyView("nowplaying")

        return True

    def exec_query(self, query: str, column: Union[int, None] = None, commit: bool = True):  # Tested
        """
        Executes an QSqlQuery and returns the query to get results

        >>> DataBaseManager.exec_query(query)

        Parameters
        ----------
        query: str
            Query to execute
        column: Union[int, None]
            count of columns to get data from
        commit: bool
            auto_commit flag
        Returns
        -------
        List
            list of matrix of Row X Column, if NULL []
        """
        # creates a connection to the DB that is linked to the main class
        with Connection(self.DB_NAME, commit) as CON:
            if isinstance(query, str):
                query_str = query
                query = QSqlQuery(db = CON)
                if not query.prepare(query_str):
                    connection_info = (str(CON))
                    raise QueryBuildFailed(f"{connection_info}\n{query_str}")
            else:
                # if creating of the Query fails it raises an exception
                connection_info = (str(CON))
                raise QueryBuildFailed(f"{connection_info}")

            # executes the given query
            query_executed = query.exec()
            if not query_executed:
                connection_info = (str(CON))
                msg = f"""
                    EXE: {query_executed}
                    ERROR: {(query.lastError().text())}
                    Query: {query.lastQuery()}
                    Connection: {connection_info}
                    """
                raise QueryExecutionFailed(dedenter(msg, 12))
            else:
                return self.fetch_all(query, column)

    def fetch_all(self, query: QSqlQuery, column: Union[int, None] = None):  # Tested
        """
        Fetches data from the given query

        >>> DataBaseManager.fetch_all(query, 5)

        Parameters
        ----------
        query: QSqlQuery
            Query to fetch result set from
        column: Union[int, None], optional
            index of Column to get data for, by default None

        Returns
        -------
        List
            list of matrix of Row X Column, if NULL []
        """
        data = []
        if column is None:
            column = query.record().count()

        if column == 1:
            while query.next():
                data.append(query.value(0))
        else:
            while query.next():
                data.append([query.value(C) for C in range(column)])

        return data

    def Index_selector(self, view_name, Column):  # Tested
        """
        Gets Column Data from a Table and View

        Parameters
        ----------
        view_name : String
            Valid view name from (now_playing)
        Column : String
            Valid Column to select data from

        Returns
        -------
        list
            Column data requested for

        Raises
        ------
        Exception
            if data retruival failed
        """

        return self.exec_query(f"SELECT {Column} FROM {view_name}", 1)

    def SelectAll(self, name):
        """
        Gets All Data from a Table and View

        Parameters
        ----------
        view_name : String
            Valid view name from (now_playing)

        Returns
        -------
        list
            Table data requested for

        Raises
        ------
        Exception
            if data retruival failed
        """
        return self.exec_query(f"SELECT * FROM {name}")

    ####################################################################################################################
    # Create, Drop, Insert Functions
    ####################################################################################################################

    def Create_LibraryTable(self):  # Tested
        """
        Creates the main Library table with yhe valid column fields
        """
        return self.exec_query(f"""
        CREATE TABLE IF NOT EXISTS library(
        file_id TEXT PRIMARY KEY ON CONFLICT IGNORE,
        path_id TEXT,
        file_name TEXT,
        file_path TEXT,
        album TEXT,
        albumartist TEXT,
        artist TEXT,
        author TEXT,
        bpm TEXT,
        compilation TEXT,
        composer TEXT,
        conductor TEXT,
        date TEXT,
        discnumber INTEGER,
        discsubtitle TEXT,
        encodedby TEXT,
        genre TEXT,
        language TEXT,
        length TEXT,
        filesize TEXT,
        lyricist TEXT,
        media TEXT,
        mood TEXT,
        organization TEXT,
        originaldate TEXT,
        performer TEXT,
        releasecountry TEXT,
        replaygain_gain TEXT,
        replaygain_peak TEXT,
        title TEXT,
        tracknumber TEXT,
        version TEXT,
        website TEXT,
        album_gain TEXT,
        bitrate TEXT,
        bitrate_mode TEXT,
        channels INTEGER,
        encoder_info TEXT,
        encoder_settings TEXT,
        frame_offset TEXT,
        layer TEXT,
        mode TEXT,
        padding TEXT,
        protected TEXT,
        sample_rate TEXT,
        track_gain TEXT,
        track_peak TEXT,
        rating INTEGER,
        playcount INTEGER)
        """)

    def Create_EmptyView(self, view_name):  # Tested
        """
        Creates an empty view as an placeholder for display

        >>> library_manager.Create_EmptyView("Example")

        Parameters
        ----------
        view_name : String
            Valid view name from (now_playing)
        """
        columns = ", ".join([f"NULL AS {k}" for k in self.db_fields])
        self.exec_query(f"CREATE VIEW IF NOT EXISTS {view_name} AS SELECT {columns}")

    def CreateView(self, view_name, Selector, **kwargs):
        """
        Creates an view from library Table by selection data from a valid field

        >>> library_manager.CreateView("Viewname", "File_id", [1,2,3,4])

        Parameters
        ----------
        view_name: String
            Valid view name from (now_playing)
        Selector: List
            Valid Selector to select and filter out Rows from the table
        FilterField: String
            Valid field to select data from
        ID: List
            File_id to indexs from if provided
        Shuffled: Bool
            Query Type to use for selecting data
        """

        # Drops thgiven view to create a new view
        self.DropView(view_name)

        # creates a a query string of items needed to be selected
        FilterItems = ", ".join([f"'{value}'" for value in Selector])

        # sets the column used to look data from
        if kwargs.get("FilterField") == None:
            Field = "file_id"
        else:
            Field = kwargs.get("FilterField")

        # a list of all file ID used for indexing
        if kwargs.get("ID") != None and kwargs.get("Shuffled") == None:
            ID = ", ".join([f"'{v}'" for v in kwargs.get("ID")])
            self.exec_query(f"""
            CREATE VIEW IF NOT EXISTS {view_name} AS
            SELECT *
            FROM library
            WHERE file_id IN (
                SELECT file_id
                FROM library
                WHERE {Field} IN ({FilterItems})
                OR lower({Field}) IN ({FilterItems})
                OR file_id IN ({ID})
            )
            """)
        # indexing items and shuffling the order
        elif kwargs.get("Shuffled") != None:
            self.exec_query(f"""
            CREATE VIEW IF NOT EXISTS {view_name} AS
            SELECT *
            FROM library
            WHERE {Field} IN ({FilterItems})
            ORDER BY RANDOM()
            """)

        else:
            self.exec_query(f"""
            CREATE VIEW IF NOT EXISTS {view_name} AS
            SELECT *
            FROM library
            WHERE {Field}
            IN ({FilterItems})
            """)

    def DropTable(self, tablename):
        """
        Drops the table from the database

        Parameters
        ----------
        table_name: String
            Name of the table to be dropped
        """
        self.exec_query(f"DROP TABLE IF EXISTS {tablename}")

    def DropView(self, viewname):
        """
        Drops the view from the database

        >>> library_manager.drop_view("viewname")

        Parameters
        ----------
        viewname: String
            Name of the view to be dropped
        """
        self.exec_query(f"DROP VIEW IF EXISTS {viewname}")

    def BatchInsert_Metadata(self, metadata):
        """
        Batch Inserts data into library table

        Parameters
        ----------
        metadata: Dict
            Distonary of all the combined metadata
        """
        with Connection(self.DB_NAME) as CON:
            # sets up the transcation
            CON.transaction()
            QSqlQuery("PRAGMA journal_mode = MEMORY", db = CON).exec()

            columns = ", ".join(metadata.keys())
            placeholders = ", ".join(["?" for i in metadata.keys()])
            query = QSqlQuery(f"INSERT OR IGNORE INTO library ({columns}) VALUES ({placeholders})", db = CON)
            for keys in metadata.keys():
                query.addBindValue(metadata.get(keys))

            if not query.execBatch():  # pragma: no cover
                msg = f"""
                    ERROR: {(query.lastError().text())}
                    Query: {query.lastQuery()}
                    """
                del CON
                raise QueryExecutionFailed(dedenter(msg, 12))

            QSqlQuery("PRAGMA journal_mode = WAL", db = CON).exec()
            CON.commit()
            del CON

    ###################################################################################################################
    # Table Stats Query
    ###################################################################################################################

    def TableSize(self, tablename="library"):
        """
        Calculates the total size in Gigabytes of all the files monitered.
        Returns the Gigabyte as a Float.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(OUTPUT, OUTPUT, 0) AS FINAL
        FROM (
            SELECT round(sum(filesize)/1024, 2) AS OUTPUT
            FROM {tablename}
            )
        """)
                 )
        return query.pop().pop()

    def TablePlaycount(self, tablename="library"):
        """
        Calculates the total Playtime and returns an Int

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(OUTPUT, OUTPUT, 0) AS FINAL
        FROM (
            SELECT sum(playcount) AS OUTPUT
            FROM {tablename}
            )
        """)
                 )
        return query.pop().pop()

    def TablePlaytime(self, tablename="library"):
        """
        Calculates the total playtime of all the files monitered.
        Returns the Playtime as a String.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(TIME_SEC, TIME_SEC, 0) AS FINAL
        FROM (
            SELECT (sum(substr(length,1,1))*360 + sum(substr(length,3,2))*60 + sum(substr(length,6,2)))
            AS TIME_SEC
            FROM {tablename}
            )
        """)
                 )
        return datetime.timedelta(seconds=query.pop().pop())

    def TableAlbumcount(self, tablename="library"):
        """
        Calculates the total count of album of all the files monitered.
        Returns the album count as a Int.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(OUTPUT, OUTPUT, 0) AS FINAL
        FROM (
            SELECT count(DISTINCT album) AS OUTPUT
            FROM {tablename}
            )
        """)
                 )
        return query.pop().pop()

    def TableArtistcount(self, tablename="library"):
        """
        Calculates the total count of albumartist of all the files monitered.
        Returns the albumartist count as a Int.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(OUTPUT, OUTPUT, 0) AS FINAL
        FROM (
            SELECT count(DISTINCT artist) AS OUTPUT
            FROM {tablename}
            )
        """)
                 )
        return query.pop().pop()

    def TableTrackcount(self, tablename="library"):
        """
        Calculates the total count of Tracks of all the files monitered.
        Returns the track count as a Int.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT IIF(OUTPUT, OUTPUT, 0) AS FINAL
        FROM (
            SELECT count(DISTINCT file_id) AS OUTPUT
            FROM {tablename}
            )
        """)
                 )
        return query.pop().pop()

    def TopAlbum(self, Tablename="library"):
        """
        Calculates the total playcount of Album of all the files monitered.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT album
        FROM {Tablename}
        WHERE album NOTNULL AND album NOT IN ('', ' ')
        GROUP BY album
        ORDER BY COUNT(playcount) DESC
        LIMIT 1;
        """)
                 )
        if query != []:
            return query.pop().pop()
        else:
            return ""

    def Topgenre(self, Tablename="library"):
        """
        Calculates the total playcount of genre of all the files monitered.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT genre
        FROM {Tablename}
        WHERE genre NOTNULL AND genre NOT IN ('', ' ')
        GROUP BY genre
        ORDER BY COUNT(playcount) DESC
        LIMIT 1;
        """)
                 )
        if query != []:
            return query.pop().pop()
        else:
            return ""

    def Topartist(self, Tablename="library"):
        """
        Calculates the total playcount of artist of all the files monitered.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT artist
        FROM {Tablename}
        WHERE artist NOTNULL AND artist NOT IN ('', ' ')
        GROUP BY artist
        ORDER BY COUNT(playcount) DESC
        LIMIT 1;
        """)
                 )
        if query != []:
            return query.pop().pop()
        else:
            return ""

    def Toptrack(self, Tablename="library"):
        """
        Calculates the total playcount of track of all the files monitered.

        Parameters
        ----------
        tablename: String
            Name of the table or view to be queried
        """
        query = (self.exec_query(f"""
        SELECT title
        FROM {Tablename}
        WHERE playcount == (
            SELECT max(playcount)
            FROM {Tablename}
        )
        LIMIT 1
        """)
                 )
        if query != []:
            return query.pop().pop()
        else:
            return ""


class FileManager(DataBaseManager):  # pragma: no cover
    """
    File manager classes manages:
    -> Scanning Directories
    -> Fetching metadata for the related file format

    Read Supported Formats:
    -> mp3
    -> flac
    -> m4a
    """

    def __init__(self):
        """
        Class Constructor
        """
        self.db_fields = DBFIELDS

    def TransposeMeatadata(self, Metadata: list):
        """
        Transposes the List given to it

        Parameters
        ----------
        Metadata : list
            List of all the Files Metadata

        Returns
        -------
        Dict
            A dict of values corresponding to the columns
        """
        T_metadata = dict.fromkeys(DBFIELDS, [])
        for index, key in enumerate(T_metadata.keys()):
            T_metadata[key] = [value[index] for value in Metadata]
        return T_metadata

    @exe_time
    def ScanDirectory(self, Dir: str, include: list = [], Slot: Callable = lambda x: ''):
        """
        Scans all the files in a directory and inserts them to the DB

        Parameters
        ----------
        Dir : str
            dir to scan
        include : list, optional
            File Extensions to look for, by default []
        Slot : Callable, optional
            Additional Callback with (arg: str) prameter, by default lambda:''
        """
        BatchMetadata = []
        Existing_Paths = []
        FileHashList = []

        Slot(f"Scanning {Dir}")
        if [[0]] != self.exec_query("SELECT COUNT(path_id) FROM library"):
            Existing_Paths = self.exec_query(f"SELECT path_id FROM library")
            FileHashList = self.exec_query(f"SELECT file_id FROM library")

        for D, SD, F in os.walk(os.path.normpath(Dir)):
            for file in F:
                # checks for file ext
                if (os.path.splitext(file)[1]).upper().replace(".", "") in include:
                    file = PathUtils.PathJoin(D, file)

                    # Generates Hashes
                    path_hash = (hashlib.md5(file.encode())).hexdigest()
                    Filehash = self.FileHasher(file)

                    # checks and add teh files to metadata dict
                    if ([path_hash] not in Existing_Paths) and ([Filehash] not in FileHashList):
                        FileHashList.append(Filehash)
                        Metadata = MediaFile(file).getMetadata()
                        Metadata["path_id"] = path_hash
                        Metadata["file_id"] = Filehash
                        BatchMetadata.append(list(Metadata.values()))
                    else:
                        Slot(f"SKIPPED: {file}")
                else:
                    Slot(f"SKIPPED: {file}")

        self.BatchInsert_Metadata(self.TransposeMeatadata(BatchMetadata))
        Slot(f"Completed Scanning {Dir}")

    def FileHasher(self, file: str, hashfun: Callable = hashlib.md5):
        """
        Creates a hash id for the file path passed and returns hash id.
        Hash id is calculated with the 1024 bytes of the file.

        Parameters
        ----------
        file : str
            File for which the hash is generated
        hashfun : Callable, optional
            Hashing algorithm method from hashlib, by default hashlib.md5

        Returns
        -------
        str
            hashval that is generated
        """
        with open(file, "rb") as fobj:
            return (hashfun(fobj.read(1024))).hexdigest()


class LibraryManager(FileManager):
    """
    Controls the database queries for table and view (creation, modification
    and deletion).

    >>> library_manager = LibraryManager()
    >>> library_manager.connect("database.db")
    """

    def __init__(self, db_name = None):
        """Constructor"""
        self.db_fields = DBFIELDS
        super().__init__()

        if not (db_name is None):
            if not self.connect(db_name):  # pragma: coverage
                raise DBStructureError("Startup Checks Failed")


if __name__ == "__main__":
    inst = LibraryManager(r"D:\dev\Apollo-dev\apollo\db\default.db")
    inst.ScanDirectory(r"D:\music", ["MP3", "FLAC"])
