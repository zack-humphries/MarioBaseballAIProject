import enum
import os

@enum.unique
class Start(enum.enum):
    NONE  = 0
    START = 1

@enum.unique
class Button(enum.Enum):
    NONE = 0
    A = 1
    B = 2
    X = 4
    Y = 8

    #BX = 6
    #BY = 'a'

@enum.unique
class Trigger(enum.Enum):
    R = 2
    L = 4

    #LR = 6

class Stick():
    NONE    = [0.5, 0.5, 0]
    left    = [0.0, 0.5, 1]
    right   = [1.0, 0.5, 2]
    down    = [0.5, 0.0, 4]
    up      = [0.5, 1.0, 8]

    upleft = [0.0, 1.0, 9]
    upright = [1.0, 1.0, 'a']
    downleft = [0.0, 0.0, 5]
    downright = [1.0, 0.0, 6]

class Base():
    all     = [0.5, 0.5, 0]
    first   = [1.0, 0.5, 2]
    second  = [0.5, 1.0, 8]
    third   = [0.0, 0.5, 1]
    home    = [0.5, 0.0, 4]

class InputAddress():
    P1Start     = 0x803c77b8 #first byte
    P1Button    = 0x803c77b8 #second byte
    P1Trigger   = 0x803c77b9 #first byte
    P1Stick     = 0x803c77b9 #second byte

    P2Start     = 0x803c77d8 #first byte
    P2Button    = 0x803c77d8 #second byte
    P2Trigger   = 0x803c77d9 #first byte
    P2Stick     = 0x803c77d9 #second byte
