import numpy as np

matrix_a = np.array([[1, 0, 0, 3, 1], [3, 6, 6, 2, 9], [4, 5, 3, 8, 0]])
print(matrix_a)

#np.min()
# Finds the lowest value of an array along a given axis
print(np.min(matrix_a))

print(np.min(matrix_a[1]))

# np.amin()

# a -> array

# Specifically designed for working with arrays

print(np.amin(matrix_a))

# Two functions native to NumPy which serve the same purpose and work with ndarrays

# np.min() and np.amin() produce the same results

# np.min() and np.amin() are absolutely equivalent and interchangeable
# Using either one is a matter of personal preference

# np.minimun()

# Requires at least 2 input arrays
# Generates an array which holds the elementwise minimal values
# Compares the values ath the same position n each of the arrays before taking the lowest one
# The output has the same shape as the inputs

print(np.minimum(matrix_a[0], matrix_a[2]))

print(np.minimum(matrix_a[1], matrix_a[2]))

# minimal instead of minimum

# Latin:
# several minimum values
# minimum - singular
# minimal - plural
# adjective:
# minimal value
# noun:
# minimum

# If we reduce the inputs of a matrix, we can essentially pass all of its rows as inputs simultaneously

print(np.minimum.reduce(matrix_a))

print(np.min(matrix_a, axis=0))

# The two expressions are equivalent (result in the same output)

# np.min() calls np.minimum()

# np.min() provides greater flexibility

# min, amin and minimum have "maximum" equivalents: max, amax, maximum

print(np.max(matrix_a))

print(np.amax(matrix_a))

print(np.maximum.reduce(matrix_a))
