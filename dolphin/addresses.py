from memorylib import Dolphin


class MemoryAddress():
    def __init__(self, dolphin: Dolphin, address):
        self.dolphin = dolphin
        self.address = address

    # to be overwritten by subclasses
    def read(self):
        pass
    def write(self):
        pass


class uint32(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_uint32(self.address)

    def write(self, val): 
        self.dolphin.write_uint32(self.address, val) 


class uint16(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_uint16(self.address)

    def write(self, val): 
        self.dolphin.write_uint16(self.address, val) 


class uint8(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_uint8(self.address)

    def write(self, val): 
        self.dolphin.write_uint8(self.address, val) 


class int32(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_int32(self.address)

    def write(self, val): 
        self.dolphin.write_int32(self.address, val) 


class int16(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_int16(self.address)

    def write(self, val): 
        self.dolphin.write_int16(self.address, val) 


class int8(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_int8(self.address)

    def write(self, val): 
        self.dolphin.write_int8(self.address, val) 


class float(MemoryAddress):
    def __init__(self, dolphin, address):
        super().__init__(dolphin, address)

    def read(self):
        self.dolphin.read_float(self.address)

    def write(self, val): 
        self.dolphin.write_float(self.address, val) 


def main():
    dolphin = Dolphin()

    numberOfStrikes = uint8(dolphin, 0x8089296b)

    if dolphin.hook():
        print(numberOfStrikes.read()) # reading doesn't work but writing does?
        numberOfStrikes.write(1)


if __name__ == '__main__':
    main()