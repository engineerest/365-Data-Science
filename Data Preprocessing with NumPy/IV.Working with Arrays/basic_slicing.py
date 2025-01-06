import numpy as np

matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_a)

# Basic Slicing

# Creating a new array by taking chunks of values out of an existing one
# The slices consist of adjacent pieces of data

# Slice:
# It can contain entire rows and columns of the original array, or just parts of them

print(matrix_a[:])

# ":" expresses an interval of values

# Starting from the row before the colon

# example_variable[1:13]

# Ending right before the row after the colon

# if we don't specify anything, we take the entire NDarray

print(matrix_a[0:0])
# In Python's eyes this is a 0-D array

# No rows between the first one and itself

print(matrix_a[0:1])
# Everything in the interval between the first two rows

# Indexing in NumPy is closed-open ( [0:1) )

# We don't include the upper limit

# We don't get an error message if we go out of bounds when indexing


print(matrix_a[:, :]) # first : is rows, second : is columns
# Going through all the columns of matrix A

# matrix_a[:, :] = matrix_a[:]

# We can omit to specify a slice for the second dimension if we're using all the columns

print(type(matrix_a[:, :]))

print(matrix_a[:1])

print(matrix_a[1:])

print(matrix_a[2:])

# Since there are only two ros, it returns an empty array

print(matrix_a[:2])

# matrix_a[n:] and matrix_a[:n] complementary slices

# matrix_a[2:] = []
# matrix_a[:2] = entire matrix

# Indexing is very similar to slicing
# indexing = specific indexing
# slicing = interval indexing

print(matrix_a[0])# 1-D slice

print(matrix_a[:1])# 2-D slice

print(matrix_a[1:])

print(matrix_a[1])

# THe numerical values are indentical but the outputs vary in dimensions

print(matrix_a[:-1])

print(matrix_a[:, 1:])
# All the rows
# The columns starting from the one with index 1

print(matrix_a)

print(matrix_a[1:, 1:])