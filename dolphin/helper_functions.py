import math

# rewritting Nuche's code in python :)
# https://github.com/ProjectRio/ProjectRio-frontend/blob/main/src/lib/helpers/MssbFunctions/mssbHelpers.ts
# these functions might not actually be useful because I can just read the values


def linearInterpolateToNewRange(value, prevMin, prevMax, nextMin, nextMax):
  min = 0.0
  max = 0.0
  calcValue = 0.0

  # adjusts previous range to return a range that reflects new inputs
  if (min == (prevMax - prevMin)):
      max = 1.0
  else:
      max = 1.0
      calcValue = (value - prevMin) / (prevMax - prevMin)

      if calcValue <= max:
          max = calcValue
          if (calcValue < min):
              max = min
  # returns adjusted max
  return (((nextMax - nextMin) * max) + nextMin)


def randBetween(param_1, param_2, StaticRandomInt1, StaticRandomInt2, TotalframesAtPlay):
  
  uVar4 = (param_2 - param_1) + 1
  iVar5 = (uVar4 >> 0x1f ^ uVar4) - (uVar4 >> 0x1f)
  if (iVar5 < 2):
    iVar5 = 0

  else:
    StaticRandomInt1 = \
         (StaticRandomInt1 - (StaticRandomInt2 & 0xff)) + \
         math.floor(StaticRandomInt2 / iVar5) + TotalframesAtPlay

    uVar1 = StaticRandomInt1 - (StaticRandomInt1 / iVar5) * iVar5
    uVar3 = math.floor(uVar1) >> 0x1f
    iVar5 = (uVar3 ^ uVar1) - uVar3
    if (uVar4 < 0):
      iVar5 = -iVar5
    
  return param_1 + iVar5


def RandomInt_Game(MaxNum, StaticRandomInt1, StaticRandomInt2, TotalframesAtPlay):
  
  randomNum = (MaxNum >> 0x1f ^ MaxNum) - (MaxNum >> 0x1f)
  if (randomNum < 2):
    randomNum = 0
  else:
    StaticRandomInt1 = \
         (StaticRandomInt1 - (StaticRandomInt2 & 0xff)) + \
         StaticRandomInt2 / randomNum + TotalframesAtPlay
    
    uVar2 = StaticRandomInt1 - (StaticRandomInt1 / randomNum) * randomNum
    uVar3 = math.floor(uVar2) >> 0x1f
    randomNum = (uVar3 ^ uVar2) - uVar3
    if (MaxNum < 0):
      randomNum = -randomNum
  
  return randomNum


def randomInRange(param_1, param_2, StaticRandomInt1, StaticRandomInt2, TotalframesAtPlay):
  # sometimes the decomp only sends 1 parameter. 
  # When this happens, I think parameter 1 is the negative version, 
  # and 2 is the positive version.

  # I honestly have no clue what this does. too lazy

  uVar4 = 0
  const_7 = (1000 * (param_2 - param_1)) + 1
  const_7_ = const_7
  if (const_7 < 0):
    const_7_ = -const_7

  if (const_7_ < 2):
    uVar1 = 0
  else:
    StaticRandomInt1 = \
         (StaticRandomInt1 - (StaticRandomInt2 & 0xff)) +\
         StaticRandomInt2 / const_7_ + TotalframesAtPlay

    uVar2 = StaticRandomInt1 - (StaticRandomInt1 / const_7_) * const_7_
    uVar1 =  math.floor(uVar2) >> 0x1f
    uVar1 = (uVar1 ^ uVar2) - uVar1
    if (const_7 < 0):
        uVar1 = -uVar1
      
  local_28 = uVar1
  return [(0.001 * (local_28) + param_1), StaticRandomInt1, StaticRandomInt2, TotalframesAtPlay]

