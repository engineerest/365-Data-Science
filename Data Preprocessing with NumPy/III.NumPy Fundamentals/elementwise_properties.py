import numpy as np

array_a = np.array([7, 8, 9])
print(array_a)

array_b = np.array([[1, 2, 3], [4, 5, 6]])
print(array_b)

print(array_b + 2)
print(array_b - 2)
print(array_b * 2)

list_a = [1, 2, 3]
print(list_a + [2])

print(array_a + 2)

# If you are used to working with lists, seeing operations work elementwise might fell counterintuitive

print(array_a + array_b[0])
print(array_a + array_b[1])

# We cna also conduct operations between arrays of different dimensions

# The shapes of the arrays need to be compatible

# The length of the 1-D array must match the "length" of the 2-D array

# When it comes to 2-D arrays, we use "length" to reffer to the sze of its elements (rows)

print(array_a + array_b)
print(array_a * array_b)
print(array_a - array_b)

# The order in which we write the arrays is important
