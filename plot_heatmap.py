# Part 3: Correlation Heatmap banana
# 1. Upper triangle ko mask (chupane) ke liye matrix banayein
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# 2. Heatmap plot karein
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix, 
    mask=mask,               # Upper triangle ko hide karega
    annot=True,              # Boxes ke andar correlation values print karega
    fmt=".2f",               # Value ko 2 decimal tak rakhega
    cmap='coolwarm',         # Colors: Red (positive), Blue (negative)
    vmin=-1, vmax=1,         # Scale limit -1 se +1
    linewidths=0.5
)

plt.title("Correlation Heatmap (Masked Upper Triangle)", fontsize=14)
plt.tight_layout()

# Chart ko PNG format mein save karein
plt.savefig("correlation_heatmap.png")
plt.show()