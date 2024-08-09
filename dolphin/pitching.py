from memorylib import Dolphin
from addresses import initializeMemoryAddresses
from characters import initializeCharacters
import memory_values
#from pitching_calculations import pitchBaseReleaseCoordinates

dolphin = Dolphin()

pitchBaseReleaseCoordinates = {
    'Mario':       {'curve': {'X': -0.358750939,    'Z': 2.9281559,     'Y': 17.6997108},       'charge': {'X': -0.370488256,   'Z': 2.83268118,    'Y': 17.872982}},
    'Luigi':       {'curve': {'X': 0.221170574,     'Z': 2.30373907,    'Y': 18.0957241},       'charge': {'X': -0.253166497,   'Z': 2.7028234,     'Y': 17.5246811}},
    'DK':          {'curve': {'X': -2.04435539,     'Z': 2.03053284,    'Y': 16.223959},        'charge': {'X': -2.04427075,    'Z': 2.03053284,    'Y': 16.2238922}},
    'Diddy':       {'curve': {'X': -0.484804153,    'Z': 2.21302128,    'Y': 18.831337},        'charge': {'X': -0.422204643,   'Z': 2.27686,       'Y': 19.3343658}},
    'Peach':       {'curve': {'X': -0.0703445852,   'Z': 2.16658092,    'Y': 18.1502056},       'charge': {'X': -0.131633073,   'Z': 2.19204974,    'Y': 19.2481537}},
    'Daisy':       {'curve': {'X': -0.281522155,    'Z': 1.16270649,    'Y': 17.975111},        'charge': {'X': -0.462917864,   'Z': 0.998229444,   'Y': 17.4418068}},
    'Yoshi':       {'curve': {'X': -0.0526904576,   'Z': 1.73863459,    'Y': 17.0554199},       'charge': {'X': -0.102338329,   'Z': 1.74589205,    'Y': 17.2527218}},
    'BabyMario':   {'curve': {'X': -0.294910491,    'Z': 0.501412511,   'Y': 17.8377438},       'charge': {'X': -0.293749392,   'Z': 1.67534804,    'Y': 18.0460491}},
    'BabyLuigi':   {'curve': {'X': -0.100495219,    'Z': 1.24129128,    'Y': 17.8929539},       'charge': {'X': -0.204690278,   'Z': 1.14138937,    'Y': 18.3971405}},
    'Bowser':      {'curve': {'X': -1.1208117,      'Z': 2.37041189,    'Y': 17.7443905},       'charge': {'X': -0.935231805,   'Z': 2.83790755,    'Y': 17.9320602}},
    'Wario':       {'curve': {'X': -0.218430877,    'Z': 2.11808395,    'Y': 18.0982456},       'charge': {'X': -0.387497813,   'Z': 2.14200447,    'Y': 18.0287138}},
    'Waluigi':     {'curve': {'X': -0.0994037464,   'Z': 2.91129541,    'Y': 16.6599312},       'charge': {'X': -0.0872518569,  'Z': 2.91058898,    'Y': 16.6630745}},
    'KoopaR':      {'curve': {'X': -0.0643017143,   'Z': 1.38116789,    'Y': 18.2691517},       'charge': {'X': -0.0115943998,  'Z': 1.42475438,    'Y': 18.2572403}},
    'ToadR':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'Boo':         {'curve': {'X': -0.976979315,    'Z': 2.43798327,    'Y': 16.8721886},       'charge': {'X': -1.05723453,    'Z': 3.21649265,    'Y': 17.1067276}},
    'Toadette':    {'curve': {'X': -0.432494819,    'Z': 1.53251338,    'Y': 17.9790344},       'charge': {'X': -0.442466974,   'Z': 0.960499167,   'Y': 18.0559368}},
    'ShyGuyR':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'Birdo':       {'curve': {'X': -0.408602893,    'Z': 0.954139769,   'Y': 18.4027977},       'charge': {'X': -0.185714141,   'Z': 0.965393066,   'Y': 18.973381}},
    'Monty':       {'curve': {'X': -0.392196894,    'Z': 1.25717086,    'Y': 15.9324245},       'charge': {'X': -0.337694883,   'Z': 1.46883655,    'Y': 15.9852085}},
    'BowserJr':    {'curve': {'X': -1.17502844,     'Z': 0.908061326,   'Y': 18.7266293},       'charge': {'X': -0.954403996,   'Z': 1.51448655,    'Y': 18.1687946}},
    'ParatroopaR': {'curve': {'X': -0.0549990535,   'Z': 2.26200676,    'Y': 18.3726215},       'charge': {'X': 0.0554796606,   'Z': 2.54858708,    'Y': 18.4819603}},
    'PiantaB':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'PiantaR':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'PiantaY':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'NokiB':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'NokiR':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'NokiG':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'BroH':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
    'Toadsworth':  {'curve': {'X': -0.645938098,    'Z': 0.680195332,   'Y': 18.2057915},       'charge': {'X': -0.0759834051,  'Z': 1.17852771,    'Y': 18.0417519}},
    'ToadB':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadY':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadG':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadP':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'MagikoopaB':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaR':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaG':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaY':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'KingBoo':     {'curve': {'X': -1.19448996,     'Z': 2.59314823,    'Y': 16.9215889},       'charge': {'X': -1.27474511,    'Z': 3.37165785,    'Y': 17.1561279}},
    'Petey':       {'curve': {'X': -0.541439176,    'Z': 1.78280687,    'Y': 17.56321},         'charge': {'X': -1.13070774,    'Z': 1.67450738,    'Y': 17.7182236}},
    'Dixie':       {'curve': {'X': -1.3091619,      'Z': 1.27092195,    'Y': 18.7103424},       'charge': {'X': -0.379683375,   'Z': 1.10366392,    'Y': 18.385828}},
    'Goomba':      {'curve': {'X': -0.294719875,    'Z': 1.01028323,    'Y': 17.451561},        'charge': {'X': -0.729693174,   'Z': 0.665731907,   'Y': 18.527298}},
    'Paragoomba':  {'curve': {'X': -0.795248866,    'Z': 2.18529749,    'Y': 18.4609985},       'charge': {'X': -0.7055155504,  'Z': 3.25615358,    'Y': 18.637495}},
    'KoopaG':      {'curve': {'X': -0.0643017143,   'Z': 1.38116789,    'Y': 18.2691517},       'charge': {'X': -0.0115943998,  'Z': 1.42475438,    'Y': 18.2572403}},
    'ShyGuyB':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyY':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyG':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyBk':    {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'DryBonesGy':  {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesG':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesR':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesB':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'BroF':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
    'BroB':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
}

pitchAirResistance = {'curve': {'velocityAdjustment': 15, 'delay': 20}}


# pitchAttributes = {
#     "curveball_charge": {

#     } 
# }
# do later

# Interpreter class to initialize values and allow values to be pulled
class Initializer():
    def __init__(self):
        self.memoryAddresses = initializeMemoryAddresses()
        self.characters = initializeCharacters()
    
    def getMemoryAddressValue(self, varname: str):
        return self.memoryAddresses[varname].read()
    
    def updateMemoryAddressValue(self, varname: str, value):
        return self.memoryAddresses[varname].write(value)
    
    def getCharacterStat(self, char, varname: str):
        return self.characters[char].stats[varname].value
    
    def getCharacterAllStats(self, char):
        return self.characters[char].stats
    
    def updateCharacterStat(self, char, varname: str, value):
        self.characters[char].stats[varname].value = value
        return self.characters[char].stats[varname].value


# Basic position, velocity, and acceleration classes
class Position():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, velocity):
        self.X += velocity.X
        self.Y += velocity.Y
        self.Z += velocity.Z

    def prnt(self):
        print("(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")")

class Velocity():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, acceleration):
        self.X += acceleration.X
        self.Y += acceleration.Y
        self.Z += acceleration.Z

    def prnt(self):
        print("(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")")

class Acceleration():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, new_acceleration):
        self.X = new_acceleration.X
        self.Y = new_acceleration.Y
        self.Z = new_acceleration.Z

    def prnt(self):
        print("(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")")

# Ball comprises of position, velocity, and acceleration
class Ball():
    def __init__(self, position: Position, velocity: Velocity, acceleration: Acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self, newAcceleration = None):
        self.position.update(self.velocity)
        self.velocity.update(self.acceleration)
        if newAcceleration:
            self.acceleration.update(newAcceleration)

class Mound():
    def __init__(self, position: Position, velocity: Velocity, acceleration: Acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self, newAcceleration = None):
        self.position.update(self.velocity)
        self.velocity.update(self.acceleration)
        if newAcceleration:
            self.acceleration.update(newAcceleration)


# Pitcher contains pitcher info
class Pitcher():
    def __init__(self, initializer: Initializer):

        self.pitcher_id = initializer.getMemoryAddressValue('pitcher_id')
        self.pitcher = str(memory_values.CharacterID(self.pitcher_id).name)
        self.pitcherHand = initializer.getMemoryAddressValue('pitcher_hand')
        initializer.updateCharacterStat(self.pitcher, 'fielding_arm', self.pitcherHand)
        self.pitcherStats = initializer.getCharacterAllStats(self.pitcher)



class Pitch():

    def __init__(self, pitcher: Pitcher, initializer: Initializer):

        def returnBasePosition(pitcher: Pitcher, type: str):
            tempbase = pitchBaseReleaseCoordinates[pitcher.pitcher][type]
            if pitcher.pitcherHand == 1:
                baseReleasePosition = Position(-1*tempbase['X'], tempbase['Y'], tempbase['Z'])
            else:
                baseReleasePosition = Position(tempbase['X'], tempbase['Y'], tempbase['Z'])
            return baseReleasePosition
        
        def returnPitchSpeed(char: str, type: str):
            return initializer.getCharacterStat(char, type + "_ball_speed")
        
        def add(obj1, obj2):
            obj1.X += obj2.X
            obj1.Y += obj2.Y
            obj1.Z += obj2.Z
            return obj1
        
        def subtract(obj1, obj2):
            obj1.X += obj2.X
            obj1.Y += obj2.Y
            obj1.Z += obj2.Z
            return obj1

        # Establish release position
        self.baseReleasePosition = returnBasePosition(pitcher, 'curve')
        self.moundPositionDiff = Position(initializer.getMemoryAddressValue('pitcher_mound_position_x'), 0, 0)
        self.initialPosition = add(self.baseReleasePosition, self.moundPositionDiff)

        # I personally don't like the XYZ structure. Swap Z for Y
        frontOfPlateY = 0.5 * (1.05 + 0.5)
        initialVelocityY = returnPitchSpeed(pitcher.pitcher, 'curve')/-240
        initialVelocityX = ((self.moundPositionDiff.X * initialVelocityY) / (self.initialPosition.Y - frontOfPlateY))
        
        # Adjust for bat height self.initialPosition.Z - self.batHeight.Z
        initialVelocityZ = ((self.initialPosition.Z * initialVelocityY) / (self.initialPosition.Y - frontOfPlateY))

        self.initialVelocity = Velocity(initialVelocityX, initialVelocityY, initialVelocityZ)
        self.initialAcceleration = Acceleration(0, 0, 0)

        self.ball = Ball(self.initialPosition, self.initialVelocity, self.initialAcceleration)
        #self.mound = Mound(blah, blah, blah)

        


    

def main():
    initializer = Initializer()
    pitcher = Pitcher(initializer)
    pitch = Pitch(pitcher, initializer)

    print(initializer.getMemoryAddressValue('pitcher_mound_position_x'))
    pitch.initialPosition.prnt()
    pitch.initialVelocity.prnt()

    # print(info.getMemoryAddressValue('pitcher_id'))
    #print(pitchBaseReleaseCoordinates['Mario']['curve'])



if __name__ == '__main__':
    main()




# class Pitching():
#     memoryAddresses = initializeMemoryAddresses()
#     allCharacters = initializeCharacters()

#     def __init__(self):
#         self.pitcher = self.memoryAddresses['pitcher_id'].read()
#         self.batter = self.memoryAddresses['batter_id'].read()
#         self.pitch = None
        
#     def updatePitcher(self):
#         self.pitcher = self.memoryAddresses['pitcher_id'].read()
#         return self.pitcher
    
#     def updateHitter(self):
#         self.batter = self.memoryAddresses['batter_id'].read()
#         return self.batter
    
#     def updatePitchType(self):
#         self.pitchType = self.memoryAddresses['pitch_type'].read()
#         return self.pitchType


# class Position():
#     def __init__(self):
#         self.X = None
#         self.Y = None
#         self.Z = None

#     def update(self, velocity):
#         self.X = self.X + velocity.X
#         self.Y = self.Y + velocity.Y
#         self.Z = self.Z + velocity.Z

# class Velocity():
#     def __init__(self):
#         self.X = None
#         self.Y = None
#         self.Z = None

#     def update(self, prevPosition, currPosition):

# class Velocity():
#     def __init__(self):
#         self.X = None
#         self.Y = None
#         self.Z = None

#     def initialize_velocity(self, release_position: Position, target_position: Position, character: ):
#         self.X = release_position.X - target_position.X
#         self.Y = release_position.Y - target_position.Y
#         self.Z = (character.stats['curve_ball_speed'].value)/(-240)

#     def calculateVelocity(self, currFrameBall, curveInput):
#         self.X = None # something with curve input, curve speed, and curve control
#         self.Y = None # something dependent on pitch speed, air resistance, and other stuff
#         self.Z = None # not sure if this even matters. jk it does

#     def returnVelocity(self, currFrameBall, prevFrameBall):
#         self.X = currFrameBall.position.X - prevFrameBall.position.X
#         self.Y = currFrameBall.position.Y - prevFrameBall.position.Y
#         self.Z = currFrameBall.position.Z - prevFrameBall.position.Z

#     def applyAirResistance(frame):
#         #example code. idk how it works
#         airResistanceVelocityAdjustment = 15
#         airResistanceDelay = 20


# def CurveInput():
#     def __init__(self):
#         # need to research more
#         self.input = None

#     def move_pitch(self, direction):
#         pass


# class Ball():
#     def __init__(self):
#         self.position = None
#         self.velocity = None
#         self.curveInput = None

#     def initialize_velocity(self, release_position, target_position):
#         pass

#     def updateBall(self, lastBall):
#         pass

        
# class Pitch(Pitching):
#     def __init__(self, memoryAddresses):
#         self.memoryAddresses = memoryAddresses
#         self.ball = None
#         self.pitchType = None
#         self.type = None
#         self.frame = None
#         self.mound = None

#     def getFrame(self):
#         self.frame = self.memoryAddresses['pitch_frame'].read()
#         return self.frame

#     def pitchCurve(pitcher, ):
#         pitcher_stats = pitcher.stats

#     def isStrike(self):
#         if (0.5 <= self.ball.position.Z <= 1.05):
#             if (-0.53 <= self.ball.position.X <= 0.53):
#                 return True
#             else:
#                 return False
#         else:
#             return None

# class Mound():
#     def __init__(self, memoryAddresses):
#         self.memoryAddresses = memoryAddresses
#         self.moundPosition = None

#     def updateMoundPosition(self):
#         self.moundPosition = self.memoryAddresses['pitcher_mound_position_x'].read()
#         return self.moundPosition

    
    

# def setupPitching():
#     pitching = Pitching()
#     pitching.pitch = Pitch(pitching.memoryAddresses)
#     pitching.pitch.mound = Mound(pitching.memoryAddresses)
#     pitching.pitch.ball = Ball(pitching.memoryAddresses)
    



    

        





