import numpy as np

matrix_c = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
print(matrix_c)

print(matrix_c[:, 0])

print(matrix_c[:, 0] > 2) # Array filled with True and False values

print(matrix_c[:, :] > 2)

# What if we wanted to know the exact values which satisfy the condition
# We need to write the conditional part as an index

print(matrix_c[matrix_c[:, :] > 2])# The output is a 1-D array

# Reasons why the output is a 1-D array:
# 1.) NumPy doesn't know how many of the elements would fit this condition
# 2.) Python takes the flattened array (which is 1-D) and applies the condition on it

# Several Conditions:
# >= greater than or equal to
# <= less than or equal to
# != NOT equal to
# == equal to
# % remainder after division
# % 2 == 0 is even

print(matrix_c[matrix_c[:, :] % 2 == 0])

# Multiple Conditions:
# & = "and"
# | = "or"

print(matrix_c[(matrix_c[:, :] % 2 == 0) & (matrix_c[:, :] <= 4)])
# Even numbers less than or equal to 4

#