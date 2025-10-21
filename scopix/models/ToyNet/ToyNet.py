from flax import nnx
from typing import Any


class ToyNet(nnx.Module):
    """A simple toy neural network for experimentation."""

    NetName = 'ToyNet'

    def __init__(
            self,
            hidden_size: int,
            output_size: int,
            *,
            rngs: nnx.Rngs,
            **kwargs: Any
            ):
        self.linear1 = nnx.Linear(hidden_size, hidden_size, rngs=rngs)
        self.linear2 = nnx.Linear(hidden_size, output_size, use_bias=False, rngs=rngs)

    def __call__(self, x):
        x = self.linear1(x)
        x = nnx.relu(x)
        x = self.linear2(x)
        return x
