from datasets import load_dataset
from torch.utils.data import DataLoader, Dataset
import numpy as np
import torch

class CIFARTorchDataset(Dataset):
    def __init__(self, hf_dataset, transform=None):
        self.dataset = hf_dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        item = self.dataset[idx]
        image = item['img']  # HF CIFAR-10 uses key "img"
        label = item['label']

        if self.transform:
            image = self.transform(image)

        return image, label

def load_cifar10(batch_size=64):
    # 1️⃣ Load CIFAR-10 from HF datasets
    dataset = load_dataset("cifar10")

    # 2️⃣ Split train set into train/val
    split_dataset = dataset["train"].train_test_split(test_size=0.2, seed=42)
    train_ds = split_dataset["train"]
    eval_ds = split_dataset["test"]
    test_ds = dataset["test"]  # keep the official test set

    print(f"Train size: {len(train_ds)}, Eval size: {len(eval_ds)}, Test size: {len(test_ds)}")

    # 3️⃣ Define transform
    def transform(pil_image):
        """
        Takes image, standardise and return
        """
        np_img = np.array(pil_image, dtype=np.float32) / 255.0
        tensor_img = torch.tensor(np_img, dtype=torch.float32)
        return tensor_img

    # 4️⃣ Wrap in PyTorch Dataset
    train_torch_ds = CIFARTorchDataset(train_ds, transform=transform)
    eval_torch_ds = CIFARTorchDataset(eval_ds, transform=transform)
    test_torch_ds = CIFARTorchDataset(test_ds, transform=transform)

    # 5️⃣ DataLoaders
    train_loader = DataLoader(train_torch_ds, batch_size=batch_size, shuffle=True)
    eval_loader = DataLoader(eval_torch_ds, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_torch_ds, batch_size=batch_size, shuffle=False)

    # Example usage
    images, labels = next(iter(train_loader))
    print(f"Batch images shape: {images.shape}, Batch labels shape: {labels.shape}")
    return train_loader, eval_loader, test_loader
