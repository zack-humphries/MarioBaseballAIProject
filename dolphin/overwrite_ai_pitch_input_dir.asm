# To be inserted at 806b00a0
# Source function: pitchCurve @ 0x806AFF88
# injection location: 806B00A0 (else statement branches to AI input selection function)

### this would be where you'd inject the value if you just wanted to do a raw write instead of calling the function. the other variation loads a value into r12 and then skips the ai function
# li r3, [YOUR VALUE HERE] ## raw write (0x0 no dir, 0x1 right, 0xFF left)


##### ACTUAL CODE #####

### uncomment and replace XXXX with the top and YYYY with bottom of the address you're reading from
# lis r12, 0xXXXX (load byte from memory indicating which direction to go) 
# ori r12, 0xYYYY
# lbz r12, 0x0(r12)


### check if inputs are legal
cmpwi r12, 0x1
beq LOAD_CUSTOM_INPUT

cmpwi r12, 0x0
beq LOAD_CUSTOM_INPUT

cmpwi r12, 0xFF
beq LOAD_CUSTOM_INPUT

b CALL_FUNCTION # failsafe in case it somehow receives an invalid value

LOAD_CUSTOM_INPUT:
  mr r3, r12 # skip the function call and just write the input to r3



CALL_FUNCTION:
  lis r12, 0x8065
  ori r12, r12, 0xfd80
  mtctr r12
  bctrl