import numpy as np

# Broadcasting

array_a = np.array([1, 2, 3])
print(array_a)

array_b = np.array([[1], [2]])
print(array_b)

matrix_c = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_c)

# Broadcasting

# We want to conduct elementwise operations but have elements of different sizes, and/or dimensions
# We can broadcast the smaller variable and create a broadcasted version with the size of the larger one

print(np.add(array_a, matrix_c))
# Their sizes are broadcastable
# [1, 2, 3] -> [[1, 2, 3], [1, 2, 3]]
# [[1, 2, 3], [1, 2, 3]] + [[1, 2, 3], [4, 5, 6]] = [[2, 4, 6], [5, 7, 9]]

print(np.add(array_b, matrix_c))
# [1 2] - > [[1, 1, 1,], [2, 2, 2]]
# [[1, 1, 1], [2, 2, 2]] + [[1, 2, 3], [4, 5, 6]] = [[2, 3, 4], [6, 7, 8]]

# Broadcasting can seem extremely complicated at first
# We're just matching arrays of different shps in order to use a given function

# The function compiles if the sizes of the two variables are broadcastable

# Broadcasting Rules:
# 1.The arrays have the same shape
# 2.The arrays have the same number of dimensions, and the length of each dimension is either common or 1
# 3.The arrays that have too few dimensions can have their shapes altered with a dimension 1, to satisfy the second rule

# 1-D vector of length 3 is now a 1x3 matrix 2-D

# Type Casting

# Taking every element of an array and changing it to a specified datatype

print(np.add(array_b, matrix_c, dtype=np.float64))

# Does not only change the results,
# but rather changes the inputs themselves

# print(np.add(array_b, matrix_c, dtype=np.str_)) error in course, but actually no
# 1.) Converts all numbers into strings
# 2.) Tries to add them up

# Casting is very widely used
# The preferred way to unify datatypes across a project

# Running over an Axis

# 1.) NumPy breaks down an ND-array into smaller arrays of (N-1)-many dimensions
# 2.) Applies the function to each one
# We can use this feature to run a function along each row or column

print(np.mean(matrix_c, axis=0))
print(matrix_c)

# axis:
# axis = 0: Finding the mean for each column of the array

# Useful when we have a large array, where each column is a different category

# axis = 1: Finding the mean for each row of the array

print(np.mean(matrix_c, axis=1))

