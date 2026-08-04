"""
==========================================================
RetinaSense

Main Training Script

Description:
Loads the dataset, model and starts training.

==========================================================
"""

import torch

from core.constants import RANDOM_SEED
from models.efficientnet_b3 import build_model
from utils.dataloader import get_dataloaders
from engine.trainer import Trainer


def main():

    torch.manual_seed(RANDOM_SEED)

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    print("=" * 70)
    print("RetinaSense")
    print("=" * 70)
    print(f"Device : {device}")

    dataset_root = "datasets/RetinaSense_Dataset"

    train_loader, validation_loader, test_loader = (
        get_dataloaders(dataset_root)
    )

    model = build_model()

    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        validation_loader=validation_loader,
        device=device
    )

    trainer.train()


if __name__ == "__main__":
    main()