import os
import time
from threading import Thread, Event
from typing import Union
from functools import reduce

import av
import numpy as np
import pyo

from apollo import exe_time


class Buffer_Info:
    """
    Buffer info that holds the info for the audio Tables
    """
    TIMEBASE_SEC: int = 0.026122448979591838
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

        self.VirtualBuffer = dict.fromkeys(range(self.Frame_VirtualSize + 1), False)
        self.VirtualCursor = 0
        self.ActualBuffer = dict.fromkeys(range(self.Frame_ActualSize + 1), False)

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

    def IsWritten(self, packet: av.packet.Packet):
        """
        Gets the state of a frame if is written

        Parameters
        ----------
        packet: av.packet.Packet
            packet to check for

        Returns
        -------
        bool
            if frame is written
        """
        return self.ActualBuffer[self.CalculateFrame(pts = packet.pts)]

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
        self.file_path = path
        self.InputStream = av.open(path)
        self.FrameInfo = self.GetFrameInfo(self.InputStream)
        self.Decoder = AudioDecoder(InputStream = self.InputStream, Buffer = self)

        # Additional Info
        self.sample_rate = samplerate
        self.duration = int(self.InputStream.duration / 1000000) if (duration is None) else duration
        self.BufferInfo = Buffer_Info(Time_VirtualSize = self.duration,
                                      Time_ActualSize = int(self.InputStream.duration / 1000000))
        self.table_size = int(self.duration * self.sample_rate)
        self.cursor = 0
        self.index = self.GetIndex()

        super().__init__(size = self.table_size, chnls = channels)
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

    def FillSample(self, obj, samples, pos):
        cursor = pos
        for sample in samples:
            # writes so fast that no time to read quick
            if cursor < self.table_size:
                obj.put(sample, cursor)
                cursor += 1
            else:
                self.Decoder.Pause()
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

        # 2.1 channel audio support
        # 5.1 channel audio support
        # 7.1 channel audio support

        else:
            raise Exception("Audio Channels Not Compatable")

        # DEBUG
        self.refreshView()

    def AppendFrame(self, frame: av.audio.frame.AudioFrame):
        """
        appends an audioframe and extends the audio table with given frame

        Parameters
        ----------
        frame : av.audio.frame.AudioFrame
            A frame of audio
        """
        print(frame)
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

    def Seek(self, time: float):
        """
        seeks to a given time in an audio table

        Parameters
        ----------
        time: int, float
            -> time in seconds to seek to
        """
        return int(round(time / TIMEBASE_SEC)) * TIMEBASE_PTS

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


class AudioTable_Circular(AudioTable):

    def __init__(self, path: str, duration: Union[int, None] = None, samplerate: int = 44100, channels: int = 2):
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
        self.refreshView()

    def WriteResidue(self):
        self.WriteBuffer(self.WriteResidue(), Residue = True)
        self.ResidueSamples = np.empty((2, 1))


class AudioDecoder(Thread):

    def __init__(self, path: str = None, InputStream: av.container.InputContainer = None, Buffer: AudioTable = None):
        super().__init__()
        if path is not None and Buffer is not None:
            self.file_path = path if path else ""
            self.Stream = av.open(self.file_path)
            self.Buffer = Buffer
            self.name = f"AudioDecoder_{id(path)}"
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
                    frame = next(self.Decoder(False))
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
                if not self.BufferTable.BufferInfo.IsWritten(packet):
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

    def play(self, dur = 0, delay = 0):
        """
        Start processing without sending samples to output.
        This method is called automatically at the object creation.

        This method returns `self`, allowing it to be applied at the object
        creation.

        Parameters
        ----------
        dur: float, optional
            Duration, in seconds, of the object's activation. The default
            is 0 and means infinite duration.
        delay: float, optional
            Delay, in seconds, before the object's activation. Defaults to 0.
        """
        self.index.play(dur, delay)
        super().play(dur, delay)

    def stop(self, wait=0):
        """
        Stop processing.

        This method returns `self`, allowing it to be applied at the object
        creation.

        .. note::
            if the method setStopDelay(x) was called before calling stop(wait)
            with a positive `wait` value, the `wait` value won't overwrite the
            value given to setStopDelay for the current object, but will be
            the one propagated to children objects. This allow to set a waiting
            time for a specific object with setStopDelay whithout changing the
            global delay time given to the stop method.

            Fader and Adsr objects ignore waiting time given to the stop
            method because they already implement a delayed processing
            triggered by the stop call.

        Parameters
        ----------

            wait: float, optional
                Delay, in seconds, before the process is actually stopped.
                If autoStartChildren is activated in the Server, this value
                is propagated to the children objects. Defaults to 0.
        """
        self.index.stop(wait)
        super().stop(wait)
        return self


class AudioPlayer:

    def __init__(self, PlayingQueue: Union[list]):
        self.ActiveReaders = []
        self.PlayingQueue = PlayingQueue


if __name__ == "__main__":
    Server = pyo.Server().boot().start()
    Server.setAmp(0.01)
    paths = [os.path.join(r"D:\music", path) for path in os.listdir(r"D:\music")]
    Player = AudioPlayer(paths)
    Server.gui()
