# Preprocessing with NumPy

import numpy as np

# Checking for Missing Values

# np.loadtxt()
# Outputs an error message when we try to call a text file with missing values in it

lending_co_data_numeric = np.loadtxt('Lending-company-Numeric.csv', delimiter=',')

# It is a sign of good practice to make sure your data is of good quality

# np.isnan()

# Return array with the same shape and size as the one we input

# Every individual element of the original array is replaced with a Boolean (True/False)
# True -> Missing Value
# False -> No Missing Value

print(np.isnan(lending_co_data_numeric))
# False -> 0

# We can't be certain that the entire array contains only False values

# Boolean Values
# True -> 1
# False -> 0
# If we add up all the individual values (of the Boolean array),
# the sum should equal the total number of missing values in the original dataset

print(np.isnan(lending_co_data_numeric).sum())
# This dataset contains no missing values

# lending_co_data_numeric_NAN = np.loadtxt('Lending-company-Numeric-NAN.csv', delimiter=';') error
# N-aN -> Not a Number

lending_co_data_numeric_NAN = np.genfromtxt('Lending-company-Numeric-NAN.csv',
                                            delimiter=';',
                                            filling_values=0) # filled instead NAN value
# However, 0 could be used to numerically represent something meaningful in our dataset

print(np.isnan(lending_co_data_numeric_NAN))

print(np.isnan(lending_co_data_numeric_NAN).sum())

# Filling Missing Values
# Values that aren't part of our dataset
# We can later substitute all such values with something more appropriate
# Use a number greater that the highest value of the dataset
# np.nanmax()

temporary_fill = np.nanmax(lending_co_data_numeric_NAN).round(2) + 1
print(temporary_fill)

lending_co_data_numeric_NAN = np.genfromtxt('Lending-company-Numeric-NAN.csv',
                                            delimiter=';',
                                            filling_values=temporary_fill)


print(np.isnan(lending_co_data_numeric_NAN).sum())