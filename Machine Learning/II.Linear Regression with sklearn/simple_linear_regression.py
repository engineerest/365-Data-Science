# Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

# Load the data

data = pd.read_csv('1.01. Simple linear regression.csv')
print(data.head())

# Create the regression

# Declare the dependent and independent variables

# GPA[y] (dependent variable output) - target <= SAT[x] (independent variable input) - feature

x = data['SAT']
y = data['GPA']

# Out algorithm will find the optimal coefficients of a linear regression model

print(x.shape) # 1-dimensional
print(y.shape)

# Error: ValueError: Expected a 2-dimensional container but got <class 'pandas.core.series.Series'> instead.
# Pass a DataFrame containing a single row (i.e. single sample) or a single column (i.e. single feature) instead

# We must reshape X into a matrix (2D object)

x_matrix = x.values.reshape(-1, 1) # 2-dimensional
# In this way we are not changing anything but the dimensionality
print(x_matrix.shape)

# Regression itself

reg = LinearRegression()
# 'reg' is now an instance of the LinearRegression class

reg.fit(x_matrix, y) # fit(inputs, target)
# STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation (a type of normalization)
# NORMALIZATION: has different meaning depending on the case; here - we subtract the mean but divide by the L2-norm of the inputs
# copy_x - This is a safety net against normalization and other transformation
# fit_intercept - in statsmodels we had to manually add a constant
# 'n_jobs' - is a parameter used when we want to parallelize routines

# R-squared

# reg.score(x, y) returns the R-squared of a linear regression
print(reg.score(x_matrix, y))

# Coefficients

print(reg.coef_)
# When we get to the multiple regression lectures, this array will be filled with coefficients of each of the features

# Intercept

print(reg.intercept_)
# A simple linear regression always has a single intercept

# Making predictions

# reg.predict(new_inputs) returns the predictions of the linear regression model for some new inputs
# reg.predict(1740)

new_data = pd.DataFrame(data=[1740, 1760], columns=['SAT'])
print(new_data)

print(reg.predict(new_data))

new_data['Predicted_GPA'] = reg.predict(new_data)
print(new_data)

plt.scatter(x, y)
yhat = reg.coef_*x_matrix + reg.intercept_
# yhat = 0.0017*x + 0.275
fig = plt.plot(x, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()