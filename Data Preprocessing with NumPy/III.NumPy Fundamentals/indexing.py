import numpy as np

# Indexing

array_a = np.array([[1, 2, 3], [4, 5, 6]])
print(array_a)

# Indices (or indexes):
# We use indices to refer to the individual elements within an array
# Coordinates that help us navigate through the array
# Integers array_a[0]

# 1st position = index 0
# 2nd position = index 1

# Python uses 0 indexing

# Specific Values

print(array_a[0])

# When working with arrays of 2 dimensions (like array_a)
# rows: separate numeric values
# elements: individual elements

print(array_a[1])

#print(array_a[2]) error
# index 2 = 3rd element (row)

# We need to provide an index for each dimension of the variable
# array_a is 2-D
#   0 1 2
# [[1 2 3] 0
#  [4 5 6]] 1

# array[row, element]
print(array_a[1][0])# specific
print(array_a[0][1])# specific

print(array_a[1, 0])# specific

# Go through all the rows from this column
# slicing

print(array_a[:, 0])# interval index

# Negative indices

# Traversing the array backward

array_b = np.array([1, 2, 3])
print(array_b[-1])

# if [1] = 2nd element, why doesn't [-1] = second-last element?
# -0  =0
# Negative indices start from -1

print(array_a)
print(array_a[-1])

print(array_a[:, -1])

print(array_a[-1, -1])

#print(array_a[-3]) error
# Negative indices are just as viable as their positive counterparts

