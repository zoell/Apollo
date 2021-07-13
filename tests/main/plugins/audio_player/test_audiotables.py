import pytest
from unittest.mock import Mock

from apollo.plugins.audio_player.audiotables import Buffer_Info

@pytest.fixture
def getBuffer_Info_Uniform():
    return Buffer_Info(Time_ActualSize = 10, Time_VirtualSize = 10)


class Test_Buffer_Info:

    def test_CalculatePoint(self, getBuffer_Info_Uniform: Buffer_Info):
        Obj = getBuffer_Info_Uniform
        time = 10
        assert time == int(Obj.TIMEBASE_SEC * (Obj.CalculateFrame(pts = Obj.CalculatePoint(time = time))))

    def test_CalculateFrame(self, getBuffer_Info_Uniform: Buffer_Info):
        Obj = getBuffer_Info_Uniform
        time = 10
        assert time == int(Obj.TIMEBASE_SEC * (Obj.CalculateFrame(time = time)))

    def test_IsWritten_1(self, getBuffer_Info_Uniform: Buffer_Info):
        """
        Checks for Normal Frames in a Buffer
        """
        Obj = getBuffer_Info_Uniform
        Obj.FrameWrite(200)
        packet = Mock(pts = Obj.CalculatePoint(Obj.TIMEBASE_SEC * 200))
        assert (Obj.IsWritten(packet))

    def test_IsWritten_2(self, getBuffer_Info_Uniform: Buffer_Info):
        """
        Checks for if a new frame is queried, if not present is added or else normal operation
        """
        Obj = getBuffer_Info_Uniform
        packet = Mock(pts = Obj.CalculatePoint(Obj.TIMEBASE_SEC * Obj.CalculateFrame(time = 11)))
        assert not (Obj.IsWritten(packet))
        assert Obj.ActualBuffer[Obj.CalculateFrame(time = 11)] == False

    def test_IsWritten_3(self, getBuffer_Info_Uniform: Buffer_Info):
        """
        Checks for if a new frame is queried, if not present is added or else normal operation
        """
        Obj = getBuffer_Info_Uniform
        Obj.FrameWrite(200)
        assert (Obj.IsWritten(frame = Obj.CalculateFrame(time = Obj.TIMEBASE_SEC * 200)))

    def test_FrameWrite_1(self, getBuffer_Info_Uniform: Buffer_Info):
        Obj = getBuffer_Info_Uniform
        Obj.FrameWrite(200)
        packet = Mock(pts = Obj.CalculatePoint(Obj.TIMEBASE_SEC * 200))
        assert (Obj.IsWritten(packet))

    def test_UpdateVirtualBuffer(self, getBuffer_Info_Uniform: Buffer_Info):
        Obj = getBuffer_Info_Uniform
        Obj.Update_VirtualBuffer(0)  # insert at start
        assert Obj.VirtualBuffer[0] == 0

        Obj.VirtualCursor = len(Obj.VirtualBuffer) - 1
        Obj.Update_VirtualBuffer(1)  # insert at end
        assert Obj.VirtualBuffer[len(Obj.VirtualBuffer) - 1] == 1

        Obj.Update_VirtualBuffer(2)  # insert more than end, wrap
        assert Obj.VirtualBuffer[0] == 2
