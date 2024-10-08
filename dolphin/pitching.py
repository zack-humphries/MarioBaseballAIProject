from memorylib import Dolphin
from addresses import initializeMemoryAddresses
from characters import initializeCharacters
import memory_values
from helper_functions import linearInterpolateToNewRange
#from pitching_calculations import pitchBaseReleaseCoordinates
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import math


dolphin = Dolphin()

pitchTypes = {
    'curve': {'pitchProperty': 'curve', 'pitchBaseReleaseCoordinates': 'curve', 'ballSpeed': 'curve_ball_speed'},
    'charge': {'pitchProperty': 'curve', 'pitchBaseReleaseCoordinates': 'charge', 'ballSpeed': 'fast_ball_speed'},
    'perfect': {'pitchProperty': 'curve', 'pitchBaseReleaseCoordinates': 'charge', 'ballSpeed': 'fast_ball_speed'},
    'change': {'pitchProperty': 'change', 'pitchBaseReleaseCoordinates': 'charge', 'ballSpeed': 'fast_ball_speed'}
}

pitchBaseReleaseCoordinates = {
    'Mario':       {'curve': {'X': -0.358750939,    'Z': 2.9281559,     'Y': 17.6997108},       'charge': {'X': -0.370488256,   'Z': 2.83268118,    'Y': 17.872982}},
    'Luigi':       {'curve': {'X': 0.221170574,     'Z': 2.30373907,    'Y': 18.0957241},       'charge': {'X': -0.253166497,   'Z': 2.7028234,     'Y': 17.5246811}},
    'DK':          {'curve': {'X': -2.04435539,     'Z': 2.03053284,    'Y': 16.223959},        'charge': {'X': -2.04427075,    'Z': 2.03053284,    'Y': 16.2238922}},
    'Diddy':       {'curve': {'X': -0.484804153,    'Z': 2.21302128,    'Y': 18.831337},        'charge': {'X': -0.422204643,   'Z': 2.27686,       'Y': 19.3343658}},
    'Peach':       {'curve': {'X': -0.0703445852,   'Z': 2.16658092,    'Y': 18.1502056},       'charge': {'X': -0.131633073,   'Z': 2.19204974,    'Y': 19.2481537}},
    'Daisy':       {'curve': {'X': -0.281522155,    'Z': 1.16270649,    'Y': 17.975111},        'charge': {'X': -0.462917864,   'Z': 0.998229444,   'Y': 17.4418068}},
    'Yoshi':       {'curve': {'X': -0.0526904576,   'Z': 1.73863459,    'Y': 17.0554199},       'charge': {'X': -0.102338329,   'Z': 1.74589205,    'Y': 17.2527218}},
    'BabyMario':   {'curve': {'X': -0.294910491,    'Z': 0.501412511,   'Y': 17.8377438},       'charge': {'X': -0.293749392,   'Z': 1.67534804,    'Y': 18.0460491}},
    'BabyLuigi':   {'curve': {'X': -0.100495219,    'Z': 1.24129128,    'Y': 17.8929539},       'charge': {'X': -0.204690278,   'Z': 1.14138937,    'Y': 18.3971405}},
    'Bowser':      {'curve': {'X': -1.1208117,      'Z': 2.37041189,    'Y': 17.7443905},       'charge': {'X': -0.935231805,   'Z': 2.83790755,    'Y': 17.9320602}},
    'Wario':       {'curve': {'X': -0.218430877,    'Z': 2.11808395,    'Y': 18.0982456},       'charge': {'X': -0.387497813,   'Z': 2.14200447,    'Y': 18.0287138}},
    'Waluigi':     {'curve': {'X': -0.0994037464,   'Z': 2.91129541,    'Y': 16.6599312},       'charge': {'X': -0.0872518569,  'Z': 2.91058898,    'Y': 16.6630745}},
    'KoopaR':      {'curve': {'X': -0.0643017143,   'Z': 1.38116789,    'Y': 18.2691517},       'charge': {'X': -0.0115943998,  'Z': 1.42475438,    'Y': 18.2572403}},
    'ToadR':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'Boo':         {'curve': {'X': -0.976979315,    'Z': 2.43798327,    'Y': 16.8721886},       'charge': {'X': -1.05723453,    'Z': 3.21649265,    'Y': 17.1067276}},
    'Toadette':    {'curve': {'X': -0.432494819,    'Z': 1.53251338,    'Y': 17.9790344},       'charge': {'X': -0.442466974,   'Z': 0.960499167,   'Y': 18.0559368}},
    'ShyGuyR':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'Birdo':       {'curve': {'X': -0.408602893,    'Z': 0.954139769,   'Y': 18.4027977},       'charge': {'X': -0.185714141,   'Z': 0.965393066,   'Y': 18.973381}},
    'Monty':       {'curve': {'X': -0.392196894,    'Z': 1.25717086,    'Y': 15.9324245},       'charge': {'X': -0.337694883,   'Z': 1.46883655,    'Y': 15.9852085}},
    'BowserJr':    {'curve': {'X': -1.17502844,     'Z': 0.908061326,   'Y': 18.7266293},       'charge': {'X': -0.954403996,   'Z': 1.51448655,    'Y': 18.1687946}},
    'ParatroopaR': {'curve': {'X': -0.0549990535,   'Z': 2.26200676,    'Y': 18.3726215},       'charge': {'X': 0.0554796606,   'Z': 2.54858708,    'Y': 18.4819603}},
    'PiantaB':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'PiantaR':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'PiantaY':     {'curve': {'X': -0.902026832,    'Z': 2.77712846,    'Y': 17.7310047},       'charge': {'X': -1.41902661,    'Z': 4.07295799,    'Y': 16.8742599}},
    'NokiB':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'NokiR':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'NokiG':       {'curve': {'X': -1.00128365,     'Z': 1.20490992,    'Y': 18.1284885},       'charge': {'X': -0.832903445,   'Z': 2.27637315,    'Y': 17.8932285}},
    'BroH':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
    'Toadsworth':  {'curve': {'X': -0.645938098,    'Z': 0.680195332,   'Y': 18.2057915},       'charge': {'X': -0.0759834051,  'Z': 1.17852771,    'Y': 18.0417519}},
    'ToadB':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadY':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadG':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'ToadP':       {'curve': {'X': 0.0409559123,    'Z': 1.2589829,     'Y': 17.795105},        'charge': {'X': 0.0392686874,   'Z': 1.24723339,    'Y': 17.8072586}},
    'MagikoopaB':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaR':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaG':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'MagikoopaY':  {'curve': {'X': -0.0110720694,   'Z': 1.12154889,    'Y': 17.2940254},       'charge': {'X': 0.274167657,    'Z': 1.36672831,    'Y': 17.4065056}},
    'KingBoo':     {'curve': {'X': -1.19448996,     'Z': 2.59314823,    'Y': 16.9215889},       'charge': {'X': -1.27474511,    'Z': 3.37165785,    'Y': 17.1561279}},
    'Petey':       {'curve': {'X': -0.541439176,    'Z': 1.78280687,    'Y': 17.56321},         'charge': {'X': -1.13070774,    'Z': 1.67450738,    'Y': 17.7182236}},
    'Dixie':       {'curve': {'X': -1.3091619,      'Z': 1.27092195,    'Y': 18.7103424},       'charge': {'X': -0.379683375,   'Z': 1.10366392,    'Y': 18.385828}},
    'Goomba':      {'curve': {'X': -0.294719875,    'Z': 1.01028323,    'Y': 17.451561},        'charge': {'X': -0.729693174,   'Z': 0.665731907,   'Y': 18.527298}},
    'Paragoomba':  {'curve': {'X': -0.795248866,    'Z': 2.18529749,    'Y': 18.4609985},       'charge': {'X': -0.7055155504,  'Z': 3.25615358,    'Y': 18.637495}},
    'KoopaG':      {'curve': {'X': -0.0643017143,   'Z': 1.38116789,    'Y': 18.2691517},       'charge': {'X': -0.0115943998,  'Z': 1.42475438,    'Y': 18.2572403}},
    'ParatroopaR': {'curve': {'X': -0.0549990535,   'Z': 2.26200676,    'Y': 18.3726215},       'charge': {'X': 0.0554796606,   'Z': 2.54858708,    'Y': 18.4819603}},
    'ShyGuyB':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyY':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyG':     {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'ShyGuyBk':    {'curve': {'X': -0.525757074,    'Z': 4.07900000,    'Y': 18.8315792},       'charge': {'X': -0.491243154,   'Z': 3.79274869,    'Y': 18.9465904}},
    'DryBonesGy':  {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesG':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesR':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'DryBonesB':   {'curve': {'X': -0.137758076,    'Z': 2.01307893,    'Y': 18.0202503},       'charge': {'X': -0.30223608,    'Z': 2.3172307,     'Y': 18.1311436}},
    'BroF':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
    'BroB':        {'curve': {'X': 0.276068062,     'Z': 3.39618778,    'Y': 19.1116161},       'charge': {'X': -0.770916998,   'Z': 2.54096055,    'Y': 18.5399666}},
}

pitchProperties = {'curve': {'minCurve': 25, 'maxCurve': 50, 'velocityAdjustment': 15, 'delay': 20},
                   'change': {'minCurve': 8, 'maxCurve': 10, 'velocityAdjustment': 30, 'delay': 35}}

batterHitbox = {
                'Mario':       {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Luigi':       {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.899999976158142, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 },
                'DK':          {'HitboxMultiplier': [1.11, 1.0], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.4000000059604645, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.6500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0 }, 
                'Diddy':       {'HitboxMultiplier': [1.18, 1.15], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.30000001192092896, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Peach':       {'HitboxMultiplier': [1.18, 1.08], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.5,                  'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Daisy':       {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6000000238418579,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Yoshi':       {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.049999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'BabyMario':   {'HitboxMultiplier': [1.2, 1.1], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.2999999523162842, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'BabyLuigi':   {'HitboxMultiplier': [1.2, 1.18], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.149999976158142, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Bowser':      {'HitboxMultiplier': [1.0, 0.8], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 1.4500000476837158,   'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 0.20000000298023224, 'EasyBattingSpotHorizontal': -3.5999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Wario':       {'HitboxMultiplier': [1.18, 1.06], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.75,                 'VerticalRangeFront': 0.4000000059604645, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.4000000953674316, 'EasyBattingSpotVertical': -1.600000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 },
                'Waluigi':     {'HitboxMultiplier': [1.0, 0.8], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'KoopaR':      {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.5,                  'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.1500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ToadR':       {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.949999988079071,    'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'Boo':         {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.4000000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.100000023841858, 'TrimmedBat': 0.0 }, 
                'Toadette':    {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.5,                  'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.7999999523162842, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'ShyGuyR':     {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Birdo':       {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'Monty':       {'HitboxMultiplier': [1.0, 0.92], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': 0.30000001192092896, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'BowserJr':    {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ParatroopaR': {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.200000047683716, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'PiantaB':     {'HitboxMultiplier': [1.2, 1.08], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'PiantaR':     {'HitboxMultiplier': [1.2, 1.08], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'PiantaY':     {'HitboxMultiplier': [1.2, 1.08], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.8500000238418579,   'VerticalRangeFront': 0.5, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'NokiB':       {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'NokiR':       {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'NokiG':       {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': 0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.2000000476837158, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'BroH':        {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0 }, 
                'Toadsworth':  {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -1.75, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 1.0 }, 
                'ToadB':       {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.44999998807907104,  'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'ToadY':       {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.44999998807907104,  'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'ToadG':       {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.44999998807907104,  'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'ToadP':       {'HitboxMultiplier': [1.4, 1.32], 'HorizontalRangeNear': -0.44999998807907104,  'HorizontalRangeFar': 0.44999998807907104,  'VerticalRangeFront': -0.6000000238418579, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'MagikoopaB':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6000000238418579,   'HorizontalRangeFar': 0.699999988079071,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'MagikoopaR':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6000000238418579,   'HorizontalRangeFar': 0.699999988079071,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'MagikoopaG':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6000000238418579,   'HorizontalRangeFar': 0.699999988079071,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'MagikoopaY':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6000000238418579,   'HorizontalRangeFar': 0.699999988079071,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'KingBoo':     {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.7999999523162842, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.2000000476837158, 'TrimmedBat': 0.0 }, 
                'Petey':       {'HitboxMultiplier': [1.1, 0.7], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.399999976158142, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.100000023841858, 'TrimmedBat': 0.0 }, 
                'Dixie':       {'HitboxMultiplier': [1.18, 1.15], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': 0.20000000298023224, 'VerticalRangeBack': 1.7000000476837158, 'EasyBattingSpotHorizontal': -1.600000023841858, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.2000000476837158, 'TrimmedBat': 0.0 }, 
                'Goomba':      {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': 0.0, 'VerticalRangeBack': 1.5, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 0.75, 'TrimmedBat': 0.0 }, 
                'Paragoomba':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.299999952316284, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'KoopaG':      {'HitboxMultiplier': [1.18, 1.1], 'HorizontalRangeNear': -0.5,                  'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.1500000953674316, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ParatroopaG': {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.600000023841858, 'EasyBattingSpotHorizontal': -2.0999999046325684, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ShyGuyB':     {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ShyGuyY':     {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ShyGuyG':     {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'ShyGuyBk':    {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.550000011920929,    'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.399999976158142, 'EasyBattingSpotHorizontal': -2.5, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'DryBonesGy':  {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'DryBonesG':   {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'DryBonesR':   {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'DryBonesB':   {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.75,                 'HorizontalRangeFar': 0.550000011920929,    'VerticalRangeFront': -0.10000000149011612, 'VerticalRangeBack': 1.2999999523162842, 'EasyBattingSpotHorizontal': -1.899999976158142, 'EasyBattingSpotVertical': -1.100000023841858, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 0.0 }, 
                'BroF':        {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0 }, 
                'BroB':        {'HitboxMultiplier': [1.2, 1.12], 'HorizontalRangeNear': -0.6499999761581421,   'HorizontalRangeFar': 0.6499999761581421,   'VerticalRangeFront': -0.20000000298023224, 'VerticalRangeBack': 1.2000000476837158, 'EasyBattingSpotHorizontal': -1.7000000476837158, 'EasyBattingSpotVertical': -1.0, 'BoxMoveSpeed': 0.05000000074505806, 'PitchingHeight': 1.0, 'TrimmedBat': 1.0 }
 }

# pitchAttributes = {
#     "curveball_charge": {

#     } 
# }
# do later

# Interpreter class to initialize values and allow values to be pulled
class Initializer():
    def __init__(self):
        self.memoryAddresses = initializeMemoryAddresses()
        self.characters = initializeCharacters()
    
    def getMemoryAddressValue(self, varname: str):
        return self.memoryAddresses[varname].read()
    
    def updateMemoryAddressValue(self, varname: str, value):
        return self.memoryAddresses[varname].write(value)
    
    def getCharacterStat(self, char, varname: str):
        return self.characters[char].stats[varname].value
    
    def getCharacterAllStats(self, char):
        return self.characters[char].stats
    
    def updateCharacterStat(self, char, varname: str, value):
        self.characters[char].stats[varname].value = value
        return self.characters[char].stats[varname].value


# Basic position, velocity, and acceleration classes
class Position():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, velocity):
        self.X += velocity.X
        self.Y += velocity.Y
        self.Z += velocity.Z

    def prnt(self):
        print("(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")")

class Velocity():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, acceleration):
        self.X += acceleration.X
        self.Y += acceleration.Y
        self.Z += acceleration.Z

    def update_mult(self, acceleration):
        self.X *= (1 + acceleration.X)
        self.Y *= (1 + acceleration.Y)
        self.Z *= (1 + acceleration.Z)

    def prnt(self):
        print("<" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ">")

class Acceleration():
    def __init__(self, X: float, Y: float, Z: float):
        self.X = X
        self.Y = Y
        self.Z = Z

    def update(self, new_acceleration):
        self.X = new_acceleration.X
        self.Y = new_acceleration.Y
        self.Z = new_acceleration.Z

    def prnt(self):
        print("(" + str(self.X) + ", " + str(self.Y) + ", " + str(self.Z) + ")")

# Pitcher contains pitcher info
class Pitcher():
    def __init__(self, initializer: Initializer):
        self.pitcher_id = initializer.getMemoryAddressValue('pitcher_id')
        self.pitcher = str(memory_values.CharacterID(self.pitcher_id).name)
        self.pitcherHand = initializer.getMemoryAddressValue('pitcher_hand')
        initializer.updateCharacterStat(self.pitcher, 'fielding_arm', self.pitcherHand)
        self.curve = initializer.getCharacterStat(self.pitcher, 'curve')
        self.curve_control = initializer.getCharacterStat(self.pitcher, 'curve_control')
        self.curveBallSpeed = initializer.getCharacterStat(self.pitcher, 'curve_ball_speed')
        self.fastBallSpeed = initializer.getCharacterStat(self.pitcher, 'fast_ball_speed')
        self.pitcherStats = initializer.getCharacterAllStats(self.pitcher)

        self.isTired = 0

    def returnPitcherHand(self):
        if self.pitcherHand == 0:
            return 'Right'
        else:
            return 'Left'
        
class Batter():
    def __init__(self, initializer: Initializer):
        self.batter_id = initializer.getMemoryAddressValue('batter_id')
        self.batter = str(memory_values.CharacterID(self.batter_id).name)
        self.batterHand = initializer.getMemoryAddressValue('batter_hand')


class Ball():
    def __init__(self):
        self.position = None
        self.velocity = None
        self.acceleration = None

    def update(self, value):
        if type(value) is Velocity:
            self.position.X += value.X
            self.position.Y += value.Y
            self.position.Z += value.Z
            return self.position
        
        elif type(value) is Acceleration:
            self.velocity.X += value.X
            self.velocity.Y += value.Y
            self.velocity.Z += value.Z
            return self.velocity

    def add(self, obj1, obj2):
            obj1.X += obj2.X
            obj1.Y += obj2.Y
            obj1.Z += obj2.Z

            if type(obj1) is Position:
                self.position = obj1
            elif type(obj1) is Velocity:
                self.velocity = obj1
            elif type(obj1) is Acceleration:
                self.acceleration = obj1
            return obj1
    
    def update_mult(self, acceleration):
        self.velocity.X *= (1 + acceleration.X)
        self.velocity.Y *= (1 + acceleration.Y)
        self.velocity.Z *= (1 + acceleration.Z)
        return self.velocity


class PitchProperties():
    def __init__(self, initializer: Initializer, pitcher: Pitcher, type:str, chargeUp = 0, moundPositionX = None):
        self.pitcher = pitcher
        self.type = type
        self.pitchType = pitchTypes[type]
        self.chargeUp = chargeUp

        if moundPositionX is None:
            moundPositionX = initializer.getMemoryAddressValue('pitcher_mound_position_x')

        self.moundPositionX = moundPositionX
        
        self.minCurve = pitchProperties[self.pitchType['pitchProperty']]['minCurve']
        self.maxCurve = pitchProperties[self.pitchType['pitchProperty']]['maxCurve']
        self.delay = pitchProperties[self.pitchType['pitchProperty']]['delay']
        self.velocityAdjustment = pitchProperties[self.pitchType['pitchProperty']]['velocityAdjustment']
        self.pitchBaseReleaseCoordinates = pitchBaseReleaseCoordinates[pitcher.pitcher][self.pitchType['pitchBaseReleaseCoordinates']]
        self.curve = pitcher.curve

        def returnAirResistanceVelocityAdjustment():
            return (0.001 * pitchProperties[self.pitchType['pitchProperty']]['velocityAdjustment'])
        
        # Initialize Air Resistance Info
        self.airResistanceVelocityAdjustment = returnAirResistanceVelocityAdjustment()
        self.decelerationFactor = 0.998
        
        
        # Each Pitch has it's own affect on speed
        def returnPitchSpeed(type, chargeUp):
            pitchSpeed = 0
            if type == 'curve':
                pitchSpeed = pitcher.curveBallSpeed
            elif type == 'charge':
                fastBallSpeed = pitcher.fastBallSpeed
                curveBallSpeed = pitcher.curveBallSpeed
                pitchSpeed = fastBallSpeed - math.floor(0.85 * (fastBallSpeed - curveBallSpeed)* (1 - chargeUp))
            elif type == 'perfect':
                pitchSpeed = math.floor(pitcher.fastBallSpeed * 1.05)
            elif type == 'change':
                pitchSpeed = pitcher.curveBallSpeed
            return pitchSpeed
        
        # Front of Plate Y for initial Velocity
        self.frontOfPlateY = 0.5 * (1.05 + 0.5)
        
        self.initialPositionY = self.pitchBaseReleaseCoordinates['Y']
        self.initialVelocityY = returnPitchSpeed(type, chargeUp)/-240

        def returnAirResistanceStartingY(delay):
            return (18.44* (100 - delay)/100)
        
        delay = pitchProperties[self.pitchType['pitchProperty']]['delay']
        self.airResistanceStartingY = returnAirResistanceStartingY(delay)


        # Z ---------------------------------------------------------------------------

        def returnBatPositionZ(char: str):
            return batterHitbox[char]['PitchingHeight'] * batterHitbox[char]['HitboxMultiplier'][0]
        
        # Bat Height for Z for initial Velocity
        batHeightZ = returnBatPositionZ(self.pitcher.pitcher)

        self.initialPositionZ = self.pitchBaseReleaseCoordinates['Z']
        self.initialVelocityZ = (((self.initialPositionZ - batHeightZ) * self.initialVelocityY) / (self.initialPositionY - self.frontOfPlateY))
        


        # Start X-----------------------------------------

        def returnCurveInterpolation():
            return 0.00005 * linearInterpolateToNewRange(self.curve, 1, 100, self.minCurve, self.maxCurve)
        
        def returnCurveControl():
            framesUntilFullControl = linearInterpolateToNewRange(pitcher.curve_control, 1, 100, 8, 2)
            if framesUntilFullControl < 1:
                return 1
            return framesUntilFullControl
        
        # Initialize Curve Info
        self.curveInterpolation = returnCurveInterpolation()
        self.curveControl = returnCurveControl()
        self.curveControlInterpolation = self.curveInterpolation/self.curveControl

        if pitcher.pitcherHand == 1:
            pitchBaseReleaseCoordinatesX = -1*self.pitchBaseReleaseCoordinates['X']
        else:
            pitchBaseReleaseCoordinatesX = self.pitchBaseReleaseCoordinates['X']


        self.initialPositionX = pitchBaseReleaseCoordinatesX + self.moundPositionX
        self.initialVelocityX = (((pitchBaseReleaseCoordinatesX - self.moundPositionX) * self.initialVelocityY) / (self.initialPositionY - self.frontOfPlateY))

    
        

class PitchXYZ():
    def __init__(self, pitchProperties: PitchProperties):
        self.pitchProperties = pitchProperties

        self.initialVelocity = [pitchProperties.initialVelocityX, pitchProperties.initialVelocityY, pitchProperties.initialVelocityZ]
        self.initialPosition = [pitchProperties.initialPositionX, pitchProperties.initialPositionY, pitchProperties.initialPositionZ]

        self.framesUncontrolable = 0
        self.framesUntilAirResistance = 0

        self.decelerationFactor = 0.998
        self.currCurveValue = 0
        self.velocityX = pitchProperties.initialVelocityX

        self.lengthX = 0
        self.frameX = 1

    def returnPositionYZ(self):
        # Y ---------------------------------------------------------------
        initialPositionY = self.initialPosition[1]
        Y = [initialPositionY]

        # Initial Position
        initialVelocityY = self.initialVelocity[1]
        positionY = initialPositionY
        velocityY = initialVelocityY

        # Z ---------------------------------------------------------------
        initialPositionZ = self.initialPosition[2]
        Z = [initialPositionZ]

        initialVelocityZ = self.initialVelocity[2]
        positionZ = initialPositionZ
        velocityZ = initialVelocityZ

        # Calc Y and Z -----------------------------------------------------
        while positionY > -3:

            if positionY >= self.pitchProperties.airResistanceStartingY:
                self.framesUntilAirResistance = len(Y)
            else:
                velocityY *= 1 - self.pitchProperties.airResistanceVelocityAdjustment
            
            velocityY *= self.decelerationFactor
            velocityZ *= self.decelerationFactor

            positionY += velocityY
            positionZ += velocityZ

            if positionY >= 18.44:
                self.framesUncontrolable = len(Y)

            Y.append(positionY)
            Z.append(positionZ)

        self.lengthX = len(Y)

        return Y, Z
    
    def returnNextPositionX(self, input, X):

        XPosition = X


        def returnCurveVelocity(input):
            prevCurveValue = self.currCurveValue

            curveControlInterpolation = self.pitchProperties.curveControlInterpolation
            curveInterpolation = self.pitchProperties.curveInterpolation

            # if no input
            if (input == 0):
                if (prevCurveValue >= 0):
                    self.currCurveValue = prevCurveValue - curveControlInterpolation
                    if (self.currCurveValue < 0):
                        self.currCurveValue = 0
                else:
                    self.currCurveValue = prevCurveValue + curveControlInterpolation
                    if (self.currCurveValue > 0):
                        self.currCurveValue = 0
            # else if left or right inputted
            else:
                self.currCurveValue = prevCurveValue + (input * curveControlInterpolation)
            
            # self correct to make sure curve is within min and max curve
            if self.currCurveValue < -curveInterpolation:
                self.currCurveValue = -curveInterpolation
            elif self.currCurveValue > curveInterpolation:
                self.currCurveValue = curveInterpolation

            return self.currCurveValue
        
        self.currCurveValue = returnCurveVelocity(input)
        
        if self.frameX > self.framesUntilAirResistance:
            self.velocityX *= (1-self.pitchProperties.airResistanceVelocityAdjustment)

        self.velocityX *= self.decelerationFactor
        self.velocityX += self.currCurveValue

        XPosition += self.velocityX

        self.frameX += 1

        return XPosition
    
    def initializeBufferFrames(self):
        return [0]*self.framesUncontrolable
    
    def initializeXBufferPositions(self):
        X = [None] * self.lengthX
        X[0] = self.initialPosition[0]
        for i in range(1, self.framesUncontrolable+1):
            X[i] = self.returnNextPositionX(0, X[i-1])

        return X
    


def displayPlot(X, Y, Z):
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure = False)
    # ax.set_title(str(self.pitch.pitcher.pitcher) + " (" + self.pitch.pitcher.returnPitcherHand() + \
    #                 " Handed): " + self.pitch.pitchTypeName +" \n10 Input Frames Right & 20 input Frames Left")
    fig.add_axes(ax)
    batHeight = 0

    x = [0.53, 0.53, -0.53]
    y = [0.5, 1.05, 1.05]
    z = [0, 0, 0]

    x1 = [-0.53, -0.53, 0.53]
    y1 = [0.5, 1.05, 0.5]
    z1 = [0, 0, 0]

    x2 = [0.4, 0.4, -0.4]
    y2 = [18.44, 19, 19]
    z2 = [0, 0, 0]

    x3 = [-0.4, -0.4, 0.4]
    y3 = [18.44, 19, 18.44]
    z3 = [0, 0, 0]

    strikeZone = [list(zip(x,y,z))]
    strikeZone1 = [list(zip(x1,y1,z1))]
    pitchingMound = [list(zip(x2,y2,z2))]
    pitchingMound1 = [list(zip(x3,y3,z3))]

    ax.add_collection3d(Poly3DCollection(strikeZone))
    ax.add_collection3d(Poly3DCollection(strikeZone1))
    ax.add_collection3d(Poly3DCollection(pitchingMound))
    ax.add_collection3d(Poly3DCollection(pitchingMound1))

    ax.scatter(X, Y, Z)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-3, 20])
    ax.set_zlim([0, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()




def main():

    initializer = Initializer()
    pitcher = Pitcher(initializer)
    pitchProperties = PitchProperties(initializer, pitcher, 'curve', 0, 0)
    pitch = PitchXYZ(pitchProperties)

    [Y, Z] = pitch.returnPositionYZ()
    X = pitch.initializeXBufferPositions()

    for i in range(pitch.framesUncontrolable + 1, len(X)):
        X[i] = pitch.returnNextPositionX(0, X[i-1])

    print(pitch.frameX)
    print(len(X))
    #displayPlot(X, Y, Z)






if __name__ == '__main__':
    main()



