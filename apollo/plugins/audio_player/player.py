import time, os, threading, datetime
from pprint import pprint

import pyo, av

from apollo import PlayingQueue


class AudioInterface:
    """
    Main Interface to access all audio related functions.
    """
    def __init__(self):
        """
        Class Constructor
        """

    def ServerBootUp(self):
        """
        Starts the Audio Processor server
        """
        self.MainServer = pyo.Server().boot()
        return self

    def Gui(self):
        """
        Starts the GUI for Audio Processor server
        """
        self.MainServer.gui(locals())

    @property
    def ServerInfo(self):
        """
        Gets server and device info
        """
        info = {}
        info["pa_count_devices"] = pyo.pa_count_devices()
        info["pa_get_default_input"] = pyo.pa_get_default_input()
        info["pa_get_default_output"] = pyo.pa_get_default_output()
        info["pm_get_input_devices"] = pyo.pm_get_input_devices()
        info["pa_count_host_apis"] = pyo.pa_count_host_apis()
        info["pa_get_default_host_api"] = pyo.pa_get_default_host_api()
        info["pm_count_devices"] = pyo.pm_count_devices()
        info["pa_get_input_devices"] = pyo.pa_get_input_devices()
        info["pm_get_default_input"] = pyo.pm_get_default_input()
        info["pm_get_output_devices"] = pyo.pm_get_output_devices()
        info["pm_get_default_output"] = pyo.pm_get_default_output()
        info["pa_get_devices_infos"] = pyo.pa_get_devices_infos()
        info["pa_get_version"] = pyo.pa_get_version()
        info["pa_get_version_text"] = pyo.pa_get_version_text()
        return info

class PlayBack_Interface(AudioInterface):

    def __init__(self, PlayingQueue: PlayingQueue):
        super().__init__()
        self.PlayingQueue = PlayingQueue

        self.AudioDecoder = None
        self.CurrentFile = None
        self.AudioTable = None

    def play(self, file = None):

        if file is not None and os.path.isfile(file):
            self.CurrentFile = file
            self.AudioTable = self.AudioDecoder.GetTable()
            self.reader = pyo.TableRead(self.AudioTable, self.AudioTable.getRate()).out()
            return True

        elif file is None:
            return True

        else:
            return False

    def pause(self): ...

    def stop(self):
        self.AudioDecoder.stop()

    def seek_f(self): ...

    def seek_b(self): ...

    def skip_f(self):
        self.PlayingQueue.GetNext()

    def skip_b(self):
        self.PlayingQueue.GetPrevious()

if __name__ == "__main__":
    Queue = PlayingQueue()
    Player = PlayBack_Interface(Queue).ServerBootUp()
    # Player.play("D:\\music\\cantstopohn.mp3")
    Player.Gui()