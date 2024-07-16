import os
from pad import *

class PadBasicActions():
    """Writes out controller inputs."""
    def __init__(self, path):
        """Create, but do not open the fifo."""
        self.pipe = None
        self.path = path
        try:
            os.mkfifo(self.path)
        except OSError:
            pass

    def __enter__(self):
        """Opens the fifo. Blocks until the other side is listening."""
        self.pipe = open(self.path, 'w', buffering=1)
        return self

    def __exit__(self, *args):
        """Closes the fifo."""
        if self.pipe:
            self.pipe.close()

    def press_button(self, *args):
        """Press Buttons"""
        for arg in args:
            assert arg in Button
            self.pipe.write('PRESS {}\n'.join(arg.name))
        

    def release_button(self, *args):
        """Release a button."""
        for arg in args:
            assert arg in Button
            self.pipe.write('RELEASE {}\n'.join(arg.name))

    def press_start_button(self):
        self.pipe.write('PRESS START\n')

    def release_start_button(self):
        self.pipe.write('RELEASE START\n')

    def press_trigger(self, *args):
        """Press a trigger"""
        for arg in args:
            assert arg in Trigger
            self.pipe.write('SET {} {:.2f}\n'.join(arg.name, 1.0))

    def release_trigger(self, *args):
        """Release a Trigger."""
        for arg in args:
            assert arg in Trigger
            self.pipe.write('SET {} {:.2f}\n'.join(arg.name, 0.0))

    def tilt_stick(self, *args):

        for arg in args:
            assert arg in Stick or Base

            x = arg.value[0]
            y = arg.value[1]

            """Tilt a stick"""
            assert 0.0 <= x <= 1.0
            assert 0.0 <= y <= 1.0
            self.pipe.write('SET MAIN {:.2f} {:.2f}\n'.join(x, y))

    def release_stick(self):
        """Release stick"""
        self.pipe.write('SET MAIN {:.2f} {:.2f}\n'.join(0.5, 0.5))

    

    # def release_stick(self, *args):
    #     """Release a Stick."""
    #     for arg in args:
    #         assert arg in Stick
    #     self.pipe.write('RESET %s' % ', '.join(arg.name for arg in args))




class PadSubActions(PadBasicActions):

    def reset(self):
        self.press_trigger(Trigger.L)
        self.release_trigger(Trigger.L)
        for button in Button:
            self.release_button(button)
        self.release_start_button()
        self.release_trigger(Trigger.R)
        self.release_stick()


    def sprint(self):
        self.press_button(Button.B)
        self.release_button(Button.B)

    def jump(self):
        self.release_stick()
        self.press_button(Button.A)
        self.release_button(Button.A)
        self.release_stick()

    #def walljump(self):

    def dive(self, directions):
        self.tilt_stick(directions)
        self.press_button(Button.A)
        self.release_button(Button.A)
        self.release_stick()


    def advance_runner_to(self, base):
        assert base is Base
        self.tilt_stick(base)
        self.press_button(Button.Y)
        self.release_button(Button.Y)
        self.release_stick()


    def return_runner_to(self, base):
        assert base is Base
        self.tilt_stick(base)
        self.press_button(Button.X)
        self.release_button(Button.X)
        self.release_stick()

    def return_to_main_menu(self):
        self.press_start_button()
        self.release_start_button()

        i = 0
        while(i<19):
            self.tilt_stick(Stick.down)
            self.release_stick()
            i += 1

        self.press_button(Button.A)
        self.release_button(Button.A)

        self.tilt_stick(Stick.left)
        self.release_stick()

        self.press_button(Button.A)
        self.release_button(Button.A)




    