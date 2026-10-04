import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset load karein (yahan built-in 'iris' dataset use kar rahe hain)
df = sns.load_dataset('iris')

# Correlation ke liye sirf numeric (numbers wale) columns filter karein
numeric_df = df.select_dtypes(include=[np.number])

# Check karein ki data kaisa dikh raha hai
print("--- Dataset ke pehle 5 rows ---")
print(numeric_df.head())

print("\n--- Columns ki details ---")
print(numeric_df.info())