# Import the relevant libraries

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load the data

raw_data = pd.read_csv('2.02. Binary predictors.csv')
print(raw_data)

data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes':1, 'No':0})
data['Gender'] = data['Gender'].map({'Male':1, 'Female':0})
print(data)

# Declare the dependent and the independent variables

y = data['Admitted']
x1 = data[['SAT', 'Gender']]

# Regression

x = sm.add_constant(x1)
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()
print(results_log.summary())

print(np.exp(2.0786))
# There was a strong relationship between SAT score and admittance

# Given the same SAT score, a female has 7 times higher odds to get admitted
# Int this particular university (degree) it is much easier for females to enter
# Universities place quotas... so:
# Communications -> predominantly
# STEM -> predominantly male
# Much easier for females to enter

# Always interpret the results considering the context

# We have a model that predicts values and we also have the actual values (data['Admitted'])

# Accuracy

# sm.LogitResults.predict() returns the values predicted by our model

np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
print(results_log.predict())# Predicted values by the model

print(np.array(data['Admitted']))# Actual values
# If 80% of the predicted values coincide with the actual values, we say the model has 80% accuracy

# sm.LogitResult.pred_table() returns a table which compares predicted and actual values
print(results_log.pred_table())

cm_df = pd.DataFrame(results_log.pred_table())
cm_df.columns = ['Predicted 0', 'Predicted 1']
cm_df = cm_df.rename(index={0: 'Actual 0', 1: 'Actual 1'})
print(cm_df) # Confusion matrix
# Confusion matrix - shows how confused our model is

# For 69 observations the model predicted 0 and the true value was 0
# } the model did its job well
# For 90 observations the model predicted 1 and the true value was 1

# For 4 observations the model predicted 0 while the true value was 1
# } the model 'got confused'
# For 5 observations the model predicted 1 and the true value was 0

# The most important metric we can calculate is 'accuracy'

# Overall the model made an accurate prediction in 159 out of 168 cases
# 159/168 = 0.946 = 94.6% accuracy

cm = np.array(cm_df)
accuracy_train = (cm[0, 0]+cm[1, 1]/cm.sum())
print(accuracy_train)

# Testing the model and assessing its accuracy

# Testing is done on a dataset the model has never seen before

test = pd.read_csv('2.03. Test dataset.csv')
print(test)

# 'test_data' and 'raw_data' were a part of the same file, but we secretly split it

# My split was 90-10, thus there are 19 observations for the test - Instructor

test['Admitted'] = test['Admitted'].map({'Yes':1, 'No':0})
test['Gender'] = test['Gender'].map({'Female':1, 'Male':0})
print(test)

# 1.We will use our model to make predictions based on the test data
# 2.We will compare those with the actual outcome
# 3.Calculate the accuracy
# 4.Create a confusion matrix

print(x)
# Order is very important, because the coefficients of the reg will expect

test_actual = test['Admitted']
test_data = test.drop(['Admitted'], axis=1)
test_data = sm.add_constant(test_data)
print(test_data)

# sm.LogtResults.pred_table() does not provide testing as a functionalty

def confusion_matrix(data, actual_values, model):
    pred_values = model.predict(data)
    bins = np.array([0, 0.5, 1])
    cm = np.histogram(actual_values, pred_values, bins=bins)[0]
    accuracy = (cm[0, 0]+cm[1, 1])/cm.sum()
    return cm, accuracy

cm = confusion_matrix(test_data, test_actual, results_log)
print(cm)

# The test accuracy is the figure we use when we refer to overall accuracy

# Almost always the training accuracy is higher that the test accuracy

# The opposite of accuracy is 'missclassification rate'

# Missclassification rate = # missclassified/ # all elements
print('Missclassification rate' + str((1+1)/19))