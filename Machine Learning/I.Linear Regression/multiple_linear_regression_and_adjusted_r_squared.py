# Import the relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Load the data
data = pd.read_csv('1.02. Multiple linear regression.csv')
print(data)
print(data.describe())

# Crate your first multiple regression

y = data['GPA']
x1 = data[['SAT', 'Rand 1,2,3']]

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()

# GPA = b0 + b1*SAT + b2*Rand1,2,3

print(results.summary())

# H0:в=0 - p-value of Rand 1,2,3 is 0.762
# We cannot reject the null hypothesis at 76% level!
# We want a p-value < 0.05!

# The variable 'Rand 1,2,3' not only worsens the explanatory power, but is also insignificant

# yhat1 = 0.275 + 0.0017*x1 -> yhat2 = 0.296 + 0.0017*x1 - 0.0083*x2(because coef Rand... is negative)
# The bias of this variable is reflected into the coefficients of the others
# We can add 100 variables to a model, but this strategy makes regression analysis futile