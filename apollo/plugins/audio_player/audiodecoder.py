import os
import time
from threading import Thread, Event
from typing import Union

import av
import pyo
import numpy as np

from apollo import tryit, exe_time


class Audio__Table(pyo.DataTable):

    def __init__(self, path: str, duration: float = None, sample_rate: int = None):
        self._sample_rate = sample_rate if sample_rate else 44100
        self._chnls = 2
        self._audio_stream: av.container.InputContainer = av.open(path)
        self._table_duration = round(self._audio_stream.duration / 1000000, 2) if (duration is None) else duration
        self._table_size = round(self._table_duration * self._sample_rate)
        self._write_pos = 0
        self._path = path

        self.Init_Writer()
        super().__init__(size = self._table_size, chnls = self._chnls)

    @exe_time
    def decoder(self):
        for packet in self._audio_stream.demux(audio = 0):
            if not (packet.size <= 0):
                self.WriteFunction(packet)

    def Init_Writer(self):
        if os.path.splitext(self._path)[1] == ".mp3":
            self._resampler = av.AudioResampler(
                    format = av.AudioFormat('s16'),
                    layout = 'stereo',
                    rate = self._sample_rate
            )
            self.WriteFunction = self.WriteFrame_MP3

        elif os.path.splitext(self._path)[1] == ".flac":
            self._resampler = av.AudioResampler(
                    format = av.AudioFormat('s16'),
                    layout = 'stereo',
                    rate = self._sample_rate
            )
            self.WriteFunction = self.WriteFrame_FLAC

        elif os.path.splitext(self._path)[1].lower() == ".wav":
            self._resampler = av.AudioResampler(
                    format = av.AudioFormat('flt'),
                    layout = 'stereo',
                    rate = self._sample_rate
            )
            self.WriteFunction = self.WriteFrame_WAV

        else:
            self.WriteFunction = lambda x: print(x)

    def WriteFrame_MP3(self, packet: av.packet.Packet):
        def CreateTable(frame):
            frame: np.ndarray = frame.to_ndarray()
            frame = np.asarray([frame[0][0::2], frame[0][1::2]])
            return pyo.DataTable(len(frame[0]), self._chnls, frame.tolist()).normalize()

        for frame in packet.decode():
            frame = self._resampler.resample(frame)
            self.copyData(CreateTable(frame), 0, self._write_pos)
            self._write_pos += frame.samples - 1

    def WriteFrame_FLAC(self, packet: av.packet.Packet):
        def CreateTable(frame):
            frame: np.ndarray = frame.to_ndarray()
            frame = np.asarray([frame[0][0::2], frame[0][1::2]])
            return pyo.DataTable(len(frame[0]), self._chnls, frame.tolist()).normalize()

        for frame in packet.decode():
            frame = self._resampler.resample(frame)
            self.copyData(CreateTable(frame), 0, self._write_pos)
            self._write_pos += frame.samples - 1

    def WriteFrame_WAV(self, packet: av.packet.Packet):
        def CreateTable(frame):
            frame: np.ndarray = frame.to_ndarray()
            frame = np.asarray([frame[0][0::2], frame[0][1::2]])
            return pyo.DataTable(len(frame[0]), self._chnls, frame.tolist()).normalize()

        for frame in packet.decode():

            frame = self._resampler.resample(frame)
            self.copyData(CreateTable(frame), 0, self._write_pos)
            self._write_pos += frame.samples - 1


class ASF:

    def __init__(self): ...


class FLAC:

    def __init__(self): ...


class MP4:

    def __init__(self): ...


class Monkey_Audio:

    def __init__(self): ...


class MP3:

    def __init__(self): ...


class Musepack:

    def __init__(self): ...


class Ogg_Opus:

    def __init__(self): ...


class Ogg_FLAC:

    def __init__(self): ...


class Ogg_Speex:

    def __init__(self): ...


class Ogg_Theora:

    def __init__(self): ...


class Ogg_Vorbis:

    def __init__(self): ...


class True_Audio:

    def __init__(self): ...


class WavPack:

    def __init__(self): ...


class OptimFROG:

    def __init__(self): ...


class AIFF:

    def __init__(self): ...


class Audio_Table(pyo.DataTable):

    def __init__(self, path: str, duration: float = None):
        self._chnls = 2
        self._write_pos = 0
        self._path = path

        self._sample_rate = sample_rate if sample_rate else 44100
        self._audio_stream: av.container.InputContainer = av.open(self._path)
        self._table_duration = round(self._audio_stream.duration / 1000000, 2) if (duration is None) else duration
        self._table_size = round(self._table_duration * self._sample_rate)

        super().__init__(size = self._table_size, chnls = self._chnls)

        self._Buffer = np.asarray(self.getBuffer())

    @property
    def SamplesBuffer(self):
        return self._Buffer

    @SamplesBuffer.setter
    def SamplesBuffer(self, value):
        print("Read-Only Property")


if __name__ == '__main__':
    from pyo import Server

    _sample_rate = 44100
    server = Server(sr = _sample_rate).boot().start()
    server.setAmp(0.001)

    # Table = Audio_Table(r"D:\music\04 Back 2 U (DBSTF Remix).flac") # FLAC
    # Table = Audio_Table(r"D:\music\03. Doctor P, Flux PavilionStampede (Original Mix).flac") # FLAC
    # Table = Audio_Table(r"D:\music\02. Doctor P, Flux PavilionFuckers (Original Mix).flac") # FLAC
    # Table = Audio_Table(r"D:\music\03 Catch me if you Can.mp3") # MP3 E
    Table = Audio_Table(r"D:\music\04 Demons.mp3") # MP3
    # Table = Audio_Table(r"D:\music\06 Hands Up (feat. DNCE) [Raven & Kreyn Remix] - FrkMusic.Net.mp3")  # MP3

    # Table = Audio_Table(r"D:\music\32_bit_float_30_dB_atten.wav")
    # Table = Audio_Table(r"D:\music\32_bit_float.WAV")
    # Table = Audio_Table(r"D:\music\24_bit_fixed_30_dB_atten.wav")
    # Table = Audio_Table(r"D:\music\24_bit_fixed.WAV")

    Table.decoder()
    Table.view()
    Reader = pyo.TableRead(Table, Table.getRate(), loop = 1).out()
    spec = pyo.Spectrum(Reader)
    scope = pyo.Scope(Reader)
    server.gui(locals())
