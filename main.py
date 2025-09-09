import sys
from pathlib import Path
from _src.logger.loader import load_logger
from _src.networks.DummyNet.Constructor import DummyNetConstructor
from experiments.dummy_net_arc2_toy import (
    load_configs, load_dataset, load_model
)
import logging as std_logger


if __name__ == "__main__":
    root = Path('./')
    std_logger.basicConfig(
        level=std_logger.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stdout
    )
    configs = load_configs(root)
    train_set, eval_set, test_set = load_dataset(configs['dataset'])
    logger = load_logger(configs['logger'])
    model_constructor = load_model(configs['model'])
    dummy_net_constructor = DummyNetConstructor(
        **configs['model']['DummyNet'],
        Logger=logger
    )
    _, model_apply, model_param = dummy_net_constructor.construct()

    inputs, outputs, test_input, test_output = next(iter(eval_set))

    std_logger.info(
        "input, ouput, test_input, test_output shapes: %s, %s, %s, %s",
        str(inputs.shape),
        str(outputs.shape),
        str(test_input.shape),
        str(test_output.shape),
    )
    std_logger.info(
        "train, eval, test lengths: %d, %d, %d",
        len(train_set),
        len(eval_set),
        len(test_set)
    )

    for batch_index, (inputs, outputs, test_input, test_output) in enumerate(iter(test_set)):
        print(batch_index)
        pass
