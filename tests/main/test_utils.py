import sys
import os
import pytest

from apollo import ConfigManager, PlayingQueue

@pytest.fixture
def getConfigManager():
    json_dict =  {
        "destination_addresses": [
            "Philadelphia, PA, USA"
        ],
        "origin_addresses": [
            "New York, NY, USA"
        ],

        "rows": {
            "elements": {
            "distance": {
                "text": "94.6 mi",
                "value": 152193
            },
            "duration": {
                "text": "1 hour 44 mins",
                "value": [6227, 1324]
            },
            "status": "OK"
            }
        },
        "status": "OK"
    }
    config_manager = ConfigManager()
    config_manager.config_dict = json_dict
    return json_dict, config_manager

@pytest.fixture
def PQ():
    return PlayingQueue()


class Test_ConfigManager:

    def test_Getvalue(self, getConfigManager):
        Dict, manager = getConfigManager
        assert (Dict == manager.Getvalue(path = ""))
        assert ("94.6 mi" == manager.Getvalue(path = "rows/elements/distance/text"))
        assert ([6227, 1324] == manager.Getvalue(path = "rows/elements/duration/value"))
        assert (False == manager.Getvalue(path = "rows/elements/distance/text_NONE"))


    def test_Setvalue(self, getConfigManager):
        Dict, manager = getConfigManager
        assert (None == manager.Setvalue("TEST", ""))

        manager.Setvalue("TEST", "rows/elements/distance/text")
        assert ("TEST" == manager.Getvalue("rows/elements/distance/text", Dict))

        manager.Setvalue("TEST", "rows/elements/duration/value")
        assert ("TEST" == manager.Getvalue("rows/elements/duration/value", Dict))

        manager.Setvalue([6227, 13224, "TEST"], "rows/elements/duration/value")
        assert ([6227, 13224, "TEST"] == manager.Getvalue("rows/elements/duration/value", Dict))

        manager.Setvalue("TEST", "rows/elements/distance/text_NONE")
        assert ("TEST" == manager.Getvalue("rows/elements/distance/text_NONE", Dict))


class Test_PlayingQueue():

    def test_AddElements(self, PQ):
        PQ.AddElements([0, 1, 2, 3, 4])
        assert ([0, 1, 2, 3, 4] == PQ.GetQueue())

        PQ.AddElements([11, 21, 31, 41], 3)
        assert ([0, 1, 2, 11, 21, 31, 41, 3, 4] == PQ.GetQueue())

        PQ.AddElements([12, 22, 32, 42])
        assert ([0, 1, 2, 11, 21, 31, 41, 3, 4, 12, 22, 32, 42] == PQ.GetQueue())

        PQ.AddElements([13, 23, 33, 43], 18)
        expectedlist = [0, 1, 2, 11, 21, 31, 41, 3, 4, 12, 22, 32, 42, 13, 23, 33, 43]
        assert (expectedlist == PQ.GetQueue())

        PQ.JumpPos(3)
        PQ.AddNext([53, 53, 53, 53])
        expectedlist = [0, 1, 2, 11, 53, 53, 53, 53, 21, 31, 41, 3, 4, 12, 22, 32, 42, 13, 23, 33, 43]
        assert (expectedlist == PQ.GetQueue())

        PQ.RemoveElements()
        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.JumpPos(3)

        PQ.AddElements([11, 12, 13, 14, 15], 3)
        assert (8 == PQ.GetPointer())
        assert (3 == PQ.GetCurrent())

        PQ.AddElements([21, 22, 23, 24, 25], 3)
        assert (13 == PQ.GetPointer())
        assert (3 == PQ.GetCurrent())

    def test_RemoveElements(self, PQ):
        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.RemoveElements(Index = 3)
        assert ([0, 1, 2, 4, 5, 6, 7, 8, 9] == PQ.GetQueue())

        PQ.RemoveElements(Start = 1, End = 4)
        assert ([0, 5, 6, 7, 8, 9] == PQ.GetQueue())

        PQ.RemoveElements(Start = 0, End = 8)
        assert ([] == PQ.GetQueue())

        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.RemoveElements(Start = 3)
        assert ([0, 1, 2] == PQ.GetQueue())


        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.JumpPos(5)

        PQ.RemoveElements(Index = 5)
        assert (0 == PQ.GetPointer())

        PQ.JumpPos(3)
        PQ.RemoveElements(Index = 2)
        assert (2 == PQ.GetPointer())

        PQ.RemoveElements()

        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.JumpPos(5)

        PQ.RemoveElements(Start = 4, End = 7)
        assert ([0, 1, 2, 3, 7, 8, 9] == PQ.GetQueue())
        assert (0 == PQ.GetPointer())

        PQ.JumpPos(5)
        PQ.RemoveElements(Start = 4)
        assert ([0, 1, 2, 3] == PQ.GetQueue())
        assert (0 == PQ.GetPointer())

        PQ.RemoveElements(Start = 0)
        assert ([] == PQ.GetQueue())
        assert (0 == PQ.GetPointer())

        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        PQ.JumpPos(7)
        PQ.RemoveElements(Start = 0, End = 6)
        assert ([6, 7, 8, 9] == PQ.GetQueue())
        assert (1 == PQ.GetPointer())

    def test_IncrementPointer(self, PQ):
        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        PQ.IncrementPointer(9)
        assert (9 == PQ.GetCurrent())

        PQ.JumpPos(0)
        assert (0 == PQ.GetCurrent())

        PQ.IncrementPointer(3)
        assert (3 == PQ.GetCurrent())

        assert (4 == PQ.GetNext())

        PQ.SetCircular(True)
        PQ.IncrementPointer(6)
        assert (0 == PQ.GetCurrent())

        PQ.IncrementPointer(3)
        assert (3 == PQ.GetCurrent())
        PQ.SetCircular(False)

        try:
            PQ.IncrementPointer(9)
        except IndexError:
            assert (True)
        else:
            assert (False)

    def test_DecrementPointer(self, PQ):
        PQ.AddElements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        PQ.IncrementPointer(9)
        assert (9 == PQ.GetCurrent())

        PQ.DecrementPointer(9)
        assert (0 == PQ.GetCurrent())

        PQ.IncrementPointer(9)

        PQ.DecrementPointer(3)
        assert (6 == PQ.GetCurrent())

        assert (5 == PQ.GetPrevious())

        PQ.SetCircular(True)
        PQ.DecrementPointer(6)
        assert (9 == PQ.GetCurrent())

        PQ.DecrementPointer(3)
        assert (6 == PQ.GetCurrent())
        PQ.SetCircular(False)

        try:
            PQ.IncrementPointer(9)
        except IndexError:
            assert (True)
        else:
            assert (False)
