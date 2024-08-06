from memorylib import Dolphin
from addresses import initializeMemoryAddresses
from api.characters import initializeCharacters

dolphin = Dolphin()

# pitchAttributes = {
#     "curveball_charge": {

#     } 
# }
# do later


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

    def initialize_velocity(self, release_position: Position, target_position: Position, character: ):
        self.X = release_position.X - target_position.X
        self.Y = release_position.Y - target_position.Y
        self.Z = (character.stats['curve_ball_speed'].value)/-240

    def calculateVelocity(self, currFrameBall, curveInput):
        self.X = None # something with curve input, curve speed, and curve control
        self.Y = None # something dependent on pitch speed, air resistance, and other stuff
        self.Z = None # not sure if this even matters

    def returnVelocity(self, currFrameBall, prevFrameBall):
        self.X = currFrameBall.position.X - prevFrameBall.position.X
        self.Y = currFrameBall.position.Y - prevFrameBall.position.Y
        self.Z = currFrameBall.position.Z - prevFrameBall.position.Z

    def applyAirResistance(frame):
        airResistanceVelocityAdjustment = 15
        airResistanceDelay = 20

        




def CurveInput():
    def __init__(self):
        # need to research more
        self.input = None

    def move_pitch(self, direction):
        pass


class Ball():
    def __init__(self):
        self.position = None
        self.velocity = None
        self.curveInput = None


    def initialize_velocity(self, release_position, target_position):
        pass


    def updateBall(self, lastBall):
        pass
        
class Pitch():
    def __init__(self, memoryAddresses):
        self.memoryAddresses = memoryAddresses
        self.ball = None
        self.mound = None
        self.pitchType = None
        self.type = None
        self.frame = None

    def getFrame(self):
        self.frame = self.memoryAddresses['pitch_frame'].read()
        return self.frame

    def pitchCurve(pitcher, ):
        pitcher_stats = pitcher.stats

    def isStrike(self):
        if (0.5 <= self.ball.position.Z <= 1.05):
            if (-0.53 <= self.ball.position.X <= 0.53):
                return True
            else:
                return False
        else:
            return None

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
    


    

        
        





