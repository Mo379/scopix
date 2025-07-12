from _src.logger.WANDB import WANDBLogger


def load_logger(config):
    if config['name'] == 'wandb':
        return WANDBLogger(**config)
