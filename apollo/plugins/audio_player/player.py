import time, os, threading, datetime
from pprint import pprint

import pyo, av

from apollo import PlayingQueue

if __name__ == "__main__":
    Queue = PlayingQueue()
    Player = PlayBack_Interface(Queue).ServerBootUp()
    # Player.play("D:\\music\\cantstopohn.mp3")
    Player.Gui()