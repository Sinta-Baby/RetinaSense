"""
==========================================================
RetinaSense

Training Engine

Description:
Trains EfficientNet-B3 for retinal disease classification.

==========================================================
"""

from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim

from tqdm import tqdm

from core.constants import (
    NUM_EPOCHS,
    LEARNING_RATE,
    WEIGHT_DECAY,
    BEST_MODEL_NAME
)


class Trainer:

    def __init__(
        self,
        model,
        train_loader,
        validation_loader,
        device
    ):

        self.model = model

        self.train_loader = train_loader

        self.validation_loader = validation_loader

        self.device = device

        self.criterion = nn.CrossEntropyLoss()

        self.optimizer = optim.AdamW(
            self.model.parameters(),
            lr=LEARNING_RATE,
            weight_decay=WEIGHT_DECAY
        )

        self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer,
            T_max=NUM_EPOCHS
        )

        self.best_accuracy = 0.0

        self.model.to(self.device)

    # =====================================================
    # Train One Epoch
    # =====================================================

    def train_epoch(self):

        self.model.train()

        running_loss = 0.0

        correct = 0

        total = 0

        progress = tqdm(
            self.train_loader,
            desc="Training",
            leave=False
        )

        for images, labels in progress:

            images = images.to(self.device)

            labels = labels.to(self.device)

            self.optimizer.zero_grad()

            outputs = self.model(images)

            loss = self.criterion(
                outputs,
                labels
            )

            loss.backward()

            self.optimizer.step()

            running_loss += loss.item()

            predictions = outputs.argmax(dim=1)

            correct += (
                predictions == labels
            ).sum().item()

            total += labels.size(0)

            progress.set_postfix(
                loss=loss.item()
            )

        accuracy = 100 * correct / total

        return (
            running_loss / len(self.train_loader),
            accuracy
        )

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):

        self.model.eval()

        running_loss = 0.0

        correct = 0

        total = 0

        with torch.no_grad():

            for images, labels in self.validation_loader:

                images = images.to(self.device)

                labels = labels.to(self.device)

                outputs = self.model(images)

                loss = self.criterion(
                    outputs,
                    labels
                )

                running_loss += loss.item()

                predictions = outputs.argmax(dim=1)

                correct += (
                    predictions == labels
                ).sum().item()

                total += labels.size(0)

        accuracy = 100 * correct / total

        return (
            running_loss / len(self.validation_loader),
            accuracy
        )

    # =====================================================
    # Save Best Model
    # =====================================================

    def save_model(self):

        Path("saved_models").mkdir(
            exist_ok=True
        )

        torch.save(
            self.model.state_dict(),
            Path("saved_models") / BEST_MODEL_NAME
        )

    # =====================================================
    # Complete Training
    # =====================================================

    def train(self):

        print("=" * 70)
        print("Training Started")
        print("=" * 70)

        for epoch in range(NUM_EPOCHS):

            train_loss, train_accuracy = (
                self.train_epoch()
            )

            validation_loss, validation_accuracy = (
                self.validate()
            )

            self.scheduler.step()

            print(
                f"\nEpoch {epoch + 1}/{NUM_EPOCHS}"
            )

            print(
                f"Train Loss : {train_loss:.4f}"
            )

            print(
                f"Train Accuracy : {train_accuracy:.2f}%"
            )

            print(
                f"Validation Loss : {validation_loss:.4f}"
            )

            print(
                f"Validation Accuracy : {validation_accuracy:.2f}%"
            )

            if validation_accuracy > self.best_accuracy:

                self.best_accuracy = validation_accuracy

                self.save_model()

                print("✅ Best model saved.")

        print("\nTraining Completed.")