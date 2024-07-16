import enum


@enum.unique
class CharacterID(enum.Enum):
    Mario       = 0
    Luigi       = 1
    DK          = 2
    Diddy       = 3
    Peach       = 4
    Daisy       = 5
    Yoshi       = 6
    BabyMario   = 7
    BabyLuigi   = 8
    Bowser      = 9
    Wario       = 10
    Waluigi     = 11
    KoopaR      = 12
    ToadR       = 13
    Boo         = 14
    Toadette    = 15
    ShyGuyR     = 16
    Birdo       = 17
    Monty       = 18
    BowserJr    = 19
    ParatroopaR = 20
    PiantaB     = 21
    PiantaR     = 22
    PiantaY     = 23
    NokiB       = 24
    NokiR       = 25
    NokiG       = 26
    BroH        = 27
    Toadsworth  = 28
    ToadB       = 29
    ToadY       = 30
    ToadG       = 31
    ToadP       = 32
    MagikoopaB  = 33
    MagikoopaR  = 34
    MagikoopaG  = 35
    MagikoopaY  = 36
    KingBoo     = 37
    Petey       = 38
    Dixie       = 39
    Goomba      = 40
    Paragoomba  = 41
    KoopaG      = 42
    ParatroopaG = 43
    ShyGuyB     = 44
    ShyGuyY     = 45
    ShyGuyG     = 46
    ShyGuyBk    = 47
    DryBonesGy  = 48
    DryBonesG   = 49
    DryBonesR   = 50
    DryBonesB   = 51
    BroF        = 52
    BroB        = 53

@enum.unique
class FieldingArm(enum.Enum):
    right   = 0
    left    = 1

@enum.unique
class BattingStance(enum.Enum):
    right   = 0
    left    = 1

@enum.unique
class CharacterClass(enum.Enum):
    balance     = 0
    power       = 1
    speed       = 2
    technique   = 3

@enum.unique
class WeightType(enum.Enum):
    featherweight   = 0
    lightweight     = 1
    welterweight    = 2
    middleweight    = 3
    heavyweight     = 4

@enum.unique
class IsCapitan(enum.Enum):
    no  = 0
    yes = 1

@enum.unique
class hitTrajectoryX(enum.Enum):
    mid     = 0
    pull    = 1
    push    = 2

@enum.unique
class hitTrajectoryHeight(enum.Enum):
    mid     = 0
    high    = 1
    low     = 2

@enum.unique
class FieldingAbilities(enum.Enum):
    # 2^k for actual value 
    tongue      = 0
    suction     = 1
    supercatch  = 2
    balldash    = 3
    bodycheck   = 4
    curve       = 5

    # 2^k + 2^(6+j)
    wallsplat       = 6
    walljump        = 7
    clamber         = 8
    slidingcatch    = 9
    laser           = 10
    quickthrow      = 11
    superjump       = 12
    magiccatch      = 13


@enum.unique
class CapitanStarAbility(enum.Enum):
    nothing         = 0
    mfireball       = 1 # idk they call it "fireball" in his Mario's bio
    lfireball       = 2 # vs "green fireball" in Luigi's bio
    phonyball       = 3
    liarball        = 4
    bananaball      = 5
    boomerangball   = 6
    killerball      = 7
    killerjrball    = 8
    eggball         = 9
    weirdball       = 10
    heartball       = 11
    flowerball      = 12

@enum.unique
class StarSwing(enum.Enum):
    none        = 0
    popfly      = 1
    grounder    = 2
    linedrive   = 3

@enum.unique
class StarPitch(enum.Enum):
    none        = 0
    curve       = 1
    fastball    = 2
    changeup    = 3

@enum.unique
class StadiumID(enum.Enum):
    MarioStadium    = 0
    PeachGarden     = 1
    WarioPalace     = 2
    YoshiPark       = 3
    DKJungle        = 4
    BowserStadium   = 5
    ToyField        = 6



class ChemestryTable():
    chemestryMatrix =  [[50, 99, 30, 59, 95, 88, 90, 87, 89, 15, 10, 20, 65, 82, 50, 81, 48, 63, 71, 25, 62, 86, 86, 86, 85, 85, 85, 38, 76, 82, 82, 82, 82, 40, 40, 40, 40, 49, 35, 55, 42, 43, 65, 62, 48, 48, 48, 48, 32, 32, 32, 32, 38, 38],
                        [99, 50, 35, 55, 90, 95, 86, 89, 87, 25, 20, 10, 62, 81, 15, 82, 47, 60, 72, 30, 65, 83, 83, 83, 80, 80, 80, 39, 75, 81, 81, 81, 81, 51, 51, 51, 51, 11, 34, 57, 40, 41, 62, 65, 47, 47, 47, 47, 28, 28, 28, 28, 39, 39],
                        [30, 35, 50, 99, 22, 24, 77, 58, 57, 41, 59, 34, 67, 65, 68, 61, 50, 40, 83, 69, 72, 55, 55, 55, 45, 45, 45, 75, 63, 65, 65, 65, 65, 29, 29, 29, 29, 81, 91, 90, 80, 79, 67, 72, 50, 50, 50, 50, 43, 43, 43, 43, 75, 75],
                        [59, 55, 99, 50, 64, 68, 72, 79, 78, 34, 33, 32, 75, 67, 60, 65, 66, 45, 77, 71, 70, 46, 46, 46, 56, 56, 56, 58, 62, 67, 67, 67, 67, 57, 57, 57, 57, 48, 52, 95, 91, 80, 75, 70, 66, 66, 66, 66, 44, 44, 44, 44, 58, 58],
                        [95, 90, 22, 64, 50, 97, 83, 85, 80, 9, 14, 25, 60, 93, 31, 94, 58, 84, 45, 82, 57, 87, 87, 87, 88, 88, 88, 32, 96, 93, 93, 93, 93, 43, 43, 43, 43, 41, 5, 70, 44, 40, 60, 57, 58, 58, 58, 58, 35, 35, 35, 35, 32, 32],
                        [88, 95, 24, 68, 97, 50, 80, 82, 85, 11, 25, 15, 57, 86, 34, 87, 55, 81, 43, 45, 60, 77, 77, 77, 83, 83, 83, 33, 79, 86, 86, 86, 86, 41, 41, 41, 41, 40, 6, 72, 46, 47, 57, 60, 55, 55, 55, 55, 30, 30, 30, 30, 33, 33],
                        [90, 86, 77, 72, 83, 80, 50, 95, 94, 37, 50, 54, 78, 76, 53, 75, 45, 97, 73, 48, 74, 89, 89, 89, 82, 82, 82, 40, 71, 76, 76, 76, 76, 49, 49, 49, 49, 66, 42, 60, 67, 68, 78, 74, 45, 45, 45, 45, 46, 46, 46, 46, 40, 40],
                        [87, 89, 58, 79, 85, 82, 95, 50, 99, 19, 12, 22, 66, 84, 14, 86, 10, 75, 60, 35, 61, 76, 76, 76, 77, 77, 77, 28, 88, 84, 84, 84, 84, 34, 34, 34, 34, 21, 24, 71, 45, 42, 66, 61, 10, 10, 10, 10, 33, 33, 33, 33, 28, 28],
                        [89, 87, 57, 78, 80, 85, 94, 99, 50, 18, 22, 12, 64, 83, 13, 84, 15, 70, 56, 41, 77, 79, 79, 79, 81, 81, 81, 27, 86, 83, 83, 83, 83, 33, 33, 33, 33, 10, 23, 73, 47, 44, 64, 77, 15, 15, 15, 15, 34, 34, 34, 34, 27, 27],
                        [15, 25, 41, 34, 9, 11, 37, 19, 18, 50, 65, 60, 91, 10, 80, 5, 85, 71, 59, 99, 90, 30, 30, 30, 35, 35, 35, 95, 13, 10, 10, 10, 10, 88, 88, 88, 88, 75, 66, 33, 73, 72, 91, 90, 85, 85, 85, 85, 92, 92, 92, 92, 95, 95],
                        [10, 20, 59, 33, 14, 25, 50, 12, 22, 65, 50, 99, 58, 15, 90, 16, 80, 30, 70, 81, 55, 39, 39, 39, 48, 48, 48, 84, 24, 15, 15, 15, 15, 71, 71, 71, 71, 82, 63, 21, 62, 61, 58, 55, 80, 80, 80, 80, 42, 42, 42, 42, 84, 84],
                        [20, 10, 34, 32, 25, 15, 54, 22, 12, 60, 99, 50, 55, 16, 88, 17, 78, 35, 67, 77, 58, 42, 42, 42, 47, 47, 47, 86, 23, 16, 16, 16, 16, 91, 91, 91, 91, 80, 51, 24, 61, 63, 55, 58, 78, 78, 78, 78, 48, 48, 48, 48, 86, 86],
                        [65, 62, 67, 75, 60, 57, 78, 66, 64, 91, 58, 55, 50, 39, 84, 36, 70, 68, 80, 87, 99, 53, 53, 53, 71, 71, 71, 85, 31, 39, 39, 39, 39, 81, 81, 81, 81, 69, 44, 63, 88, 86, 50, 99, 70, 70, 70, 70, 90, 90, 90, 90, 85, 85],
                        [82, 81, 65, 67, 93, 86, 76, 84, 83, 10, 15, 16, 39, 50, 25, 99, 53, 74, 52, 46, 38, 85, 85, 85, 78, 78, 78, 35, 92, 50, 50, 50, 50, 36, 36, 36, 36, 37, 31, 64, 66, 60, 39, 38, 53, 53, 53, 53, 29, 29, 29, 29, 35, 35],
                        [50, 15, 68, 60, 31, 34, 53, 14, 13, 80, 90, 88, 84, 25, 50, 23, 86, 83, 55, 70, 89, 49, 49, 49, 65, 65, 65, 71, 27, 25, 25, 25, 25, 95, 95, 95, 95, 98, 64, 51, 82, 87, 84, 89, 86, 86, 86, 86, 85, 85, 85, 85, 71, 71],
                        [81, 82, 61, 65, 94, 87, 75, 86, 84, 5, 16, 17, 36, 99, 23, 50, 51, 80, 49, 47, 35, 78, 78, 78, 74, 74, 74, 34, 91, 99, 99, 99, 99, 31, 31, 31, 31, 32, 30, 62, 64, 59, 36, 35, 51, 51, 51, 51, 27, 27, 27, 27, 34, 34],
                        [48, 47, 50, 66, 58, 55, 45, 10, 15, 85, 80, 78, 70, 53, 86, 51, 50, 90, 91, 83, 75, 60, 60, 60, 62, 62, 62, 72, 46, 53, 53, 53, 53, 84, 84, 84, 84, 65, 33, 67, 52, 54, 70, 75, 50, 50, 50, 50, 68, 68, 68, 68, 72, 72],
                        [63, 60, 40, 45, 84, 81, 97, 75, 70, 71, 30, 35, 68, 74, 83, 80, 90, 50, 42, 38, 64, 51, 51, 51, 67, 67, 67, 73, 69, 74, 74, 74, 74, 37, 37, 37, 37, 79, 92, 89, 54, 55, 68, 64, 90, 90, 90, 90, 56, 56, 56, 56, 73, 73],
                        [71, 72, 83, 77, 45, 43, 73, 60, 56, 59, 70, 67, 80, 52, 55, 49, 91, 42, 50, 76, 82, 68, 68, 68, 40, 40, 40, 25, 51, 52, 52, 52, 52, 39, 39, 39, 39, 47, 37, 74, 95, 90, 80, 82, 91, 91, 91, 91, 81, 81, 81, 81, 25, 25],
                        [25, 30, 69, 71, 82, 45, 48, 35, 41, 99, 81, 77, 87, 46, 70, 47, 83, 38, 76, 50, 80, 20, 20, 20, 24, 24, 24, 91, 52, 46, 46, 46, 46, 90, 90, 90, 90, 58, 68, 66, 55, 51, 87, 80, 83, 83, 83, 83, 84, 84, 84, 84, 91, 91],
                        [62, 65, 72, 70, 57, 60, 74, 61, 77, 90, 55, 58, 99, 38, 89, 35, 75, 64, 82, 80, 50, 50, 50, 50, 68, 68, 68, 83, 30, 38, 38, 38, 38, 79, 79, 79, 79, 73, 43, 59, 85, 91, 99, 50, 75, 75, 75, 75, 88, 88, 88, 88, 83, 83],
                        [86, 83, 55, 46, 87, 77, 89, 76, 79, 30, 39, 42, 53, 85, 49, 78, 60, 51, 68, 20, 50, 50, 50, 50, 98, 98, 98, 69, 72, 85, 85, 85, 85, 61, 61, 61, 61, 54, 15, 44, 38, 36, 53, 50, 60, 60, 60, 60, 58, 58, 58, 58, 69, 69],
                        [86, 83, 55, 46, 87, 77, 89, 76, 79, 30, 39, 42, 53, 85, 49, 78, 60, 51, 68, 20, 50, 50, 50, 50, 98, 98, 98, 69, 72, 85, 85, 85, 85, 61, 61, 61, 61, 54, 15, 44, 38, 36, 53, 50, 60, 60, 60, 60, 58, 58, 58, 58, 69, 69],
                        [86, 83, 55, 46, 87, 77, 89, 76, 79, 30, 39, 42, 53, 85, 49, 78, 60, 51, 68, 20, 50, 50, 50, 50, 98, 98, 98, 69, 72, 85, 85, 85, 85, 61, 61, 61, 61, 54, 15, 44, 38, 36, 53, 50, 60, 60, 60, 60, 58, 58, 58, 58, 69, 69],
                        [85, 80, 45, 56, 88, 83, 82, 77, 81, 35, 48, 47, 71, 78, 65, 74, 62, 67, 40, 24, 68, 98, 98, 98, 50, 50, 50, 42, 73, 78, 78, 78, 78, 54, 54, 54, 54, 38, 10, 75, 70, 69, 71, 68, 62, 62, 62, 62, 55, 55, 55, 55, 42, 42],
                        [85, 80, 45, 56, 88, 83, 82, 77, 81, 35, 48, 47, 71, 78, 65, 74, 62, 67, 40, 24, 68, 98, 98, 98, 50, 50, 50, 42, 73, 78, 78, 78, 78, 54, 54, 54, 54, 38, 10, 75, 70, 69, 71, 68, 62, 62, 62, 62, 55, 55, 55, 55, 42, 42],
                        [85, 80, 45, 56, 88, 83, 82, 77, 81, 35, 48, 47, 71, 78, 65, 74, 62, 67, 40, 24, 68, 98, 98, 98, 50, 50, 50, 42, 73, 78, 78, 78, 78, 54, 54, 54, 54, 38, 10, 75, 70, 69, 71, 68, 62, 62, 62, 62, 55, 55, 55, 55, 42, 42],
                        [38, 39, 75, 58, 32, 33, 40, 28, 27, 95, 84, 86, 85, 35, 71, 34, 72, 73, 25, 91, 83, 69, 69, 69, 42, 42, 42, 50, 36, 35, 35, 35, 35, 87, 87, 87, 87, 76, 81, 54, 78, 77, 85, 83, 72, 72, 72, 72, 82, 82, 82, 82, 50, 50],
                        [76, 75, 63, 62, 96, 79, 71, 88, 86, 13, 24, 23, 31, 92, 27, 91, 46, 69, 51, 52, 30, 72, 72, 72, 73, 73, 73, 36, 50, 92, 92, 92, 92, 25, 25, 25, 25, 39, 28, 61, 60, 58, 31, 30, 46, 46, 46, 46, 38, 38, 38, 38, 36, 36],
                        [82, 81, 65, 67, 93, 86, 76, 84, 83, 10, 15, 16, 39, 50, 25, 99, 53, 74, 52, 46, 38, 85, 85, 85, 78, 78, 78, 35, 92, 50, 50, 50, 50, 36, 36, 36, 36, 37, 31, 64, 66, 60, 39, 38, 53, 53, 53, 53, 29, 29, 29, 29, 35, 35],
                        [82, 81, 65, 67, 93, 86, 76, 84, 83, 10, 15, 16, 39, 50, 25, 99, 53, 74, 52, 46, 38, 85, 85, 85, 78, 78, 78, 35, 92, 50, 50, 50, 50, 36, 36, 36, 36, 37, 31, 64, 66, 60, 39, 38, 53, 53, 53, 53, 29, 29, 29, 29, 35, 35],
                        [82, 81, 65, 67, 93, 86, 76, 84, 83, 10, 15, 16, 39, 50, 25, 99, 53, 74, 52, 46, 38, 85, 85, 85, 78, 78, 78, 35, 92, 50, 50, 50, 50, 36, 36, 36, 36, 37, 31, 64, 66, 60, 39, 38, 53, 53, 53, 53, 29, 29, 29, 29, 35, 35],
                        [82, 81, 65, 67, 93, 86, 76, 84, 83, 10, 15, 16, 39, 50, 25, 99, 53, 74, 52, 46, 38, 85, 85, 85, 78, 78, 78, 35, 92, 50, 50, 50, 50, 36, 36, 36, 36, 37, 31, 64, 66, 60, 39, 38, 53, 53, 53, 53, 29, 29, 29, 29, 35, 35],
                        [40, 51, 29, 57, 43, 41, 49, 34, 33, 88, 71, 91, 81, 36, 95, 31, 84, 37, 39, 90, 79, 61, 61, 61, 54, 54, 54, 87, 25, 36, 36, 36, 36, 50, 50, 50, 50, 44, 38, 35, 65, 67, 81, 79, 84, 84, 84, 84, 86, 86, 86, 86, 87, 87],
                        [40, 51, 29, 57, 43, 41, 49, 34, 33, 88, 71, 91, 81, 36, 95, 31, 84, 37, 39, 90, 79, 61, 61, 61, 54, 54, 54, 87, 25, 36, 36, 36, 36, 50, 50, 50, 50, 44, 38, 35, 65, 67, 81, 79, 84, 84, 84, 84, 86, 86, 86, 86, 87, 87],
                        [40, 51, 29, 57, 43, 41, 49, 34, 33, 88, 71, 91, 81, 36, 95, 31, 84, 37, 39, 90, 79, 61, 61, 61, 54, 54, 54, 87, 25, 36, 36, 36, 36, 50, 50, 50, 50, 44, 38, 35, 65, 67, 81, 79, 84, 84, 84, 84, 86, 86, 86, 86, 87, 87],
                        [40, 51, 29, 57, 43, 41, 49, 34, 33, 88, 71, 91, 81, 36, 95, 31, 84, 37, 39, 90, 79, 61, 61, 61, 54, 54, 54, 87, 25, 36, 36, 36, 36, 50, 50, 50, 50, 44, 38, 35, 65, 67, 81, 79, 84, 84, 84, 84, 86, 86, 86, 86, 87, 87],
                        [49, 11, 81, 48, 41, 40, 66, 21, 10, 75, 82, 80, 69, 37, 98, 32, 65, 79, 47, 58, 73, 54, 54, 54, 38, 38, 38, 76, 39, 37, 37, 37, 37, 44, 44, 44, 44, 50, 95, 42, 71, 70, 69, 73, 65, 65, 65, 65, 77, 77, 77, 77, 76, 76],
                        [35, 34, 91, 52, 5, 6, 42, 24, 23, 66, 63, 51, 44, 31, 64, 30, 33, 92, 37, 68, 43, 15, 15, 15, 10, 10, 10, 81, 28, 31, 31, 31, 31, 38, 38, 38, 38, 95, 50, 56, 74, 73, 44, 43, 33, 33, 33, 33, 41, 41, 41, 41, 81, 81],
                        [55, 57, 90, 95, 70, 72, 60, 71, 73, 33, 21, 24, 63, 64, 51, 62, 67, 89, 74, 66, 59, 44, 44, 44, 75, 75, 75, 54, 61, 64, 64, 64, 64, 35, 35, 35, 35, 42, 56, 50, 77, 88, 63, 59, 67, 67, 67, 67, 37, 37, 37, 37, 54, 54],
                        [42, 40, 80, 91, 44, 46, 67, 45, 47, 73, 62, 61, 88, 66, 82, 64, 52, 54, 95, 55, 85, 38, 38, 38, 70, 70, 70, 78, 60, 66, 66, 66, 66, 65, 65, 65, 65, 71, 74, 77, 50, 97, 88, 85, 52, 52, 52, 52, 63, 63, 63, 63, 78, 78],
                        [43, 41, 79, 80, 40, 47, 68, 42, 44, 72, 61, 63, 86, 60, 87, 59, 54, 55, 90, 51, 91, 36, 36, 36, 69, 69, 69, 77, 58, 60, 60, 60, 60, 67, 67, 67, 67, 70, 73, 88, 97, 50, 86, 91, 54, 54, 54, 54, 62, 62, 62, 62, 77, 77],
                        [65, 62, 67, 75, 60, 57, 78, 66, 64, 91, 58, 55, 50, 39, 84, 36, 70, 68, 80, 87, 99, 53, 53, 53, 71, 71, 71, 85, 31, 39, 39, 39, 39, 81, 81, 81, 81, 69, 44, 63, 88, 86, 50, 99, 70, 70, 70, 70, 90, 90, 90, 90, 85, 85],
                        [62, 65, 72, 70, 57, 60, 74, 61, 77, 90, 55, 58, 99, 38, 89, 35, 75, 64, 82, 80, 50, 50, 50, 50, 68, 68, 68, 83, 30, 38, 38, 38, 38, 79, 79, 79, 79, 73, 43, 59, 85, 91, 99, 50, 75, 75, 75, 75, 88, 88, 88, 88, 83, 83],
                        [48, 47, 50, 66, 58, 55, 45, 10, 15, 85, 80, 78, 70, 53, 86, 51, 50, 90, 91, 83, 75, 60, 60, 60, 62, 62, 62, 72, 46, 53, 53, 53, 53, 84, 84, 84, 84, 65, 33, 67, 52, 54, 70, 75, 50, 50, 50, 50, 68, 68, 68, 68, 72, 72],
                        [48, 47, 50, 66, 58, 55, 45, 10, 15, 85, 80, 78, 70, 53, 86, 51, 50, 90, 91, 83, 75, 60, 60, 60, 62, 62, 62, 72, 46, 53, 53, 53, 53, 84, 84, 84, 84, 65, 33, 67, 52, 54, 70, 75, 50, 50, 50, 50, 68, 68, 68, 68, 72, 72],
                        [48, 47, 50, 66, 58, 55, 45, 10, 15, 85, 80, 78, 70, 53, 86, 51, 50, 90, 91, 83, 75, 60, 60, 60, 62, 62, 62, 72, 46, 53, 53, 53, 53, 84, 84, 84, 84, 65, 33, 67, 52, 54, 70, 75, 50, 50, 50, 50, 68, 68, 68, 68, 72, 72],
                        [48, 47, 50, 66, 58, 55, 45, 10, 15, 85, 80, 78, 70, 53, 86, 51, 50, 90, 91, 83, 75, 60, 60, 60, 62, 62, 62, 72, 46, 53, 53, 53, 53, 84, 84, 84, 84, 65, 33, 67, 52, 54, 70, 75, 50, 50, 50, 50, 68, 68, 68, 68, 72, 72],
                        [32, 28, 43, 44, 35, 30, 46, 33, 34, 92, 42, 48, 90, 29, 85, 27, 68, 56, 81, 84, 88, 58, 58, 58, 55, 55, 55, 82, 38, 29, 29, 29, 29, 86, 86, 86, 86, 77, 41, 37, 63, 62, 90, 88, 68, 68, 68, 68, 50, 50, 50, 50, 82, 82],
                        [32, 28, 43, 44, 35, 30, 46, 33, 34, 92, 42, 48, 90, 29, 85, 27, 68, 56, 81, 84, 88, 58, 58, 58, 55, 55, 55, 82, 38, 29, 29, 29, 29, 86, 86, 86, 86, 77, 41, 37, 63, 62, 90, 88, 68, 68, 68, 68, 50, 50, 50, 50, 82, 82],
                        [32, 28, 43, 44, 35, 30, 46, 33, 34, 92, 42, 48, 90, 29, 85, 27, 68, 56, 81, 84, 88, 58, 58, 58, 55, 55, 55, 82, 38, 29, 29, 29, 29, 86, 86, 86, 86, 77, 41, 37, 63, 62, 90, 88, 68, 68, 68, 68, 50, 50, 50, 50, 82, 82],
                        [32, 28, 43, 44, 35, 30, 46, 33, 34, 92, 42, 48, 90, 29, 85, 27, 68, 56, 81, 84, 88, 58, 58, 58, 55, 55, 55, 82, 38, 29, 29, 29, 29, 86, 86, 86, 86, 77, 41, 37, 63, 62, 90, 88, 68, 68, 68, 68, 50, 50, 50, 50, 82, 82],
                        [38, 39, 75, 58, 32, 33, 40, 28, 27, 95, 84, 86, 85, 35, 71, 34, 72, 73, 25, 91, 83, 69, 69, 69, 42, 42, 42, 50, 36, 35, 35, 35, 35, 87, 87, 87, 87, 76, 81, 54, 78, 77, 85, 83, 72, 72, 72, 72, 82, 82, 82, 82, 50, 50],
                        [38, 39, 75, 58, 32, 33, 40, 28, 27, 95, 84, 86, 85, 35, 71, 34, 72, 73, 25, 91, 83, 69, 69, 69, 42, 42, 42, 50, 36, 35, 35, 35, 35, 87, 87, 87, 87, 76, 81, 54, 78, 77, 85, 83, 72, 72, 72, 72, 82, 82, 82, 82, 50, 50]]   


class AddressLocation():
    def __init__():
        RunsAway = 0x808928a7
        RunsHome = 0x808928cd

        Balls = 0x8089296f
        Strikes = 0x8089296b
        Outs = 0x80892973

        IsOnABase = 0x80892734
        IsOnThird = 0x80892735
        IsOnSecond = 0x80892736
        IsOnFirst = 0x80892737
        IsAtHome = 0x80892738

        StarsHome = 0x80892ad6
        StarsAway = 0x80892ad7

        StadiumID = 0x800e8705

        

        PitcherID = 0x80890adb #idk check on that
        PitcherHandedness = 0x80890b01
        
        PitcherPositionX = 0x80890A4C       #float
        PitcherCurrentCurve = 0x80890A24    #float

        BatterID = 0x80890973
        BatterHandedness = 0x8089098b


        BatterPositionX = 0x80890910    #float
        BatterPositionY = 0x80890914    #float



    

class State():
    pass 