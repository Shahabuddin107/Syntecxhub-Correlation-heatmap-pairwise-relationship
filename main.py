import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Dataset Load & Preprocess
df = sns.load_dataset('iris')
numeric_df = df.select_dtypes(include=[np.number])

# 2. Pearson Correlation
corr_matrix = numeric_df.corr(method='pearson')
print("Correlation Matrix:\n", corr_matrix)

# 3. Correlation Heatmap (Masked)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.title("Correlation Heatmap (Masked Upper Triangle)")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# 4. Pairplot
pair_fig = sns.pairplot(numeric_df, diag_kind='kde')
pair_fig.fig.subplots_adjust(top=0.95)
pair_fig.fig.suptitle("Pairwise Relationships (Scatter Matrix)")
plt.savefig("pairwise_relationships.png")
plt.close()

print("Execution complete! Plots saved successfully.")