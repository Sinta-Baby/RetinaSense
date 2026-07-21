"""
==========================================================
RetinaSense

Image Copier

Description:
Copies images into the RetinaSense dataset structure
using the split metadata files.

==========================================================
"""
import shutil

import pandas as pd

from pathlib import Path

from core.paths import *

from core.logger import logger

# =====================================================
# Disease Classes
# =====================================================

CLASSES = [
    "Healthy",
    "DR",
    "Glaucoma",
    "AMD"
]


# =====================================================
# Create Dataset Folder Structure
# =====================================================

def create_dataset_structure():

    print("=" * 70)
    print("Creating Dataset Folder Structure")
    print("=" * 70)

    datasets = [
        TRAIN_DATASET,
        VALIDATION_DATASET,
        TEST_DATASET
    ]

    for dataset in datasets:

        dataset.mkdir(parents=True, exist_ok=True)

        for disease in CLASSES:

            (dataset / disease).mkdir(
                parents=True,
                exist_ok=True
            )

    logger.info("Dataset folder structure created successfully.")
    

# =====================================================
# Load Metadata
# =====================================================

def load_metadata(metadata_path):

    print("\n" + "=" * 70)
    print(f"Loading {metadata_path.name}")
    print("=" * 70)

    metadata = pd.read_csv(metadata_path)

    print(f"Total Records : {len(metadata)}")

    logger.info(f"{metadata_path.name} loaded successfully.")

    return metadata

# =====================================================
# Copy Images
# =====================================================

def copy_images(metadata, destination_folder):

    print("\n" + "=" * 70)
    print(f"Copying Images to {destination_folder.name}")
    print("=" * 70)

    copied = 0
    skipped = 0

    for _, row in metadata.iterrows():

        source = Path(row["filepath"])

        disease = row["disease"]

        destination = destination_folder / disease / row["filename"]

        if source.exists():

            shutil.copy2(source, destination)

            copied += 1

        else:

            skipped += 1

    print(f"Copied Images : {copied}")
    print(f"Skipped Images: {skipped}")

    logger.info(f"{destination_folder.name}: {copied} images copied.")
    

# =====================================================
# Main
# =====================================================

def main():

    create_dataset_structure()

    # Train
    train_metadata = load_metadata(TRAIN_METADATA)
    copy_images(train_metadata, TRAIN_DATASET)

    # Validation
    validation_metadata = load_metadata(VALIDATION_METADATA)
    copy_images(validation_metadata, VALIDATION_DATASET)

    # Test
    test_metadata = load_metadata(TEST_METADATA)
    copy_images(test_metadata, TEST_DATASET)

    print("\n" + "=" * 70)
    print("Image Copy Completed")
    print("=" * 70)

    logger.info("All images copied successfully.")

# =====================================================
# Run
# =====================================================

if __name__ == "__main__":

    main() 