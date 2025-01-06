import numpy as np

# Reshaping

lending_co_data_numeric = np.loadtxt('Lending-company-Numeric.csv', delimiter=',')

# We'll be mainly using the same 2 or 3 files

print(lending_co_data_numeric)


# Reshaping:
# Why is reshaping useful?

# Certain conditions about shapes and sizes need to be met
# Not always possible to store the outputs of a function as a part of existing array (or series)

# In NumPy, we'll be altering the shapes of arrays

# There are certain restrictions rto the shape we can give to an array,
# since we have a fixed amount of data available

print(lending_co_data_numeric.shape)

print(np.reshape(lending_co_data_numeric, (6, 1043)))
# Not a sideways flipped version of the original one

# Reshaped array
# First row: The first 1043 values of the flattened array
# Second row: The next 1043 values of the flattened array
# ...
# Last row: The last 1043 values of the flattened array

print(np.transpose(lending_co_data_numeric))

# print(np.reshape(lending_co_data_numeric, (3, 500))) error
print(np.reshape(lending_co_data_numeric, (3, 2086)))
# The total product of the sizes of all the dimensions must equal 6258

print(np.reshape(lending_co_data_numeric, (2, 3, 1043)))

print(np.reshape(lending_co_data_numeric, (1, 1, 2, 3, 1043)))

# Adding Dimensions
# Useful when a method or function only rakes inputs with a
# higher number of dimensions than the array we want to plug in

# Reshaping doesn't immediately alter the dataset

print(lending_co_data_numeric)

lending_co_data_numeric_2 = np.reshape(lending_co_data_numeric, (6, 1043))
print(lending_co_data_numeric_2)

print(lending_co_data_numeric.reshape(6, 1043))