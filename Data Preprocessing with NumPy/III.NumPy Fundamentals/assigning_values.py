import numpy as np

array_a = np.array([[1, 2, 3], [4, 5, 6]])
print(array_a)

array_a[0, 2] = 9
print(array_a)

# We can also change entire vectors within an array

array_a[0] = 9
print(array_a)

array_a[:, 0] = 9
print(array_a)

list_a = [8, 7, 8]

array_a[0] = list_a
print(array_a)

print(type(array_a[0]))

# Even if we set a specific part of an array equal to a scalar or list,
# the array simply takes the values, rather that the type

array_a[:] = 9
print(array_a)

array_a = 9
print(array_a)

print(type(array_a))

array_a = np.array([[1, 2, 3], [4, 5, 6]])
print(array_a)
