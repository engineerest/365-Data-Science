import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

raw_data = pd.read_csv('1.03. Dummies.csv')
print(raw_data)

data = raw_data.copy()

data['Attendance'] = data['Attendance'].map({'Yes': 1, 'No': 0})
print(data)
print(data.describe())

# Regression

y = data['GPA']
x1 = data[['SAT', 'Attendance']]

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
print(results.summary())

plt.scatter(data['SAT'], y)
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665 + 0.0014*data['SAT']
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837')
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Attendance', fontsize=20)
plt.show()

plt.scatter(data['SAT'], y, c=data['Attendance'], cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665 + 0.0014*data['SAT']
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837')
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Attendance', fontsize=20)
plt.show()

plt.scatter(data['SAT'], y, c=data['Attendance'], cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665 + 0.0014*data['SAT']
yhat = 0.0017*data['SAT'] + 0.275
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837', label='regression line1')
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026', label='regression line2')
fig = plt.plot(data['SAT'], yhat, lw=3, c='#4C72B0', label='regression line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Attendance', fontsize=20)
plt.show()

# How to make predictions based on the regressions we create

print(x)

new_data = pd.DataFrame({'const': 1, 'SAT':[1700, 1670], 'Attendance':[0, 1]})
new_data = new_data[['const', 'SAT', 'Attendance']]
print(new_data)

new_data.rename(index={0:'Bob', 1:'Alice'})

predictions = results.predict(new_data)

predictionsdf = pd.DataFrame({'Predictions': predictions})
joined = new_data.join(predictionsdf)
joined.rename(index={0: 'Bob', 1: 'Alice'})