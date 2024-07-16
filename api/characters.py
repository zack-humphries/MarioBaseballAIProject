import memory_values

class AllCharacters:
    def __init__(self):
        self.list = []

    def add_character(self, character):
        self.list.append(character)




class Character:
    def __init__(self):
        self.id = None
        self.name = None
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
        

    

    
# class CharacterStats(Character):
#     def __init__(self):
#         self.fielding_arm = None
#         self.batting_stance = None
#         self.character_class = None
#         self.weight_class = None
#         self.is_captain = None
#         self.curve_ball_speed = None
#         self.fast_ball_speed = None
#         self.cursed_ball = None
#         self.curve = None
#         self.curve_control = None
#         self.fielding_ability1 = None
#         self.fielding_ability2 = None
#         self.slap_contact_mult = None
#         self.charge_contact_mult = None
#         self.slap_power = None
#         self.charge_power = None
#         self.bunting = None
#         self.hit_trajectory_X = None
#         self.hit_trajectory_Y = None
#         self.speed = None
#         self.throwing_arm = None
#         self.captain_stars = None
#         self.star_swing = None
#         self.star_pitch = None
#         self.chemestry = None

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

