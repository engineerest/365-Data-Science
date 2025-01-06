# Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Apply a fix to the statsmodels library
# from scipy import stats
# stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)
# They won't bother until next release (or at all)
# 1.Open-source projects like Python and its libraries are not immaculate
# 2.Workarounds are out there, waiting for you to find them!
# Load the data

raw_data = pd.read_csv('2.01. Admittance.csv')

data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes': 1, 'No': 0})
print(data)

# Declare the dependent and the independent variables

y = data['Admitted']
x1 = data['SAT']

# Regression
x = sm.add_constant(x1)
# This time I'll create the regression in two steps - Instructor
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()
# SM uses a machine learning algorithm to fit the regression
# Value of the 'objective function' at the 10th iteration
# There is always the possibility the model won't learn the relationship

# Summary

print(results_log.summary())

x0 = np.ones(168)
reg_log = sm.Logit(y, x0)
results_log = reg_log.fit()
print(results_log.summary())
# You may want to compare the log-likehood of your model with the LL-nul,
# to see if your model has any explanatory power