from memorylib import Dolphin


class MemoryAddress():
    def __init__(self, address, type: str):
        if type not in ['int6', 'uint8', 'float', 'int16', 'uint16', 'int32', 'uint32']:
            AssertionError

        self.address = address
        self.type = type


def initializeMemoryAddresses():
    blah
 

def main():
    dolphin = Dolphin()

    hand = MemoryAddress(0x8089296b, 'int8')

    if dolphin.hook():
        print(dolphin.read(hand.address, hand.type)) # reading doesn't work but writing does?
        print(dolphin.read_int8(hand.address))
        #numberOfStrikes.write(1)


if __name__ == '__main__':
    main()