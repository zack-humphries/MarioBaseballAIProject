import memory_values
from memory_values import *
import csv
import os
import math


class AllCharacters:
    def __init__(self):
        self.allCharacters = {}

    def add_character(self, character):
        self.allCharacters[character.name] = character



class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.stats = {}
        self.attributes = {}


class CharacterStats(Character):
    def __init__(self):
        self.stats = {}

    def add_stat(self, stat):
        self.stats[stat.stat["name"]] = stat

    def change_stat(self, name, value, *args):
        self.stats[name] = value


class Stat(CharacterStats):
    def __init__(self, name, value, address = None, type = None, class_type = None):
        self.stat =  {
            'name' : name,
            'value' : value,
            'type' : type,
            'address': address,
            'class_type' : class_type
        }

        setattr(self, name, self.stat)

        self.name = name
        self.type = type
        self.address = address
        self.value = value
        self.class_type = class_type


def returnFilePath(filename):
    scriptdir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(scriptdir, filename)
    return filepath

def convertValueTypeString(str):
    if str == '':
        return None
    else:
        return eval(str)
    
def findClosestPow2(num):
    closestlog2 = math.floor(math.log2(num))

    return (2**closestlog2)

def checkAndConvertIfPow2Type(temptype, tempvalue):
    pow2Types = [FieldingAbility1, FieldingAbility2]

    templist = []
    # takes value and separates into indvidual pow2 values if part of FieldingAbility1 or FieldingAbility2
    if (temptype in pow2Types) and (tempvalue != 0):
    
        # ex: 19 -> [16, 2, 1] 
        while tempvalue != 0:
            temppow2 = findClosestPow2(tempvalue)
            templist.append(temppow2)
            tempvalue = tempvalue - temppow2

        # [16, 2, 1] -> [enumtype(16), enumtype(2), enumtype(1)]    
        for index in range(len(templist)):
            templist[index] = temptype(templist[index])
        return templist
    
    #if value is zero, return [enumtype(0)]
    elif (temptype in pow2Types) and (tempvalue == 0):
        return [temptype(tempvalue)]
    
    return temptype(tempvalue)



def appendCharacterData(allcharacters : AllCharacters, csvreader):
    # returns stat's names, data types, and actual data
    fields = list(next(csvreader))
    datatypes = list(next(csvreader))
    data = list(csvreader)

    # loops through all characters IDs in memory_values and inputs their stats
    for character in memory_values.CharacterID:

        #pulls row data corresponding with character_id
        datarow = data[character.value]

        #creates new character object for that specific character
        currcharacter = Character(character.value, character.name)

        #creates character stats object for that character
        characterstats = CharacterStats()

        # for loop ignores char_id and trailing column ''
        for statindex in range(1, len(fields)-1):

            # converts string to enum class name in memory_values.py
            temptype = convertValueTypeString(datatypes[statindex])

            tempvalue = int(datarow[statindex])
            tempvalue = checkAndConvertIfPow2Type(temptype, tempvalue)

            characterstats.add_stat(Stat(fields[statindex], tempvalue, type=temptype))

        # print(characterstats.stats['fielding_arm'].value.value)

        currcharacter.stats = characterstats.stats

        allcharacters.add_character(currcharacter)


def initializeCharacters():

    # initialize all characters class
    allcharacters = AllCharacters()

    # return current filepath (which should contain character_stats.csv)
    filepath = returnFilePath("character_stats.csv")

    with open(filepath, 'r') as csvfile:

        csvreader = csv.reader(csvfile)

        appendCharacterData(allcharacters, csvreader)
        
    return allcharacters.allCharacters

        
def main():
    all_characters = initializeCharacters()

    print(all_characters['Mario'].stats['fielding_arm'].value)
    
    
if __name__ == '__main__':
    main()
