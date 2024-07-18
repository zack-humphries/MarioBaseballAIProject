import memory_values
from memory_values import *
import csv
import os
import math


class AllCharacters:
    def __init__(self):
        self.list = []

    def add_character(self, character):
        self.list.append(character)


class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.stats = None
        self.attributes = None


class CharacterStats(Character):
    def __init__(self):
        self.stats = []

    def add_stat(self, stat):
        self.stats.append(stat)

    def change_stat(self, name, value, *args):
        for stat in self.stats:
            if stat.name == name:
                stat.value = value

class Stat(CharacterStats):
    def __init__(self, name, value, address = None, type = None, class_type = None):
        self.name = name
        self.type = type
        self.address = address
        self.value = value
        self.class_type = class_type


    #def get_value??

    #def turn pow2 to list?
        
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

    if (temptype in pow2Types) and (tempvalue != 0):
        while tempvalue != 0:
            temppow2 = findClosestPow2(tempvalue)
            templist.append(temppow2)
            tempvalue = tempvalue - temppow2
        for index in range(len(templist)):
            templist[index] = temptype(templist[index])
        return templist
    elif (temptype in pow2Types) and (tempvalue == 0):
        return [temptype(tempvalue)]
    
    return temptype(tempvalue)

    



def appendCharacterData(allcharacters : AllCharacters, csvreader):
    # returns stat's names, data types, and actual data
    fields = list(next(csvreader))
    datatypes = list(next(csvreader))
    data = list(csvreader)

    # loops through all characters IDs in memory_values and inputs their stats
    for characterid in memory_values.CharacterID:

        #pulls row data corresponding with character_id
        datarow = data[characterid.value]

        #creates new character object for that specific character
        currcharacter = Character(characterid.value, characterid.name)

        #creates character stats object for that character
        characterstats = CharacterStats()

        # for loop ignores char_id and trailing column ''
        for statindex in range(1, len(fields)-1):

            # converts string to enum class name in memory_values.py
            temptype = convertValueTypeString(datatypes[statindex])

            tempvalue = int(datarow[statindex])
            tempvalue = checkAndConvertIfPow2Type(temptype, tempvalue)

            characterstats.add_stat(Stat(fields[statindex], tempvalue, type=temptype))


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
        
    return allcharacters

        
def main():
    all_characters = initializeCharacters()

    for character in all_characters.list:
        print("ID: " + str(character.id) + " " + str(character.name))

        for stat in character.stats:
            print(stat.name + ": " + str(stat.value) + " <- " + str(stat.type))

        print()

    
if __name__ == '__main__':
    main()

#    stat_list = [
#         "fielding_arm",
#         "batting_stance",
#         "character_class",
#         "weight_class",
#         "is_captain",
#         "curve_ball_speed",
#         "fast_ball_speed",
#         "cursed_ball",
#         "curve",
#         "curve_control",
#         "fielding_ability1",
#         "fielding_ability2",
#         "slap_contact_mult",
#         "charge_contact_mult",
#         "slap_power",
#         "charge_power",
#         "bunting",
#         "hit_trajectory_X",
#         "hit_trajectory_Y",
#         "speed",
#         "throwing_arm",
#         "captain_stars",
#         "star_swing",
#         "star_pitch",
#         "chemestry"
#     ]
# class Chemestry(CharacterStats):
#     def __init__(self):
        

# class Stat:
#     def __init__(self, name, value, *args, **kwargs):
#         self.name = name

#         self.type = kwargs.get('type', None)
#         if self.type is not None:
#             assert value in self.type
#             self.value = value
#         else:
#             self.value = value

