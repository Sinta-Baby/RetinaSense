"""
========================================================
RetinaSense
Project Paths
========================================================


Description:
Stores every project path in one place.
No script should hardcode folder locations.

========================================================
"""

from pathlib import Path

# ======================================================
# Project Root
# ======================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ======================================================
# Core Folders
# ======================================================

CORE = PROJECT_ROOT / "core"
UTILS = PROJECT_ROOT / "utils"
SCRIPTS = PROJECT_ROOT / "scripts"

# ======================================================
# Dataset Folders
# ======================================================

DATASETS = PROJECT_ROOT / "datasets"

RAW_DATASET = DATASETS / "raw"

EXTRACTED_DATASET = DATASETS / "extracted"

PROCESSED_DATASET = DATASETS / "processed"

RETINASENSE_DATASET = DATASETS / "RetinaSense_Dataset"

TRAIN_DATASET = RETINASENSE_DATASET / "train"

VALIDATION_DATASET = RETINASENSE_DATASET / "validation"

TEST_DATASET = RETINASENSE_DATASET / "test"

METADATA = RETINASENSE_DATASET / "metadata"

MASTER_METADATA = METADATA / "master_metadata.csv"

TRAIN_METADATA = METADATA / "train_metadata.csv"

VALIDATION_METADATA = METADATA / "validation_metadata.csv"

TEST_METADATA = METADATA / "test_metadata.csv"

# ======================================================
# Other Project Folders
# ======================================================

MODELS = PROJECT_ROOT / "models"

SAVED_MODELS = PROJECT_ROOT / "saved_models"

LOGS = PROJECT_ROOT / "logs"

REPORTS = PROJECT_ROOT / "reports"

RESULTS = PROJECT_ROOT / "results"

CONFIG = PROJECT_ROOT / "config"

DOCS = PROJECT_ROOT / "docs"

NOTEBOOKS = PROJECT_ROOT / "notebooks"



# =====================================================
# ODIR DATASET
# =====================================================

# ODIR Dataset Root
ODIR_DATASET = EXTRACTED_DATASET / "ODIR"

# ODIR Metadata CSV
ODIR_METADATA = ODIR_DATASET / "full_df.csv"

# Preprocessed Images (used for RetinaSense)
ODIR_IMAGES = ODIR_DATASET / "preprocessed_images"


# =====================================================
# APTOS DATASET
# =====================================================

APTOS_DATASET = EXTRACTED_DATASET / "APTOS"

# Metadata
APTOS_TRAIN_METADATA = APTOS_DATASET / "train_1.csv"
APTOS_VALID_METADATA = APTOS_DATASET / "valid.csv"
APTOS_TEST_METADATA = APTOS_DATASET / "test.csv"

# Images
APTOS_TRAIN_IMAGES = APTOS_DATASET / "train_images" / "train_images"

APTOS_VALID_IMAGES = APTOS_DATASET / "val_images" / "val_images"

APTOS_TEST_IMAGES = APTOS_DATASET / "test_images" / "test_images"


# =====================================================
# GLAUCOMA Dataset
# =====================================================

GLAUCOMA_DATASET = EXTRACTED_DATASET / "GLAUCOMA"

GLAUCOMA_IMAGES = (
    GLAUCOMA_DATASET
    / "Fundus_Train_Val_Data"
    / "Fundus_Scanes_Sorted"
)

GLAUCOMA_TRAIN = GLAUCOMA_IMAGES / "Train"
GLAUCOMA_VALIDATION = GLAUCOMA_IMAGES / "Validation"


# =====================================================
# ARMD Dataset
# =====================================================

ARMD_DATASET = (
    EXTRACTED_DATASET
    / "ARMD"
    / "Macular Degeneration Disease Dataset"
)

ARMD_TRAIN = ARMD_DATASET / "train"

ARMD_VALIDATION = ARMD_DATASET / "val"