import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Project 3: Correlation & Relationships", layout="wide")

st.title("Project 3: Correlation Heatmap & Pairwise Relationships")
st.write("Visualizing Pearson correlation and pairwise distributions.")

# 1. Dataset Load
df = sns.load_dataset('iris')
numeric_df = df.select_dtypes(include=[np.number])

# Data preview
if st.checkbox("Show Raw Data Preview"):
    st.dataframe(numeric_df.head())

# 2. Pearson Correlation
corr_matrix = numeric_df.corr(method='pearson')

# 3. Heatmap
st.subheader("1. Correlation Heatmap (Masked Upper Triangle)")
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
fig_heat, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5, ax=ax)
st.pyplot(fig_heat)

# 4. Pairplot
st.subheader("2. Pairwise Relationships (Scatter Matrix)")
pair_fig = sns.pairplot(numeric_df, diag_kind='kde')
st.pyplot(pair_fig.fig)

# 5. Summary Findings
st.subheader("3. Key Observations")
st.markdown("""
- **Strongest Positive Correlation:** `petal_length` & `petal_width` (+0.96)
- **Strongest Negative Correlation:** `sepal_width` & `petal_length` (-0.43)
- **Weakest Correlation:** `sepal_length` & `sepal_width` (-0.12)
""")