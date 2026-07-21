"""
====================================================
RetinaSense
Core Constants
====================================================

Description:
This file stores all constant values used
throughout the RetinaSense project.

====================================================
"""

# ====================================================
# Project Information
# ====================================================

PROJECT_NAME = "RetinaSense"

PROJECT_VERSION = "1.0.0"

AUTHOR = "Sinta Baby"

# ====================================================
# Dataset Names
# ====================================================

DATASET_NAMES = [
    "ODIR",
    "APTOS",
    "GLAUCOMA",
    "ARMD"
]

# ====================================================
# Disease Labels
# ====================================================

DISEASE_LABELS = [
    "Healthy",
    "DR",
    "Glaucoma",
    "AMD"
]

# Disease to Index Mapping

DISEASE_TO_INDEX = {
    "Healthy": 0,
    "DR": 1,
    "Glaucoma": 2,
    "AMD": 3
}

# Index to Disease Mapping

INDEX_TO_DISEASE = {
    0: "Healthy",
    1: "DR",
    2: "Glaucoma",
    3: "AMD"
}

# ====================================================
# DR Severity Labels
# ====================================================

DR_SEVERITY = {
    0: "No DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferative DR"
}

# ====================================================
# Image Settings
# ====================================================

IMAGE_SIZE = (224, 224)

IMAGE_CHANNELS = 3

# ====================================================
# Training Settings
# ====================================================

BATCH_SIZE = 32

RANDOM_SEED = 42

NUM_WORKERS = 2

# ====================================================
# Supported File Extensions
# ====================================================

IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
]

CSV_EXTENSION = ".csv"

EXCEL_EXTENSIONS = [
    ".xlsx",
    ".xls"
]

# ====================================================
# Confidence Threshold
# ====================================================

CONFIDENCE_THRESHOLD = 0.50