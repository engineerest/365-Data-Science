import numpy as np

list_a = [1, 2, 3, 4, 5, 6]
print(len(list_a))

list_a = [[1, 2, 3], [4, 5, 6]]
print(len(list_a))

# Even though the syntax resembles arrays, Python recognizes lists as a separate datatype

array_a = np.array(list_a)

print(type(array_a))

print(list_a)
print(array_a)

print(array_a.shape)
# print(list_a.shape) error
# Lists don't have shapes
# Lists have length
print(len(list_a)) # How many smaller lists a re a part of the bigger list
# How many sublists/inner lists are contained in the nested list called "list_a"
print(len(list_a[0]))
print(len(list_a[1]))

# Array operations work elementwise

list_b = list_a[0] + list_a[1]
array_b = array_a[0] + array_a[1]

print(list_b)
print(array_b)

# Arrays compute the element of one array to its corresponding element in a different array

# ndarrays have the added benefit of using built-in functions and methods

import math
# array_e = math.sqrt(list_a)
# array_e = math.sqrt(list_a[1, 0]) error
array_e = math.sqrt(array_a[1, 0])
print(array_e)

print(np.sqrt(array_a))
# Elementwise functionality is a great advantage arrays have over lists when it comes to computations