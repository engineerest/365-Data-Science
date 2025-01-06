import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

# NAN-equivalent functions
# Functions that work arrays with missing values in them

# Many of the functions we examined in this section have NAN equivalents

# np.nanmean()
# The NAN equivalent of np.mean()

print(np.nanmean(matrix_a))

print(np.mean(matrix_a))

# Both the NAN an the regular version return indentical results when the dataset is complete

matrix_b = np.array([[1, 0, 0, 3, 1], [3, 6, np.nan, 2, 9], [4, 5, 3, 8, 0]])
# np.nan - Elements that are Not A Number
print(matrix_b)

print(np.nanmean(matrix_b))
# 6 > 3.4

print(np.mean(matrix_b))
# nan - Does not provide any numeric value when facing incomplete data

print(np.nanquantile(matrix_b, 0.7))

print(np.nanvar(matrix_b))

# NAN-equivalent functions are very useful when we have incomplete data
# They run while ignoring all NAN values in the data
# It would be in our best interest to find and fill any missing values,
# if we have the chance

# How programming in Python, and particulary NumPy,
# can help us put mathematics and statistics into practice
