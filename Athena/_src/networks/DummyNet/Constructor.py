import os
import haiku as hk
import jax
import jax.numpy as jnp
import graphviz
from DummyNet import DummyNet


class Constructor():
    def __init__(
            self,
            seed,
            n_hidden,
            hidden_size,
            output_size,
            batch_dim_size,
            input_dim_size,
            Logger,
        ):
        """Testing the DummyNet network
        """
        self.seed = seed
        self.n_hidden = n_hidden
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.B = batch_dim_size
        self.V = input_dim_size
        self.Logger = Logger
        self.NetName = DummyNet.NetName

    def _construct(self):
        def net_module(x):
            x = DummyNet(
                    n_hidden=self.n_hidden,
                    hidden_size=self.hidden_size,
                    output_size=self.output_size
                )(x)
            return x
        key = jax.random.PRNGKey(seed=self.seed)
        example_batch = jax.random.normal(key, (self.B, self.V))
        model_init, model_apply = hk.transform(net_module, apply_rng=True)
        model_params = model_init(key, example_batch)
        example = model_apply(model_params, key, example_batch)
        if self.Logger:
            self._visualise(key, model_apply, model_params, example_batch)
        print(example.shape)
        #print(model_params)
        #print(example)
        return model_init, model_apply, model_params

    # Visualise the model
    def _visualise(self, key, model_apply, model_params, batch_input):
        dot = hk.experimental.to_dot(model_apply)(
                model_params, key, batch_input
            )
        try:
            graphviz.Source(dot).render(
                    os.path.join(self.Logger.img_dir, self.NetName)
                )
            result = True
        except Exception:
            result = False
        return result


