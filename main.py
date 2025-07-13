from pathlib import Path
from _src.logger.loader import load_logger
from _src.networks.DummyNet.Constructor import DummyNetConstructor
from experiments.dummy_net_arc2_toy import load_configs, load_dataset


if __name__ == "__main__":
    root = Path('./')
    configs = load_configs(root)
    train_set, eval_set, test_set = load_dataset(configs['dataset'])
    logger = load_logger(configs['logger'])
    dummy_net_constructor = DummyNetConstructor(
        **configs['model']['DummyNet'],
        Logger=logger
    )
    _, model_apply, model_param = dummy_net_constructor.construct()
    train_features = next(iter(test_set))
    print(train_features)
