import math
from pitching import *
from addresses import initializeMemoryAddresses
from characters import initializeCharacters
from memory_values import *

dolphin = Dolphin()

class Interpreter():
    def __init__(self):
        self.initializer = Initializer()
        self.pitcher = Pitcher(self.initializer)
        self.batter = Batter(self.initializer)
        self.pitchType = None
        self.pitchChargeUp = None
        self.pitch = None
        self.pitchInAir = None
        self.pitchFramesInAir = None
        self.pitchIsInControl = False
        self.pitchTrajectory = None

        self.X = None
        self.Y = None
        self.Z = None


    def updatePitcher(self):
        self.pitcher = Pitcher(self.initializer)

    def updateBatter(self):
        self.batter = Batter(self.initializer)

    def isPitchInAir(self):
        pitchState = self.initializer.getMemoryAddressValue('pitch_state')
        if pitchState == 3:
            self.pitchInAir = True
        else: 
            self.pitchInAir = False
        return self.pitchInAir
    
    def returnPitchState(self):
        return self.initializer.getMemoryAddressValue('pitch_state')
    
    def returnPitchFramesInAir(self, pitchState):
        if pitchState == 3:
            pitchFramesInAir = self.initializer.getMemoryAddressValue('pitch_state_frame')
            return pitchFramesInAir
        return None
    
    def initializePitchTypeAndCharge(self, chargeUp = 0):
        pitchID = self.initializer.getMemoryAddressValue('pitch_type')
        if pitchID == 0:
            self.pitchType = 'curve'
            self.pitchChargeUp = chargeUp
        elif pitchID == 2:
            self.pitchType = 'change'
            self.pitchChargeUp = chargeUp
        elif pitchID == 1:
            chargeUp = self.initializer.getMemoryAddressValue('pitch_charge')
            if chargeUp > 0.85:
                self.pitchType = 'perfect'
                self.pitchChargeUp = chargeUp
            else:
                self.pitchType = 'charge'
                self.pitchChargeUp = chargeUp
        else:
            return None
        return [self.pitchType, self.pitchChargeUp]
    
    def returnMoundPositionX(self):
        return self.initializer.getMemoryAddressValue('pitcher_mound_position_x')
    
    def returnBatterPositionX(self):
        return self.initializer.getMemoryAddressValue('batter_position_x')
        
    
    def initializePitch(self):
        [pitchType, pitchChargeUp] = self.initializePitchTypeAndCharge()
        self.pitch = PitchProperties(self.initializer, self.pitcher, pitchType, pitchChargeUp)
        return self.pitch
    
    def initializeCurvePitch(self):
        self.pitch = PitchProperties(self.initializer, self.pitcher, 'curve', 0)
        return self.pitch
    
    def returnIsInControl(self):
        pitchIsInControl = self.initializer.getMemoryAddressValue('pitch_is_in_control')
        if pitchIsInControl == 1 and self.isPitchInAir():
            self.pitchIsInControl = True
        else:
            self.pitchIsInControl = False
        return self.pitchIsInControl


    def initializePitchTrajectory(self, pitch):
        self.pitchTrajectory = PitchXYZ(pitch)
        [self.Y, self.Z] = self.pitchTrajectory.returnPositionYZ()
        self.X = self.pitchTrajectory.initializeXBufferPositions()

    

    
    def movePitch(self, direction, frameCount = 1):
        # while(not self.pitchIsInControl):
        #     self.returnIsInControl()

        for i in range(frameCount):
            frameX = self.pitchTrajectory.frameX
            try:
                if direction in ['left', 'L', -1]:
                    self.X[frameX] = self.pitchTrajectory.returnNextPositionX(-1, self.X[frameX-1])
                elif direction in ['right', 'R', 1]:
                    self.X[frameX] = self.pitchTrajectory.returnNextPositionX(1, self.X[frameX-1])
                else:
                    self.X[frameX] = self.pitchTrajectory.returnNextPositionX(0, self.X[frameX-1])
            except:
                pass

    def applyMove(self, input):

        direction = 998244353

        if input in ['left', 'L', -1]:
            direction = 998309887
        elif direction in ['right', 'R', 1]:
            direction = 998244352

        self.initializer.updateMemoryAddressValue('pitch_move', direction)

    def setBallPosition(self, X, Y = None, Z = None):
        self.initializer.updateMemoryAddressValue('ball_position_x', X)
        if Y: self.initializer.updateMemoryAddressValue('ball_position_z', Y)
        if Z: self.initializer.updateMemoryAddressValue('ball_position_y', Z)


def pitchAI(ai: Interpreter, function):
    pitch = ai.initializeCurvePitch()
    ai.initializePitchTrajectory(pitch)
    frameCount = 0
    input = 'S'


    while True:
        pitchInAir = ai.returnPitchState()
        if pitchInAir == 3:
            pitchFramesInAir = ai.returnPitchFramesInAir(pitchInAir)
            if pitchFramesInAir >= frameCount:
                frameAdvance = pitchFramesInAir - frameCount + 1
                input = function(ai, frameCount)
                print(f'{pitchFramesInAir}/{frameCount}: {ai.X[frameCount]}, {ai.Y[frameCount]}, {input}, {frameAdvance}')
                ai.movePitch(input, frameAdvance)
                frameCount += frameAdvance
            try:
                ai.setBallPosition(ai.X[frameCount], ai.Y[frameCount], ai.Z[frameCount])
            except IndexError:
                pass
        else:
            frameCount = 0
            ai.updatePitcher()
            pitch = ai.initializeCurvePitch()
            ai.initializePitchTrajectory(pitch)


        
            
def main():
    ai = Interpreter()

    def pitchLogic(ai: Interpreter, frameCount):
        edge = 2.6
        near = 1.3
        center = (edge+near)/2

        batterPosition = abs(ai.returnBatterPositionX())
        batterHand = ai.batter.batterHand
        mult = 0
        if batterHand == 0:
            mult = 1
        else:
            mult = -1

        if (batterPosition < center) and (-0.5 < ai.X[frameCount]):
            input = -1
        else:
            input = 1

        return input*mult
    

    pitchAI(ai, pitchLogic)
        

        




        

    

if __name__ == '__main__':
    main()


    