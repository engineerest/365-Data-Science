# Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

# Load the data

data = pd.read_csv('1.02. Multiple linear regression.csv')
print(data.head())
print(data.describe())

# Create the multiple and independent regression

# Declare the dependent and independent variables

x = data[['SAT', 'Rand 1,2,3']]
y = data['GPA']

# Standardization

# StandardScaler() a preprocessing module used to standardize (or scale) data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
# We have created an empty StandardScaler object
# 'scaler' will be used to subtract the mean divide by the standard deviation

scaler.fit(x) # scaling mechanism
# 'fit' calculates and stores the mean and standard deviation of each feature
# new_data = pd.read_csv('new_data.csv')
# scaler #contains all standardization info

x_scaled = scaler.transform(x)
# StandardScaler.transform(x) transforms the unscaled inputs using the information contained in the scaler object (feature-wise)
# new_data_scaled = scaler.transform(new_data)

print(x_scaled)

# Regression with scaled features

reg = LinearRegression()
reg.fit(x_scaled, y)

print(reg.coef_)
print(reg.intercept_)

# Creating a summary table

reg_summary = pd.DataFrame([['Intercept'], ['SAT'], ['Rand 1,2,3']], columns=['Features'])
reg_summary['Weights'] = reg.intercept_, reg.coef_[0], reg.coef_[1]

print(reg_summary)
# Weights is a the 'machine learning word' for coefficients
# The bigger the weight, the bigger the impact!
# The 'ML' for intercept is 'bias'

# Using these new naming conventions we can coveniently distinguish between a 'regular coefficients summary table' and this new one with
# standardized coefficients (weights)

# The closer a weight is to 0, the smaller its impact;
# The bigger the weights, the bigger its impact

# We can clearly see that 'Rand 1,2,3' barely contributes to our output, if at all
# When we perform feature scaling, we don't care if a useless variable is there or not

# In general, I always prefer to leave out the worst performing features

# Making predictions with the standardized coefficients (weights)

new_data = pd.DataFrame(data=[[1700, 2], [1800, 1]], columns=['SAT', 'Rand 1,2,3'])

print(reg.predict(new_data)) # This is not even a valid GPA!!!

# Out model expects values that are of the same magnitude

# The new data frame should be arrange in the same way..
# and also must be standardized in the same way

new_data_scaled = scaler.transform(new_data)
print(new_data_scaled)

print(reg.predict(new_data_scaled))

# What if we removed the 'Random 1,2,3' variable?

reg_simple = LinearRegression()
x_simple_matrix = x_scaled[:,0].reshape(-1, 1)
reg_simple.fit(x_simple_matrix, y)

print(reg_simple.predict(new_data_scaled[:,0].reshape(-1, 1)))
# We only feed the SAT score, because this regression was trained only on SAT!
# Their weights will be so close to 0 that they will barely influence the predictions
