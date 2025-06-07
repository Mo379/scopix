import jax
import haiku as hk


class DummyNet(hk.Module):
    NetName = 'DummyNet'

    def __init__(
            self,
            n_hidden,
            hidden_size,
            output_size,
            name='DummyNet'
            ):
        super().__init__(name=name)
        self.n_hidden = n_hidden
        self.hidden_size = hidden_size
        self.output_size = output_size

    def __call__(self, x):
        x = hk.Linear(
                output_size=self.hidden_size,
                name=None,
            )(x)
        x_residual = jax.nn.relu(x)
        for i in range(self.n_hidden):
            x = hk.Linear(
                    output_size=self.hidden_size,
                    name=None,
                )(x_residual)
            x = jax.nn.relu(x)
            x_residual = x_residual + x
        x = hk.Linear(
                output_size=self.output_size,
                with_bias=False,
                name=None,
            )(x_residual)
        return x
