import memorylib
from memorylib import Dolphin
import os
import csv
from memory_values import *
import time

dolphin = Dolphin()

# checks if variable is None or empty string
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

        # assert classtype if member of enum class in memory_values.py
        if isNoneOrEmpty(classtype):
            self.classtype = None
        else:
            self.classtype = eval(classtype)

        self.notes = notes

    # reads specific memory address on given frame
    def read(self):
        if dolphin.hook():
            return dolphin.read(self.address, self.type)
        else:
            return Exception
        
    # overwrites value onto address on given frame
    def write(self, value):
        if dolphin.hook():
            return dolphin.write(self.address, self.type, value)
        else:
            return Exception

    # returns memoryAddress info in a dict format
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

# modify "addresses.csv" to add any addresses you want
def appendMemoryAddresses(csvreader):

    memoryAddresses = {}

    fields = list(next(csvreader))
    data = list(next(csvreader))

    # loops through csv data and appends info to memoryAddresses
    # not super well written with try & except's
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

    # prints all keys
    for key in memoryAddresses.keys(): print(key)

    # example for changing away score
    print(memoryAddresses["score_away"].read())
    memoryAddresses["score_away"].write(20)
    memoryAddresses["score_display_away"].write(20)
    print(memoryAddresses["score_away"].read())

    memoryAddresses["desired_mound_position_x"].write(0.2)

    # example for reading p1 stick & trigger inputs and ball position y
    for i in range(50):
        print(memoryAddresses["p1_stick_trigger_input"].read())
        print(str(memoryAddresses["ball_position_y"].read()))


if __name__ == '__main__':
    main()