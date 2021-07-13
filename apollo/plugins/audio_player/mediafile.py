import datetime

import av
import mutagen
import pyo


class Media:
    DBFIELDS = ("file_id", "path_id", "file_name", "file_path", "album",
                "albumartist", "artist", "author", "bpm", "compilation",
                "composer", "conductor", "date", "discnumber", "encodedby",
                "discsubtitle", "genre", "language", "length", "filesize",
                "lyricist", "media", "mood", "organization", "originaldate",
                "performer", "releasecountry", "replaygain_gain", "replaygain_peak",
                "title", "tracknumber", "version", "website", "album_gain",
                "bitrate", "bitrate_mode", "channels", "encoder_info", "encoder_settings",
                "frame_offset", "layer", "mode", "padding", "protected", "sample_rate",
                "track_gain", "track_peak", "rating", "playcount")

    def __init__(self, path):
        self._file_path = path

    def RestartStream(self):
        self._audio_stream = av.open(self._file_path)
        return self._audio_stream

    def WriteFrame(self, Packet: av.packet.Packet, Buffer: pyo.DataTable, Pos: int):
        raise NotImplementedError

    def TransfromFrame(self, Frame, channels = 2):
        raise NotImplementedError

    def Create_DataTable(self, Frame, channels = 2, normalize = True):
        raise NotImplementedError

    @property
    def AudioStream(self):
        if not hasattr(self, "_audio_stream"):
            self._audio_stream = av.open(self._file_path)
        return self._audio_stream

    @property
    def Metadata(self):
        if not hasattr(self, "_metadata"):
            Media = mutagen.File(self._file_path, easy = True)
            metadata = dict.fromkeys(self.DBFIELDS, "")
            for key in self.DBFIELDS:
                metadata[key] = Media.get(key, [""])[0]

            # Misc info
            metadata["filesize"] = f"{round(os.path.getsize(Media.filename) * 0.00000095367432, 2)} Mb"
            metadata["file_name"] = os.path.split(Media.filename)[1]
            metadata["file_path"] = Media.filename
            metadata["rating"] = 0
            metadata["playcount"] = 0

            # Stream info
            if hasattr(Media.info, "bitrate_mode"):
                metadata["bitrate_mode"] = str(Media.info.bitrate_mode).replace('BitrateMode', "").replace('.', "")
            if hasattr(Media.info, "album_gain"):
                metadata['album_gain'] = Media.info.album_gain
            if hasattr(Media.info, "encoder_info"):
                metadata['encoder_info'] = Media.info.encoder_info
            if hasattr(Media.info, "encoder_settings"):
                metadata['encoder_settings'] = Media.info.encoder_settings
            if hasattr(Media.info, "frame_offset"):
                metadata['frame_offset'] = Media.info.frame_offset
            if hasattr(Media.info, "layer"):
                metadata['layer'] = Media.info.layer
            if hasattr(Media.info, "mode"):
                metadata['mode'] = Media.info.mode
            if hasattr(Media.info, "padding"):
                metadata['padding'] = Media.info.padding
            if hasattr(Media.info, "protected"):
                metadata['protected'] = Media.info.protected
            if hasattr(Media.info, "track_gain"):
                metadata['track_gain'] = Media.info.track_gain
            if hasattr(Media.info, "track_peak"):
                metadata['track_peak'] = Media.info.track_peak
            if hasattr(Media.info, "version"):
                metadata['version'] = Media.info.version
            if hasattr(Media.info, "sample_rate"):
                metadata['sample_rate'] = f"{Media.info.sample_rate}Hz"
            if hasattr(Media.info, "length"):
                metadata["length"] = str(datetime.timedelta(seconds = Media.info.length))
            if hasattr(Media.info, "bitrate"):
                metadata["bitrate"] = f"{int(Media.info.bitrate / 1000)} Kbps"
            if hasattr(Media.info, "channels"):
                metadata['channels'] = Media.info.channels

            self._metadata = metadata
        return self._metadata

    @property
    def Artwork(self):
        if not hasattr(self, "_artwork"):
            Media = mutagen.File(self._file_path)
            Artwork = Media.tags.getall("APIC:")
            Artwork = {int(data.type): data.data for data in Artwork}
            self._artwork = Artwork
            return Artwork
        else:
            return self._artwork


# Media Formats --------------------------------------------------------------------------------------------------------
class MP3(Media):
    def __init__(self, path):
        super().__init__(path)

    def TransfromFrame(self, Frame: av.audio.frame.AudioFrame, channels: int = 2):
        Frame: np.ndarray = Frame.to_ndarray()
        Frame = np.asarray([Frame[0][c::channels] for c in range(channels)])
        return Frame.tolist()

    def Create_DataTable(self, Frame: av.audio.frame.AudioFrame, channels: int = 2, normalize: bool = True):
        Frame = self.TransfromFrame(Frame, channels)
        if normalize:
            return pyo.DataTable(len(Frame[0]), channels, Frame).normalize()
        else:
            return pyo.DataTable(len(Frame[0]), channels, Frame)

    def WriteFrame(self, Packet: av.packet.Packet, Buffer: pyo.DataTable, Pos: int):
        for frame in Packet.decode():
            Buffer.copyData(self.CreateTable(frame, Buffer.chnl), 0, Pos)
            Pos += frame.samples - 1

    @staticmethod
    def IsFile(ext):
        return ext in [".mp3"]

    @property
    def extension(self):
        return ".mp3"


class WAV(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".wav"]

    @property
    def extension(self):
        return ".wav"


class FLAC(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".flac"]

    @property
    def extension(self):
        return ".flac"


class OPUS(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".opus"]

    @property
    def extension(self):
        return ".opus"


class OGG(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".ogg"]

    @property
    def extension(self):
        return ".ogg"


class AAC(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".aac"]

    @property
    def extension(self):
        return ".aac"


class AC3(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".ac3"]

    @property
    def extension(self):
        return ".ac3"


class AIFF(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".aiff"]

    @property
    def extension(self):
        return ".aiff"


class APE(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".ape"]

    @property
    def extension(self):
        return ".ape"


class M4A(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".m4a"]

    @property
    def extension(self):
        return ".m4a"


class MP4(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".mp4"]

    @property
    def extension(self):
        return ".mp4"


class WMA(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".wma"]

    @property
    def extension(self):
        return ".wma"


class DSF(Media):
    def __init__(self, path):
        super().__init__(path)

    @staticmethod
    def IsFile(ext):
        return ext in [".dsf"]

    @property
    def extension(self):
        return ".dsf"


# Main Interface -------------------------------------------------------------------------------------------------------
class MediaFile:

    def __init__(self, file: str):
        file = os.path.normpath(file)
        if os.path.isfile(file):
            self.Create_MediaObject(file)
        else:
            raise FileNotFoundError()

    def Create_MediaObject(self, path: str):
        EXT = os.path.splitext(path)[1].lower()
        if MP3.IsFile(EXT):
            self.Media = MP3(path)
        elif FLAC.IsFile(EXT):
            self.Media = FLAC(path)
        elif OPUS.IsFile(EXT):
            self.Media = OPUS(path)
        elif OGG.IsFile(EXT):
            self.Media = OGG(path)
        elif AAC.IsFile(EXT):
            self.Media = AAC(path)
        elif AC3.IsFile(EXT):
            self.Media = AC3(path)
        elif AIFF.IsFile(EXT):
            self.Media = AIFF(path)
        elif APE.IsFile(EXT):
            self.Media = APE(path)
        elif M4A.IsFile(EXT):
            self.Media = M4A(path)
        elif MP4.IsFile(EXT):
            self.Media = MP4(path)
        elif WMA.IsFile(EXT):
            self.Media = WMA(path)
        elif DSF.IsFile(EXT):
            self.Media = DSF(path)
        elif WAV.IsFile(EXT):
            self.Media = WAV(path)
        else:
            raise NotImplementedError(f"File Extension Not supported {EXT}")

    def RestartStream(self):
        self.Media.RestartStream()
        return self.Media.AudioStream

    @staticmethod
    def IsSupported(path):
        EXT = os.path.splitext(path)[1].lower()
        if MP3.IsFile(EXT):
            return True
        elif FLAC.IsFile(EXT):
            return True
        elif OPUS.IsFile(EXT):
            return True
        elif OGG.IsFile(EXT):
            return True
        elif AAC.IsFile(EXT):
            return True
        elif AC3.IsFile(EXT):
            return True
        elif AIFF.IsFile(EXT):
            return True
        elif APE.IsFile(EXT):
            return True
        elif M4A.IsFile(EXT):
            return True
        elif MP4.IsFile(EXT):
            return True
        elif WMA.IsFile(EXT):
            return True
        elif DSF.IsFile(EXT):
            return True
        elif WAV.IsFile(EXT):
            return True
        else:
            return False

    @property
    def SupportedFormats(self):
        return (MP3.extension,
                FLAC.extension,
                OPUS.extension,
                OGG.extension,
                AAC.extension,
                AC3.extension,
                AIFF.extension,
                APE.extension,
                M4A.extension,
                MP4.extension,
                WMA.extension,
                DSF.extension,
                WAV.extension)

    @property
    def AudioStream(self):
        return self.Media.AudioStream

    @property
    def Metadata(self):
        return self.Media.Metadata

    @property
    def Artwork(self):
        ArtworkInfo = {0: "OTHER",
                       1: "FILE_ICON",
                       2: "OTHER_FILE_ICON",
                       3: "COVER_FRONT",
                       4: "COVER_BACK",
                       5: "LEAFLET_PAGE",
                       6: "MEDIA",
                       7: "LEAD_ARTIST",
                       8: "ARTIST",
                       9: "CONDUCTOR",
                       10: "BAND",
                       11: "COMPOSER",
                       12: "LYRICIST",
                       13: "RECORDING_LOCATION",
                       14: "DURING_RECORDING",
                       15: "DURING_PERFORMANCE",
                       16: "SCREEN_CAPTURE",
                       17: "FISH",
                       18: "ILLUSTRATION",
                       19: "BAND_LOGOTYPE",
                       20: "PUBLISHER_LOGOTYPE"
                       }

        Artwork = self.Media.Artwork
        Artwork = {ArtworkInfo.get(keys): values for keys, values in Artwork.items()}
        return Artwork


class MP32:
    def __init__(self, path): ...  # lazy load instance variables

    def CreateWritableFrame(self, frame): ...

    def ConfigureResampler(self, smaplerate, ch_format, dtype): ...

    def RefreshStream(self): ...

    def RefreshArtwork(self): ...

    def RefreshMetadata(self): ...

    @property
    def AudioStream(self): ...

    @AudioStream.setter
    def AudioStream(self, value): ...

    @property
    def Metadata(self): ...

    @Metadata.setter
    def Metadata(self, value): ...

    @property
    def ArtWork(self): ...

    @ArtWork.setter
    def ArtWork(self, value): ...


if __name__ == "__main__":
    import os
    for file in os.listdir("D:\\test_samples"):
        EXT = os.path.splitext(file)[1]
        if MP3.IsFile(EXT):
            try:
                inst = MediaFile(os.path.join(r"D:\test_samples", file))
                print(inst.AudioStream)
            except Exception as e:
                print(os.path.join(r"D:\test_samples", file), e)
            print("---------------------------")
