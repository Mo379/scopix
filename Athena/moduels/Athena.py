import time
from _src.memory.FlashMemory import _FlashMemory
from _src.memory.CrystalMemory import _CrystalMemory
from moduels.Orchistrator import _Orchistrator


class Athena():
    """ The Athena highest level composer/operator

    This class enables athena to operate with all of her different components
    from from memory and networks to cues and other services required for
    correct operation.
    """
    def __init__(self):
        self.FlashMemory = _FlashMemory()
        self.CrystalMemory = _CrystalMemory()
        self.Orchistrator = _Orchistrator(self.FlashMemory, self.CrystalMemory)

    def wake(self):
        self.FlashMemory._create('athena_state', 'wake')
        self.Orchistrator._orchistrate()
        current = 'wake'
        while True:
            state = self.FlashMemory._read('athena_state')
            if state != current:
                print(state)
            if state == b'off':
                # Turn off
                self.Orchistrator.turnoff_fun()
                break
            elif state == b'wake':
                # Start operations
                self.Orchistrator.waking_fun()
            elif state == b'sleeping':
                # Switch to sleep mode
                self.Orchistrator.sleeping_fun()
            current = state
