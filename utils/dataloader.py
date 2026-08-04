"""
==========================================================
RetinaSense

DataLoader

Description:
Creates PyTorch DataLoaders for
training, validation and testing.

==========================================================
"""

from torch.utils.data import DataLoader

from core.constants import (
    BATCH_SIZE,
    NUM_WORKERS
)

from utils.dataset import RetinaDataset
from utils.transforms import (
    get_train_transforms,
    get_validation_transforms,
    get_test_transforms
)


def get_dataloaders(dataset_root):
    """
    Returns train, validation and test dataloaders.
    """

    train_dataset = RetinaDataset(
        metadata_file=f"{dataset_root}/metadata/train_metadata.csv",
        dataset_root=dataset_root,
        split="train",
        transforms=get_train_transforms()
    )

    validation_dataset = RetinaDataset(
        metadata_file=f"{dataset_root}/metadata/validation_metadata.csv",
        dataset_root=dataset_root,
        split="validation",
        transforms=get_validation_transforms()
    )

    test_dataset = RetinaDataset(
        metadata_file=f"{dataset_root}/metadata/test_metadata.csv",
        dataset_root=dataset_root,
        split="test",
        transforms=get_test_transforms()
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    validation_loader = DataLoader(
        validation_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
        pin_memory=True
    )

    return (
        train_loader,
        validation_loader,
        test_loader
    )