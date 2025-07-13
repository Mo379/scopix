import json

import jax.numpy as jnp
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

import matplotlib.pyplot as plt
from matplotlib import colors


class ArcDataset(Dataset):
    """ARC AGI Dataset."""

    def __init__(self, input_path=None, target_path=None):
        self.input_data = self._load_json(input_path) if input_path else {}
        self.target_data = self._load_json(target_path) if target_path else {}

        self.ARC_COLORMAP = colors.ListedColormap([
            '#301934', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00',
            '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25', '#000000'  # 11th color for blank
        ])
        self.ARC_NORM = colors.Normalize(vmin=0, vmax=11)
        self.task_order = sorted(
            self.input_data.keys()) if self.input_data.keys() else False

    def _load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, idx, max_length=5):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        index_key = self.task_order[idx]
        input_datapoint = self.input_data[index_key]
        target_datapoint = self.target_data[index_key] \
            if index_key in self.target_data else {}

        inputs = [self.resize_grid_to_30x30(
            point['input']) for point in input_datapoint['train']]
        outputs = [self.resize_grid_to_30x30(
            point['output']) for point in input_datapoint['train']]

        test_input = [self.resize_grid_to_30x30(
            point['input']) for point in input_datapoint['test']]
        test_output = [self.resize_grid_to_30x30(
            point) for point in target_datapoint]
        # Pad or truncate
        inputs = self._pad_or_truncate(inputs, max_length)
        outputs = self._pad_or_truncate(outputs, max_length)
        test_input = self._pad_or_truncate(test_input, max_length)
        test_output = self._pad_or_truncate(test_output, max_length)
        return inputs, outputs, test_input, test_output

    def _pad_or_truncate(self, lst, max_length):
        dummy = self.dummy_grid(None)
        if len(lst) < max_length:
            lst += [dummy] * (max_length - len(lst))
        elif len(lst) > max_length:
            lst = lst[:max_length]
        return lst

    def dummy_grid(self, grid):
        return [[10] * 30 for _ in range(30)]

    def resize_grid_to_30x30(self, grid):
        new_grid = [[10] * 30 for _ in range(30)]
        original_height = len(grid)
        original_width = len(grid[0])
        for i in range(original_height):
            for j in range(original_width):
                new_grid[i][j] = grid[i][j]
        return np.asarray(new_grid)

    def plot_grid(self, grid, title="Grid Visualization"):
        colormap = self.ARC_COLORMAP
        norm = self.ARC_NORM
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap=colormap, norm=norm)
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        plt.show()


def load_arc2(config):
    data_dir = config["data_dir"]
    batch_size = config["batch_size"]

    training_data = ArcDataset(
        input_path=f'{data_dir}/arc-agi_training_challenges.json',
        target_path=f'{data_dir}/arc-agi_training_solutions.json',
    )

    validation_data = ArcDataset(
        input_path=f'{data_dir}/arc-agi_evaluation_challenges.json',
        target_path=f'{data_dir}/arc-agi_evaluation_solutions.json',
    )
    testing_data = ArcDataset(
        input_path=f'{data_dir}/arc-agi_test_challenges.json',
    )

    # iterator = iter(validation_data)
    # i = 0
    # for inputs, outputs, test_input, test_output in iterator:
    #    if i >= 10:
    #        break
    #    i += 1
    #    for iinput, ooutput in zip(inputs, outputs):
    #        training_data.plot_grid(iinput)
    #        training_data.plot_grid(ooutput)
    #        print('\n\n\n\n')

    def collate_fn(batch):
        # batch is a list of dataset items: [(inputs, outputs, test_input, test_output), …]
        inputs, outputs, test_inputs, test_outputs = zip(*batch)
        # stack each into a jnp array
        inputs = jnp.array(inputs)
        outputs = jnp.array(outputs)
        test_inputs = jnp.array(test_inputs)
        test_outputs = jnp.array(test_outputs)
        return inputs, outputs, test_inputs, test_outputs
    train_loader = DataLoader(
        training_data, batch_size=batch_size, shuffle=True,
        collate_fn=collate_fn
    )
    eval_loader = DataLoader(
        validation_data, batch_size=batch_size, shuffle=False,
        collate_fn=collate_fn
    )
    test_loader = DataLoader(
        testing_data, batch_size=batch_size, shuffle=False,
        collate_fn=collate_fn
    )
    return train_loader, eval_loader, test_loader
