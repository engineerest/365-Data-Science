import numpy as np

# Equivalent to np.empty, np.zeros, np.ones, np.full

# Don't need to specify a shape or type

# We need to provide another array (whose shape and type we take)

matrix_a = np.array([[1,0,9,2,2], [2, 23, 4, 5, 1], [0, 2, 3, 4, 1]])
print(matrix_a)

array_empty_like = np.empty_like(matrix_a)
print(array_empty_like)
# Remember, the empty function does not provide consistent output

array_0s_like = np.zeros_like(matrix_a)
print(array_0s_like)

# What is the application of zeros_like in analysis
# 1.) Starting point for a planner
# 2.) A "switch" where we change the values from 0 to 1 (and back)

# Really useful when working with dummy variables

# Why are _like functions useful?

# A second array where we store a value or each element of the original one
# Convenient when working with huge databases (faster loading times)