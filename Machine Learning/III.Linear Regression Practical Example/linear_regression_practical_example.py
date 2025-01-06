# Importing the relevant libraries

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()

# Loading the raw data

raw_data = pd.read_csv('1.04. Real-life example.csv')
print(raw_data.head())
# We would like to predict the price a used car depending on its specifications
# A BMW is generally more expensive than a Toyota
# The more a car is driven, the cheaper it should be
# Sports cars have larger engines than economy cars
# The rest are categorical variables which we will deal with on a case-by-case basis
# We haven't spoken about data cleaning so far...

# Preprocessing

# Exploring the descriptive statistics of the variable
print(raw_data.describe(include='all'))
# We only got descriptives for numerical variables (by default)
# With our current knowledge that would mean more than 300 dummies
# Almost all of the entries are 'Yes'... looks like this variable won't be useful
# A lot of the information from 'Model' could be engineered from 'Brand',
# 'Year', and 'EngineV' so we won't be losing too much variability

# Determining the variables of interest
data = raw_data.drop(['Model'], axis=1)
# DataFrame.drop(columns, axis) returns new object with the indicated columns dropped
print(data.describe(include='all'))

# Dealing with missing values

print(data.isnull().sum())
# Rule of thumb: if you are removing <5% of the observarions, you are free to just remove all that have MV
data_no_mv = data.dropna(axis=0)
print(data_no_mv.describe(include='all'))

# Exploring the PDFs

# sns.distplot(data_no_mv['Price']) old
sns.histplot(data_no_mv['Price'])
# Outliner = observations that lie on abnormal distance from other observations in the data
# One way to deal with outliers seemlessly is to remove top 1% of observations

# DataFrame.quantile(the quantile) returns the value at the given quantile (= np.percentile)

# Dealing with outliers

# I want to get the 99th percentile and keep the data below it
q = data_no_mv['Price'].quantile(0.99)
# The quantile is actually a value!
data_1 = data_no_mv[data_no_mv['Price']<q]
print(data_1.describe(include='all'))
sns.displot(data_1['Price'])
sns.displot(data_no_mv['Mileage'])

q = data_no_mv['Mileage'].quantile(0.99)
data_2 = data_no_mv[data_no_mv['Mileage']<q]

sns.displot(data_2['Mileage'])

sns.displot(data_no_mv['EngineV'])
# 99.99 - These are not usual values
# An interval where engine volume should normally fall is 0.6 to 6.5
# A common way to label missing values is by assigning 99.99
# It is a bad idea to label values in such ways as it is hard for other users of the data to distinguish them from true values

data_3 = data_2[data_2['EngineV']<6.5]
sns.displot(data_3['EngineV'])

sns.displot(data_no_mv['Year'])

q = data_3['Year'].quantile(0.01)
data_4 = data_3[data_3['Year']>q]

sns.displot(data_4['Year'])

data_cleaned = data_4.reset_index(drop=True)
# Currently the indices refer to all the data (including the observations we removed)
print(data_cleaned.describe(include='all'))
plt.show()

# Checking the OLS assumptions

# 'Price', 'Year', 'EngineV', and 'Mileage' are those that are likely to be more challenging and cause us more problems

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(15,3))
ax1.scatter(data_cleaned['Year'], data_cleaned['Price'])
ax1.set_title('Price and Year')
ax2.scatter(data_cleaned['EngineV'], data_cleaned['Price'])
ax2.set_title('Price and EngineV')
ax3.scatter(data_cleaned['Mileage'], data_cleaned['Price'])
ax3.set_title('Price and Mileage')

plt.show()

# We should first transform one or more variables

sns.displot(data_cleaned['Price'])

# Log transformations are especially useful when facing exponential relationship


# Relaxing the assumptions

log_price = np.log(data_cleaned['Price'])
# np.log(x) returns the natural logarithm of a number of array of numbers
data_cleaned['Price'] = log_price
print(data_cleaned)

f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(15,3))
ax1.scatter(data_cleaned['Year'], data_cleaned['Price'])
ax1.set_title('Log Price and Year')
ax2.scatter(data_cleaned['EngineV'], data_cleaned['Price'])
ax2.set_title('Log Price and EngineV')
ax3.scatter(data_cleaned['Mileage'], data_cleaned['Price'])
ax3.set_title('Log Price and Mileage')

data_cleaned = data_cleaned.drop(['Price'], axis=1)

plt.show()

# We already implemented a log transformation

# The observations that we have are not coming from time series data or panel data

# Multicollinearity

print(data_cleaned.columns.values)

# It is logical that 'Year' and 'Mileage' will be correlated
# sklearn does not have a dedicated method to check this assumption

# One of the best ways to check for multicollinearity is through VIF (variance inflation factor)

from statsmodels.stats.outliers_influence import variance_inflation_factor

variables = data_cleaned[['Mileage', 'Year', 'EngineV']]
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif['features'] = variables.columns
print(vif)

data_no_multicollinearity = data_cleaned.drop(['Year'], axis=1)

# Create dummy variables

# pd.get_dummies(df, [drop first]) spots all categorical variables and creates dummies automatically
data_with_dummies = pd.get_dummies(data_no_multicollinearity, drop_first=True)
print(data_with_dummies.head())

# Rearrange a bit

print(data_with_dummies.columns.values)

cols = data_with_dummies.columns.values
print(cols)

data_preprocessed = data_with_dummies[cols]
print(data_preprocessed.head())

# Linear regression model

# Declare the inputs and the targets
targets = data_preprocessed['log']
inputs = data_preprocessed.drop(['log_price'], axis=1)

# Scale the data

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(inputs)

inputs_scaled = scaler.transform(inputs)
# It is not usually recommended to standardize dummy variables
# Scaling has no effect on the predictive power of dummies, once scaled, though, they lose all their dummy meaning

# Train Test Split

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, targets, test_size=0.2, random_state=365)

# Create the regression

reg = LinearRegression()
reg.fit(x_train, y_train)

# In fact is a log-linear regression as the dependent variable is the log of 'Price'
# A simple way to check the final result is to plot the predicted values against the observed values

y_hat = reg.predict(x_train)
plt.scatter(y_train, y_hat)
plt.xlabel('Targets (y_train)', size=18)
plt.ylabel('Predictions (y_hat)', size=18)
plt.xlim(6, 13)
plt.ylim(6, 13)
plt.show()

# Residual = Differences between the targets and the predictions

sns.displot(y_train - y_hat)
plt.title("Residuals PDF", size=18)

# The residuals the estimates

# The are certain observations for which (y_train - y_hat) is much lower than the mean (a much higher price is predicted than is observed)

print(reg.score(x_train, y_train))

# Finding the weights and bias

print(reg.intercept_)
print(reg.coef_)

reg_summary = pd.DataFrame(inputs.columns.values, columns=['Features'])
reg_summary['Weights'] = reg.coef_
print(reg_summary)
# The model is far from interpretable

# Weights interpretation:
# I. Continuous variables:
# 1.A positive weight shows that as a feature increases in value, so do the log_price and 'Price' respectively
# 2.A negative weight shows that as a feature increases in value, log_price and 'Price' decrease

print(data_cleaned['Brand'].unique())

# II. Dummy variables:
# 1.A positive weight shows that the respective category (Brand) is more expensive than the benchmark(Audi)
# 2.A negative weight shows that the respective category (Brand) is less expensive than the benchmark(Audi)

# The bigger the weight, the bigger the impact

# Dummies are only compared to their respective benchmark

# Testing

y_hat_test = reg.predict(x_test)

plt.scatter(y_test, y_hat_test, alpha=0.2)
# plt.scatter(x,y [, alpha]) creates a scatter plot
# alpha: specifies the opacity

# The more saturated the color, the higher the concentration

plt.xlabel('Targets (y_test)', size=18)
plt.ylabel('Predictions (y_hat_test)', size=18)
plt.xlim(6, 13)
plt.ylim(6, 13)
plt.show()

# Our model is very good at predicting higher prices

# df_pf = pd.DataFrame(y_hat_test, columns=['Prediction'])
df_pf = pd.DataFrame(np.exp(y_hat_test), columns=['Prediction'])
# np.exp(x) returns the exponential of x (the Euler number 'e' to the power of x)
print(df_pf.head())

# exp(In(x)) = |x|
# (for a positive x)
# log(exp(x)) = x

# If we take exponentials of the log prices, we will reach the original prices

df_pf['Target'] = np.exp(y_test)
print(df_pf.head())

print(y_test)
# Pandas tried to match the indices
y_test = y_test.reset_index(drop=True)
print(y_test.head())

df_pf['Target'] = np.exp(y_test)
print(df_pf)

df_pf['Residual'] - df_pf['Target'] - df_pf['Prediction']
# Examining the residuals is the same as examining the heart of the algorithm
df_pf['Difference%'] = np.absolute(df_pf['Residual']/df_pf['Target']*100)
# Whether an observation is off by +1% or - 1% is mostly irrelevant
print(df_pf)

print(df_pf.describe())
# In that case the output was spot on!

pd.options.display.max_rows = 999
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(df_pf.sort_values(by=['Difference%']))

# The observed prices (targets) are extremely low
# On average our model is pretty decent at predicting the price
# Their predictions are higher than the targets
# It may be the model of the car, which we removed, or it may be that the car was damaged in some way

# How to improve our model
# 1.Use a different set of variables
# 2.Remove a bigger part of the outliers
# 3.Use different kinds of transformations

