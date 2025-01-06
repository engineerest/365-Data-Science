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
# Sample is the 'machine learning word' for observation

# Create the multiple linear regression

# Declare the dependent and independent variables

x = data[['SAT', 'Rand 1,2,3']]
y = data['GPA']

# Regression itself
reg = LinearRegression()
reg.fit(x, y)
# Notice that the cell executed without an error

print(reg.coef_)
# They are ordered in the way we fed them!

print(reg.intercept_)

# Calculating the R-squared

# The R-squared is a universal measure to evaluate how well linear regressions fare and compare

# reg.score(x, y) returns the R-squared of a linear regression
# regression -> 1.Simple, 2.Multiple

reg.score(x, y)

print(x.shape)
# The Adjusted R-squared steps on the R-squared and adjusts for the number of variables included in the model

# Formula for Adjusted R-squared
# R-squared adjusted = 1-(1-R-squared)*n-1/n-p-1

# n = 84 (the number of observations)
# p =2(the number of predictions)

r2 = reg.score(x, y)
n = x.shape[0]
p = x.shape[1]

adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
print(adjusted_r2)
# You can define your own Python functon which calculates adj. R-squared (x, y)
# Adj. R-squared < R-squared, therefore one or more of the predictors have little or no explanatory power

# Feature selection simplifies models, improves speed and prevents a series of unwanted issues arising from having too many features
# feature_selection.f_regression:
# F-regression creates linear regressions of each feature and the dependent variable
# 1.GPA <- SAT
# 2.GPA <- Rand 1,2,3

# Note that for a simple linear regression. the p-value of F-stat = the p-value of the only independent variable

# Feature selection

from sklearn.feature_selection import f_regression

print(f_regression(x, y))

p_values = f_regression(x, y)[1]
print(p_values)
print(p_values.round(3))

# Note: these are the univariate p-values reached from simple linear models.
# They do not reflect the interconnection of the features in our multiple linear regression

# Creating a summary table

reg_summary = pd.DataFrame(data=['SAT', 'Rand 1,2,3'], columns=['Features'])
print(reg_summary)

reg_summary['Coefficients'] = reg.coef_
reg_summary['p-values'] = p_values.round(3)

print(reg_summary)
# p-value = 0.676 - does not contribute to our model

# P-values are one of the best ways to determine if a variable is redundant but they provide no information whasoever about HOW USEFUL a variable is