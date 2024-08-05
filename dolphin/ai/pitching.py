from memorylib import Dolphin
from addresses import initializeMemoryAddresses
from api.characters import initializeCharacters

dolphin = Dolphin()

class Pitching():

    memoryAddresses = initializeMemoryAddresses()
    allCharacters = initializeCharacters()

    def __init__(self):
        self.pitcher = self.memoryAddresses['pitcher_id'].read()
        self.batter = self.memoryAddresses['batter_id'].read()


    def updatePitcher(self):
        self.pitcher = self.memoryAddresses['pitcher_id'].read()
        return self.pitcher
    
    def updateHitter(self):
        self.batter = self.memoryAddresses['batter_id'].read()
        return self.batter

    def move_pitch(self):
        #blah

