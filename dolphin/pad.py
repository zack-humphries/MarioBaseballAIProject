import enum
import os

@enum.unique
class Start(enum.Enum):
    NONE  = 0
    START = 16

@enum.unique
class Button(enum.Enum):
    NONE = 0
    A = 1
    B = 2
    X = 4
    Y = 8

    #BX = 6
    #BY = 'a'
###################################
@enum.unique
class Trigger(enum.Enum):
    NONE = 0
    Z = 16
    R = 32
    L = 64

    #LR = 6

@enum.unique
class Stick(enum.Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 4
    UP = 8


# class Stick():
#     NONE    = [0.5, 0.5, 0]
#     left    = [0.0, 0.5, 1]
#     right   = [1.0, 0.5, 2]
#     down    = [0.5, 0.0, 4]
#     up      = [0.5, 1.0, 8]

#     upleft = [0.0, 1.0, 9]
#     upright = [1.0, 1.0, 'a']
#     downleft = [0.0, 0.0, 5]
#     downright = [1.0, 0.0, 6]

class Base():
    all     = 0
    first   = 2
    second  = 8
    third   = 1
    home    = 4

class Player1():
    startAddress     = 0x803c77b8 #first byte
    buttonAddress    = 0x803c77b8 #second byte
    triggerAddress   = 0x803c77b9 #first byte
    stickAddress     = 0x803c77b9 #second byte

class Player2():
    startAddress     = 0x803c77d8 #first byte
    buttonAddress    = 0x803c77d8 #second byte
    triggerAddress   = 0x803c77d9 #first byte
    stickAddress     = 0x803c77d9 #second byte


class InputAddress():
    P1Start     = 0x803c77b8 #first byte
    P1Button    = 0x803c77b8 #second byte
    P1Trigger   = 0x803c77b9 #first byte
    P1Stick     = 0x803c77b9 #second byte

    P2Start     = 0x803c77d8 #first byte
    P2Button    = 0x803c77d8 #second byte
    P2Trigger   = 0x803c77d9 #first byte
    P2Stick     = 0x803c77d9 #second byte
