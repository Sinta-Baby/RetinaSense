# RetinaSense Dataset

The retinal image datasets are **not included** in this repository because of their size and licensing restrictions.

## Required Datasets

- ODIR
- APTOS 2019 Blindness Detection
- ARMD Dataset
- Glaucoma Dataset

Download the datasets and place them inside:

datasets/raw/

Example:

datasets/
└── raw/
    ├── ODIR/
    ├── APTOS/
    ├── ARMD/
    └── Glaucoma/

After downloading, run:

python -m scripts.build_dataset
python -m scripts.split_dataset
python -m scripts.copy_images