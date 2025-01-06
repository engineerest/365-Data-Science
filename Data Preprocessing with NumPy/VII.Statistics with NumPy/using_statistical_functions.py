import numpy as np

# 2-D Arrays are equivalent to matrices

# np.mean()
matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

print(np.mean(matrix_a))
# The mean value for the flattened array
# Ignoring the shape of the array and flattening it down to a long 1-dimensional array
# [1, 0, 0, 3, 1, 3, 6, 6, 2, 9, 4, 5, 3, 8, 0]
# 1 + 0 + 0 + 3 + 1 + 3 + 6 + 6 + 2 + 9 + 4 + 5 + 3 + 8 + 0 / 5

print(np.mean(matrix_a[0]))
# All individual elements of the matrix

# An integer is displayed as a decimal
# The default datatype (for the output of the np.mean function) is actually float 64

# 1 + 0 + 0 + 3 + 1 / 5 = 5/5 = 1

print(np.mean(matrix_a[:, 0]))
# 1 + 3 + 4 / 3 = 8/3 = 2.6(6)

print(np.mean(matrix_a, axis=0))
# Specifying an axis argument allows us to compute several means simutaneously

print(np.mean(matrix_a, axis=1))

# NumPy also contains many methods
# If the output are indentical then why do we prefer using the functions

print(np.sqrt(matrix_a))
# Finds the square root of every element within the array

# print(matrix_a.sqrt()) error

print(np.mean(matrix_a, axis=1, dtype=np.int64))
# "first" as in, axis with index 1, as opposed to the "zeroth" axis

import numpy as np


