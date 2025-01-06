import numpy as np

matrix_d = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
print(matrix_d)

print(type(matrix_d[0, 0])) # Single numerical value

print(matrix_d[0, 0])

print(type(matrix_d[0, 0:1])) # Only include the first element of the first column of the array

print(matrix_d[0, 0:1])# An array
# The type changes depending on our syntax

print(type(matrix_d[0:1, 0:1]))
print(matrix_d[0:1, 0:1])# 2-Dimensional array

print(matrix_d[0, 0].shape)# scalar
print(matrix_d[0, 0:1].shape)# vector
print(matrix_d[0:1, 0:1].shape)# matrix

# What difference does it make whether we're storing it as a scalar, vecto or matrix?
# Certain functions or methods can only be executed with inputs of a fixed size

# It's important to be consistent when working with arrays

# The Squeeze Method
# Removes all the unnecessary dimensions of an array

print(matrix_d[0:1, 0:1].squeeze())

# When we squeeze an array (holing a single value) along all its axes,
# we get a single numeric value

print(type(matrix_d[0:1, 0:1].squeeze()))

print(type(matrix_d[0:1, 0:1].squeeze().shape))

print(matrix_d[0:1, 0:1].squeeze().shape)

# Equivalent Function:
# variable_name.squeeze()
# =
# np.squeeze(variable_name)

print(np.squeeze(matrix_d[0:1, 0:1]))

print(matrix_d[0,0].squeeze().shape) # scalar
print(matrix_d[0, 0:1].squeeze().shape) # scalar
print(matrix_d[0:1, 0:1].squeeze().shape) # scalar

# In conclusion:
# As long as we apply the squeeze method or function
# we can use any slicing variation to get the same chunk of data
# [x, y]
# [x:x+1, y]
# [x, y:y+1]
# [x:x+1, y:y+1]

A = np.array([[12,3,4, 7], [23,31,-12,10], [24,9,18,15], [81,5,6,1], [-10,18,17,29]])
print(A[::2, 1::3])