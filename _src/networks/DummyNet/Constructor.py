import os
import haiku as hk
import jax
import jax.numpy as jnp
import graphviz
from _src.networks.DummyNet.DummyNet import DummyNet


class Constructor():
    def __init__(
        self,
        seed,
        Logger,
        n_hidden,
        hidden_size,
        output_size,
        batch_dim_size,
        input_dim_size,
    ):
        """Testing the DummyNet network
        """
        self.seed = seed
        self.Logger = Logger
        #
        self.n_hidden = n_hidden
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.B = batch_dim_size
        self.V = input_dim_size
        #
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
        if self.Logger:
            self._visualise(key, model_apply, model_params, example_batch)
            self.Logger._log_img(
                'Model_graphs',
                os.path.join(self.Logger.img_dir, self.NetName+'.png')
            )
        return model_init, model_apply, model_params

    # Visualise the model
    def _visualise(self, key, model_apply, model_params, batch_input):
        dot = hk.experimental.to_dot(model_apply)(
            model_params, key, batch_input
        )
        try:
            graphviz.Source(dot).render(
                os.path.join(self.Logger.img_dir, self.NetName),
                engine='dot',
                format='png'
            )
            result = True
        except Exception:
            result = False
        return result

    def _log_parameters(self, parameters):
        if self.Logger:
            for layer in parameters:
                for sub_params in parameters[layer]:
                    self.Logger._log_params(
                        layer+'/'+sub_params, parameters[layer][sub_params]
                    )
