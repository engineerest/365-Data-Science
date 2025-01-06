# Import the relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

sns.set()
# Load the data
data = pd.read_csv('1.01. Simple linear regression.csv')
print(data)

print(data.describe())

# Create your first regression

# Define the dependent and the independent variables

y = data['GPA']
x1 = data['SAT']

# Explore the data

plt.scatter(x1, y)
yhat = 0.275+0.0017*x1
# yhat = b0(coef const) + b1(coef SAT)*x1(our 'SAT')
# b0 and b1 these are the only two numbers we need to define the regression equation
# yhat = 0.275 + 0.0017x1
# GPA = 0.275 + 0.0017 * SAT
# 3.165 (GPA) = 0.275 + 0.0017 * 1700 (SAT)
# The expected GPA fot this student, according to our model

# Dep. Variable: GPA - Especially in the beginning it's good to double check if you coded the regression properly

# Model: OLS - OLS = Ordinary least squares

# R-squared = SSR(Variability explained by the regression)/SST(Total variability of the dataset)

# College GPA = 0.275+0.0017*SAT, R-squared=0.406

# Adjusted R-squared:
# 1. The R-squared measures how much of the total variability is explained by our model
# 2. Multiple regressions are always better than simple ones, as with each additional variable you add,
# the explanatory power may only increase or stay the same

# another data in columns
# std err - The standard error shows the accuracy of prediction
# t -

# P>|t| - p-value -

# H0:beta=0 Is the coefficient equal to zero

# A p-value < 0.05, meant that variable is significant

# p-value SAT - SAT is a significant variable when predicting college GPA

# F-test:
# H0:beta1=beta2=...=beta-k=0
# H1:at least one beta-i!=0
# If all betas are 0, then none of the Xs matter => out model has no merit

# That's the best fitting line, or the line which is closest to all observations simultaneously
fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.show()

# Regression itself

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
# fit() will apply a specific estimation technique (OLS in this case) to obtain the fit of the model
print(results.summary())

plt.scatter(x1, y)
yhat = 0.275+0.0017*0
fig2 = plt.plot(x1, yhat, lw=4, c='green', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.xlim(0)
plt.ylim(0)
plt.show()

plt.scatter(x1, y)
yhat = 0+0.0017*0
# if b1 = 0, then yhat = b0
fig3 = plt.plot(x1, yhat, lw=4, c='green', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.xlim(0)
plt.ylim(0)
plt.show()