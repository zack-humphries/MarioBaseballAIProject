import os
from pad import *
from memorylib import *
import math

class PadBasicActions(Dolphin):

    def __init__(self, dolphin: Dolphin, player):

        self.dolphin = dolphin
        self.player = player
        self.buttons = 0
        self.sticktrigger = 0

    def applyInputs(self):

        print(str(self.player.buttonAddress) + " " + str(self.buttons) + "     " + str(self.player.stickAddress) + " " + str(self.sticktrigger))

        self.dolphin.write_int8(self.player.buttonAddress, self.buttons)
        self.dolphin.write_int8(self.player.stickAddress, self.sticktrigger)

    def findClosestPow2(self, num):
        closestlog2 = math.floor(math.log2(num))

        return (2**closestlog2)

        
    def convertPow2TypeToInputs(self):

        tempvalue = self.sticktrigger
        templist = []

        if (tempvalue != 0):
            while tempvalue != 0:
                temppow2 = self.findClosestPow2(tempvalue)
                templist.append(temppow2)
                tempvalue = tempvalue - temppow2
            return templist
        
        return [tempvalue]
    
    def returnStickOpposite(self, input):
        assert input in Stick

        if input == Stick.LEFT:
            return Stick.RIGHT
        elif input == Stick.RIGHT:
            return Stick.LEFT
        elif input == Stick.DOWN:
            return Stick.UP
        elif input == Stick.UP:
            return Stick.DOWN


    def autoSubtract(self, input):
        # Auto Adjusts if someone inputs left and then right or up and then down 
        # so they dont have to "release" left/whatever stick input

        allInputValues = self.convertPow2TypeToInputs()

        oppositeStickInput = self.returnStickOpposite(input)

        if oppositeStickInput.value in allInputValues:
            self.sticktrigger -= oppositeStickInput.value


    def input(self, *args):

        for arg in args:
            if arg in Button or Start:
                self.buttons += arg.value
            elif arg in Trigger:
                self.sticktrigger += arg.value
            elif arg in Stick:
                self.autoSubtract(arg)
                self.sticktrigger += arg.value
            else:
                assert arg in Button or Start or Stick or Trigger
        
        self.applyInputs()

    def releaseInput(self, *args):
        for arg in args:
            if arg in Button or Start:
                self.buttons -= arg.value
            elif arg in Stick or Trigger:
                self.sticktrigger -= arg.value
            else:
                assert arg in Button or Start or Stick or Trigger
        
        self.applyInputs()

    def releaseAllInputs(self):
        self.buttons = 0
        self.sticktrigger = 0
        self.applyInputs()

    def releaseStick(self):
        if self.sticktrigger <= Trigger.Z.value:
            self.sticktrigger = 0
        elif self.sticktrigger >= Trigger.Z.value and self.sticktrigger < Trigger.R.value:
            self.sticktrigger = Trigger.Z.value
        elif self.sticktrigger >= Trigger.R.value and self.sticktrigger < Trigger.L.value:
            self.sticktrigger = Trigger.R.value
        else:
            self.sticktrigger = Trigger.L.value






    # """Writes out controller inputs."""
    # def __init__(self, path):
    #     """Create, but do not open the fifo."""
    #     self.pipe = None
    #     self.path = path
    #     try:
    #         os.mkfifo(self.path)
    #     except OSError:
    #         pass

    # def __enter__(self):
    #     """Opens the fifo. Blocks until the other side is listening."""
    #     self.pipe = open(self.path, 'w', buffering=1)
    #     return self

    # def __exit__(self, *args):
    #     """Closes the fifo."""
    #     if self.pipe:
    #         self.pipe.close()

    # def press_button(self, *args):
    #     """Press Buttons"""
    #     for arg in args:
    #         assert arg in Button
    #         self.pipe.write('PRESS {}\n'.join(arg.name))
        

    # def release_button(self, *args):
    #     """Release a button."""
    #     for arg in args:
    #         assert arg in Button
    #         self.pipe.write('RELEASE {}\n'.join(arg.name))

    # def press_start_button(self):
    #     self.pipe.write('PRESS START\n')

    # def release_start_button(self):
    #     self.pipe.write('RELEASE START\n')

    # def press_trigger(self, *args):
    #     """Press a trigger"""
    #     for arg in args:
    #         assert arg in Trigger
    #         self.pipe.write('SET {} {:.2f}\n'.join(arg.name, 1.0))

    # def release_trigger(self, *args):
    #     """Release a Trigger."""
    #     for arg in args:
    #         assert arg in Trigger
    #         self.pipe.write('SET {} {:.2f}\n'.join(arg.name, 0.0))

    # def tilt_stick(self, *args):

    #     for arg in args:
    #         assert arg in Stick or Base

    #         x = arg.value[0]
    #         y = arg.value[1]

    #         """Tilt a stick"""
    #         assert 0.0 <= x <= 1.0
    #         assert 0.0 <= y <= 1.0
    #         self.pipe.write('SET MAIN {:.2f} {:.2f}\n'.join(x, y))

    # def release_stick(self):
    #     """Release stick"""
    #     self.pipe.write('SET MAIN {:.2f} {:.2f}\n'.join(0.5, 0.5))

    

    # # def release_stick(self, *args):
    # #     """Release a Stick."""
    # #     for arg in args:
    # #         assert arg in Stick
    # #     self.pipe.write('RESET %s' % ', '.join(arg.name for arg in args))



    all     = Stick.NONE
    first   = Stick.RIGHT
    second  = Stick.UP
    third   = Stick.LEFT
    home    = Stick.DOWN


    def reset(self):
        self.input(Trigger.L)
        self.releaseInput(Trigger.L)
        self.releaseAllInputs()


    def sprint(self):
        self.input(Button.B)
        self.releaseInput(Button.B)

    def jump(self):
        self.releaseStick()
        self.input(Button.A)
        self.releaseInput(Button.A)
    
    #def walljump(self):

    # def dive(self, directions):
    #     self.tilt_stick(directions)
    #     self.press_button(Button.A)
    #     self.release_button(Button.A)
    #     self.release_stick()


    def advance_runner_to(self, base):
        self.releaseStick()
        self.input(base, Button.Y)
        self.releaseInput(Button.Y)
        self.releaseStick()


    def return_runner_to(self, base):
        self.releaseStick()
        self.input(base, Button.X)
        self.releaseInput(Button.X)
        self.releaseStick()



    def return_to_main_menu(self):
        self.releaseAllInputs()
        self.input(Start.START)
        self.releaseInput(Start.START)

        i = 0
        while(i<19):
            self.input(Stick.DOWN)
            self.releaseInput(Stick.DOWN)
            i += 1
        
        self.input(Button.A)
        self.releaseInput(Button.A)

        self.input(Stick.LEFT)
        self.releaseStick()

        self.input(Button.A)
        self.releaseInput(Button.A)



def main():
    dolphin = Dolphin()
    player1 = Player1()
    actions = PadBasicActions(dolphin, player1)
    if dolphin.hook():
        print(dolphin.read_int8(player1.buttonAddress))
        actions.return_to_main_menu()
    else:
        print("ERROR")

if __name__ == '__main__':
    main()
    