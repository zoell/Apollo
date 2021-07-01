import os
import time
from threading import Thread, Event
from typing import Union

import av
import numpy as np
import pyo


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
        self.Frame_ActualSize = kwargs.get("Frame_ActualSize", self.CalculateFrame(self.Time_ActualSize))

        # actual size of the time in file
        self.Time_VirtualSize = kwargs.get("Time_VirtualSize", 0)
        # actual size of the frames in file
        self.Frame_VirtualSize = kwargs.get("Frame_VirtualSize", self.CalculateFrame(self.Time_VirtualSize))

        self.VirtualBuffer = dict.fromkeys(range(self.Frame_VirtualSize + 1), False)
        self.ActualBuffer = dict.fromkeys(range(self.Frame_ActualSize + 1), False)

    @staticmethod
    def CalculateFrame(time: float):
        """
        Gets a rough estimate of the frame at the given time

        Parameters
        ----------
        time: float
            time in float

        Returns
        -------
        int
            frame
        """
        return int(round(time / Buffer_Info.TIMEBASE_SEC))

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


class Audio_Table(pyo.DataTable):

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
        self.Decoder = Audio_Decoder(InputStream = self.InputStream, BufferTable = self, Name = id(path))

        # Additional Info
        self.sample_rate = samplerate
        self.channels = channels
        self.duration = int(self.InputStream.duration / 1000000) if (duration is None) else duration
        self.BufferInfo = Buffer_Info(Time_VirtualSize = self.duration,
                                      Time_ActualSize = int(self.InputStream.duration / 1000000))
        self.table_size = int(self.duration * self.sample_rate)
        self.cursor = 0

        super().__init__(size = self.table_size, chnls = self.channels)
        self.Decode()

    def write(self, array: np.array, pos: int):
        """
        Adds given samples to the audio table.

        Parameters
        ----------
        array : np.array
            array that contains audio samples
        pos : int
            pos to add samples to
        """

        def FillSamples(obj, samples, cursor):
            for sample in samples:
                # writes so fast that no time to read quick
                if cursor >= self.table_size:
                    cursor = 0
                    obj.put(sample, cursor)
                    self.Decoder.Pause()
                else:
                    obj.put(sample, cursor)
                    cursor += 1
            return cursor

        array_channels = array.shape[0]

        # noramal one to one cration of channels
        if array_channels == self._chnls:
            for index, obj in enumerate(self._base_objs):
                self.cursor = FillSamples(obj, array[index], pos)

        # for mono audio copies on both channels same audio and converts to dual
        elif (array_channels == 1) and (self._chnls == 2):
            for obj in self._base_objs:
                self.cursor = FillSamples(obj, array[0], pos)

        # 2.1 channel audio support
        # 5.1 channel audio support
        # 7.1 channel audio support

        else:
            raise Exception("Audio Channels Not Compatable")

        # DEBUG
        self.refreshView()

    def append_frame(self, frame):
        """
        appends an audioframe and extends the audio table with given frame

        Parameters
        ----------
        frame : av.audio.frame.AudioFrame
            A frame of audio
        """
        # if not self.BufferInfo.isWritten(frame):
        self.write(frame.to_ndarray(), self.cursor)

    def append_array(self, array):
        """
        appends the audio table with given samples.

        Parameters
        ----------
        array : np.array
            array that contains audio samples
        """
        self.write(array, self.cursor)

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

    def Seek(self, time: float):
        """
        seeks to a given time in an audio table

        Parameters
        ----------
        time: int, float
            -> time in seconds to seek to
        """
        return int(round(time / TIMEBASE_SEC)) * TIMEBASE_PTS

    def Close(self):
        """
        Exit function for the AudioTable
        """
        self.Decoder.Kill()


class Audio_Decoder(Thread):

    def __init__(self, InputStream: av.container.InputContainer, BufferTable: Audio_Table, Name: str):
        """
        Thread that decodes the given stream of Audio

        Parameters
        ----------
        InputStream: av.container.InputContainer
            Input Stream To decode
        BufferTable: Audio_Table
            Audio Buffer to fill with Decoded Frames
        Name: str
            name of the given thread
        """
        super().__init__()
        self.name = f"AudioDecoder_{Name}"
        self.InputStream = InputStream
        self.BufferTable = BufferTable
        self.InitEvents()
        self.start()

    def InitEvents(self):
        """
        Inits all the thread events taht can be triggered
        """
        self.Event_DeoderAlive = Event()
        self.Event_DeoderAlive.set()

        self.Event_Decode = Event()
        self.Event_Pause = Event()
        self.Pause()

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
                    frame = next(self._DecodeFrame())
                    self.BufferTable.append_frame(frame)
                except StopIteration:
                    print("EOF")

    def _DecodeFrame(self):
        """
        Decoder Generator that Generates the frames

        Returns
        -------
        av.audio.frame
            frame that has been decoded
        """

        # actual decoding and demuxing of file
        for packet in self.InputStream.demux(audio = 0):
            if not (packet.size <= 0):
                for frame in packet.decode():
                    yield frame
            else:
                self.Pause()

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


class Audio_Reader(pyo.Pointer2):
    index: pyo.Linseg

    def __init__(self, table, interp = 4, autosmooth = True, mul = 1, add = 0):
        """
        Class Constructor

        Parameters
        ----------
        table: PyoTableObject
            Table containing the waveform samples.

        index: PyoObject
            Normalized position in the table between 0 and 1.

        interp: int {1, 2, 3, 4}, optional
            Choice of the interpolation method. Defaults to 4.
            1: no interpolation
            2: linear
            3: cosinus
            4: cubic

        autosmooth: boolean, optional
            If True, a lowpass filter, following the pitch, is applied on
            the output signal to reduce the quantization noise produced
            by very low transpositions. Defaults to True.
        """
        self.current_table = table
        super().__init__(table, self.GetIndex(), interp = 4, autosmooth = True, mul = 1, add = 0)

    def Seek_Back(self, time: float): ...
    def Seek_Front(self, time: float): ...

    def GetIndex(self):
        """
        Draw a series of line segments between specified break-points.

        Returns
        -------
        pyo.Linseg
            line segment that is the index of the table
        """
        if self.current_table.BufferInfo.Time_ActualSize == self.current_table.BufferInfo.Time_VirtualSize:
            Duration = self.current_table.BufferInfo.Time_ActualSize
            Loop = False
        else:
            Duration = self.current_table.BufferInfo.Time_VirtualSize
            Loop = True
        return pyo.Linseg([(0, 0), (Duration, 1)], loop = Loop)

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
        self.index.play()
        super().play(dur, delay)

    def out(self, chnl = 0, inc = 1, dur = 0, delay = 0):
        """
        Start processing and send samples to audio output beginning at `chnl`.

        This method returns `self`, allowing it to be applied at the object
        creation.

        If `chnl` >= 0, successive streams increment the output number by
        `inc` and wrap around the global number of channels.

        If `chnl` is negative, streams begin at 0, increment
        the output number by `inc` and wrap around the global number of
        channels. Then, the list of streams is scrambled.

        If `chnl` is a list, successive values in the list will be
        assigned to successive streams.

        Parameters
        ----------
        chnl: int, optional
            Physical output assigned to the first audio stream of the
            object. Defaults to 0.
        inc: int, optional
            Output channel increment value. Defaults to 1.
        dur: float, optional
            Duration, in seconds, of the object's activation. The default
            is 0 and means infinite duration.
        delay: float, optional
            Delay, in seconds, before the object's activation.
            Defaults to 0.
        """
        self.index.play()
        super().out(chnl = 0, inc = 1, dur = 0, delay = 0)


if __name__ == "__main__":
    Server = pyo.Server().boot()
    Queue = Audio_Table("D:\\music\\AviciiForever Yours.mp3")
    Reader = Audio_Reader(Queue)
    Reader.out()
    Reader.index.graph()
    Server.gui()
