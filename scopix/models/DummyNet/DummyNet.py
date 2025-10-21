from flax import nnx
from typing import Any


class DummyNet(nnx.Module):
    """A dummy neural network with residual connections for experimentation."""

    NetName = 'DummyNet'

    def __init__(
            self,
            n_hidden: int,
            hidden_size: int,
            output_size: int,
            *,
            rngs: nnx.Rngs,
            **kwargs: Any
            ):
        self.input_linear = nnx.Linear(hidden_size, hidden_size, rngs=rngs)
        self.hidden_linears = [nnx.Linear(hidden_size, hidden_size, rngs=rngs) for _ in range(n_hidden)]
        self.output_linear = nnx.Linear(hidden_size, output_size, use_bias=False, rngs=rngs)

    def __call__(self, x):
        x = self.input_linear(x)
        x_residual = nnx.relu(x)
        for linear in self.hidden_linears:
            x = linear(x_residual)
            x = nnx.relu(x)
            x_residual = x_residual + x
        x = self.output_linear(x_residual)
        return x
