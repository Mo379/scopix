# Scopix

Scopix is a library designed to advance Large Language Models (LLMs) to the next cognitive processing domain. It focuses on deeply understanding the current mode of LLM functionality and then upgrading it to enhance general intelligence.

The library provides toy models built with Flax NNX, a modern neural network library for JAX, to facilitate experimentation and research in cognitive AI.

## Installation

Install Scopix using pip:

```bash
pip install scopix
```

Or using Poetry:

```bash
poetry add scopix
```

## Quick Start

```python
import jax
from flax import nnx
from scopix import ToyNet, DummyNet

# Create RNGs
rngs = nnx.Rngs(params=jax.random.PRNGKey(0))

# Initialize a simple toy model
toy_model = ToyNet(hidden_size=64, output_size=10, rngs=rngs)

# Or a more complex dummy model with residuals
dummy_model = DummyNet(n_hidden=3, hidden_size=64, output_size=10, rngs=rngs)

# Use the model
import jax.numpy as jnp
x = jnp.ones((32, 64))  # batch of 32, input dim 64
output = toy_model(x)
```

## Documentation

Full documentation is available at [Read the Docs](https://scopix.readthedocs.io/).

## Contributing

Contributions are welcome. Please see the documentation for development setup.