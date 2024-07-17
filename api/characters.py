import memory_values
from memory_values import *
import csv
import os


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

    
def initializeCharacters():

    allcharacters = AllCharacters()

    filepath = returnFilePath("character_stats.csv")

    with open(filepath, 'r') as csvfile:

        csvreader = csv.reader(csvfile)

        fields = list(next(csvreader))
        datatype = list(next(csvreader))
        data = list(csvreader)

        print(fields)

        for characterid in memory_values.CharacterID:

            datarow = data[characterid.value]

            currcharacter = Character(characterid.value, characterid.name)

            characterstats = CharacterStats()

            count = 0
            for statindex in range(1, len(fields)-1):

                if datatype[statindex] != '':
                    temptype = eval(datatype[statindex])
                    tempvalue = temptype(int(datarow[statindex]))
                    characterstats.add_stat(Stat(fields[statindex], tempvalue, type=temptype))
                count += 1

            currcharacter.stats = characterstats.stats

            allcharacters.add_character(currcharacter)

    return allcharacters

        
def main():
    all_characters = initializeCharacters()

    for character in all_characters.list:
        print(str(character.id) + " " + str(character.name))

        for stat in character.stats:
            print(stat.name + ": " + str(stat.value) + " <- " + str(stat.type))

        return

    
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

