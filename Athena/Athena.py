from _src.CrystalMemory import _CrystalMemory


class Athena():
    """ The Athena highest level athena composer/operator

    This class enables athena to operate with all of her different components
    from from memory and networks to cues and other services required for
    correct operation.
    """
    def __init__(self):
        self.CrystalMemory = _CrystalMemory()

    def _sleep(self):
        self.CrystalMemory._disconnect()
