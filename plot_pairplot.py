# Part 4: Pairwise Relationships / Scatter Matrix plot karna
pair_fig = sns.pairplot(numeric_df, diag_kind='kde')

# Title set karein
pair_fig.fig.subplots_adjust(top=0.95)
pair_fig.fig.suptitle("Pairwise Relationships (Scatter Matrix)", fontsize=14)

# Plot ko PNG format mein save karein
plt.savefig("pairwise_relationships.png")
plt.show()