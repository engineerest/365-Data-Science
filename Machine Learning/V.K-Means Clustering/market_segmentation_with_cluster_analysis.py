# Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# Load the data

data = pd.read_csv('3.12. Example.csv')

print(data)

# Plot the data

plt.scatter(data['Satisfaction'], data['Loyalty'])
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

# Select the features

x = data.copy()

kmeans = KMeans(2)
kmeans.fit(x)

# Clustering results
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
# The column 'cluster_pred' of 'clusters' will contain the predictions

plt.scatter(data['Satisfaction'], data['Loyalty'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()
# Most probably the algorithm ONLY considered satisfaction as a feature
# Whenever we cluster on the basis of a single feature, the result looks like this graph

# Standardize the variable

from sklearn import preprocessing
x_scaled = preprocessing.scale(x)
# skleanr.preprocessing.scale(x) scales (standardizes with mean 0, and standard deviation of 1 by default) each variable (column) separately
print(x_scaled)
# x_scaled contains the standardized 'Satisfaction' and the same values for 'Loyalty'

# Take advantage of the Elbow method

wcss = []
for i in range(1, 10):
    kmeans = KMeans(i)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

print(wcss)

plt.plot(range(1, 10), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
# Given this graph, think about the number of clusters of clusters we should use

# We can see the change, but we don't really know which solution is the best one

# It is worth inspecting the difference with standardized variables

# Explore clustering solutions and select the number of clusters

kmeans_new = KMeans(4)
kmeans_new.fit(x_scaled)
clusters_new = x.copy()
clusters_new['cluster_pred'] = kmeans_new.fit_predict(x_scaled)
print(clusters_new)
# We will plot the data without standardizing the AXES but the solution will be that standardized one

# Keeping the original x-axis we get an intuition for HOW SATISFIED WERE THE CUSTOMERS

plt.scatter(clusters_new['Satisfaction'], clusters_new['Loyalty'], c=clusters_new['cluster_pred'], cmap='rainbow')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

# We often choose to plot using the original values for clearer interpretability.
# Note: the discrepancy we observe here depends on the range of the axes, too

# We are now much more confident that standardization is a good thing

# In unsupervized learning the algorithm will do the magic but WE need to interpret the result

# Eventually we hope that all points on the graph will turn into 'Fans'