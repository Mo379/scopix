from pathlib import Path
from _src.logger.loader import load_logger
from _src.networks.DummyNet.Constructor import DummyNetConstructor
from experiments.dummy_net_mnist_toy import load_configs, load_dataset


if __name__ == "__main__":
    root = Path('./')
    configs = load_configs(root)
    train_set, eval_set, test_set = load_dataset(configs['dataset'])
    logger = load_logger(configs['logger'])
    dummy_net_constructor = DummyNetConstructor(
        **configs['model']['DummyNet'],
        Logger=logger
    )
    print(configs)
    print(train_set)
    print(dummy_net_constructor.construct())
