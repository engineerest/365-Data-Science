import numpy as np

# Stepwise Slicing
# Slicing, where we don't take consecutive values
# Values which are a certain distance apart

matrix_b = np.array([[1, 1, 1, 2, 0], [3, 6, 6, 7, 4], [4, 5, 3, 8, 0]])
print(matrix_b)

print(matrix_b[:, :]) # The entire dataset

# The default values for the start and end of the slice are the start and end of the array

print(matrix_b[::, ::])

# Stepwise Slicing Syntax
# matrix_b[1: 10: 3, 2: 11: 3]
# where 1 and 2 are start, 10 and 11 are end, 3 and 3 are step
# By default step = 1

print(matrix_b[::2, ::])

# We're slicing every other row

print(matrix_b[::, ::2])

# The "step" part of slicing works indentically for each dimension

# Every other value of every other row starting from the first
# We're interested in every "second" values of the rows
# ... for every "second" row

print(matrix_b[::2, ::2])

# The step argument can be positive or negative, but it can't be 0
# We would not be traversing rhe array at all
# Stuck at our starting position

# Going trough the array backwards

print(matrix_b[::-2, ::2])

# By default (for negative indices and steps), we're starting from the bottom of the matrix and moving up

print(matrix_b[-1::-1, ::2])

# We can use negative steps for the columns as well
# We'll leave it as a homework exercise
