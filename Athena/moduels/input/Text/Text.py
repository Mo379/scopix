from _src.networks.DummyNet.DummyNet import DummyNet


class _Input_text():
    def __init__(self, Logger, FlashMemory, CrystalMemory):
        """ Initialising the text input sensor
        """
        self.Logger = Logger
        self.FlashMemory = FlashMemory
        self.CrystalMemory = CrystalMemory

    def _waking_fun(self):
        """ The waking function of the text input sensor
        """
        if self.Logger():
            pass
        pass

    def _learning_fun(self):
        """ The waking function of the text input sensor
        """
        pass

    def _sleeping_fun(self):
        """ The input have no sleeping functions
        """
        pass

    def _turnoff_fun(self):
        """ The turning off function of the text input sensor

        This function deletes the output variables of this moduel
        """
        pass
