from moduels.input.Text.Text import _Input_text


class _Orchistrator():
    """"""
    def __init__(self, Logger, FlashMemory, CrystalMemory):
        self.Logger = Logger
        self.FlashMemory = FlashMemory
        self.CrystalMemory = CrystalMemory
        #
        self.input_moduels = [
                _Input_text(self.Logger, self.FlashMemory, self.CrystalMemory),
            ]
        self.latent_moduels = [
            ]
        self.output_moduels = [
            ]

    def _orchistrate(self):
        """Orchistrates the entire network's connections"""
        def turnoff_fun():
            for input_mod in self.input_moduels:
                input_mod._turnoff_fun()
            for latent_mod in self.input_moduels:
                latent_mod._turnoff_fun()
            for output_mod in self.input_moduels:
                output_mod._turnoff_fun()
            if self.Logger:
                self.Logger._finish()
        self.turnoff_fun = turnoff_fun

        def waking_fun():
            for input_mod in self.input_moduels:
                input_mod._waking_fun()
            for latent_mod in self.input_moduels:
                latent_mod._waking_fun()
            for output_mod in self.input_moduels:
                output_mod._waking_fun()
        self.waking_fun = waking_fun

        def learning_fun():
            for input_mod in self.input_moduels:
                input_mod._learning_fun()
            for latent_mod in self.input_moduels:
                latent_mod._learning_fun()
            for output_mod in self.input_moduels:
                output_mod._learning_fun()
        self.waking_fun = waking_fun

        def sleeping_fun():
            for input_mod in self.input_moduels:
                input_mod._sleeping_fun()
            for latent_mod in self.input_moduels:
                latent_mod._sleeping_fun()
            for output_mod in self.input_moduels:
                output_mod._sleeping_fun()
        self.sleeping_fun = sleeping_fun

