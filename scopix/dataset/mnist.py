from datasets import load_dataset
from torch.utils.data import DataLoader, Dataset
import jax.numpy as jnp
import numpy as np


class MNISTTorchDataset(Dataset):
    def __init__(self, hf_dataset, transform=None):
        self.dataset = hf_dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        image = item['image']
        label = item['label']

        if self.transform:
            image = self.transform(image)

        return image, label


def load_mnist(config):
    # Load MNIST from huggigface atasets

    # This loads the original MNIST (train: 60k, test: 10k)
    dataset = load_dataset("mnist")

    # Custom split (e.g. use 80% of train for training, 20% of train for eval)
    split_dataset = dataset["train"].train_test_split(test_size=0.2, seed=42)

    train_ds = split_dataset["train"]
    eval_ds = split_dataset["test"]
    test_ds = dataset["test"]  # keep the official test set

    print(
        f"Train size: {len(train_ds)}, Eval size: {len(eval_ds)}, Test size: {len(test_ds)}"
    )

    # 3️⃣ Torch Dataset wrapper

    # Define transforms (optional — normalization, etc.)

    def transform(pil_image):
        """
        Takes a PIL image, converts to float32 numpy,
        scales to [0,1], casts to jax array, adds channel dim,
        and normalizes with MNIST stats.
        """
        # PIL → H×W uint8 → float32 in [0,1]
        np_img = np.array(pil_image, dtype=np.float32) / 255.0

        # to jax array, add channel dim → (1, H, W)
        np_img = np.expand_dims(jnp.array(np_img), axis=0)

        # normalize: (x - μ) / σ
        mean = 0.1307
        std = 0.3081
        return (np_img - mean) / std
    # Wrap in PyTorch datasets
    train_torch_ds = MNISTTorchDataset(train_ds, transform=transform)
    eval_torch_ds = MNISTTorchDataset(eval_ds, transform=transform)
    test_torch_ds = MNISTTorchDataset(test_ds, transform=transform)

    # Create DataLoaders
    train_loader = DataLoader(train_torch_ds, batch_size=8, shuffle=True)
    eval_loader = DataLoader(eval_torch_ds, batch_size=8, shuffle=False)
    test_loader = DataLoader(test_torch_ds, batch_size=8, shuffle=False)

    # Example usage
    batch = next(iter(train_loader))
    print(
        f"Batch images shape: {batch[0].shape}, Batch labels shape: {batch[1].shape}"
    )
    return train_loader, eval_loader, test_loader
