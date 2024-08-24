import math
from pitching import *
from addresses import initializeMemoryAddresses
from characters import initializeCharacters

class Interpreter():
    def __init__(self):
        self.initializer = Initializer()
        self.pitcher = Pitcher(self.initializer)
        self.pitchType = None
        self.pitchChargeUp = None
        self.pitch = None
        self.pitchInAir = None
        self.pitchFramesInAir = None
        self.pitchIsInControl = False
        self.pitchTrajectory = None


    def updatePitcher(self):
        self.pitcher = Pitcher(self.initializer)

    def isPitchInAir(self):
        pitchState = self.initializer.getMemoryAddressValue('pitch_duration')
        if pitchState != 255 or pitchState != -1:
            self.pitchInAir = True
        else: 
            self.pitchInAir = False
        return self.pitchInAir
    
    def returnPitchFramesInAir(self):
        pitchState = self.initializer.getMemoryAddressValue('pitch_duration')
        if pitchState != 255 or pitchState != -1:
            self.pitchFramesInAir = pitchState
            return pitchState
        self.pitchFramesInAir = None
        return None
    
    def initializePitchTypeAndCharge(self):
        pitchID = self.initializer.getMemoryAddressValue('pitch_type')
        chargeUp = 0
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
    
    def initializePitch(self):
        [pitchType, pitchChargeUp] = self.initializePitchTypeAndCharge()
        self.pitch = Pitch(self.initializer, self.pitcher, pitchType, pitchChargeUp)
        return self.pitch
    
    def returnIsInControl(self):
        self.pitchIsInControl = bool(self.initializer.getMemoryAddressValue('pitch_is_in_control'))
        return self.pitchIsInControl

    def initializePitchTrajectory(self):
        self.pitchTrajectory = PitchTrajectory(self.pitch)

    
    def move(self, direction, frameCount = 0):
        while(not self.pitchIsInControl):
            self.returnIsInControl()
            self.applyChanges(0)

        if direction in ['left', 'L']:
            self.pitchTrajectory.calculateNextFrame([-1]*frameCount)
        elif direction in ['right', 'R']:
            self.pitchTrajectory.calculateNextFrame([1]*frameCount)
        else:
            self.pitchTrajectory.calculateNextFrame([0]*frameCount)

        
            
def main():
    ai = Interpreter()

    pitchframeCount = 0
    flag = 0
    while(True):
        if ai.isPitchInAir() and not flag:
            ai.initializePitch()
            flag = 1
            pitchframeCount += 1
        elif ai.isPitchInAir() and flag and (pitchframeCount == ai.returnPitchFramesInAir()):
            pitchframeCount += 1
        elif ai.pitchIsInControl():
            while(ai.pitchIsInControl()):
                if (pitchframeCount == ai.returnPitchFramesInAir()):
                    ai.move('left')
                    pitchframeCount += 1

    

    