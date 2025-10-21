import jax
import jax.numpy as jnp
from flax import nnx
from scopix import ToyNet, DummyNet


def test_toynet_init():
    rngs = nnx.Rngs(params=jax.random.PRNGKey(42))
    model = ToyNet(hidden_size=64, output_size=10, rngs=rngs)
    assert model.linear1.in_features == 64
    assert model.linear1.out_features == 64
    assert model.linear2.in_features == 64
    assert model.linear2.out_features == 10


def test_toynet_forward():
    rngs = nnx.Rngs(params=jax.random.PRNGKey(42))
    model = ToyNet(hidden_size=64, output_size=10, rngs=rngs)
    x = jnp.ones((32, 64))
    output = model(x)
    assert output.shape == (32, 10)


def test_dummynet_init():
    rngs = nnx.Rngs(params=jax.random.PRNGKey(42))
    model = DummyNet(n_hidden=3, hidden_size=64, output_size=10, rngs=rngs)
    assert len(model.hidden_linears) == 3
    assert model.input_linear.in_features == 64
    assert model.input_linear.out_features == 64
    assert model.output_linear.in_features == 64
    assert model.output_linear.out_features == 10


def test_dummynet_forward():
    rngs = nnx.Rngs(params=jax.random.PRNGKey(42))
    model = DummyNet(n_hidden=2, hidden_size=64, output_size=10, rngs=rngs)
    x = jnp.ones((32, 64))
    output = model(x)
    assert output.shape == (32, 10)