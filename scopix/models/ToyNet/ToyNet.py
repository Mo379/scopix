import jax
import haiku as hk


class ToyNet(hk.Module):
    NetName = 'ToyNet'

    def __init__(
            self,
            n_hidden,
            hidden_size,
            output_size,
            name='ToyNet'
            ):
        super().__init__(name=name)
        self.hidden_size = hidden_size
        self.output_size = output_size

    def __call__(self, x):
        x = hk.Linear(
                output_size=self.hidden_size,
                name=None,
            )(x)
        x = jax.nn.relu(x)
        x = hk.Linear(
                output_size=self.output_size,
                with_bias=False,
                name=None,
            )(x)
        return x
