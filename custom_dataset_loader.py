# custom_dataset_loader.py
from wildlife_datasets import datasets
import pandas as pd
import os

# dataset_classes = [name for name in dir(datasets) if not name.startswith("_")]
# print(dataset_classes)

# ===== CONFIG =====
dataset_name = "CatIndividualImages"  # change to any dataset class name
data_dir = f"data/{dataset_name}"  # where dataset will be downloaded/extracted
output_csv = f"{data_dir}/custom_labels.csv"  # file to save your relabels

# ===== DOWNLOAD & LOAD =====
# Download and extract the dataset
datasets.__dict__[dataset_name].get_data(data_dir)

# Load dataset object
dataset = datasets.__dict__[dataset_name](data_dir)

# Show basic info
print("Dataset summary:")
print(dataset.summary)
print("\nFirst few entries:")
print(dataset.df.head())

