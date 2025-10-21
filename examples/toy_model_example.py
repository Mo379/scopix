import jax
import jax.numpy as jnp
from flax import nnx
from scopix import ToyNet


def main():
    print("ToyNet Example")
    rngs = nnx.Rngs(params=jax.random.PRNGKey(0))
    model = ToyNet(hidden_size=64, output_size=10, rngs=rngs)

    print("Model parameters:")
    for name, param in nnx.iter_parameters(model):
        print(f"{name}: {param.shape}")

    x = jnp.ones((4, 64))
    output = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")


if __name__ == "__main__":
    main()