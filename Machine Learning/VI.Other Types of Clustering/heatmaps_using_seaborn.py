# Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data

data = pd.read_csv('Country clusters standardized.csv', index_col='Country')
# pd.read_csv(*.csv, index_col) loads a given CSV file as a data frame;
# index_col is an argument which can specify a given column from the CSV as index of the data frame
x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'], axis=1)
print(x_scaled)

# Plot the data
sns.clustermap(x_scaled, cmap='mako')
# Seaborn is a really easy library to use, should you know the exact feature you need
plt.show()
# Line above, It is another dendrogram! This time uniting the two features (NOT observations)

# In the same way, we can cluster the observations,
# we can reduce the dimensionality of the problem, by combining the features themselves

# The rectangle of colors is called HEATMAP