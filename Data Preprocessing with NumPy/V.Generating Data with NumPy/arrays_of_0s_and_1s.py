import numpy as np

# Creates an "empty" N-D array
# Return an array without initializing entries
# Fastest way to generate an N-D array

# np.empty()

array_empty = np.empty(shape=(2, 3))
print(array_empty)
# It's possible to get some random numbers instead

# An array is assigned memory from our RAM

# Example of allocating unused memory vs used memory:
# [0][0][0][0][0][0]
#[199][0][0][1][-24][0]

# np.zeros

array_0s = np.zeros(shape=(2, 3))
print(array_0s)

# Creates an array full of 0s
# np.zeros vs np.empty
# np.zeros has consistent output

array_0s = np.zeros(shape=(2, 3), dtype=np.int8)
print(array_0s)

# np.ones

# The "1" equivalent to np.zeros
# Generates an arrays of 1s

array_1s = np.ones(shape=(2, 3))
print(array_1s)

# np.full()

# Generates an array filled entirely with a specified value

# Contains an additional mandatory argument: fill_value

# fill_value takes scalar values

# array_full = np.full(shape=(2, 3)) error
array_full = np.full(shape=(2, 3), fill_value=2)
print(array_full)

array_full = np.full(shape=(2, 3), fill_value="Three-Six-Five")
print(array_full)