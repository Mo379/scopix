import os
import yaml

from _src.dataset.arc2 import load_arc2


def load_configs(root):
    dataset_config_path = os.path.join(root, 'config/dataset/arc2_toy.yaml')
    logger_config_path = os.path.join(root, 'config/logger/wandb.yaml')
    model_config_path = os.path.join(root, 'config/model/dummy_toy.yaml')
    optimiser_config_path = os.path.join(root, 'config/optimiser/adam.yaml')

    with open(dataset_config_path, "r") as f:
        dataset_config = yaml.safe_load(f)

    with open(logger_config_path, "r") as f:
        logger_config = yaml.safe_load(f)

    with open(model_config_path, "r") as f:
        model_config = yaml.safe_load(f)

    with open(optimiser_config_path, "r") as f:
        optimiser_config = yaml.safe_load(f)

    return {
        'dataset': dataset_config,
        'logger': logger_config,
        'model': model_config,
        'optimiser': optimiser_config,
    }


def load_dataset(config):
    return load_arc2(config)


def load_model(config):
    return load_arc2(config)
