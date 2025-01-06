# Import the relevant libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# Load the data

data = pd.read_csv('3.01. Country clusters.csv')
print(data)
# How did we gather the data
# The Latitude and Longitude correspond to the geographic centers of the countries

# Plot the data

plt.scatter(data['Longitude'], data['Latitude'])
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# Select the features

# DataFrame.iloc(row indices, column indices) slices the data frame, given rows and columns to be kept
x = data.iloc[:, 1:3]
print(x)

# Clustering
kmeans = KMeans(3)
# The value in brackets is K (the number of clusters)

kmeans.fit(x)
# This code will apply k-means clustering with 2 clusters to X


# Clustering results

# sklearn.cluster.KMeans.fit_predict(x) returns the cluster predictions in an array
indentified_clusters = kmeans.fit_predict(x)
print(indentified_clusters)

data_with_clusters = data.copy()
data_with_clusters['Cluster'] = indentified_clusters
print(data_with_clusters)

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# In matplotlib, we can set the color to be determined by a variable

# Map the data

data_mapped = data.copy()
data_mapped['Language'] = data_mapped['Language'].map({'English': 0, 'French': 1, 'German': 2})
# This is NOT the optimal way to encode them but it will work for now
print(data_mapped)

# Select the features

# x = data_mapped.iloc[:, 3:4]
x = data_mapped.iloc[:, 1:4]
print(x)

# Clustering
kmeans = KMeans(3)

kmeans.fit(x)

indentified_clusters = kmeans.fit_predict(x)
print(indentified_clusters)

data_with_clusters = data_mapped.copy()
data_with_clusters['Cluster'] = indentified_clusters
print(data_with_clusters)


plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'], c=data_with_clusters['Cluster'], cmap='rainbow')
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.show()

# This time the 3 clusters are based simply on geographical location

# Selecting the number of clustering

# WCSS

# WCSS similar to SST, SSR and SSE, WCSS is a measure developed within the ANOVA framework
# WCSS - within-cluster sum of squares
# If we minimize WCSS, we have reached the perfect clustering solution*
print(kmeans.inertia_)

# We need to solve the problem with 1,2,3,4,5,6 clusters and calculate WCSS

wcss = []

for i in range(1, 7):
    kmeans = KMeans(i)
    kmeans.fit(x)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)

print(wcss)
# The sequence is decreasing with very big leaps in the first two steps

# The Elbow Method

number_clusters = range(1, 7)
plt.plot(number_clusters, wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Within-cluster Sum of Squares')
plt.show()
# A two cluster solution would be suboptimal as the leap from 2 to 3 iis very big