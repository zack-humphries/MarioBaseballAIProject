from memorylib import Dolphin
import memorylib
import os
import csv
from api.memory_values import *
import time

dolphin = Dolphin()

def isNoneOrEmpty(var):
    if var == '' or var == None:
        return True
    return False

class MemoryAddress():  

    def __init__(self, name, address, type: str, classtype = None, notes = None):
        if type not in ['int6', 'uint8', 'float', 'int16', 'uint16', 'int32', 'uint32']:
            AssertionError

        self.name = name
        self.address = address
        self.type = type

        if isNoneOrEmpty(classtype):
            self.classtype = None
        else:
            self.classtype = eval(classtype)

        self.notes = notes

    def read(self):
        if dolphin.hook():
            return dolphin.read(self.address, self.type)
        else:
            return Exception
    
    def write(self, value):
        if dolphin.hook():
            return dolphin.write(self.address, self.type, value)
        else:
            return Exception

    def get_dict(self):
        tempValue = self.read()

        if isNoneOrEmpty(self.classtype):
            tempEnumValue = None
        else:
            tempEnumValue = self.classtype(tempValue)
        

        returnDict = {
            'name' : self.name,
            'address' : self.address,
            'type' : self.type,
            'classtype' : self.classtype,
            'value' : tempValue,
            'enumvalue' : tempEnumValue
        }
        return returnDict

def returnFilePath(filename):
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(scriptdir, filename)
    return filepath

def convertValueTypeString(str):
    if str == '':
        return None
    else:
        return eval(str)

def appendMemoryAddresses(csvreader):

    memoryAddresses = {}

    fields = list(next(csvreader))
    data = list(next(csvreader))

    while data is not None:
        if data[0] == '':
            try:
                data = list(next(csvreader))
            except:
                return memoryAddresses
            pass
        else:
            tempMemoryAddress = MemoryAddress(data[0], int(data[1], 16), data[2], data[3], data[4])
            memoryAddresses[data[0]] = tempMemoryAddress
            try:
                data = list(next(csvreader))
            except:
                return memoryAddresses

    return memoryAddresses



def initializeMemoryAddresses():


    # return current filepath (which should contain addresses.csv)
    filepath = returnFilePath("addresses.csv")

    with open(filepath, 'r') as csvfile:

        csvreader = csv.reader(csvfile)

        all_addresses = appendMemoryAddresses(csvreader)

    return all_addresses
 

def main():

    memoryAddresses = initializeMemoryAddresses()

    print(memoryAddresses["desired_mound_position_x"].read())
    memoryAddresses["desired_mound_position_x"].write(-0.2)
    print(memoryAddresses["desired_mound_position_x"].read())

    #for i in range(100):
        
        # time.sleep(0.5)
        # memoryAddresses["score_display_away"].write(5)
        # print(memoryAddresses["score_display_away"].read())
        # time.sleep(0.5)


    #print("--- %s actions per frame ---" % str(1/((time.time() - start)/100 * 60)))

    # dolphin = Dolphin()

    # hand = MemoryAddress('away_score', int('0x808928a7', 16), 'int8')



    # if dolphin.hook():
    #     print(dolphin.read(hand.address, hand.type)) # reading doesn't work but writing does?
    #     print(dolphin.read_int8(hand.address))
    #     #numberOfStrikes.write(1)


if __name__ == '__main__':
    main()