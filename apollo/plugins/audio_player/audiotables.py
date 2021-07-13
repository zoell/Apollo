import datetime
import os
import time
from threading import Thread, Event
from typing import Union
from functools import reduce

import av
import numpy as np
import pyo

from apollo import exe_time, PlayingQueue
from apollo.plugins.audio_player.mediafile import MediaFile


class Buffer_Info:
    """
    Buffer info that holds the info for the audio Tables

    Information Present:
    1. Actual BUffer info
    2. Virtual Buffer Info
    """
    TIMEBASE_SEC: float = 0.026122448979591838
    TIMEBASE_PTS: int = 368640

    def __init__(self, **kwargs):
        """
        Class Constructor
        """
        # size of time buffer in memory
        self.Time_ActualSize = kwargs.get("Time_ActualSize", 0)
        # size of frame buffer in memory
        self.Frame_ActualSize = kwargs.get("Frame_ActualSize", self.CalculateFrame(time = self.Time_ActualSize))

        # actual size of the time in file
        self.Time_VirtualSize = kwargs.get("Time_VirtualSize", 0)
        # actual size of the frames in file
        self.Frame_VirtualSize = kwargs.get("Frame_VirtualSize", self.CalculateFrame(time = self.Time_VirtualSize))

        self.VirtualCursor = 0
        self.VirtualBuffer = dict.fromkeys(range(self.Frame_VirtualSize + 1), False)
        self.ActualBuffer = dict.fromkeys(range(self.Frame_ActualSize + 1), False)

        # time pointer for the Audio Table
        self.TimePointer = 0

    def FrameWrite(self, index: int):
        """
        Updates when the frame is written to the buffer

        Parameters
        ----------
        index: int
            index of the frame
        """
        self.ActualBuffer[index] = True
        self.Update_VirtualBuffer(index)

    def Update_VirtualBuffer(self, index: int):
        """
        Updates when the frame is written to the Virtual buffer

        Parameters
        ----------
        index: int
            index of the frame
        """
        if self.VirtualCursor >= len(self.VirtualBuffer):
            self.VirtualCursor = 0
            self.VirtualBuffer[self.VirtualCursor] = index
        else:
            self.VirtualBuffer[self.VirtualCursor] = index
            self.VirtualCursor += 1

    def IsWritten(self, packet: av.packet.Packet = None, frame: av.audio.frame.AudioFrame = None):
        """
        Gets the state of a frame if is written

        Parameters
        ----------
        packet: av.packet.Packet
            packet to check for
        frame: av.audio.frame.AudioFrame
            frame to check for

        Returns
        -------
        bool
            if frame is written
        """
        if packet is not None:
            frame = self.CalculateFrame(pts = packet.pts)

        try:
            return self.ActualBuffer[frame]
        except KeyError:
            self.ActualBuffer[frame] = False
            return False

    @staticmethod
    def CalculateFrame(time: Union[None, float] = None, pts: Union[None, int] = None):
        """
        Gets a rough estimate of the frame at the given time

        Parameters
        ----------
        time: Union[None, float]
            time in float
        pts: Union[None, int]
            point to use

        Returns
        -------
        int
            frame
        """
        if time is not None:
            return int(round(time / Buffer_Info.TIMEBASE_SEC))
        if pts is not None:
            return int(round(pts / Buffer_Info.TIMEBASE_PTS))

    @staticmethod
    def CalculatePoint(time: float):
        """
        Gets a rough estimate of the point at the given time

        Parameters
        ----------
        time: float
            time in float

        Returns
        -------
        int
            Point
        """
        return int(round(time / Buffer_Info.TIMEBASE_SEC)) * Buffer_Info.TIMEBASE_PTS


class AudioTable(pyo.DataTable):
    """
    Audio Table Buffer to add decoded samples
    """

    def __init__(self, path: str, duration: Union[int, None] = None, samplerate: int = 44100, channels: int = 2):
        """
        creates a datatable of decoded samples for a give file path

        Parameters
        ----------
        path : str
            path to a file to decode
        duration : int
            duration of the table, by default None
        samplerate : int, optional
            samplerate of the audio table, by default 44100
        channels : int, optional
            channels of audio, by default 2
        """
        # Creates the Audio Table
        self.file_path = path
        self.sample_rate = samplerate
        self.cursor = 0
        self.InputStream: av.container.InputContainer = av.open(path)
        self.duration = int(self.InputStream.duration / 1000000) if (duration is None) else duration
        self.FrameInfo = self.GetFrameInfo(self.InputStream)
        self.BufferInfo = Buffer_Info(Time_VirtualSize = self.duration,
                                      Time_ActualSize = int(self.InputStream.duration / 1000000))
        self.table_size = int(self.duration * self.sample_rate)
        self.index = self.GetIndex()
        super().__init__(size = self.table_size, chnls = channels)

        # Creates the Decoder
        self.Decoder = AudioDecoder(InputStream = self.InputStream, Buffer = self)
        self.Decode()

    def GetIndex(self):
        """
        Draw a series of line segments between specified break-points.

        Returns
        -------
        pyo.Linseg
            line segment that is the index of the table
        """
        if self.BufferInfo.Time_ActualSize == self.BufferInfo.Time_VirtualSize:
            Duration = self.BufferInfo.Time_ActualSize
            Loop = False
        else:
            Duration = self.BufferInfo.Time_VirtualSize
            Loop = True
        return pyo.Linseg([(0, 0), (Duration, 1)], loop = Loop)

    def GetFrameInfo(self, Stream: av.container.InputContainer):
        """
        Gets the frame info

        Parameters
        ----------
        Stream: av.container.InputContainer
            input stream to get frame from

        Returns
        -------
        tuple
            Frame info
        """
        for packet in Stream.demux(audio = 0):
            for frame in packet.decode():
                if frame.index == 1:
                    Stream.seek(0)
                    return tuple([frame.samples, len(frame.planes)])

    def FillSample(self, obj: pyo.PyoTableObject, samples: np.array, pos: int):
        """
        Fills the given samples in the table

        Parameters
        ----------
        obj: pyo.PyoTableObject
            table to put samples to
        samples: np.array
            samples to put on the table
        pos: int
            position to start insert at
        Returns
        -------
        int
            last position samples were entered to
        """
        cursor = pos
        for sample in samples:
            # writes so fast that no time to read quick
            if cursor < self.table_size:
                obj.put(sample, cursor)
                cursor += 1
            else:
                self.BufferEnd()
                cursor = 0
                break
        return cursor

    def WriteBuffer(self, array: np.array, pos: int = None):
        """
        Adds given samples to the audio table.

        Parameters
        ----------
        array : np.array
            array that contains audio samples
        pos : int
            pos to add samples to
        """
        # 'run' 4.4445 s
        array_channels = array.shape[0]
        if pos is None:
            pos = self.cursor

        # noramal one to one cration of channels
        if array_channels == self._chnls:
            for index, obj in enumerate(self._base_objs):
                self.cursor = self.FillSample(obj, array[index], pos)

        # for mono audio copies on both channels same audio and converts to dual
        elif (array_channels == 1) and (self._chnls == 2):
            for obj in self._base_objs:
                self.cursor = self.FillSample(obj, array[0], pos)

        # TODO: 2.1 channel audio support
        # TODO: 5.1 channel audio support
        # TODO: 7.1 channel audio support

        else:
            raise Exception("Audio Channels Not Compatable")

        # DEBUG
        # self.refreshView()

    def AppendFrame(self, frame: av.audio.frame.AudioFrame):
        """
        appends an audioframe and extends the audio table with given frame

        Parameters
        ----------
        frame : av.audio.frame.AudioFrame
            A frame of audio
        """
        self.BufferInfo.FrameWrite(frame.index)
        self.WriteBuffer(frame.to_ndarray())

    def AppendArray(self, array: np.array):
        """
        appends the audio table with given samples.

        Parameters
        ----------
        array : np.array
            array that contains audio samples
        """
        self.WriteBuffer(array)

    def Seek_B(self, time: float = 5):
        """
        Seeks Back to a given time in an audio table

        Parameters
        ----------
        time: int, float
            -> time in seconds to seek to
        """
        Current_time = self.BufferInfo.CurrentTime - time
        if Current_time < 0:
            Current_time = 0
        elif Current_time > self.BufferInfo.Time_ActualSize:
            Current_time = self.BufferInfo.Time_ActualSize
        else:
            Current_time = round(Current_time, 2)
        self.Seek(Current_time)

    def Seek_F(self, time: float = 5):
        """
        Seeks Forward to a given time in an audio table

        Parameters
        ----------
        time: int, float
            -> time in seconds to seek to
        """
        Current_time = self.BufferInfo.CurrentTime + time
        if Current_time < 0:
            Current_time = 0
        elif Current_time > self.BufferInfo.Time_ActualSize:
            Current_time = self.BufferInfo.Time_ActualSize
        else:
            Current_time = round(Current_time, 2)
        self.Seek(Current_time)

    def Seek(self, time: float):
        """
        seeks to a given time in an audio table

        Parameters
        ----------
        time: int, float
            -> time in seconds to seek to
        """
        if self.BufferInfo.IsWritten(frame = self.BufferInfo.CalculateFrame(time = time)):
            # move index to point
            pass
        else:
            # Start a decoder and seek to time
            self.Decoder.Pause()
            point = int(round(time / TIMEBASE_SEC)) * TIMEBASE_PTS
            self.InputStream.seek(point)
            # calculate frame and sample position
            # move write pointer to that position
            # move read pointer to that position
            self.Decoder.Decode()

    def BufferEnd(self):
        """
        Called when the buffer reaches the end and resets
        """
        self.Decoder.Pause()

    def Decode(self):
        """
        Called to  start the paused decoder
        """
        self.Decoder.Decode()

    def Close(self):
        """
        Exit function for the AudioTable
        """
        self.Decoder.Kill()

    def Pause(self):
        """
        Pauses the Table Reader Pointer
        """
        self.index.pause()

    def Play(self):
        """
        Starts the Table Reader Pointer
        """
        self.index.play()


class AudioTable_Circular(AudioTable):
    """
    Circular implementation of the Audio Table Calss
    """

    def __init__(self, path: str, duration: Union[int, None] = None, samplerate: int = 44100, channels: int = 2):
        """
        Class Constructor

        Parameters
        ----------
        path: str
            File Path
        duration: Union[int, None]
            Duartion of the table
        samplerate: int
            Sample rate of the table
        channels: int
            Channels of the audio table
        """
        super().__init__(path, duration, samplerate, channels)
        self.ResidueSamples = np.empty((2, 1))

    def WriteBuffer(self, array: np.array, pos: int = None, Residue: bool = False):
        """
        Adds given samples to the audio table.

        Parameters
        ----------
        array : np.array
            array that contains audio samples
        pos : int
            pos to add samples to
        Residue: bool
            if this function need to disable Writing residue
        """
        array_channels = array.shape[0]
        array_length = array.shape[1]

        if pos is None:
            pos = self.cursor

        if Residue:
            self.WriteResidue()

        # normal one to one creation of channels
        if array_channels == self._chnls:
            for index, obj in enumerate(self._base_objs):
                self.cursor = self.FillSample(obj, array[index], pos)
            if (array_length + pos) >= self.table_size:
                self.ResidueSamples = np.asarray([chns[((array_length + pos) - self.table_size):] for chns in array])

        # for mono audio copies on both channels same audio and converts to dual
        elif (array_channels == 1) and (self._chnls == 2):
            for obj in self._base_objs:
                self.cursor = self.FillSample(obj, array[0], pos)
            if (array_length + pos) >= self.table_size:
                self.ResidueSamples = np.asarray(array[0][((array_length + pos) - self.table_size):])

        # TODO: 2.1 channel audio support
        # TODO: 5.1 channel audio support
        # TODO: 7.1 channel audio support

        else:
            raise Exception("Audio Channels Not Compatable")

        # DEBUG
        # self.refreshView()

    def WriteResidue(self):
        """
        Writes the residue samples to the buffere when it resets
        """
        self.WriteBuffer(self.WriteResidue(), Residue = True)
        self.ResidueSamples = np.empty((2, 1))


class AudioDecoder(Thread):
    """
    Audio decoder for the audio Tables
    """

    def __init__(self, path: str = None, InputStream: av.container.InputContainer = None, Buffer: AudioTable = None):
        """
        Class Constrtuctor

        Parameters
        ----------
        path: str
            Path of the file to read
        InputStream: av.container.InputContainer
            Input stream to decode
        Buffer: AudioTable
            Buffer to write samples to
        """
        super().__init__()
        # runs when a path is given and a stream is created internally
        if path is not None and Buffer is not None:
            self.file_path = path if path else ""
            self.Stream = av.open(self.file_path)
            self.Buffer = Buffer
            self.name = f"AudioDecoder_{id(path)}"
        # runs when a stream is passed in and is not inited internally
        elif InputStream is not None and Buffer is not None:
            self.Stream = InputStream
            self.Buffer = Buffer
            self.name = f"AudioDecoder_{id(Buffer.file_path)}"
        else:
            raise ValueError("Invalid Arguments Passed to AudioDecoder")
        self.CreateEvents()
        self.start()

    def run(self):
        """
        Run function of the thread
        """
        while self.Event_DeoderAlive.isSet():
            if self.Event_Pause.isSet():
                time.sleep(0.01)
                continue

            if self.Event_Decode.isSet():
                try:
                    frame = next(self.Decoder(True))
                    # if frame.index == 1000:
                    #     self.Kill()
                    if frame != "WRITTEN":
                        self.Buffer.AppendFrame(frame)
                except StopIteration:
                    print("EOF")
                    self.Pause()
                continue
        print("Decoder Stopped")

    def CreateEvents(self):
        """
        Inits all the thread events taht can be triggered
        """
        self.Event_DeoderAlive = Event()
        self.Event_DeoderAlive.set()

        self.Event_Decode = Event()
        self.Event_Pause = Event()
        self.Pause()

    def Decoder(self, Check: bool):
        """
        Decoder Generator that Generates the frames

        Returns
        -------
        av.audio.frame
            frame that has been decoded
        """
        # actual decoding and demuxing of file
        for packet in self.Stream.demux(audio = 0):
            if packet.size <= 0:
                break
            if Check:
                if not self.Buffer.BufferInfo.IsWritten(packet):
                    for frame in packet.decode():
                        yield frame
                else:
                    yield "WRITTEN"
            else:
                for frame in packet.decode():
                    yield frame

    def Decode(self):
        """
        Starts the decoder and writes samples to the buffer
        """
        self.Event_Pause.clear()
        self.Event_Decode.set()

    def Pause(self):
        """
        Pauses The Decoder
        """
        self.Event_Pause.set()
        self.Event_Decode.clear()

    def Kill(self):
        """
        Kills the Thread
        """
        self.Event_DeoderAlive.clear()


class AudioReader(pyo.Pointer2):
    """
    Audio reader for the tables
    """
    index: pyo.Linseg

    def __init__(self, table: AudioTable):
        """
        Class Constructor

        Parameters
        ----------
        table: PyoTableObject
            Table containing the waveform samples.
        """
        self.current_table = table
        super().__init__(self.current_table, self.current_table.index)

    def setTable(self, Table: AudioTable):
        """
        Replaces the table attribute

        Parameters
        ----------
        Table: AudioTable
            Tale to replace with
        """
        self.setTable(Table)
        self.setIndex(Table.index)


class Apollo_AudioPlayer:
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
        # debug methods
        self.MainServer.setAmp(0.05)
        return self

    def Gui(self):
        """
        Starts the GUI for Audio Processor server
        """
        self.MainServer.gui(locals())

    def Play(self):
        """
        Play playback
        """
        self.MainServer.start()

    def Pause(self):
        """
        Pause playback
        """
        self.MainServer.stop()

    def Stop(self):
        """
        Stop playback
        """
        self.MainServer.stop()

    def Seek_F(self):
        """
        Seek_F playback
        """
        pass

    def Seek_B(self):
        """
        Seek_B playback
        """
        pass

    def Skip_F(self):
        """
        Skip_F playback
        """
        pass

    def Skip_B(self):
        """
        Skip_B playback
        """
        pass

    @property
    def ServerInfo(self):
        """
        Gets server and device info
        """
        return {"pa_count_devices": pyo.pa_count_devices(),
                "pa_get_default_input": pyo.pa_get_default_input(),
                "pa_get_default_output": pyo.pa_get_default_output(),
                "pm_get_input_devices": pyo.pm_get_input_devices(),
                "pa_count_host_apis": pyo.pa_count_host_apis(),
                "pa_get_default_host_api": pyo.pa_get_default_host_api(),
                "pm_count_devices": pyo.pm_count_devices(),
                "pa_get_input_devices": pyo.pa_get_input_devices(),
                "pm_get_default_input": pyo.pm_get_default_input(),
                "pm_get_output_devices": pyo.pm_get_output_devices(),
                "pm_get_default_output": pyo.pm_get_default_output(),
                "pa_get_devices_infos": pyo.pa_get_devices_infos(),
                "pa_get_version": pyo.pa_get_version(),
                "pa_get_version_text": pyo.pa_get_version_text()
                }


if __name__ == "__main__":
    pass
    # @property
    # def BufferMetadata(self):
    #     if not hasattr(self, "CurrentFile_Info"):
    #         self.CurrentFile_Info = MediaFile(self.PlayingQueue.GetCurrent())
    #     track_length = datetime.datetime.strptime(self.CurrentFile_Info["length"], "%H:%M:%S.%f")
    #
    # @BufferMetadata.setter
    # def BufferMetadata(self, value):
    #     raise NotImplementedError

    # from PySide6 import QtWidgets, QtGui, QtCore
    # from PySide6.QtWidgets import QApplication
    #
    # from apollo.plugins.audio_player.ui_trial_player import Ui_MainWindow as PlayerUI
    # from apollo import PlayingQueue
    #
    #
    # class PlayerUI_obj(PlayerUI, QtWidgets.QMainWindow):
    #
    #     def __init__(self):
    #         super().__init__()
    #         self.setupUi(self)
    #         self.Player = Apollo_AudioPlayer().ServerBootUp()
    #         self.Init_Model()
    #         self.FunctionBindings()
    #
    #         self.Table = AudioTable(self.PlayingQueue.GetCurrent())
    #         self.Reader = AudioReader(self.Table)
    #         self.Table.Play()
    #         self.Reader.out()
    #
    #     def FunctionBindings(self):
    #         self.pushButton.pressed.connect(self.Player.Stop)
    #         self.pushButton_2.pressed.connect(self.Player.Play)
    #         self.pushButton_3.pressed.connect(print)
    #         self.pushButton_4.pressed.connect(print)
    #         self.pushButton_5.pressed.connect(print)
    #         self.pushButton_6.pressed.connect(print)
    #         self.pushButton_7.pressed.connect(print)
    #
    #     def Init_Model(self):
    #         model = QtGui.QStandardItemModel()
    #         self.PlayingQueue = PlayingQueue()
    #         self.PlayingQueue.AddElements([os.path.join(r"D:\music", path) for path in os.listdir(r"D:\music")])
    #         self.PlayingQueue.GetNext()
    #         for r, v in enumerate(self.PlayingQueue.GetQueue()):
    #             model.insertRow(r, QtGui.QStandardItem(v))
    #         self.listView.setModel(model)
    #
    #
    # app = QApplication([])
    # app.setStyle("Fusion")
    # UI = PlayerUI_obj()
    # UI.show()
    # app.exec()