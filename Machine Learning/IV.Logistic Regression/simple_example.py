# Basics of logistic regression

# Import the relevant libraries

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load the data

raw_data = pd.read_csv('2.01. Admittance.csv')
print(raw_data)
# Like dummies, we must convert Yes/No to 1s and 0s

data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes': 1, 'No': 0})
print(data)

# Variables

y = data['Admitted']
x1 = data['SAT']

# Let's plot the data

# Scatter plot

plt.scatter(x1, y, color='C0')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Admitted', fontsize=20)
plt.show()
# This is a pretty strange scatter plot, isn't it?

# Plot with a regression line

x = sm.add_constant(x1)
reg_lin = sm.OLS(y, x)
results_lin = reg_lin.fit()

plt.scatter(x1, y, color='C0')
y_hat = x1*results_lin.params[1]+results_lin.params[0]

plt.plot(x1, y_hat, color='C8')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Admitted', fontsize=20)
plt.show()
# This regression doesn't even know that our values are bounded between 0 and 1
# Linear regression is a great tehcnique but is simply not fit for this kind of analysis
# Our data is non-linear, thus, we must use non-linear approaches!

# Plot with a Logistic Regression

reg_log = sm.Logit(y, x)
results_log = reg_log.fit()

def f(x, b0, b1):
    return np.array(np.exp(b0+x*b1)/(1+np.exp(b0+x*b1)))

f_sorted = np.sort(f(x1, results_log.params[0], results_log.params[1]))
x_sorted = np.sort(np.array(x1))

plt.scatter(x1, y, color='C0')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('Admitted', fontsize=20)
plt.plot(x_sorted, f_sorted, color='C8')
plt.show()
# This function shows the probability of admission, given an SAT score
# When the SAT score is relatively LOW, the Prob of getting admitted is 0
# A score between 1600 and 1750 is uncertain

# LOGISTIC MODEL
# The logistic regression predicts the probability of an event
# INPUT -> PROBABILITY

# Linear regression model:
# y = beta0 + beta1*x1 + ... + beta_k*x_k + e
# Logistic regression model:
# p(X) = e^(beta0 + beta1*x1+...+ beta_k*x_k)/1 + e^(beta0 + beta1*x1+...+ beta_k*x_k)
# Logit regression model:
# p(X)/1 - p(X) = e^(beta0 + beta1*x1+...+ beta_k*x_k)
# log(p(X)/1 - p(X)) = log(e^(beta0 + beta1*x1+...+ beta_k*x_k))
# log(p(X)/1 - p(X)) = beta0 + beta1*x1 + ... + beta_k*x_k
# log(odds) = beta0 + beta1*x1 + ... + beta_k*x_k