import time
from _src.memory.FlashMemory import _FlashMemory
from _src.memory.CrystalMemory import _CrystalMemory
from _src.logger.WANDB import _WANDBLogger
from moduels.Orchistrator import _Orchistrator


class Athena():
    """ The Athena highest level composer/operator

    This class enables athena to operate with all of her different components
    from from memory and networks to cues and other services required for
    correct operation.
    """
    def __init__(self, seed=0, logging=False):
        self.seed = seed
        self.Logger = _WANDBLogger() if logging else None
        self.FlashMemory = _FlashMemory()
        self.CrystalMemory = _CrystalMemory()
        self.Orchistrator = _Orchistrator(
                self.seed,
                self.Logger,
                self.FlashMemory,
                self.CrystalMemory
            )
        self.state_dict = {
                b'off': 0,
                b'wake': 1,
                b'learning': 2,
                b'sleeping': 3,
            }

    def wake(self):
        self.FlashMemory._create('athena_state', 'wake')
        self.Orchistrator._orchistrate()
        current = 'wake'
        while True:
            state = self.FlashMemory._read('athena_state')
            # Logging the current state
            if self.Logger:
                self.Logger._log({'state': self.state_dict[state]})
            # Printing state changes
            if state != current:
                print(state)
            # Off state code
            if state == b'off':
                # Turn off
                self.Orchistrator.turnoff_fun()
                break
            # Awake state code
            elif state == b'wake':
                # Start operations
                self.Orchistrator.waking_fun()
            # Learning state code
            elif state == b'learning':
                # Switch to sleep mode
                self.Orchistrator.learning_fun()
            # Sleeping state code
            elif state == b'sleeping':
                # Switch to sleep mode
                self.Orchistrator.sleeping_fun()
            current = state
