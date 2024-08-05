from memorylib import Dolphin
from addresses import initializeMemoryAddresses
from api.characters import initializeCharacters

dolphin = Dolphin()

class Position():
    def __init__(self):
        self.X = None
        self.Y = None
        self.Z = None

    def updatePosition(self, velocity):
        self.X = self.X + velocity.X
        self.Y = self.Y + velocity.Y
        self.Z = self.Z + velocity.Z

def Velocity():
    def __init__(self):
        self.X = None
        self.Y = None
        self.Z = None

    def calculateVelocity(self, currFrameBall, curveInput):
        self.X = None # something with curve input, curve speed, and curve control
        self.Y = None # something dependent on pitch speed, air resistance, and other stuff
        self.Z = None # not sure if this even matters

    def returnVelocity(self, currFrameBall, prevFrameBall):
        self.X = currFrameBall.position.X - prevFrameBall.position.X
        self.Y = currFrameBall.position.Y - prevFrameBall.position.Y
        self.Z = currFrameBall.position.Z - prevFrameBall.position.Z


def CurveInput():
    def __init__(self):
        # need to research more
        self.input = None

class Ball():
    def __init__(self):
        self.position = None
        self.velocity = None
        self.curveInput = None

    def updateBall(self, lastBall):
        


class Pitch():
    def __init__(self, memoryAddresses):
        self.memoryAddresses = memoryAddresses
        self.ball = None
        self.mound = None
        self.pitchType = None
        self.frame = None

    def getFrame(self):
        self.frame = self.memoryAddresses['pitch_frame'].read()
        return self.frame


        
        



class Pitching():

    memoryAddresses = initializeMemoryAddresses()
    allCharacters = initializeCharacters()

    def __init__(self, pitch: Pitch):
        self.pitcher = self.memoryAddresses['pitcher_id'].read()
        self.batter = self.memoryAddresses['batter_id'].read()
        self.pitch = pitch
        

    def updatePitcher(self):
        self.pitcher = self.memoryAddresses['pitcher_id'].read()
        return self.pitcher
    
    def updateHitter(self):
        self.batter = self.memoryAddresses['batter_id'].read()
        return self.batter
    
    def updatePitchType(self):
        self.pitchType = self.memoryAddresses['pitch_type'].read()
        return self.pitchType

    

    def move_pitch(self, direction):
        #blah


