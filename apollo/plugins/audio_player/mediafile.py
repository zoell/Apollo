import json
import os, sys, datetime
from pathlib import Path

from mutagen import easyid3
import mutagen

from apollo.db import DBFIELDS


# FileEXT Support

# ASF  -> No
# FLAC -> Yes
# MP4 -> Yes
# Monkey's Audio -> No
# MP3 -> Yes
# Musepack -> No
# Ogg Opus -> No
# Ogg FLAC -> No
# Ogg Speex -> No
# Ogg Theora -> No
# Ogg Vorbis -> No
# True Audio -> No
# WavPack -> Yes
# OptimFROG -> No
# AIFF -> No


class MP3:
    """
    MP3 File format metadata reader class
    """
    def __init__(self, path):
        self.FILEPATH = path
        self.Metadata = self.GetMetadata()

    def GetMetadata(self):
        Media = mutagen.File(self.FILEPATH, easy = True)
        metadata = dict.fromkeys(DBFIELDS, "")

        for key in Media.keys():
            metadata[key] = Media.get(key, [""])[0]
        metadata["bitrate_mode"] = str(Media.info.bitrate_mode).replace('BitrateMode', "").replace('.', "")
        metadata['album_gain'] = Media.info.album_gain
        metadata['encoder_info'] = Media.info.encoder_info
        metadata['encoder_settings'] = Media.info.encoder_settings
        metadata['frame_offset'] = Media.info.frame_offset
        metadata['layer'] = Media.info.layer
        metadata['mode'] = Media.info.mode
        metadata['padding'] = Media.info.padding
        metadata['protected'] = Media.info.protected
        metadata['track_gain'] = Media.info.track_gain
        metadata['track_peak'] = Media.info.track_peak
        metadata['version'] = Media.info.version
        metadata['sample_rate'] = f"{Media.info.sample_rate}Hz"
        metadata["length"] = str(datetime.timedelta(seconds = Media.info.length))
        metadata["bitrate"] = f"{int(Media.info.bitrate / 1000)} Kbps"
        metadata['channels'] = Media.info.channels
        metadata["filesize"] = f"{round(os.path.getsize(Media.filename) * 0.00000095367432, 2)} Mb"
        metadata["file_name"] = os.path.split(Media.filename)[1]
        metadata["file_path"] = Media.filename
        metadata["rating"] = 0
        metadata["playcount"] = 0
        return metadata

    def GetArtwork(self):
        Media = mutagen.File(self.FILEPATH)
        Artwork = Media.tags.getall("APIC:")
        Artwork = {int(data.type): data.data for data in Artwork}
        return Artwork


class WAVE:
    """
    WAVE File format metadata reader class
    """
    def __init__(self, path):
        self.FILEPATH = path
        self.Metadata = self.GetMetadata()

    def GetMetadata(self):
        Media = easyid3.EasyID3FileType(self.FILEPATH)
        metadata = dict.fromkeys(DBFIELDS, "")

        for key in Media.keys():
            metadata[key] = Media.get(key, [""])[0]

        Media = mutagen.File(self.FILEPATH, easy = True)
        metadata['sample_rate'] = f"{Media.info.sample_rate}Hz"
        metadata["length"] = str(datetime.timedelta(seconds = Media.info.length))
        metadata["bitrate"] = f"{int(Media.info.bitrate / 1000)} Kbps"
        metadata['channels'] = Media.info.channels
        metadata["filesize"] = f"{round(os.path.getsize(Media.filename) * 0.00000095367432, 2)} Mb"
        metadata["file_name"] = os.path.split(Media.filename)[1]
        metadata["file_path"] = Media.filename
        metadata["rating"] = 0
        metadata["playcount"] = 0
        return metadata

    def GetArtwork(self):
        Media = mutagen.File(self.FILEPATH)
        Artwork = Media.tags.getall("APIC:")
        Artwork = {int(data.type): data.data for data in Artwork}
        return Artwork


class FLAC:
    """
    FLAC File format metadata reader class
    """
    def __init__(self, path):
        self.FILEPATH = path
        self.Metadata = self.GetMetadata()

    def GetMetadata(self):
        Media = mutagen.File(self.FILEPATH, easy = True)
        metadata = dict.fromkeys(DBFIELDS, "")

        for key in Media.keys():
            metadata[key] = Media.get(key, [""])[0]

        metadata['encoder_info'] = Media.get("encoder", [""])[0]
        metadata['sample_rate'] = f"{Media.info.sample_rate}Hz"
        metadata["length"] = str(datetime.timedelta(seconds = Media.info.length))
        metadata["bitrate"] = f"{int(Media.info.bitrate / 1000)} Kbps"
        metadata['channels'] = Media.info.channels
        metadata["filesize"] = f"{round(os.path.getsize(Media.filename) * 0.00000095367432, 2)} Mb"
        metadata["file_name"] = os.path.split(Media.filename)[1]
        metadata["file_path"] = Media.filename
        metadata["rating"] = 0
        metadata["playcount"] = 0
        return metadata

    def GetArtwork(self):
        Media = mutagen.File(self.FILEPATH)
        Artwork = Media.pictures
        Artwork = {int(data.type): data.data for data in Artwork}
        return Artwork

class MP4:
    """
    MP4 File format metadata reader class
    """
    def __init__(self, path):
        self.FILEPATH = path
        self.Metadata = self.GetMetadata()

    def GetMetadata(self):
        Media = mutagen.File(self.FILEPATH, easy = True)
        metadata = dict.fromkeys(DBFIELDS, "")

        for key in Media.keys():
            metadata[key] = Media.get(key, [""])[0]
        metadata['encoder_info'] = Media.info.codec_description
        metadata['encoder_settings'] = Media.info.codec
        metadata['sample_rate'] = f"{Media.info.sample_rate}Hz"
        metadata["length"] = str(datetime.timedelta(seconds = Media.info.length))
        metadata["bitrate"] = f"{int(Media.info.bitrate / 1000)} Kbps"
        metadata['channels'] = Media.info.channels
        metadata["filesize"] = f"{round(os.path.getsize(Media.filename) * 0.00000095367432, 2)} Mb"
        metadata["file_name"] = os.path.split(Media.filename)[1]
        metadata["file_path"] = Media.filename
        metadata["rating"] = 0
        metadata["playcount"] = 0
        return metadata

    def GetArtwork(self):
        Media = mutagen.File(self.FILEPATH)
        Artwork = Media.tags.get("covr")
        Artwork = {3: data for data in Artwork}
        return Artwork

# @exe_time
class MediaFile(dict):

    def __init__(self, file: str):
        file = Path(file)
        if not os.path.isfile(file):
            raise FileNotFoundError()

        EXT = os.path.splitext(file)[1].upper().replace(".", "")
        if EXT in ["MP3"]:
            self.Media = MP3(file)
        elif EXT in ["WAV"]:
            self.Media = WAVE(file)
        elif EXT in ["FLAC"]:
            self.Media = FLAC(file)
        elif EXT in ["M4A"]:
            self.Media = MP4(file)
        else:
            raise Exception(f"{EXT}: File Format Not Implemented")

    def __getitem__(self, key):
        return self.Media.Metadata.get(key, '')

    def get(self, key):
        return self.Media.Metadata.get(key, '')

    def __repr__(self):
        return json.dumps(self.Media.Metadata, indent = 2)

    def __str__(self):
        return json.dumps(self.Media.Metadata, indent = 2)

    def getMetadata(self):
        return self.Media.GetMetadata()

    def getArtwork(self):
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

        Artwork = self.Media.getArtwork()
        Artwork = {ArtworkInfo.get(keys):values  for keys, values in Artwork.items()}
        return Artwork


if __name__ == "__main__":
    inst = MediaFile("D:\\music\\cantstopohn.mp3")

