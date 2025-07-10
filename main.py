from pathlib import Path
from experiments.dummy_net_mnist_toy import load_configs, load_dataset


if __name__ == "__main__":
    root = Path('./')
    configs = load_configs(root)
    train_set, eval_set, test_set = load_dataset(configs['dataset'])
    print(configs)
